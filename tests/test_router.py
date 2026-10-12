from app.config import get_settings
from app.llm import LLMClient
from app.rag import answer_question
from app.retrieval import HybridRetriever
from app.router import _heuristic_route, _parse_intent, _parse_systemone, route

from conftest import DB_PATH


def _ctx():
    settings = get_settings()
    llm = LLMClient(api_key="", base_url=settings.llm_base_url, chat_model="m", embed_model="e")
    from app.indexer import build_retriever, ingest

    ingest(settings, llm)
    chunks, _ = build_retriever(settings)
    return settings, llm, HybridRetriever(chunks)


def test_heuristic_routes_image_generate():
    s = get_settings()
    d = _heuristic_route("Tạo cho tôi một logo công ty", s)
    assert d.intent == "image_generate"


def test_heuristic_routes_image_analyze():
    s = get_settings()
    d = _heuristic_route("Phân tích ảnh này giúp tôi", s)
    assert d.intent == "image_analyze"


def test_heuristic_routes_out_of_scope():
    s = get_settings()
    d = _heuristic_route("Thời tiết hôm nay thế nào", s)
    assert d.intent == "out_of_scope"


def test_heuristic_defaults_to_chat_rag():
    s = get_settings()
    d = _heuristic_route("API trả về lỗi 401 thì sao?", s)
    assert d.intent == "chat_rag"


def test_parse_intent_extracts_json():
    intent, reason = _parse_intent('{"intent": "image_generate", "reason": "user wants image"}')
    assert intent == "image_generate"
    assert "image" in reason


def test_parse_intent_fallback_on_garbage():
    intent, _ = _parse_intent("không phải json")
    assert intent == "chat_rag"


def test_route_falls_back_to_heuristic_without_llm():
    s, llm, _ = _ctx()
    d = route("Tạo ảnh minh họa cho bài viết", llm, s)
    assert d.intent == "image_generate"
    assert d.router_mode == "heuristic"


def test_answer_question_routes_image_generate_without_model():
    s, llm, retriever = _ctx()
    ans = answer_question("Tạo cho tôi một banner quảng cáo", retriever, llm, s)
    assert ans.route is not None and ans.route["intent"] == "image_generate"
    assert ans.escalate_suggested is True


def test_answer_question_rag_keeps_route():
    s, llm, retriever = _ctx()
    ans = answer_question("API trả về lỗi 401 thì xử lý sao?", retriever, llm, s)
    assert ans.route is not None and ans.route["intent"] == "chat_rag"
    assert ans.sources


def test_answer_question_out_of_scope():
    s, llm, retriever = _ctx()
    ans = answer_question("Thời tiết hôm nay thế nào?", retriever, llm, s)
    assert ans.route is not None and ans.route["intent"] == "out_of_scope"
    assert ans.escalate_suggested is True


def test_answer_question_with_image_forces_vision():
    s, llm, retriever = _ctx()
    ans = answer_question(
        "Xem giúp tôi",
        retriever,
        llm,
        s,
        image_data="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==",
    )
    assert ans.route is not None and ans.route["intent"] == "image_analyze"


def test_parse_systemone_choice_and_signals():
    s = get_settings()
    answers = {
        "intent": {"choice": "image_generate", "confidence": 0.983, "type": "choice"},
        "urgent": {"noul": 0.871, "type": "noul"},
        "mood": {"score": 0.981, "legend": {"0": "calm", "1": "annoyed", "2": "angry"}, "type": "score"},
    }
    d = _parse_systemone(answers, s, "Quyet-1.0-Large")
    assert d.intent == "image_generate"
    assert d.router_mode == "systemone"
    assert d.confidence == 0.983
    assert d.urgent is True
    assert d.mood == "angry"
    assert d.model == s.llm_image_model


def test_parse_systemone_defaults_on_garbage():
    s = get_settings()
    d = _parse_systemone({}, s, "Quyet-1.0-Large")
    assert d.intent == "chat_rag"
    assert d.urgent is False
    assert d.mood == ""