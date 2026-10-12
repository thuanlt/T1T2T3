"""Registry dịch vụ FPT AI Factory + agent chuyên trách (trụ !)."""
from __future__ import annotations

SERVICE_REGISTRY = [
    {"key": "portal", "name": "Portal v2", "owner": "Sơn", "category": "Platform",
     "desc": "Cổng quản trị, đăng ký dịch vụ, quản lý API key.", "depends_on": ["billing"]},
    {"key": "billing", "name": "Billing", "owner": "Quyên", "category": "Finance",
     "desc": "Hóa đơn, thanh toán, hạn mức tài khoản.", "depends_on": []},
    {"key": "voucher", "name": "Cấp voucher", "owner": "Duyên", "category": "Finance",
     "desc": "Cấp mã voucher dùng thử, gia hạn trial.", "depends_on": ["billing"]},
    {"key": "serverless", "name": "Serverless Inference", "owner": "Sang", "category": "Inference",
     "desc": "Triển khai suy luận serverless, auto-scale.", "depends_on": ["gpu-vm"]},
    {"key": "dedicated", "name": "Dedicated Inference", "owner": "Nguyên", "category": "Inference",
     "desc": "GPU H100 instances chuyên dụng, cấu hình riêng.", "depends_on": ["gpu-vm", "network-volume"]},
    {"key": "gpu-vm", "name": "GPU VM", "owner": "Duy", "category": "Compute",
     "desc": "Máy ảo GPU theo yêu cầu.", "depends_on": ["network-volume"]},
    {"key": "gpu-container", "name": "GPU Container", "owner": "Vinh", "category": "Compute",
     "desc": "Chạy workload trong container có GPU.", "depends_on": ["gpu-vm"]},
    {"key": "metal", "name": "Metal Cloud", "owner": "Tuyền", "category": "Compute",
     "desc": "Bare metal server, truy cập vật lý.", "depends_on": []},
    {"key": "network-volume", "name": "Network Volume", "owner": "Duy", "category": "Storage",
     "desc": "Lưu trữ khối qua mạng, gắn vào instance.", "depends_on": []},
    {"key": "gpu-cluster", "name": "GPU Cluster", "owner": "ThanhTV", "category": "Compute",
     "desc": "Cụm GPU cho workload phân tán.", "depends_on": ["gpu-vm", "network-volume"]},
]

# Map dịch vụ → agent chuyên trách (trụ !)
SERVICE_TO_AGENT = {
    "portal": "portal",
    "billing": "billing",
    "voucher": "billing",
    "serverless": "gpu",
    "dedicated": "dedicated-inference",
    "gpu-vm": "gpu",
    "gpu-container": "gpu",
    "metal": "gpu",
    "network-volume": "network",
    "gpu-cluster": "gpu",
}

SERVICE_CATEGORIES = ["Platform", "Finance", "Inference", "Compute", "Storage"]

AGENT_REGISTRY = [
    {"name": "billing", "label": "Agent Billing", "icon": "💰",
     "desc": "Hóa đơn, thanh toán, hạn mức",
     "system": "Bạn là chuyên viên Billing của FPT AI Factory. Trả lời bằng tiếng Việt, tập trung vào hóa đơn, thanh toán, hạn mức tài khoản. Nếu cần tra cứu tài liệu, hãy gợi ý hỏi chi tiết hơn."},
    {"name": "dedicated-inference", "label": "Agent Dedicated Inference", "icon": "🎛️",
     "desc": "GPU H100, cấu hình, giá",
     "system": "Bạn là chuyên viên Dedicated Inference của FPT AI Factory. Trả lời bằng tiếng Việt, tập trung vào gói H100 GPU Instances, cấu hình, giá và vận hành. Nếu cần tra cứu tài liệu, hãy gợi ý hỏi chi tiết hơn."},
    {"name": "portal", "label": "Agent Portal", "icon": "🖥️",
     "desc": "Đăng ký, API key, truy cập",
     "system": "Bạn là chuyên viên Portal v2 của FPT AI Factory. Trả lời bằng tiếng Việt, tập trung vào đăng ký dịch vụ, quản lý API key, truy cập cổng. Nếu cần tra cứu tài liệu, hãy gợi ý hỏi chi tiết hơn."},
    {"name": "network", "label": "Agent Network & Storage", "icon": "🌐",
     "desc": "Network Volume, kết nối",
     "system": "Bạn là chuyên viên Network & Storage của FPT AI Factory. Trả lời bằng tiếng Việt, tập trung vào Network Volume, kết nối mạng, lưu trữ. Nếu cần tra cứu tài liệu, hãy gợi ý hỏi chi tiết hơn."},
    {"name": "gpu", "label": "Agent GPU Compute", "icon": "⚙️",
     "desc": "GPU VM, Container, Cluster, Metal",
     "system": "Bạn là chuyên viên GPU Compute của FPT AI Factory. Trả lời bằng tiếng Việt, tập trung vào GPU VM, GPU Container, GPU Cluster, Metal Cloud. Nếu cần tra cứu tài liệu, hãy gợi ý hỏi chi tiết hơn."},
]


def get_agent(name: str) -> dict | None:
    for a in AGENT_REGISTRY:
        if a["name"] == name:
            return a
    return None