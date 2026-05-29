# 破晓 PoXiao · AI 原生驱动的个人情报系统

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/Skill-v1.6-purple.svg" alt="Skill v1.6">
  <img src="https://img.shields.io/badge/Briefings-35+-orange.svg" alt="Briefings">
</p>

<p align="center">
  <strong>不出门，可知天下事</strong><br>
  <sub>AI 驱动 · Vibe Coding 原生 · 学术 + 社区 + 财经 + 职场 全栈情报</sub>
</p>

---

## ✨ 最近更新（v1.6 / 2026-05）

- **🆕 信息图引用唯一化**：早报 markdown 中 `![今日早报信息图]` 引用强制去重，幂等插入逻辑已固化到 SKILL（修复 12 篇历史早报重复引用 bug）
- **🆕 按月归档 briefs**：`briefs/YYYY-MM/DD/` 三级目录，每月最多 31 个子目录，浏览效率显著提升
- **🆕 五板块格式标准化**：学术 + 社区 + 财经 + 职场 + 总结，每个板块字段精细化（详见 [SKILL.md](.codeflicker/skills/poxiao-briefing/SKILL.md)）
- **🆕 配套信息图**：每篇早报自动生成 16:9 信息图（2K，约 5MB），相对路径嵌入 md，GitHub 直接可看
- **🆕 三层 fallback 数据抓取**：vibe_fetch + gen_brief.sh + HuggingFace API 直取，应对 RSS 源不稳定
- **🆕 敏感词净化对照表**：18 组生图 API 触发审核词的中性替换，保证信息图 100% 出图
- **🆕 格式漂移自动修复**：定时任务自动生成的早报若不符合标准，技能会读取重写而非重跑
- **🆕 raw_context.md → 早报.md 补写**：抓取成功但生成失败时可基于原始数据补写完整日报
- **🆕 MIT License**：欢迎 fork、修改、二次分发

---

## 🎯 快速开始

### 在 IDE 中触发（推荐）

```
生成今日早报      # 抓取 + 早报 + 信息图 + 推送 一条龙
今天的日报        # 同上
调整 profile     # 修改兴趣权重
配置定时任务      # 设置每日 7:00 自动跑
```

### 命令行运行

```bash
cd poxiao-repo
source venv/bin/activate

# 数据抓取（输出到 briefs/YYYY-MM/DD/raw_context.md）
python fetch/vibe_fetch.py

# 备用：HN + HuggingFace + Reddit 补充
bash scripts/gen_brief.sh

# 单篇论文深度分析
python fetch/deep_dive.py 2605.27891
```

> ⚠️ **跨平台 venv 不兼容**：如果是 Windows 创建的 venv，先 `rm -rf venv && python3 -m venv venv && pip install -r requirements.txt`。

---

## 📁 项目结构

```
poxiao-repo/
├── briefs/                    # 早报输出（按月归档）
│   ├── 2026-04/
│   │   ├── 20/
│   │   │   ├── 早报.md
│   │   │   ├── infographic.jpg     # 16:9 配套信息图
│   │   │   └── raw_context.md      # 原始抓取数据
│   │   ├── 21/...
│   │   └── 30/
│   └── 2026-05/
│       ├── 01/...
│       └── 29/
├── fetch/
│   ├── vibe_fetch.py          # 异步多源抓取（核心）
│   ├── deep_dive.py           # arXiv 论文深度分析
│   └── diagnose_sources.py    # 信源连通性诊断
├── scripts/
│   └── gen_brief.sh           # HN/HF/Reddit fallback 抓取
├── profiles/
│   ├── profile_demo.yaml      # 默认兴趣配置
│   └── profile_example.yaml   # 配置示例
├── config.json                # RSS 源开关 + 信源配置
├── requirements.txt           # Python 依赖
├── LICENSE                    # MIT
└── README.md
```

> 项目根目录 `.codeflicker/skills/poxiao-briefing/` 与 `.codeflicker/skills/poxiao-briefing-infographic/` 包含 Skill 定义，IDE 加载后即可触发。

---

## 📐 早报格式规范（v1.3+）

每篇早报严格遵循五板块结构：

```
📡 学术概览  →  🔥 社区速递  →  💰 财经简报  →  🏢 职场动态  →  📊 今日总结
```

### 学术 Tier 1 必填字段

- 一句话核心贡献（含"做了什么 + 解决什么 + 结果如何"）
- 摘要精译（≥3 段，含背景/方法/量化结果）
- 核心创新点（每点 ≤25 字）
- `<details>` 折叠块（方法细节 + 实验结果 + 局限性 + 链接）

### 社区 Tier 1 必填字段

