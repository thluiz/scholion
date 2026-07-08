// Usage: node glossary-batch.mjs [--force 字字]
// Gera os verbetes de TODOS os primitivos parqueados (PARK) que ainda não têm
// fragmento em .crawl/gloss/. Números de radical vêm do índice os-214.
// Sequencial (chamadas LLM via gateway). --force regenera os chars indicados.
import { readFileSync, existsSync } from 'fs';
import { spawnSync } from 'child_process';

const argv = process.argv.slice(2);
const fi = argv.indexOf('--force');
const FORCE = new Set(fi >= 0 ? [...argv[fi + 1]] : []);

const PARK = [...'丨丶丿亅亠儿冂冖冫凵勹匚匸卩厶囗夂夊尢屮巛廴廾彐彡彳疒癶禸舛虍襾釆'];
const byChar = new Map();
for (const line of readFileSync('content/notes/os-214-radicais-kangxi.md', 'utf8').split(/\r?\n/)) {
  const m = line.match(/^\|\s*(\d{1,3})\s*\|\s*\[?([^\s|()\]]+)/);
  if (m) { const ch = [...m[2].trim()][0]; if (!byChar.has(ch)) byChar.set(ch, +m[1]); }
}

let ok = 0, fail = 0, skip = 0;
for (const ch of PARK) {
  const num = byChar.get(ch);
  if (!num) { console.log(`${ch}: não achei no índice — PULANDO`); fail++; continue; }
  const hex = ch.codePointAt(0).toString(16);
  const frag = `.crawl/gloss/entry-${String(num).padStart(3, '0')}-${hex}.md`;
  if (existsSync(frag) && !FORCE.has(ch)) { skip++; continue; }
  const r = spawnSync('node', ['.claude/skills/research-chinese-etymology/glossary-entry.mjs', ch, String(num), hex], { encoding: 'utf8', maxBuffer: 16 * 1024 * 1024 });
  let v; try { v = JSON.parse(r.stdout.trim().split('\n').pop()); } catch { v = { ok: false, reason: 'sem JSON' }; }
  console.log(`${ch} (rad ${num}): ${v.ok ? 'OK ' + v.bytes + 'b' : 'FALHOU — ' + v.reason}`);
  v.ok ? ok++ : fail++;
}
console.log(`fim: ${ok} ok, ${skip} já existiam, ${fail} falhas`);
process.exit(fail ? 1 : 0);
