# Hướng dẫn vận hành — FPT AI Factory Support Agent

## 1. Tổng quan

Agent hỗ trợ đội **L1/L2** trả lời khách hàng dựa trên kho tài liệu (KB) của FPT AI Factory:
tài liệu vận hành, hướng dẫn sử dụng dịch vụ, FAQ + đáp án. Case không giải quyết được
sẽ tạo **ticket** kèm toàn bộ ngữ cảnh hội thoại đẩy lên **L3**.

```
Khách hàng → servicedesk.fci.vn → L1 → L2 (Agent hỗ trợ trả lời) → không xử lý được → ticket → L3
```

## 2. Cấu hình (biến môi trường)

| Biến | Mặc định | Mô tả |
|---|---|---|
| `LLM_API_KEY` | *(trống)* | API key LLM. Để trống → chạy chế độ keyword-only (không cần LLM). |
| `LLM_BASE_URL` | `https://api.openai.com/v1` | Base URL API tương thích OpenAI. |
| `LLM_CHAT_MODEL` | `gpt-4o-mini` | Model sinh câu trả lời (RAG/chat). |
| `LLM_EMBED_MODEL` | `text-embedding-3-small` | Model embedding. |
| `LLM_ROUTER_MODEL` | *(trống)* | Model **judge decision** — chạy TRƯỚC mỗi câu hỏi, quyết định route: `chat_rag` / `general` / `image_generate` / `image_analyze` / `out_of_scope` + tín hiệu `urgent` / `mood`. Nếu tên model chứa "quyet" → gọi endpoint **`/v1/systemone`** (FPT Quyet, trả choice/noul/score kèm confidence). Để trống → dùng `LLM_CHAT_MODEL` (chat completions JSON, hoặc heuristic keyword khi không có LLM). |
| `LLM_IMAGE_MODEL` | *(trống)* | Model tạo ảnh (`images/generations`). **FPT Smart Cloud hiện không có endpoint này** → để trống; yêu cầu tạo ảnh sẽ gợi ý escalate. |
| `LLM_VISION_MODEL` | *(trống)* | Model phân tích ảnh (multimodal). FPT có `Qwen2.5-VL-7B-Instruct`. Cần `image_url` công khai (FPT không nhận base64 data URI). |
| `DB_PATH` | `data/agent.db` | File SQLite. |
| `KB_DIR` | `kb` | Thư mục chứa tài liệu KB (markdown). |
| `TOP_K` | `5` | Số đoạn tài liệu truy xuất mỗi câu hỏi. |
| `LOW_CONF_THRESHOLD` | `0.35` | Ngưỡng tin cậy (chế độ vector/LLM). |
| `LLM_TIMEOUT` | `60` | Timeout (giây) mỗi request LLM. |
| `LLM_VERIFY_SSL` | `true` | Bật/tắt kiểm tra SSL khi gọi LLM. Đặt `false` nếu chạy sau proxy có cert tự ký (môi trường preview của VibeFlow). |
| `KEYWORD_CONF_THRESHOLD` | `0.15` | Ngưỡng tin cậy (chế độ keyword). |

**Cách cấu hình trong VibeFlow**: vào *Project settings → Environment variables* để đặt
`LLM_API_KEY` (cần restart sandbox). Hoặc sửa trực tiếp file `.env.preview` để preview
nhận ngay mà không cần restart.

## 3. Cập nhật kho tài liệu (KB)

1. Thêm/sửa file `.md` trong `kb/` theo cấu trúc:
   - `kb/faq/` — FAQ + đáp án.
   - `kb/operations/` — tài liệu vận hành.
   - `kb/guides/` — hướng dẫn sử dụng dịch vụ (có thể chia subfolder, VD `kb/guides/dedicated-inference/`).
2. Nạp lại index:
   ```bash
   python scripts/ingest_kb.py
   ```
   Hoặc gọi API: `POST /api/kb/reload`.

