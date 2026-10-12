"""Pipeline RAG: truy xuất KB → sinh câu trả lời (LLM hoặc tổng hợp keyword)."""
from __future__ import annotations

import logging
from dataclasses import dataclass, field

from .config import Settings
from .llm import LLMClient, LLMError
from .retrieval import Chunk, Hit, HybridRetriever
from .router import RouteDecision, route

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """Bạn là trợ lý hỗ trợ kỹ thuật của FPT AI Factory, phục vụ đội L1/L2 để trả lời khách hàng.

QUY TẮC:
1. Chỉ trả lời dựa trên tài liệu được cung cấp trong <context>. Không bịa thông tin.
2. Nếu tài liệu không đủ thông tin để trả lời, nói rõ "Thông tin hiện chưa có trong kho tài liệu" và đề xuất escalate lên L3.
3. Trả lời bằng tiếng Việt, ngắn gọn, rõ ràng, có cấu trúc (bullet khi cần).
4. Cuối câu trả lời, trích dẫn nguồn dưới dạng [Nguồn: <tên tài liệu>].
5. Nếu khách hàng đang gặp lỗi, hướng dẫn các bước kiểm tra cụ thể theo tài liệu.
"""

GENERAL_SYSTEM_PROMPT = """Bạn là trợ lý của FPT AI Factory phục vụ đội L1/L2.
Trả lời bằng tiếng Việt, ngắn gọn, thân thiện. Nếu câu hỏi cần tra cứu tài liệu kỹ thuật, hãy gợi ý hỏi chi tiết hơn."""


@dataclass
class Answer:
    text: str
    mode: str  # "llm" | "keyword"
    confidence: float
    sources: list[dict] = field(default_factory=list)
    escalate_suggested: bool = False
    route: dict | None = None


def _sources_from_hits(hits: list[Hit]) -> list[dict]:
    seen: set[tuple[str, str]] = set()
    out: list[dict] = []
    for h in hits:
        key = (h.doc_path, h.content)
        if key in seen:
            continue
        seen.add(key)
        out.append(
            {
                "title": h.doc_title,
                "path": h.doc_path,
                "category": h.category,
                "snippet": h.content[:400],
                "score": round(h.score, 3),
            }
        )
    return out


def _keyword_answer(question: str, hits: list[Hit], threshold: float) -> Answer:
    """Chế độ không LLM: tổng hợp từ các đoạn tài liệu khớp."""
    top = hits[0] if hits else None
    if not top or top.score < threshold:
        return Answer(
            text="Thông tin hiện chưa có trong kho tài liệu. Vui lòng kiểm tra lại câu hỏi "
                 "hoặc tạo ticket để đội L3 hỗ trợ.",
            mode="keyword",
            confidence=round(top.score, 3) if top else 0.0,
            sources=_sources_from_hits(hits),
            escalate_suggested=True,
        )
    parts = [f"Câu hỏi: {question}", "", "Các tài liệu liên quan:", ""]
    for i, h in enumerate(hits[:3], 1):
        parts.append(f"[{i}] {h.doc_title} ({h.category}):")
        parts.append(h.content.strip())
        parts.append("")
    text = "\n".join(parts)
    return Answer(
        text=text,
        mode="keyword",
        confidence=round(top.score, 3),
        sources=_sources_from_hits(hits),
        escalate_suggested=False,
    )


