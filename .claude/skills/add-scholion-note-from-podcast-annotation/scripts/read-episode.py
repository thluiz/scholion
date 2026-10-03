#!/usr/bin/env python3
"""Print the fields of a Vox episode that the note skill needs, read from origin/main.

Usage (from Windows, piped through stdin so no nested quoting is needed):

    cat read-episode.py | wsl -d HermesTools -u hermes -- bash -c "python3 - YYYY/MM/WXX/slug"

Fetches the HermesTools clone first, then reads the JSON with `git show` from
origin/main (never the working tree). Only title, metadata, tags and
annotations are printed; the transcript never reaches the caller's context.
"""

import json
import subprocess
import sys

REPO = "/home/hermes/vox-content"
FIELDS = ("title", "metadata", "tags", "annotations")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: read-episode.py <YYYY/MM/WXX/slug>", file=sys.stderr)
        return 2
    path = sys.argv[1].strip("/")
    for ext in (".md", ".json"):
        if path.endswith(ext):
            path = path[: -len(ext)]

    sys.stdout.reconfigure(encoding="utf-8")
    subprocess.run(["git", "-C", REPO, "fetch", "origin", "--quiet"], check=True)
    try:
        raw = subprocess.check_output(
            ["git", "-C", REPO, "show", f"origin/main:{path}.json"],
            stderr=subprocess.PIPE,
        )
    except subprocess.CalledProcessError as exc:
        print(f"NOT_FOUND origin/main:{path}.json", file=sys.stderr)
        print(exc.stderr.decode("utf-8", "replace"), file=sys.stderr)
        return 1

    episode = json.loads(raw)
    print(json.dumps({k: episode.get(k) for k in FIELDS}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
