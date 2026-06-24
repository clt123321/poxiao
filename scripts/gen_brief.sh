#!/bin/bash
# 破晓日报一键生成脚本
# 用法: bash scripts/gen_brief.sh [YYYY-MM-DD]

set -e
SCRIPT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$SCRIPT_DIR"

DATE="${1:-$(date +%Y-%m-%d)}"
YM="${DATE:0:7}"
DATE_DIR="briefs/$YM/$DATE"
RAW_FILE="$DATE_DIR/raw_context-$DATE.md"
BRIEF_FILE="$DATE_DIR/早报-$DATE.md"
LOG_FILE="/tmp/fetch_${DATE//-/}.log"

echo "[gen_brief] 日期: $DATE"
mkdir -p "$DATE_DIR"

# 1. 后台启动 fetch（不等待）
if [ ! -f "$RAW_FILE" ]; then
  echo "[gen_brief] 启动后台 fetch..."
  python3 fetch/vibe_fetch.py > "$LOG_FILE" 2>&1 &
  FETCH_PID=$!
  echo "[gen_brief] fetch PID=$FETCH_PID，继续获取实时数据..."
fi

# 2. 获取 HN top stories
echo "[gen_brief] 获取 HackerNews 数据..."
python3 - <<'EOF' > /tmp/hn_data.json
import httpx, json, sys
try:
    top = json.loads(httpx.get('https://hacker-news.firebaseio.com/v0/topstories.json', timeout=10).text)[:30]
    results = []
    for item_id in top:
        try:
            item = json.loads(httpx.get(f'https://hacker-news.firebaseio.com/v0/item/{item_id}.json', timeout=5).text)
            results.append({"title": item.get("title",""), "url": item.get("url",""), "score": item.get("score",0), "id": item_id})
        except: pass
    results.sort(key=lambda x: x["score"], reverse=True)
    print(json.dumps(results[:20], ensure_ascii=False))
except Exception as e:
    print("[]")
    sys.stderr.write(str(e))
EOF

# 3. 获取 HF Daily Papers
echo "[gen_brief] 获取 HuggingFace Daily Papers..."
python3 - <<'EOF' > /tmp/hf_papers.json
import httpx, json, sys
from datetime import datetime, timedelta
try:
    # 尝试今天和昨天
    for delta in [0, 1]:
        d = (datetime.utcnow() - timedelta(days=delta)).strftime("%Y-%m-%d")
        r = httpx.get(f'https://huggingface.co/api/daily_papers?date={d}', timeout=15)
        papers = json.loads(r.text)
        if papers:
            result = []
            for p in papers[:15]:
                paper = p.get("paper", {})
                result.append({
                    "title": paper.get("title",""),
                    "arxiv": f"https://arxiv.org/abs/{paper.get('id','')}",
                    "authors": [a.get("name","") for a in paper.get("authors",[])[:3]],
                    "summary": paper.get("summary","")[:400]
                })
            print(json.dumps(result, ensure_ascii=False))
            break
    else:
        print("[]")
except Exception as e:
    print("[]")
    sys.stderr.write(str(e))
EOF

# 4. 获取 Reddit LocalLLaMA
echo "[gen_brief] 获取 Reddit 数据..."
python3 - <<'EOF' > /tmp/reddit_data.json
import feedparser, json, re, sys
try:
    feed = feedparser.parse('https://www.reddit.com/r/LocalLLaMA/hot.rss')
    results = []
    for e in feed.entries[:20]:
        results.append({"title": e.get("title",""), "link": e.get("link","")})
    print(json.dumps(results, ensure_ascii=False))
except Exception as e:
    print("[]")
    sys.stderr.write(str(e))
EOF

# 5. 输出数据摘要供 Agent 使用
echo ""
echo "=== HackerNews TOP 15 ==="
python3 -c "
import json
data = json.load(open('/tmp/hn_data.json'))
for item in data[:15]:
    print(f\"[{item['score']}] {item['title']} | {item['url']}\")
"

echo ""
echo "=== HuggingFace Papers TOP 10 ==="
python3 -c "
import json
data = json.load(open('/tmp/hf_papers.json'))
for p in data[:10]:
    print(f\"### {p['title']}\")
    print(f\"  arxiv: {p['arxiv']}\")
    print(f\"  authors: {p['authors']}\")
    print(f\"  summary: {p['summary'][:250]}\")
    print()
"

echo ""
echo "=== Reddit LocalLLaMA TOP 15 ==="
python3 -c "
import json
data = json.load(open('/tmp/reddit_data.json'))
for p in data[:15]:
    print(f\"  {p['title']} | {p['link']}\")
"

echo ""
echo "[gen_brief] 数据获取完成。请基于以上数据生成早报并保存到: $BRIEF_FILE"
echo "[gen_brief] 生成后执行: git add $DATE_DIR && git commit -m 'feat: add $DATE daily briefing' && git push origin main"
