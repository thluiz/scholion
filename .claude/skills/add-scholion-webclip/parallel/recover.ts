// Recover failed webclip items as legacy-style captured Markdown files, so the
// md_file pipeline (text mode, never refetched) can process them unchanged.
//
//   bun run recover.ts <recovery.json> <out-list.json>
//
// recovery.json: { "wayback": {origUrl: snapshotUrl}, "medium_wayback": {...}, "tweet": [origUrl] }
// Writes C:\Users\conta\OneDrive\MD\<name>.md per recovered item and a list of
// { url, md_path, recovered_from, chars } (or { url, error }) to out-list.json.
import { Readability } from "E:/scholion-webclipper/node_modules/@mozilla/readability/index.js";
import { JSDOM, VirtualConsole } from "E:/scholion-webclipper/node_modules/jsdom/lib/api.js";
import TurndownService from "E:/scholion-webclipper/node_modules/turndown/lib/turndown.cjs.js";
import { existsSync, readFileSync, writeFileSync } from "fs";

const MD_ROOT = "C:/Users/conta/OneDrive/MD/";
const MIN_CHARS = 400;
const [inPath, outPath] = process.argv.slice(2);
const input = JSON.parse(readFileSync(inPath, "utf8"));
const turndown = new TurndownService({ headingStyle: "atx", codeBlockStyle: "fenced" });
const quiet = new VirtualConsole();
const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));

function stamp(d: Date): string {
  return d.toISOString().slice(0, 19) + " (UTC +00:00)";
}

function fileName(title: string): string {
  const base = (title || "untitled").replace(/[\\/:*?"<>|\r\n]+/g, " ").replace(/\s+/g, " ").trim().slice(0, 120);
  let name = `${base}.md`;
  for (let n = 2; existsSync(MD_ROOT + name) || existsSync(MD_ROOT + "_processed/" + name); n++) name = `${base} (${n}).md`;
  return name;
}

function writeCapture(title: string, source: string, created: Date, body: string, extra: Record<string, string>): string {
  const name = fileName(title);
  const fm = [`created: ${stamp(created)}`, "tags: []", `source: ${source}`, ...Object.entries(extra).map(([k, v]) => `${k}: ${v}`)];
  writeFileSync(MD_ROOT + name, `---\n${fm.join("\n")}\n---\n\n# ${title}\n\n${body.trim()}\n`, "utf8");
  return name;
}

async function fromWayback(orig: string, snap: string) {
  // "id_" after the timestamp returns the archived page without the Wayback toolbar.
  const raw = snap.replace(/^http:/, "https:").replace(/\/web\/(\d+)\//, "/web/$1id_/");
  const ts = snap.match(/\/web\/(\d{14})/)?.[1] ?? "";
  const res = await fetch(raw, { headers: { "User-Agent": "Mozilla/5.0" }, redirect: "follow" });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  // Decode as UTF-8 ourselves: archived responses often carry a stale latin-1 charset
  // header, which turned "Você" into "VocÃª". Fall back to latin-1 only if UTF-8 fails.
  const buf = new Uint8Array(await res.arrayBuffer());
  let html = new TextDecoder("utf-8").decode(buf);
  if ((html.match(/�/g) ?? []).length > 20) html = new TextDecoder("latin1").decode(buf);
  const dom = new JSDOM(html, { url: orig, virtualConsole: quiet });
  const art = new Readability(dom.window.document).parse();
  if (!art?.content) throw new Error("readability found no article");
  const md = turndown.turndown(art.content);
  const chars = (art.textContent ?? "").replace(/\s+/g, " ").trim().length;
  if (chars < MIN_CHARS) throw new Error(`too thin (${chars} chars)`);
  const created = ts ? new Date(`${ts.slice(0, 4)}-${ts.slice(4, 6)}-${ts.slice(6, 8)}T${ts.slice(8, 10)}:${ts.slice(10, 12)}:${ts.slice(12, 14)}Z`) : new Date();
  const name = writeCapture(art.title || orig, orig, created, md, { archived_copy: snap });
  return { md_path: name, recovered_from: "wayback", chars };
}

async function fromTweet(orig: string) {
  const id = orig.match(/status(?:es)?\/(\d+)/)?.[1];
  if (!id) throw new Error("no status id in url");
  const res = await fetch(`https://api.fxtwitter.com/status/${id}`);
  const j: any = await res.json();
  if (j.code !== 200 || !j.tweet) throw new Error(`fxtwitter ${j.code}: ${j.message}`);
  const t = j.tweet;
  let text: string = t.text ?? "";
  if (t.article?.content?.blocks) text = t.article.content.blocks.map((b: any) => b.text).join("\n\n");
  if (t.quote?.text) text += `\n\n> ${t.quote.author?.name ?? ""} (@${t.quote.author?.screen_name ?? ""}): ${t.quote.text}`;
  const chars = text.replace(/\s+/g, " ").trim().length;
  if (chars < MIN_CHARS) throw new Error(`too thin (${chars} chars)`);
  const title = t.article?.title || `${t.author?.name} (@${t.author?.screen_name}) on X`;
  const name = writeCapture(title, orig, new Date(t.created_timestamp * 1000), text, { author: t.author?.name ?? "", fetched_via: "api.fxtwitter.com" });
  return { md_path: name, recovered_from: "fxtwitter", chars };
}

const jobs: [string, () => Promise<any>][] = [
  ...Object.entries<string>(input.wayback ?? {}).map(([u, s]) => [u, () => fromWayback(u, s)] as [string, () => Promise<any>]),
  ...Object.entries<string>(input.medium_wayback ?? {}).map(([u, s]) => [u, () => fromWayback(u, s)] as [string, () => Promise<any>]),
  ...(input.tweet ?? []).map((u: string) => [u, () => fromTweet(u)] as [string, () => Promise<any>]),
];

const out: any[] = [];
for (const [url, job] of jobs) {
  try {
    out.push({ url, ...(await job()) });
  } catch (e) {
    out.push({ url, error: e instanceof Error ? e.message : String(e) });
  }
  await sleep(1500); // be polite to archive.org / fxtwitter
}
writeFileSync(outPath, JSON.stringify(out, null, 1), "utf8");
const ok = out.filter((o) => !o.error);
console.log(`recovered ${ok.length} of ${out.length}`);
