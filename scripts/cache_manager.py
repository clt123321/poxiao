"""
cache_manager.py — 破晓 PoXiao S2 论文缓存层 + 智能熔断器

解决问题：
  Semantic Scholar 公开 API 在串行多 Query 场景下极易触发 429 连环限流，
  旧代码 sleep(30) × N queries 导致主线程最坏挂起 240s+。

V1.1 解决方案：
  1. S2CircuitBreaker  — 全局熔断器，连续 2 次 429 后立即断路，跳过剩余请求
  2. S2PaperCache      — SQLite 本地缓存，论文核心字段 TTL=7天
  3. s2_resilient_v2   — 重构装饰器，优先读缓存，429 仅退避 5s + 重试 1 次

架构图：
  caller
    │
    ├─[cache hit?]──→ return cached_data (0 API calls)
    │
    └─[miss]──→ CircuitBreaker.is_open?
                    │
                    ├─[open]──→ WarningCollector + return []
                    │
                    └─[closed]──→ S2 API request
                                    │
                                    ├─[429]──→ sleep(5) + retry once
                                    │           ├─[ok]──→ cache + return
                                    │           └─[429 again]──→ CircuitBreaker.record_failure()
                                    │                            └─[trip?]──→ CircuitBreaker.open()
                                    │
                                    └─[ok]──→ cache + return
"""

from __future__ import annotations

import hashlib
import json
import logging
import os
import sqlite3
import time
import threading
from contextlib import contextmanager
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

# --------------------------------------------------------------------------
# 常量
# --------------------------------------------------------------------------

CACHE_TTL_DAYS      = 7       # 论文缓存有效期
S2_429_BACKOFF_SEC  = 5       # 429 后退避等待时间（秒）
S2_429_MAX_RETRIES  = 1       # 429 后最多重试次数（不含首次）
CB_FAILURE_THRESHOLD = 2      # 连续 N 次 429 后开路
CB_HALF_OPEN_SEC    = 3600    # 熔断后多少秒进入半开状态（允许探测）


# --------------------------------------------------------------------------
# S2 智能熔断器
# --------------------------------------------------------------------------

class S2CircuitBreaker:
    """
    线程安全的 Circuit Breaker，专用于 Semantic Scholar API。

    状态机：
      CLOSED  ──(连续 N 次 429)──→  OPEN
      OPEN    ──(超时 T 秒后)  ──→  HALF_OPEN
      HALF_OPEN ──(探测成功)   ──→  CLOSED
      HALF_OPEN ──(探测失败)   ──→  OPEN

    用法：
        if S2CircuitBreaker.is_open():
            return []            # 直接跳过，不发请求

        try:
            result = call_s2_api(...)
        except RateLimitError:
            S2CircuitBreaker.record_429()
            return []
        else:
            S2CircuitBreaker.record_success()
    """

    _lock             = threading.Lock()
    _consecutive_429  = 0           # 连续 429 计数
    _opened_at: float | None = None # 开路时间戳
    _state            = "CLOSED"    # CLOSED / OPEN / HALF_OPEN

    @classmethod
    def _now(cls) -> float:
        return time.monotonic()

    @classmethod
    def is_open(cls) -> bool:
        """
        检查熔断器是否开路（即：是否应跳过本次 S2 请求）。
        HALF_OPEN 状态允许一次探测通过。
        """
        with cls._lock:
            if cls._state == "CLOSED":
                return False
            if cls._state == "OPEN":
                # 检查是否已超时，可进入半开状态
                if cls._opened_at and cls._now() - cls._opened_at > CB_HALF_OPEN_SEC:
                    cls._state = "HALF_OPEN"
                    logger.info("[S2CircuitBreaker] 进入半开状态，允许一次探测请求")
                    return False  # 放行一次探测
                return True  # 仍在开路超时期内
            # HALF_OPEN: 放行探测
            return False

    @classmethod
    def record_429(cls) -> None:
        """记录一次 429 失败；连续失败达阈值则开路。"""
        with cls._lock:
            cls._consecutive_429 += 1
            logger.warning(
                "[S2CircuitBreaker] 429 记录 (%d/%d)",
                cls._consecutive_429, CB_FAILURE_THRESHOLD
            )
            if cls._consecutive_429 >= CB_FAILURE_THRESHOLD:
                cls._trip()

    @classmethod
    def record_success(cls) -> None:
        """记录一次成功；重置计数，关路。"""
        with cls._lock:
            cls._consecutive_429 = 0
            if cls._state != "CLOSED":
                logger.info("[S2CircuitBreaker] 探测成功，熔断器关路")
            cls._state = "CLOSED"
            cls._opened_at = None

    @classmethod
    def _trip(cls) -> None:
        """开路（内部调用，已持锁）"""
        cls._state = "OPEN"
        cls._opened_at = cls._now()
        logger.error(
            "[S2CircuitBreaker] 熔断器开路！连续 %d 次 429，"
            "当日剩余 S2 请求将全部跳过（%d 分钟后自动半开）",
            cls._consecutive_429, CB_HALF_OPEN_SEC // 60,
        )
        # 写入全局警告
        try:
            from scripts.retry import WarningCollector
        except ImportError:
            try:
                from retry import WarningCollector
            except ImportError:
                WarningCollector = None

        if WarningCollector:
            WarningCollector.add(
                "触发 Semantic Scholar API 熔断（连续限流），今日仅展示 arXiv 与本地缓存内容"
            )

    @classmethod
    def reset(cls) -> None:
        """手动重置（测试用）"""
        with cls._lock:
            cls._consecutive_429 = 0
            cls._state = "CLOSED"
            cls._opened_at = None


