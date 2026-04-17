"""
path_utils.py — 破晓 PoXiao V1.2 路径定义模块

设计原则：
  1. 系统层与用户层物理隔离：
     - .poxiao_system/  — 配置、脚本、缓存、原始数据（隐藏）
     - PoXiao_Briefs/   — 最终简报产物（扁平化输出）
  2. 所有路径读写必须经过此模块，禁止硬编码路径字符串
  3. 自动创建缺失目录，零手动初始化

目录结构：
  WORK_DIR/
    ├── .poxiao_system/
    │   ├── profiles/
    │   ├── scripts/
    │   ├── cache/
    │   └── raw/{date}/
    └── PoXiao_Briefs/
        └── {date}_{display_name}的{类型}.md
"""

from __future__ import annotations

import os
import re
from datetime import datetime
from pathlib import Path
from typing import Any

# --------------------------------------------------------------------------
# 工作目录定位
# --------------------------------------------------------------------------

def get_work_dir() -> Path:
    """
    返回项目根目录（poxiao.py 所在目录）。
    支持从任意子脚本调用时正确定位。
    """
    return Path(__file__).parent.parent.parent


def get_system_dir() -> Path:
    """返回 .poxiao_system/ 目录（自动创建）"""
    system_dir = get_work_dir() / ".poxiao_system"
    system_dir.mkdir(exist_ok=True)
    return system_dir


def get_briefs_dir() -> Path:
    """返回 PoXiao_Briefs/ 输出目录（自动创建）"""
    briefs_dir = get_work_dir() / "PoXiao_Briefs"
    briefs_dir.mkdir(exist_ok=True)
    return briefs_dir


# --------------------------------------------------------------------------
# 系统层路径（.poxiao_system/）
# --------------------------------------------------------------------------

def get_profiles_dir() -> Path:
    """返回 .poxiao_system/profiles/"""
    profiles_dir = get_system_dir() / "profiles"
    profiles_dir.mkdir(exist_ok=True)
    return profiles_dir


def get_profile_path(username: str) -> Path:
    """
    返回 profiles/profile_{username}.yaml。
    不存在时 fallback 到 default.yaml，再 fallback 到根目录 profile.yaml（历史兼容）。
    """
    profiles_dir = get_profiles_dir()
    path = profiles_dir / f"profile_{username}.yaml"
    if path.exists():
        return path
    default = profiles_dir / "default.yaml"
    if default.exists():
        return default
    # 历史兼容：根目录 profile.yaml
    legacy = get_work_dir() / "profile.yaml"
    if legacy.exists():
        return legacy
    raise FileNotFoundError(
        f"找不到用户 '{username}' 的 profile。\n"
        f"请先运行: python poxiao.py setup --user {username}"
    )


def get_scripts_dir() -> Path:
    """返回 .poxiao_system/scripts/"""
    scripts_dir = get_system_dir() / "scripts"
    scripts_dir.mkdir(exist_ok=True)
    return scripts_dir


def get_cache_dir() -> Path:
    """返回 .poxiao_system/cache/"""
    cache_dir = get_system_dir() / "cache"
    cache_dir.mkdir(exist_ok=True)
    return cache_dir


def get_cache_db_path() -> Path:
    """返回 SQLite 缓存数据库路径"""
    return get_cache_dir() / "s2_papers.db"


def get_raw_dir(date_str: str | None = None) -> Path:
    """
    返回 .poxiao_system/raw/{date}/ 原始数据目录。
    日期格式：YYYY-MM-DD
    """
    date = date_str or datetime.now().strftime("%Y-%m-%d")
    raw_dir = get_system_dir() / "raw" / date
    raw_dir.mkdir(parents=True, exist_ok=True)
    return raw_dir


def get_fetched_json_path(date_str: str | None = None) -> Path:
    """返回 fetched.json 路径"""
    return get_raw_dir(date_str) / "fetched.json"


def get_papers_json_path(date_str: str | None = None) -> Path:
    """返回 papers.json 路径"""
    return get_raw_dir(date_str) / "papers.json"


def get_clustered_json_path(date_str: str | None = None) -> Path:
    """返回 clustered.json 路径"""
    return get_raw_dir(date_str) / "clustered.json"


# --------------------------------------------------------------------------
# 用户层路径（PoXiao_Briefs/）
# --------------------------------------------------------------------------

def get_briefing_filename(
    date_str: str,
    display_name: str,
    report_type: str,
) -> str:
    """
    规范化简报文件名：{date}_{display_name}的{类型}.md
    示例：2026-04-17_Andy的学术概览.md
    """
    type_map = {
        "academic":  "学术概览",
        "community": "社区速递",
        "finance":   "财经简报",
        "index":     "今日索引",
    }
    type_label = type_map.get(report_type, report_type)
    # 清理 display_name 中的非法字符
    safe_name = re.sub(r'[<>:"/\\|？*]', '', display_name)
    return f"{date_str}_{safe_name}的{type_label}.md"


