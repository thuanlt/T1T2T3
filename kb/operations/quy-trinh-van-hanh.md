# Quy trình vận hành hỗ trợ khách hàng

## Mô hình hỗ trợ 3 tầng (L1/L2/L3)

Luồng xử lý support của FPT AI Factory:

1. **Khách hàng** gửi yêu cầu qua các kênh: servicedesk.fci.vn, email, điện thoại.
2. **L1** tiếp nhận thông tin, phân loại yêu cầu, ghi nhận ticket trên hệ thống.
3. **L2** (đội vận hành) xử lý bằng kho tài liệu: tài liệu vận hành, hướng dẫn sử dụng, FAQ, và hướng dẫn từ đội sản phẩm L3.
4. Nếu L2 **không xử lý được**, đẩy ticket về **đầu mối FPT AI Factory** (team group).
5. Đầu mối chuyển tiếp cho **L3** (đội sản phẩm/tech) xử lý và hỗ trợ.

## Phân loại mức độ ưu tiên

| Mức | Mô tả | Thời gian phản hồi | Thời gian xử lý |
|---|---|---|---|
| P1 | Dịch vụ ngừng hoạt động, ảnh hưởng toàn bộ khách hàng | 30 phút | 4 giờ |
| P2 | Sự cố nghiêm trọng ảnh hưởng một khách hàng | 2 giờ | 8 giờ |
| P3 | Sự cố nhỏ, không gián đoạn | 4 giờ | 24 giờ |
| P4 | Yêu cầu thông tin, tư vấn | 8 giờ | 3 ngày |

## Quy trình xử lý ticket

1. **Tiếp nhận**: L1 tạo ticket, điền đầy đủ thông tin khách hàng, mô tả sự cố, mức ưu tiên.
2. **Phân tích**: L2 tra cứu kho tài liệu, xác định nguyên nhân và phương án xử lý.
3. **Xử lý**: Áp dụng hướng dẫn từ tài liệu, thông báo khách hàng tiến độ.
4. **Escalate**: Nếu hết khả năng, chuyển ticket lên đầu mối FPT AI Factory → L3, kèm toàn bộ ngữ cảnh.
5. **Đóng ticket**: Xác nhận với khách hàng, ghi lại bài học kinh nghiệm, cập nhật kho tài liệu nếu cần.

## Yêu cầu thông tin tối thiểu khi tạo ticket

- Tên khách hàng, mã khách hàng, gói dịch vụ.
- Kênh tiếp nhận (servicedesk, email, phone).
- Mô tả sự cố: thời điểm xảy ra, tần suất, ảnh hưởng.
- Mã lỗi, log, request/response mẫu (nếu có).
- Bước đã thử và kết quả.

## Nguyên tắc giao tiếp với khách hàng

- Luôn xác nhận đã nhận yêu cầu trong vòng 30 phút làm việc.
- Cập nhật trạng thái cho khách hàng mỗi 4 giờ làm việc với ticket P1/P2.
- Không hứa thời gian xử lý ngoài SLA đã cam kết.
- Ngôn ngữ rõ ràng, tránh thuật ngữ kỹ thuật khi không cần thiết.