"""SQLite-backed :class:`~zam_agent.store.base.Store`.

SQLite in WAL mode is the right default here: the workload is a few writes per
message in one channel, and a single file is far easier to operate than a
database server. To move to Postgres, implement ``Store`` against it -- nothing
else in the codebase touches SQL.

Set ``DATABASE_URL=sqlite:///./data/zam_agent.db`` (or ``sqlite://:memory:``).
On a container with an ephemeral filesystem, mount a volume at the DB path or
the de-duplication guarantee is lost across restarts.
"""

from __future__ import annotations

import hashlib
import sqlite3
import threading
import time
from collections.abc import Sequence
from pathlib import Path
from typing import Any

from ..language import normalize_for_search
from ..observability.logging import get_logger
from .base import EscalationRecord, KnowledgeGap, Store

log = get_logger(__name__)

SCHEMA = """
CREATE TABLE IF NOT EXISTS processed_events (
    event_key   TEXT PRIMARY KEY,
    channel_id  TEXT NOT NULL DEFAULT '',
    message_ts  TEXT NOT NULL DEFAULT '',
    created_at  REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS escalations (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    question_key   TEXT NOT NULL,
    channel_id     TEXT NOT NULL,
    thread_ts      TEXT,
    product        TEXT,
    owner_user_id  TEXT NOT NULL,
    topic          TEXT NOT NULL DEFAULT '',
    question       TEXT NOT NULL DEFAULT '',
    status         TEXT NOT NULL DEFAULT 'open',
    created_at     REAL NOT NULL,
    resolved_at    REAL,
    resolved_by    TEXT,
    resolution_note TEXT
);
CREATE INDEX IF NOT EXISTS idx_escalations_lookup
    ON escalations (question_key, channel_id, created_at DESC);
CREATE INDEX IF NOT EXISTS idx_escalations_thread ON escalations (thread_ts);

CREATE TABLE IF NOT EXISTS interactions (
    id                INTEGER PRIMARY KEY AUTOINCREMENT,
    event_key         TEXT NOT NULL DEFAULT '',
    channel_id        TEXT NOT NULL DEFAULT '',
    thread_ts         TEXT,
    message_ts        TEXT NOT NULL DEFAULT '',
    user_id           TEXT NOT NULL DEFAULT '',
    category          TEXT NOT NULL DEFAULT '',
    action            TEXT NOT NULL DEFAULT '',
    confidence_level  TEXT NOT NULL DEFAULT '',
    confidence_score  REAL NOT NULL DEFAULT 0,
    language          TEXT NOT NULL DEFAULT '',
    topic             TEXT NOT NULL DEFAULT '',
    product           TEXT,
    reasons           TEXT NOT NULL DEFAULT '',
    source_ids        TEXT NOT NULL DEFAULT '',
    latency_ms        INTEGER NOT NULL DEFAULT 0,
    created_at        REAL NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_interactions_created ON interactions (created_at DESC);
CREATE INDEX IF NOT EXISTS idx_interactions_thread ON interactions (channel_id, thread_ts);

CREATE TABLE IF NOT EXISTS knowledge_gaps (
    question_key     TEXT PRIMARY KEY,
    question         TEXT NOT NULL,
    topic            TEXT NOT NULL DEFAULT '',
    product          TEXT,
    occurrences      INTEGER NOT NULL DEFAULT 1,
    first_seen       REAL NOT NULL,
    last_seen        REAL NOT NULL,
    last_channel_id  TEXT NOT NULL DEFAULT '',
    last_thread_ts   TEXT,
    resolved         INTEGER NOT NULL DEFAULT 0,
    resolved_at      REAL,
    resolved_by      TEXT,
    resolution_note  TEXT
);
"""


def question_key(question: str, product: str | None = None) -> str:
    """Stable key for 'the same question asked again', language-normalized."""

    basis = f"{product or 'any'}|{normalize_for_search(question)}"
    return hashlib.sha256(basis.encode("utf-8")).hexdigest()[:32]


def path_from_database_url(url: str) -> str:
    if url.startswith("sqlite:///"):
        return url[len("sqlite:///") :]
    if url.startswith("sqlite://"):
        return url[len("sqlite://") :]
    if url.startswith("sqlite:"):
        return url[len("sqlite:") :]
    raise ValueError(
        f"Unsupported DATABASE_URL {url.split('://')[0]!r}: the bundled store is SQLite only. "
        "Implement zam_agent.store.base.Store for another engine."
    )


