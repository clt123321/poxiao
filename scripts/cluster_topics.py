"""
cluster_topics.py - 社区内容话题聚类与降噪

功能：
  1. 读取 fetch.py 产出的 fetched.json（来自 HN/Reddit/RSS/GitHub）
  2. 用 TF-IDF + 关键词重叠 做轻量文本相似度聚类，识别同一事件的多条帖子
  3. 每个 Topic 合并为一个结构化对象，输出：
     - topic_title:  代表性标题
     - sources:      聚合的所有来源链接
     - item_count:   合并的帖子数量
     - top_signal:   最高信号值（upvote/score）
     - raw_texts:    各帖子原始摘要（供下游 LLM 生成 consensus/debate）
  4. 对聚类结果按 signal×item_count 加权排序（hot topic 靠前）
  5. 可选：输出 Claude 可直接调用的 prompt，用于生成"核心共识 vs 主要争议"

输出格式（clustered.json）：
  {
    "topics": [
      {
        "topic_id": 0,
        "topic_title": "Qwen3.6 Released by Alibaba",
        "item_count": 5,
        "top_signal": 1243,
        "sources": [{"title": "...", "url": "...", "feed": "...", "signal": 1243}],
        "raw_texts": ["...", "..."],
        "consensus_prompt": "..."   // 若 --with-prompts 则输出
      }
    ],
    "unclustered": [...],    // 孤立帖子（未被聚类）
    "stats": {...}
  }

用法：
    python scripts/cluster_topics.py \\
        --input data/2026-04-17/fetched.json \\
        --output data/2026-04-17/clustered.json \\
        --profile profile.yaml \\
        --category community \\
        --with-prompts
"""

from __future__ import annotations

import json
import re
import os
import sys
import math
import logging
import argparse
from collections import defaultdict
from typing import Any

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")


# ---------------------------------------------------------------------------
# 文本工具
# ---------------------------------------------------------------------------

# 停用词（英文+中文高频词）
STOP_WORDS = {
    # 英文
    "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
    "of", "with", "is", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "do", "does", "did", "will", "would", "could",
    "should", "may", "might", "this", "that", "these", "those", "it",
    "its", "we", "they", "he", "she", "you", "i", "my", "our", "their",
    "new", "how", "why", "what", "when", "who", "use", "using", "used",
    "from", "by", "as", "if", "so", "then", "just", "about", "up", "out",
    # 中文高频词
    "的", "了", "是", "在", "和", "有", "也", "不", "这", "我",
    "他", "她", "它", "们", "个", "以", "为", "上", "下", "到",
    "对", "说", "从", "于", "被", "让", "着", "过", "与", "及",
}


def tokenize(text: str) -> list[str]:
    """简单 tokenizer：英文小写分词 + 中文字符 2-gram"""
    tokens: list[str] = []
    # 英文 token
    en_tokens = re.findall(r"[a-zA-Z][a-zA-Z0-9+#\-\.]*", text.lower())
    tokens.extend(t for t in en_tokens if len(t) >= 2 and t not in STOP_WORDS)
    # 中文 unigram（保留有意义单字也丢掉，改用 bigram）
    zh_chars = re.findall(r"[\u4e00-\u9fff]+", text)
    for seg in zh_chars:
        # 滑动 bigram
        for i in range(len(seg) - 1):
            bigram = seg[i: i + 2]
            if bigram not in STOP_WORDS:
                tokens.append(bigram)
    return tokens


def build_tfidf(docs: list[list[str]]) -> list[dict[str, float]]:
    """
    计算 TF-IDF 向量（简化版，不依赖 scikit-learn）。
    返回每篇文档的 {term: tfidf_score} 字典列表。
    """
    n = len(docs)
    if n == 0:
        return []

    # 计算 DF
    df: dict[str, int] = defaultdict(int)
    for tokens in docs:
        for term in set(tokens):
            df[term] += 1

    # 计算 TF-IDF
    vectors: list[dict[str, float]] = []
    for tokens in docs:
        tf: dict[str, int] = defaultdict(int)
        for t in tokens:
            tf[t] += 1
        total = max(len(tokens), 1)
        vec: dict[str, float] = {}
        for term, count in tf.items():
            tfidf = (count / total) * math.log((n + 1) / (df[term] + 1))
            vec[term] = tfidf
        vectors.append(vec)

    return vectors


def cosine_similarity(v1: dict[str, float], v2: dict[str, float]) -> float:
    """计算两个 TF-IDF 向量的余弦相似度"""
    common = set(v1) & set(v2)
    if not common:
        return 0.0
    dot = sum(v1[t] * v2[t] for t in common)
    norm1 = math.sqrt(sum(x * x for x in v1.values()))
    norm2 = math.sqrt(sum(x * x for x in v2.values()))
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return dot / (norm1 * norm2)


