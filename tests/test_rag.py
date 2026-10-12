from app.config import get_settings
from app.indexer import build_retriever, ingest
from app.llm import LLMClient
from app.rag import generate_answer

from conftest import DB_PATH


def _setup():
    settings = get_settings()
    llm = LLMClient(api_key="", base_url=settings.llm_base_url, chat_model="m", embed_model="e")
    ingest(settings, llm)
    chunks, _ = build_retriever(settings)
    from app.retrieval import HybridRetriever

    return settings, llm, HybridRetriever(chunks)


def test_answer_relevant_question_with_sources():
    settings, llm, retriever = _setup()
    ans = generate_answer("API trả về lỗi 401 thì xử lý sao?", retriever, llm, settings)
    assert ans.sources, "phải có nguồn trích dẫn"
    assert not ans.escalate_suggested
    assert ans.confidence > 0


def test_answer_out_of_kb_suggests_escalation():
    settings, llm, retriever = _setup()
    ans = generate_answer("thời tiết hôm nay thế nào", retriever, llm, settings)
    assert ans.escalate_suggested is True
    assert "L3" in ans.text


def test_empty_question_returns_guidance():
    settings, llm, retriever = _setup()
    ans = generate_answer("   ", retriever, llm, settings)
    assert "câu hỏi" in ans.text.lower() or "nhập" in ans.text.lower()


def test_answer_sources_are_unique():
    settings, llm, retriever = _setup()
    ans = generate_answer("Làm sao đăng ký sử dụng dịch vụ?", retriever, llm, settings)
    keys = {(s["path"], s["snippet"]) for s in ans.sources}
    assert len(keys) == len(ans.sources)