**Docs FPT Cloud → KB**: dùng `python scripts/fetch_fpt_docs.py` để crawl toàn bộ 2 category
**FPT AI Factory** (55 bài) và **AI Infrastructure** (40 bài) từ docs.fptcloud.com vào
`kb/guides/fpt-ai-factory/` và `kb/guides/ai-infrastructure/` (giữ nguyên cấu trúc URL
lồng nhau để tránh trùng tên bài Overview/Quickstart/FAQ). Script tự khám phá toàn bộ
bài qua sidebar + BFS qua các trang category. Chạy `--dry-run` để xem danh sách trước.

> Lưu ý: nếu có `LLM_API_KEY`, ingest sẽ tạo embedding cho tài liệu (tốn phí nhỏ).
> Nếu không có key, agent chạy chế độ keyword (vẫn trả về đoạn tài liệu khớp).

## 4. Vận hành hàng ngày cho L1/L2

- **Tra cứu**: nhập câu hỏi của khách hàng vào ô chat. Agent trả câu trả lời kèm
  **% tin cậy** và **nguồn tài liệu** (click để xem trích đoạn).
- **Tin cậy thấp / không có nguồn**: agent tự đề xuất tạo ticket. L1/L2 nên kiểm tra
  lại câu hỏi hoặc escalate.
- **Escalate L3**: bấm **Escalate L3** (hoặc nút trong câu trả lời), điền tiêu đề +
  mô tả. Transcript hội thoại tự động kèm theo. Ticket xuất hiện ở sidebar trái.
- **Theo dõi ticket**: sidebar hiển thị trạng thái `OPEN` / `L3` / `RESOLVED`. Click
  ticket để xem chi tiết.

## 5. API

| Method | Path | Mô tả |
|---|---|---|
| GET | `/api/health` | Trạng thái hệ thống, số chunks, chế độ (llm/keyword). |
| GET | `/api/models` | Danh sách model đang cấu hình (chat/embed/router/image/vision). |
| POST | `/api/chat` | `{question, session_id?, image_url?, image_data?}` → `{answer, confidence, sources[], escalate_suggested, route}`. `image_data` = base64 data URI (upload ảnh trực tiếp, ≤5MB). Có ảnh đính kèm → tự chuyển sang `image_analyze`. |
| POST | `/api/tickets` | Tạo ticket `{subject, description, transcript[], level}` |
| GET | `/api/tickets` | Danh sách ticket. |
| GET | `/api/tickets/{id}` | Chi tiết ticket. |
| PATCH | `/api/tickets/{id}` | Cập nhật `{status, resolution}`. |
| POST | `/api/kb/reload` | Nạp lại KB. |

Docs tự động tại `/docs` (Swagger UI).

## 6. Kiểm thử

```bash
pip install -r requirements.txt
python -m pytest tests/ -q
```

## 7. Khắc phục sự cố

| Triệu chứng | Nguyên nhân | Xử lý |
|---|---|---|
| Health báo `keyword` mode | Chưa đặt `LLM_API_KEY` | Đặt key trong `.env.preview` hoặc Env Vars, restart. |
| Embedding thất bại `SSL: CERTIFICATE_VERIFY_FAILED` | Proxy có cert tự ký | Thêm `LLM_VERIFY_SSL=false` vào `.env.preview`. |
| Câu trả lời không có nguồn | KB chưa có tài liệu liên quan | Bổ sung tài liệu vào `kb/`, reload. |
| `POST /api/chat` lỗi 500 | Lỗi LLM/network | Xem log; hệ thống tự fallback keyword. |
| Model trả `content` rỗng (reasoning model) | Reasoning model dùng hết token budget | App tự retry với budget ×2; vẫn lỗi thì tăng `max_tokens`. |
| Ticket tạo xong không thấy | DB path khác nhau | Kiểm tra `DB_PATH` nhất quán. |

## 8. Mở rộng sau này

- Tích hợp webhook servicedesk.fci.vn: khi ticket L1 tạo trên servicedesk → tự động
  POST vào `/api/tickets`.
- Gửi email/notification tới đầu mối FPT AI Factory khi ticket escalate.
- Thay SQLite bằng Postgres khi KB lớn (hàng chục nghìn chunks).
- Thêm auth (login L1/L2) trước khi đưa ra production.