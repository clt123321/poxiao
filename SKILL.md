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

  Vibe Coding 友好：支持多种 LLM 提供商，可通过环境变量一键切换。
---

# 破晓 PoXiao Skill

## 触发词

| 词 | 用途 |
|----|------|
| `/poxiao` | 等同于 `/briefing`，生成今日三份简报 |
| `/briefing` | 生成学术/社区/财经三份早报 |
| `/deep_dive <arxiv_id>` | 深度分析单篇论文 |

## 快速上手

```bash
# 首次使用：交互式配置
python poxiao.py setup

# 生成今日早报（使用 demo 用户）
python poxiao.py generate --user demo

# 仅生成学术简报
python poxiao.py generate --user demo --type academic

# 强制刷新数据（忽略缓存）
python poxiao.py generate --user demo --force-refresh

# 跳过 LLM，使用原生摘要（快速预览）
python poxiao.py generate --user demo --skip-llm
```

## LLM 配置（多提供商支持）

破晓默认使用**智谱 GLM**，国内厂商优先。自动检测环境变量，按优先级切换：

### 1. 智谱 AI（GLM）✓ 默认
```bash
export ZHIPU_API_KEY=sk-...
export ZHIPU_MODEL=glm-4-flash
```

### 2. MiniMax
```bash
export MINIMAX_API_KEY=sk-...
export MINIMAX_MODEL=MiniMax-Text-01
```

### 3. 火山引擎（字节）
```bash
export VOLC_API_KEY=sk-...
export VOLC_MODEL=doubao-pro-32k
```

### 4. DeepSeek
```bash
export DEEPSEEK_API_KEY=sk-...
```

### 5. Claude（Anthropic）
```bash
export ANTHROPIC_API_KEY=sk-ant-...
```

### 6. OpenAI
```bash
export OPENAI_API_KEY=sk-...
```

### 零配置模式
不配置任何 LLM Key 时，自动切换至**原生摘要模式**（无需 API Key）。

## 便利参数（Vibe Coding 优化）

| 参数 | 用途 |
|------|------|
| `--force-refresh` | 强制重新抓取，忽略缓存 |
| `--skip-llm` | 跳过 LLM 过滤，使用原生摘要快速预览 |
| `--output <dir>` | 自定义输出目录 |
| `--days <N>` | 设置抓取时间窗口（默认周一3天，其他1天） |

## 配置文件位置

| 类型 | 路径 |
|------|------|
| 用户画像 | `.poxiao_system/profiles/profile_{user}.yaml` |
| 原始数据 | `data/{user}/{date}/` |
| 输出简报 | `data/{user}/{date}/{display_name}的{类型}.md` |

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

未配置任何 LLM API 时：
- 学术简报：仅展示 arXiv 关键词匹配结果
- 社区简报：使用 TF-IDF 原生摘要
- 财经简报：简单过滤 category=finance

## 故障排查

| 症状 | 检查项 |
|------|--------|
| `未检测到任何 LLM API Key` | 确认环境变量或 .env 文件 |
| S2 API 429 限流 | 等待 1 小时或配置 `SEMANTIC_SCHOLAR_API_KEY` |
| 输出目录为空 | 检查网络连接，使用 `--skip-llm` 快速预览 |

## Scale 化使用

对于需要批量处理或 CI/CD 场景：

```bash
# 批量生成多个用户的早报
for user in demo example test; do
  python poxiao.py generate --user $user --skip-llm
done

# 无头模式（使用默认配置）
python poxiao.py setup --defaults
python poxiao.py generate --user default --force-refresh
```

---

**提示**：首次使用请运行 `python poxiao.py setup` 完成交互式配置。
