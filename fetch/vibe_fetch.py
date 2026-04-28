#!/usr/bin/env python3
"""
破晓 PoXiao V2.0 — 极简神经末梢 (The Fetcher)
唯一职责：极速获取"生肉"数据，输出纯文本 raw_context.md
"""
import os
import logging
from logging.handlers import RotatingFileHandler

# 绕过代理问题（某些环境下系统代理配置无效）
os.environ["no_proxy"] = "*"

import json
import re
import calendar
import feedparser
import httpx
import asyncio
import yaml
from pathlib import Path
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime

# 配置文件路径
CONFIG_PATH = Path("config.json")
OUTPUT_DIR = Path("briefs")
LOG_DIR = Path("logs")
PROFILE_DIR = Path("profiles")
DEFAULT_PROFILE = PROFILE_DIR / "profile_demo.yaml"

# HTML 标签清理正则
HTML_CLEAN_RE = re.compile(r'<[^>]+>')

# ========== 网络请求全局配置 ==========

# 1. 伪装层：真实浏览器 Header
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
}

# 2. 代理穿透层：读取环境变量
def get_proxy_dict():
    """读取代理环境变量，返回 proxies 字典"""
    proxy = os.environ.get("HTTP_PROXY") or os.environ.get("HTTPS_PROXY") or os.environ.get("ALL_PROXY")
    if proxy:
        logger.info(f"检测到代理配置: {proxy}")
        return {"http://": proxy, "https://": proxy}
    return None

# 3. 重试配置
MAX_RETRIES = 3
RETRY_DELAY = 2  # 秒

# 4. arXiv API 速率限制防护
ARXIV_REQUEST_DELAY = 5.0  # 每个关键词查询之间的固定延迟（秒）
ARXIV_BACKOFF_BASE = 10.0  # 429错误的指数退避基数（秒）
ARXIV_MAX_BACKOFF = 120.0  # 最大退避时间（秒）

# 配置日志
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
LOG_FORMAT = "[%(asctime)s] [%(levelname)s] [%(module)s] - %(message)s"

# 创建日志目录
LOG_DIR.mkdir(parents=True, exist_ok=True)

# 配置日志
logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)

# 控制台输出
console_handler = logging.StreamHandler()
console_handler.setLevel(LOG_LEVEL)
console_handler.setFormatter(logging.Formatter(LOG_FORMAT))
logger.addHandler(console_handler)

# 文件输出（按天滚动）
log_file = LOG_DIR / f"fetch_{datetime.now().strftime('%Y-%m-%d')}.log"
file_handler = RotatingFileHandler(
    log_file, maxBytes=10*1024*1024, backupCount=7, encoding="utf-8"
)
file_handler.setLevel(LOG_LEVEL)
file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
logger.addHandler(file_handler)


def strip_html_tags(text):
    """清理 HTML 标签"""
    if not text:
        return ""
    # 替换 HTML 标签为空格，然后清理多余的空格
    text = HTML_CLEAN_RE.sub(' ', text)
    # 清理多余的空格
    text = ' '.join(text.split())
    # 清理首尾空格
    return text.strip()


def load_config():
    """加载 config.json"""
    try:
        logger.info(f"加载配置文件: {CONFIG_PATH}")
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            config = json.load(f)
        logger.info("配置文件加载成功")
        return config
    except FileNotFoundError:
        logger.critical(f"配置文件不存在: {CONFIG_PATH}")
        raise
    except json.JSONDecodeError as e:
        logger.critical(f"配置文件格式错误: {e}")
        raise
    except Exception as e:
        logger.critical(f"加载配置文件时发生错误: {e}")
        raise


