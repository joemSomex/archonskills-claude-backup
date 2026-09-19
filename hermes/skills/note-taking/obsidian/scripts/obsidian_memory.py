#!/usr/bin/env python3
"""Store and retrieve durable Markdown notes in an Obsidian vault."""

from __future__ import annotations

import argparse
import json
import os
import re
import tempfile
import unicodedata
from datetime import datetime, timezone
from pathlib import Path


def vault_path(value: str | None) -> Path:
    configured = value or os.environ.get("OBSIDIAN_VAULT_PATH")
    return Path(configured or "~/Documents/Obsidian Vault").expanduser().resolve()


def memory_path(vault: Path) -> Path:
    path = vault / "Memory"
    path.mkdir(parents=True, exist_ok=True)
    return path.resolve()


def slugify(title: str) -> str:
    normalized = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", normalized).strip("-").lower()
    return slug[:80] or "note"


def unique_note_path(folder: Path, title: str) -> Path:
    base = slugify(title)
    candidate = folder / f"{base}.md"
    suffix = 2
    while candidate.exists():
        candidate = folder / f"{base}-{suffix}.md"
        suffix += 1
    return candidate


def yaml_scalar(value: str) -> str:
    reserved = {"null", "true", "false", "yes", "no", "on", "off", "~"}
    is_plain = (
        bool(re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9 _./-]*", value))
        and value.casefold() not in reserved
    )
    return value if is_plain else json.dumps(value, ensure_ascii=False)


def atomic_write(path: Path, content: str) -> None:
    descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(content)
        os.replace(temporary, path)
    except BaseException:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def save_note(vault: Path, title: str, content: str, source: str) -> dict[str, str]:
    title = title.strip()
    content = content.strip()
    if not title:
        raise ValueError("title must not be empty")
    if not content:
        raise ValueError("content must not be empty")

    folder = memory_path(vault)
    path = unique_note_path(folder, title)
    created = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    markdown = (
        "---\n"
        f"title: {yaml_scalar(title)}\n"
        f"created: {json.dumps(created)}\n"
        f"source: {yaml_scalar(source.strip() or 'unspecified')}\n"
        "tags: [memory]\n"
        "---\n\n"
        f"# {title}\n\n{content}\n"
    )
    atomic_write(path, markdown)
    return {"path": path.relative_to(vault).as_posix(), "title": title, "created": created}


def note_files(vault: Path) -> list[Path]:
    folder = memory_path(vault)
    return sorted(folder.rglob("*.md"))


def make_snippet(text: str, query: str, width: int = 180) -> str:
    flat = re.sub(r"\s+", " ", text).strip()
    index = flat.casefold().find(query.casefold())
    if index < 0:
        return flat[:width]
    start = max(0, index - width // 3)
    end = min(len(flat), start + width)
    prefix = "…" if start else ""
    suffix = "…" if end < len(flat) else ""
    return prefix + flat[start:end] + suffix


def search_notes(vault: Path, query: str) -> dict[str, object]:
    query = query.strip()
    if not query:
        raise ValueError("query must not be empty")
    results = []
    for path in note_files(vault):
        text = path.read_text(encoding="utf-8")
        if query.casefold() in text.casefold():
            results.append(
                {
                    "path": path.relative_to(vault).as_posix(),
                    "snippet": make_snippet(text, query),
                }
            )
    return {"query": query, "count": len(results), "results": results}


STOP_WORDS = {
    "a",
    "about",
    "an",
    "and",
    "did",
    "for",
    "in",
    "is",
    "of",
    "on",
    "our",
    "the",
    "to",
    "we",
    "what",
    "which",
}


def query_terms(query: str) -> list[str]:
    terms = re.findall(r"[A-Za-z0-9]+", query.casefold())
    return list(dict.fromkeys(term for term in terms if len(term) > 1 and term not in STOP_WORDS))


def recall_notes(vault: Path, query: str, limit: int) -> dict[str, object]:
    terms = query_terms(query)
    if not terms:
        raise ValueError("query must contain a meaningful search term")
    if limit < 1:
        raise ValueError("limit must be at least 1")

    ranked = []
    for path in note_files(vault):
        text = path.read_text(encoding="utf-8")
        folded_text = text.casefold()
        folded_name = path.stem.casefold()
        score = sum(folded_text.count(term) for term in terms)
        score += 3 * sum(folded_name.count(term) for term in terms)
        if query.casefold() in folded_text:
            score += 10
        if score:
            snippet_term = next((term for term in terms if term in folded_text), terms[0])
            ranked.append(
                {
                    "path": path.relative_to(vault).as_posix(),
                    "score": score,
                    "snippet": make_snippet(text, snippet_term),
                }
            )
    ranked.sort(key=lambda item: (-item["score"], item["path"]))
    results = ranked[:limit]
    return {"query": query, "count": len(results), "results": results}


def resolve_note(vault: Path, requested: str) -> Path:
    folder = memory_path(vault)
    relative = Path(requested)
    if relative.parts and relative.parts[0] == "Memory":
        relative = Path(*relative.parts[1:])
    candidate = (folder / relative).resolve()
    try:
        candidate.relative_to(folder)
    except ValueError as exc:
        raise ValueError("note path must stay inside the Memory folder") from exc
    if not candidate.is_file():
        raise ValueError(f"note not found: {requested}")
    return candidate


def get_note(vault: Path, requested: str) -> dict[str, str]:
    path = resolve_note(vault, requested)
    return {
        "path": path.relative_to(vault).as_posix(),
        "content": path.read_text(encoding="utf-8"),
    }


def recent_notes(vault: Path, limit: int) -> dict[str, object]:
    files = sorted(note_files(vault), key=lambda item: item.stat().st_mtime, reverse=True)
    results = [
        {
            "path": path.relative_to(vault).as_posix(),
            "modified": datetime.fromtimestamp(path.stat().st_mtime, timezone.utc)
            .replace(microsecond=0)
            .isoformat(),
        }
        for path in files[:limit]
    ]
    return {"count": len(results), "results": results}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", help="Obsidian vault path; defaults to OBSIDIAN_VAULT_PATH")
    commands = parser.add_subparsers(dest="command", required=True)

    save = commands.add_parser("save", help="save a durable memory note")
    save.add_argument("title")
    save.add_argument("content")
    save.add_argument("--source", default="user request")

    search = commands.add_parser("search", help="search memory note contents")
    search.add_argument("query")

    recall = commands.add_parser("recall", help="rank memory notes for a natural-language query")
    recall.add_argument("query")
    recall.add_argument("--limit", type=int, default=5)

    get = commands.add_parser("get", help="read one memory note")
    get.add_argument("path")

    recent = commands.add_parser("recent", help="list recently modified memory notes")
    recent.add_argument("--limit", type=int, default=10)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    vault = vault_path(args.vault)
    try:
        if args.command == "save":
            result = save_note(vault, args.title, args.content, args.source)
        elif args.command == "search":
            result = search_notes(vault, args.query)
        elif args.command == "recall":
            result = recall_notes(vault, args.query, args.limit)
        elif args.command == "get":
            result = get_note(vault, args.path)
        else:
            if args.limit < 1:
                raise ValueError("limit must be at least 1")
            result = recent_notes(vault, args.limit)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
