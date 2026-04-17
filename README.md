# 破晓 PoXiao - AI 原生驱动的个人情报系统

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/Vibe%20Coding-Ready-purple.svg" alt="Vibe Coding">
</p>

<p align="center">
  <strong>不出门，可知天下事</strong><br>
  <sub>每天早晨自动生成学术/社区/财经三份高信噪比 Markdown 早报</sub>
</p>

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
pip install -r requirements.txt
```

### 3. 配置 LLM（可选但推荐）

创建 `.env` 文件：

```env
OPENAI_API_KEY=sk-...
OPENAI_BASE_URL=https://api.openai.com/v1  # 可选，代理地址
```

> 未配置时自动降级为关键词模式（效果较差）

### 4. 运行配置引导

```bash
python setup.py
```

按提示输入：
- 用户名（如 `andy`）
- 显示名称（如 `Andy`）
- 研究领域（多选）
- 商业关注面（多选）
- 是否创建 `.env` 文件
- 定时任务方式

### 5. 生成早报

```bash
python poxiao.py generate --user andy
```

输出位置：`PoXiao_Briefs/2026-04-17_Andy的学术概览.md`

---

## 🖥️ Vibe Coding 平台适配

破晓原生支持主流 AI 编程助手的 Skill 系统：

| 平台 | 触发方式 | 配置文件 |
|------|---------|----------|
| **CodeFlicker / KwaiPilot** | `/poxiao`, `/briefing`, `/deep_dive` | `SKILL.md`（项目根目录） |
| **Claude Code** | 自动识别 `SKILL.md` | `SKILL.md` |
| **Cursor** | 自动识别 `SKILL.md` | `SKILL.md` |
| **Trae / 其他 Skill 兼容平台** | 手动导入 | `SKILL.md` |

### 定时任务配置

**CodeFlicker 定时任务**：

1. 打开 CodeFlicker 设置 → 定时任务
2. 添加新任务：
   - Prompt: `/briefing --days 1`
   - Cron: `0 9 * * 1-5`（工作日早 9 点）
   - 工作目录：项目根目录

**macOS launchd**（setup.py 自动安装）：

```bash
python setup.py  # 选择 "launchd"
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
├── SKILL.md               # Vibe Coding Skill 定义
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
├── .poxiao_system/        # 系统数据（隐藏）
│   ├── profiles/          # 用户画像
│   ├── cache/             # SQLite 缓存
│   └── raw/               # 原始 JSON 数据
│
├── PoXiao_Briefs/         # 输出简报（用户主要交互面）
│
└── examples/              # 示例数据
    ├── briefs/            # 示例简报
    └── raw/               # 示例原始数据
```

---

## 🎯 使用场景

- **研究者**：每天追踪 arXiv 最新论文，自动识别高相关度研究
- **工程师**：监控 HackerNews/Reddit 技术热点，聚类去重
- **投资人**：关注 AI 行业融资/IPO 动态
- **产品经理**：追踪竞品发布、技术趋势

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
- [Semantic Scholar](https://www.semanticscholar.org/) — 学术论文知识图谱
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