def load_user_profile(profile_path=DEFAULT_PROFILE):
    """加载用户品味配置"""
    try:
        logger.info(f"加载用户品味配置: {profile_path}")
        with open(profile_path, "r", encoding="utf-8") as f:
            profile = yaml.safe_load(f)
        logger.info("用户品味配置加载成功")
        return profile
    except FileNotFoundError:
        logger.warning(f"用户品味配置不存在: {profile_path}，使用默认配置")
        return {"research_domains": {}}
    except yaml.YAMLError as e:
        logger.warning(f"用户品味配置格式错误: {e}，使用默认配置")
        return {"research_domains": {}}
    except Exception as e:
        logger.warning(f"加载用户品味配置时发生错误: {e}，使用默认配置")
        return {"research_domains": {}}


async def fetch_all(config, since, http_client):
    all_items = []

    # 1. 抓取 RSS
    rss_sources = config.get("sources", {}).get("rss", [])
    for source in rss_sources:
        if source.get("enabled", True):
            items = await fetch_rss_source(source, since, http_client)
            all_items.extend(items)

    # 2. 抓取 HackerNews
    hn_config = config.get("sources", {}).get("hackernews", {})
    if hn_config.get("enabled", False):
        count = hn_config.get("fetch_top_stories", 15)
        items = await fetch_hackernews(since, count, http_client)
        all_items.extend(items)

    # 3. 抓取 GitHub
    github_sources = config.get("sources", {}).get("github", [])
    items = await fetch_github_releases(github_sources, since, http_client)
    all_items.extend(items)

    # 4. 抓取 arXiv
    arxiv_config = config.get("sources", {}).get("arxiv", {})
    if arxiv_config.get("enabled", False):
        # 从用户品味配置中读取关键词
        profile = load_user_profile()
        research_domains = profile.get("research_domains", {})
        
        # 提取所有关键词
        keywords = []
        for domain, domain_config in research_domains.items():
            domain_keywords = domain_config.get("keywords", [])
            keywords.extend(domain_keywords)
        
        # 如果没有从用户品味中获取到关键词，使用默认关键词
        if not keywords:
            keywords = arxiv_config.get("keywords", ["LLM", "RLHF", "alignment", "transformer", "vLLM"])
        
        categories = arxiv_config.get("categories", ["cs.AI", "cs.LG", "cs.CL"])
        items = await fetch_arxiv_papers(categories, keywords, since, http_client)
        all_items.extend(items)

    return all_items


async def fetch_rss_source(source, since, http_client):
    """抓取单个 RSS 源（带重试机制）"""
    items = []
    source_name = source.get("name", "unknown")
    source_url = source.get("url", "")
    
    for attempt in range(MAX_RETRIES):
        try:
            logger.info(f"开始抓取 RSS 源: {source_name} ({source_url}) [尝试 {attempt + 1}/{MAX_RETRIES}]")
            response = await http_client.get(
                source["url"], 
                headers=HEADERS,
                follow_redirects=True, 
                timeout=15
            )
            response.raise_for_status()
            feed = feedparser.parse(response.text)
            
            logger.info(f"解析 RSS 源成功: {source_name} - 找到 {len(feed.entries)} 条条目")
            logger.info(f"过滤时间: {since}")

            for entry in feed.entries:
                published_at = _parse_rss_date(entry)
                if not published_at or published_at < since:
                    continue

                title = entry.get("title", "Untitled")
                url = entry.get("link", source["url"])
                summary = _extract_rss_summary(entry)

                items.append(f"[RSS:{source['name']}]\n{title}\n{url}\n{summary}")
            logger.info(f"RSS 源抓取成功: {source_name} - 找到 {len(items)} 条新内容")
            return items  # 成功，直接返回
        except httpx.TimeoutException as e:
            logger.warning(f"[ERROR] RSS 源 {source_name} 超时 (尝试 {attempt + 1}/{MAX_RETRIES}): {e}")
            if attempt < MAX_RETRIES - 1:
                logger.info(f"等待 {RETRY_DELAY} 秒后重试...")
                await asyncio.sleep(RETRY_DELAY)
        except httpx.HTTPStatusError as e:
            if e.response.status_code in (403, 404, 410):
                logger.error(f"[ERROR] RSS 源 {source_name} 返回致命错误 {e.response.status_code}，跳过此源")
                return items  # 致命错误，不重试
            logger.warning(f"[ERROR] RSS 源 {source_name} HTTP 错误 (尝试 {attempt + 1}/{MAX_RETRIES}): {e}")
            if attempt < MAX_RETRIES - 1:
                logger.info(f"等待 {RETRY_DELAY} 秒后重试...")
                await asyncio.sleep(RETRY_DELAY)
        except httpx.HTTPError as e:
            logger.warning(f"[ERROR] RSS 源 {source_name} 请求失败 (尝试 {attempt + 1}/{MAX_RETRIES}): {e}")
            if attempt < MAX_RETRIES - 1:
                logger.info(f"等待 {RETRY_DELAY} 秒后重试...")
                await asyncio.sleep(RETRY_DELAY)
        except Exception as e:
            logger.error(f"[ERROR] RSS 源 {source_name} 处理失败: {e}")
            return items  # 其他异常，不重试
    
    logger.error(f"[ERROR] RSS 源 {source_name} 连续 {MAX_RETRIES} 次失败，已跳过")
    return items


