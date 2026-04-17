#!/usr/bin/env python3
"""
setup.py — 破晓 (PoXiao) 傻瓜式前导交互引导程序

设计原则：
  - 全程问答，所有步骤可直接回车跳过（使用预设默认值）
  - 多用户支持：生成 profiles/profile_{name}.yaml
  - 最后输出定时任务配置（launchd / crontab / 仅运行一次）
  - 所有文件写入强制 UTF-8

用法：
    python setup.py              # 交互式引导
    python setup.py --user andy # 跳过用户名询问，直接配置 andy
    python setup.py --defaults   # 全部使用默认值（CI/CD 用）
"""

from __future__ import annotations

import os
import sys
import re
import shutil
import argparse
import textwrap
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any

# --------------------------------------------------------------------------
# 终端样式工具（降级友好：无 ANSI 支持时退化为普通文本）
# --------------------------------------------------------------------------

_HAS_COLOR = sys.stdout.isatty()


def _c(text: str, code: str) -> str:
    return f"\033[{code}m{text}\033[0m" if _HAS_COLOR else text


def bold(t: str) -> str:   return _c(t, "1")
def green(t: str) -> str:  return _c(t, "32")
def yellow(t: str) -> str: return _c(t, "33")
def cyan(t: str) -> str:   return _c(t, "36")
def gray(t: str) -> str:   return _c(t, "90")
def red(t: str) -> str:    return _c(t, "31")


def hr(char: str = "─", width: int = 60) -> str:
    return gray(char * width)


def banner() -> None:
    print()
    print(bold(cyan("  ██████╗  ██████╗     ██╗  ██╗██╗ █████╗  ██████╗ ")))
    print(bold(cyan("  ██╔══██╗██╔═══██╗    ╚██╗██╔╝██║██╔══██╗██╔═══██╗")))
    print(bold(cyan("  ██████╔╝██║   ██║     ╚███╔╝ ██║███████║██║   ██║")))
    print(bold(cyan("  ██╔═══╝ ██║   ██║     ██╔██╗ ██║██╔══██║██║   ██║")))
    print(bold(cyan("  ██║     ╚██████╔╝    ██╔╝ ██╗██║██║  ██║╚██████╔╝")))
    print(bold(cyan("  ╚═╝      ╚═════╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝ ╚═════╝ ")))
    print()
    print(bold("  破晓 PoXiao") + gray(" — AI 原生驱动的个人情报系统"))
    print(gray("  不出门，可知天下事"))
    print()


# --------------------------------------------------------------------------
# 交互工具
# --------------------------------------------------------------------------

def ask(
    prompt: str,
    default: str = "",
    hint: str = "",
    validator=None,
    reject_single_char: bool = False,  # V1.2: 防呆
) -> str:
    """
    显示问题，读取用户输入。
    - 直接回车 → 使用 default
    - validator 不通过 → 重新询问
    - reject_single_char=True → 拒绝单字母输入（如 y/n）
    """
    default_label = gray(f"[默认: {default}]") if default else gray("[回车跳过]")
    hint_label    = gray(f"  ↳ {hint}") if hint else ""

    while True:
        if hint_label:
            print(hint_label)
        raw = input(f"  {bold('?')} {prompt} {default_label}: ").strip()
        value = raw if raw else default

        # V1.2 防呆：拒绝单字母输入（除非是默认值）
        if reject_single_char and raw and len(raw) == 1 and raw.lower() in ('y', 'n'):
            print(red(f"  ✗ 单字母 '{raw}' 容易被误认为 yes/no，请输入完整名称或回车使用默认值"))
            continue

        if validator is None or validator(value):
            return value
        print(red(f"  ✗ 输入不合法，请重试"))


