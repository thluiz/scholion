# Turn failed url items into pending md_file items after recover.ts wrote their captures.
#
#   python apply-recovery.py <recover-out.json> [<recover-out.json> ...]
#
# Recovered items keep their url (the manifest key and the note's source) and get
# type md_file, md_path, pool "recovery", recovered_from, previous_reason. Items that
# could not be recovered keep their failed status; the attempt is appended to reason.
import json, shutil, sys, collections

MANIFEST = r"C:/Users/conta/OneDrive/MD/_webclip_manifest.json"
shutil.copy(MANIFEST, MANIFEST.replace(".json", ".before-recovery.bak.json"))
m = json.load(open(MANIFEST, encoding="utf-8"))
by_url = {i["url"]: i for i in m["items"]}

counts = collections.Counter()
for path in sys.argv[1:]:
    for r in json.load(open(path, encoding="utf-8")):
        item = by_url.get(r["url"])
        if item is None or item["status"] not in ("failed", "skipped"):
            counts["not_applicable"] += 1
            continue
        if r.get("error"):
            item["reason"] = f"{item.get('reason', '')} | recovery attempt: {r['error']}".strip(" |")
            counts["still_failed"] += 1
            continue
        item["previous_reason"] = item.get("reason", "")
        item.pop("reason", None)
        item.update(type="md_file", md_path=r["md_path"], status="pending", pool="recovery", recovered_from=r["recovered_from"])
        counts[f"recovered_{r['recovered_from']}"] += 1

open(MANIFEST, "w", encoding="utf-8", newline="\n").write(json.dumps(m, ensure_ascii=False, indent=2) + "\n")
print(dict(counts))
