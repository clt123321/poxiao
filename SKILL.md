---
name: poxiao
description: |
  破晓 PoXiao — AI 原生驱动的个人情报系统。
  
  每天早晨自动抓取学术、社区、财经三路信源，经 LLM 聚类降噪后生成高信噪比 Markdown 早报。
  
  核心能力：
  - 学术：arXiv + Semantic Scholar 混合检索，priority 加权，自动触发深读
  - 社区：HackerNews + Reddit + RSS 聚合，话题聚类，共识/争议提取
  - 财经：融资/IPO/算力动态，三级公司名单过滤
  
  触发词：/poxiao, /briefing, /deep_dive
---

# 破晓 PoXiao Skill

## 触发词

| 词 | 用途 |
|----|------|
| `/poxiao` | 等同于 `/briefing`，生成今日三份简报 |
| `/briefing` | 生成学术/社区/财经三份早报 |
| `/deep_dive <arxiv_id>` | 深度分析单篇论文（调用 paper-analyze） |

## 快速上手

```bash
# 首次使用：配置用户 + API Key
python poxiao.py setup

# 生成今日早报
python poxiao.py generate --user andy

# 仅生成学术简报
python poxiao.py generate --user andy --type academic

# 深度分析论文
python poxiao.py analyze 2401.12345 --user andy
```

## 环境要求

### 必需
- Python 3.10+
- `.env` 文件（含 `OPENAI_API_KEY`）

### 可选增强
- `OPENAI_BASE_URL` — API 代理地址
- `SEMANTIC_SCHOLAR_API_KEY` — 提升并发额度

## 配置文件位置

| 类型 | 路径 |
|------|------|
| 用户画像 | `.poxiao_system/profiles/profile_{user}.yaml` |
| 原始数据 | `.poxiao_system/raw/{date}/` |
| 输出简报 | `PoXiao_Briefs/{date}_{display_name}的{类型}.md` |

## 工作流程

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   fetch.py  │────▶│ cluster.py  │────▶│  LLM Filter │
│  社区抓取   │     │  话题聚类    │     │  降噪摘要   │
└─────────────┘     └─────────────┘     └─────────────┘
       │                                         │
       ▼                                         ▼
┌─────────────┐                          ┌─────────────┐
│search_papers│                          │  Markdown   │
│  学术检索   │                          │   渲染     │
└─────────────┘                          └─────────────┘
```

## 降级模式

未配置 `OPENAI_API_KEY` 时：
- 学术简报：仅展示 arXiv 关键词匹配结果
- 社区简报：使用 TF-IDF 原生摘要
- 财经简报：简单过滤 category=finance

## 定时任务

```bash
# macOS launchd（推荐）
python poxiao.py setup  # 自动安装

# 手动安装
cp .poxiao_system/schedules/*.plist ~/Library/LaunchAgents/
launchctl load -w ~/Library/LaunchAgents/com.poxiao.briefing.*.plist
```

## 故障排查

| 症状 | 检查项 |
|------|--------|
| `OPENAI_API_KEY 未设置` | 确认 `.env` 文件存在且格式正确 |
| S2 API 429 限流 | 等待 1 小时或配置 `SEMANTIC_SCHOLAR_API_KEY` |
| 输出目录为空 | 检查 `PoXiao_Briefs/` 权限 |

---

**提示**：首次使用请运行 `python poxiao.py setup` 完成交互式配置。
