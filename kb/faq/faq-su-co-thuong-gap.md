# FAQ Sự cố thường gặp

## Khách hàng báo API trả về lỗi 401 Unauthorized

Nguyên nhân phổ biến:

1. API key sai hoặc hết hạn.
2. API key không được gửi đúng header `Authorization: Bearer <key>`.
3. API key bị vô hiệu hóa do vi phạm điều khoản hoặc quá hạn thanh toán.

Cách xử lý L1/L2:

- Kiểm tra lại API key với khách hàng, đối chiếu trên portal quản trị.
- Xác nhận định dạng request theo tài liệu tích hợp.
- Nếu key hết hạn, gia hạn qua portal và thông báo khách hàng.
- Nếu key bị vô hiệu hóa do thanh toán, chuyển sang đầu mối kinh doanh.

## Khách hàng báo lỗi 429 Too Many Requests

Lỗi 429 xảy ra khi vượt quá rate limit của gói dịch vụ.

Cách xử lý L1/L2:

- Kiểm tra mức sử dụng của khách hàng trên portal quản trị.
- Hướng dẫn khách hàng triển khai retry với exponential backoff.
- Nếu khách hàng cần dung lượng cao hơn, đề xuất nâng cấp gói hoặc tăng quota qua đầu mối kinh doanh.
- Ghi nhận thời điểm xảy ra và số lượng request bị từ chối.

## Khách hàng báo API chậm hoặc timeout

Các bước kiểm tra:

1. Kiểm tra trang trạng thái dịch vụ xem có sự cố đang diễn ra không.
2. Kiểm tra thời gian phản hồi trung bình trên dashboard giám sát.
3. Xác nhận khách hàng gọi đúng endpoint và region.
4. Kiểm tra payload request có quá lớn không (ví dụ ảnh dung lượng cao với package_vision).
5. Nếu độ trễ kéo dài trên 15 phút, tạo ticket khẩn đẩy L3.

## Khách hàng báo kết quả mô hình không chính xác

Cách xử lý L1/L2:

- Thu thập ví dụ cụ thể: request, response, dữ liệu đầu vào.
- Kiểm tra xem dữ liệu đầu vào có đúng định dạng và chất lượng không.
- Đối chiếu với tài liệu hướng dẫn về giới hạn của mô hình.
- Nếu vẫn sai, tạo ticket kèm ví dụ đầy đủ để L3 đánh giá và tinh chỉnh.

## Khách hàng báo không nhận được email thông báo

Kiểm tra:

- Email nằm trong thư mục spam/junk.
- Địa chỉ email đăng ký có đúng không.
- Kiểm tra trên portal xem thông báo đã được gửi chưa.
- Nếu cần, gửi lại email thông báo thủ công từ portal quản trị.