def ask_choice(
    prompt: str,
    choices: list[tuple[str, str]],  # [(key, label), ...]
    default: str = "",
    multi: bool = False,
) -> str | list[str]:
    """
    单选或多选菜单。
    choices: [(key, label), ...]
    multi=True 时用户可输入多个编号，如 "1,3"
    返回 key（单选）或 [key, ...] （多选）
    """
    print(f"\n  {bold('?')} {prompt}")
    for i, (key, label) in enumerate(choices, 1):
        marker = "●" if key == default else "○"
        print(f"    {gray(str(i)+'.')} {marker} {label}")

    if multi:
        raw = input(f"  输入序号（逗号分隔，回车=全选默认）: ").strip()
    else:
        default_idx = next(
            (str(i) for i, (k, _) in enumerate(choices, 1) if k == default), "1"
        )
        raw = input(f"  输入序号 {gray('[默认: '+default_idx+']')}: ").strip()

    keys = [k for k, _ in choices]

    if not raw:
        if multi:
            return [default] if default else [keys[0]]
        return default if default else keys[0]

    if multi:
        selected = []
        for part in re.split(r"[,，\s]+", raw):
            part = part.strip()
            if part.isdigit():
                idx = int(part) - 1
                if 0 <= idx < len(choices):
                    selected.append(keys[idx])
        return selected if selected else [keys[0]]
    else:
        if raw.isdigit():
            idx = int(raw) - 1
            if 0 <= idx < len(choices):
                return keys[idx]
        return keys[0]


def confirm(prompt: str, default: bool = True) -> bool:
    label = gray("[Y/n]") if default else gray("[y/N]")
    raw = input(f"  {bold('?')} {prompt} {label}: ").strip().lower()
    if not raw:
        return default
    return raw in ("y", "yes", "是", "1")


# --------------------------------------------------------------------------
# Profile 生成器
# --------------------------------------------------------------------------

# 预置研究领域选项
DOMAIN_PRESETS: list[tuple[str, str, dict]] = [
    ("rl_reasoning", "RL 推断 & 对齐 (RLHF/GRPO/PPO)", {
        "keywords": ["RLHF", "GRPO", "PPO", "DPO", "reasoning", "alignment", "reward model"],
        "arxiv_categories": ["cs.AI", "cs.LG", "cs.MA"],
        "priority": 5.0,
        "deep_analysis": True,
    }),
    ("inference_accel", "算力优化 & 推理加速 (vLLM/量化/MoE)", {
        "keywords": ["vLLM", "PagedAttention", "quantization", "speculative decoding", "MoE", "KV cache"],
        "arxiv_categories": ["cs.LG", "cs.AR"],
        "priority": 4.0,
        "deep_analysis": True,
    }),
    ("agent_engineering", "LLM Agent 工程 (工具调用/多智能体)", {
        "keywords": ["agent", "multi-agent", "tool use", "MCP", "planning", "long-horizon"],
        "arxiv_categories": ["cs.AI", "cs.MA", "cs.CL"],
        "priority": 4.0,
        "deep_analysis": True,
    }),
    ("coding_agent", "AI 编程 & Vibe Coding (SWE-bench/代码生成)", {
        "keywords": ["code generation", "SWE-bench", "coding agent", "Vibe Coding", "software engineering"],
        "arxiv_categories": ["cs.SE", "cs.AI"],
        "priority": 3.0,
        "deep_analysis": False,
    }),
    ("multimodal", "多模态 & 语音 (VLM/ASR/TTS)", {
        "keywords": ["multimodal", "vision-language", "VLM", "ASR", "speech", "CLIP"],
        "arxiv_categories": ["cs.CV", "cs.SD", "cs.MM"],
        "priority": 3.5,
        "deep_analysis": False,
    }),
    ("rag_retrieval", "RAG & 知识系统 (检索/向量库/重排)", {
        "keywords": ["RAG", "retrieval augmented generation", "vector database", "reranking"],
        "arxiv_categories": ["cs.IR", "cs.CL"],
        "priority": 3.0,
        "deep_analysis": False,
    }),
    ("foundation_models", "基础大模型 (预训练/微调/Scaling)", {
        "keywords": ["large language model", "LLM", "pre-training", "LoRA", "scaling law"],
        "arxiv_categories": ["cs.CL", "cs.AI", "cs.LG"],
        "priority": 2.0,
        "deep_analysis": False,
    }),
    ("ai_safety", "AI 安全 & 可靠性 (幻觉/越狱/对齐)", {
        "keywords": ["safety", "jailbreak", "hallucination", "robustness", "interpretability"],
        "arxiv_categories": ["cs.AI", "cs.CR"],
        "priority": 2.5,
        "deep_analysis": False,
    }),
]

