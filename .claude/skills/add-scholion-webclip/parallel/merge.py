# Apply a finished worker's results to the manifest (only the orchestrator runs this).
#
#   python merge.py <workdir> <stream> <round>
#
# Reads <workdir>/results-<stream>.json, updates the matching manifest items (by url),
# backs the manifest up first, then marks <stream><round>.json as merged and renames
# the results file so the next round starts clean.
import collections, json, os, shutil, sys

MANIFEST = r"C:/Users/conta/OneDrive/MD/_webclip_manifest.json"
workdir, stream, rnd = sys.argv[1], sys.argv[2], sys.argv[3]

res_path = os.path.join(workdir, f"results-{stream}.json")
assign_path = os.path.join(workdir, f"{stream}{rnd}.json")
results = json.load(open(res_path, encoding="utf-8"))
assigned = {i["url"] for i in json.load(open(assign_path, encoding="utf-8"))["items"]}

shutil.copy(MANIFEST, os.path.join(workdir, "manifest.before-merge.json"))
m = json.load(open(MANIFEST, encoding="utf-8"))
by_url = {i["url"]: i for i in m["items"]}

counts, problems = collections.Counter(), []
for r in results:
    item = by_url.get(r["url"])
    if item is None or r["url"] not in assigned:
        problems.append(r["url"])
        continue
    item["status"] = r["status"]
    if r["status"] == "done":
        item.pop("reason", None)
    else:
        item["reason"] = r.get("reason", "")
    counts[r["status"]] += 1

missing = assigned - {r["url"] for r in results}
open(MANIFEST, "w", encoding="utf-8", newline="\n").write(json.dumps(m, ensure_ascii=False, indent=2) + "\n")

assignment = json.load(open(assign_path, encoding="utf-8"))
assignment["merged"] = True
json.dump(assignment, open(assign_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
os.replace(res_path, res_path + f".{rnd}.merged")

print(dict(counts), "| not in assignment:", problems, "| assigned but no result:", sorted(missing))
print("pending:", dict(collections.Counter(i["type"] for i in m["items"] if i["status"] == "pending")))
