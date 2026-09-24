"""Token benchmark for webclip batch agents.

Reads the Claude Code subagent transcripts of an orchestrator session and
reports token usage per batch agent (only agents whose description starts
with "webclip batch"). Optionally appends new rows to a CSV so batch sizes
can be compared across sessions.

Usage:
    python batch-tokens.py [session-id] [--csv PATH]

Without a session id, uses the most recently modified session of the
E:\\scholion project. The item count per batch is read from the agent
description, which the orchestrator writes as "webclip batch <n> (<items> items)".

Only covers tokens spent by Claude Code itself; the compose calls' own LLM
usage happens server-side (vox-intelligence) and is not in these transcripts.
"""
import csv
import json
import re
import sys
from pathlib import Path

PROJECT_DIR = Path.home() / ".claude" / "projects" / "E--scholion"
FIELDS = ["input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens"]


def agent_usage(jsonl: Path) -> dict:
    # One API message can be split over several transcript lines that repeat
    # the same usage block; keep the last one per message id.
    per_msg = {}
    for line in jsonl.open(encoding="utf-8"):
        d = json.loads(line)
        if d.get("type") != "assistant":
            continue
        msg = d.get("message") or {}
        if msg.get("usage"):
            per_msg[msg.get("id")] = msg["usage"]
    totals = {f: 0 for f in FIELDS}
    totals["thinking_tokens"] = 0
    for u in per_msg.values():
        for f in FIELDS:
            totals[f] += u.get(f) or 0
        totals["thinking_tokens"] += (u.get("output_tokens_details") or {}).get("thinking_tokens") or 0
    totals["turns"] = len(per_msg)
    return totals


def main():
    args = sys.argv[1:]
    csv_path = None
    if "--csv" in args:
        i = args.index("--csv")
        csv_path = Path(args[i + 1])
        del args[i : i + 2]
    if args:
        session = args[0]
    else:
        session = max(PROJECT_DIR.glob("*.jsonl"), key=lambda p: p.stat().st_mtime).stem
    sub_dir = PROJECT_DIR / session / "subagents"
    if not sub_dir.is_dir():
        sys.exit(f"no subagents folder for session {session}")

    rows = []
    for meta_path in sorted(sub_dir.glob("*.meta.json"), key=lambda p: p.stat().st_mtime):
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        desc = meta.get("description") or ""
        if not desc.lower().startswith("webclip batch"):
            continue
        agent_id = meta_path.name.removesuffix(".meta.json")
        u = agent_usage(sub_dir / f"{agent_id}.jsonl")
        m = re.search(r"\((\d+) items?\)", desc)
        items = int(m.group(1)) if m else None
        total = sum(u[f] for f in FIELDS)
        rows.append({
            "session": session,
            "agent_id": agent_id,
            "description": desc,
            "items": items,
            "turns": u["turns"],
            **{f: u[f] for f in FIELDS},
            "thinking_tokens": u["thinking_tokens"],
            "total_tokens": total,
            "tokens_per_item": round(total / items) if items else None,
            "output_per_item": round(u["output_tokens"] / items) if items else None,
            "cache_hit_pct": round(100 * u["cache_read_input_tokens"] / total, 1) if total else None,
        })

    if not rows:
        sys.exit(f"no 'webclip batch' agents in session {session}")

    hdr = f"{'batch':<28}{'items':>6}{'turns':>7}{'total':>12}{'per item':>10}{'out/item':>10}{'cache%':>8}"
    print(hdr)
    for r in rows:
        print(f"{r['description'][:27]:<28}{r['items'] or '?':>6}{r['turns']:>7}{r['total_tokens']:>12,}"
              f"{r['tokens_per_item'] or '?':>10}{r['output_per_item'] or '?':>10}{r['cache_hit_pct']:>8}")

    if csv_path:
        seen = set()
        if csv_path.exists():
            with csv_path.open(encoding="utf-8", newline="") as f:
                seen = {r["agent_id"] for r in csv.DictReader(f)}
        new = [r for r in rows if r["agent_id"] not in seen]
        write_header = not csv_path.exists()
        with csv_path.open("a", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            if write_header:
                w.writeheader()
            w.writerows(new)
        print(f"\n{len(new)} new row(s) appended to {csv_path}")


if __name__ == "__main__":
    main()