class SQLiteStore(Store):
    def __init__(self, database_url: str = "sqlite:///./data/zam_agent.db") -> None:
        raw_path = path_from_database_url(database_url)
        self.in_memory = raw_path in (":memory:", "", "/:memory:")
        self.path = ":memory:" if self.in_memory else str(Path(raw_path).expanduser())
        self._lock = threading.RLock()
        self._shared: sqlite3.Connection | None = None
        if not self.in_memory:
            Path(self.path).parent.mkdir(parents=True, exist_ok=True)
        self.setup()

    # ------------------------------------------------------------ connections

    def _connect(self) -> sqlite3.Connection:
        if self.in_memory:
            if self._shared is None:
                self._shared = sqlite3.connect(":memory:", check_same_thread=False)
                self._shared.row_factory = sqlite3.Row
            return self._shared
        conn = sqlite3.connect(self.path, timeout=10.0, check_same_thread=False)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA synchronous=NORMAL")
        conn.execute("PRAGMA busy_timeout=10000")
        return conn

    def _execute(self, sql: str, params: Sequence[Any] = (), *, script: bool = False) -> sqlite3.Cursor:
        with self._lock:
            conn = self._connect()
            try:
                cursor = conn.executescript(sql) if script else conn.execute(sql, tuple(params))
                conn.commit()
                return cursor
            finally:
                if not self.in_memory:
                    conn.close()

    def _query(self, sql: str, params: Sequence[Any] = ()) -> list[sqlite3.Row]:
        with self._lock:
            conn = self._connect()
            try:
                return list(conn.execute(sql, tuple(params)).fetchall())
            finally:
                if not self.in_memory:
                    conn.close()

    # (table, column, declaration) -- applied to databases created before the
    # column existed. SQLite has no "ADD COLUMN IF NOT EXISTS".
    MIGRATIONS: tuple[tuple[str, str, str], ...] = (
        ("escalations", "resolved_by", "TEXT"),
        ("escalations", "resolution_note", "TEXT"),
        ("knowledge_gaps", "resolved_at", "REAL"),
        ("knowledge_gaps", "resolved_by", "TEXT"),
        ("knowledge_gaps", "resolution_note", "TEXT"),
    )

    def setup(self) -> None:
        self._execute(SCHEMA, script=True)
        self._migrate()

    def _migrate(self) -> None:
        for table, column, declaration in self.MIGRATIONS:
            existing = {row["name"] for row in self._query(f"PRAGMA table_info({table})")}
            if column not in existing:
                self._execute(f"ALTER TABLE {table} ADD COLUMN {column} {declaration}")  # noqa: S608
                log.info(
                    "added missing column",
                    extra={"context": {"table": table, "column": column}},
                )

    def close(self) -> None:
        with self._lock:
            if self._shared is not None:
                self._shared.close()
                self._shared = None

    # ----------------------------------------------------------- de-duplication

    def claim_event(self, event_key: str, *, channel_id: str = "", message_ts: str = "") -> bool:
        if not event_key:
            return True
        cursor = self._execute(
            "INSERT OR IGNORE INTO processed_events (event_key, channel_id, message_ts, created_at) "
            "VALUES (?, ?, ?, ?)",
            (event_key, channel_id, message_ts, time.time()),
        )
        return cursor.rowcount == 1

    def release_event(self, event_key: str) -> None:
        if event_key:
            self._execute("DELETE FROM processed_events WHERE event_key = ?", (event_key,))

    def was_processed(self, event_key: str) -> bool:
        return bool(self._query("SELECT 1 FROM processed_events WHERE event_key = ?", (event_key,)))

    # ------------------------------------------------------------- escalations

    def recent_escalation(
        self, key: str, *, channel_id: str, within_hours: int
    ) -> EscalationRecord | None:
        cutoff = time.time() - max(0, within_hours) * 3600
        rows = self._query(
            "SELECT * FROM escalations WHERE question_key = ? AND channel_id = ? "
            "AND created_at >= ? AND status = 'open' ORDER BY created_at DESC LIMIT 1",
            (key, channel_id, cutoff),
        )
        return _to_escalation(rows[0]) if rows else None

    def open_escalation_for_thread(self, channel_id: str, thread_ts: str | None) -> EscalationRecord | None:
        if not thread_ts:
            return None
        rows = self._query(
            "SELECT * FROM escalations WHERE channel_id = ? AND thread_ts = ? AND status = 'open' "
            "ORDER BY created_at DESC LIMIT 1",
            (channel_id, thread_ts),
        )
        return _to_escalation(rows[0]) if rows else None

    def record_escalation(
        self,
        *,
        question_key: str,
        channel_id: str,
        thread_ts: str | None,
        product: str | None,
        owner_user_id: str,
        topic: str,
        question: str,
    ) -> EscalationRecord:
        now = time.time()
        cursor = self._execute(
            "INSERT INTO escalations "
            "(question_key, channel_id, thread_ts, product, owner_user_id, topic, question, status, created_at) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, 'open', ?)",
            (question_key, channel_id, thread_ts, product, owner_user_id, topic, question, now),
        )
        return EscalationRecord(
            id=int(cursor.lastrowid or 0),
            question_key=question_key,
            channel_id=channel_id,
            thread_ts=thread_ts,
            product=product,
            owner_user_id=owner_user_id,
            topic=topic,
            question=question,
            status="open",
            created_at=now,
            resolved_at=None,
        )

    def resolve_escalation(self, escalation_id: int, *, note: str = "", resolved_by: str = "") -> None:
        self._execute(
            "UPDATE escalations SET status = 'resolved', resolved_at = ?, resolved_by = ?, "
            "resolution_note = ? WHERE id = ?",
            (time.time(), resolved_by, note, escalation_id),
        )

    def reopen_escalation(self, escalation_id: int) -> None:
        """Undo a resolution (a mis-clicked reaction), without re-pinging."""

        self._execute(
            "UPDATE escalations SET status = 'open', resolved_at = NULL, resolved_by = NULL, "
            "resolution_note = NULL WHERE id = ?",
            (escalation_id,),
        )

    def escalation(self, escalation_id: int) -> EscalationRecord | None:
        rows = self._query("SELECT * FROM escalations WHERE id = ?", (escalation_id,))
        return _to_escalation(rows[0]) if rows else None

    def escalation_for_thread(self, channel_id: str, thread_ts: str | None) -> EscalationRecord | None:
        """The most recent escalation in a thread, open or already resolved."""

        if not thread_ts:
            return None
        rows = self._query(
            "SELECT * FROM escalations WHERE channel_id = ? AND thread_ts = ? "
            "ORDER BY created_at DESC LIMIT 1",
            (channel_id, thread_ts),
        )
        return _to_escalation(rows[0]) if rows else None

    def open_escalations(self, *, limit: int = 50) -> list[EscalationRecord]:
        rows = self._query(
            "SELECT * FROM escalations WHERE status = 'open' ORDER BY created_at DESC LIMIT ?",
            (limit,),
        )
        return [_to_escalation(row) for row in rows]

    # ------------------------------------------------------------ interactions

    def record_interaction(self, **fields: Any) -> None:
        columns = (
            "event_key", "channel_id", "thread_ts", "message_ts", "user_id", "category",
            "action", "confidence_level", "confidence_score", "language", "topic",
            "product", "reasons", "source_ids", "latency_ms",
        )
        values = [fields.get(name) if fields.get(name) is not None else _default_for(name) for name in columns]
        self._execute(
            f"INSERT INTO interactions ({', '.join(columns)}, created_at) "
            f"VALUES ({', '.join('?' for _ in columns)}, ?)",
            (*values, time.time()),
        )

    def recent_interactions(self, *, limit: int = 20) -> list[dict[str, Any]]:
        rows = self._query("SELECT * FROM interactions ORDER BY created_at DESC LIMIT ?", (limit,))
        return [dict(row) for row in rows]

    # --------------------------------------------------------- knowledge gaps

    def upsert_knowledge_gap(
        self,
        *,
        question_key: str,
        question: str,
        topic: str,
        product: str | None,
        channel_id: str,
        thread_ts: str | None,
    ) -> None:
        now = time.time()
        self._execute(
            "INSERT INTO knowledge_gaps "
            "(question_key, question, topic, product, occurrences, first_seen, last_seen, "
            " last_channel_id, last_thread_ts, resolved) "
            "VALUES (?, ?, ?, ?, 1, ?, ?, ?, ?, 0) "
            "ON CONFLICT(question_key) DO UPDATE SET "
            "  occurrences = occurrences + 1, last_seen = excluded.last_seen, "
            "  last_channel_id = excluded.last_channel_id, last_thread_ts = excluded.last_thread_ts, "
            "  resolved = 0",
            (question_key, question, topic, product, now, now, channel_id, thread_ts),
        )

    def knowledge_gaps(self, *, limit: int = 50, include_resolved: bool = False) -> list[KnowledgeGap]:
        clause = "" if include_resolved else "WHERE resolved = 0"
        rows = self._query(
            f"SELECT * FROM knowledge_gaps {clause} ORDER BY occurrences DESC, last_seen DESC LIMIT ?",
            (limit,),
        )
        return [_to_gap(row) for row in rows]

    def resolved_knowledge_gaps(self, *, limit: int = 50) -> list[KnowledgeGap]:
        rows = self._query(
            "SELECT * FROM knowledge_gaps WHERE resolved = 1 ORDER BY resolved_at DESC LIMIT ?",
            (limit,),
        )
        return [_to_gap(row) for row in rows]

    def knowledge_gap(self, question_key: str) -> KnowledgeGap | None:
        rows = self._query("SELECT * FROM knowledge_gaps WHERE question_key = ?", (question_key,))
        return _to_gap(rows[0]) if rows else None

    def resolve_knowledge_gap(self, question_key: str, *, note: str = "", resolved_by: str = "") -> None:
        self._execute(
            "UPDATE knowledge_gaps SET resolved = 1, resolved_at = ?, resolved_by = ?, "
            "resolution_note = ? WHERE question_key = ?",
            (time.time(), resolved_by, note, question_key),
        )

    def reopen_knowledge_gap(self, question_key: str) -> None:
        self._execute(
            "UPDATE knowledge_gaps SET resolved = 0, resolved_at = NULL, resolved_by = NULL, "
            "resolution_note = NULL WHERE question_key = ?",
            (question_key,),
        )

    # -------------------------------------------------------------- operations

    def stats(self) -> dict[str, Any]:
        def scalar(sql: str) -> int:
            rows = self._query(sql)
            return int(rows[0][0]) if rows else 0

        return {
            "processed_events": scalar("SELECT COUNT(*) FROM processed_events"),
            "interactions": scalar("SELECT COUNT(*) FROM interactions"),
            "open_escalations": scalar("SELECT COUNT(*) FROM escalations WHERE status = 'open'"),
            "knowledge_gaps": scalar("SELECT COUNT(*) FROM knowledge_gaps WHERE resolved = 0"),
            "database": "memory" if self.in_memory else self.path,
        }

    def prune(self, *, older_than_days: int = 30) -> int:
        cutoff = time.time() - max(1, older_than_days) * 86400
        removed = self._execute("DELETE FROM processed_events WHERE created_at < ?", (cutoff,)).rowcount
        self._execute("DELETE FROM interactions WHERE created_at < ?", (cutoff,))
        self._execute(
            "UPDATE escalations SET status = 'expired' WHERE status = 'open' AND created_at < ?",
            (cutoff,),
        )
        return int(removed or 0)