# --------------------------------------------------------------------------
# SQLite 论文缓存层
# --------------------------------------------------------------------------

class S2PaperCache:
    """
    轻量 SQLite 缓存，存储 Semantic Scholar 返回的论文核心字段。

    表结构：
      papers(
        arxiv_id          TEXT PRIMARY KEY,
        title             TEXT,
        abstract          TEXT,
        citation_count    INTEGER,
        influential_count INTEGER,
        authors_json      TEXT,    -- JSON array
        pub_date          TEXT,
        extra_json        TEXT,    -- 其余字段
        cached_at         REAL     -- Unix timestamp
      )

    TTL 策略：
      查询时检查 cached_at，超过 CACHE_TTL_DAYS 天则视为过期，需重新拉取。
    """

    _instance: "S2PaperCache | None" = None
    _lock = threading.Lock()

    def __init__(self, db_path: str | Path):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    # ── 单例工厂 ─────────────────────────────────────────────────────────

    @classmethod
    def get_instance(cls, work_dir: str | Path | None = None) -> "S2PaperCache":
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    base = Path(work_dir) if work_dir else Path(__file__).parent.parent
                    db_path = base / "data" / ".cache" / "s2_papers.db"
                    cls._instance = cls(db_path)
        return cls._instance

    # ── DB 初始化 ────────────────────────────────────────────────────────

    def _init_db(self) -> None:
        with self._connect() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS papers (
                    arxiv_id          TEXT PRIMARY KEY,
                    title             TEXT,
                    abstract          TEXT,
                    citation_count    INTEGER DEFAULT 0,
                    influential_count INTEGER DEFAULT 0,
                    authors_json      TEXT DEFAULT '[]',
                    pub_date          TEXT,
                    extra_json        TEXT DEFAULT '{}',
                    cached_at         REAL NOT NULL
                )
            """)
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_cached_at ON papers(cached_at)
            """)

    @contextmanager
    def _connect(self):
        conn = sqlite3.connect(str(self.db_path), timeout=10)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            conn.commit()
        finally:
            conn.close()

    # ── 读取 ─────────────────────────────────────────────────────────────

    def get(self, arxiv_id: str) -> dict | None:
        """
        查询缓存。
        返回值：
          - dict   → 缓存命中且未过期
          - None   → 不存在或已过期
        """
        cutoff = time.time() - CACHE_TTL_DAYS * 86400
        with self._connect() as conn:
            row = conn.execute(
                "SELECT * FROM papers WHERE arxiv_id = ? AND cached_at > ?",
                (arxiv_id, cutoff)
            ).fetchone()

        if row is None:
            return None

        paper = {
            "arxiv_id":                arxiv_id,
            "title":                   row["title"],
            "abstract":                row["abstract"],
            "citationCount":           row["citation_count"],
            "influentialCitationCount": row["influential_count"],
            "authors":                 json.loads(row["authors_json"] or "[]"),
            "publicationDate":         row["pub_date"],
            "_from_cache":             True,
            "_cached_at":              row["cached_at"],
        }
        # 合并 extra 字段
        try:
            extra = json.loads(row["extra_json"] or "{}")
            paper.update(extra)
        except json.JSONDecodeError:
            pass

        return paper

    def get_batch(self, arxiv_ids: list[str]) -> dict[str, dict]:
        """批量查询，返回 {arxiv_id: paper_dict}（仅未过期条目）"""
        if not arxiv_ids:
            return {}
        cutoff = time.time() - CACHE_TTL_DAYS * 86400
        placeholders = ",".join("?" * len(arxiv_ids))
        with self._connect() as conn:
            rows = conn.execute(
                f"SELECT * FROM papers WHERE arxiv_id IN ({placeholders}) AND cached_at > ?",
                (*arxiv_ids, cutoff)
            ).fetchall()

        result = {}
        for row in rows:
            paper = {
                "arxiv_id":                row["arxiv_id"],
                "title":                   row["title"],
                "abstract":                row["abstract"],
                "citationCount":           row["citation_count"],
                "influentialCitationCount": row["influential_count"],
                "authors":                 json.loads(row["authors_json"] or "[]"),
                "publicationDate":         row["pub_date"],
                "_from_cache":             True,
                "_cached_at":              row["cached_at"],
            }
            try:
                extra = json.loads(row["extra_json"] or "{}")
                paper.update(extra)
            except json.JSONDecodeError:
                pass
            result[row["arxiv_id"]] = paper

        return result

    # ── 写入 ─────────────────────────────────────────────────────────────

    def put(self, paper: dict) -> None:
        """缓存单篇论文"""
        arxiv_id = (
            paper.get("arxiv_id")
            or (paper.get("externalIds") or {}).get("ArXiv")
        )
        if not arxiv_id:
            return  # 无 arXiv ID 不缓存

        # 提取已知字段，其余存入 extra_json
        known_keys = {
            "arxiv_id", "title", "abstract", "citationCount",
            "influentialCitationCount", "authors", "publicationDate",
            "_from_cache", "_cached_at",
        }
        extra = {k: v for k, v in paper.items() if k not in known_keys}

        with self._connect() as conn:
            conn.execute("""
                INSERT OR REPLACE INTO papers
                  (arxiv_id, title, abstract, citation_count, influential_count,
                   authors_json, pub_date, extra_json, cached_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                arxiv_id,
                paper.get("title", ""),
                paper.get("abstract", ""),
                paper.get("citationCount", 0) or 0,
                paper.get("influentialCitationCount", 0) or 0,
                json.dumps(paper.get("authors", []), ensure_ascii=False),
                paper.get("publicationDate", ""),
                json.dumps(extra, ensure_ascii=False),
                time.time(),
            ))

    def put_batch(self, papers: list[dict]) -> int:
        """批量写入，返回实际写入条数"""
        count = 0
        for p in papers:
            try:
                self.put(p)
                count += 1
            except Exception as e:
                logger.debug("Cache put failed for %s: %s", p.get("arxiv_id"), e)
        return count

    # ── 维护 ─────────────────────────────────────────────────────────────

    def evict_expired(self) -> int:
        """删除过期条目，返回删除数量"""
        cutoff = time.time() - CACHE_TTL_DAYS * 86400
        with self._connect() as conn:
            cur = conn.execute("DELETE FROM papers WHERE cached_at <= ?", (cutoff,))
            return cur.rowcount

    def stats(self) -> dict:
        """返回缓存统计信息"""
        cutoff = time.time() - CACHE_TTL_DAYS * 86400
        with self._connect() as conn:
            total  = conn.execute("SELECT COUNT(*) FROM papers").fetchone()[0]
            fresh  = conn.execute(
                "SELECT COUNT(*) FROM papers WHERE cached_at > ?", (cutoff,)
            ).fetchone()[0]
            oldest = conn.execute(
                "SELECT MIN(cached_at) FROM papers"
            ).fetchone()[0]
        return {
            "total": total,
            "fresh": fresh,
            "expired": total - fresh,
            "oldest_cached_at": datetime.fromtimestamp(oldest).isoformat() if oldest else None,
            "db_path": str(self.db_path),
            "ttl_days": CACHE_TTL_DAYS,
        }


# --------------------------------------------------------------------------
# 高层接口：带缓存+熔断的 S2 批量查询
# --------------------------------------------------------------------------

def fetch_s2_papers_with_cache(
    query: str,
    start_date: "datetime",
    end_date: "datetime",
    top_k: int = 10,
    api_key: str | None = None,
    work_dir: str | Path | None = None,
) -> list[dict]:
    """
    带缓存 + 熔断器的 S2 查询接口。

    策略：
      1. 熔断器是否开路？→ 开路则直接返回 []
      2. 本次 query 的结果缓存（以 query_hash 为 key）是否命中？→ 命中返回
      3. 调用实际 S2 API，成功写缓存，429 写熔断记录

    注意：此函数仅做缓存/熔断的胶水层，实际 HTTP 调用
    仍然委托给 search_papers.py 中的 search_semantic_scholar_hot_papers()
    （为了不重复代码）。通过 monkey-patch 或直接 import 使用。
    """
    import sys
    scripts_dir = str(Path(__file__).parent)
    if scripts_dir not in sys.path:
        sys.path.insert(0, scripts_dir)

    # ── 熔断检查 ─────────────────────────────────────────────────────────
    if S2CircuitBreaker.is_open():
        logger.info("[S2Cache] 熔断器开路，跳过 S2 query: %s", query[:50])
        return []

    cache = S2PaperCache.get_instance(work_dir)

    # ── Query 级缓存（以 query+日期 hash 为 key）─────────────────────────
    query_hash = _query_hash(query, start_date, end_date, top_k)
    cached_result = _get_query_cache(cache, query_hash)
    if cached_result is not None:
        logger.info("[S2Cache] Query 缓存命中: %s (hash=%s)", query[:40], query_hash[:8])
        return cached_result

    # ── 调用 S2 API（带重试 + 熔断记录）─────────────────────────────────
    from search_papers import search_semantic_scholar_hot_papers

    last_exc: Exception | None = None
    for attempt in range(S2_429_MAX_RETRIES + 1):
        try:
            papers = search_semantic_scholar_hot_papers(
                query=query,
                start_date=start_date,
                end_date=end_date,
                top_k=top_k,
                api_key=api_key,
            )
            # 成功：写缓存 + 重置熔断
            S2CircuitBreaker.record_success()
            cache.put_batch(papers)
            _put_query_cache(cache, query_hash, papers)
            logger.info("[S2Cache] S2 API 成功，写入 %d 篇到缓存", len(papers))
            return papers

        except Exception as exc:
            last_exc = exc
            exc_str = str(exc)
            is_429 = "429" in exc_str or "Too Many Requests" in exc_str.lower()

            if is_429:
                S2CircuitBreaker.record_429()
                if S2CircuitBreaker.is_open():
                    logger.warning("[S2Cache] 熔断器刚开路，终止重试")
                    return []
                if attempt < S2_429_MAX_RETRIES:
                    logger.warning(
                        "[S2Cache] 429 限流，等待 %ds 后重试 (attempt %d/%d)...",
                        S2_429_BACKOFF_SEC, attempt + 1, S2_429_MAX_RETRIES + 1
                    )
                    time.sleep(S2_429_BACKOFF_SEC)
            else:
                logger.warning("[S2Cache] S2 请求失败（非限流）: %s", exc)
                break  # 非限流错误不重试

    logger.error("[S2Cache] S2 query 最终失败: %s", last_exc)
    return []


# --------------------------------------------------------------------------
# Query 级缓存（存在 SQLite extra 表中）
# --------------------------------------------------------------------------

def _query_hash(query: str, start_date: "datetime", end_date: "datetime", top_k: int) -> str:
    """生成 query 的唯一 hash key"""
    raw = f"{query}|{start_date.date()}|{end_date.date()}|{top_k}"
    return hashlib.md5(raw.encode()).hexdigest()


def _get_query_cache(cache: S2PaperCache, query_hash: str) -> list[dict] | None:
    """从 SQLite extra 表读取 query 级缓存"""
    try:
        with cache._connect() as conn:
            # 用 extra 表存储 query → arxiv_ids 映射
            conn.execute("""
                CREATE TABLE IF NOT EXISTS query_cache (
                    query_hash TEXT PRIMARY KEY,
                    arxiv_ids_json TEXT,
                    cached_at REAL
                )
            """)
            cutoff = time.time() - CACHE_TTL_DAYS * 86400
            row = conn.execute(
                "SELECT arxiv_ids_json FROM query_cache WHERE query_hash = ? AND cached_at > ?",
                (query_hash, cutoff)
            ).fetchone()
            if row is None:
                return None
            arxiv_ids = json.loads(row[0])
        # 批量读取论文详情
        papers = list(cache.get_batch(arxiv_ids).values())
        if len(papers) < len(arxiv_ids) * 0.5:
            # 超过一半的论文详情缓存失效，视为 query cache miss
            return None
        return papers
    except Exception as e:
        logger.debug("Query cache read failed: %s", e)
        return None


def _put_query_cache(cache: S2PaperCache, query_hash: str, papers: list[dict]) -> None:
    """写入 query 级缓存"""
    arxiv_ids = [
        p.get("arxiv_id") or (p.get("externalIds") or {}).get("ArXiv")
        for p in papers
    ]
    arxiv_ids = [aid for aid in arxiv_ids if aid]
    try:
        with cache._connect() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS query_cache (
                    query_hash TEXT PRIMARY KEY,
                    arxiv_ids_json TEXT,
                    cached_at REAL
                )
            """)
            conn.execute("""
                INSERT OR REPLACE INTO query_cache (query_hash, arxiv_ids_json, cached_at)
                VALUES (?, ?, ?)
            """, (query_hash, json.dumps(arxiv_ids), time.time()))
    except Exception as e:
        logger.debug("Query cache write failed: %s", e)


