# FAQ Lỗi 403 Forbidden — Cloudflare error code 1010

## Lỗi 403 Forbidden kèm "error code: 1010" là gì?

Đây là lỗi **từ tầng Cloudflare** (WAF/CDN), KHÔNG phải lỗi từ hệ thống API FPT AI Factory.
Khi gọi API hoặc callback nhận phản hồi:

- HTTP Status: `403 Forbidden`
- Response header có dấu hiệu Cloudflare: `Server: cloudflare`, `CF-RAY: ...`, `cf-nel`
- Error body: `error code: 1010`

Error code 1010 nghĩa là **"The owner of this website has banned your access based on your browser's signature"** — Cloudflare chặn request vì không tin tưởng client (kiểm tra Browser Integrity Check / User-Agent / IP).

## Nguyên nhân phổ biến

1. **IP nguồn bị Cloudflare chặn** — IP của khách hàng bị liệt vào danh sách chặn (do spam, brute-force, hoặc IP dùng chung bị nhiễm).
2. **User-Agent bất thường** — request gửi từ script/bot với User-Agent trống hoặc giống bot bị chặn.
3. **Browser Integrity Check (BIC)** — Cloudflare không xác thực được client (thiếu cookie `cf_clearance`, JS challenge không pass).
4. **WAF rule / Firewall rule** — rule chặn theo country, ASN, hoặc pattern trong request.
5. **Callback từ server khác** — server của khách hàng gọi callback nhưng IP server bị chặn hoặc không có `cf_clearance`.

## Cách xử lý L1/L2

1. **Xác nhận đúng là lỗi Cloudflare**: kiểm tra response header có `Server: cloudflare` và `CF-RAY` không. Nếu có → lỗi tầng Cloudflare, không phải lỗi API.
2. **Thu thập thông tin từ khách hàng**:
   - IP nguồn (IPv4/IPv6) gửi request.
   - User-Agent đang dùng.
   - Thời điểm xảy ra + tần suất.
   - Đầy đủ request log (method, URL, headers).
3. **Hướng dẫn khách hàng kiểm tra**:
   - Thử từ mạng/IP khác (VD chuyển từ office sang 4G) để xác định có phải IP bị chặn.
   - Đảm bảo request có User-Agent chuẩn của HTTP client (không để trống).
   - Nếu gọi qua trình duyệt: thử hard refresh, xóa cache/cookie, tắt VPN.
   - Nếu gọi qua server/cron: kiểm tra IP server có nằm trong danh sách chặn không.
4. **Kiểm tra phía FPT**: xác nhận IP khách hàng không nằm trong danh sách chặn nội bộ; kiểm tra log gateway xem request có tới được không.

## Khi nào escalate L3

- Đã thử các bước trên nhưng vẫn 403/1010.
- Khách hàng cần whitelist IP hoặc điều chỉnh WAF rule — việc này cần đội vận hành hạ tầng/L3 xử lý.
- Nghi ngờ IP khách hàng bị chặn oan do dùng chung IP bị nhiễm.

Khi tạo ticket escalate, kèm đầy đủ: IP nguồn, User-Agent, request log, thời điểm, và xác nhận đã thử từ IP khác.