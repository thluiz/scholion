# Assign the next pending manifest items to one worker stream.
#
#   python partition.py <workdir> <stream> <round> [--n 15] [--pool arquivo] [--type url|md_file|any]
#
# Writes <workdir>/<stream><round>.json ({"round","stream","items"}). Items already
# assigned to another stream whose results were not merged yet are skipped, so
# streams never overlap. The manifest itself is only read here.
import argparse, glob, json, os

MANIFEST = r"C:/Users/conta/OneDrive/MD/_webclip_manifest.json"

ap = argparse.ArgumentParser()
ap.add_argument("workdir")
ap.add_argument("stream")
ap.add_argument("round")
ap.add_argument("--n", type=int, default=15)
ap.add_argument("--pool", default=None)
ap.add_argument("--type", default="any", choices=["url", "md_file", "any"])
a = ap.parse_args()

# Busy = items in assignment files that have no merged results file yet.
busy = set()
for f in glob.glob(os.path.join(a.workdir, "*.json")):
    name = os.path.basename(f)
    if name.startswith("results-") or name.startswith("manifest"):
        continue
    try:
        data = json.load(open(f, encoding="utf-8"))
    except (ValueError, OSError):
        continue
    if not isinstance(data, dict) or "items" not in data or data.get("merged"):
        continue
    busy.update(i["url"] for i in data["items"])

m = json.load(open(MANIFEST, encoding="utf-8"))
pick = [
    i for i in m["items"]
    if i["status"] == "pending"
    and i["url"] not in busy
    and (a.pool is None or i.get("pool") == a.pool)
    and (a.type == "any" or i["type"] == a.type)
][: a.n]

out = os.path.join(a.workdir, f"{a.stream}{a.round}.json")
json.dump({"round": a.round, "stream": a.stream, "items": pick}, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(out, len(pick))
