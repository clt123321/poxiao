# 破晓 PoXiao - AI 原生驱动的个人情报系统

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/Skill-Ready-purple.svg" alt="Skill Ready">
</p>

<p align="center">
  <strong>不出门，可知天下事</strong><br>
  <sub>每天早晨自动生成学术/社区/财经三份高信噪比 Markdown 早报</sub>
</p>

---

## 🎯 Skill 化使用方式（Vibe Coding 平台）

破晓设计为 **Vibe Coding 平台的 Skill 模块**，可以通过自然语言触发：

### 触发方式

在支持 Skill 的 AI 编程助手（CodeFlicker、Claude Code、Cursor、Trae 等）中，直接发送：

```
/poxiao
```

或者更具体地：

```
/briefing --user demo
/poxiao --type academic
/deep_dive 2401.12345
```

### 完整命令参考

```bash
# 生成今日三份简报
python poxiao.py generate --user demo

# 仅生成学术简报（快速预览）
python poxiao.py generate --user demo --type academic --skip-llm

# 强制刷新数据（忽略缓存）
python poxiao.py generate --user demo --force-refresh

# 跳过 LLM，使用原生摘要（无需 API Key）
python poxiao.py generate --user demo --skip-llm
```

---

## 🤖 LLM 提供商支持（默认智谱 GLM）

破晓**默认使用智谱 GLM**，国内厂商优先，同时支持多种 LLM 提供商自动切换：

### 1. 智谱 AI（GLM）✓ 默认推荐
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
export DEEPSEEK_MODEL=deepseek-chat
```

### 5. Claude（Anthropic）
```bash
export ANTHROPIC_API_KEY=sk-ant-...
```

### 6. OpenAI
```bash
export OPENAI_API_KEY=sk-...
export OPENAI_BASE_URL=https://api.openai.com/v1
```

### 7. 本地 Ollama
```bash
export LOCAL_LLM_URL=http://localhost:11434/v1
export LOCAL_MODEL=llama3
```

### 零配置模式
如不配置任何 LLM Key，破晓将自动切换至**原生摘要模式**（无需 API Key），仍可生成基础简报。

---

## ✨ 核心特性

| 模块 | 能力 |
|------|------|
| 🎓 **学术简报** | arXiv + Semantic Scholar 混合检索，priority 加权评分，自动触发深读 |
| 🔥 **社区简报** | HackerNews + Reddit + RSS 聚合，话题聚类降噪，共识/争议提取 |
| 💰 **财经简报** | 融资/IPO/算力动态，三级公司名单过滤，AI 行业聚焦 |
| 🤖 **LLM 聚类** | OpenAI 兼容 API 驱动的话题聚类与摘要生成 |
| 🔄 **降级模式** | 无 LLM 时自动切换关键词过滤 + 原生摘要 |
| 🧠 **熔断器** | Semantic Scholar API 智能熔断，避免连环 429 限流 |
| 📦 **本地缓存** | SQLite 缓存论文数据，7 天 TTL，减少 API 调用 |

---

## 🚀 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/clt123321/poxiao.git
cd poxiao
```

### 2. 安装依赖

```bash
# 创建虚拟环境（推荐）
py -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate   # macOS/Linux

# 安装依赖
pip install -r requirements.txt
```

### 3. 配置用户

```bash
python poxiao.py setup
```

或使用默认 demo 用户（已有示例配置）直接运行：

```bash
python poxiao.py generate --user demo --skip-llm
```

### 4. 查看输出

生成的简报位于 `data/{username}/{date}/` 目录：

```
data/demo/2026-04-18/
├── demo的早报_学术概览_2026-04-18.md
├── demo的早报_社区速递_2026-04-18.md
├── demo的早报_财经简报_2026-04-18.md
└── demo的早报_今日索引_2026-04-18.md
```

---

## 🖥️ Vibe Coding 平台适配

### 支持的平台

| 平台 | 触发方式 | 配置文件 |
|------|---------|----------|
| **CodeFlicker / KwaiPilot** | `/poxiao`, `/briefing`, `/deep_dive` | `SKILL.md` |
| **Claude Code** | 自动识别 `SKILL.md` | `SKILL.md` |
| **Cursor** | 自动识别 `SKILL.md` | `SKILL.md` |
| **Trae** | 手动导入 | `SKILL.md` |

### 定时任务配置（CodeFlicker）

1. 打开 CodeFlicker 设置 → 定时任务
2. 添加新任务：
   - Prompt: `/briefing --days 1`
   - Cron: `0 9 * * 1-5`（工作日早 9 点）
   - 工作目录：项目根目录

### macOS launchd

