#!/usr/bin/env python3
"""
poxiao.py — 破晓 PoXiao V1.2 统一入口 CLI

V1.2 新增：
  - 路径定义模块 path_utils（.poxiao_system/ + PoXiao_Briefs/ 隔离）
  - 接入 S2 熔断器 + SQLite 缓存层（scripts/cache_manager.py）
  - LLM 话题聚类（调用 OpenAI 兼容 API 进行降噪）
  - Tier 1 / Tier 2 分层 Markdown 渲染（<details> 折叠深分析）
  - 多用户数据物理隔离
  - 无 LLM 时的高质量降级渲染（原生摘要提取）

用法：
    python poxiao.py generate --user andy
    python poxiao.py analyze 2401.12345 --user andy
    python poxiao.py setup
    python poxiao.py list-users
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import re
import subprocess
import sys
import textwrap
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

# ── V1.2: 加载 path_utils（路径定义模块）───────────────────────────────
try:
    from scripts.path_utils import (
        get_work_dir, get_system_dir, get_briefs_dir,
        get_profile_path, get_output_dir, get_briefing_filename,
        get_display_name, auto_detect_days,
        check_env_file, load_env_if_needed,
        get_fetched_json_path, get_papers_json_path, get_clustered_json_path,
    )
except ImportError:
    try:
        from path_utils import (
            get_work_dir, get_system_dir, get_briefs_dir,
            get_profile_path, get_output_dir, get_briefing_filename,
            get_display_name, auto_detect_days,
            check_env_file, load_env_if_needed,
            get_fetched_json_path, get_papers_json_path, get_clustered_json_path,
        )
    except ImportError:
        # 兜底：使用内联最小实现
        def get_work_dir(): return Path(__file__).parent.resolve()
        def get_profile_path(u): return get_work_dir() / "profile.yaml"
        def get_display_name(u): return u
        def auto_detect_days(): return 3 if datetime.now().weekday() == 0 else 1
        def check_env_file(): return {"exists": False, "missing_warning": ""}
        def load_env_if_needed(): pass
        def get_output_dir(u, d=None): return get_work_dir() / "data" / u / (d or datetime.now().strftime("%Y-%m-%d"))
        def get_briefing_filename(d, dn, rt): return f"{d}_{dn}的{rt}.md"

logger = logging.getLogger("poxiao")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
    datefmt="%H:%M:%S",
)

WORK_DIR = get_work_dir()
PYTHON   = sys.executable


# ──────────────────────────────────────────────────────────────────────
# 路径工具（多用户隔离）
# ──────────────────────────────────────────────────────────────────────

def get_profile_path(username: str) -> Path:
    """返回 profiles/profile_{username}.yaml，不存在时 fallback 到 default.yaml"""
    # V1.2: 优先检查 .poxiao_system/profiles/（新标准路径）
    system_profiles = WORK_DIR / ".poxiao_system" / "profiles"
    path = system_profiles / f"profile_{username}.yaml"
    if path.exists():
        return path

    # 其次检查 profiles/（旧路径，兼容）
    legacy_profiles = WORK_DIR / "profiles"
    path = legacy_profiles / f"profile_{username}.yaml"
    if path.exists():
        return path

    # 再检查 default
    default = system_profiles / "default.yaml"
    if not default.exists():
        default = legacy_profiles / "default.yaml"
    if default.exists():
        return default

    # 终极 fallback：根目录 profile.yaml
    legacy = WORK_DIR / "profile.yaml"
    if legacy.exists():
        return legacy

    raise FileNotFoundError(
        f"找不到用户 '{username}' 的 profile。\n"
        f"请先运行: python poxiao.py setup --user {username}"
    )


def get_output_dir(username: str, date: str | None = None) -> Path:
    """返回输出目录并确保创建：data/{username}/{YYYY-MM-DD}/"""
    date_str = date or datetime.now().strftime("%Y-%m-%d")
    out_dir = WORK_DIR / "data" / username / date_str
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir


def get_briefing_filename(username: str, report_type: str, date: str | None = None) -> str:
    """中文友好文件名：{display_name}的早报_{类型}_{日期}.md"""
    date_str = date or datetime.now().strftime("%Y-%m-%d")
    type_map = {
        "academic":  "学术概览",
        "community": "社区速递",
        "finance":   "财经简报",
        "index":     "今日索引",
    }
    type_label = type_map.get(report_type, report_type)
    display_name = _get_display_name(username)
    return f"{display_name}的早报_{type_label}_{date_str}.md"


def _get_display_name(username: str) -> str:
    """从 profile.yaml 读取 meta.display_name，失败时返回 username"""
    try:
        import yaml
        path = get_profile_path(username)
        with open(path, encoding="utf-8") as f:
            cfg = yaml.safe_load(f) or {}
        return cfg.get("meta", {}).get("display_name", username)
    except Exception:
        return username


def auto_detect_days() -> int:
    """周一返回 3（覆盖周末），其余工作日返回 1"""
    weekday = datetime.now().weekday()  # 0=Monday
    return 3 if weekday == 0 else 1


# ──────────────────────────────────────────────────────────────────────
# LLM 聊天接口（OpenAI 兼容）
# ──────────────────────────────────────────────────────────────────────

def call_llm(prompt: str, model: str = "glm-4-flash", temperature: float = 0.3) -> str:
    """
    调用 LLM 进行聊天。自动检测可用提供商，优先级：

    1. ZHIPU_API_KEY     → 智谱 GLM（默认推荐）
    2. MINIMAX_API_KEY   → MiniMax
    3. VOLC_API_KEY      → 火山引擎
    4. ANTHROPIC_API_KEY → Claude
    5. OPENAI_API_KEY    → OpenAI
    6. DEEPSEEK_API_KEY  → DeepSeek
    7. LOCAL_LLM_URL     → 本地 Ollama 等
    """
    api_key = os.environ.get("ZHIPU_API_KEY", "")
    base_url = "https://open.bigmodel.cn/api/paas/v4"
    model = os.environ.get("ZHIPU_MODEL", "glm-4-flash")

    if not api_key:
        api_key = os.environ.get("MINIMAX_API_KEY", "")
        base_url = "https://api.minimax.chat/v1"
        model = os.environ.get("MINIMAX_MODEL", "MiniMax-Text-01")

    if not api_key:
        api_key = os.environ.get("VOLC_API_KEY", "")
        base_url = "https://ARK.cn-beijing.volces.com/api/v1"
        model = os.environ.get("VOLC_MODEL", "doubao-pro-32k")

    if not api_key:
        api_key = os.environ.get("ANTHROPIC_API_KEY", "")
        base_url = os.environ.get("ANTHROPIC_BASE_URL", "")
        if api_key and "anthropic" not in base_url.lower():
            base_url = ""

    if not api_key:
        api_key = os.environ.get("OPENAI_API_KEY", "")
        base_url = os.environ.get("OPENAI_BASE_URL", "")
        model = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")

    if not api_key:
        api_key = os.environ.get("DEEPSEEK_API_KEY", "")
        base_url = "https://api.deepseek.com/v1"
        model = os.environ.get("DEEPSEEK_MODEL", "deepseek-chat")

    if not api_key and os.environ.get("LOCAL_LLM_URL"):
        base_url = os.environ.get("LOCAL_LLM_URL", "")
        api_key = "local"
        model = os.environ.get("LOCAL_MODEL", "llama3")

    if not api_key:
        logger.warning("未检测到任何 LLM API Key（支持：GLM/MiniMax/火山引擎/Claude/OpenAI/DeepSeek），将使用原生摘要模式")
        return ""

    try:
        import openai
        client_kwargs = {"api_key": api_key}
        if base_url:
            client_kwargs["base_url"] = base_url
        client = openai.OpenAI(**client_kwargs)
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "你是一个专业的技术简报编辑。请用简洁、准确的中文输出，避免冗余。"},
                {"role": "user", "content": prompt},
            ],
            temperature=temperature,
            max_tokens=2000,
        )
        return response.choices[0].message.content.strip()
    except ImportError:
        logger.warning("openai 库未安装，LLM 功能跳过")
        return ""
    except Exception as e:
        logger.error("LLM 调用失败: %s", e)
        return ""


# ──────────────────────────────────────────────────────────────────────
# LLM 话题聚类与降噪（Task 2）
# ──────────────────────────────────────────────────────────────────────

def llm_filter_and_summarize(
    clustered_data: dict,
    profile: dict,
    report_type: str = "community",
) -> list[dict]:
    """
    使用 LLM 对聚类结果进行过滤和摘要生成。

    Args:
        clustered_data: cluster_topics.py 的输出（topics + stats）
        profile:        用户 profile.yaml 解析后的字典
        report_type:    'community' 或 'finance'

    Returns:
        经过 LLM 过滤和摘要后的条目列表，每个条目含：
          title, summary, sources, item_count, top_signal, tier2_details
    """
    # 构建系统级 prompt（注入用户 profile）
    domains = profile.get("research_domains", {})
    domain_names = list(domains.keys())
    business = profile.get("business_focus", {}).get("sectors", [])

    if report_type == "community":
        system_prompt = textwrap.dedent(f"""\
            你是一个技术社区简报编辑。请从以下话题列表中筛选出与用户兴趣最相关的条目。

            用户研究领域：{', '.join(domain_names)}
            用户商业关注：{', '.join(business)}

            筛选规则：
            - 优先保留：LLM Agent 工程、推理优化、多模态、RAG、AI 安全、AI 编程（Vibe Coding）
            - 排除：纯宏观经济、传统金融、与 AI 无关的硬件新闻、纯营销软文
            - 同一话题多源聚合时，提取"核心共识"和"主要争议/吐槽"

            输出格式：JSON array，每项含：
            {{
              "title": "话题标题",
              "summary": "一句话核心摘要（30字以内）",
              "consensus": "社区共识（可选，50字以内）",
              "debate": "主要争议/吐槽（可选，50字以内）",
              "relevance_score": 0-10 的整数,
              "sources": ["源1标题", "源2标题"],
              "source_count": 数字
            }}
            只返回 JSON，不要额外文字。
        """)
    elif report_type == "finance":
        system_prompt = textwrap.dedent(f"""\
            你是一个财经简报编辑。请从以下话题列表中筛选出与 AI/科技投融资相关的条目。

            用户商业关注：{', '.join(business)}

            筛选规则：
            - 优先保留：AI 算力基础设施（GPU/芯片/数据中心）融资、顶尖 AI 初创融资、大厂 AI 战略变动、AI 产品商业化里程碑
            - 排除：纯宏观经济（利率、汇率、大宗商品）、传统银行/保险业务、与 AI 无关的常规财报

            输出格式：JSON array，每项含：
            {{
              "title": "标题",
              "summary": "一句话摘要（30字以内）",
              "relevance_score": 0-10 的整数,
              "sources": ["源1", "源2"]
            }}
            只返回 JSON，不要额外文字。
        """)
    else:
        return []

    # 准备输入数据（每个 topic 的文本）
    input_items = []
    for topic in clustered_data.get("topics", []):
        if topic.get("item_count", 0) < 1:
            continue
        sources_text = "\n".join(
            f"- [{s.get('feed', '')}] {s.get('title', '')}"
            for s in topic.get("sources", [])[:5]
        )
        input_items.append({
            "topic_title": topic.get("topic_title", ""),
            "item_count": topic.get("item_count", 0),
            "top_signal": topic.get("top_signal", 0),
            "sources": sources_text,
            "has_prompt": bool(topic.get("consensus_prompt")),
        })

    if not input_items:
        return []

    input_text = "\n\n".join(
        f"【话题 {i+1}】\n标题: {item['topic_title']}\n"
        f"来源数: {item['item_count']}\n信号值: {item['top_signal']}\n"
        f"来源列表:\n{item['sources']}\n"
        for i, item in enumerate(input_items)
    )

    user_prompt = f"请分析以下 {len(input_items)} 个话题：\n\n{input_text}"

    # 调用 LLM
    result_json = call_llm(system_prompt + "\n\n" + user_prompt)
    if not result_json:
        # LLM 不可用时，回退到原始数据 + 简单关键词过滤
        return _fallback_filter(input_items, report_type)

    # 解析 JSON
    try:
        # 尝试提取 JSON 块（LLM 可能包裹在 ```json 中）
        match = re.search(r'\[\s*\{.*\}\s*\]', result_json, re.DOTALL)
        if match:
            result_json = match.group(0)
        filtered = json.loads(result_json)
    except (json.JSONDecodeError, ValueError) as e:
        logger.warning("LLM 返回 JSON 解析失败: %s, 回退到关键词过滤", e)
        filtered = _fallback_filter(input_items, report_type)

    # 转换为标准输出格式
    output = []
    for item in filtered:
        score = item.get("relevance_score", 0)
        if score < 3:
            continue  # 过滤低相关性

        output.append({
            "title": item.get("title", ""),
            "summary": item.get("summary", ""),
            "consensus": item.get("consensus", ""),
            "debate": item.get("debate", ""),
            "relevance_score": score,
            "sources": item.get("sources", []),
            "source_count": item.get("source_count", 0),
            "tier2_details": {
                "consensus": item.get("consensus", ""),
                "debate": item.get("debate", ""),
            } if item.get("consensus") or item.get("debate") else None,
        })

    # 按相关性降序排序
    output.sort(key=lambda x: x["relevance_score"], reverse=True)
    return output


def _fallback_filter(input_items: list[dict], report_type: str) -> list[dict]:
    """LLM 不可用时的关键词兜底过滤"""
    # 简单关键词匹配
    boost_kws = [
        "agent", "llm", "inference", "vllm", "quantization", "rag", "multimodal",
        "coding", "swe-bench", "reasoning", "rlhf", "grpo", "ppo", "moe",
        "融资", "估值", "ipo", "ai", "大模型", "芯片", "算力", "推理",
    ]
    result = []
    for item in input_items:
        text = (item["topic_title"] + " " + item["sources"]).lower()
        score = sum(1 for kw in boost_kws if kw in text)
        if score >= 2 or item["top_signal"] > 100:
            result.append({
                "title": item["topic_title"],
                "summary": f"[{item['item_count']} 源] 信号值 {item['top_signal']}",
                "relevance_score": min(score * 2, 10),
                "sources": [],
                "source_count": item["item_count"],
            })
    result.sort(key=lambda x: x["relevance_score"], reverse=True)
    return result[:10]


# ──────────────────────────────────────────────────────────────────────
# Markdown 渲染引擎（Task 3: Tier 1 / Tier 2 分层）
# ──────────────────────────────────────────────────────────────────────

def render_markdown_header(warnings: list[str]) -> str:
    """
    生成 Markdown 头部警告区块（来自 WarningCollector）。
    若无警告则返回空字符串。
    """
    if not warnings:
        return ""
    lines = [
        "> **⚠️ 数据完整性提示**（部分信源今日未能正常抓取）\n>",
    ]
    for w in warnings:
        lines.append(f"> - {w}")
    lines.append("")
    return "\n".join(lines)


def render_tier2_details(consensus: str = "", debate: str = "", extra: str = "") -> str:
    """
    生成 HTML <details> 折叠块（Tier 2 内容）。
    """
    parts = []
    if consensus:
        parts.append(f"**核心共识**：{consensus}")
    if debate:
        parts.append(f"**主要争议**：{debate}")
    if extra:
        parts.append(extra)
    if not parts:
        return ""
    return (
        "\n<details><summary>展开详情</summary>\n\n"
        + "\n\n".join(parts)
        + "\n\n</details>"
    )


def generate_academic_markdown(
    papers: list[dict],
    profile: dict,
    display_name: str,
    date_str: str,
    warnings: list[str],
) -> str:
    """生成学术简报 Markdown（Tier 1 / Tier 2 分层）"""
    top_n = profile.get("format_preference", {}).get("academic_top_n", 8)
    deep_threshold = profile.get("format_preference", {}).get("trigger_deep_analysis_threshold", 4.5)

    sections = [
        f"# 📡 学术概览 · {display_name} · {date_str}",
        "",
        render_markdown_header(warnings),
        f"> 时间窗口：{auto_detect_days()} 天 · 共 {len(papers)} 篇论文 · Top {top_n} 精读",
        "",
        "---",
        "",
    ]

    # Top N 精读区
    for i, paper in enumerate(papers[:top_n], 1):
        title = paper.get("title", "(no title)")
        arxiv_url = paper.get("url", "") or f"https://arxiv.org/abs/{paper.get('arxiv_id', '')}"
        score = paper.get("scores", {}).get("recommendation", 0)
        domain = paper.get("matched_domain", "")
        summary = paper.get("summary", "") or paper.get("abstract", "")[:300]

        sections.append(f"### {i}. [{title}]({arxiv_url})")
        sections.append(f"> 📌 领域：{domain} · 评分：{score}/10")
        sections.append(f"> {summary[:120]}...")

        # Tier 2: 深分析折叠块（评分 > 阈值时展开）
        if score >= deep_threshold and paper.get("trigger_deep_analysis"):
            deep_content = paper.get("deep_analysis_content", "")
            if deep_content:
                sections.append(render_tier2_details(extra=deep_content))
            else:
                sections.append(render_tier2_details(
                    consensus=f"评分 {score}（≥{deep_threshold}），建议深读",
                    debate=f"匹配领域：{domain}",
                ))

        sections.append("")

    # 其余论文（列表形式）
    if len(papers) > top_n:
        sections.append("---")
        sections.append("")
        sections.append("### 其他论文")
        sections.append("")
        for paper in papers[top_n:]:
            title = paper.get("title", "(no title)")
            arxiv_url = paper.get("url", "") or f"https://arxiv.org/abs/{paper.get('arxiv_id', '')}"
            score = paper.get("scores", {}).get("recommendation", 0)
            domain = paper.get("matched_domain", "")
            sections.append(
                f"- **[{title}]({arxiv_url})** · {domain} · {score}/10"
            )
        sections.append("")

    sections.append("---")
    sections.append(f"*生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
    return "\n".join(sections)


def generate_community_markdown(
    filtered_items: list[dict],
    raw_items: list[dict],  # V1.2 新增：原始抓取数据（用于降级渲染）
    profile: dict,
    display_name: str,
    date_str: str,
    warnings: list[str],
) -> str:
    """生成社区简报 Markdown（Tier 1 / Tier 2 分层）

    V1.2 改造：
      - 无 LLM 时，从 raw_items 提取原生摘要（Raw Snippet）
      - 即使 LLM 过滤结果为空，也展示原始数据的高质量降级版
    """
    from scripts.text_utils import render_community_item_tier1, render_community_item_tier2, render_raw_snippet

    top_n = profile.get("format_preference", {}).get("community_top_n", 10)

    sections = [
        f"# 🔥 社区速递 · {display_name} · {date_str}",
        "",
        render_markdown_header(warnings),
        f"> 时间窗口：{auto_detect_days()} 天",
        "",
        "---",
        "",
    ]

    # 如果 LLM 过滤后有结果，使用 LLM 结果；否则降级到原始数据
    if filtered_items:
        items_to_render = filtered_items
        use_llm = True
    else:
        # V1.2 降级：从原始聚类数据中提取 Top N
        items_to_render = _fallback_community_items(raw_items, top_n)
        use_llm = False

    for i, item in enumerate(items_to_render[:top_n], 1):
        title = item.get("title", "(no title)")
        source_count = item.get("source_count", item.get("item_count", 1))
        score = item.get("relevance_score", item.get("top_signal", 0))

        sections.append(f"### {i}. {title}")

        if use_llm:
            summary = item.get("summary", "")
            sections.append(f"> {summary} · {source_count} 源 · 相关性 {score}/10")
        else:
            # V1.2 降级渲染：从原始数据提取原生摘要
            snippet = render_raw_snippet(item, max_length=120)
            sections.append(f"> {snippet} · {source_count} 源 · 信号值 {score}")

        # Tier 2: 展开详情
        if use_llm:
            tier2 = item.get("tier2_details")
            if tier2:
                sections.append(render_tier2_details(
                    consensus=tier2.get("consensus", ""),
                    debate=tier2.get("debate", ""),
                ))
        else:
            # 降级模式下的 Tier 2
            sections.append(render_community_item_tier2(item))

        sections.append("")

    if not use_llm and filtered_items:
        sections.append("> *注：今日 LLM 聚类不可用，已切换为原生摘要模式*")
        sections.append("")

    sections.append("---")
    sections.append(f"*生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
    return "\n".join(sections)


def _fallback_community_items(raw_items: list[dict], top_n: int) -> list[dict]:
    """
    V1.2 降级：从原始抓取数据中选取 Top N 条目。
    按 signal 排序，去除纯 HTML/空内容。
    """
    from scripts.text_utils import strip_html

    scored = []
    for item in raw_items:
        title = item.get("title", "")
        # 计算信号值
        signal = item.get("top_signal", 0) or item.get("signal", 0)
        # 检查内容有效性
        raw_text = item.get("description", "") or item.get("content", "") or ""
        clean = strip_html(raw_text)
        if not clean and not title:
            continue  # 跳过空内容
        scored.append({
            **item,
            "_signal": signal,
        })

    scored.sort(key=lambda x: x["_signal"], reverse=True)
    return scored[:top_n]


def generate_finance_markdown(
    filtered_items: list[dict],
    profile: dict,
    display_name: str,
    date_str: str,
    warnings: list[str],
) -> str:
    """生成财经简报 Markdown"""
    top_n = profile.get("format_preference", {}).get("finance_top_n", 8)

    sections = [
        f"# 💰 财经简报 · {display_name} · {date_str}",
        "",
        render_markdown_header(warnings),
        f"> 时间窗口：{auto_detect_days()} 天 · 共 {len(filtered_items)} 条动态",
        "",
        "---",
        "",
    ]

    if not filtered_items:
        sections.append("> 今日财经动态较少，主要关注学术和社区简报。")
        sections.append("")
    else:
        for i, item in enumerate(filtered_items[:top_n], 1):
            title = item.get("title", "(no title)")
            summary = item.get("summary", "")
            score = item.get("relevance_score", 0)

            sections.append(f"### {i}. {title}")
            sections.append(f"> {summary} · 相关性 {score}/10")
            sections.append("")

    sections.append("---")
    sections.append(f"*生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
    return "\n".join(sections)


def generate_index_markdown(
    display_name: str,
    date_str: str,
    academic_count: int,
    community_count: int,
    finance_count: int,
    warnings: list[str],
) -> str:
    """生成今日索引"""
    return textwrap.dedent(f"""\
        # 每日简报 · {display_name} · {date_str}

        {render_markdown_header(warnings)}
        > 生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M')} | 时间窗口：{auto_detect_days()} 天

        ## 快速导航

        - [📡 学术概览](./{display_name}的早报_学术概览_{date_str}.md)（{academic_count} 篇论文）
        - [🔥 社区速递](./{display_name}的早报_社区速递_{date_str}.md)（{community_count} 条话题）
        - [💰 财经简报](./{display_name}的早报_财经简报_{date_str}.md)（{finance_count} 条动态）

        ## 今日三句话

        > 📡 **学术**：Top {academic_count} 论文已就绪
        > 🔥 **社区**：{community_count} 条话题已聚类降噪
        > 💰 **财经**：{finance_count} 条 AI/科技投融资动态

        ---
        *破晓 PoXiao · AI 原生驱动的个人情报系统*
    """)


# ──────────────────────────────────────────────────────────────────────
# 子命令：generate（V1.1 重构版）
# ──────────────────────────────────────────────────────────────────────

def cmd_generate(args: argparse.Namespace) -> int:
    username = args.user
    days = args.days or auto_detect_days()
    report_type = getattr(args, "type", "all")
    date_str = datetime.now().strftime("%Y-%m-%d")

    try:
        profile_path = get_profile_path(username)
    except FileNotFoundError as e:
        logger.error(str(e))
        return 1

    output_dir = get_output_dir(username, date_str)
    display_name = _get_display_name(username)

    logger.info("用户: %s | 时间窗口: %d 天 | 输出: %s", display_name, days, output_dir)

    # ── 加载 profile ──────────────────────────────────────────────────
    try:
        import yaml
        with open(profile_path, encoding="utf-8") as f:
            profile = yaml.safe_load(f) or {}
    except Exception as e:
        logger.error("加载 profile 失败: %s", e)
        return 1

    # ── 收集全局警告（来自 retry.py 的 WarningCollector）──────────────
    try:
        from scripts.retry import WarningCollector
    except ImportError:
        try:
            from retry import WarningCollector
        except ImportError:
            WarningCollector = None

    warnings = []

    # ── Step 1: 社区抓取 ──────────────────────────────────────────────
    fetch_success = False
    fetch_json = output_dir / "fetched.json"
    if report_type in ("all", "community", "finance"):
        if fetch_json.exists():
            logger.info("fetched.json 已存在，跳过重新抓取")
            fetch_success = True
        else:
            logger.info("开始社区抓取 (days=%d)...", days)
            ret = _run_script("scripts/fetch.py", ["--config", "config.json", "--days", str(days), "--output", str(output_dir)])
            if ret != 0:
                logger.error("fetch.py 运行失败（exit=%d），社区和财经简报将无法生成", ret)
                # 记录到警告
                try:
                    from scripts.retry import WarningCollector
                    WarningCollector.add("社区数据抓取失败，今日社区和财经简报无法生成")
                except ImportError:
                    pass
            else:
                src = WORK_DIR / "fetched.json"
                if src.exists():
                    src.rename(fetch_json)
                    logger.info("已移动 fetched.json → %s", fetch_json)
                    fetch_success = True
                else:
                    logger.error("fetch.py 执行成功但未生成 fetched.json")

    # ── Step 2: 学术论文搜索 ──────────────────────────────────────────
    papers_success = False
    papers_json = output_dir / "papers.json"
    if report_type in ("all", "academic"):
        if papers_json.exists():
            logger.info("papers.json 已存在，跳过重新搜索")
            papers_success = True
        else:
            logger.info("开始学术搜索...")
            ret = _run_script(
                "scripts/search_papers.py",
                [
                    "--config", str(profile_path),
                    "--output", str(papers_json),
                    "--max-results", "200",
                    "--top-n", "15",
                ],
            )
            if ret != 0:
                logger.error("search_papers.py 运行失败（exit=%d），学术简报将无法生成", ret)
                try:
                    from scripts.retry import WarningCollector
                    WarningCollector.add("学术论文搜索失败，今日学术简报无法生成")
                except ImportError:
                    pass
            else:
                papers_success = True

    # ── Step 3: 社区话题聚类 ──────────────────────────────────────────
    cluster_json = output_dir / "clustered.json"
    if report_type in ("all", "community") and fetch_json.exists():
        if cluster_json.exists():
            logger.info("clustered.json 已存在，跳过")
        else:
            logger.info("开始话题聚类...")
            ret = _run_script(
                "scripts/cluster_topics.py",
                [
                    "--input", str(fetch_json),
                    "--output", str(cluster_json),
                    "--profile", str(profile_path),
                    "--category", "community",
                    "--with-prompts",
                ],
            )
            if ret != 0:
                logger.warning("cluster_topics.py 运行失败（exit=%d），社区简报将降级", ret)

    # ── Step 4: LLM 过滤与摘要（Task 2）───────────────────────────────
    community_items = []
    finance_items = []

    if report_type in ("all", "community") and cluster_json.exists():
        try:
            with open(cluster_json, encoding="utf-8") as f:
                clustered = json.load(f)
            community_items = llm_filter_and_summarize(clustered, profile, "community")
            logger.info("LLM 过滤后社区话题: %d 条", len(community_items))
        except Exception as e:
            logger.warning("社区 LLM 过滤失败: %s", e)
            community_items = []

    if report_type in ("all", "finance") and fetch_json.exists():
        # 财经过滤：简单按 category=finance 过滤
        try:
            with open(fetch_json, encoding="utf-8") as f:
                fetched = json.load(f)
            finance_raw = [
                it for it in fetched.get("items", [])
                if it.get("metadata", {}).get("category") == "finance"
            ]
            if finance_raw:
                # 简单聚类（按 feed 分组）
                clustered_finance = {
                    "topics": [
                        {
                            "topic_title": it.get("title", ""),
                            "item_count": 1,
                            "top_signal": 0,
                            "sources": [{"feed": it.get("metadata", {}).get("feed_name", ""), "title": it.get("title", "")}],
                        }
                        for it in finance_raw[:20]
                    ]
                }
                finance_items = llm_filter_and_summarize(clustered_finance, profile, "finance")
                logger.info("LLM 过滤后财经话题: %d 条", len(finance_items))
        except Exception as e:
            logger.warning("财经 LLM 过滤失败: %s", e)
            finance_items = []

    # ── Step 5: 读取学术数据 ──────────────────────────────────────────
    academic_papers = []
    if report_type in ("all", "academic") and papers_json.exists():
        try:
            with open(papers_json, encoding="utf-8") as f:
                papers_data = json.load(f)
            academic_papers = papers_data.get("top_papers", [])
            logger.info("学术论文: %d 篇", len(academic_papers))
        except Exception as e:
            logger.warning("读取论文数据失败: %s", e)

    # ── Step 6: 收集警告 ─────────────────────────────────────────────
    if WarningCollector:
        warnings = WarningCollector.get_all()

    # ── Step 7: 生成 Markdown 文件（Task 3）───────────────────────────
    files_generated = []

    # 检查是否有任何数据可用
    has_data = (len(academic_papers) > 0) or (len(community_items) > 0) or (len(finance_items) > 0)

    if not has_data:
        logger.error("所有数据源均失败，无法生成简报")
        print("\n  ❌ 生成失败：所有数据源（社区/学术/财经）均未能成功获取数据")
        print("  请检查网络连接或稍后重试\n")
        return 1

    if report_type in ("all", "academic") and len(academic_papers) > 0:
        ac_file = output_dir / get_briefing_filename(username, "academic", date_str)
        ac_md = generate_academic_markdown(academic_papers, profile, display_name, date_str, warnings)
        ac_file.write_text(ac_md, encoding="utf-8")
        files_generated.append(str(ac_file.relative_to(WORK_DIR)))

    if report_type in ("all", "community") and (len(community_items) > 0 or cluster_json.exists()):
        co_file = output_dir / get_briefing_filename(username, "community", date_str)
        co_md = generate_community_markdown(
            community_items,
            _load_raw_community_items(cluster_json) if cluster_json.exists() else [],
            profile,
            display_name,
            date_str,
            warnings,
        )
        co_file.write_text(co_md, encoding="utf-8")
        files_generated.append(str(co_file.relative_to(WORK_DIR)))

    if report_type in ("all", "finance") and len(finance_items) > 0:
        fi_file = output_dir / get_briefing_filename(username, "finance", date_str)
        fi_md = generate_finance_markdown(finance_items, profile, display_name, date_str, warnings)
        fi_file.write_text(fi_md, encoding="utf-8")
        files_generated.append(str(fi_file.relative_to(WORK_DIR)))

    # Index（只有当生成了文件时才创建）
    if files_generated:
        idx_file = output_dir / get_briefing_filename(username, "index", date_str)
        idx_md = generate_index_markdown(
            display_name, date_str,
            len(academic_papers), len(community_items), len(finance_items),
            warnings,
        )
        idx_file.write_text(idx_md, encoding="utf-8")
        files_generated.append(str(idx_file.relative_to(WORK_DIR)))

    # ── 输出摘要 ──────────────────────────────────────────────────────
    print(f"""
