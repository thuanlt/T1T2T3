"""Registry lỗi liên quan nhau (error correlation graph)."""
from __future__ import annotations

ERROR_REGISTRY = [
    {"code": "401", "name": "Unauthorized", "icon": "🔑",
     "symptoms": "API trả 401 khi gọi với API key.",
     "causes": ["API key hết hạn", "Sai key", "Key không có quyền với dịch vụ"],
     "related": ["403", "429"], "relation": "cause",
     "playbook": "/401-error", "service": "portal"},
    {"code": "403", "name": "Forbidden · Cloudflare 1010", "icon": "🚫",
     "symptoms": "403 Forbidden kèm error code 1010, header Server: cloudflare, CF-RAY.",
     "causes": ["IP nguồn bị chặn", "User-Agent trống", "Browser Integrity Check", "WAF rule"],
     "related": ["429"], "relation": "related",
     "playbook": "/403-error", "service": "platform"},
    {"code": "429", "name": "Rate limit / Quota", "icon": "⏳",
     "symptoms": "429 Too Many Requests, quota exceeded, rate limit.",
     "causes": ["Vượt rate limit", "Quota hết", "Hạn mức tài khoản chưa gia hạn"],
     "related": ["401", "billing"], "relation": "cause",
     "playbook": "/429-error", "service": "billing"},
    {"code": "503", "name": "Service Unavailable", "icon": "🔧",
     "symptoms": "503 khi gọi inference hoặc API.",
     "causes": ["Dedicated Inference quá tải", "GPU instance down", "Maintenance"],
     "related": ["timeout"], "relation": "related",
     "playbook": "/503-error", "service": "dedicated"},
    {"code": "timeout", "name": "Timeout", "icon": "⏱️",
     "symptoms": "Request timeout, connection timed out, gateway timeout.",
     "causes": ["Model xử lý chậm", "Network giữa client và API", "Instance quá tải"],
     "related": ["503"], "relation": "symptom",
     "playbook": "/timeout-error", "service": "dedicated"},
    {"code": "quota", "name": "Quota exceeded", "icon": "📊",
     "symptoms": "Quota exceeded, insufficient quota, hết hạn mức.",
     "causes": ["Hạn mức tài khoản thấp", "Chưa gia hạn", "Dùng quá gói"],
     "related": ["429", "billing"], "relation": "cause",
     "playbook": "/429-error", "service": "billing"},
]

SERVICE_ERRORS = {
    "portal": ["401"],
    "billing": ["429", "quota"],
    "dedicated": ["503", "timeout"],
    "serverless": ["429", "503"],
    "gpu-vm": ["503"],
    "gpu-container": ["503"],
    "gpu-cluster": ["503", "timeout"],
    "network-volume": ["timeout"],
    "metal": ["503"],
    "voucher": ["429"],
}


def get_error(code: str) -> dict | None:
    for e in ERROR_REGISTRY:
        if e["code"] == code:
            return e
    return None