def _parse_rss_date(entry):
    """解析 RSS 日期"""
    for field in ("published", "updated", "created"):
        if field in entry:
            try:
                parsed_field = f"{field}_parsed"
                if parsed_field in entry and entry[parsed_field]:
                    return datetime.fromtimestamp(calendar.timegm(entry[parsed_field]), tz=timezone.utc)
                return parsedate_to_datetime(entry[field])
            except Exception:
                continue
    return None


def _extract_rss_summary(entry):
    """提取 RSS 摘要，清理 HTML 并截断"""
    content = ""
    if "summary" in entry:
        content = entry.summary
    elif "description" in entry:
        content = entry.description
    elif "content" in entry and entry.content:
        content = entry.content[0].get("value", "")

    content = strip_html_tags(content)
    return content[:300]


async def fetch_hackernews(since, count, http_client):
    """抓取 HackerNews（带重试机制）"""
    items = []
    
    for attempt in range(MAX_RETRIES):
        try:
            logger.info(f"开始抓取 HackerNews - 前 {count} 条故事 [尝试 {attempt + 1}/{MAX_RETRIES}]")
            base_url = "https://hacker-news.firebaseio.com/v0"
            response = await http_client.get(f"{base_url}/topstories.json", headers=HEADERS, timeout=15)
            response.raise_for_status()
            story_ids = response.json()[:count]

            # 并发获取故事详情
            tasks = []
            for sid in story_ids:
                tasks.append(http_client.get(f"{base_url}/item/{sid}.json", headers=HEADERS, timeout=15))
            story_responses = await asyncio.gather(*tasks, return_exceptions=True)

            for resp in story_responses:
                if isinstance(resp, Exception) or not resp:
                    continue
                try:
                    # 检查 resp 是否已经是字典（可能是直接返回的 JSON）
                    if isinstance(resp, dict):
                        story = resp
                    else:
                        # 正常的 HTTP 响应对象
                        story = resp.json()
                    published_at = datetime.fromtimestamp(story.get("time", 0), tz=timezone.utc)
                    if published_at < since:
                        continue

                    title = story.get("title", "Untitled")
                    url = story.get("url", f"https://news.ycombinator.com/item?id={story.get('id', '')}")
                    score = story.get("score", 0)
                    descendants = story.get("descendants", 0)

                    items.append(
                        f"[HACKERNEWS]\n{title}\n{url}\n"
                        f"Score: {score} | Comments: {descendants}"
                    )
                except Exception as e:
                    logger.error(f"处理 HackerNews 条目失败: {e}")
                    continue

            logger.info(f"HackerNews 抓取成功 - 找到 {len(items)} 条新内容")
            return items  # 成功，直接返回
        except httpx.TimeoutException as e:
            logger.warning(f"[ERROR] HackerNews 超时 (尝试 {attempt + 1}/{MAX_RETRIES}): {e}")
            if attempt < MAX_RETRIES - 1:
                logger.info(f"等待 {RETRY_DELAY} 秒后重试...")
                await asyncio.sleep(RETRY_DELAY)
        except httpx.HTTPStatusError as e:
            if e.response.status_code in (403, 404, 410):
                logger.error(f"[ERROR] HackerNews 返回致命错误 {e.response.status_code}，跳过")
                return items
            logger.warning(f"[ERROR] HackerNews HTTP 错误 (尝试 {attempt + 1}/{MAX_RETRIES}): {e}")
            if attempt < MAX_RETRIES - 1:
                logger.info(f"等待 {RETRY_DELAY} 秒后重试...")
                await asyncio.sleep(RETRY_DELAY)
        except Exception as e:
            logger.error(f"[ERROR] HackerNews 请求失败: {e}")
            if attempt < MAX_RETRIES - 1:
                logger.info(f"等待 {RETRY_DELAY} 秒后重试...")
                await asyncio.sleep(RETRY_DELAY)
    
    logger.error(f"[ERROR] HackerNews 连续 {MAX_RETRIES} 次失败，已跳过")
    return items


