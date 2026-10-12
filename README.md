# FPT AI Factory Support Agent (L1/L2)

Agent hỗ trợ đội L1/L2 của FPT AI Factory trả lời khách hàng dựa trên kho tài liệu
(RAG + LLM), và tạo ticket escalate lên L3 khi không giải quyết được.

```
Khách hàng → servicedesk.fci.vn → L1 → L2 (Agent trả lời bằng KB) → không xử lý được → ticket → L3
```

## Tính năng

- **Chat RAG**: trả lời câu hỏi kèm % tin cậy + trích dẫn nguồn tài liệu.
- **Knowledge base**: `kb/` (faq, operations, guides) — markdown, nạp lại bằng 1 lệnh.
- **Escalation**: nút "Escalate L3" tạo ticket kèm toàn bộ ngữ cảnh hội thoại.
- **Chế độ linh hoạt**: có `LLM_API_KEY` → RAG đầy đủ; không có → keyword mode vẫn chạy.

## Chạy nhanh

```bash
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Mở `http://localhost:8000` (hoặc dùng Preview trong VibeFlow).

## Cấu hình

Xem `docs/ops.md` — biến môi trường `LLM_API_KEY`, `LLM_BASE_URL`, `LLM_CHAT_MODEL`,
`LLM_EMBED_MODEL`, `DB_PATH`, `KB_DIR`…

## Test

```bash
python -m pytest tests/ -q
```

## Tài liệu

- `docs/spec.md` — đặc tả
- `docs/plan.md` — kế hoạch triển khai
- `docs/ops.md` — hướng dẫn vận hành