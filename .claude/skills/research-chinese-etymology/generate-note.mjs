// Usage: node generate-note.mjs <char> <radicalNum> <hex> [model]
// Lê .crawl/clean-<hex>.md (fallback crawl-<hex>.md), envia char + gabarito
// (nota de 水) + dump para o preset scholion/etymology-note da vox-intelligence,
// e grava content/notes/<slug>.md. Emite veredito JSON. NÃO builda nem comita.
// A síntese, o parse do contrato SLUG/nota e um repair round-trip acontecem
// no servidor (templates/scholion/etymology-note.ts).
// Override do endpoint: env VOX_INTELLIGENCE_URL.
import { readFileSync, writeFileSync, existsSync } from 'fs';

// timestamp local com offset (ex.: 2026-07-05T14:03:22+01:00), sem shell
function isoWithOffset(d = new Date()) {
  const pad = n => String(n).padStart(2, '0');
  const off = -d.getTimezoneOffset();
  const sign = off >= 0 ? '+' : '-';
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}` +
         `T${pad(d.getHours())}:${pad(d.getMinutes())}:${pad(d.getSeconds())}` +
         `${sign}${pad(Math.floor(Math.abs(off) / 60))}:${pad(Math.abs(off) % 60)}`;
}

const [char, numArg, hexArg, model] = process.argv.slice(2);
if (!char || !numArg || !hexArg) {
  console.error('Usage: node generate-note.mjs <char> <radicalNum> <hex> [model]');
  process.exit(2);
}
const hex = hexArg.toLowerCase();
const VOX_URL = process.env.VOX_INTELLIGENCE_URL
  || 'http://localhost:8080/api/vox-intelligence';

const dumpFile = existsSync(`.crawl/clean-${hex}.md`) ? `.crawl/clean-${hex}.md`
              : existsSync(`.crawl/crawl-${hex}.md`) ? `.crawl/crawl-${hex}.md` : null;
if (!dumpFile) { console.log(JSON.stringify({ char, ok: false, reason: 'dump inexistente' })); process.exit(1); }

const body = {
  char,
  radicalNum: numArg,
  hex,
  date: isoWithOffset(),
  gabarito: readFileSync('content/notes/etimologia-de-seoi-shui-6c34.md', 'utf8'),
  dump: readFileSync(dumpFile, 'utf8'),
};
if (model) body.model = model;

let res, data;
try {
  const ctrl = new AbortController();
  const t = setTimeout(() => ctrl.abort(), 600000);
  res = await fetch(`${VOX_URL}/presets/scholion/etymology-note`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
    signal: ctrl.signal,
  });
  clearTimeout(t);
  data = await res.json();
} catch (err) {
  console.log(JSON.stringify({ char, ok: false, reason: `vox-intelligence inacessível: ${err.message}` }));
  process.exit(1);
}
if (!res.ok || !data.slug || !data.note) {
  const reason = data?.error?.message || `HTTP ${res.status}`;
  console.log(JSON.stringify({ char, ok: false, reason: `vox-intelligence falhou: ${reason}` }));
  process.exit(1);
}

const { slug, note } = data;
const file = `content/notes/${slug}.md`;
writeFileSync(file, note, 'utf8');
console.log(JSON.stringify({
  char, slug, ok: true, file,
  bytes: Buffer.byteLength(note, 'utf8'),
  model: data.model,
  tokens: data.usage ? `${data.usage.prompt_tokens}in/${data.usage.completion_tokens}out` : undefined,
}));
