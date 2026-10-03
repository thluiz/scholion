// Usage: node check-exists.mjs <CHAR...> [--json]
// Pre-flight check: does the Scholion already have an etymology note for each
// character? Must run BEFORE any research or fetch (sources are rate-sensitive
// and the research is expensive). Node only, no dependencies.
//
// For each character it prints one of:
//   EXISTS <path>[, <path>...]   dedicated etymology note(s) found
//   MISSING                      no dedicated note
// plus, when applicable:
//   DUPLICATE                    more than one dedicated note for the same character
//   embedded: <path>...          compound etymology notes (etimologia-de-*) that carry a
//                                per-character section for it ("### <CHAR>" or
//                                "**<CHAR>** — U+...") — material to extract, not a note
//   related: <path>...           other notes/research whose title cites the character
//                                (quotes, disciple notes, living research) — link candidates
//
// A note is "dedicated" to a character when any of these holds:
//   1. its filename matches etimologia-de-*-<hex>.md (hex = lowercase codepoint);
//   2. its frontmatter title starts with "Etimologia de <CHAR>" followed by a
//      space, "(" or end of title (legacy slugs without hex);
//   3. its filename starts with etimologia-de-, its title names a single
//      character, and the body opens with "**<CHAR>** — U+..." (legacy notes
//      whose title does not follow the convention).
// Searched: content/notes/ and content/research/ (feedback_buscar_em_research).
// Exit code: 0 always (informational). Use --json for machine-readable output.
import { readdirSync, readFileSync, existsSync } from 'fs';
import { resolve, dirname, join } from 'path';
import { fileURLToPath } from 'url';

const argv = process.argv.slice(2);
const JSON_OUT = argv.includes('--json');
const chars = [...argv.filter(a => !a.startsWith('--')).join('')]
  .filter(ch => /\p{Script=Han}/u.test(ch));
if (!chars.length) {
  console.error('Usage: node check-exists.mjs <CHAR...> [--json]');
  process.exit(2);
}

// Repo root derived from the script location: <root>/.claude/skills/<skill>/check-exists.mjs
const ROOT = process.env.SCHOLION_ROOT || resolve(dirname(fileURLToPath(import.meta.url)), '../../..');
const DIRS = ['content/notes', 'content/research'].map(d => join(ROOT, d)).filter(existsSync);

// Load every markdown file once: path, filename, frontmatter title, body lines.
const docs = [];
for (const dir of DIRS) {
  for (const f of readdirSync(dir)) {
    if (!f.endsWith('.md')) continue;
    const path = join(dir, f).replace(/\\/g, '/');
    const text = readFileSync(path, 'utf8');
    const lines = text.split(/\r?\n/);
    const titleLine = lines.find(l => /^title:/.test(l)) || '';
    const title = titleLine.replace(/^title:\s*/, '').replace(/^['"]|['"]$/g, '').trim();
    // body = after the closing frontmatter fence
    let fenceCount = 0, bodyStart = 0;
    for (let i = 0; i < lines.length; i++) {
      if (/^---\s*$/.test(lines[i])) { fenceCount++; if (fenceCount === 2) { bodyStart = i + 1; break; } }
    }
    const body = lines.slice(bodyStart).filter(l => l.trim() !== '');
    docs.push({ path, file: f, title, body, bodyHead: body.slice(0, 12) });
  }
}

const esc = s => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
// "Etimologia de <one Han char>" in the title, as opposed to a compound (尋橋)
const SINGLE_CHAR_TITLE = /^Etimologia de \p{Script=Han}(\s|\(|$)/u;

function classify(ch) {
  const hex = ch.codePointAt(0).toString(16).toLowerCase();
  const reHexFile = new RegExp(`^etimologia-de-.*-${hex}\\.md$`);
  const reTitle = new RegExp(`^Etimologia de ${esc(ch)}(\\s|\\(|$)`);
  const reDataLine = new RegExp(`^\\*\\*${esc(ch)}\\*\\*\\s*[—–-]\\s*U\\+`);
  const reSection = new RegExp(`^#{2,4}\\s+${esc(ch)}(\\s|$)`);
  const dedicated = [], embedded = [], related = [];
  for (const d of docs) {
    const isEtym = d.file.startsWith('etimologia-de-');
    const byHex = reHexFile.test(d.file);
    const byTitle = reTitle.test(d.title);
    const byBody = isEtym && SINGLE_CHAR_TITLE.test(d.title) && d.bodyHead.some(l => reDataLine.test(l));
    if (byHex || byTitle || byBody) { dedicated.push(d.path); continue; }
    const hasSection = isEtym && d.body.some(l => reSection.test(l) || reDataLine.test(l));
    if (hasSection) embedded.push(d.path);
    else if (d.title.includes(ch)) related.push(d.path);
  }
  return { char: ch, hex, dedicated, embedded, related, duplicate: dedicated.length > 1 };
}

const results = chars.map(classify);

if (JSON_OUT) {
  console.log(JSON.stringify(results, null, 2));
} else {
  const MAX = 8;
  for (const r of results) {
    const head = `${r.char} (U+${r.hex.toUpperCase()}):`;
    if (r.dedicated.length) {
      console.log(`${head} EXISTS ${r.dedicated.join(', ')}`);
      if (r.duplicate) console.log(`  DUPLICATE: ${r.dedicated.length} notas dedicadas ao mesmo caractere`);
    } else {
      console.log(`${head} MISSING`);
    }
    if (r.embedded.length) console.log(`  embedded: ${r.embedded.join(', ')}`);
    if (r.related.length) {
      const more = r.related.length > MAX ? ` (+${r.related.length - MAX} mais; --json lista todas)` : '';
      console.log(`  related: ${r.related.slice(0, MAX).join(', ')}${more}`);
    }
  }
}
