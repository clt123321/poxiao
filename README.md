# 破晓 PoXiao V2.0 - AI 原生驱动的个人情报系统

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/Skill-V2.0-purple.svg" alt="Skill V2.0">
</p>

<p align="center">
  <strong>不出门，可知天下事</strong><br>
  <sub>AI 驱动 • Vibe Coding 原生 • HermeScroll 双核</sub>
</p>

---

## 🎯 快速开始

### 触发方式

在支持 Skill 的 AI 编程助手中，直接发送：

```
/poxiao
```

或使用完整命令：

```
/briefing
/早报
/deep_dive <arxiv_id>   # 单篇论文深度分析
```

### 本地运行

```bash
# 抓取数据
python fetch/vibe_fetch.py

# 输出：PoXiao_Briefs/raw_context.md

# 深度分析某篇论文
python fetch/deep_dive.py 2604.14895
# 输出：PoXiao_Briefs/deep_context.md
```

---

## 📐 架构设计

### 双核引擎

```
┌─────────────────────────────────────────────────────────────┐
│                        破晓 V2.0                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌──────────────┐    ┌──────────────┐                    │
│   │  Hermes 循环  │    │ HermeScroll  │                    │
│   │  (品味引擎)   │    │  (数据引擎)   │                    │
│   │              │    │              │                    │
│   │  • 读 profile│    │  • 抓取 raw  │                    │
│   │  • 写 profile│    │  • 格式化 md │                    │
│   │  • 自我进化  │    │  • 异步并发  │                    │
│   └──────┬───────┘    └──────┬───────┘                    │
│          │                   │                             │
│          └─────────┬─────────┘                             │
│                    ▼                                       │
│          ┌─────────────────┐                              │
│          │  raw_context.md │                              │
│          └────────┬────────┘                              │
│                   ▼                                       │
│          ┌─────────────────┐                              │
│          │   Trae/Skill    │                              │
│          │  (智能过滤/输出) │                              │
│          └────────┬────────┘                              │
│                   ▼                                       │
│          ┌─────────────────┐                              │
│          │ YYYY-MM-DD_早报 │                              │
│          └─────────────────┘                              │
└─────────────────────────────────────────────────────────────┘
```

### 核心模块

| 模块 | 文件 | 职责 |
|------|------|------|
| **数据抓取** | `fetch/vibe_fetch.py` | 异步并发抓取 arXiv/RSS/HackerNews |
| **深度分析** | `fetch/deep_dive.py` | 根据 arXiv ID 获取论文完整信息 |
| **品味引擎** | `profiles/profile_demo.yaml` | 用户兴趣配置，Hermes 联动 |
| **原始数据** | `PoXiao_Briefs/raw_context.md` | 所有抓取数据的统一输出 |
| **早报生成** | `.trae/skills/poxiao/SKILL.md` | Trae 执行的 Skill 指令定义 |
| **早报输出** | `PoXiao_Briefs/YYYY-MM-DD_早报.md` | 最终格式化早报 |
| **信源配置** | `config.json` | RSS/API 源配置与开关 |

---

## 📁 项目结构

```
poxiao/
├── fetch/
│   ├── vibe_fetch.py          # 极简数据抓取（V2.0 核心）
│   ├── deep_dive.py           # 论文深度分析（/deep_dive 引擎）
│   └── diagnose_sources.py    # 信源诊断工具
├── profiles/
│   ├── profile_demo.yaml      # 演示用户品味配置
│   └── profile_example.yaml   # 示例模板
├── PoXiao_Briefs/
│   ├── raw_context.md         # 原始数据（自动生成）
│   └── YYYY-MM-DD_早报.md     # 格式化早报
├── .trae/skills/poxiao/
│   └── SKILL.md              # Vibe Coding Skill 定义
├── config.json                # RSS/API 源配置
├── requirements.txt           # Python 依赖
└── README.md                 # 本文件
```

---

## � 筛选逻辑详解

### 三层过滤架构

#### 第一层：时间过滤（Time Filter）
```python
# vibe_fetch.py 中的时间窗口控制
TIME_WINDOW_HOURS = 48  # 默认 48 小时

# 论文是否在时间窗口内
published > datetime.now(timezone.utc) - timedelta(hours=TIME_WINDOW_HOURS)
```
- **目的**：只保留最近 48 小时内的内容，避免信息过载
- **Fallback**：如果某关键词在 48 小时内无新论文，收集最新 5 篇

#### 第二层：关键词匹配（Keyword Matching）
```yaml
# profile_demo.yaml 中的关键词配置
research_domains:
  RL 推断 & 对齐:
    keywords: [RLHF, GRPO, PPO, DPO, reasoning, alignment]
    priority: 5.0
  LLM Agent 工程:
    keywords: [agent, multi-agent, tool use, MCP]
    priority: 4.0
  算力优化 & 推理加速:
    keywords: [vLLM, PagedAttention, quantization, MoE]
    priority: 4.0
```

**匹配逻辑**：
```python
def match_score(paper_title: str, keywords: list[str]) -> float:
    """计算论文与关键词的匹配分数"""
    title_lower = paper_title.lower()
    score = 0.0
    for keyword in keywords:
        if keyword.lower() in title_lower:
            score += 1.0
    return score
```

