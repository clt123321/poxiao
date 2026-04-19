#!/usr/bin/env python3
"""信源连通性诊断工具"""
import asyncio
import time
from pathlib import Path
import httpx
import yaml

CONFIG_PATH = Path("config.json")

async def test_url(client, url, name, src_type):
    if not url:
        return {"source_type": src_type, "name": name, "status": "error", "message": "URL为空"}
    try:
        start = time.time()
        resp = await client.get(url, follow_redirects=True, timeout=15.0)
        elapsed = (time.time() - start) * 1000
        if resp.status_code == 200:
            return {"source_type": src_type, "name": name, "status": "ok", "message": f"HTTP 200 | {len(resp.content)} bytes | {elapsed:.0f}ms"}
        elif resp.status_code == 403:
            return {"source_type": src_type, "name": name, "status": "blocked", "message": "HTTP 403"}
        else:
            return {"source_type": src_type, "name": name, "status": "error", "message": f"HTTP {resp.status_code}"}
    except httpx.TimeoutException:
        return {"source_type": src_type, "name": name, "status": "timeout", "message": "超时 15s"}
    except Exception as e:
        return {"source_type": src_type, "name": name, "status": "network", "message": f"错误: {str(e)[:50]}"}

async def main():
    with open(CONFIG_PATH, encoding="utf-8") as f:
        config = yaml.safe_load(f)
    sources = config.get("sources", {})
    results = []
    async with httpx.AsyncClient(trust_env=False) as client:
        for src in sources.get("github", []):
            if not src.get("enabled", True):
                results.append({"source_type": "github", "name": f"github/{src.get('owner')}/{src.get('repo')}", "status": "disabled", "message": "已禁用"})
                continue
            url = f"https://api.github.com/repos/{src['owner']}/{src['repo']}/releases"
            results.append(await test_url(client, url, f"github/{src.get('owner')}/{src.get('repo')}", "github"))
        hn = sources.get("hackernews", {})
        if hn.get("enabled"):
            results.append(await test_url(client, "https://hacker-news.firebaseio.com/v0/topstories.json", "HackerNews", "hackernews"))
        else:
            results.append({"source_type": "hackernews", "name": "HackerNews", "status": "disabled", "message": "已禁用"})
        for src in sources.get("rss", []):
            if not src.get("enabled", True):
                results.append({"source_type": "rss", "name": src.get("name", "RSS"), "status": "disabled", "message": "已禁用"})
                continue
            results.append(await test_url(client, src.get("url", ""), src.get("name", "RSS"), "rss"))
        for src in sources.get("aggregators", []):
            if not src.get("enabled", True):
                results.append({"source_type": "aggregator", "name": src.get("name", "聚合源"), "status": "disabled", "message": "已禁用"})
                continue
            results.append(await test_url(client, src.get("url", ""), src.get("name", "聚合源"), "aggregator"))
        reddit = sources.get("reddit", {})
        if reddit.get("enabled"):
            for sub in reddit.get("subreddits", []):
                name = f"Reddit/{sub.get('subreddit', '')}"
                if not sub.get("enabled", True):
                    results.append({"source_type": "reddit", "name": name, "status": "disabled", "message": "已禁用"})
                    continue
                url = f"https://www.reddit.com/r/{sub.get('subreddit', '')}/hot.json?limit=1"
                results.append(await test_url(client, url, name, "reddit"))
        else:
            results.append({"source_type": "reddit", "name": "Reddit", "status": "disabled", "message": "已禁用"})
        for src in sources.get("telegram", []):
            if not src.get("enabled", True):
                results.append({"source_type": "telegram", "name": src.get("name", "Telegram"), "status": "disabled", "message": "已禁用"})
                continue
            results.append(await test_url(client, src.get("url", ""), src.get("name", "Telegram"), "telegram"))

    # Write to diag_result.txt in current directory
    OUTPUT = Path("diag_result.txt")
    labels = {"ok": "[OK]", "disabled": "[DIS]", "error": "[ERR]", "blocked": "[BLK]", "timeout": "[TMO]", "network": "[NET]"}
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(f"Source Diagnostic Report\n")
        f.write(f"Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total sources: {len(results)}\n\n")
        current_type = None
        for r in results:
            if r["source_type"] != current_type:
                f.write(f"\n=== {r['source_type'].upper()} ===\n")
                current_type = r["source_type"]
            icon = labels.get(r["status"], "[?]")
            f.write(f"{icon} {r['name']} - {r['message']}\n")
    print(f"Done. {len(results)} sources tested. Results in {OUTPUT}")

if __name__ == "__main__":
    asyncio.run(main())