╔══════════════════════════════════════════════════════════════╗
║          破晓 PoXiao — 生成任务完成                           ║
╚══════════════════════════════════════════════════════════════╝

用户:     {display_name} ({username})
日期:     {date_str}
窗口:     {days} 天

📡 学术: {len(academic_papers)} 篇论文
🔥 社区: {len(community_items)} 条话题（LLM 过滤后）
💰 财经: {len(finance_items)} 条动态

{'⚠️ 警告: ' + chr(10).join('    ' + w for w in warnings) if warnings else '✅ 无警告'}

输出文件:
{chr(10).join('  ' + f for f in files_generated)}
""")

    return 0


# ──────────────────────────────────────────────────────────────────────
# 其余子命令（analyze / setup / list-users）
# ──────────────────────────────────────────────────────────────────────

def cmd_analyze(args: argparse.Namespace) -> int:
    arxiv_id = args.arxiv_id
    username = args.user
    date_str = datetime.now().strftime("%Y-%m-%d")
    output_dir = get_output_dir(username, date_str)
    display_name = _get_display_name(username)

    logger.info("深度分析论文: %s", arxiv_id)
    print(f"""
╔══════════════════════════════════════════════════════════════╗
║         破晓 PoXiao — 论文深度分析任务                        ║
╚══════════════════════════════════════════════════════════════╝

