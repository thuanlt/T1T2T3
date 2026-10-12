"""Nạp KB: chunk → embedding → lưu SQLite."""
from __future__ import annotations

import logging

from .config import Settings
from . import db
from .llm import LLMClient, LLMError
from .retrieval import Chunk, load_kb

logger = logging.getLogger(__name__)


def ingest(settings: Settings, llm: LLMClient | None = None) -> dict:
    """Đọc kb/, chunk, embed (nếu có LLM), ghi vào DB. Trả về thống kê."""
    chunks = load_kb(settings.kb_dir, max_chars=settings.chunk_size, overlap=settings.chunk_overlap)
    embedded = 0
    if llm is not None and llm.available and chunks:
        try:
            batch = 64
            for i in range(0, len(chunks), batch):
                texts = [c.content for c in chunks[i : i + batch]]
                vecs = llm.embed(texts)
                for c, v in zip(chunks[i : i + batch], vecs):
                    c.embedding = v
                embedded += len(vecs)
        except LLMError as exc:
            logger.error("Embedding thất bại (%s), lưu chunk không embedding.", exc)
    records = [
        {
            "doc_path": c.doc_path,
            "doc_title": c.doc_title,
            "category": c.category,
            "content": c.content,
            "embedding": c.embedding,
        }
        for c in chunks
    ]
    db.init_db(settings.db_path)
    db.upsert_chunks(settings.db_path, records)
    return {"chunks": len(records), "embedded": embedded}


def build_retriever(settings: Settings) -> tuple[list[Chunk], bool]:
    """Tải chunks từ DB; nếu rỗng thì ingest ngay. Trả về (chunks, đã_ingest)."""
    db.init_db(settings.db_path)
    records = db.load_chunks(settings.db_path)
    if not records:
        return [], False
    chunks = [
        Chunk(
            doc_path=r["doc_path"],
            doc_title=r["doc_title"],
            category=r["category"],
            content=r["content"],
            embedding=r["embedding"],
        )
        for r in records
    ]
    return chunks, True