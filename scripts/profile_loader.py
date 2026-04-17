"""
profile_loader.py - 用户兴趣画像加载与评分引擎

设计原则：
  - priority 是乘数（multiplier），不是加分项
  - 最终评分 = base_score × (domain_priority / max_priority)
  - 支持 profile.yaml v1（旧格式）和 v2（新格式）兼容加载
  - 可作为独立模块被 search_papers.py / cluster_topics.py 等脚本 import

用法：
    from scripts.profile_loader import ProfileLoader

    loader = ProfileLoader("profile.yaml")
    score, domain, keywords = loader.score_relevance(title, abstract, categories)
    final = loader.compute_final_score(score, recency, popularity, quality, domain)
    should_deep = loader.should_trigger_deep_analysis(final, domain)
"""

from __future__ import annotations

import os
import logging
from dataclasses import dataclass, field
from typing import Any

import yaml

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# 数据结构
# ---------------------------------------------------------------------------

@dataclass
class DomainConfig:
    name: str
    keywords: list[str] = field(default_factory=list)
    arxiv_categories: list[str] = field(default_factory=list)
    priority: float = 1.0          # 乘数权重，越高越优先
    deep_analysis: bool = False     # 命中时是否触发 paper-analyze


@dataclass
class BusinessFocus:
    sectors: list[str] = field(default_factory=list)
    noise_filter_prompt: str = ""
    tracked_companies: dict[str, list[str]] = field(default_factory=dict)
    # tier -> score boost
    tier_boosts: dict[str, float] = field(default_factory=lambda: {
        "tier1": 3.0, "tier2": 2.0, "tier3": 1.0
    })


@dataclass
class FormatPreference:
    academic_top_n: int = 8
    community_top_n: int = 10
    finance_top_n: int = 8
    finance_min_score: float = 3.0
    trigger_deep_analysis_threshold: float = 4.5
    topic_dedup: bool = True
    summary_style: str = "tier2"
    language: str = "zh"


@dataclass
class RelevanceResult:
    """单次相关性匹配的结果"""
    base_score: float               # 原始加权分（关键词 + 类别）
    domain: str | None              # 命中的领域名称
    matched_keywords: list[str]     # 命中的关键词列表
    priority_multiplier: float      # 领域优先级乘数（已归一化）
    weighted_score: float           # 最终加权分 = base_score × multiplier


# ---------------------------------------------------------------------------
# ProfileLoader
# ---------------------------------------------------------------------------

