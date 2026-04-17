"""
retry.py — 破晓 (PoXiao) 生产级网络请求防爆兜底装饰器

设计原则：
  1. 单一职责：只做重试/超时/降级逻辑，不关心业务
  2. 零强依赖：优先使用 tenacity（若安装），否则内置纯标准库实现
  3. 优雅降级：任何信源/API 彻底失败后，记录日志 + 返回默认值，
               绝不向上抛出未处理异常，不影响后续信源的处理
  4. 可观测：所有重试、失败事件记录到结构化日志，
             并收集到全局 WarningCollector 供最终报告显示友好提示

用法：
    from scripts.retry import resilient, WarningCollector

    @resilient(
        source_name="HackerNews",
        max_attempts=3,
        timeout_seconds=10,
        fallback=[],         # 失败时返回此值（None 会自动推断空类型）
    )
    def fetch_hn_stories(n: int) -> list[dict]:
        ...

    # 在最终 Markdown 生成时获取所有警告
    warnings = WarningCollector.get_all()
    if warnings:
        header = "\\n".join(f"> ⚠️ {w}" for w in warnings)
"""

from __future__ import annotations

import functools
import logging
import random
import socket
import time
from collections import deque
from typing import Any, Callable, TypeVar

logger = logging.getLogger(__name__)

F = TypeVar("F", bound=Callable[..., Any])


# --------------------------------------------------------------------------
# 全局警告收集器（线程安全的简化版）
# --------------------------------------------------------------------------

class WarningCollector:
    """
    收集全局运行警告，最终写入简报头部。

    使用方式：
        WarningCollector.add("HackerNews 抓取超时，已跳过")
        warnings = WarningCollector.get_all()
    """
    _queue: deque[str] = deque()

    @classmethod
    def add(cls, message: str) -> None:
        cls._queue.append(message)
        logger.warning("[PoXiao Warning] %s", message)

    @classmethod
    def get_all(cls) -> list[str]:
        return list(cls._queue)

    @classmethod
    def clear(cls) -> None:
        cls._queue.clear()

    @classmethod
    def render_markdown_header(cls) -> str:
        """返回适合插入 Markdown 头部的警告区块（空则返回 ''）"""
        warnings = cls.get_all()
        if not warnings:
            return ""
        lines = ["> **⚠️ 数据完整性提示**（部分信源今日未能正常抓取）\n>"]
        for w in warnings:
            lines.append(f"> - {w}")
        lines.append("")
        return "\n".join(lines)


# --------------------------------------------------------------------------
# 内置轻量重试（无 tenacity 时的 fallback 实现）
# --------------------------------------------------------------------------

_RETRYABLE_EXCEPTIONS = (
    OSError,
    TimeoutError,
    socket.timeout,
    ConnectionError,
    ConnectionResetError,
    ConnectionRefusedError,
)

# 动态追加：urllib 超时异常
try:
    import urllib.error
    _RETRYABLE_EXCEPTIONS = _RETRYABLE_EXCEPTIONS + (urllib.error.URLError,)
except ImportError:
    pass

# 动态追加：requests 异常
try:
    import requests.exceptions as _req_exc
    _RETRYABLE_EXCEPTIONS = _RETRYABLE_EXCEPTIONS + (
        _req_exc.ConnectionError,
        _req_exc.Timeout,
        _req_exc.ChunkedEncodingError,
    )
except ImportError:
    pass

# 动态追加：httpx 异常
try:
    import httpx
    _RETRYABLE_EXCEPTIONS = _RETRYABLE_EXCEPTIONS + (
        httpx.TimeoutException,
        httpx.ConnectError,
        httpx.RemoteProtocolError,
    )
except ImportError:
    pass


def _is_retryable(exc: BaseException) -> bool:
    """判断异常是否值得重试（网络/超时类）"""
    if isinstance(exc, _RETRYABLE_EXCEPTIONS):
        return True
    # HTTP 5xx 通常可重试
    status = getattr(exc, "response", None)
    if status is not None:
        code = getattr(status, "status_code", None) or getattr(status, "code", None)
        if code and code >= 500:
            return True
    return False


def _backoff_wait(attempt: int, base: float, jitter: float) -> None:
    """指数退避 + 随机抖动"""
    delay = min(base * (2 ** attempt) + random.uniform(0, jitter), 60.0)
    logger.debug("Retry backoff: %.1f s (attempt %d)", delay, attempt + 1)
    time.sleep(delay)


# --------------------------------------------------------------------------
# 核心装饰器：@resilient
# --------------------------------------------------------------------------

