# Kiểm tra hệ thống và giám sát

## Kiểm tra nhanh (Health Check)

Khi khách hàng báo sự cố, L2 thực hiện kiểm tra nhanh theo thứ tự:

1. **Trang trạng thái dịch vụ**: truy cập trang trạng thái nội bộ, xác nhận không có sự cố đang diễn ra.
2. **Dashboard giám sát**: kiểm tra độ trễ, tỷ lệ lỗi, tỷ lệ thành công của API trong 24 giờ gần nhất.
3. **Log tập trung**: tìm log theo mã khách hàng và khoảng thời gian sự cố.
4. **Portal quản trị**: kiểm tra trạng thái API key, mức sử dụng, hạn mức của khách hàng.

## Các chỉ số cần kiểm tra

| Chỉ số | Mô tả | Cảnh báo |
|---|---|---|
| Error rate | Tỷ lệ request lỗi (4xx/5xx) | > 1% trong 5 phút |
| Latency p95 | Độ trễ phân vị 95 | > 3 giây |
| Queue depth | Độ sâu hàng đợi xử lý | Tăng liên tục 15 phút |
| Utilization | Mức sử dụng GPU/CPU | > 85% kéo dài |

## Xử lý khi phát hiện bất thường

- Ghi nhận thời điểm bắt đầu và kết thúc bất thường.
- Thông báo cho đội trực theo kênh nội bộ (P1/P2).
- Tạo ticket nội bộ kèm biểu đồ và log.
- Theo dõi đến khi chỉ số trở lại bình thường.

## Checklist trước khi escalate L3

- [ ] Đã kiểm tra trang trạng thái và dashboard.
- [ ] Đã thu thập log, request/response mẫu.
- [ ] Đã xác nhận API key và hạn mức của khách hàng.
- [ ] Đã thử các hướng dẫn trong tài liệu.
- [ ] Đã ghi đầy đủ thông tin vào ticket.