- 热度信号（HN Score / HF 排名）
- 一句话核心 / 核心共识 / 主要争议 / 影响评估
- 来源链接

### 今日总结

- 3 条独立洞察
- 每条 ≥40 字，含**现象 → 逻辑 → 预测**三段

完整规范见 [poxiao-briefing/SKILL.md](.codeflicker/skills/poxiao-briefing/SKILL.md)。

---

## 🎨 配套信息图

每篇早报附带 16:9 高清信息图（2K，约 5MB），放在同目录 `infographic.jpg`，markdown 通过相对路径 `![今日早报信息图](./infographic.jpg)` 嵌入。

**生成原理**：
1. 从早报中提炼 ≤8 个核心信息点（学术 Tier1 + 社区热点 + 今日总结）
2. 敏感词净化（18 组对照表，避免触发生图 API 审核）
3. 调用 `designai-infographic-image` skill 生图
4. 唯一性约束（一篇一图，永不重复引用）

---

## ⚙️ 配置说明

### 兴趣权重（profiles/profile_demo.yaml）

```yaml
research_domains:
  视频生成 & 视频理解:
    keywords: [video generation, video diffusion, world model, NeRF]
    priority: 5.5    # 最高优先级
  基础模型 & 推理:
    keywords: [LLM, foundation model, reasoning, inference]
    priority: 5.0
  多模态 / 3D / 具身智能:
    keywords: [VLM, VLA, 3D generation, embodied AI]
    priority: 4.5
  Agent / RL:
    keywords: [agent, RLHF, alignment]
    priority: 2.5    # 大幅降低（避免 Agent 论文淹没视频内容）
```

### 信源开关（config.json）

```json
{
  "sources": {
    "arxiv": { "enabled": true, "time_window_hours": 48 },
    "hackernews": { "enabled": true, "min_upvotes": 10 },
    "rss": [
      { "name": "Ars Technica AI", "enabled": true },
      { "name": "Reddit MachineLearning", "enabled": true },
      { "name": "HuggingFace Daily Papers", "enabled": false }
    ]
  }
}
```

> **当前已知不稳定源**：HuggingFace via rsshub.app（403）、36kr via rsshub（403）、量子位 decemberpei（404）、Reddit LocalLLaMA RSS（2026-05-28 起 403）。建议依赖 `gen_brief.sh` 的直接 API 调用兜底。

---

## 🛠️ 已知问题与解决方案

| 问题 | 解决 |
|------|------|
| venv 跨平台不兼容 | `rm -rf venv && python3 -m venv venv && pip install -r requirements.txt` |
| RSS 源超时 | 降级到 `bash scripts/gen_brief.sh` |
| arXiv API 严重限流 (429) | 用 HuggingFace Daily Papers 替代 |
| 信息图生成"未找到相关内容" | 提示词触发审核，按 SKILL 中 18 组敏感词对照表替换 |
| 信息图无 CDN URL | 已保存到本地 `infographic.jpg`，用相对路径嵌入即可 |
| 早报里出现 2-3 个相同信息图 | 已修复并固化到 SKILL，存量数据已批量去重 |
| 定时任务格式漂移 | SKILL 步骤 0 会先检查格式，不符则读取重写 |
| raw_context.md 存在但早报缺失 | SKILL 步骤 6 支持基于原始数据补写完整日报 |

---

## 🗺️ 路线图

### ✅ 已完成
- [x] 五板块格式标准化（v1.3）
- [x] 配套信息图生成（v1.4）
- [x] 三层 fallback 数据抓取（v1.5）
- [x] 信息图引用唯一化（v1.6）
- [x] briefs 按月归档
- [x] MIT License

### 🚧 进行中
- [ ] **品味闭环**：用户对单条新闻 👍/👎，自动调整 profile 权重
- [ ] **多轮对话记忆**：同一会话内记住上下文偏好

### 📅 规划中
- [ ] **PDF 全文提取**：deep_dive 不止抓摘要
- [ ] **Twitter/X 追踪**：特定研究员动态
- [ ] **向量数据库**：历史早报语义检索
- [ ] **MCP 工具链集成**：标准化工具调用

---

## 🤝 致谢

- [arXiv](https://arxiv.org/) · [HuggingFace](https://huggingface.co/) · [Hacker News](https://news.ycombinator.com/) · [Reddit](https://reddit.com/)
- [httpx](https://www.python-httpx.org/) · [feedparser](https://github.com/kurtmckee/feedparser) · [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

---

## 📄 License

[MIT](./LICENSE) — 欢迎 fork、修改、二次分发，仅需保留版权声明。

---

<p align="center">
  <strong>破晓 PoXiao · 让 AI 帮你看世界</strong>
</p>