def resilient(
    source_name: str,
    max_attempts: int = 3,
    timeout_seconds: float | None = 15.0,
    backoff_base: float = 1.0,
    backoff_jitter: float = 0.5,
    fallback: Any = None,
    warn_on_failure: bool = True,
) -> Callable[[F], F]:
    """
    生产级重试 + 降级装饰器。

    Args:
        source_name:      信源/模块名称（用于日志和警告提示）
        max_attempts:     最大尝试次数（含首次）
        timeout_seconds:  单次调用超时（秒）；None = 不设置超时
        backoff_base:     指数退避基础等待时间（秒）
        backoff_jitter:   随机抖动范围（秒）
        fallback:         彻底失败时的返回值（默认 None）
        warn_on_failure:  失败后是否向 WarningCollector 登记

    Example:
        @resilient(source_name="ArXiv API", max_attempts=3, fallback=[])
        def search_arxiv(query: str) -> list[dict]:
            ...
    """
    def decorator(func: F) -> F:

        # ── 尝试使用 tenacity（更完整的重试库）──────────────────────────
        try:
            from tenacity import (
                retry,
                stop_after_attempt,
                wait_exponential_jitter,
                retry_if_exception,
                before_sleep_log,
            )

            _tenacity_retry = retry(
                stop=stop_after_attempt(max_attempts),
                wait=wait_exponential_jitter(initial=backoff_base, jitter=backoff_jitter),
                retry=retry_if_exception(_is_retryable),
                before_sleep=before_sleep_log(logger, logging.WARNING),
                reraise=True,
            )

            @functools.wraps(func)
            def tenacity_wrapper(*args: Any, **kwargs: Any) -> Any:
                try:
                    return _tenacity_retry(func)(*args, **kwargs)
                except Exception as exc:
                    _handle_failure(source_name, exc, warn_on_failure, fallback)
                    return fallback

            return tenacity_wrapper  # type: ignore[return-value]

        except ImportError:
            pass  # 降级到内置实现

        # ── 内置重试实现 ────────────────────────────────────────────────
        @functools.wraps(func)
        def builtin_wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exc: Exception | None = None

            for attempt in range(max_attempts):
                try:
                    if timeout_seconds is not None:
                        # 使用 signal-based timeout（仅 Unix 主线程有效）
                        return _call_with_timeout(func, timeout_seconds, *args, **kwargs)
                    return func(*args, **kwargs)

                except Exception as exc:
                    last_exc = exc
                    if attempt < max_attempts - 1 and _is_retryable(exc):
                        logger.warning(
                            "[%s] 第 %d/%d 次尝试失败: %s, %.1fs 后重试...",
                            source_name, attempt + 1, max_attempts, exc,
                            backoff_base * (2 ** attempt),
                        )
                        _backoff_wait(attempt, backoff_base, backoff_jitter)
                    else:
                        break

            _handle_failure(source_name, last_exc, warn_on_failure, fallback)
            return fallback

        return builtin_wrapper  # type: ignore[return-value]

    return decorator


def _call_with_timeout(
    func: Callable,
    timeout: float,
    *args: Any,
    **kwargs: Any,
) -> Any:
    """
    用 signal.alarm 实现超时（仅适用于 Unix 主线程）。
    非 Unix 或非主线程时直接透传调用。
    """
    import signal
    import threading

    if not hasattr(signal, "SIGALRM") or threading.current_thread() is not threading.main_thread():
        return func(*args, **kwargs)

    def _handler(signum: int, frame: Any) -> None:
        raise TimeoutError(f"调用超时（{timeout}s）")

    old_handler = signal.signal(signal.SIGALRM, _handler)
    signal.setitimer(signal.ITIMER_REAL, timeout)
    try:
        return func(*args, **kwargs)
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, old_handler)


def _handle_failure(
    source_name: str,
    exc: Exception | None,
    warn: bool,
    fallback: Any,
) -> None:
    """彻底失败后的统一处理：记录日志 + 写入 WarningCollector"""
    msg = f"[{source_name}] 多次重试后仍然失败: {exc}"
    logger.error(msg)

    if warn:
        # 生成用户友好的中文提示
        friendly = _friendly_warning(source_name, exc)
        WarningCollector.add(friendly)


def _friendly_warning(source_name: str, exc: Exception | None) -> str:
    """将技术异常转换为用户友好的中文提示"""
    exc_str = str(exc) if exc else "未知错误"

    if "timeout" in exc_str.lower() or isinstance(exc, (TimeoutError, socket.timeout)):
        reason = "抓取超时"
    elif "429" in exc_str or "rate limit" in exc_str.lower():
        reason = "API 访问频率限制（429 Too Many Requests）"
    elif "403" in exc_str or "forbidden" in exc_str.lower():
        reason = "访问被拒绝（403 Forbidden）"
    elif "404" in exc_str:
        reason = "资源不存在（404 Not Found）"
    elif "ssl" in exc_str.lower() or "certificate" in exc_str.lower():
        reason = "SSL 证书验证失败"
    elif "dns" in exc_str.lower() or "name resolution" in exc_str.lower():
        reason = "DNS 解析失败"
    else:
        reason = f"网络错误（{exc_str[:60]}）"

    return f"今日 **{source_name}** 源 {reason}，暂未收录相关内容"


