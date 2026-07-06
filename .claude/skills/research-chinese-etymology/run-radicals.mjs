// Usage: node run-radicals.mjs [--limit N] [--only 字字字] [--model NAME] [--no-commit]
// Orquestra o pipeline dos radicais plenos que faltam:
//   para cada caractere -> crawl -> audit -> generate (claude -p)
// Depois: UM hugo build; se passar, commit-por-nota + push.
// Resumível: pula radicais que já têm nota (audit por título). Loga em stdout + .crawl/run.log.
import { readFileSync, writeFileSync, appendFileSync, existsSync, readdirSync } from 'fs';
import { spawnSync } from 'child_process';

const argv = process.argv.slice(2);
const opt = (flag, def = null) => { const i = argv.indexOf(flag); return i >= 0 ? argv[i + 1] : def; };
const has = flag => argv.includes(flag);
const LIMIT = opt('--limit') ? +opt('--limit') : Infinity;
const ONLY = opt('--only');
const MODEL = opt('--model');
const NO_COMMIT = has('--no-commit');

const SKILL = '.claude/skills/research-chinese-etymology';
const LOG = '.crawl/run.log';
const log = m => { const line = `[${new Date().toISOString()}] ${m}`; console.log(line); appendFileSync(LOG, line + '\n'); };
const sh = (cmd, args, o = {}) => spawnSync(cmd, args, { encoding: 'utf8', maxBuffer: 64 * 1024 * 1024, ...o });

// primitivos de traço parqueados (glossário no fim) — NÃO entram no batch
const PARK = new Set([...'丨丶丿亅亠儿冂冖冫凵勹匚匸卩厶囗夂夊尢屮巛廴廾彐彡彳疒癶禸舛虍襾釆']);

// --- montar worklist: radicais faltantes (por título) menos PARK ---
const idx = readFileSync('content/notes/os-214-radicais-kangxi.md', 'utf8').split(/\r?\n/);
const files = readdirSync('content/notes').filter(f => f.endsWith('.md'));
const titles = files.map(f => (readFileSync('content/notes/' + f, 'utf8').split(/\r?\n/).find(l => l.startsWith('title:')) || ''));
const doneChar = ch => titles.some(t => { const m = t.match(/Etimologia de (\S)/); return m && m[1] === ch; });

const rows = []; const seen = new Set();
for (const line of idx) {
  const m = line.match(/^\|\s*(\d{1,3})\s*\|\s*([^\s|(]+)/);
  if (!m) continue;
  const num = +m[1]; if (num < 1 || num > 214 || seen.has(num)) continue;
  seen.add(num); rows.push({ num, ch: [...m[2].trim()][0] });
}
let work = rows.filter(r => !doneChar(r.ch) && !PARK.has(r.ch));
if (ONLY) { const set = new Set([...ONLY]); work = work.filter(r => set.has(r.ch)); }
work = work.slice(0, LIMIT);

log(`worklist: ${work.length} radicais plenos -> ${work.map(r => r.ch).join('')}`);
if (!work.length) { log('nada a fazer'); process.exit(0); }

const done = []; const failed = [];
for (const { num, ch } of work) {
  const hex = ch.codePointAt(0).toString(16);
  log(`--- ${ch} (rad ${num}, ${hex}) ---`);

  // crawl (se dump ausente)
  if (!existsSync(`.crawl/crawl-${hex}.md`)) {
    const c = sh('node', [`${SKILL}/crawl-radical.mjs`, ch]);
    if (c.status !== 0) { log(`  CRAWL falhou: ${(c.stderr || '').slice(0, 200)}`); failed.push({ ch, num, hex, stage: 'crawl' }); continue; }
    writeFileSync(`.crawl/crawl-${hex}.md`, c.stdout, 'utf8');
  }
  // audit
  const a = sh('node', [`${SKILL}/audit-crawl.mjs`, hex]);
  let verdict; try { verdict = JSON.parse(a.stdout.trim()); } catch { verdict = { ok: false, reason: 'audit sem JSON' }; }
  if (!verdict.ok) { log(`  AUDIT reprovou: missing=${(verdict.missing || []).join(',')} ${verdict.reason || ''}`); failed.push({ ch, num, hex, stage: 'audit', verdict }); continue; }
  if (verdict.warnings?.length) log(`  audit warnings: ${verdict.warnings.join(' | ')}`);

  // generate
  const gArgs = [`${SKILL}/generate-note.mjs`, ch, String(num), hex];
  if (MODEL) gArgs.push(MODEL);
  const g = sh('node', gArgs);
  let gen; try { gen = JSON.parse(g.stdout.trim().split('\n').find(l => l.startsWith('{')) || '{}'); } catch { gen = { ok: false, reason: 'generate sem JSON', head: (g.stdout || g.stderr || '').slice(0, 200) }; }
  if (!gen.ok) { log(`  GENERATE falhou: ${gen.reason || ''}`); failed.push({ ch, num, hex, stage: 'generate', gen }); continue; }
  log(`  OK -> ${gen.slug} (${gen.bytes}b, ~${verdict.estTokens} tok in)`);
  done.push({ ch, num, hex, slug: gen.slug, file: gen.file });
}

log(`gerados: ${done.length} | falhas: ${failed.length}`);
if (failed.length) log(`falhas: ${failed.map(f => f.ch + ':' + f.stage).join(', ')}`);
if (!done.length) { log('nenhuma nota gerada — sem build/commit'); process.exit(1); }

// build único
log('hugo build...');
const b = sh('hugo', ['--minify', '--gc', '--quiet'], { shell: true });
if (b.status !== 0) {
  log(`BUILD FALHOU — nada será comitado. stderr: ${(b.stderr || '').slice(0, 800)}`);
  process.exit(1);
}
log('build OK');

if (NO_COMMIT) { log('--no-commit: notas geradas mas não comitadas'); process.exit(0); }

// commit por nota + push
for (const d of done) {
  sh('git', ['add', d.file], { shell: true });
  writeFileSync('.crawl/msg.txt', `feat: etimologia de ${d.ch} (radical Kangxi ${d.num})\n`, 'utf8');
  const c = sh('git', ['commit', '-F', '.crawl/msg.txt', '--no-verify'], { shell: true });
  if (c.status !== 0) { log(`  commit falhou (${d.ch}): ${(c.stdout || c.stderr || '').slice(0, 200)}`); }
}
log('push...');
const p = sh('git', ['push'], { shell: true });
log(p.status === 0 ? 'push OK' : `push falhou: ${(p.stderr || '').slice(0, 300)}`);
log(`FIM — ${done.length} notas comitadas${p.status === 0 ? ' e pushed' : ''}`);
