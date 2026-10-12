from app.retrieval import (
    Chunk,
    HybridRetriever,
    KeywordIndex,
    VectorIndex,
    chunk_text,
    load_kb,
    normalize,
    tokenize,
)

DOC = """# Tài liệu mẫu

Đây là đoạn văn đầu tiên nói về dịch vụ OCR và trích xuất hóa đơn.

Đây là đoạn văn thứ hai nói về API key và xác thực bearer token.
"""


def test_normalize_removes_vietnamese_accents():
    assert normalize("Xử lý sự cố API") == "xu ly su co api"
    assert normalize("TRẢ VỀ LỖI 401") == "tra ve loi 401"


def test_tokenize_filters_stopwords():
    toks = tokenize("Làm sao để đăng ký sử dụng dịch vụ OCR")
    assert "lam" not in toks
    assert "sao" not in toks
    assert "dang" not in toks
    assert "ky" in toks


def test_chunk_text_splits_and_overlaps():
    chunks = chunk_text(DOC, max_chars=60, overlap=10)
    assert len(chunks) >= 2
    assert all(isinstance(c, str) and c for c in chunks)


TABLE_DOC = """# Bảng giá

| Gói | RAM | Giá/giờ |
|---|---|---|
| 1x GPU H100 SXM5 | 250GB | $3.70 |
| 2x GPU H100 SXM5 | 500GB | $7.40 |
| 3x GPU H100 SXM5 | 750GB | $11.10 |
| 4x GPU H100 SXM5 | 1000GB | $14.80 |
| 5x GPU H100 SXM5 | 1250GB | $18.50 |
| 6x GPU H100 SXM5 | 1500GB | $22.20 |
| 7x GPU H100 SXM5 | 1750GB | $25.90 |
| 8x GPU H100 SXM5 | 2000GB | $29.60 |
"""


def test_chunk_text_keeps_markdown_table_intact():
    chunks = chunk_text(TABLE_DOC, max_chars=100, overlap=10)
    table_chunks = [c for c in chunks if "1x GPU" in c]
    assert table_chunks, "bảng phải nằm trong ít nhất một chunk"
    assert any("8x GPU" in c for c in table_chunks), "bảng không được cắt giữa chừng"
    rows = [l for c in table_chunks for l in c.splitlines() if l.startswith("|") and "GPU" in l]
    assert len(rows) == 8


def test_load_kb_reads_seed_documents():
    chunks = load_kb("kb", max_chars=700, overlap=100)
    assert len(chunks) >= 10
    titles = {c.doc_title for c in chunks}
    assert any("FAQ" in t for t in titles)
    cats = {c.category for c in chunks}
    assert cats >= {"faq", "operations", "guides"}


def test_keyword_search_ranks_relevant_first():
    chunks = [
        Chunk(doc_path="a.md", doc_title="A", category="", content="API key hết hạn trả về lỗi 401 unauthorized"),
        Chunk(doc_path="b.md", doc_title="B", category="", content="Thời tiết hôm nay nắng đẹp"),
    ]
    idx = KeywordIndex(chunks)
    hits = idx.search("API trả về lỗi 401", top_k=2)
    assert hits and hits[0].doc_path == "a.md"
    assert hits[0].score > 0.3


def test_keyword_search_zero_for_unrelated():
    chunks = [Chunk(doc_path="a.md", doc_title="A", category="", content="Hướng dẫn OCR trích xuất hóa đơn")]
    idx = KeywordIndex(chunks)
    assert idx.search("thời tiết hôm nay ra sao", top_k=2) == []


def test_vector_index_cosine():
    chunks = [
        Chunk(doc_path="a.md", doc_title="A", category="", content="x", embedding=[1.0, 0.0]),
        Chunk(doc_path="b.md", doc_title="B", category="", content="y", embedding=[0.0, 1.0]),
    ]
    idx = VectorIndex(chunks)
    hits = idx.search([1.0, 0.0], top_k=2)
    assert hits[0].doc_path == "a.md"
    assert abs(hits[0].score - 1.0) < 1e-6


def test_hybrid_merges_vector_and_keyword():
    chunks = [
        Chunk(doc_path="a.md", doc_title="A", category="", content="lỗi 401 api key", embedding=[1.0, 0.0, 0.0]),
        Chunk(doc_path="b.md", doc_title="B", category="", content="chuyện khác", embedding=[0.0, 1.0, 0.0]),
    ]
    r = HybridRetriever(chunks)
    hits = r.search("lỗi 401", [1.0, 0.0, 0.0], top_k=2)
    assert hits[0].doc_path == "a.md"
    assert hits[0].mode == "hybrid"


def test_hybrid_falls_back_to_keyword_without_vectors():
    chunks = [Chunk(doc_path="a.md", doc_title="A", category="", content="lỗi 401 api key")]
    r = HybridRetriever(chunks)
    hits = r.search("lỗi 401", None, top_k=2)
    assert hits and hits[0].mode == "keyword"