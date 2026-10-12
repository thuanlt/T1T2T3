"""FPT AI Factory Support Agent — FastAPI app."""
from __future__ import annotations

import logging
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from . import db, indexer
from .config import get_settings
from .errors import ERROR_REGISTRY, SERVICE_ERRORS, get_error
from .llm import LLMClient
from .rag import answer_question
from .registry import (
    AGENT_REGISTRY,
    SERVICE_CATEGORIES,
    SERVICE_REGISTRY,
    SERVICE_TO_AGENT,
    get_agent,
)
from .retrieval import Chunk, HybridRetriever, chunk_text
from .tickets import (
    L3_ASSIGNEE_MAP,
    Ticket,
    create_ticket,
    get_ticket,
    list_tickets,
    update_ticket,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
logger = logging.getLogger(__name__)

STATIC_DIR = Path(__file__).resolve().parent.parent / "static"


class ChatRequest(BaseModel):
    question: str = Field(min_length=1, max_length=4000)
    session_id: str | None = None
    image_url: str | None = None
    image_data: str | None = Field(default=None, max_length=8_000_000)
    model: str | None = None
    agent: str | None = None


class TicketCreate(BaseModel):
    subject: str = Field(min_length=1, max_length=500)
    description: str = Field(min_length=1, max_length=8000)
    transcript: list[dict] = []
    level: str = "L2"
    assignee: str = ""


class TicketUpdate(BaseModel):
    status: str | None = None
    resolution: str | None = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    llm = LLMClient(
        api_key=settings.llm_api_key,
        base_url=settings.llm_base_url,
        chat_model=settings.llm_chat_model,
        embed_model=settings.llm_embed_model,
        timeout=settings.llm_timeout,
        verify_ssl=settings.llm_verify_ssl,
    )
    chunks, loaded = indexer.build_retriever(settings)
    if not loaded:
        stats = indexer.ingest(settings, llm)
        chunks = indexer.build_retriever(settings)[0]
        logger.info("KB rỗng, đã ingest: %s", stats)
    retriever = HybridRetriever(chunks)
    logger.info(
        "Khởi động: %d chunks, vector=%s, LLM=%s",
        len(chunks),
        retriever.has_vector,
        llm.available,
    )
    app.state.settings = settings
    app.state.llm = llm
    app.state.retriever = retriever
    yield
    llm.close()


app = FastAPI(title="FPT AI Factory Support Agent", version="1.0.0", lifespan=lifespan)


@app.get("/api/health")
def health() -> dict:
    s = app.state.settings
    r = app.state.retriever
    return {
        "status": "ok",
        "chunks": len(r.chunks),
        "vector_indexed": r.has_vector,
        "llm_available": app.state.llm.available,
        "mode": "llm" if app.state.llm.available else "keyword",
    }


@app.post("/api/chat")
def chat(req: ChatRequest) -> dict:
    agent = get_agent(req.agent) if req.agent else None
    answer = answer_question(
        req.question,
        app.state.retriever,
        app.state.llm,
        app.state.settings,
        image_url=req.image_url,
        image_data=req.image_data,
        model=req.model,
        agent_system=agent["system"] if agent else None,
    )
    return {
        "question": req.question,
        "session_id": req.session_id,
        "answer": answer.text,
        "mode": answer.mode,
        "confidence": answer.confidence,
        "sources": answer.sources,
        "escalate_suggested": answer.escalate_suggested,
        "route": answer.route,
        "agent": agent["name"] if agent else None,
    }


@app.get("/api/models")
def models_list() -> dict:
    s = app.state.settings
    return {
        "chat": s.llm_chat_model,
        "embed": s.llm_embed_model,
        "router": s.llm_router_model or s.llm_chat_model,
        "image": s.llm_image_model or None,
        "vision": s.llm_vision_model or None,
        "llm_available": app.state.llm.available,
    }


@app.post("/api/tickets", status_code=201)
def create_ticket_endpoint(req: TicketCreate) -> dict:
    try:
        ticket = create_ticket(
            app.state.settings.db_path,
            Ticket(
                subject=req.subject,
                description=req.description,
                transcript=req.transcript,
                level=req.level,
                assignee=req.assignee,
            ),
        )
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    return ticket.to_dict()


@app.get("/api/tickets")
def tickets_list() -> list[dict]:
    return list_tickets(app.state.settings.db_path)


@app.get("/api/tickets/assignees")
def ticket_assignees() -> dict:
    return {
        "assignees": [
            {"service": svc, "name": name} for svc, name in L3_ASSIGNEE_MAP.items()
        ]
    }


@app.get("/api/tickets/audit")
def tickets_audit() -> dict:
    return {"events": db.list_audit(app.state.settings.db_path, limit=200)}


@app.get("/api/tickets/{ticket_id}")
def ticket_detail(ticket_id: int) -> dict:
    t = get_ticket(app.state.settings.db_path, ticket_id)
    if t is None:
        raise HTTPException(status_code=404, detail="Ticket không tồn tại")
    return t


@app.patch("/api/tickets/{ticket_id}")
def ticket_update(ticket_id: int, req: TicketUpdate) -> dict:
    try:
        ok = update_ticket(
            app.state.settings.db_path,
            ticket_id,
            status=req.status,
            resolution=req.resolution,
        )
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    if not ok:
        raise HTTPException(status_code=404, detail="Ticket không tồn tại")
    t = get_ticket(app.state.settings.db_path, ticket_id)
    assert t is not None
    return t


@app.post("/api/kb/reload")
def kb_reload() -> dict:
    stats = indexer.ingest(app.state.settings, app.state.llm)
    chunks = indexer.build_retriever(app.state.settings)[0]
    app.state.retriever = HybridRetriever(chunks)
    return {"status": "ok", **stats, "vector_indexed": app.state.retriever.has_vector}


@app.get("/api/services")
def services_list() -> dict:
    return {
        "categories": SERVICE_CATEGORIES,
        "services": SERVICE_REGISTRY,
        "service_to_agent": SERVICE_TO_AGENT,
    }


@app.get("/api/errors")
def errors_list() -> dict:
    return {
        "errors": ERROR_REGISTRY,
        "service_errors": SERVICE_ERRORS,
    }


@app.get("/api/errors/{code}")
def error_detail(code: str) -> dict:
    e = get_error(code)
    if e is None:
        raise HTTPException(status_code=404, detail="Lỗi không tồn tại")
    return e


class FlowCreate(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    data: dict = {}


@app.get("/api/flows")
def flows_list() -> list[dict]:
    return db.list_flows(app.state.settings.db_path)


@app.post("/api/flows", status_code=201)
def flow_create(req: FlowCreate) -> dict:
    import json as _json

    fid = db.insert_flow(app.state.settings.db_path, req.name, _json.dumps(req.data, ensure_ascii=False))
    return {"id": fid, "name": req.name, "data": req.data}


@app.delete("/api/flows/{flow_id}")
def flow_delete(flow_id: int) -> dict:
    if not db.delete_flow(app.state.settings.db_path, flow_id):
        raise HTTPException(status_code=404, detail="Flow không tồn tại")
    return {"status": "ok"}


@app.get("/api/agents")
def agents_list() -> dict:
    return {"agents": AGENT_REGISTRY}


@app.get("/api/kb/docs")
def kb_docs() -> dict:
    root = Path(app.state.settings.kb_dir)
    docs = []
    for path in sorted(root.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        title = text.splitlines()[0].lstrip("#").strip() if text.splitlines() else path.stem
        n_chunks = len(chunk_text(text, max_chars=app.state.settings.chunk_size, overlap=app.state.settings.chunk_overlap))
        rel = str(path.relative_to(root))
        docs.append({
            "path": rel,
            "title": title,
            "category": path.parent.name if path.parent != root else "",
            "size": len(text),
            "chunks": n_chunks,
        })
    return {"docs": docs}


@app.get("/api/kb/docs/{doc_path:path}")
def kb_doc_get(doc_path: str) -> dict:
    root = Path(app.state.settings.kb_dir).resolve()
    target = (root / doc_path).resolve()
    if not target.is_file() or root not in target.parents:
        raise HTTPException(status_code=404, detail="Tài liệu không tồn tại")
    return {"path": doc_path, "content": target.read_text(encoding="utf-8")}


class DocUpdate(BaseModel):
    content: str = Field(max_length=200_000)


@app.put("/api/kb/docs/{doc_path:path}")
def kb_doc_put(doc_path: str, req: DocUpdate) -> dict:
    root = Path(app.state.settings.kb_dir).resolve()
    target = (root / doc_path).resolve()
    if root not in target.parents:
        raise HTTPException(status_code=422, detail="Đường dẫn không hợp lệ")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(req.content, encoding="utf-8")
    return {"status": "ok", "path": doc_path}


@app.get("/")
def index() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")


app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")