# 预置商业关注面
BUSINESS_PRESETS: list[tuple[str, str]] = [
    ("silicon_valley",   "硅谷动态 (Anthropic/OpenAI/Meta AI 产品与融资)"),
    ("ai_investment",    "AI 二级市场投资 (AI 相关股票/ETF/算力基础设施)"),
    ("china_ai",         "国内大厂动向 (字节/阿里/腾讯/百度/华为/快手)"),
    ("chips_compute",    "芯片 & 算力基础设施 (NVIDIA/台积电/AMD)"),
    ("embodied_ai",      "具身智能 & 机器人 (融资动态/产品发布)"),
    ("quant_finance",    "量化金融 & AI 在金融领域的应用"),
]

# 预置定时任务选项
SCHEDULE_OPTIONS: list[tuple[str, str]] = [
    ("launchd",  "macOS launchd 后台静默运行（推荐，系统级定时任务）"),
    ("crontab",  "Linux / macOS crontab（传统 cron 方式）"),
    ("once",     "仅在此刻运行一次（不配置定时任务）"),
    ("skip",     "跳过，稍后手动配置"),
]


def build_profile_yaml(
    username: str,
    display_name: str,
    domains: list[str],
    business: list[str],
    deep_threshold: float,
    extra_excluded: list[str],
    s2_api_key: str = "",
) -> str:
    """根据用户选择生成 profile.yaml 内容"""

    import yaml

    # 构建 research_domains
    domain_map = {d[0]: d[2] for d in DOMAIN_PRESETS}
    research_domains: dict[str, Any] = {}
    for key in domains:
        if key in domain_map:
            research_domains[next(d[1] for d in DOMAIN_PRESETS if d[0] == key)] = domain_map[key]

    # 若没有选择任何域，使用默认
    if not research_domains:
        for key in ("rl_reasoning", "agent_engineering", "inference_accel"):
            research_domains[next(d[1] for d in DOMAIN_PRESETS if d[0] == key)] = domain_map[key]

    # 构建 business_focus sectors
    business_label_map = {k: v for k, v in BUSINESS_PRESETS}
    sectors = [business_label_map.get(k, k) for k in business] or [
        "硅谷动态", "国内大厂动向", "芯片 & 算力基础设施"
    ]

    # 追踪公司
    tracked_companies: dict[str, list[str]] = {
        "tier1": ["Anthropic", "OpenAI", "DeepSeek", "Google DeepMind"],
        "tier2": ["Meta AI", "Mistral", "字节跳动", "阿里云", "华为", "快手"],
        "tier3": ["NVIDIA", "台积电", "AMD", "Sequoia"],
    }
    if "china_ai" in business:
        tracked_companies["tier2"].extend(["腾讯", "百度"])
    if "embodied_ai" in business:
        tracked_companies["tier2"].append("Figure AI")
        tracked_companies["tier3"].extend(["加速进化", "智元机器人", "宇树科技"])

    excluded = ["workshop", "medical image", "pathology", "remote sensing", "radiology"]
    excluded.extend([kw for kw in extra_excluded if kw])

    config: dict[str, Any] = {
        "version": "2.0",
        "meta": {
            "username": username,
            "display_name": display_name,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "generated_by": "poxiao-setup",
        },
        "research_domains": research_domains,
        "business_focus": {
            "sectors": sectors,
            "noise_filter_prompt": (
                "排除纯宏观经济和传统金融新闻；保留 AI 算力、顶尖 AI 初创融资、"
                "科技大厂 AI 战略变动、AI 产品商业化里程碑。"
            ),
            "tracked_companies": tracked_companies,
        },
        "format_preference": {
            "academic_top_n": 8,
            "community_top_n": 10,
            "finance_top_n": 8,
            "finance_min_score": 3.0,
            "trigger_deep_analysis_threshold": deep_threshold,
            "topic_dedup": True,
            "summary_style": "tier2",
            "language": "zh",
            "output_name": display_name,    # 用于文件名中显示："{display_name}的早报"
        },
        "excluded_keywords": excluded,
        "system": {
            "semantic_scholar_api_key": s2_api_key,
            "python_path": sys.executable,
            "work_dir": str(Path(__file__).parent.resolve()),
        },
    }

    return yaml.dump(config, allow_unicode=True, default_flow_style=False, sort_keys=False)


