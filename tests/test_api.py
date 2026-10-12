import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c


def test_health(client):
    resp = client.get("/api/health")
    assert resp.status_code == 200
    body = resp.json()
    assert body["status"] == "ok"
    assert body["chunks"] > 0
    assert body["mode"] in {"llm", "keyword"}


def test_chat_returns_answer_and_sources(client):
    resp = client.post("/api/chat", json={"question": "API trả về lỗi 401 thì xử lý sao?"})
    assert resp.status_code == 200
    body = resp.json()
    assert body["answer"]
    assert isinstance(body["sources"], list)
    assert body["confidence"] >= 0
    assert body["route"]["intent"] == "chat_rag"


def test_chat_routes_image_request(client):
    resp = client.post("/api/chat", json={"question": "Tạo cho tôi một logo công ty"})
    assert resp.status_code == 200
    body = resp.json()
    assert body["route"]["intent"] == "image_generate"


def test_chat_with_image_data_forces_vision(client):
    resp = client.post(
        "/api/chat",
        json={
            "question": "Xem giúp tôi ảnh này",
            "image_data": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==",
        },
    )
    assert resp.status_code == 200
    body = resp.json()
    assert body["route"]["intent"] == "image_analyze"


def test_models_endpoint(client):
    resp = client.get("/api/models")
    assert resp.status_code == 200
    body = resp.json()
    assert body["chat"]
    assert "image" in body
    assert "vision" in body
    assert "router" in body


def test_chat_validates_input(client):
    assert client.post("/api/chat", json={"question": ""}).status_code == 422


def test_ticket_crud_flow(client):
    created = client.post(
        "/api/tickets",
        json={
            "subject": "Lỗi 401 khách hàng ABC",
            "description": "Khách hàng báo API trả về 401",
            "transcript": [{"role": "user", "content": "API lỗi 401"}],
            "level": "L2",
        },
    )
    assert created.status_code == 201
    tid = created.json()["id"]
    assert created.json()["status"] == "open"

    listed = client.get("/api/tickets").json()
    assert any(t["id"] == tid for t in listed)

    detail = client.get(f"/api/tickets/{tid}").json()
    assert detail["transcript"][0]["content"] == "API lỗi 401"

    updated = client.patch(f"/api/tickets/{tid}", json={"status": "escalated_to_l3"})
    assert updated.status_code == 200
    assert updated.json()["status"] == "escalated_to_l3"

    resolved = client.patch(f"/api/tickets/{tid}", json={"status": "resolved", "resolution": "Đã xử lý"})
    assert resolved.json()["resolution"] == "Đã xử lý"


def test_ticket_invalid_level(client):
    resp = client.post(
        "/api/tickets",
        json={"subject": "x", "description": "y", "level": "L4"},
    )
    assert resp.status_code == 422


def test_ticket_l3_requires_assignee(client):
    resp = client.post(
        "/api/tickets",
        json={"subject": "x", "description": "y", "level": "L3"},
    )
    assert resp.status_code == 422

    ok = client.post(
        "/api/tickets",
        json={"subject": "x", "description": "y", "level": "L3", "assignee": "Nguyên"},
    )
    assert ok.status_code == 201
    assert ok.json()["assignee"] == "Nguyên"


def test_ticket_assignees_endpoint(client):
    d = client.get("/api/tickets/assignees").json()
    names = [a["name"] for a in d["assignees"]]
    assert "Nguyên" in names and "Sơn" in names and "ThanhTV" in names
    assert len(d["assignees"]) == 10


def test_services_and_agents_endpoints(client):
    svc = client.get("/api/services").json()
    assert len(svc["services"]) == 10
    assert any(s["key"] == "dedicated" and s["owner"] == "Nguyên" for s in svc["services"])
    ag = client.get("/api/agents").json()
    names = {a["name"] for a in ag["agents"]}
    assert {"billing", "dedicated-inference", "portal"} <= names


def test_kb_docs_endpoints(client):
    docs = client.get("/api/kb/docs").json()["docs"]
    assert len(docs) >= 10
    first = docs[0]["path"]
    detail = client.get(f"/api/kb/docs/{first}").json()
    assert detail["content"].strip()


def test_ticket_audit_logged(client):
    created = client.post(
        "/api/tickets",
        json={"subject": "audit test", "description": "desc", "level": "L2"},
    ).json()
    client.patch(f"/api/tickets/{created['id']}", json={"status": "escalated_to_l3"})
    events = client.get("/api/tickets/audit").json()["events"]
    actions = [e["action"] for e in events]
    assert "created" in actions and "status_change" in actions


def test_errors_endpoint(client):
    d = client.get("/api/errors").json()
    codes = {e["code"] for e in d["errors"]}
    assert {"401", "403", "429", "503"} <= codes
    assert d["service_errors"]["dedicated"] == ["503", "timeout"]
    detail = client.get("/api/errors/403").json()
    assert "Cloudflare" in detail["name"] or "cloudflare" in detail["symptoms"].lower()


def test_flows_crud(client):
    created = client.post("/api/flows", json={"name": "incident-gpu", "data": {"nodes": []}})
    assert created.status_code == 201
    fid = created.json()["id"]
    flows = client.get("/api/flows").json()
    assert any(f["id"] == fid and f["name"] == "incident-gpu" for f in flows)
    assert client.delete(f"/api/flows/{fid}").status_code == 200
    assert client.delete(f"/api/flows/{fid}").status_code == 404


def test_ticket_not_found(client):
    assert client.get("/api/tickets/99999").status_code == 404


def test_kb_reload(client):
    resp = client.post("/api/kb/reload")
    assert resp.status_code == 200
    body = resp.json()
    assert body["status"] == "ok"
    assert body["chunks"] > 0