# Hướng dẫn sử dụng FPT GenAI Platform (package_genai)

## Giới thiệu

package_genai cung cấp API truy cập các mô hình ngôn ngữ lớn (LLM) của FPT. Khách hàng gọi API theo chuẩn tương thích OpenAI để tích hợp chatbot, tóm tắt văn bản, sinh nội dung.

## Lấy API key

1. Đăng nhập portal quản trị của FPT AI Factory.
2. Vào mục **API Keys** → **Generate New Key**.
3. Đặt tên cho key và chọn hạn mức.
4. Copy key ngay lập tức (chỉ hiển thị một lần).
5. Key có dạng `fpt-xxxxxxxxxxxx`.

## Gọi API Chat Completion

Endpoint: `POST /v1/chat/completions`

Header bắt buộc:

```
Authorization: Bearer <API_KEY>
Content-Type: application/json
```

Body mẫu:

```json
{
  "model": "fpt-genai-2",
  "messages": [
    {"role": "system", "content": "Bạn là trợ lý hữu ích."},
    {"role": "user", "content": "Xin chào!"}
  ],
  "temperature": 0.7
}
```

## Rate limit mặc định

- Gói Standard: 60 request/phút.
- Gói Pro: 300 request/phút.
- Gói Enterprise: tùy chỉnh theo hợp đồng.

Khi vượt hạn mức, API trả về mã lỗi `429` kèm header `Retry-After`.

## Xử lý lỗi phổ biến

| Mã lỗi | Ý nghĩa | Xử lý |
|---|---|---|
| 400 | Request sai định dạng | Kiểm tra lại body theo tài liệu |
| 401 | API key không hợp lệ | Kiểm tra key, tạo key mới nếu cần |
| 404 | Model hoặc endpoint không tồn tại | Kiểm tra tên model chính xác |
| 413 | Payload quá lớn | Giảm kích thước input |
| 429 | Vượt rate limit | Retry với backoff, nâng gói nếu cần |
| 500 | Lỗi hệ thống | Báo L2, kiểm tra trang trạng thái |

## Giới hạn mô hình

- Max input tokens: 32.000 tokens.
- Max output tokens: 4.000 tokens.
- Không hỗ trợ streaming cho gói Standard (chỉ gói Pro trở lên).