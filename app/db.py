"""Helpers SQLite: lưu chunks KB và tickets."""
from __future__ import annotations

import json
import sqlite3
from contextlib import contextmanager
from pathlib import Path

_SCHEMA = """
CREATE TABLE IF NOT EXISTS chunks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doc_path TEXT NOT NULL,
    doc_title TEXT NOT NULL,
    category TEXT NOT NULL DEFAULT '',
    content TEXT NOT NULL,
    embedding TEXT
);
CREATE INDEX IF NOT EXISTS idx_chunks_doc_path ON chunks(doc_path);

CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT NOT NULL,
    description TEXT NOT NULL,
    transcript TEXT NOT NULL DEFAULT '[]',
    status TEXT NOT NULL DEFAULT 'open',
    level TEXT NOT NULL DEFAULT 'L2',
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    resolution TEXT NOT NULL DEFAULT '',
    assignee TEXT NOT NULL DEFAULT ''
);
CREATE TABLE IF NOT EXISTS audit (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticket_id INTEGER,
    action TEXT NOT NULL,
    detail TEXT NOT NULL DEFAULT '',
    created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS flows (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    data TEXT NOT NULL DEFAULT '{}',
    created_at TEXT NOT NULL
);
"""


def _connect(db_path: str) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    return conn


@contextmanager
def db_session(db_path: str):
    conn = _connect(db_path)
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def init_db(db_path: str) -> None:
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)
    with db_session(db_path) as conn:
        conn.executescript(_SCHEMA)
        cols = [r["name"] for r in conn.execute("PRAGMA table_info(tickets)")]
        if "assignee" not in cols:
            conn.execute("ALTER TABLE tickets ADD COLUMN assignee TEXT NOT NULL DEFAULT ''")


def upsert_chunks(db_path: str, chunks: list[dict]) -> None:
    """chunks: list of dict(doc_path, doc_title, category, content, embedding|None)."""
    with db_session(db_path) as conn:
        conn.execute("DELETE FROM chunks")
        conn.executemany(
            "INSERT INTO chunks (doc_path, doc_title, category, content, embedding) "
            "VALUES (:doc_path, :doc_title, :category, :content, :embedding)",
            [
                {
                    "doc_path": c["doc_path"],
                    "doc_title": c["doc_title"],
                    "category": c.get("category", ""),
                    "content": c["content"],
                    "embedding": json.dumps(c["embedding"]) if c.get("embedding") else None,
                }
                for c in chunks
            ],
        )


def load_chunks(db_path: str) -> list[dict]:
    with db_session(db_path) as conn:
        rows = conn.execute(
            "SELECT doc_path, doc_title, category, content, embedding FROM chunks"
        ).fetchall()
    out = []
    for r in rows:
        emb = json.loads(r["embedding"]) if r["embedding"] else None
        out.append(
            {
                "doc_path": r["doc_path"],
                "doc_title": r["doc_title"],
                "category": r["category"],
                "content": r["content"],
                "embedding": emb,
            }
        )
    return out


def insert_ticket(db_path: str, ticket: dict) -> int:
    with db_session(db_path) as conn:
        cur = conn.execute(
            "INSERT INTO tickets (subject, description, transcript, status, level, created_at, updated_at, resolution, assignee) "
            "VALUES (:subject, :description, :transcript, :status, :level, :created_at, :updated_at, :resolution, :assignee)",
            ticket,
        )
        lid = cur.lastrowid
        assert lid is not None
        return int(lid)


def _row_to_ticket(row: sqlite3.Row) -> dict:
    d = dict(row)
    try:
        d["transcript"] = json.loads(d["transcript"])
    except (TypeError, json.JSONDecodeError):
        d["transcript"] = []
    return d


def list_tickets(db_path: str) -> list[dict]:
    with db_session(db_path) as conn:
        rows = conn.execute("SELECT * FROM tickets ORDER BY id DESC").fetchall()
    return [_row_to_ticket(r) for r in rows]


def get_ticket(db_path: str, ticket_id: int) -> dict | None:
    with db_session(db_path) as conn:
        row = conn.execute("SELECT * FROM tickets WHERE id = ?", (ticket_id,)).fetchone()
    return _row_to_ticket(row) if row else None


def update_ticket(db_path: str, ticket_id: int, *, status: str | None = None, resolution: str | None = None) -> bool:
    fields, params = [], []
    if status is not None:
        fields.append("status = ?")
        params.append(status)
    if resolution is not None:
        fields.append("resolution = ?")
        params.append(resolution)
    if not fields:
        return False
    fields.append("updated_at = ?")
    params.append(_now())
    params.append(ticket_id)
    with db_session(db_path) as conn:
        cur = conn.execute(f"UPDATE tickets SET {', '.join(fields)} WHERE id = ?", params)
        return cur.rowcount > 0


def insert_audit(db_path: str, ticket_id: int | None, action: str, detail: str = "") -> None:
    with db_session(db_path) as conn:
        conn.execute(
            "INSERT INTO audit (ticket_id, action, detail, created_at) VALUES (?, ?, ?, ?)",
            (ticket_id, action, detail, _now()),
        )


def list_audit(db_path: str, limit: int = 100) -> list[dict]:
    with db_session(db_path) as conn:
        rows = conn.execute(
            "SELECT * FROM audit ORDER BY id DESC LIMIT ?", (limit,)
        ).fetchall()
    return [dict(r) for r in rows]


def insert_flow(db_path: str, name: str, data: str) -> int:
    with db_session(db_path) as conn:
        cur = conn.execute(
            "INSERT INTO flows (name, data, created_at) VALUES (?, ?, ?)",
            (name, data, _now()),
        )
        lid = cur.lastrowid
        assert lid is not None
        return int(lid)


def list_flows(db_path: str) -> list[dict]:
    with db_session(db_path) as conn:
        rows = conn.execute("SELECT * FROM flows ORDER BY id DESC").fetchall()
    out = []
    for r in rows:
        d = dict(r)
        try:
            d["data"] = json.loads(d["data"])
        except (TypeError, json.JSONDecodeError):
            d["data"] = {}
        out.append(d)
    return out


def delete_flow(db_path: str, flow_id: int) -> bool:
    with db_session(db_path) as conn:
        cur = conn.execute("DELETE FROM flows WHERE id = ?", (flow_id,))
        return cur.rowcount > 0


def _now() -> str:
    from datetime import datetime, timezone

    return datetime.now(timezone.utc).isoformat(timespec="seconds")