def get_briefing_path(
    date_str: str,
    display_name: str,
    report_type: str,
) -> Path:
    """返回简报文件的完整路径"""
    filename = get_briefing_filename(date_str, display_name, report_type)
    return get_briefs_dir() / filename


def list_briefs(limit: int = 10) -> list[Path]:
    """列出最近的简报文件（按修改时间倒序）"""
    briefs_dir = get_briefs_dir()
    files = sorted(briefs_dir.glob("*.md"), key=lambda f: f.stat().st_mtime, reverse=True)
    return files[:limit]


# --------------------------------------------------------------------------
# 用户信息工具
# --------------------------------------------------------------------------

def get_display_name(username: str) -> str:
    """
    从 profile.yaml 读取 meta.display_name，失败时返回 username。
    """
    try:
        import yaml
        path = get_profile_path(username)
        with open(path, encoding="utf-8") as f:
            cfg = yaml.safe_load(f) or {}
        return cfg.get("meta", {}).get("display_name", username)
    except Exception:
        return username


def auto_detect_days() -> int:
    """周一返回 3（覆盖周末），其余工作日返回 1"""
    weekday = datetime.now().weekday()  # 0=Monday
    return 3 if weekday == 0 else 1


# --------------------------------------------------------------------------
# 环境检测（.env）
# --------------------------------------------------------------------------

def check_env_file() -> dict[str, Any]:
    """
    检查根目录 .env 文件，返回检测结果。
    如果 .env 存在，自动加载其中的环境变量（不覆盖已设置的）。
    """
    env_file = get_work_dir() / ".env"
    result = {
        "exists": env_file.exists(),
        "has_openai_key": False,
        "has_base_url": False,
        "missing_warning": "",
    }

    if not result["exists"]:
        result["missing_warning"] = (
            "⚠️ 未检测到 .env 文件。\n"
            "   破晓的‘LLM 聚类与总结魔法’需要 OpenAI API Key 才能生效。\n"
            "   建议在项目根目录创建 .env 文件并填入：\n"
            "     OPENAI_API_KEY=sk-...\n"
            "     OPENAI_BASE_URL=https://your-proxy (可选)"
        )
        return result

    # 解析 .env
    try:
        with open(env_file, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, value = line.split("=", 1)
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                if key == "OPENAI_API_KEY" and value:
                    result["has_openai_key"] = True
                elif key == "OPENAI_BASE_URL" and value:
                    result["has_base_url"] = True
    except Exception:
        pass

    if not result["has_openai_key"]:
        result["missing_warning"] = (
            "⚠️ .env 文件中未找到有效的 OPENAI_API_KEY。\n"
            "   破晓的「LLM 聚类与总结魔法」需要 OpenAI API Key 才能生效。"
        )

    return result


def load_env_if_needed() -> None:
    """
    如果 .env 存在且 python-dotenv 已安装，自动加载环境变量（不覆盖已设置的）。
    """
    env_file = get_work_dir() / ".env"
    if not env_file.exists():
        return

    try:
        from dotenv import load_dotenv as _load_dotenv
        _load_dotenv(env_file, override=False)
    except ImportError:
        # 手动加载（不依赖 python-dotenv）
        with open(env_file, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, value = line.split("=", 1)
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                if key not in os.environ:
                    os.environ[key] = value


# --------------------------------------------------------------------------
# CLI（路径管理工具）
# --------------------------------------------------------------------------

if __name__ == "__main__":
    import json
    import sys

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")

    print("\n=== 破晓 PoXiao 路径检测 ===\n")

    print(f"工作目录:       {get_work_dir()}")
    print(f"系统目录:       {get_system_dir()}")
    print(f"简报输出目录:   {get_briefs_dir()}")
    print(f"Profiles 目录:  {get_profiles_dir()}")
    print(f"缓存数据库:     {get_cache_db_path()}")
    print(f"原始数据目录:   {get_raw_dir()}")
    print()

    env_check = check_env_file()
    print(f".env 文件:       {'✅ 存在' if env_check['exists'] else '❌ 不存在'}")
    print(f"  OPENAI_API_KEY: {'✅' if env_check['has_openai_key'] else '❌'}")
    print(f"  OPENAI_BASE_URL: {'✅' if env_check['has_base_url'] else '❌'}")
    if env_check["missing_warning"]:
        print(f"\n{env_check['missing_warning']}")

    recent = list_briefs(5)
    if recent:
        print(f"\n最近 {len(recent)} 份简报:")
        for f in recent:
            print(f"  {f.name}  ({f.stat().st_size} bytes)")
    else:
        print("\n尚未生成任何简报。运行 python poxiao.py generate 开始。")
