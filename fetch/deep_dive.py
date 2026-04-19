#!/usr/bin/env python3
"""
破晓 PoXiao V2.0 — 深读引擎 (The Deep Diver)
唯一职责：根据 arXiv ID 抓取论文全文/核心内容，输出 deep_context.md
"""
import os
import sys
import logging
import re
import asyncio
from pathlib import Path
from datetime import datetime, timezone

import httpx
import feedparser

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] [%(levelname)s] - %(message)s')
logger = logging.getLogger(__name__)

ARXIV_ABSTRACT_URL = "http://export.arxiv.org/api/query"
OUTPUT_DIR = Path("PoXiao_Briefs")
DEEP_CONTEXT_PATH = OUTPUT_DIR / "deep_context.md"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
}


def strip_html_tags(text):
    """清理 HTML 标签"""
    if not text:
        return ""
    text = re.sub(r'<[^>]+>', ' ', text)
    text = ' '.join(text.split())
    return text.strip()


async def fetch_arxiv_full_content(arxiv_id: str, http_client: httpx.AsyncClient) -> dict:
    """抓取 arXiv 论文的完整信息"""
    logger.info(f"开始抓取 arXiv 论文: {arxiv_id}")
    
    params = {
        "id_list": arxiv_id,
        "max_results": 1,
    }
    
    try:
        response = await http_client.get(
            ARXIV_ABSTRACT_URL,
            params=params,
            headers=HEADERS,
            timeout=30,
            follow_redirects=True
        )
        response.raise_for_status()
        feed = feedparser.parse(response.text)
        
        if not feed.entries:
            logger.error(f"未找到论文: {arxiv_id}")
            return None
        
        entry = feed.entries[0]
        
        paper_info = {
            "id": arxiv_id,
            "title": entry.get("title", "Untitled").replace("\n", " ").strip(),
            "authors": [a.get("name", "") for a in entry.get("authors", [])],
            "published": entry.get("published", ""),
            "updated": entry.get("updated", ""),
            "summary": entry.get("summary", "").strip(),
            "abstract": entry.get("summary", "").strip(),
            "link": entry.get("link", ""),
            "pdf_link": entry.get("link", "").replace("/abs/", "/pdf/") + ".pdf",
            "comment": entry.get("arxiv_comment", ""),
            "doi": entry.get("arxiv_doi", ""),
            "journal_ref": entry.get("arxiv_journal_ref", ""),
            "categories": [tag.get("term", "") for tag in entry.get("tags", [])],
        }
        
        logger.info(f"论文抓取成功: {paper_info['title'][:50]}...")
        return paper_info
        
    except httpx.TimeoutException:
        logger.error(f"请求超时: {arxiv_id}")
        return None
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP 错误 {e.response.status_code}: {arxiv_id}")
        return None
    except Exception as e:
        logger.error(f"抓取失败: {e}")
        return None


async def fetch_with_fallback(arxiv_id: str, http_client: httpx.AsyncClient) -> dict:
    """尝试多种方式获取论文信息"""
    paper_info = await fetch_arxiv_full_content(arxiv_id, http_client)
    
    if paper_info:
        return paper_info
    
    logger.warning(f"主方式失败，尝试备用方案: {arxiv_id}")
    
    return None


def format_deep_context(paper_info: dict) -> str:
    """格式化深读内容"""
    if not paper_info:
        return ""
    
    lines = []
    lines.append("# 破晓 PoXiao — 深度阅读上下文")
    lines.append(f"生成时间: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    lines.append("=" * 80)
    lines.append("")
    
    lines.append("## 📄 论文元数据")
    lines.append("")
    lines.append(f"**arXiv ID**: {paper_info['id']}")
    lines.append(f"**标题**: {paper_info['title']}")
    lines.append(f"**作者**: {', '.join(paper_info['authors']) if paper_info['authors'] else 'Unknown'}")
    lines.append(f"**发表时间**: {paper_info['published']}")
    if paper_info.get('categories'):
        lines.append(f"**分类**: {', '.join(paper_info['categories'])}")
    lines.append(f"**链接**: {paper_info['link']}")
    lines.append(f"**PDF**: {paper_info['pdf_link']}")
    if paper_info.get('doi'):
        lines.append(f"**DOI**: {paper_info['doi']}")
    if paper_info.get('journal_ref'):
        lines.append(f"**期刊引用**: {paper_info['journal_ref']}")
    if paper_info.get('comment'):
        lines.append(f"**评论**: {paper_info['comment']}")
    
    lines.append("")
    lines.append("## 📝 完整摘要")
    lines.append("")
    lines.append(strip_html_tags(paper_info['abstract']))
    
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*以下内容供深度分析使用*")
    lines.append("")
    
    return "\n".join(lines)


def write_deep_context(content: str, output_path: Path = None):
    """写入深读上下文文件"""
    if output_path is None:
        output_path = DEEP_CONTEXT_PATH
    
    try:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
        
        logger.info(f"深读上下文已写入: {output_path}")
        return True
    except Exception as e:
        logger.error(f"写入失败: {e}")
        return False


async def main(arxiv_id: str):
    """主函数"""
    if not arxiv_id:
        print("用法: python deep_dive.py <arXiv ID>")
        print("示例: python deep_dive.py 2604.14895")
        return
    
    arxiv_id = arxiv_id.strip()
    
    logger.info(f"深读任务启动 - arXiv ID: {arxiv_id}")
    
    proxy = os.environ.get("HTTP_PROXY") or os.environ.get("HTTPS_PROXY") or os.environ.get("ALL_PROXY")
    
    async with httpx.AsyncClient(timeout=60, proxy=proxy, trust_env=bool(proxy)) as http_client:
        paper_info = await fetch_with_fallback(arxiv_id, http_client)
    
    if not paper_info:
        logger.error(f"无法获取论文 {arxiv_id} 的信息")
        sys.exit(1)
    
    content = format_deep_context(paper_info)
    
    if write_deep_context(content):
        print(f"\n✅ 深读上下文已生成: {DEEP_CONTEXT_PATH}")
        print(f"📄 论文: {paper_info['title']}")
        print(f"🔗 链接: {paper_info['link']}")
    else:
        logger.error("深读上下文生成失败")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python deep_dive.py <arXiv ID>")
        print("示例: python deep_dive.py 2604.14895")
        sys.exit(1)
    
    arxiv_id = sys.argv[1]
    asyncio.run(main(arxiv_id))
