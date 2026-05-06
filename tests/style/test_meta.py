"""Checks meta — encoding, frontmatter, datas.

Estes não são sobre estilo do texto, mas sobre integridade do arquivo
(Hugo 404 em data futura; cp1252 quebra UTF-8; frontmatter mínimo).
"""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import pytest
import yaml

from conftest import NOTES_DIR, Note


# ---------- 1. UTF-8 limpo ----------

def test_utf8_decodable(note: Note):
    """Se o arquivo não decodifica como UTF-8, conftest._load_note não cria
    o Note. Esta checagem percorre os arquivos brutos.
    """
    raw_bytes = note.path.read_bytes()
    try:
        raw_bytes.decode("utf-8")
    except UnicodeDecodeError as e:
        pytest.fail(
            f"\n[encoding] {note.relpath}: não decodifica como UTF-8 — {e}\n"
            f"  provavelmente cp1252; rodar com PYTHONIOENCODING=utf-8 e re-salvar.",
            pytrace=False,
        )


def test_no_orphan_cp1252_chars():
    """Pega arquivos que tools Windows produziram com cp1252 e não foram
    detectados acima (raros — geralmente o arquivo todo decodifica falsamente).
    """
    suspects = []
    for md in NOTES_DIR.rglob("*.md"):
        if md.name == "_index.md":
            continue
        try:
            md.read_bytes().decode("utf-8")
        except UnicodeDecodeError:
            suspects.append(str(md.relative_to(NOTES_DIR.parent.parent)))
    if suspects:
        pytest.fail(
            "\n[encoding] arquivo(s) não-UTF-8:\n  " + "\n  ".join(suspects),
            pytrace=False,
        )


# ---------- 2. Frontmatter mínimo ----------

REQUIRED_FIELDS = {"title", "date", "summary", "tags", "has_commentary", "sources"}


def test_frontmatter_required_fields(note: Note):
    fm = note.frontmatter
    if not fm:
        pytest.fail(f"\n[frontmatter] {note.relpath}: sem frontmatter YAML",
                    pytrace=False)
    missing = REQUIRED_FIELDS - set(fm.keys())
    if missing:
        pytest.fail(
            f"\n[frontmatter] {note.relpath}: faltam campos {sorted(missing)}",
            pytrace=False,
        )


def test_frontmatter_types(note: Note):
    fm = note.frontmatter
    if not fm:
        pytest.skip("sem frontmatter — outro teste pega")

    issues = []
    if "tags" in fm and not isinstance(fm["tags"], list):
        issues.append(f"tags deve ser lista, é {type(fm['tags']).__name__}")
    if "sources" in fm and not isinstance(fm["sources"], list):
        issues.append(f"sources deve ser lista, é {type(fm['sources']).__name__}")
    if "has_commentary" in fm and not isinstance(fm["has_commentary"], bool):
        issues.append(
            f"has_commentary deve ser bool, é {type(fm['has_commentary']).__name__}"
        )
    if issues:
        pytest.fail(
            f"\n[frontmatter] {note.relpath}: " + "; ".join(issues),
            pytrace=False,
        )


# ---------- 3. Data não no futuro ----------

def _parse_date(raw) -> datetime | None:
    if isinstance(raw, datetime):
        # PyYAML pode retornar datetime naive — assumir UTC pra comparar
        if raw.tzinfo is None:
            return raw.replace(tzinfo=timezone.utc)
        return raw
    if isinstance(raw, str):
        # Hugo aceita várias formas; tentar ISO 8601
        try:
            s = raw.replace("Z", "+00:00")
            return datetime.fromisoformat(s)
        except ValueError:
            return None
    return None


def test_date_not_in_future(note: Note):
    fm = note.frontmatter
    if "date" not in fm:
        pytest.skip("sem campo date — outro teste pega")
    dt = _parse_date(fm["date"])
    if dt is None:
        pytest.fail(
            f"\n[date] {note.relpath}: campo 'date' não parseável: {fm['date']!r}",
            pytrace=False,
        )
    now = datetime.now(timezone.utc)
    # Tolerar até 1h de skew (timezone confusion)
    if (dt - now).total_seconds() > 3600:
        pytest.fail(
            f"\n[date] {note.relpath}: data futura ({dt.isoformat()}); "
            f"Hugo gera 404 em produção. Use `date +'%Y-%m-%dT%H:%M:%S%:z'`.",
            pytrace=False,
        )