# --------------------------------------------------------------------------
# 定时任务生成器
# --------------------------------------------------------------------------

def gen_launchd_plist(username: str, work_dir: str, python_path: str) -> str:
    label = f"com.poxiao.briefing.{username}"
    return textwrap.dedent(f"""\
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
            "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
        <plist version="1.0">
        <dict>
            <key>Label</key>
            <string>{label}</string>

            <key>ProgramArguments</key>
            <array>
                <string>{python_path}</string>
                <string>{work_dir}/poxiao.py</string>
                <string>generate</string>
                <string>--user</string>
                <string>{username}</string>
            </array>

            <key>WorkingDirectory</key>
            <string>{work_dir}</string>

            <!-- 工作日（周一~周五）早上 09:00 触发 -->
            <key>StartCalendarInterval</key>
            <array>
                <!-- 周二~周五: 24h 窗口 -->
                <dict>
                    <key>Weekday</key><integer>2</integer>
                    <key>Hour</key><integer>9</integer>
                    <key>Minute</key><integer>0</integer>
                </dict>
                <dict>
                    <key>Weekday</key><integer>3</integer>
                    <key>Hour</key><integer>9</integer>
                    <key>Minute</key><integer>0</integer>
                </dict>
                <dict>
                    <key>Weekday</key><integer>4</integer>
                    <key>Hour</key><integer>9</integer>
                    <key>Minute</key><integer>0</integer>
                </dict>
                <dict>
                    <key>Weekday</key><integer>5</integer>
                    <key>Hour</key><integer>9</integer>
                    <key>Minute</key><integer>0</integer>
                </dict>
                <!-- 周一: 72h 窗口（覆盖周末） -->
                <dict>
                    <key>Weekday</key><integer>1</integer>
                    <key>Hour</key><integer>9</integer>
                    <key>Minute</key><integer>0</integer>
                </dict>
            </array>

            <key>StandardOutPath</key>
            <string>{work_dir}/logs/poxiao_{username}.log</string>
            <key>StandardErrorPath</key>
            <string>{work_dir}/logs/poxiao_{username}.err</string>

            <key>EnvironmentVariables</key>
            <dict>
                <key>PATH</key>
                <string>/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin</string>
            </dict>
        </dict>
        </plist>
    """)


def gen_crontab_entry(username: str, work_dir: str, python_path: str) -> str:
    return textwrap.dedent(f"""\
        # 破晓 (PoXiao) 早报 - {username}
        # 周二~周五 09:00: 24h 窗口
        0 9 * * 2-5  cd {work_dir} && {python_path} poxiao.py generate --user {username} --days 1 >> {work_dir}/logs/poxiao_{username}.log 2>&1
        # 周一 09:00: 72h 窗口（覆盖周末）
        0 9 * * 1    cd {work_dir} && {python_path} poxiao.py generate --user {username} --days 3 >> {work_dir}/logs/poxiao_{username}.log 2>&1
    """)


def install_launchd(plist_content: str, username: str, work_dir: str) -> bool:
    """写入 plist 到 ~/Library/LaunchAgents/ 并 load"""
    label = f"com.poxiao.briefing.{username}"
    plist_dir = Path.home() / "Library" / "LaunchAgents"
    plist_path = plist_dir / f"{label}.plist"

    try:
        plist_dir.mkdir(parents=True, exist_ok=True)
        plist_path.write_text(plist_content, encoding="utf-8")

        # 确保 logs 目录存在
        (Path(work_dir) / "logs").mkdir(exist_ok=True)

        # load
        result = subprocess.run(
            ["launchctl", "load", "-w", str(plist_path)],
            capture_output=True, text=True
        )
        return result.returncode == 0
    except Exception:
        return False