async def fetch_github_releases(sources, since, http_client):
    """抓取 GitHub releases"""
    items = []
    try:
        logger.info(f"开始抓取 GitHub releases - 共 {len(sources)} 个仓库")
        base_url = "https://api.github.com"
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "PoXiao-Vibe-Fetcher"
        }
        # 可选：使用 GITHUB_TOKEN 环境变量
        token = os.getenv("GITHUB_TOKEN")
        if token:
            headers["Authorization"] = f"token {token}"

        for source in sources:
            if not source.get("enabled", True):
                continue
            owner = source.get("owner")
            repo = source.get("repo")
            if not owner or not repo:
                continue

            try:
                logger.info(f"开始抓取 GitHub 仓库: {owner}/{repo}")
                url = f"{base_url}/repos/{owner}/{repo}/releases"
                response = await http_client.get(url, headers=headers, follow_redirects=True)
                response.raise_for_status()
                releases = response.json()

                for release in releases:
                    published_str = release.get("published_at", "")
                    try:
                        published = datetime.fromisoformat(published_str.replace("Z", "+00:00"))
                    except Exception:
                        published = None

                    if not published or published < since:
                        continue

                    tag = release.get("tag_name", "")
                    title = f"{owner}/{repo} released {tag}"
                    url = release.get("html_url", "")
                    body = strip_html_tags(release.get("body", "")).strip()[:300]
                    author = release.get("author", {}).get("login", "unknown")

                    items.append(
                        f"[GITHUB]\n{title}\n{url}\n"
                        f"Author: {author}\n{body}"
                    )
                logger.info(f"GitHub 仓库抓取成功: {owner}/{repo} - 找到 {len(items)} 条新内容")
            except httpx.HTTPError as e:
                logger.error(f"GitHub {owner}/{repo} 抓取失败: {e}")
            except Exception as e:
                logger.error(f"GitHub {owner}/{repo} 处理失败: {e}")

        logger.info(f"GitHub releases 抓取完成 - 共找到 {len(items)} 条新内容")
    except Exception as e:
        logger.error(f"GitHub releases 整体处理失败: {e}")

    return items