class ProfileLoader:
    """
    从 profile.yaml 加载用户画像，提供评分与过滤接口。

    兼容两种格式：
      v2: 顶层 key = user_profile（新格式）或直接 research_domains（v1 旧格式）
    """

    # 相关性评分常量（与 search_papers.py 保持一致）
    TITLE_KW_BOOST = 0.5      # 标题关键词命中
    SUMMARY_KW_BOOST = 0.3    # 摘要关键词命中
    CATEGORY_BOOST = 1.0      # arXiv 类别命中
    SCORE_MAX = 10.0           # 各维度满分

    # 综合评分权重（普通论文 / 高影响力论文）
    WEIGHTS_NORMAL = {"relevance": 0.40, "recency": 0.20, "popularity": 0.20, "quality": 0.20}
    WEIGHTS_HOT    = {"relevance": 0.35, "recency": 0.10, "popularity": 0.40, "quality": 0.15}

    def __init__(self, config_path: str):
        self.config_path = os.path.expanduser(config_path)
        self._raw: dict[str, Any] = {}
        self.domains: dict[str, DomainConfig] = {}
        self.business: BusinessFocus = BusinessFocus()
        self.format: FormatPreference = FormatPreference()
        self.excluded_keywords: list[str] = []
        self.system: dict[str, Any] = {}
        self._max_priority: float = 1.0

        self._load()

    # ------------------------------------------------------------------
    # 加载
    # ------------------------------------------------------------------

    def _load(self) -> None:
        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                self._raw = yaml.safe_load(f) or {}
        except FileNotFoundError:
            logger.warning("Profile not found at %s, using defaults", self.config_path)
            self._raw = {}
        except Exception as e:
            logger.error("Failed to load profile: %s", e)
            self._raw = {}

        # 支持 v2（user_profile 包裹）和 v1（直接 research_domains）
        root = self._raw.get("user_profile", self._raw)

        self._parse_domains(root.get("research_domains", {}))
        self._parse_business(root.get("business_focus", {}))
        self._parse_format(root.get("format_preference", {}))
        self.excluded_keywords = [
            kw.lower()
            for kw in self._raw.get("excluded_keywords", [])
        ]
        self.system = self._raw.get("system", {})

    def _parse_domains(self, raw: dict) -> None:
        for name, cfg in raw.items():
            if not isinstance(cfg, dict):
                continue
            self.domains[name] = DomainConfig(
                name=name,
                keywords=[str(k) for k in cfg.get("keywords", [])],
                arxiv_categories=cfg.get("arxiv_categories", []),
                priority=float(cfg.get("priority", 1.0)),
                deep_analysis=bool(cfg.get("deep_analysis", False)),
            )
        if self.domains:
            self._max_priority = max(d.priority for d in self.domains.values())

    def _parse_business(self, raw: dict) -> None:
        self.business = BusinessFocus(
            sectors=raw.get("sectors", []),
            noise_filter_prompt=raw.get("noise_filter_prompt", ""),
            tracked_companies=raw.get("tracked_companies", {}),
        )

    def _parse_format(self, raw: dict) -> None:
        self.format = FormatPreference(
            academic_top_n=raw.get("academic_top_n", 8),
            community_top_n=raw.get("community_top_n", 10),
            finance_top_n=raw.get("finance_top_n", 8),
            finance_min_score=raw.get("finance_min_score", 3.0),
            trigger_deep_analysis_threshold=raw.get("trigger_deep_analysis_threshold", 4.5),
            topic_dedup=raw.get("topic_dedup", True),
            summary_style=raw.get("summary_style", "tier2"),
            language=raw.get("language", "zh"),
        )

    # ------------------------------------------------------------------
    # 核心接口 1：学术相关性评分（修复 priority 忽略 Bug）
    # ------------------------------------------------------------------

    def score_relevance(
        self,
        title: str,
        abstract: str,
        arxiv_categories: list[str] | None = None,
    ) -> RelevanceResult:
        """
        计算论文与用户兴趣的相关性，并乘以领域优先级乘数。

        Args:
            title:            论文标题
            abstract:         论文摘要
            arxiv_categories: 论文的 arXiv 分类列表

        Returns:
            RelevanceResult（包含 base_score、domain、weighted_score 等）
        """
        title_lower = title.lower()
        abstract_lower = abstract.lower()
        cats = arxiv_categories or []

        # 排除检查（全局 excluded_keywords）
        for ex_kw in self.excluded_keywords:
            if ex_kw in title_lower or ex_kw in abstract_lower:
                return RelevanceResult(
                    base_score=0.0, domain=None, matched_keywords=[],
                    priority_multiplier=0.0, weighted_score=0.0
                )

        best: RelevanceResult | None = None

        for domain_cfg in self.domains.values():
            base, matched = self._score_one_domain(
                domain_cfg, title_lower, abstract_lower, cats
            )
            if base == 0:
                continue

            # priority 归一化为乘数：最高 priority 对应乘数=1，其余按比例缩放
            multiplier = domain_cfg.priority / self._max_priority
            weighted = base * multiplier

            if best is None or weighted > best.weighted_score:
                best = RelevanceResult(
                    base_score=base,
                    domain=domain_cfg.name,
                    matched_keywords=matched,
                    priority_multiplier=multiplier,
                    weighted_score=weighted,
                )

        if best is None:
            return RelevanceResult(
                base_score=0.0, domain=None, matched_keywords=[],
                priority_multiplier=0.0, weighted_score=0.0
            )
        return best

    def _score_one_domain(
        self,
        cfg: DomainConfig,
        title_lower: str,
        abstract_lower: str,
        cats: list[str],
    ) -> tuple[float, list[str]]:
        """针对单个领域计算原始 base_score（不含 priority 乘数）"""
        score = 0.0
        matched: list[str] = []

        for kw in cfg.keywords:
            kw_lower = kw.lower()
            if kw_lower in title_lower:
                score += self.TITLE_KW_BOOST
                matched.append(kw)
            elif kw_lower in abstract_lower:
                score += self.SUMMARY_KW_BOOST
                matched.append(kw)

        for cat in cfg.arxiv_categories:
            if cat in cats:
                score += self.CATEGORY_BOOST
                matched.append(cat)

        return score, matched

    # ------------------------------------------------------------------
    # 核心接口 2：综合推荐评分（含 priority 乘数）
    # ------------------------------------------------------------------

    def compute_final_score(
        self,
        relevance_result: RelevanceResult,
        recency_score: float,
        popularity_score: float,
        quality_score: float,
        is_hot_paper: bool = False,
    ) -> float:
        """
        综合四维评分，并把 priority 乘数融入 relevance 维度。

        最终评分 = weighted_sum(relevance×priority, recency, popularity, quality)
        所有维度先归一化到 0-10，再按权重加权。

        Args:
            relevance_result: score_relevance() 的返回值
            recency_score:    0~SCORE_MAX
            popularity_score: 0~SCORE_MAX
            quality_score:    0~SCORE_MAX
            is_hot_paper:     是否来自 Semantic Scholar 高影响力批次

        Returns:
            综合评分 0-10（保留两位小数）
        """
        weights = self.WEIGHTS_HOT if is_hot_paper else self.WEIGHTS_NORMAL

        # relevance 已经含 priority 乘数（weighted_score），归一化到 0-10
        rel_norm     = (relevance_result.weighted_score / self.SCORE_MAX) * 10
        recency_norm = (recency_score / self.SCORE_MAX) * 10
        pop_norm     = (popularity_score / self.SCORE_MAX) * 10
        qual_norm    = (quality_score / self.SCORE_MAX) * 10

        final = (
            rel_norm     * weights["relevance"]
            + recency_norm * weights["recency"]
            + pop_norm     * weights["popularity"]
            + qual_norm    * weights["quality"]
        )
        return round(final, 2)

    # ------------------------------------------------------------------
    # 核心接口 3：是否触发深度分析
    # ------------------------------------------------------------------

    def should_trigger_deep_analysis(
        self,
        final_score: float,
        domain: str | None,
    ) -> bool:
        """
        返回是否自动触发 paper-analyze。
        条件：final_score >= threshold 且 domain 配置了 deep_analysis=True
        """
        if final_score < self.format.trigger_deep_analysis_threshold:
            return False
        if domain is None:
            return False
        cfg = self.domains.get(domain)
        return bool(cfg and cfg.deep_analysis)

    # ------------------------------------------------------------------
    # 核心接口 4：财经条目加权
    # ------------------------------------------------------------------

    def score_finance_item(self, title: str, content: str = "") -> float:
        """
        根据 business_focus.tracked_companies 为财经条目计算附加分。
        返回附加分（0 ~ 3.0），由外部叠加到基础评分上。
        """
        text = (title + " " + content).lower()
        boost = 0.0

        tier_boosts = {"tier1": 3.0, "tier2": 2.0, "tier3": 1.0}
        for tier, companies in self.business.tracked_companies.items():
            tier_boost = tier_boosts.get(tier, 1.0)
            for company in companies:
                if company.lower() in text:
                    boost = max(boost, tier_boost)
                    break  # 每 tier 最多加一次

        return boost

    # ------------------------------------------------------------------
    # 工具方法
    # ------------------------------------------------------------------

    def get_all_arxiv_categories(self) -> list[str]:
        """获取所有领域配置的 arXiv 分类（去重）"""
        cats: set[str] = set()
        for d in self.domains.values():
            cats.update(d.arxiv_categories)
        return sorted(cats)

    def get_domains_by_priority(self, min_priority: float = 0.0) -> list[DomainConfig]:
        """按优先级降序返回领域列表"""
        return sorted(
            [d for d in self.domains.values() if d.priority >= min_priority],
            key=lambda d: d.priority,
            reverse=True,
        )

    def summary(self) -> str:
        """打印画像摘要（调试用）"""
        lines = [
            f"ProfileLoader v2 — {len(self.domains)} domains loaded",
            f"  Max priority: {self._max_priority}",
        ]
        for d in self.get_domains_by_priority():
            lines.append(
                f"  [{d.priority:.1f}] {d.name} ({len(d.keywords)} kws, "
                f"{len(d.arxiv_categories)} cats, deep={d.deep_analysis})"
            )
        lines += [
            f"  Excluded keywords: {len(self.excluded_keywords)}",
            f"  Deep analysis threshold: {self.format.trigger_deep_analysis_threshold}",
            f"  Tracked companies: "
            + ", ".join(f"{t}:{len(c)}" for t, c in self.business.tracked_companies.items()),
        ]
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI 入口（验证用）
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else "profile.yaml"
    loader = ProfileLoader(path)
    print(loader.summary())

    # 快速测试
    test_cases = [
        (
            "GRPO: Group Relative Policy Optimization for LLM Alignment",
            "We propose GRPO, a novel RLHF algorithm based on PPO with group-level reward normalization. "
            "Achieves state-of-the-art results on mathematical reasoning benchmarks.",
            ["cs.AI", "cs.LG"],
        ),
        (
            "Pathology Image Segmentation with Diffusion Models",
            "We present a novel approach for medical image segmentation using diffusion models, "
            "achieving superior performance on histological pathology datasets.",
            ["cs.CV"],
        ),
        (
            "vLLM: Efficient Memory Management for LLM Serving with PagedAttention",
            "We present PagedAttention, a new attention algorithm that manages key-value cache in pages, "
            "enabling vLLM to achieve near-zero waste in KV cache memory.",
            ["cs.LG", "cs.AR"],
        ),
    ]

    print("\n--- Relevance Test ---")
    for title, abstract, cats in test_cases:
        result = loader.score_relevance(title, abstract, cats)
        final = loader.compute_final_score(result, recency_score=3.0, popularity_score=1.5, quality_score=2.0)
        deep = loader.should_trigger_deep_analysis(final, result.domain)
        print(
            f"\n  Title : {title[:60]}"
            f"\n  Domain: {result.domain} (priority_mul={result.priority_multiplier:.2f})"
            f"\n  Base  : {result.base_score:.2f}  Weighted: {result.weighted_score:.2f}"
            f"\n  Final : {final}  DeepAnalysis: {deep}"
        )