#### 第三层：噪声过滤（Noise Filter）
```yaml
# profile_demo.yaml 中的噪声过滤
noise_filter_prompt: >
  排除纯宏观经济和传统金融新闻；
  保留 AI 算力、顶尖 AI 初创融资、
  科技大厂 AI 战略变动、AI 产品商业化里程碑。

excluded_keywords:
  - workshop
  - medical image
  - pathology
  - remote sensing
  - radiology
```

### 优先级评分公式

```
final_score = base_priority * keyword_match_count * time_decay_factor

其中：
- base_priority: 用户配置的领域优先级（0-5）
- keyword_match_count: 标题中匹配的关键词数量
- time_decay_factor: 时间衰减因子（越新越高）
```

### 相似论文去重（SimHash）

```python
def compute_similarity_hash(title: str) -> int:
    """计算标题的特征哈希"""
    words = title.lower().split()
    # 取关键词的哈希叠加
    hash_value = 0
    for word in words:
        if len(word) > 4:  # 忽略短词
            hash_value ^= hash(word)
    return hash_value

def deduplicate(papers: list[dict]) -> list[dict]:
    """去除相似论文（哈希值相近的）"""
    seen_hashes = set()
    unique_papers = []
    for paper in papers:
        h = compute_similarity_hash(paper['title'])
        if h not in seen_hashes:
            seen_hashes.add(h)
            unique_papers.append(paper)
    return unique_papers
```

---

## �🔧 配置说明

### 用户品味 (profile_demo.yaml)

```yaml
research_domains:
  RL 推断 & 对齐 (RLHF/GRPO/PPO):
    keywords: [RLHF, GRPO, PPO, DPO, reasoning, alignment]
    priority: 5.0
  LLM Agent 工程:
    keywords: [agent, multi-agent, tool use, MCP]
    priority: 4.0
  算力优化 & 推理加速:
    keywords: [vLLM, PagedAttention, quantization, MoE]
    priority: 4.0

business_focus:
  sectors:
    - 硅谷动态 (Anthropic/OpenAI/Meta AI)
    - 国内大厂动向 (字节/阿里/腾讯)
    - 芯片 & 算力基础设施
  tracked_companies:
    tier1: [Anthropic, OpenAI, DeepSeek, Google DeepMind]
    tier2: [Meta AI, Mistral, 字节跳动, 阿里云]
    tier3: [NVIDIA, 台积电, AMD]

format_preference:
  academic_top_n: 8
  community_top_n: 10
  finance_top_n: 8
```

### 信源配置 (config.json)

```json
{
  "sources": {
    "arxiv": {
      "enabled": true,
      "time_window_hours": 48,
      "categories": ["cs.AI", "cs.LG", "cs.CL"]
    },
    "hackernews": { "enabled": true, "min_upvotes": 10 },
    "rss": [
      {
        "name": "TechCrunch AI",
        "url": "https://techcrunch.com/category/artificial-intelligence/feed/",
        "enabled": true,
        "category": "finance"
      }
    ]
  }
}
```

---

## 🚀 迭代方向（Sign Action）

### Phase 1: 巩固数据层（已实现）
- [x] arXiv 学术论文抓取
- [x] HackerNews 社区热点
- [x] RSS 财经动态
- [x] 用户品味绑定（profile.yaml）
- [x] /deep_dive 深度分析

### Phase 2: 增强交互层（进行中）
- [ ] **Hermes 品味闭环验证**：测试 IDE 是否能响应用户修正，自动修改 profile.yaml
- [ ] **多轮对话记忆**：在同一次 /poxiao 会话中记住上下文
- [ ] **实时反馈机制**：用户对单条新闻点赞/踩，系统记录并调整权重

### Phase 3: 扩展信源层（规划中）
- [ ] **PDF 全文提取**：/deep_dive 不仅抓摘要，还要能下载 PDF 并提取正文
- [ ] **Twitter/X 追踪**：抓取特定 AI 研究员的最新动态
- [ ] **Reddit 专题订阅**：追踪 r/MachineLearning 等高质量社区
- [ ] **中文信源增强**：36kr、机器之心等国内高质量源

### Phase 4: 智能化层（远期规划）
- [ ] **MCP 工具链集成**：标准化工具调用协议
- [ ] **Crawl4AI 精读引擎**：网页深度内容提取
- [ ] **向量数据库**：存储历史早报，支持语义检索
- [ ] **多模型路由**：根据内容类型路由到最适合的 LLM

---

## 🤝 致谢

- [arXiv](https://arxiv.org/) — 开放学术预印本平台
- [Hacker News](https://news.ycombinator.com/) — 技术社区风向标
- [TechCrunch](https://techcrunch.com/) — 全球创业融资第一手资讯
- [httpx](https://www.python-httpx.org/) — 异步 HTTP 客户端
- [feedparser](https://github.com/kurtmckee/feedparser) — RSS 解析利器

---

<p align="center">
  <strong>破晓 PoXiao — 让 AI 帮你看世界</strong>
</p>
