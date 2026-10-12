"""Router (judge decision): quyết định route cho mỗi câu hỏi TRƯỚC khi gọi vLLM/LLM/RAG.

Intent:
  chat_rag       -> tra cứu KB + sinh câu trả lời bằng chat model (RAG)
  general        -> trò chuyện chung, không cần KB (chat model trực tiếp)
  image_generate -> tạo ảnh (image model)
  image_analyze  -> phân tích ảnh (vision model, cần image_url)
  out_of_scope   -> ngoài phạm vi, đề xuất escalate L3
"""
from __future__ import annotations

import json
import logging
import re
from dataclasses import dataclass

from .config import Settings
from .llm import LLMClient, LLMError

logger = logging.getLogger(__name__)

ROUTER_SYSTEM_PROMPT = """Bạn là bộ định tuyến (router) của hệ thống hỗ trợ FPT AI Factory.
Phân loại câu hỏi của khách hàng thành ĐÚNG MỘT intent, trả về JSON duy nhất:
{"intent": "...", "reason": "..."}

Các intent hợp lệ:
- "chat_rag": câu hỏi về dịch vụ, sản phẩm, sự cố, hướng dẫn sử dụng FPT AI Factory / FPT Cloud (cần tra cứu tài liệu).
- "image_generate": khách hàng YÊU CẦU TẠO / SINH / VẼ một hình ảnh, logo, ảnh minh họa.
- "image_analyze": khách hàng muốn PHÂN TÍCH / NHẬN DIỆN / MÔ TẢ một hình ảnh (có kèm ảnh).
- "general": chào hỏi, cảm ơn, câu hỏi chung không thuộc các loại trên.
- "out_of_scope": câu hỏi ngoài phạm vi hỗ trợ (chính trị, pháp luật, dịch vụ không liên quan, nội dung nhạy cảm).

Chỉ trả về JSON, không thêm chữ nào khác."""

INTENTS = ("chat_rag", "general", "image_generate", "image_analyze", "out_of_scope")

_IMAGE_GEN_KEYWORDS = [
    "tạo ảnh", "sinh ảnh", "vẽ", "vẽ hình", "vẽ logo", "vẽ tranh", "vẽ ảnh", "vẽ banner",
    "generate image", "generate a", "create image", "create a picture", "draw",
    "ảnh minh họa", "logo", "hình ảnh về", "tạo hình", "ảnh đại diện",
    "illustration", "picture of", "image of", "banner", "poster", "tạo banner", "tạo poster",
]
_IMAGE_ANALYZE_KEYWORDS = [
    "phân tích ảnh", "nhận diện ảnh", "mô tả ảnh", "xem ảnh", "kiểm tra ảnh", "ảnh này",
    "analyze image", "describe image", "this image", "nhìn ảnh", "đọc ảnh", "ảnh đính kèm",
]
_OUT_OF_SCOPE_KEYWORDS = [
    "thời tiết", "tin tức", "bóng đá", "nấu ăn", "du lịch", "game", "phim", "âm nhạc",
    "weather", "news", "recipe", "travel", "movie", "music", "football",
]


def _normalize(text: str) -> str:
    import unicodedata

    text = unicodedata.normalize("NFD", text.lower())
    return "".join(ch for ch in text if unicodedata.category(ch) != "Mn")


def _match(keyword: str, raw: str, q: str) -> bool:
    """Keyword có dấu -> so khớp trên text gốc (giữ dấu, tránh "vẽ" vs "về").
    Keyword ASCII (logo, image, draw...) -> so khớp trên text đã bỏ dấu."""
    if any(ord(ch) > 127 for ch in keyword):
        return keyword in raw
    return keyword in q


@dataclass
class RouteDecision:
    intent: str
    model: str
    reason: str
    router_mode: str  # "systemone" | "llm" | "heuristic"
    confidence: float = 0.0
    urgent: bool = False
    mood: str = ""

    def to_dict(self) -> dict:
        return {
            "intent": self.intent,
            "model": self.model,
            "reason": self.reason,
            "router_mode": self.router_mode,
            "confidence": self.confidence,
            "urgent": self.urgent,
            "mood": self.mood,
        }


_INTENT_CRITERIA = {
    "chat_rag": "hỏi về dịch vụ, sự cố, hướng dẫn sử dụng FPT AI Factory / FPT Cloud",
    "image_generate": "muốn tạo / sinh / vẽ một hình ảnh, logo, banner",
    "image_analyze": "muốn phân tích / nhận diện / mô tả một hình ảnh",
    "general": "chào hỏi, cảm ơn, câu hỏi chung",
    "out_of_scope": "ngoài phạm vi hỗ trợ (thời tiết, tin tức, chính trị, ...)",
}