# --------------------------------------------------------------------------
# 便捷预设：常见信源的装饰器工厂
# --------------------------------------------------------------------------

def hn_resilient(fallback: Any = None) -> Callable[[F], F]:
    """HackerNews 专用（海外网络，超时常见）"""
    return resilient("HackerNews", max_attempts=3, timeout_seconds=12, fallback=fallback)


def arxiv_resilient(fallback: Any = None) -> Callable[[F], F]:
    """arXiv API 专用（服务稳定但有时慢）"""
    return resilient("arXiv API", max_attempts=4, timeout_seconds=20,
                     backoff_base=2.0, fallback=fallback)


def s2_resilient(fallback: Any = None) -> Callable[[F], F]:
    """Semantic Scholar 专用（公开 API 限流严重）"""
    return resilient("Semantic Scholar", max_attempts=3, timeout_seconds=15,
                     backoff_base=3.0, backoff_jitter=2.0, fallback=fallback)


def rss_resilient(source_name: str = "RSS", fallback: Any = None) -> Callable[[F], F]:
    """RSS 源通用（快速失败，单条不影响整体）"""
    return resilient(source_name, max_attempts=2, timeout_seconds=8,
                     backoff_base=0.5, fallback=fallback)


def reddit_resilient(fallback: Any = None) -> Callable[[F], F]:
    """Reddit API 专用"""
    return resilient("Reddit", max_attempts=3, timeout_seconds=10,
                     backoff_base=1.5, fallback=fallback)


# --------------------------------------------------------------------------
# 批量执行器：safe_gather
# --------------------------------------------------------------------------

def safe_gather(
    tasks: list[tuple[Callable, tuple, dict]],
    source_names: list[str] | None = None,
) -> list[Any]:
    """
    顺序执行多个任务，每个任务独立捕获异常，互不影响。

    Args:
        tasks: [(callable, args_tuple, kwargs_dict), ...]
        source_names: 对应的信源名称（用于错误日志）

    Returns:
        每个任务的返回值列表（失败的位置为 None）

    Example:
        results = safe_gather([
            (fetch_hn, (30,), {}),
            (fetch_reddit, ("LocalLLaMA",), {}),
            (fetch_rss, ("https://example.com/feed",), {}),
        ], source_names=["HN", "Reddit/LocalLLaMA", "example RSS"])
    """
    results: list[Any] = []
    names = source_names or [f"Task-{i}" for i in range(len(tasks))]

    for (func, args, kwargs), name in zip(tasks, names):
        try:
            result = func(*args, **kwargs)
            results.append(result)
        except Exception as exc:
            logger.error("[safe_gather] %s 执行失败: %s", name, exc)
            WarningCollector.add(_friendly_warning(name, exc))
            results.append(None)

    return results


# --------------------------------------------------------------------------
# 单元测试（python -m scripts.retry）
# --------------------------------------------------------------------------

if __name__ == "__main__":
    import sys
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s %(name)s: %(message)s")

    print("\n=== 测试 1: 正常成功 ===")
    @resilient(source_name="Test-OK", fallback=[])
    def always_ok() -> list[int]:
        return [1, 2, 3]
    print(f"Result: {always_ok()}")

    print("\n=== 测试 2: 超时后降级 ===")
    @resilient(source_name="Test-Timeout", max_attempts=2, timeout_seconds=1, fallback={"error": True})
    def always_slow() -> dict:
        time.sleep(5)
        return {}
    result = always_slow()
    print(f"Result: {result}")
    print(f"Warnings: {WarningCollector.get_all()}")

    print("\n=== 测试 3: 网络错误重试后降级 ===")
    attempt_count = {"n": 0}

    @resilient(source_name="Test-Flaky", max_attempts=3, backoff_base=0.1, fallback=[])
    def flaky_fetch() -> list:
        attempt_count["n"] += 1
        if attempt_count["n"] < 3:
            raise ConnectionError("模拟网络抖动")
        return ["ok"]

    result = flaky_fetch()
    print(f"Result: {result} (attempts: {attempt_count['n']})")

    print("\n=== Markdown 警告头部 ===")
    print(WarningCollector.render_markdown_header())