# --------------------------------------------------------------------------
# CLI（缓存管理工具）
# --------------------------------------------------------------------------

if __name__ == "__main__":
    import argparse
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")

    parser = argparse.ArgumentParser(description="破晓 S2 缓存管理工具")
    sub = parser.add_subparsers(dest="cmd")
    sub.add_parser("stats",  help="显示缓存统计")
    sub.add_parser("evict",  help="删除过期条目")
    sub.add_parser("reset",  help="重置熔断器状态")
    p_get = sub.add_parser("get", help="查询单篇缓存")
    p_get.add_argument("arxiv_id")
    args = parser.parse_args()

    cache = S2PaperCache.get_instance()

    if args.cmd == "stats":
        s = cache.stats()
        print(json.dumps(s, ensure_ascii=False, indent=2))

    elif args.cmd == "evict":
        n = cache.evict_expired()
        print(f"已删除 {n} 条过期缓存")

    elif args.cmd == "reset":
        S2CircuitBreaker.reset()
        print("熔断器已重置为 CLOSED 状态")

    elif args.cmd == "get":
        p = cache.get(args.arxiv_id)
        if p:
            print(json.dumps(p, ensure_ascii=False, indent=2))
        else:
            print(f"[miss] {args.arxiv_id} 不在缓存中或已过期")

    else:
        parser.print_help()
