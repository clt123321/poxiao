"""
text_utils.py — 破晓 PoXiao V1.2 文本处理工具

核心功能：
  1. HTML 标签剔除（正则 + BeautifulSoup fallback）
  2. 原生摘要提取（前 150 字符，智能断句）
  3. 中英文混合截断（避免腰斩汉字/单词）
  4. Markdown 安全转义

降级模式下的富文本渲染依赖此模块生成"原生摘要 (Raw Snippet)"，
确保即使无 LLM，输出也接近高级 RSS 阅读器的观感。
"""

from __future__ import annotations

import re
import html
from typing import Any

# --------------------------------------------------------------------------
# HTML 清理
# --------------------------------------------------------------------------

# 预编译正则（快速路径，覆盖 90% 场景）
_HTML_TAG_RE = re.compile(r'<[^>]+>')
_HTML_ENTITY_RE = re.compile(r'&(?:#\d+|#x[\da-fA-F]+|[a-zA-Z]+);')
_BR_RE = re.compile(r'<br\s*/?>', re.IGNORECASE)
_P_RE = re.compile(r'</p>', re.IGNORECASE)
_LIST_ITEM_RE = re.compile(r'<li[^>]*>', re.IGNORECASE)
_HEADING_RE = re.compile(r'<h\d[^>]*>(.*?)</h\d>', re.IGNORECASE | re.DOTALL)

# 保留的格式化标签（用于部分保留场景）
_SAFE_TAGS = {'<b>', '<strong>', '<i>', '<em>', '<code>', '<pre>'}


def strip_html(text: str, preserve_formatting: bool = False) -> str:
    """
    从 HTML/RSS 内容中剔除标签，返回纯文本。

    Args:
        text: 含 HTML 标签的原始文本
        preserve_formatting: 是否保留 <b>/<i>/<code> 等格式化标签（用于 Markdown 渲染）

    Returns:
        清理后的纯文本
    """
    if not text:
        return ""

    # 快速路径：纯文本（无标签）
    if '<' not in text:
        return text.strip()

    # 1. 处理特殊标签 → 换行
    text = _BR_RE.sub('\n', text)
    text = _P_RE.sub('\n', text)
    text = _LIST_ITEM_RE.sub('\n• ', text)

    # 2. 处理标题 → 加粗
    if preserve_formatting:
        text = _HEADING_RE.sub(r'**\1**', text)

    # 3. 剔除剩余标签
    if preserve_formatting:
        # 保留安全标签
        for tag in _SAFE_TAGS:
            placeholder = f"__PRESERVE_{tag[1:-1].upper()}__"
            text = text.replace(tag, placeholder)
            text = text.replace(tag.replace('<', '</') + '>', placeholder)
        text = _HTML_TAG_RE.sub('', text)
        for tag in _SAFE_TAGS:
            placeholder = f"__PRESERVE_{tag[1:-1].upper()}__"
            markdown_tag = '**' if tag in {'<b>', '<strong>'} else '_'
            text = text.replace(placeholder, markdown_tag)
    else:
        text = _HTML_TAG_RE.sub('', text)

    # 4. 解码 HTML 实体
    text = html.unescape(text)

    # 5. 清理多余空白
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'[ \t]+', ' ', text)

    return text.strip()


# --------------------------------------------------------------------------
# 智能摘要提取
# --------------------------------------------------------------------------

def extract_snippet(
    text: str,
    max_length: int = 150,
    html_content: bool = True,
    ellipsis: str = "…",
) -> str:
    """
    从原始内容中提取原生摘要（Raw Snippet）。

    策略：
      1. 先清理 HTML（若 html_content=True）
      2. 在 max_length 附近寻找合适的断点（句子边界/空格/中文标点）
      3. 避免在汉字中间腰斩

    Args:
        text:       原始内容（可能含 HTML）
        max_length: 最大字符数
        html_content: 是否先清理 HTML
        ellipsis:   截断后缀（默认 "…"）

    Returns:
        智能截断的摘要文本
    """
    if not text:
        return ""

    if html_content:
        text = strip_html(text)

    if len(text) <= max_length:
        return text.strip()

    # 在 max_length 附近寻找最佳断点
    # 优先：中文句号/问号/感叹号
    # 其次：英文句号+空格/换行
    # 再次：空格
    # 最后：直接截断
    search_start = max(0, max_length - 30)
    search_end = max_length

    snippet = text[:max_length]

    # 尝试在中文标点处断句
    for i in range(len(snippet) - 1, search_start - 1, -1):
        if snippet[i] in '。！？；!?;':
            return snippet[:i + 1].strip() + ellipsis

    # 尝试在空格处断句
    for i in range(len(snippet) - 1, search_start - 1, -1):
        if snippet[i] == ' ':
            return snippet[:i].strip() + ellipsis

    # 尝试在中文词边界（非标点非汉字连续区的中间）
    for i in range(len(snippet) - 1, search_start - 1, -1):
        c = snippet[i]
        if '\u4e00' <= c <= '\u9fff':
            continue  # 跳过汉字
        if c.isalnum():
            continue  # 跳过英数字
        return snippet[:i].strip() + ellipsis

    # 直接截断
    return snippet.strip() + ellipsis