# ---------------------------------------------------------------------------
# 聚类核心
# ---------------------------------------------------------------------------

class TopicClusterer:
    """
    基于 TF-IDF + 余弦相似度的简单贪心聚类器。

    算法：
      1. 按 signal（upvotes/score）降序处理帖子
      2. 对每篇帖子，找相似度最高的已有 Topic（>= threshold）
      3. 若找到则合并；否则创建新 Topic
      - 时间复杂度 O(n²)，适用于 n < 500 的日常批量
    """

    def __init__(
        self,
        similarity_threshold: float = 0.25,
        min_signal: int = 0,
    ):
        self.threshold = similarity_threshold
        self.min_signal = min_signal
        self.topics: list[dict[str, Any]] = []
        self._topic_vectors: list[dict[str, float]] = []

    def _item_text(self, item: dict) -> str:
        title = item.get("title", "")
        content = item.get("content", "")[:300]
        return title + " " + content

    def fit(self, items: list[dict]) -> "TopicClusterer":
        """执行聚类"""
        # 按 signal 降序（确保高热帖成为 Topic 代表）
        sorted_items = sorted(
            items,
            key=lambda x: x.get("metadata", {}).get("upvotes", 0)
            or x.get("metadata", {}).get("score", 0)
            or 0,
            reverse=True,
        )

        # 预处理文本
        texts = [self._item_text(it) for it in sorted_items]
        token_lists = [tokenize(t) for t in texts]
        tfidf_vecs = build_tfidf(token_lists)

        for idx, item in enumerate(sorted_items):
            vec = tfidf_vecs[idx]
            signal = (
                item.get("metadata", {}).get("upvotes", 0)
                or item.get("metadata", {}).get("score", 0)
                or 0
            )

            best_topic_idx = -1
            best_sim = 0.0

            for ti, topic_vec in enumerate(self._topic_vectors):
                sim = cosine_similarity(vec, topic_vec)
                if sim > best_sim:
                    best_sim = sim
                    best_topic_idx = ti

            meta = item.get("metadata", {})
            entry = {
                "title": item.get("title", ""),
                "url": item.get("url", ""),
                "feed": meta.get("feed_name", "") or meta.get("subreddit", ""),
                "signal": signal,
                "content_snippet": (item.get("content", "") or "")[:300],
            }

            if best_sim >= self.threshold and best_topic_idx >= 0:
                # 合并到已有 Topic
                topic = self.topics[best_topic_idx]
                topic["sources"].append(entry)
                topic["item_count"] += 1
                topic["top_signal"] = max(topic["top_signal"], signal)
                topic["raw_texts"].append(entry["content_snippet"])
                # 更新 Topic 向量为加权平均（近似）
                old_vec = self._topic_vectors[best_topic_idx]
                n = topic["item_count"]
                merged = {
                    t: (old_vec.get(t, 0) * (n - 1) / n + vec.get(t, 0) / n)
                    for t in set(old_vec) | set(vec)
                }
                self._topic_vectors[best_topic_idx] = merged
            else:
                # 新建 Topic
                new_topic: dict[str, Any] = {
                    "topic_id": len(self.topics),
                    "topic_title": item.get("title", "(no title)"),
                    "item_count": 1,
                    "top_signal": signal,
                    "sources": [entry],
                    "raw_texts": [entry["content_snippet"]],
                    "consensus_prompt": "",   # 由 build_prompts() 填充
                }
                self.topics.append(new_topic)
                self._topic_vectors.append(vec)

        return self

    def sorted_topics(self) -> list[dict[str, Any]]:
        """按 signal × log(item_count+1) 热度排序"""
        return sorted(
            self.topics,
            key=lambda t: t["top_signal"] * math.log(t["item_count"] + 1),
            reverse=True,
        )

    def build_prompts(self) -> None:
        """
        为每个 multi-source Topic 生成 LLM 调用 prompt，
        用于后续让 Claude 输出"核心共识 + 主要争议"。
        """
        for topic in self.topics:
            if topic["item_count"] < 2:
                topic["consensus_prompt"] = ""
                continue

            sources_text = "\n".join(
                f"- [{s['feed']}] {s['title']}: {s['content_snippet']}"
                for s in topic["sources"][:6]
            )
            topic["consensus_prompt"] = (
                f"以下是来自不同来源的{topic['item_count']}条关于同一话题的帖子，"
                f"话题标题：《{topic['topic_title']}》\n\n"
                f"{sources_text}\n\n"
                "请用中文输出：\n"
                "1. **核心共识**（2-3句话）：这件事的关键事实是什么？社区普遍认同什么？\n"
                "2. **主要争议/吐槽**（2-3句话）：社区对什么有分歧？有什么批评或担忧？\n"
                "3. **信号强度判断**：这条信息对 LLM/AI 工程师有多大参考价值？(高/中/低 + 一句理由)\n"
                "回复控制在 150 字以内，避免复读标题。"
            )