# --------------------------------------------------------------------------
# 主引导流程
# --------------------------------------------------------------------------

def run_setup(
    preset_user: str | None = None,
    use_defaults: bool = False,
) -> None:
    banner()

    work_dir = str(Path(__file__).parent.resolve())
    python_path = sys.executable

    print(hr())
    print(f"  {bold('欢迎使用破晓 PoXiao 配置引导')}")
    print(f"  配置文件将保存到 {cyan('profiles/')} 目录")
    print(hr())
    print()

    # ── Step 0: 用户名 ───────────────────────────────────────────────────
    print(bold("▶ Step 0 / 5  用户身份"))
    print(gray("  （支持一机多用户独立简报，如 andy / alice / work）"))

    if preset_user:
        username = preset_user
        print(f"  使用预设用户名: {cyan(username)}")
    elif use_defaults:
        username = "default"
    else:
        username = ask(
            "请输入用户名（英文/拼音，用于文件命名）",
            default="default",
            validator=lambda x: bool(re.match(r"^[a-zA-Z][a-zA-Z0-9_\-]{0,30}$", x)),
        )

    display_name = ask(
        "显示名称（出现在简报标题中，如 'Andy'）",
        default=username,
        reject_single_char=True,  # V1.2 防呆：拒绝 y/n 单字母
    ) if not use_defaults else username

    profiles_dir = Path(work_dir) / ".poxiao_system" / "profiles"
    profiles_dir.mkdir(parents=True, exist_ok=True)
    profile_path = profiles_dir / f"profile_{username}.yaml"

    if profile_path.exists() and not use_defaults:
        print()
        overwrite = confirm(
            f"  {yellow('⚠')} .poxiao_system/profiles/profile_{username}.yaml 已存在，覆盖？",
            default=False,
        )
        if not overwrite:
            print(gray("  已跳过，退出引导。"))
            return

    print()

    # ── Step 1: 研究领域 ────────────────────────────────────────────────
    print(bold("▶ Step 1 / 5  研究领域（学术简报兴趣加权）"))
    domain_choices = [(d[0], d[1]) for d in DOMAIN_PRESETS]

    if use_defaults:
        selected_domains = ["rl_reasoning", "agent_engineering", "inference_accel"]
    else:
        selected_domains = ask_choice(
            "选择你关注的研究领域（可多选，逗号分隔，回车=前3项）",
            domain_choices,
            default="rl_reasoning",
            multi=True,
        )
        if isinstance(selected_domains, str):
            selected_domains = [selected_domains]

    print(green(f"  ✓ 已选: {', '.join(selected_domains)}"))
    print()

    # ── Step 2: 商业关注面 ────────────────────────────────────────────
    print(bold("▶ Step 2 / 5  商业关注面（财经简报过滤）"))

    if use_defaults:
        selected_business = ["silicon_valley", "china_ai", "chips_compute"]
    else:
        selected_business = ask_choice(
            "选择你关注的商业/行业方向（可多选）",
            BUSINESS_PRESETS,
            default="silicon_valley",
            multi=True,
        )
        if isinstance(selected_business, str):
            selected_business = [selected_business]

    print(green(f"  ✓ 已选: {', '.join(selected_business)}"))
    print()

    # ── Step 3: 深度分析阈值 ───────────────────────────────────────────
    print(bold("▶ Step 3 / 5  深度分析触发阈值"))
    print(gray("  论文评分 ≥ 此阈值时，自动触发深读（paper-analyze）"))

    if use_defaults:
        deep_threshold = 4.5
    else:
        threshold_choices = [
            ("3.5", "宽松 (3.5) — 更多论文进入深读队列"),
            ("4.5", "标准 (4.5) — 推荐，只有高度相关才触发（默认）"),
            ("6.0", "严格 (6.0) — 仅最顶尖论文触发"),
        ]
        threshold_key = ask_choice(
            "深度分析触发阈值",
            threshold_choices,
            default="4.5",
        )
        deep_threshold = float(threshold_key)

    print(green(f"  ✓ 阈值: {deep_threshold}"))
    print()

    # ── Step 4: 排除关键词 ───────────────────────────────────────────
    print(bold("▶ Step 4 / 5  自定义排除词（可选）"))
    print(gray("  论文/内容标题中含这些词会被过滤，多个词用逗号分隔"))

    if use_defaults:
        extra_excluded_raw = ""
    else:
        extra_excluded_raw = ask(
            "输入额外排除关键词",
            default="",
            hint="示例: cryptocurrency,blockchain,NFT",
        )

    extra_excluded = [k.strip() for k in extra_excluded_raw.split(",") if k.strip()]
    print(green(f"  ✓ 额外排除词: {extra_excluded or '无'}"))
    print()

    # ── .env 检测（V1.2 新增）──────────────────────────────────────────
    try:
        from scripts.path_utils import check_env_file
    except ImportError:
        try:
            from path_utils import check_env_file
        except ImportError:
            check_env_file = lambda: {"exists": False, "has_openai_key": False, "missing_warning": ""}

    env_info = check_env_file()
    if env_info.get("missing_warning") or not env_info.get("has_openai_key"):
        print()
        print(yellow("  ⚠  LLM 配置提示"))
        print(gray("    破晓的「聚类与总结魔法」需要 OpenAI API Key 才能生效。"))
        print(gray("    未配置时，系统将使用关键词降级模式（效果较差）。"))
        print()

        if not use_defaults:
            create_env = confirm(
                "  是否现在创建 .env 文件？",
                default=True,
            )
            if create_env:
                openai_key = ask(
                    "  请输入 OPENAI_API_KEY",
                    default="",
                    hint="格式：sk-...",
                )
                base_url = ask(
                    "  请输入 OPENAI_BASE_URL（可选，代理地址）",
                    default="",
                    hint="如 https://api.openai-proxy.org/v1",
                )

                env_path = Path(work_dir) / ".env"
                env_lines = ["# 破晓 PoXiao LLM 配置\n"]
                if openai_key:
                    env_lines.append(f"OPENAI_API_KEY={openai_key}\n")
                if base_url:
                    env_lines.append(f"OPENAI_BASE_URL={base_url}\n")

                if len(env_lines) > 1:
                    env_path.write_text("".join(env_lines), encoding="utf-8")
                    print(green("  ✓ .env 文件已创建"))
                    # 立即加载环境变量
                    os.environ["OPENAI_API_KEY"] = openai_key
                    if base_url:
                        os.environ["OPENAI_BASE_URL"] = base_url
                else:
                    print(yellow("  ⚠ 未输入有效 Key，跳过创建"))
                print()

    # ── Step 5: 定时任务 ─────────────────────────────────────────────
    print(bold("▶ Step 5 / 5  自动运行配置"))

    if use_defaults:
        schedule = "skip"
    else:
        schedule = ask_choice(
            "希望如何自动运行破晓？",
            SCHEDULE_OPTIONS,
            default="launchd",
        )

    print()

    # ── Step 5b: Semantic Scholar API Key（可选）──────────────────────
    s2_api_key = ""
    if not use_defaults:
        print(bold("▶ 附加配置（可选）"))
        s2_api_key = ask(
            "Semantic Scholar API Key（有 Key 可大幅提升并发额度，没有则回车跳过）",
            default="",
            hint="获取地址：https://www.semanticscholar.org/product/api",
        )

    # ── 生成 Profile ─────────────────────────────────────────────────
    print(bold("⚙  正在生成配置文件..."))

    try:
        import yaml  # 验证 yaml 可用
    except ImportError:
        print(red("  ✗ 缺少依赖：pip install pyyaml"))
        sys.exit(1)

    yaml_content = build_profile_yaml(
        username=username,
        display_name=display_name,
        domains=selected_domains,
        business=selected_business,
        deep_threshold=deep_threshold,
        extra_excluded=extra_excluded,
        s2_api_key=s2_api_key,
    )

    profile_path.write_text(yaml_content, encoding="utf-8")
    print(green(f"  ✓ Profile 已保存: {profile_path.relative_to(work_dir)}"))

    # 若是 default 用户，同时创建 .poxiao_system/profiles/default.yaml
    if username == "default":
        default_link = profiles_dir / "default.yaml"
        if not default_link.exists():
            shutil.copy2(str(profile_path), str(default_link))
            print(green(f"  ✓ 默认 profile 已同步: .poxiao_system/profiles/default.yaml"))

    # ── 定时任务 ─────────────────────────────────────────────────────
    sched_dir = Path(work_dir) / "schedules"
    sched_dir.mkdir(exist_ok=True)

    if schedule == "launchd":
        plist_content = gen_launchd_plist(username, work_dir, python_path)
        plist_file = sched_dir / f"com.poxiao.briefing.{username}.plist"
        plist_file.write_text(plist_content, encoding="utf-8")

        print()
        print(bold("  📅 macOS launchd 定时任务"))
        installed = install_launchd(plist_content, username, work_dir)
        if installed:
            print(green(f"  ✓ launchd 已自动加载 — 每个工作日 09:00 自动运行"))
        else:
            print(yellow(f"  ⚠ 自动加载失败，请手动执行："))
            print(gray(f"    cp {plist_file} ~/Library/LaunchAgents/"))
            print(gray(f"    launchctl load -w ~/Library/LaunchAgents/com.poxiao.briefing.{username}.plist"))

    elif schedule == "crontab":
        cron_entry = gen_crontab_entry(username, work_dir, python_path)
        cron_file = sched_dir / f"crontab_{username}.txt"
        cron_file.write_text(cron_entry, encoding="utf-8")

        print()
        print(bold("  📅 crontab 定时任务"))
        print(gray(f"  规则已保存至: {cron_file.relative_to(work_dir)}"))
        print(gray("  执行以下命令安装："))
        print(cyan(f"    (crontab -l 2>/dev/null; cat {cron_file}) | crontab -"))

    elif schedule == "once":
        print()
        print(bold("  🚀 立即运行一次"))
        print(gray(f"    python poxiao.py generate --user {username}"))
        run_now = confirm("  现在立即运行？", default=True)
        if run_now:
            print()
            subprocess.run(
                [python_path, str(Path(work_dir) / "poxiao.py"),
                 "generate", "--user", username],
                cwd=work_dir,
            )

    # ── 完成 ─────────────────────────────────────────────────────────
    print()
    print(hr("═"))
    print()
    print(f"  {bold(green('✅ 配置完成！'))}")
    print()
    print(f"  {bold('快速上手：')}")
    print(f"    {cyan('python poxiao.py generate --user ' + username)}")
    print(f"    {cyan('python poxiao.py analyze 2401.12345 --user ' + username)}")
    print()
    print(f"  {bold('配置文件：')} {gray(str(profile_path))}")
    print(f"  {bold('输出目录：')} {gray(str(Path(work_dir) / 'data' / username))}")
    print()
    print(hr("═"))
    print()


# --------------------------------------------------------------------------
# CLI 入口
# --------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="破晓 PoXiao — 傻瓜式初始化配置引导",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            示例：
              python setup.py                   # 交互式引导
              python setup.py --user andy      # 跳过用户名询问
              python setup.py --defaults        # 全部默认值（CI/CD）
        """),
    )
    parser.add_argument("--user", help="预设用户名（跳过询问）")
    parser.add_argument(
        "--defaults",
        action="store_true",
        help="全部使用默认值，无需交互（适合 CI/脚本调用）",
    )
    args = parser.parse_args()

    try:
        run_setup(preset_user=args.user, use_defaults=args.defaults)
    except KeyboardInterrupt:
        print(f"\n\n  {gray('已取消配置，再见！')}\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