async def fetch_arxiv_papers(categories, keywords, since, http_client):
    """抓取 arXiv 论文元数据，带速率限制防护"""
    items = []
    consecutive_429s = 0  # 连续429计数
    
    try:
        logger.info(f"开始抓取 arXiv 论文 - 分类: {categories}, 关键词数量: {len(keywords)}")
        
        # 为每个关键词单独查询
        for idx, keyword in enumerate(keywords):
            logger.info(f"正在查询关键词 [{idx+1}/{len(keywords)}]: {keyword}")
            
            # 关键词之间的固定延迟（第一个关键词不延迟）
            if idx > 0:
                delay = ARXIV_REQUEST_DELAY
                # 如果之前有连续429，增加延迟
                if consecutive_429s > 0:
                    delay = min(ARXIV_BACKOFF_BASE * (2 ** consecutive_429s), ARXIV_MAX_BACKOFF)
                    logger.info(f"检测到之前有{consecutive_429s}次429，增加延迟至 {delay:.1f} 秒")
                logger.debug(f"等待 {delay:.1f} 秒后查询下一个关键词...")
                await asyncio.sleep(delay)
            
            # 构建查询参数
            query_parts = []
            if categories:
                query_parts.append(f"cat:({' OR '.join(categories)})")
            query_parts.append(f"all:{keyword}")
            
            query = " AND ".join(query_parts)
            params = {
                "search_query": query,
                "start": 0,
                "max_results": 5,  # 每个关键词最多抓取5篇
                "sortBy": "submittedDate",  # 按提交日期排序
                "sortOrder": "descending"
            }

            url = "http://export.arxiv.org/api/query"
            
            # 添加重试机制
            for attempt in range(MAX_RETRIES):
                try:
                    response = await http_client.get(url, params=params, follow_redirects=True, timeout=15)
                    response.raise_for_status()
                    feed = feedparser.parse(response.text)
                    
                    logger.info(f"关键词 {keyword} 找到 {len(feed.entries)} 篇论文")
                    
                    # 收集符合条件的论文
                    keyword_items = []
                    for entry in feed.entries:
                        published_str = entry.get("published", "")
                        try:
                            published = datetime.fromisoformat(published_str.replace("Z", "+00:00"))
                            logger.debug(f"论文发布时间: {published}, 过滤时间: {since}")
                            logger.debug(f"是否在过滤时间之后: {published >= since}")
                        except Exception as e:
                            logger.warning(f"解析发布时间失败: {e}, 时间字符串: {published_str}")
                            published = None

                        # 只收集在过滤时间之后的论文
                        if published and published >= since:
                            title = entry.get("title", "Untitled").replace("\n", " ").strip()
                            link = entry.get("link", "https://arxiv.org")
                            summary = strip_html_tags(entry.get("summary", "")).strip()  # 保留完整摘要
                            authors = [a.get("name", "") for a in entry.get("authors", [])]
                            authors_str = ", ".join(authors) if authors else "Unknown"
                            
                            # 构建格式化的条目
                            item = f"[ACADEMIC - ARXIV]\n"
                            item += f"标题: {title}\n"
                            item += f"作者: {authors_str}\n"
                            item += f"链接: {link}\n"
                            item += f"完整摘要: {summary}\n"
                            item += f"匹配关键词: {keyword}"
                            
                            keyword_items.append(item)
                    
                    # 如果没有符合时间条件的论文，收集前5篇最新的
                    if not keyword_items and feed.entries:
                        logger.info(f"关键词 {keyword} 没有找到最近48小时的论文，收集前5篇最新的")
                        for i, entry in enumerate(feed.entries[:5]):
                            title = entry.get("title", "Untitled").replace("\n", " ").strip()
                            link = entry.get("link", "https://arxiv.org")
                            summary = strip_html_tags(entry.get("summary", "")).strip()  # 保留完整摘要
                            authors = [a.get("name", "") for a in entry.get("authors", [])]
                            authors_str = ", ".join(authors) if authors else "Unknown"
                            
                            # 构建格式化的条目
                            item = f"[ACADEMIC - ARXIV]\n"
                            item += f"标题: {title}\n"
                            item += f"作者: {authors_str}\n"
                            item += f"链接: {link}\n"
                            item += f"完整摘要: {summary}\n"
                            item += f"匹配关键词: {keyword}"
                            
                            keyword_items.append(item)
                    
                    # 限制每个关键词最多5篇
                    keyword_items = keyword_items[:5]
                    
                    # 添加到总列表
                    items.extend(keyword_items)
                    
                    # 成功获取后重置429计数
                    consecutive_429s = 0
                    # 成功获取后跳出重试循环
                    break
                except httpx.TimeoutException as e:
                    logger.warning(f"[ERROR] arXiv API 超时 (尝试 {attempt + 1}/{MAX_RETRIES}): {e}")
                    if attempt < MAX_RETRIES - 1:
                        logger.info(f"等待 {RETRY_DELAY} 秒后重试...")
                        await asyncio.sleep(RETRY_DELAY)
                except httpx.HTTPStatusError as e:
                    if e.response.status_code == 429:
                        # 429 Too Many Requests - 速率限制
                        consecutive_429s += 1
                        backoff_time = min(ARXIV_BACKOFF_BASE * (2 ** consecutive_429s), ARXIV_MAX_BACKOFF)
                        logger.warning(f"[429] arXiv API 速率限制 (连续第{consecutive_429s}次)，等待 {backoff_time:.1f} 秒后重试...")
                        if attempt < MAX_RETRIES - 1:
                            await asyncio.sleep(backoff_time)
                            continue
                        else:
                            logger.error(f"关键词 {keyword} 重试{MAX_RETRIES}次后仍被限流，跳过")
                            break
                    elif e.response.status_code in (403, 404, 410):
                        logger.error(f"[ERROR] arXiv API 返回致命错误 {e.response.status_code}，跳过此关键词")
                        break
                    else:
                        consecutive_429s = 0  # 重置429计数
                        logger.warning(f"[ERROR] arXiv API HTTP 错误 (尝试 {attempt + 1}/{MAX_RETRIES}): {e}")
                        if attempt < MAX_RETRIES - 1:
                            logger.info(f"等待 {RETRY_DELAY} 秒后重试...")
                            await asyncio.sleep(RETRY_DELAY)
                except Exception as e:
                    logger.error(f"[ERROR] 处理关键词 {keyword} 时发生错误: {e}")
                    break

        logger.info(f"arXiv 论文抓取成功 - 找到 {len(items)} 条新内容")
    except Exception as e:
        logger.error(f"arXiv 整体处理失败: {e}")

    return items


