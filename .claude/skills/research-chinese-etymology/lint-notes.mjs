// Usage: node lint-notes.mjs [--fix] [--quiet]
// Lint determinístico (zero tokens) das notas de etimologia:
//   1. Léxico PT-EU -> PT-BR (corrigível com --fix)
//   2. Acento errado "cantonêsa(s)" (corrigível com --fix)
//   3. CJK colado em prosa latina (APENAS reporta — pode ser citação verbatim)
//   4. "Note-se / Nota-se que" (APENAS reporta — meta-narração)
// Saída: JSON com achados por arquivo. Com --fix, aplica 1-2 e lista os alterados.
// Pensado para rodar também dentro do driver, após cada generate.
import { readFileSync, writeFileSync, readdirSync } from 'fs';

const FIX = process.argv.includes('--fix');
const QUIET = process.argv.includes('--quiet');

// pares PT-EU -> PT-BR; \b nas bordas; só prosa PT (tokens latinos, não aparecem em chinês)
const LEXICON = [
  [/\bregista\b/g, 'registra'], [/\bregistam\b/g, 'registram'],
  [/\bregistou\b/g, 'registrou'], [/\bregistado(s?)\b/g, 'registrado$1'],
  [/\bregistada(s?)\b/g, 'registrada$1'], [/\bregistar\b/g, 'registrar'],
  [/\bregiste\b/g, 'registre'],
  [/génese/g, 'gênese'], [/género(s?)\b/g, 'gênero$1'],
  [/polémic/g, 'polêmic'], [/académic/g, 'acadêmic'],
  [/topónim/g, 'topônim'], [/sinónim/g, 'sinônim'], [/homónim/g, 'homônim'],
  [/fenómen/g, 'fenômen'], [/\bsecção\b/g, 'seção'], [/\bsecções\b/g, 'seções'],
  [/\bfacto\b/g, 'fato'], [/\bfactos\b/g, 'fatos'],
  [/\bactuais\b/g, 'atuais'], [/\bactual\b/g, 'atual'],
  [/cantonês(a|as)\b/g, 'cantones$1'],
];
// reporta, não corrige
const REPORT_ONLY = [
  { name: 'cjk-colado', re: /[a-záéíóúâêôãõç,;][一-鿿]|[一-鿿][a-záéíóúâêôãõç]/ },
  { name: 'note-se', re: /\b[Nn]ote-se\b|\b[Nn]ota-se que\b/ },
];

const files = readdirSync('content/notes').filter(f => /^etimologia-de-.*\.md$/.test(f));
const results = []; const changed = [];

for (const f of files) {
  const path = `content/notes/${f}`;
  let text = readFileSync(path, 'utf8');
  const findings = [];

  for (const [re, sub] of LEXICON) {
    const m = text.match(re);
    if (m) findings.push({ tipo: 'pt-eu', token: m[0], n: m.length, fix: FIX });
    if (FIX && m) text = text.replace(re, sub);
  }
  for (const { name, re } of REPORT_ONLY) {
    const lines = text.split('\n');
    for (let i = 0; i < lines.length; i++) {
      const m = lines[i].match(re);
      if (m) findings.push({ tipo: name, linha: i + 1, trecho: lines[i].slice(Math.max(0, m.index - 12), m.index + 15) });
    }
  }
  if (findings.length) {
    results.push({ file: f, findings });
    if (FIX && findings.some(x => x.fix)) { writeFileSync(path, text, 'utf8'); changed.push(path); }
  }
}

if (!QUIET) console.log(JSON.stringify({ scanned: files.length, comAchados: results.length, results }, null, 1));
if (FIX) console.log(JSON.stringify({ changed }, null, 1));
process.exit(0);
