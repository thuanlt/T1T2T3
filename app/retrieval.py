"""Retrieval: chunk KB, vector search (cosine) + keyword search (TF-IDF), hybrid."""
from __future__ import annotations

import math
import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np

_WORD_RE = re.compile(r"[a-z0-9]+")

VIETNAMESE_STOPWORDS = {
    "va", "cua", "cho", "voi", "duoc", "khi", "neu", "cac", "mot", "nhung",
    "nay", "do", "day", "co", "khong", "la", "thi", "ma", "de", "nhu",
    "cung", "da", "dang", "se", "deu", "vao", "ra", "len", "xuong", "o",
    "tai", "tu", "theo", "ve", "trong", "ngoai", "tren", "duoi", "cung",
    "hay", "hoac", "nhung", "vi", "nen", "do", "boi", "them", "lam", "sao",
    "nao", "gi", "ai", "dau", "vay", "thoi", "toi", "ban", "anh", "chi",
    "em", "minh", "ta", "chung", "hom", "ngay", "thang", "nam", "gio", "phut",
    "bao", "bi", "duoc", "rat", "hon", "kem", "qua", "lan", "luot", "ca",
    "xin", "moi", "gui", "den", "lai", "di", "den", "tu", "bang", "viet",
    "the", "a", "an", "and", "or", "of", "to", "in", "on", "for", "with",
    "is", "are", "was", "be", "by", "at", "as", "it", "this", "that",
    "you", "your", "we", "our", "how", "what", "when", "where", "why",
    "can", "could", "will", "would", "should", "please", "help", "need",
    "want", "get", "use", "used", "using", "do", "does", "did", "have",
    "has", "had", "not", "no", "yes", "ok", "hello", "hi", "thanks",
}


def normalize(text: str) -> str:
    """Lowercase + bỏ dấu tiếng Việt + giữ token alnum."""
    text = unicodedata.normalize("NFD", text.lower())
    text = "".join(ch for ch in text if unicodedata.category(ch) != "Mn")
    return " ".join(_WORD_RE.findall(text))


def tokenize(text: str) -> list[str]:
    return [t for t in normalize(text).split() if t not in VIETNAMESE_STOPWORDS]


@dataclass
class Chunk:
    doc_path: str
    doc_title: str
    category: str
    content: str
    embedding: list[float] | None = None


@dataclass
class Hit:
    doc_path: str
    doc_title: str
    category: str
    content: str
    score: float
    mode: str


def _split_long(text: str, max_chars: int) -> list[str]:
    parts: list[str] = []
    lines = text.split("\n")
    segments: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("|") and line.endswith("|"):
            block = [line]
            j = i + 1
            while j < len(lines) and lines[j].strip().startswith("|") and lines[j].strip().endswith("|"):
                block.append(lines[j].strip())
                j += 1
            segments.append("\n".join(block))
            i = j
        else:
            segments.append(line)
            i += 1
    for seg in segments:
        if seg.startswith("|"):
            parts.append(seg)
            continue
        for sent in re.split(r"(?<=[.!?。])\s+", seg):
            sent = sent.strip()
            while len(sent) > max_chars:
                cut = sent.rfind(" ", 0, max_chars)
                cut = cut if cut > max_chars // 2 else max_chars
                parts.append(sent[:cut].strip())
                sent = sent[cut:].strip()
            if sent:
                parts.append(sent)
    return parts


def chunk_text(text: str, max_chars: int = 700, overlap: int = 100) -> list[str]:
    """Chia văn bản thành các đoạn, ưu tiên theo đoạn văn, chồng lấp overlap ký tự."""
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    chunks: list[str] = []
    buf = ""
    for para in paragraphs:
        for piece in _split_long(para, max_chars):
            candidate = (buf + "\n\n" + piece).strip() if buf else piece
            if len(candidate) > max_chars and buf:
                chunks.append(buf)
                tail = buf[-overlap:] if overlap else ""
                buf = (tail + "\n\n" + piece).strip()
            else:
                buf = candidate
    if buf:
        chunks.append(buf)
    return [c for c in chunks if c]


def _doc_title(path: Path, text: str) -> str:
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("#"):
            return line.lstrip("#").strip()
    return path.stem.replace("_", " ").replace("-", " ").title()


