"""Cấu hình ứng dụng từ biến môi trường."""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from functools import lru_cache


@dataclass(frozen=True)
class Settings:
    llm_api_key: str = ""
    llm_base_url: str = "https://api.openai.com/v1"
    llm_chat_model: str = "gpt-4o-mini"
    llm_embed_model: str = "text-embedding-3-small"
    llm_router_model: str = ""
    llm_image_model: str = ""
    llm_vision_model: str = ""
    db_path: str = "data/agent.db"
    kb_dir: str = "kb"
    chunk_size: int = 700
    chunk_overlap: int = 100
    top_k: int = 5
    low_conf_threshold: float = 0.35
    keyword_conf_threshold: float = 0.15
    llm_timeout: float = 60.0
    llm_verify_ssl: bool = True
    extra_env: dict = field(default_factory=dict)

    @property
    def llm_available(self) -> bool:
        return bool(self.llm_api_key)

    @classmethod
    def from_env(cls) -> "Settings":
        return cls(
            llm_api_key=os.getenv("LLM_API_KEY", "").strip(),
            llm_base_url=os.getenv("LLM_BASE_URL", "https://api.openai.com/v1").strip().rstrip("/"),
            llm_chat_model=os.getenv("LLM_CHAT_MODEL", "gpt-4o-mini").strip(),
            llm_embed_model=os.getenv("LLM_EMBED_MODEL", "text-embedding-3-small").strip(),
            llm_router_model=os.getenv("LLM_ROUTER_MODEL", "").strip(),
            llm_image_model=os.getenv("LLM_IMAGE_MODEL", "").strip(),
            llm_vision_model=os.getenv("LLM_VISION_MODEL", "").strip(),
            db_path=os.getenv("DB_PATH", "data/agent.db").strip(),
            kb_dir=os.getenv("KB_DIR", "kb").strip(),
            chunk_size=int(os.getenv("CHUNK_SIZE", "700")),
            chunk_overlap=int(os.getenv("CHUNK_OVERLAP", "100")),
            top_k=int(os.getenv("TOP_K", "5")),
            low_conf_threshold=float(os.getenv("LOW_CONF_THRESHOLD", "0.35")),
            keyword_conf_threshold=float(os.getenv("KEYWORD_CONF_THRESHOLD", "0.15")),
            llm_timeout=float(os.getenv("LLM_TIMEOUT", "60")),
            llm_verify_ssl=os.getenv("LLM_VERIFY_SSL", "true").strip().lower() not in {"0", "false", "no", "off"},
        )


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings.from_env()