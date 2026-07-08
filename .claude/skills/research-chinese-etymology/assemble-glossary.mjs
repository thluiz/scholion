// Usage: node assemble-glossary.mjs [--out content/notes/glossario-dos-radicais-primitivos.md]
// Monta a nota-glossário única a partir dos fragmentos .crawl/gloss/entry-*.md
// (ordenados pelo nº do radical no nome do arquivo). Determinístico, zero LLM.
import { readFileSync, writeFileSync, readdirSync } from 'fs';

const argv = process.argv.slice(2);
const opt = (flag, def) => { const i = argv.indexOf(flag); return i >= 0 ? argv[i + 1] : def; };
const OUT = opt('--out', 'content/notes/glossario-dos-radicais-primitivos.md');

function isoWithOffset(d = new Date()) {
  const pad = n => String(n).padStart(2, '0');
  const off = -d.getTimezoneOffset();
  const sign = off >= 0 ? '+' : '-';
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}` +
         `T${pad(d.getHours())}:${pad(d.getMinutes())}:${pad(d.getSeconds())}` +
         `${sign}${pad(Math.floor(Math.abs(off) / 60))}:${pad(Math.abs(off) % 60)}`;
}

const frags = readdirSync('.crawl/gloss').filter(f => /^entry-\d{3}-[0-9a-f]+\.md$/.test(f)).sort();
if (!frags.length) { console.error('nenhum fragmento em .crawl/gloss'); process.exit(1); }
const entries = frags.map(f => readFileSync(`.crawl/gloss/${f}`, 'utf8').trim());
const chars = entries.map(e => (e.match(/^### (\S)/) || [])[1]).filter(Boolean);

const note = `---
title: "Glossário dos radicais primitivos (Kangxi)"
date: '${isoWithOffset()}'
summary: 'Verbete compacto para cada um dos ${entries.length} radicais Kangxi que não são caracteres plenos de uso corrente — primitivos de traço e componentes gráficos (丨 丶 丿 亅 冖 勹…): Shuowen verbatim, leituras atestadas e leitura paleográfica, das mesmas 7 fontes das notas individuais.'
toc: true
tags: ["china", "linguagem", "etimologia", "ideogramas", "radicais"]
category: etymology
has_commentary: false
sources:
- title: MDBG Chinese Dictionary
  url: https://www.mdbg.net/chinese/dictionary
  kind: wiki
- title: chardb — Academia Sinica
  url: https://chardb.iis.sinica.edu.tw
  kind: wiki
- title: CantoDict (cantonese.org)
  url: https://www.cantonese.org
  kind: wiki
- title: Chinese Etymology (hanziyuan.net)
  author: Richard Sears
  url: https://hanziyuan.net
  kind: wiki
- title: 小學堂 — Academia Sinica
  url: https://xiaoxue.iis.sinica.edu.tw
  kind: wiki
- title: 漢語多功能字庫 (CUHK)
  url: https://humanum.arts.cuhk.edu.hk/Lexis/lexi-mf/
  kind: wiki
---

Dos 214 radicais Kangxi, ${entries.length} não são caracteres plenos de uso corrente: são primitivos de traço e componentes gráficos que funcionam quase só como chave de indexação (${chars.join(' ')}). Em vez de uma nota de etimologia por caractere, este glossário reúne um verbete compacto para cada um, com as mesmas fontes e regras das notas individuais. Ver [Os 214 radicais Kangxi](/notes/os-214-radicais-kangxi/).

${entries.join('\n\n')}
`;

writeFileSync(OUT, note, 'utf8');
console.log(JSON.stringify({ ok: true, out: OUT, entries: entries.length, bytes: Buffer.byteLength(note, 'utf8') }));