# ---------------------------------------------------------------------------
# 过滤器（基于 ProfileLoader）
# ---------------------------------------------------------------------------

def apply_profile_filter(
    items: list[dict],
    profile_path: str | None,
    category: str = "community",
) -> list[dict]:
    """
    按 profile.yaml 进行简单关键词预过滤（减少聚类规模）。
    category='community' 时：不做强过滤，只按 community_boost_keywords 加权
    category='finance'   时：只保留 business_focus.sectors 相关内容
    """
    if not profile_path:
        return items

    try:
        scripts_dir = os.path.dirname(os.path.abspath(__file__))
        if scripts_dir not in sys.path:
            sys.path.insert(0, scripts_dir)
        from profile_loader import ProfileLoader
        loader = ProfileLoader(profile_path)
    except Exception as e:
        logger.warning("ProfileLoader unavailable for filtering: %s", e)
        return items

    if category == "finance":
        # 财经过滤：只保留 metadata.category == 'finance'
        return [
            it for it in items
            if it.get("metadata", {}).get("category") == "finance"
        ]

    # community: 返回全部，但添加 profile_boost 字段（供排序使用）
    boost_kws = [
        kw.lower()
        for domain in loader.domains.values()
        for kw in domain.keywords
    ]
    for item in items:
        text = (item.get("title", "") + " " + (item.get("content", "") or "")[:200]).lower()
        boost = sum(1 for kw in boost_kws if kw in text)
        meta = item.setdefault("metadata", {})
        meta["profile_boost"] = boost

    return items


# ---------------------------------------------------------------------------
# 主函数
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Cluster community items into topics (dedup + consensus)"
    )
    parser.add_argument("--input", required=True, help="fetched.json 路径")
    parser.add_argument("--output", required=True, help="clustered.json 输出路径")
    parser.add_argument("--profile", default="profile.yaml", help="profile.yaml 路径")
    parser.add_argument(
        "--category",
        default="community",
        choices=["community", "finance", "all"],
        help="过滤的内容类别",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.25,
        help="相似度聚类阈值（0~1，越高越严格，推荐 0.20~0.35）",
    )
    parser.add_argument(
        "--with-prompts",
        action="store_true",
        help="是否为多源 Topic 生成 consensus_prompt",
    )
    parser.add_argument(
        "--min-signal",
        type=int,
        default=0,
        help="过滤掉 signal（upvotes/score）低于此值的帖子",
    )
    args = parser.parse_args()

    # 加载
    logger.info("Loading %s ...", args.input)
    with open(args.input, encoding="utf-8") as f:
        fetched = json.load(f)

    items: list[dict] = fetched.get("items", [])
    logger.info("Total items: %d", len(items))

    # 过滤
    filtered = apply_profile_filter(items, args.profile, args.category)
    if args.min_signal > 0:
        before = len(filtered)
        filtered = [
            it for it in filtered
            if (
                it.get("metadata", {}).get("upvotes", 0)
                or it.get("metadata", {}).get("score", 0)
                or 0
            ) >= args.min_signal
        ]
        logger.info("Signal filter: %d → %d (min_signal=%d)", before, len(filtered), args.min_signal)

    logger.info("Items after filter: %d", len(filtered))

    # 聚类
    clusterer = TopicClusterer(similarity_threshold=args.threshold)
    clusterer.fit(filtered)

    if args.with_prompts:
        clusterer.build_prompts()

    sorted_topics = clusterer.sorted_topics()

    # 孤立帖子（单源 Topic，signal 较低的）
    unclustered = [t for t in sorted_topics if t["item_count"] == 1]
    multi_topics = [t for t in sorted_topics if t["item_count"] > 1]

    logger.info(
        "Clustering done: %d multi-source topics, %d singletons",
        len(multi_topics),
        len(unclustered),
    )

    # 统计
    stats = {
        "input_items": len(items),
        "filtered_items": len(filtered),
        "total_topics": len(sorted_topics),
        "multi_source_topics": len(multi_topics),
        "singletons": len(unclustered),
        "threshold": args.threshold,
        "category": args.category,
    }

    result = {
        "topics": multi_topics + unclustered,  # 多源在前
        "stats": stats,
    }

    # 输出
    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    logger.info("Written to %s", args.output)

    # 打印预览
    print(f"\n=== Topic Clusters ({len(multi_topics)} multi-source) ===")
    for t in multi_topics[:10]:
        print(
            f"\n[{t['item_count']} sources | signal={t['top_signal']}] "
            f"{t['topic_title'][:70]}"
        )
        for s in t["sources"][:3]:
            print(f"  · [{s['feed']}] {s['title'][:60]}")
        if t.get("consensus_prompt"):
            print(f"  → prompt ready ({len(t['consensus_prompt'])} chars)")


if __name__ == "__main__":
    main()