def load_kb(kb_dir: str, *, max_chars: int = 700, overlap: int = 100) -> list[Chunk]:
    root = Path(kb_dir)
    if not root.exists():
        return []
    chunks: list[Chunk] = []
    for path in sorted(root.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        title = _doc_title(path, text)
        category = path.parent.name if path.parent != root else ""
        for piece in chunk_text(text, max_chars=max_chars, overlap=overlap):
            chunks.append(
                Chunk(
                    doc_path=str(path),
                    doc_title=title,
                    category=category,
                    content=piece,
                )
            )
    return chunks


class VectorIndex:
    """Cosine similarity trên ma trận embedding."""

    def __init__(self, chunks: list[Chunk]):
        self.chunks = [c for c in chunks if c.embedding is not None]
        if self.chunks:
            mat = np.array([c.embedding for c in self.chunks], dtype=np.float32)
            self._mat = mat / np.linalg.norm(mat, axis=1, keepdims=True)
        else:
            self._mat = np.zeros((0, 0), dtype=np.float32)

    @property
    def empty(self) -> bool:
        return len(self.chunks) == 0

    def search(self, query_vec: list[float], top_k: int) -> list[Hit]:
        if self.empty:
            return []
        q = np.asarray(query_vec, dtype=np.float32)
        q = q / np.linalg.norm(q)
        sims = self._mat @ q
        order = np.argsort(-sims)[:top_k]
        return [
            Hit(
                doc_path=self.chunks[i].doc_path,
                doc_title=self.chunks[i].doc_title,
                category=self.chunks[i].category,
                content=self.chunks[i].content,
                score=float(sims[i]),
                mode="vector",
            )
            for i in order
            if sims[i] > 0
        ]


class KeywordIndex:
    """TF-IDF cosine trên token đã chuẩn hóa (bỏ dấu). Score tuyệt đối trong [0,1]."""

    def __init__(self, chunks: list[Chunk]):
        self.chunks = chunks
        corpus: list[list[str]] = [tokenize(c.content) for c in chunks]
        self._n = len(corpus)
        df: dict[str, int] = {}
        for toks in corpus:
            for t in set(toks):
                df[t] = df.get(t, 0) + 1
        self._idf = {t: math.log((self._n + 1) / (d + 1)) + 1 for t, d in df.items()}
        self._docs: list[dict[str, float]] = []
        for toks in corpus:
            counts: dict[str, float] = {}
            for t in toks:
                counts[t] = counts.get(t, 0) + 1
            vec = {t: c * self._idf.get(t, 1.0) for t, c in counts.items()}
            denom = math.sqrt(sum(v * v for v in vec.values())) or 1.0
            self._docs.append({t: v / denom for t, v in vec.items()})

    @property
    def empty(self) -> bool:
        return self._n == 0

    def search(self, query: str, top_k: int) -> list[Hit]:
        if self.empty:
            return []
        qtoks = tokenize(query)
        if not qtoks:
            return []
        counts: dict[str, float] = {}
        for t in qtoks:
            counts[t] = counts.get(t, 0) + 1
        qvec = {t: c * self._idf.get(t, 1.0) for t, c in counts.items()}
        qnorm = math.sqrt(sum(v * v for v in qvec.values())) or 1.0
        qvec = {t: v / qnorm for t, v in qvec.items()}
        scored: list[tuple[int, float]] = []
        for i, doc in enumerate(self._docs):
            s = sum(v * doc.get(t, 0.0) for t, v in qvec.items())
            if s > 0:
                scored.append((i, s))
        scored.sort(key=lambda x: -x[1])
        return [
            Hit(
                doc_path=self.chunks[i].doc_path,
                doc_title=self.chunks[i].doc_title,
                category=self.chunks[i].category,
                content=self.chunks[i].content,
                score=round(s, 4),
                mode="keyword",
            )
            for i, s in scored[:top_k]
        ]


class HybridRetriever:
    """Kết hợp vector + keyword; fallback keyword khi không có embedding."""

    def __init__(self, chunks: list[Chunk], *, vec_weight: float = 0.6):
        self.chunks = chunks
        self.vector = VectorIndex(chunks)
        self.keyword = KeywordIndex(chunks)
        self.vec_weight = vec_weight

    @property
    def has_vector(self) -> bool:
        return not self.vector.empty

    def search(self, query: str, query_vec: list[float] | None, top_k: int) -> list[Hit]:
        kw_hits = self.keyword.search(query, top_k)
        if query_vec is None or self.vector.empty:
            return kw_hits
        vec_hits = self.vector.search(query_vec, top_k)
        merged: dict[tuple[str, str], Hit] = {}
        for h in vec_hits:
            merged[(h.doc_path, h.content)] = h
        for h in kw_hits:
            key = (h.doc_path, h.content)
            if key in merged:
                merged[key].score = self.vec_weight * merged[key].score + (1 - self.vec_weight) * h.score
                merged[key].mode = "hybrid"
            else:
                merged[key] = h
        hits = sorted(merged.values(), key=lambda h: -h.score)[:top_k]
        return hits