_SYSTEMONE_QUESTIONS = {
    "intent": {
        "type": "choice",
        "instructions": "Loại yêu cầu của khách hàng?",
        "criteria": _INTENT_CRITERIA,
    },
    "urgent": {"type": "noul", "instructions": "Yêu cầu có khẩn cấp không (dịch vụ ngừng, ảnh hưởng sản xuất)?"},
    "mood": {
        "type": "score",
        "instructions": "Mức độ bực bội của khách hàng?",
        "criteria": ["calm", "annoyed", "angry"],
    },
}


def _model_for_intent(intent: str, settings: Settings) -> str:
    return {
        "chat_rag": settings.llm_chat_model,
        "general": settings.llm_chat_model,
        "image_generate": settings.llm_image_model,
        "image_analyze": settings.llm_vision_model,
        "out_of_scope": "",
    }[intent]


def _parse_systemone(answers: dict, settings: Settings, router_model: str) -> RouteDecision:
    intent = "chat_rag"
    confidence = 0.0
    reason = f"Router model {router_model} (systemone)"
    intent_a = answers.get("intent") or {}
    if isinstance(intent_a, dict):
        intent = intent_a.get("choice") or intent
        if intent not in INTENTS:
            intent = "chat_rag"
        confidence = float(intent_a.get("confidence") or 0.0)
    urgent = False
    urg_a = answers.get("urgent") or {}
    if isinstance(urg_a, dict) and isinstance(urg_a.get("noul"), (int, float)):
        urgent = float(urg_a["noul"]) >= 0.5
    mood = ""
    mood_a = answers.get("mood") or {}
    if isinstance(mood_a, dict):
        legend = mood_a.get("legend") or {}
        score = mood_a.get("score")
        if isinstance(score, (int, float)) and legend:
            idx = min(len(legend) - 1, max(0, round(float(score) * (len(legend) - 1))))
            mood = str(legend.get(str(idx), ""))
    return RouteDecision(
        intent=intent,
        model=_model_for_intent(intent, settings),
        reason=reason,
        router_mode="systemone",
        confidence=round(confidence, 4),
        urgent=urgent,
        mood=mood,
    )


def _heuristic_route(question: str, settings: Settings) -> RouteDecision:
    raw = question.lower()
    q = _normalize(question)
    if any(_match(k, raw, q) for k in _OUT_OF_SCOPE_KEYWORDS):
        return RouteDecision("out_of_scope", "", "Câu hỏi ngoài phạm vi hỗ trợ (heuristic)", "heuristic")
    if any(_match(k, raw, q) for k in _IMAGE_GEN_KEYWORDS):
        return RouteDecision(
            "image_generate",
            settings.llm_image_model,
            "Yêu cầu tạo hình ảnh (heuristic)",
            "heuristic",
        )
    if any(_match(k, raw, q) for k in _IMAGE_ANALYZE_KEYWORDS):
        return RouteDecision(
            "image_analyze",
            settings.llm_vision_model,
            "Yêu cầu phân tích ảnh (heuristic)",
            "heuristic",
        )
    return RouteDecision("chat_rag", settings.llm_chat_model, "Mặc định tra KB (heuristic)", "heuristic")


def _parse_intent(text: str) -> tuple[str, str]:
    try:
        m = re.search(r"\{.*\}", text, re.S)
        if m is None:
            raise ValueError("no json")
        data = json.loads(m.group(0))
    except (ValueError, json.JSONDecodeError):
        for it in INTENTS:
            if it in text:
                return it, "Trích từ phản hồi router"
        return "chat_rag", "Không parse được JSON, mặc định chat_rag"
    intent = data.get("intent", "chat_rag")
    if intent not in INTENTS:
        intent = "chat_rag"
    return intent, str(data.get("reason", ""))[:300]


def route(question: str, llm: LLMClient, settings: Settings) -> RouteDecision:
    """Judge decision: Quyet (systemone) → chat completions JSON → heuristic fallback."""
    router_model = settings.llm_router_model or settings.llm_chat_model
    if llm.available:
        if "quyet" in router_model.lower():
            try:
                answers = llm.systemone(router_model, question, _SYSTEMONE_QUESTIONS)
                return _parse_systemone(answers, settings, router_model)
            except LLMError as exc:
                logger.warning("SystemOne (Quyet) lỗi, fallback chat router: %s", exc)
        try:
            text = llm.chat(
                [
                    {"role": "system", "content": ROUTER_SYSTEM_PROMPT},
                    {"role": "user", "content": question},
                ],
                temperature=0.0,
                max_tokens=120,
            )
            intent, reason = _parse_intent(text)
            return RouteDecision(
                intent=intent,
                model=_model_for_intent(intent, settings),
                reason=reason or f"Router model {router_model}",
                router_mode="llm",
            )
        except LLMError as exc:
            logger.warning("Router LLM lỗi, fallback heuristic: %s", exc)
    return _heuristic_route(question, settings)