# --------------------------------------------------------------------------
# Markdown 安全渲染
# --------------------------------------------------------------------------

def safe_markdown_text(text: str) -> str:
    """
    将纯文本安全地嵌入 Markdown，转义特殊字符。
    注意：不转义已经在 **bold** 或 _italic_ 中的内容。
    """
    if not text:
        return ""

    # 转义 Markdown 特殊字符（但保留已有的格式化）
    # 简单策略：只转义行首的 # 和列表符号
    lines = text.split('\n')
    safe_lines = []
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith('#') and not stripped.startswith('##'):
            # 转义可能被误认为标题的 #
            line = line.replace('#', '\\#', 1)
        elif stripped.startswith(('-', '*', '+')) and len(stripped) > 1 and stripped[1] == ' ':
            # 转义可能被误认为列表的符号
            line = line[0] + '\\n' + line[1:]
        safe_lines.append(line)

    return '\n'.join(safe_lines)


# --------------------------------------------------------------------------
# 降级渲染辅助函数
# --------------------------------------------------------------------------

def render_raw_snippet(
    item: dict[str, Any],
    max_length: int = 150,
) -> str:
    """
    从原始抓取数据中提取并渲染原生摘要。

    优先级：
      1. description / content / selftext（RSS/Reddit）
      2. summary / abstract（论文）
      3. title 本身（兜底）

    Args:
        item:       原始抓取数据项
        max_length: 摘要最大长度

    Returns:
        格式化后的摘要文本（含来源标注）
    """
    # 尝试多个字段
    raw_text = ""
    for field in ('description', 'content', 'selftext', 'summary', 'abstract', 'content_snippet'):
        raw_text = item.get(field, "")
        if raw_text:
            break

    if not raw_text:
        return item.get("title", "(no title)")

    snippet = extract_snippet(raw_text, max_length)
    return snippet


def render_community_item_tier1(
    item: dict[str, Any],
    index: int,
    max_snippet: int = 120,
) -> str:
    """
    渲染社区简报 Tier 1 条目（一句话摘要）。

    格式：
      ### {index}. {title}
      > {snippet} · {source_count} 源 · 相关性 {score}/10
    """
    title = item.get("title", "(no title)")
    snippet = render_raw_snippet(item, max_snippet)
    source_count = item.get("source_count", item.get("item_count", 1))
    score = item.get("relevance_score", item.get("top_signal", 0))

    lines = [
        f"### {index}. {title}",
        f"> {snippet} · {source_count} 源 · 相关性 {score}/10",
        "",
    ]
    return "\n".join(lines)


def render_community_item_tier2(
    item: dict[str, Any],
    max_snippet: int = 200,
) -> str:
    """
    渲染社区简报 Tier 2 折叠块（<details>）。

    包含：完整原生摘要 + 来源列表 + 原始链接
    """
    raw_text = ""
    for field in ('description', 'content', 'selftext', 'summary'):
        raw_text = item.get(field, "")
        if raw_text:
            break

    if not raw_text:
        return ""

    # 清理 HTML 但保留基本格式
    clean_text = strip_html(raw_text, preserve_formatting=False)

    # 来源列表
    sources = item.get("sources", [])
    sources_text = ""
    if sources:
        source_lines = []
        for s in sources[:5]:
            s_title = s.get("title", "") or s.get("url", "")
            s_feed = s.get("feed", "")
            if s_title and s_feed:
                source_lines.append(f"- [{s_feed}] {s_title}")
            elif s_url := s.get("url", ""):
                source_lines.append(f"- {s_url}")
        if source_lines:
            sources_text = "\n**来源**：\n" + "\n".join(source_lines)

    # 原始链接
    url = item.get("url", "")
    link_text = f"\n🔗 [原文链接]({url})" if url else ""

    details_content = clean_text[:800] + sources_text + link_text
    if len(clean_text) > 800:
        details_content += "\n…（内容已截断）"

    return (
        "\n<details><summary>展开详情（完整摘要 + 来源）</summary>\n\n"
        + details_content
        + "\n\n</details>"
    )


# --------------------------------------------------------------------------
# 单元测试
# --------------------------------------------------------------------------

if __name__ == "__main__":
    # 测试用例
    test_html = """
    <p>这是一段<strong>加粗</strong>的测试文本。</p>
    <p>第二行内容，包含<a href="#">链接</a>和&nbsp;空格。</p>
    <br/>
    <ul><li>列表项1</li><li>列表项2</li></ul>
    """

    print("=== HTML 清理测试 ===")
    print(strip_html(test_html))
    print()
    print(strip_html(test_html, preserve_formatting=True))
    print()

    test_long = "这是一段很长的中文文本，包含多个句子。第一句结束了。第二句也结束了！第三句还没完，继续延伸下去以达到截断长度。第四句。"
    print("=== 智能摘要测试 ===")
    print(extract_snippet(test_long, max_length=50))
    print(extract_snippet(test_long, max_length=80))
    print(extract_snippet(test_long, max_length=150))
