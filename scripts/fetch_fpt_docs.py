#!/usr/bin/env python3
"""Crawl FPT Cloud docs categories (fpt-ai-factory, ai-infrastructure) -> markdown KB.

Cách dùng:
  python scripts/fetch_fpt_docs.py --dry-run   # liệt kê URL sẽ tải
  python scripts/fetch_fpt_docs.py             # tải toàn bộ
"""
from __future__ import annotations

import argparse
import re
import sys
import time
from pathlib import Path

import httpx
from bs4 import BeautifulSoup
from html2text import HTML2Text

BASE = "https://docs.fptcloud.com"
OUT = Path(__file__).resolve().parent.parent / "kb" / "guides"
PREFIXES = ("/docs/fpt-ai-factory/", "/docs/ai-infrastructure/")
SEED = [
    f"{BASE}/docs/category/fpt-ai-factory/",
    f"{BASE}/docs/category/ai-infrastructure/",
]

H = HTML2Text()
H.body_width = 0
H.ignore_images = True
H.ignore_links = True
H.unicode_snob = True
H.single_line_break = False

_client = httpx.Client(timeout=60, follow_redirects=True)


def fetch(url: str) -> str:
    r = _client.get(url)
    r.raise_for_status()
    return r.text


def discover(html: str) -> tuple[set[str], set[str]]:
    """Trả về (article_urls, category_urls) trong cây sidebar của 2 category.

    Docusaurus render các mục sau của menu lồng vào <li> của mục đang mở rộng,
    nên phải lọc link theo prefix URL của từng tree.
    """
    TREES = {
        "FPT AI Factory": "/docs/fpt-ai-factory/",
        "AI Infrastructure": "/docs/ai-infrastructure/",
    }
    soup = BeautifulSoup(html, "html.parser")
    arts: set[str] = set()
    cats: set[str] = set()
    for li in soup.select("nav.menu li.menu__list-item, aside.theme-doc-sidebar-container li.menu__list-item"):
        a = li.find("a", href=True)
        if a is None:
            continue
        prefix = TREES.get(a.get_text(strip=True))
        if prefix is None:
            continue
        for link in li.find_all("a", href=True):
            href = str(link["href"]).split("#")[0]
            if not href.startswith("/docs/"):
                continue
            if not href.endswith("/"):
                href += "/"
            if "/category/" in href:
                cats.add(href)
            elif href.startswith(prefix):
                arts.add(href)
    return arts, cats


def extract_article(html: str) -> tuple[str, str]:
    soup = BeautifulSoup(html, "html.parser")
    art = soup.find("article")
    if art is None:
        raise RuntimeError("Không tìm thấy <article>")
    h1 = art.find("h1")
    title = h1.get_text(strip=True) if h1 else "Untitled"
    for tag in art.select(
        "script, style, nav, .theme-doc-footer, .pagination-nav, .tocCollapsible, "
        ".theme-doc-toc-desktop, .theme-doc-toc-mobile, .table-of-contents"
    ):
        tag.decompose()
    md = H.handle(str(art))
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    md = re.sub(r"(?im)^On this page\s*$", "", md)
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    return title, md


def rel_path(href: str) -> str:
    """/docs/fpt-ai-factory/a/b/ -> fpt-ai-factory/a/b"""
    return href[len("/docs/") :].rstrip("/")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    arts: set[str] = set()
    cats: set[str] = set()
    for seed in SEED:
        try:
            a, c = discover(fetch(seed))
            arts |= a
            cats |= c
        except Exception as exc:
            print(f"FAIL seed {seed}: {exc}")

    # BFS qua category VÀ article: mỗi trang mở rộng category của nó trong sidebar,
    # nên duyệt thêm article để lộ các subcategory đang thu gọn (VD Settings/Billing).
    queue = list(cats) + list(arts)
    seen: set[str] = set()
    while queue:
        url = queue.pop(0)
        if url in seen:
            continue
        seen.add(url)
        try:
            a, c = discover(fetch(BASE + url))
        except Exception as exc:
            print(f"FAIL {url}: {exc}")
            continue
        new_arts = a - arts
        if new_arts:
            print(f"+{len(new_arts)} bài từ {url}")
        arts |= a
        cats |= c
        for cu in c - seen:
            queue.append(cu)
        for au in a - seen:
            queue.append(au)
        time.sleep(0.15)

    sorted_arts = sorted(arts)
    print(f"\nTổng cộng {len(sorted_arts)} bài viết.")
    if args.dry_run:
        for u in sorted_arts:
            print(" ", u)
        return 0

    ok = fail = 0
    for href in sorted_arts:
        url = BASE + href
        rel = rel_path(href)
        dest = OUT / f"{rel}.md"
        try:
            title, md = extract_article(fetch(url))
        except Exception as exc:
            print(f"FAIL {rel}: {exc}")
            fail += 1
            continue
        md = f"# {title} (FPT Cloud docs)\n\n> Nguồn: {url}\n\n" + md
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(md + "\n", encoding="utf-8")
        ok += 1
        time.sleep(0.15)
    print(f"Xong: {ok} OK, {fail} lỗi. Lưu tại {OUT}")
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())