def _doc_context(retriever: HybridRetriever, hits: list[Hit], *, max_docs: int = 3, max_chars: int = 5000) -> list[str]:
    """Gom context theo doc: nếu 1 chunk của doc được match, đưa cả doc (các chunk anh em) vào.
    Chunk được match ưu tiên trước, phần còn lại của doc điền theo thứ tự, giới hạn max_chars."""
    doc_order: list[str] = []
    for h in hits:
        if h.doc_path not in doc_order:
            doc_order.append(h.doc_path)
    doc_chunks: dict[str, list[Chunk]] = {p: [] for p in doc_order}
    for c in retriever.chunks:
        if c.doc_path in doc_chunks:
            doc_chunks[c.doc_path].append(c)
    matched_idx: dict[str, set[int]] = {p: set() for p in doc_order}
    for h in hits:
        for i, c in enumerate(doc_chunks[h.doc_path]):
            if c.content == h.content:
                matched_idx[h.doc_path].add(i)
                break
    blocks: list[str] = []
    for path in doc_order[:max_docs]:
        cs = doc_chunks.get(path, [])
        if not cs:
            continue
        title = cs[0].doc_title or path
        ordered = sorted(
            enumerate(cs),
            key=lambda ic: (0 if ic[0] in matched_idx[path] else 1, ic[0]),
        )
        parts: list[str] = []
        total = 0
        for _, c in ordered:
            if total + len(c.content) > max_chars and parts:
                break
            parts.append(c.content)
            total += len(c.content)
        blocks.append(f"[Tài liệu: {title}]\n" + "\n\n".join(parts))
    return blocks


def generate_answer(
    question: str,
    retriever: HybridRetriever,
    llm: LLMClient,
    settings: Settings,
    model: str | None = None,
    agent_system: str | None = None,
) -> Answer:
    question = question.strip()
    if not question:
        return Answer(text="Vui lòng nhập câu hỏi.", mode="keyword", confidence=0.0)

    query_vec: list[float] | None = None
    if llm.available and retriever.has_vector:
        try:
            query_vec = llm.embed([question])[0]
        except LLMError as exc:
            logger.warning("Không embed được query, dùng keyword: %s", exc)

    hits = retriever.search(question, query_vec, settings.top_k)
    top_score = hits[0].score if hits else 0.0
    confidence = round(min(1.0, top_score), 3)
    sources = _sources_from_hits(hits)
    using_vector = query_vec is not None and retriever.has_vector
    threshold = settings.low_conf_threshold if using_vector else settings.keyword_conf_threshold
    low_conf = confidence < threshold or not hits

    if low_conf:
        return Answer(
            text="Thông tin hiện chưa có trong kho tài liệu hoặc câu hỏi chưa rõ ràng. "
                 "Vui lòng kiểm tra lại câu hỏi, hoặc tạo ticket để đội L3 hỗ trợ.",
            mode="llm" if llm.available else "keyword",
            confidence=confidence,
            sources=sources,
            escalate_suggested=True,
        )

    if not llm.available:
        return _keyword_answer(question, hits, settings.keyword_conf_threshold)

    context = "\n\n---\n\n".join(_doc_context(retriever, hits))
    user_msg = f"<context>\n{context}\n</context>\n\nCâu hỏi của khách hàng: {question}"
    try:
        text = llm.chat(
            [
                {"role": "system", "content": agent_system or SYSTEM_PROMPT},
                {"role": "user", "content": user_msg},
            ],
            max_tokens=1200,
            model=model,
        )
    except LLMError as exc:
        logger.error("LLM trả lời thất bại, fallback keyword: %s", exc)
        return _keyword_answer(question, hits, settings.keyword_conf_threshold)

    return Answer(
        text=text,
        mode="llm",
        confidence=confidence,
        sources=sources,
        escalate_suggested=False,
    )


