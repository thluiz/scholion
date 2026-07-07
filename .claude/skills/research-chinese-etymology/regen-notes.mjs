// Usage: node regen-notes.mjs <hex> [hex...] [--model NAME] [--no-commit]
// Regenera notas de etimologia existentes (pós-auditoria de fontes):
//   hex -> char+radicalNum via índice os-214-radicais-kangxi.md ->
//   audit-crawl (regenera clean com o limpador atual) -> generate-note ->
//   se o slug mudou, git rm do arquivo antigo.
// Depois: UM hugo build; commit-por-nota "fix: ..." + push. Loga em .crawl/regen.log.
import { readFileSync, writeFileSync, appendFileSync, existsSync, readdirSync } from 'fs';
import { spawnSync } from 'child_process';

const argv = process.argv.slice(2);
const opt = (flag, def = null) => { const i = argv.indexOf(flag); return i >= 0 ? argv[i + 1] : def; };
const MODEL = opt('--model');
const NO_COMMIT = argv.includes('--no-commit');
const hexes = argv.filter(a => /^[0-9a-f]{4,5}$/i.test(a)).map(h => h.toLowerCase());
if (!hexes.length) { console.error('Usage: node regen-notes.mjs <hex> [hex...] [--model NAME] [--no-commit]'); process.exit(2); }

const SKILL = '.claude/skills/research-chinese-etymology';
const LOG = '.crawl/regen.log';
const log = m => { const line = `[${new Date().toISOString()}] ${m}`; console.log(line); appendFileSync(LOG, line + '\n'); };
const sh = (cmd, args, o = {}) => spawnSync(cmd, args, { encoding: 'utf8', maxBuffer: 64 * 1024 * 1024, ...o });

// índice: char por número de radical; mapear por codepoint
const byHex = new Map();
for (const line of readFileSync('content/notes/os-214-radicais-kangxi.md', 'utf8').split(/\r?\n/)) {
  const m = line.match(/^\|\s*(\d{1,3})\s*\|\s*([^\s|(]+)/);
  if (!m) continue;
  const num = +m[1]; if (num < 1 || num > 214) continue;
  const ch = [...m[2].trim()][0];
  const hx = ch.codePointAt(0).toString(16);
  if (!byHex.has(hx)) byHex.set(hx, { ch, num });
}

const done = []; const failed = [];
for (const hex of hexes) {
  const entry = byHex.get(hex);
  if (!entry) { log(`${hex}: não está no índice dos 214 — pulando`); failed.push({ hex, stage: 'indice' }); continue; }
  const { ch, num } = entry;
  const oldFile = readdirSync('content/notes').find(f => f.endsWith(`-${hex}.md`) && f.startsWith('etimologia-de-'));
  log(`--- ${ch} (rad ${num}, ${hex}) ${oldFile ? `[substitui ${oldFile}]` : '[nota antiga não achada]'} ---`);

  if (!existsSync(`.crawl/crawl-${hex}.md`)) { log('  sem dump — pulando (rode crawl-radical antes)'); failed.push({ ch, hex, stage: 'dump' }); continue; }
  const a = sh('node', [`${SKILL}/audit-crawl.mjs`, hex]);
  let verdict; try { verdict = JSON.parse(a.stdout.trim()); } catch { verdict = { ok: false }; }
  if (!verdict.ok) { log(`  AUDIT reprovou: ${(verdict.missing || []).join(',')}`); failed.push({ ch, hex, stage: 'audit' }); continue; }

  const gArgs = [`${SKILL}/generate-note.mjs`, ch, String(num), hex];
  if (MODEL) gArgs.push(MODEL);
  const g = sh('node', gArgs);
  let gen; try { gen = JSON.parse(g.stdout.trim().split('\n').find(l => l.startsWith('{')) || '{}'); } catch { gen = { ok: false }; }
  if (!gen.ok) { log(`  GENERATE falhou: ${gen.reason || (g.stderr || '').slice(0, 150)}`); failed.push({ ch, hex, stage: 'generate' }); continue; }

  // slug mudou? NÃO fazer git rm aqui — staging antecipado vaza para o commit
  // do primeiro da fila (o commit -F sem pathspec leva tudo que estiver staged).
  // A remoção acontece junto do commit da própria nota, lá embaixo.
  let oldPath = null;
  if (oldFile && `content/notes/${oldFile}` !== gen.file) {
    log(`  slug mudou: ${oldFile} -> ${gen.slug}.md (remoção adiada p/ o commit)`);
    oldPath = `content/notes/${oldFile}`;
  }
  log(`  OK -> ${gen.slug} (${gen.bytes}b, ${gen.model})`);
  done.push({ ch, num, hex, slug: gen.slug, files: [gen.file], oldPath });
}

log(`regeneradas: ${done.length} | falhas: ${failed.length}${failed.length ? ' (' + failed.map(f => `${f.ch || f.hex}:${f.stage}`).join(', ') + ')' : ''}`);
if (!done.length) process.exit(1);

log('hugo build...');
const b = sh('hugo', ['--minify', '--gc', '--quiet'], { shell: true });
if (b.status !== 0) { log(`BUILD FALHOU — nada comitado. ${(b.stderr || '').slice(0, 500)}`); process.exit(1); }
log('build OK');
if (NO_COMMIT) { log('--no-commit: fim sem commit'); process.exit(0); }

for (const d of done) {
  sh('git', ['add', ...d.files], { shell: true });
  if (d.oldPath) sh('git', ['rm', '-q', '--ignore-unmatch', d.oldPath], { shell: true });
  writeFileSync('.crawl/msg.txt', `fix: regenera etimologia de ${d.ch} (auditoria de fontes, radical Kangxi ${d.num})\n`, 'utf8');
  const c = sh('git', ['commit', '-F', '.crawl/msg.txt', '--no-verify'], { shell: true });
  if (c.status !== 0) log(`  commit falhou (${d.ch}): ${(c.stdout || c.stderr || '').slice(0, 150)}`);
}
log('push...');
const p = sh('git', ['push'], { shell: true });
log(p.status === 0 ? 'push OK' : `push falhou: ${(p.stderr || '').slice(0, 200)}`);
log(`FIM — ${done.length} notas regeneradas${p.status === 0 ? ' e pushed' : ''}`);
