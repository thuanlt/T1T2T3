"""Model + nghiệp vụ ticket (escalation L1→L2→L3)."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
import json

from . import db

VALID_STATUSES = {"open", "escalated_to_l3", "resolved"}
VALID_LEVELS = {"L1", "L2", "L3"}

# Đại diện kỹ thuật L3 theo dịch vụ
L3_ASSIGNEE_MAP = {
    "Portal v2": "Sơn",
    "Billing": "Quyên",
    "Cấp voucher": "Duyên",
    "Serverless Inference": "Sang",
    "Dedicated Inference": "Nguyên",
    "GPU VM": "Duy",
    "GPU Container": "Vinh",
    "Metal Cloud": "Tuyền",
    "Network Volume": "Duy",
    "GPU Cluster": "ThanhTV",
}


@dataclass
class Ticket:
    subject: str
    description: str
    transcript: list[dict] = field(default_factory=list)
    status: str = "open"
    level: str = "L2"
    resolution: str = ""
    assignee: str = ""
    id: int | None = None

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "subject": self.subject,
            "description": self.description,
            "transcript": self.transcript,
            "status": self.status,
            "level": self.level,
            "resolution": self.resolution,
            "assignee": self.assignee,
        }


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def create_ticket(db_path: str, ticket: Ticket) -> Ticket:
    if ticket.status not in VALID_STATUSES:
        raise ValueError(f"Status không hợp lệ: {ticket.status}")
    if ticket.level not in VALID_LEVELS:
        raise ValueError(f"Level không hợp lệ: {ticket.level}")
    if ticket.level == "L3" and not ticket.assignee.strip():
        raise ValueError("Vui lòng chọn kỹ thuật viên L3 phụ trách")
    now = _now()
    tid = db.insert_ticket(
        db_path,
        {
            "subject": ticket.subject,
            "description": ticket.description,
            "transcript": json.dumps(ticket.transcript, ensure_ascii=False),
            "status": ticket.status,
            "level": ticket.level,
            "created_at": now,
            "updated_at": now,
            "resolution": ticket.resolution,
            "assignee": ticket.assignee,
        },
    )
    ticket.id = tid
    db.insert_audit(
        db_path,
        tid,
        "created",
        f"Ticket {ticket.level} tạo bởi L1/L2" + (f" · assignee {ticket.assignee}" if ticket.assignee else ""),
    )
    return ticket


def list_tickets(db_path: str) -> list[dict]:
    return db.list_tickets(db_path)


def get_ticket(db_path: str, ticket_id: int) -> dict | None:
    return db.get_ticket(db_path, ticket_id)


def update_ticket(db_path: str, ticket_id: int, *, status: str | None = None, resolution: str | None = None) -> bool:
    if status is not None and status not in VALID_STATUSES:
        raise ValueError(f"Status không hợp lệ: {status}")
    old = db.get_ticket(db_path, ticket_id)
    ok = db.update_ticket(db_path, ticket_id, status=status, resolution=resolution)
    if ok and old:
        if status and status != old["status"]:
            db.insert_audit(db_path, ticket_id, "status_change", f"{old['status']} → {status}")
        if resolution:
            db.insert_audit(db_path, ticket_id, "resolved", f"Đã xử lý: {resolution[:120]}")
    return ok