def _default_for(name: str) -> Any:
    if name in ("confidence_score",):
        return 0.0
    if name in ("latency_ms",):
        return 0
    if name in ("thread_ts", "product"):
        return None
    return ""


def _to_gap(row: sqlite3.Row) -> KnowledgeGap:
    keys = row.keys()
    return KnowledgeGap(
        question_key=row["question_key"],
        question=row["question"],
        topic=row["topic"],
        product=row["product"],
        occurrences=int(row["occurrences"]),
        first_seen=float(row["first_seen"]),
        last_seen=float(row["last_seen"]),
        last_channel_id=row["last_channel_id"],
        last_thread_ts=row["last_thread_ts"],
        resolved=bool(row["resolved"]),
        resolved_at=float(row["resolved_at"]) if "resolved_at" in keys and row["resolved_at"] else None,
        resolved_by=row["resolved_by"] if "resolved_by" in keys else None,
        resolution_note=row["resolution_note"] if "resolution_note" in keys else None,
    )


def _to_escalation(row: sqlite3.Row) -> EscalationRecord:
    # `in row` would test the VALUES, not the column names, so keep .keys().
    keys = row.keys()
    return EscalationRecord(
        id=int(row["id"]),
        question_key=row["question_key"],
        channel_id=row["channel_id"],
        thread_ts=row["thread_ts"],
        product=row["product"],
        owner_user_id=row["owner_user_id"],
        topic=row["topic"],
        question=row["question"],
        status=row["status"],
        created_at=float(row["created_at"]),
        resolved_at=float(row["resolved_at"]) if row["resolved_at"] is not None else None,
        resolved_by=row["resolved_by"] if "resolved_by" in keys else None,
        resolution_note=row["resolution_note"] if "resolution_note" in keys else None,
    )