```bash
python setup.py  # 选择 "launchd" 自动安装
```

---

## 📁 项目结构

```
poxiao/
├── poxiao.py              # 统一 CLI 入口
├── setup.py               # 交互式配置引导
├── config.json            # RSS/Reddit/HN 源配置
├── profile.yaml           # 用户兴趣画像模板
├── requirements.txt       # Python 依赖
├── SKILL.md               # Vibe Coding Skill 定义（核心！）
│
├── scripts/               # 核心脚本
│   ├── fetch.py           # 社区数据抓取
│   ├── search_papers.py   # 学术论文检索
│   ├── cluster_topics.py  # 话题聚类
│   ├── retry.py           # 重试装饰器 + 警告收集
│   ├── cache_manager.py   # SQLite 缓存 + S2 熔断器
│   ├── text_utils.py      # HTML 清理 + 摘要提取
│   └── path_utils.py      # 路径定义模块
│
├── .poxiao_system/        # 系统数据
│   └── profiles/          # 用户画像
│
└── data/                  # 输出数据（按用户/日期组织）
    └── {user}/
        └── {date}/
            ├── fetched.json
            ├── clustered.json
            ├── papers.json
            └── demo的早报_*.md
```

---

## 🎯 使用场景

| 用户类型 | 使用方式 |
|---------|---------|
| **研究者** | `/poxiao --type academic` 追踪 arXiv 最新论文 |
| **工程师** | `/poxiao --type community` 监控技术热点 |
| **投资人** | `/poxiao --type finance` 关注 AI 融资动态 |
| **产品经理** | `/poxiao` 获取每日三路简报 |

---

## 🔧 命令行参数

| 参数 | 用途 |
|------|------|
| `--user <name>` | 指定用户名（默认 demo） |
| `--type <type>` | 简报类型：`all`, `academic`, `community`, `finance` |
| `--days <N>` | 抓取时间窗口（默认周一3天，其他1天） |
| `--force-refresh` | 强制重新抓取，忽略缓存 |
| `--skip-llm` | 跳过 LLM，使用原生摘要（无需 API Key） |
| `--output <dir>` | 自定义输出目录 |

---

## 🔮 未来迭代方向

### 短期（V1.3）

- [ ] 多语言支持（英文简报选项）
- [ ] 邮件/微信推送集成
- [ ] Web UI 配置界面

### 中期（V2.0）

- [ ] 多模态内容支持（播客/视频摘要）
- [ ] 协作过滤推荐（基于相似用户）
- [ ] 自定义信源接入（Notion/飞书）

### 长期

- [ ] 本地 LLM 支持（Ollama/LM Studio）
- [ ] 知识图谱构建
- [ ] Agent 自主探索模式

---

## 🔑 SEO 关键词

`AI 早报` `个人情报系统` `LLM 聚类` `arXiv 监控` `HackerNews 聚合` `RSS 阅读器替代` `Vibe Coding` `Skill 系统` `CodeFlicker` `Claude Code` `Cursor` `知识管理` `信息过载` `自动化早报` `Semantic Scholar` `论文追踪` `技术情报`

---

## 🤝 参与贡献

欢迎二次开发！破晓采用 MIT 协议开源。

### 贡献方式

1. **Fork 仓库** → 创建你的分支
2. **添加新信源**：编辑 `config.json`，添加 RSS/API
3. **改进聚类算法**：修改 `scripts/cluster_topics.py`
4. **优化 UI 模板**：调整 Markdown 渲染逻辑
5. **提交 PR**：描述你的改进

### 开发指南

```bash
# 安装开发依赖
pip install -r requirements.txt
pip install pytest ruff mypy

# 运行测试
python -m pytest tests/

# 代码检查
ruff check scripts/
```

---

## 🙏 致谢

破晓的诞生离不开以下开源项目：

- [arXiv](https://arxiv.org/) — 开放学术预印本平台
- [Semantic Scholar](https://www.semanticschcholar.org/) — 学术论文知识图谱
- [Hacker News](https://news.ycombinator.com/) — 技术社区风向标
- [OpenAI API](https://openai.com/) — LLM 聚类引擎
- [httpx](https://www.python-httpx.org/) — 高性能异步 HTTP 客户端
- [feedparser](https://github.com/kurtmckee/feedparser) — RSS 解析利器

特别感谢 **CodeFlicker / KwaiPilot** 团队提供的 Vibe Coding 基础设施。

---

<p align="center">
  <strong>破晓 PoXiao — 让 AI 帮你看世界</strong><br>
  <sub>如果觉得有用，请给个 ⭐ Star 支持一下！</sub>
</p>