def write_raw_context(all_items, output_path):
    """扁平化输出到 raw_context.md"""
    try:
        logger.info(f"开始写入原始数据到: {output_path}")
        output_path.parent.mkdir(parents=True, exist_ok=True)

        content = "# 破晓 PoXiao — 原始数据 (Raw Context)\n"
        content += f"生成时间: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}\n"
        content += "=" * 80 + "\n\n"

        for item in all_items:
            content += item + "\n---\n\n"

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)

        logger.info(f"生肉数据已写入: {output_path} - 共 {len(all_items)} 条内容")
    except Exception as e:
        logger.critical(f"写入原始数据失败: {e}")
        raise


async def main(days=2):
    try:
        logger.info(f"开始执行数据抓取任务 - 抓取最近 {days} 天的内容")
        config = load_config()
        
        date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        date_dir = OUTPUT_DIR / date_str
        date_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"输出目录已创建: {date_dir}")

        since = datetime.now(timezone.utc) - timedelta(days=days)
        
        proxy = os.environ.get("HTTP_PROXY") or os.environ.get("HTTPS_PROXY") or os.environ.get("ALL_PROXY")
        if proxy:
            logger.info(f"检测到代理配置: {proxy}")
        else:
            logger.info("未检测到代理配置，使用直连模式")
        
        async with httpx.AsyncClient(timeout=30, proxy=proxy, trust_env=bool(proxy)) as http_client:
            all_items = await fetch_all(config, since, http_client)

        write_raw_context(all_items, date_dir / "raw_context.md")
        logger.info(f"数据抓取任务完成 - 共抓取 {len(all_items)} 条内容")
    except Exception as e:
        logger.critical(f"执行数据抓取任务时发生错误: {e}")
        raise


if __name__ == "__main__":
    import sys

    days = 1
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        days = int(sys.argv[1])

    asyncio.run(main(days=days))