def _dispatch(
    decision: RouteDecision,
    question: str,
    image_url: str | None,
    image_data: str | None,
    retriever,
    llm,
    settings,
    model: str | None = None,
    agent_system: str | None = None,
) -> Answer:
    intent = decision.intent
    has_image = bool(image_url or image_data)

    # Có ảnh đính kèm + câu hỏi không phải tạo ảnh -> ép về phân tích ảnh
    if has_image and intent in ("chat_rag", "general"):
        intent = "image_analyze"
        decision.intent = intent
        decision.model = settings.llm_vision_model
        decision.reason = "Có ảnh đính kèm -> phân tích ảnh"

    if intent == "general" and llm.available:
        try:
            text = llm.chat(
                [
                    {"role": "system", "content": agent_system or GENERAL_SYSTEM_PROMPT},
                    {"role": "user", "content": question},
                ],
                max_tokens=400,
                model=model,
            )
            return Answer(text=text, mode="llm", confidence=0.5, route=decision.to_dict())
        except LLMError as exc:
            logger.warning("General chat lỗi, fallback RAG: %s", exc)

    if intent == "image_generate":
        if llm.available and settings.llm_image_model:
            try:
                url = llm.generate_image(question, model=settings.llm_image_model)
                return Answer(
                    text=f"Đã tạo ảnh theo yêu cầu bằng model **{settings.llm_image_model}**:\n\n{url}",
                    mode="image",
                    confidence=0.8,
                    route=decision.to_dict(),
                )
            except LLMError as exc:
                logger.error("Image generation lỗi: %s", exc)
                return Answer(
                    text=f"Không tạo được ảnh: {exc}. Vui lòng kiểm tra cấu hình LLM_IMAGE_MODEL "
                         "hoặc tạo ticket để L3 hỗ trợ.",
                    mode="image",
                    confidence=0.0,
                    escalate_suggested=True,
                    route=decision.to_dict(),
                )
        return Answer(
            text="Agent chưa được cấu hình model tạo ảnh (LLM_IMAGE_MODEL). Vui lòng bổ sung cấu hình "
                 "hoặc tạo ticket để L3 hỗ trợ.",
            mode="image",
            confidence=0.0,
            escalate_suggested=True,
            route=decision.to_dict(),
        )

    if intent == "image_analyze":
        image_input = image_data or image_url
        if llm.available and settings.llm_vision_model and image_input:
            try:
                text = llm.chat_with_image(
                    question,
                    image_input,
                    system="Bạn là trợ lý FPT AI Factory. Phân tích ảnh khách hàng gửi, trả lời bằng tiếng Việt, rõ ràng.",
                    model=settings.llm_vision_model,
                )
                return Answer(text=text, mode="vision", confidence=0.7, route=decision.to_dict())
            except LLMError as exc:
                logger.error("Vision lỗi: %s", exc)
                return Answer(
                    text=f"Không phân tích được ảnh: {exc}. Tạo ticket để L3 hỗ trợ.",
                    mode="vision",
                    confidence=0.0,
                    escalate_suggested=True,
                    route=decision.to_dict(),
                )
        return Answer(
            text="Yêu cầu phân tích ảnh cần model vision (LLM_VISION_MODEL) và ảnh đính kèm (image_data/image_url). "
                 "Vui lòng bổ sung cấu hình hoặc tạo ticket để L3 hỗ trợ.",
            mode="vision",
            confidence=0.0,
            escalate_suggested=True,
            route=decision.to_dict(),
        )

    if intent == "out_of_scope":
        return Answer(
            text="Câu hỏi này ngoài phạm vi hỗ trợ của FPT AI Factory. Vui lòng chuyển khách hàng "
                 "đến bộ phận phù hợp hoặc tạo ticket để đầu mối xử lý.",
            mode="llm" if llm.available else "keyword",
            confidence=0.0,
            escalate_suggested=True,
            route=decision.to_dict(),
        )

    # chat_rag (mặc định)
    answer = generate_answer(question, retriever, llm, settings, model=model)
    answer.route = decision.to_dict()
    return answer


def answer_question(
    question: str,
    retriever: HybridRetriever,
    llm: LLMClient,
    settings: Settings,
    image_url: str | None = None,
    image_data: str | None = None,
    model: str | None = None,
    agent_system: str | None = None,
) -> Answer:
    """Pipeline đầy đủ: judge decision (router) → dispatch (vLLM/LLM/RAG/image/vision)."""
    decision = route(question, llm, settings)
    return _dispatch(
        decision, question, image_url, image_data, retriever, llm, settings,
        model=model, agent_system=agent_system,
    )