#!/usr/bin/env python3
"""Nạp KB vào index: python scripts/ingest_kb.py"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.config import get_settings  # noqa: E402
from app.indexer import ingest  # noqa: E402
from app.llm import LLMClient  # noqa: E402


def main() -> None:
    settings = get_settings()
    llm = LLMClient(
        api_key=settings.llm_api_key,
        base_url=settings.llm_base_url,
        chat_model=settings.llm_chat_model,
        embed_model=settings.llm_embed_model,
        timeout=settings.llm_timeout,
        verify_ssl=settings.llm_verify_ssl,
    )
    try:
        stats = ingest(settings, llm)
    finally:
        llm.close()
    print(f"Ingested {stats['chunks']} chunks ({stats['embedded']} embedded) from {settings.kb_dir}")


if __name__ == "__main__":
    main()