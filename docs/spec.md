# SPEC: FPT AI Factory Support Agent (L1/L2)

## 1. Objective

Xây dựng agent hỗ trợ đội **L1/L2** của FPT AI Factory trong luồng xử lý support khách hàng:

```
Khách hàng ──► Kênh tiếp nhận (servicedesk.fci.vn) ──► L1 ──► L2 (vận hành)
                                                          │
                              ┌───────────────────────────┤
                              ▼                           ▼
                     Agent trả lời bằng KB            Case khó
                    (tài liệu vận hành, HD sử dụng,     │
                     FAQ có sẵn)                        ▼
                                                Đầu mối FPT AI Factory ──► L3
```

Agent giúp L1/L2 trả lời nhanh, chính xác dựa trên knowledge base (tài liệu vận hành,
hướng dẫn sử dụng, FAQ + đáp án). Chỉ những case **không xử lý được** mới tạo ticket
đẩy lên L3.

### Người dùng
- **L1**: tiếp nhận thông tin khách hàng từ các kênh, hỏi agent để có câu trả lời chuẩn.
- **L2**: đội vận hành, tra cứu tài liệu qua agent, soạn câu trả lời, quyết định escalate L3.

### Tiêu chí thành công
- L1/L2 nhập câu hỏi → nhận câu trả lời có **trích dẫn nguồn tài liệu** (citations).
- Câu hỏi không có trong KB → agent báo rõ "không đủ thông tin" + gợi ý escalate.
- Nút "Không giải quyết được" → tạo ticket kèm **toàn bộ ngữ cảnh hội thoại** đẩy L3.
- Chạy được qua Preview, có test tự động, có tài liệu vận hành.

## 2. Tech Stack

| Thành phần | Lựa chọn | Lý do |
|---|---|---|
| Ngôn ngữ | Python 3.11 | Hệ sinh thái AI/RAG mạnh |
| Web framework | FastAPI + Uvicorn | Async, nhẹ, tự động docs |
| LLM | OpenAI-compatible API (chat + embeddings) | Cấu hình qua env, đổi provider dễ |
| Vector search | NumPy cosine similarity trên SQLite | Nhẹ, không cần service ngoài |
| Storage | SQLite | Không cần DB riêng, dễ vận hành |
| Frontend | HTML/JS tĩnh do FastAPI serve | Nhẹ, không build step |
| Test | pytest | Chuẩn Python |

## 3. Commands

```bash
# Cài đặt
pip install -r requirements.txt

# Chạy dev (qua Preview)
uvicorn app.main:app --host 0.0.0.0 --port 8000

# Test
pytest -q

# Nạp lại KB (sau khi sửa tài liệu)
python scripts/ingest_kb.py
```

## 4. Project Structure

```
.
├── app/
│   ├── main.py          # FastAPI app + routes
│   ├── config.py        # Settings từ env
│   ├── llm.py           # Client LLM (chat + embeddings), fallback keyword
│   ├── retrieval.py     # Chunking, embedding, vector + keyword search
│   ├── rag.py           # Sinh câu trả lời RAG + citations
│   ├── tickets.py       # Model + storage ticket/escalation
│   └── db.py            # SQLite helpers
├── static/              # Web chat console (HTML/CSS/JS)
├── kb/                  # Knowledge base (markdown)
│   ├── faq/             # FAQ + đáp án
│   ├── operations/      # Tài liệu vận hành
│   └── guides/          # Hướng dẫn sử dụng dịch vụ
├── scripts/
│   └── ingest_kb.py     # Nạp KB → index (embedding/chunks)
├── tests/               # pytest
├── docs/
│   ├── spec.md          # (file này)
│   ├── plan.md          # Kế hoạch triển khai
│   └── ops.md           # Hướng dẫn vận hành cho L1/L2/admin
└── requirements.txt
```

## 5. Code Style

- Python: PEP8, type hints, docstring ngắn tiếng Việt/Anh, không comment thừa.
- Module không phụ thuộc vòng: `config → db → llm → retrieval → rag → tickets → main`.
- Mọi cấu hình nhạy cảm qua env (`LLM_API_KEY`...), không hardcode secret.
- Ví dụ:

```python
from dataclasses import dataclass

@dataclass
class Source:
    title: str
    path: str
    snippet: str

def answer(question: str) -> Answer:
    ...
```

## 6. Testing Strategy

- `tests/test_retrieval.py` — chunking, search trả về kết quả đúng thứ tự.
- `tests/test_rag.py` — pipeline trả lời có sources; câu ngoài KB → low confidence.
- `tests/test_api.py` — TestClient: `/api/chat`, `/api/tickets`, `/api/health`.
- Chạy `pytest -q` trước khi kết thúc mỗi phase.

## 7. Boundaries

- **Always**: validate input, trả citations, test trước khi xong, log lỗi LLM.
- **Ask first**: thêm dependency mới, đổi schema DB, đổi LLM provider.
- **Never**: commit API key, ghi secret ra file/log, xóa ticket.

## 8. Success Criteria

- [ ] `pytest -q` pass toàn bộ.
- [ ] `/api/chat` trả câu trả lời + `sources[]` từ KB.
- [ ] Câu hỏi ngoài KB → `confidence` thấp + khuyến nghị escalate.
- [ ] `/api/tickets` tạo ticket kèm transcript, có status `escalated_to_l3`.
- [ ] Web console: chat + nút escalate + danh sách ticket.
- [ ] Chạy được qua Preview (app-preview skill).

## 9. Open Questions

- (Đã hỏi) Cơ chế trả lời: RAG + LLM qua OpenAI-compatible API. ✅
- (Đã hỏi) Giao diện: Web chat console. ✅
- (Đã hỏi) Stack: Python FastAPI. ✅
- KB thật sẽ được đưa vào `kb/` sau; hiện dùng dữ liệu mẫu FPT AI Factory.