arXiv ID: {arxiv_id}
用户:     {display_name} ({username})
输出目录: {output_dir}/papers/

请调用 paper-analyze skill 对论文 {arxiv_id} 进行深度分析，保存到:
  {output_dir}/papers/{arxiv_id}.md
""")
    return 0


def cmd_setup(args: argparse.Namespace) -> int:
    setup_script = WORK_DIR / "setup.py"
    if not setup_script.exists():
        logger.error("找不到 setup.py")
        return 1
    cmd = [PYTHON, str(setup_script)]
    if args.user:
        cmd += ["--user", args.user]
    if getattr(args, "defaults", False):
        cmd += ["--defaults"]
    return subprocess.run(cmd, cwd=str(WORK_DIR)).returncode


def cmd_list_users(args: argparse.Namespace) -> int:
    profiles_dir = WORK_DIR / "profiles"
    if not profiles_dir.exists():
        print("  尚未创建任何用户 Profile。运行 python poxiao.py setup 开始配置。")
        return 0
    profiles = sorted(profiles_dir.glob("profile_*.yaml"))
    if not profiles:
        print("  尚未创建任何用户 Profile。")
        return 0
    print(f"\n  已配置用户（{len(profiles)} 个）：\n")
    for p in profiles:
        username = p.stem.replace("profile_", "")
        data_dir = WORK_DIR / "data" / username
        report_count = len(list(data_dir.glob("**/*.md"))) if data_dir.exists() else 0
        display = _get_display_name(username)
        print(f"    • {username:15s}  显示名: {display:10s}  历史简报: {report_count} 份")
    print()
    return 0


# ──────────────────────────────────────────────────────────────────────
# 工具函数
# ──────────────────────────────────────────────────────────────────────

def _load_raw_community_items(cluster_json: Path) -> list[dict]:
    """从 clustered.json 加载原始话题数据（用于降级渲染）"""
    try:
        with open(cluster_json, encoding="utf-8") as f:
            data = json.load(f)
        return data.get("topics", [])
    except Exception:
        return []


def _run_script(script: str, extra_args: list[str]) -> int:
    cmd = [PYTHON, str(WORK_DIR / script)] + extra_args
    logger.debug("运行: %s", " ".join(cmd))
    return subprocess.run(cmd, cwd=str(WORK_DIR)).returncode


# ──────────────────────────────────────────────────────────────────────
# CLI 定义
# ──────────────────────────────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="poxiao",
        description="破晓 PoXiao V1.1 — AI 原生驱动的个人情报系统",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
触发词（Skill 模式）:
  /poxiao generate        → 生成今日三份简报
  /briefing               → 同上
  /deep_dive 2401.12345   → 深度分析论文

示例:
  python poxiao.py generate                         # default 用户
  python poxiao.py generate --user andy --days 3   # andy 用户，3天窗口
  python poxiao.py generate --user andy --type academic
  python poxiao.py analyze 2401.12345 --user andy
  python poxiao.py setup --user alice
  python poxiao.py list-users
        """,
    )
    sub = parser.add_subparsers(dest="command", metavar="<command>")

    p_gen = sub.add_parser("generate", help="生成今日情报简报")
    p_gen.add_argument("--user",  default="default", help="用户名")
    p_gen.add_argument("--days",  type=int, default=None, help="抓取时间窗口（天）")
    p_gen.add_argument("--type",  default="all", choices=["all", "academic", "community", "finance"])
    p_gen.add_argument("--date",  default=None, help="目标日期 YYYY-MM-DD")
    p_gen.add_argument("--force-refresh", action="store_true", help="强制重新抓取数据（忽略缓存）")
    p_gen.add_argument("--skip-llm", action="store_true", help="跳过 LLM 过滤，使用原生摘要模式")
    p_gen.add_argument("--output", default=None, help="自定义输出目录")

    p_ana = sub.add_parser("analyze", help="深度分析单篇 arXiv 论文")
    p_ana.add_argument("arxiv_id", help="arXiv 论文编号，如 2401.12345（不含 arXiv: 前缀）")
    p_ana.add_argument("--user", default="default")

    p_setup = sub.add_parser("setup", help="交互式用户配置引导")
    p_setup.add_argument("--user",     default=None)
    p_setup.add_argument("--defaults", action="store_true")

    sub.add_parser("list-users", help="列出所有已配置用户")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    handlers = {
        "generate":   cmd_generate,
        "analyze":    cmd_analyze,
        "setup":      cmd_setup,
        "list-users": cmd_list_users,
    }

    if args.command is None:
        parser.print_help()
        sys.exit(0)

    handler = handlers.get(args.command)
    if handler is None:
        parser.print_help()
        sys.exit(1)

    sys.exit(handler(args))


if __name__ == "__main__":
    main()
