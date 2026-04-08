"""
Migrate notes from Silva (Astro) into Scholion (Hugo).

- Reads E:/silva/src/content/note/**/*.md
- Parses YAML frontmatter
- Extracts sources from `Fonte:` / `Fontes:` lines
- Heuristic for has_commentary
- Generates summary
- Writes to E:/scholion/content/notes/<slug>.md (or page bundle if image present)

Idempotent: skips files already present in scholion (so it can be run repeatedly
during the parallel-edit period; manually-curated notes are preserved).

Usage:
    python scripts/migrate_from_silvae.py            # dry run, prints summary
    python scripts/migrate_from_silvae.py --write    # actually write files
    python scripts/migrate_from_silvae.py --write --force   # overwrite existing
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

import yaml

SILVA_NOTES = Path("E:/silva/src/content/note")
SCHOLION_NOTES = Path("E:/scholion/content/notes")

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def detect_kind(url: str) -> str:
    u = url.lower()
    if "wikipedia.org" in u:
        return "wiki"
    if "arxiv.org" in u or u.endswith(".pdf"):
        return "paper"
    if "youtube.com" in u or "youtu.be" in u:
        return "video"
    if "vox.thluiz.com" in u:
        return "podcast"
    if "github.com" in u:
        return "repo"
    if "poetryfoundation" in u or "poets.org" in u:
        return "poem"
    return "article"


def parse_sources(line: str) -> list[dict]:
    """Parse a 'Fonte:' or 'Fontes:' line into structured sources."""
    # strip the leading "Fonte:"/"Fontes:" and trailing whitespace
    body = re.sub(r"^Fontes?:\s*", "", line.strip(), flags=re.IGNORECASE)
    # split multiple sources by " · " (middle dot, the silvae convention)
    parts = [p.strip() for p in body.split(" · ") if p.strip()]
    sources = []
    for part in parts:
        m = LINK_RE.search(part)
        if m:
            title, url = m.group(1), m.group(2)
            src = {"title": title.strip(), "url": url.strip(), "kind": detect_kind(url)}
        else:
            # plain-text source: keep as title only
            src = {"title": part, "kind": "other"}
        sources.append(src)
    return sources


def extract_sources_and_strip(body: str) -> tuple[list[dict], str]:
    """Find Fonte(s) lines at the end of body, return (sources, body_without_them)."""
    lines = body.rstrip().split("\n")
    sources = []
    while lines and (
        lines[-1].strip().lower().startswith("fonte:")
        or lines[-1].strip().lower().startswith("fontes:")
    ):
        sources = parse_sources(lines[-1]) + sources
        lines.pop()
        # also pop any blank line immediately above
        while lines and not lines[-1].strip():
            lines.pop()
    return sources, "\n".join(lines).rstrip() + "\n"


def word_count_excluding_quotes(body: str) -> int:
    """Count words in body, excluding lines that start with '>' (blockquotes)."""
    words = 0
    for line in body.splitlines():
        if line.lstrip().startswith(">"):
            continue
        words += len(line.split())
    return words


def detect_has_commentary(body: str) -> bool:
    """Heuristic: notes with substantial non-quote text get marked as commentary."""
    return word_count_excluding_quotes(body) > 120


def generate_summary(body: str, max_len: int = 200) -> str:
    """First non-quote, non-heading sentence/paragraph of the body."""
    paragraphs = []
    current = []
    for line in body.splitlines():
        s = line.strip()
        if not s:
            if current:
                paragraphs.append(" ".join(current))
                current = []
            continue
        if s.startswith(">") or s.startswith("#") or s.startswith("!["):
            if current:
                paragraphs.append(" ".join(current))
                current = []
            continue
        current.append(s)
    if current:
        paragraphs.append(" ".join(current))

    if not paragraphs:
        return ""

    text = paragraphs[0]
    # collapse markdown emphasis markers, links → keep text only
    text = LINK_RE.sub(r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)

    if len(text) <= max_len:
        return text
    # truncate at a word boundary near max_len
    cut = text[:max_len].rsplit(" ", 1)[0]
    return cut + "…"


def parse_silva_note(path: Path) -> dict | None:
    raw = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(raw)
    if not m:
        print(f"  ! no frontmatter: {path}", file=sys.stderr)
        return None
    fm_text, body = m.group(1), m.group(2)
    fm = yaml.safe_load(fm_text) or {}

    sources, body_clean = extract_sources_and_strip(body)
    has_commentary = detect_has_commentary(body_clean)
    summary = generate_summary(body_clean)

    return {
        "path": path,
        "title": fm.get("title", path.stem),
        "date": fm.get("publishDate"),
        "tags": fm.get("tags", []),
        "summary": summary,
        "has_commentary": has_commentary,
        "sources": sources,
        "body": body_clean,
    }


def yaml_dump(data: dict) -> str:
    """Dump frontmatter with consistent ordering and double-quoted strings where needed."""
    # Use custom ordering for readability
    ordered = {}
    for k in ("title", "date", "summary", "tags", "has_commentary", "sources"):
        if k in data:
            ordered[k] = data[k]
    return yaml.dump(
        ordered,
        sort_keys=False,
        allow_unicode=True,
        default_flow_style=False,
        width=10000,
    )


def render_note(parsed: dict) -> str:
    fm = {
        "title": parsed["title"],
        "date": parsed["date"],
        "summary": parsed["summary"],
        "tags": parsed["tags"] or [],
        "has_commentary": parsed["has_commentary"],
        "sources": parsed["sources"],
    }
    return f"---\n{yaml_dump(fm)}---\n\n{parsed['body'].lstrip()}"


def slug_from_silva_path(path: Path) -> str:
    """Return scholion-friendly slug. Page bundles use parent dir name."""
    if path.name == "index.md":
        return path.parent.name
    return path.stem


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true", help="actually write files")
    ap.add_argument("--force", action="store_true", help="overwrite existing files")
    args = ap.parse_args()

    md_files = sorted(SILVA_NOTES.rglob("*.md"))
    print(f"Found {len(md_files)} silvae notes")

    SCHOLION_NOTES.mkdir(parents=True, exist_ok=True)

    stats = {
        "total": 0,
        "skipped_existing": 0,
        "with_commentary": 0,
        "gloss": 0,
        "no_sources": 0,
        "page_bundles": 0,
        "written": 0,
    }

    for src in md_files:
        parsed = parse_silva_note(src)
        if not parsed:
            continue
        stats["total"] += 1

        slug = slug_from_silva_path(src)
        is_bundle = src.name == "index.md"
        if is_bundle:
            stats["page_bundles"] += 1

        if parsed["has_commentary"]:
            stats["with_commentary"] += 1
        else:
            stats["gloss"] += 1
        if not parsed["sources"]:
            stats["no_sources"] += 1

        # determine output path
        if is_bundle:
            out_dir = SCHOLION_NOTES / slug
            out_path = out_dir / "index.md"
        else:
            out_path = SCHOLION_NOTES / f"{slug}.md"

        if out_path.exists() and not args.force:
            stats["skipped_existing"] += 1
            continue

        if args.write:
            if is_bundle:
                out_dir.mkdir(parents=True, exist_ok=True)
                # copy any sibling assets (images, etc.)
                for asset in src.parent.iterdir():
                    if asset.name == "index.md":
                        continue
                    shutil.copy2(asset, out_dir / asset.name)
            out_path.write_text(render_note(parsed), encoding="utf-8")
            stats["written"] += 1

    print()
    print("Summary:")
    for k, v in stats.items():
        print(f"  {k:20s} {v}")
    if not args.write:
        print()
        print("(dry run — pass --write to actually create files)")


if __name__ == "__main__":
    main()
