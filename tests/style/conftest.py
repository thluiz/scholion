"""Fixtures e helpers para style-test.

Coleta notas .md em content/notes/ e expõe via parametrize.
Cada teste recebe um (path, frontmatter, body) e roda sua checagem.

Filtro: env var STYLE_TEST_FILTER, vírgula-separada de slugs. Quando setada,
só notas cujo slug está na lista são coletadas. Skill /style-test usa isso
pra rodar só nas N últimas notas modificadas (default 1).
"""
from __future__ import annotations

import os
import re
from dataclasses import dataclass
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
NOTES_DIR = REPO_ROOT / "content" / "notes"

FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n(.*)\Z", re.DOTALL)


@dataclass
class Note:
    path: Path
    relpath: str
    raw: str
    frontmatter: dict
    body: str

    @property
    def slug(self) -> str:
        if self.path.name == "index.md":
            return self.path.parent.name
        return self.path.stem


def _load_note(path: Path) -> Note | None:
    raw = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(raw)
    if not m:
        return Note(path=path, relpath=str(path.relative_to(REPO_ROOT)),
                    raw=raw, frontmatter={}, body=raw)
    fm_text, body = m.group(1), m.group(2)
    try:
        fm = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError:
        fm = {}
    return Note(path=path, relpath=str(path.relative_to(REPO_ROOT)),
                raw=raw, frontmatter=fm, body=body)


def _collect_notes() -> list[Note]:
    filter_raw = os.environ.get("STYLE_TEST_FILTER", "").strip()
    filter_slugs = {s.strip() for s in filter_raw.split(",") if s.strip()} if filter_raw else None

    notes: list[Note] = []
    for md in NOTES_DIR.rglob("*.md"):
        if md.name == "_index.md":
            continue
        # Slug check antes do load — economiza I/O quando o filter é pequeno
        slug = md.parent.name if md.name == "index.md" else md.stem
        if filter_slugs is not None and slug not in filter_slugs:
            continue
        try:
            n = _load_note(md)
        except UnicodeDecodeError:
            continue
        if n is not None:
            notes.append(n)
    return notes


ALL_NOTES = _collect_notes()


def _id(note: Note) -> str:
    return note.slug


def pytest_generate_tests(metafunc):
    if "note" in metafunc.fixturenames:
        metafunc.parametrize("note", ALL_NOTES, ids=[_id(n) for n in ALL_NOTES])


# ---------- helpers ----------

def find_lines(body: str, pattern: re.Pattern[str]) -> list[tuple[int, str, str]]:
    """Return list of (line_number, matched_text, full_line)."""
    hits = []
    for i, line in enumerate(body.splitlines(), start=1):
        for m in pattern.finditer(line):
            hits.append((i, m.group(0), line.strip()))
    return hits


# Strip out content where banned patterns are expected/legitimate:
# - blockquotes (synopsis, citations)
# - inline code, fenced code
# - markdown links (URLs/slugs may contain banned words)
# - HTML tags
def strip_quotes_and_code(body: str) -> str:
    # remove fenced code blocks
    body = re.sub(r"```.*?```", "", body, flags=re.DOTALL)
    # remove inline code
    body = re.sub(r"`[^`]*`", "", body)
    # remove blockquote lines (synopsis, source quotes)
    body = "\n".join(l for l in body.splitlines() if not l.lstrip().startswith(">"))
    # collapse markdown links: keep text, drop URL
    body = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", body)
    # remove HTML tags
    body = re.sub(r"<[^>]+>", "", body)
    return body


def fail_if_hits(note: Note, hits: list[tuple[int, str, str]], rule: str) -> None:
    if not hits:
        return
    lines_summary = "\n".join(
        f"  L{ln}: «{match}» — {snippet[:120]}" for ln, match, snippet in hits[:10]
    )
    extra = f"\n  ...e mais {len(hits) - 10}" if len(hits) > 10 else ""
    pytest.fail(
        f"\n[{rule}] {note.relpath}: {len(hits)} ocorrência(s)\n{lines_summary}{extra}",
        pytrace=False,
    )
