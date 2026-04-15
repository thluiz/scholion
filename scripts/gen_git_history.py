#!/usr/bin/env python3
"""Generate per-note git history JSON files for Hugo data templates."""

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIRS = [ROOT / "content" / "notes", ROOT / "content" / "research"]
CONTENT_PREFIXES = [("content", "notes"), ("content", "research")]
OUT_DIR = ROOT / "data" / "git_history"


def git_log(filepath: Path, n: int = 3) -> list[dict]:
    result = subprocess.run(
        ["git", "log", f"-{n}", "--format=%ai|||%s", "--follow", "--", str(filepath)],
        capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=ROOT,
    )
    entries = []
    for line in result.stdout.strip().splitlines():
        if "|||" not in line:
            continue
        date, subject = line.split("|||", 1)
        entries.append({"date": date.split(" ")[0], "subject": subject})
    return entries


def note_slug(note: Path) -> str:
    """Extract slug: for page bundles (dir/index.md) use dir name, else file stem."""
    if note.name == "index.md":
        return note.parent.name.replace("-", "_")
    return note.stem.replace("-", "_")


def process(note: Path):
    slug = note_slug(note)
    history = git_log(note)
    if not history:
        return
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / f"{slug}.json").write_text(
        json.dumps(history, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def main():
    if "--all" in sys.argv:
        notes = []
        for d in CONTENT_DIRS:
            if d.exists():
                # Regular notes (slug.md)
                notes.extend(n for n in sorted(d.glob("*.md")) if n.name != "_index.md")
                # Page bundles (slug/index.md)
                notes.extend(n for n in sorted(d.glob("*/index.md")))
        for note in notes:
            process(note)
        print(f"Generated history for {len(notes)} notes.")
    elif "--staged" in sys.argv:
        result = subprocess.run(
            ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"],
            capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=ROOT,
        )
        count = 0
        for line in result.stdout.strip().splitlines():
            p = Path(line)
            if p.parts[:2] in CONTENT_PREFIXES and p.suffix == ".md" and p.name != "_index.md":
                process(ROOT / p)
                count += 1
        if count:
            print(f"Updated history for {count} staged note(s).")
    else:
        print("Usage: gen_git_history.py --all | --staged", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
