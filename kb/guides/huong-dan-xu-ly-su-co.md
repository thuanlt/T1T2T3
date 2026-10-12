# Hướng dẫn xử lý sự cố theo từng dịch vụ

## package_vision (Computer Vision)

### Lỗi ảnh không nhận diện được

1. Kiểm tra định dạng ảnh: hỗ trợ JPEG, PNG, WEBP, tối đa 10MB.
2. Kiểm tra kích thước tối thiểu: mặt người cần tối thiểu 80x80 pixel.
3. Kiểm tra chất lượng ảnh: không bị mờ, không bị che khuất.
4. Ảnh quá tối hoặc ngược sáng có thể giảm độ chính xác.

### Độ chính xác nhận diện thấp

- Sử dụng ảnh có độ phân giải cao hơn.
- Đảm bảo đối tượng chiếm trên 30% diện tích ảnh.
- Liên hệ L3 nếu cần tinh chỉnh mô hình cho domain cụ thể.

## package_ocr (Document AI)

### Trích xuất sai nội dung

1. Kiểm tra độ phân giải bản scan: khuyến nghị 300 DPI trở lên.
2. Kiểm tra ảnh có bị nghiêng, méo không.
3. Kiểm tra loại giấy tờ có trong danh sách hỗ trợ không.
4. Hóa đơn, chứng từ cần đúng template chuẩn.

### Không nhận diện được chữ viết tay

- package_ocr hiện chỉ hỗ trợ chữ in.
- Chữ viết tay chuyển sang package_vision với mô hình chuyên dụng (nếu có).

## package_voice (TTS/ASR)

### Audio không nhận diện được

1. Kiểm tra định dạng: WAV, MP3, FLAC, tối đa 15 phút.
2. Kiểm tra sample rate: 16kHz trở lên.
3. Kiểm tra tạp âm nền: giảm nhiễu trước khi gửi.
4. Tiếng Việt cần đúng giọng miền (Bắc/Trung/Nam) đã đăng ký.

### Giọng đọc TTS không tự nhiên

- Sử dụng tham số `speed` trong khoảng 0.8–1.2.
- Kiểm tra dấu câu trong văn bản đầu vào.
- Văn bản chứa số, đơn vị cần định dạng rõ ràng.

## package_conversational (Chatbot)

### Bot không trả lời đúng ý

1. Kiểm tra cấu hình intent và entity trong nền tảng.
2. Kiểm tra training data đã được huấn luyện lại chưa.
3. Thu thập câu hỏi thực tế của khách hàng để bổ sung training.
4. Nếu vấn đề thuộc về mô hình NLU, tạo ticket đẩy L3.