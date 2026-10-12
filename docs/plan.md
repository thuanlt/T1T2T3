# Implementation Plan: FPT AI Factory Support Agent

## Overview

Agent hỗ trợ L1/L2 trả lời khách hàng dựa trên knowledge base (RAG + LLM qua
OpenAI-compatible API), kèm luồng escalate tạo ticket đẩy L3 khi không xử lý được.

## Architecture Decisions

1. **RAG pipeline**: chunk KB markdown → embedding (LLM API) → lưu SQLite →
   hybrid search (cosine + keyword) → LLM sinh câu trả lời kèm citations.
2. **Graceful degradation**: nếu chưa cấu hình API key → chạy chế độ keyword-only
   (vẫn trả về đoạn tài liệu khớp, đánh dấu `mode=keyword`), demo chạy được ngay.
3. **SQLite + NumPy**: không cần service ngoài, dễ vận hành, đủ cho KB trăm-chunk.
4. **Ticket = escalation object**: lưu transcript + câu trả lời agent + mức độ
   (L1→L2→L3), status machine đơn giản `open → escalated_to_l3 → resolved`.
5. **Frontend tĩnh**: FastAPI serve `static/`, không build step.

## Task List

### Phase 1: Foundation
- [ ] Task 1: Scaffold project (requirements, config, db helpers)
- [ ] Task 2: KB seed data (faq/operations/guides mẫu FPT AI Factory)
- [ ] Task 3: LLM client + fallback keyword mode

### Checkpoint 1
- [ ] Import toàn bộ module không lỗi, config đọc từ env

### Phase 2: Retrieval + RAG
- [ ] Task 4: Chunking + ingestion script (`scripts/ingest_kb.py`)
- [ ] Task 5: Hybrid retrieval (cosine + keyword) + tests
- [ ] Task 6: RAG answer generation + citations + tests

### Checkpoint 2
- [ ] `pytest -q` pass; chat pipeline chạy được qua REPL

### Phase 3: API + Tickets
- [ ] Task 7: `/api/chat`, `/api/health` + tests
- [ ] Task 8: Ticket/escalation model + `/api/tickets` + tests

### Checkpoint 3
- [ ] `pytest -q` pass; API chạy qua TestClient

### Phase 4: Frontend
- [ ] Task 9: Web chat console (chat + citations + nút escalate + ticket list)

### Checkpoint 4
- [ ] Preview chạy, luồng chat → escalate hoạt động end-to-end

### Phase 5: Ops
- [ ] Task 10: `docs/ops.md` (vận hành cho L1/L2/admin), README cập nhật

## Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Chưa có API key LLM | Không sinh được câu trả lời | Keyword fallback + hướng dẫn cấu hình rõ |
| Tài liệu KB thật chưa có | Demo thiếu tính thực tế | Seed dữ liệu mẫu sát nghiệp vụ FPT AI Factory |
| Embedding cần mạng | Ingest fail offline | Bắt lỗi, log rõ, cho phép retry |
| Prompt trả lời sai/ảo giác | Sai thông tin cho KH | System prompt bắt buộc trích nguồn, low-confidence → từ chối trả lời |

## Open Questions
- Provider LLM cụ thể (base_url/model) sẽ do user điền vào env khi chạy thật.