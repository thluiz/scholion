// Usage: node audit-crawl.mjs <hex>
// Lê .crawl/crawl-<hex>.md, remove ruído de navegação, valida que as fontes
// críticas vieram, e grava .crawl/clean-<hex>.md. Emite um veredito JSON em
// stdout. Exit 0 = pronto para gerar; exit 1 = fonte crítica faltando.
import { readFileSync, writeFileSync, existsSync } from 'fs';

const hex = (process.argv[2] || '').toLowerCase();
if (!hex) { console.error('Usage: node audit-crawl.mjs <hex>'); process.exit(2); }

const raw = `.crawl/crawl-${hex}.md`;
if (!existsSync(raw)) { console.log(JSON.stringify({ hex, ok: false, reason: 'dump inexistente' })); process.exit(1); }

let text = readFileSync(raw, 'utf8');

// hanziyuan: cortar a cauda institucional da página (artigos, news, vídeos,
// biografia do Richard Sears, doações, contribuidores) — nada disso é dado do
// caractere e custa milhares de tokens por chamada.
text = text.replace(
  /(## hanziyuan\.net[\s\S]*?)\n\s*(?:Chinese character and etymology research|News 新闻|About Uncle Hanzi)[\s\S]*?(?=\n## |$)/,
  '$1\n',
);

// linhas de chrome/boilerplate a descartar (match exato após trim)
const CHROME = new Set([
  'This website uses cookies to ensure you get the best experience on our website. Learn more',
  'Got it!', 'WORDS', 'CHARACTERS', 'TRANSLATE', 'PRACTICE', 'HELP',
  'Look up Chinese, Pinyin or English? | Look up All Chinese Words in a Text?',
  'Simplified Chinese', 'Traditional Chinese', 'Advanced Search', 'Show Examples and Help',
  'Auto complete input: off | on', 'Usage Tips', 'Close', 'Show Legend', 'Display Settings',
  'Automated or scripted access is prohibited', 'Privacy and cookies',
  '正體字', '簡化字', '單字 部首 部件 相似字 UNICODE編碼',
  '基本資料', '字形演變', '異體字', '異體詞及成語', '分享',
]);
// regex de linhas de chrome (footers, menus dinâmicos)
const CHROME_RE = [
  /^\d+ results? on this page\.?$/i,
  /^Click the .*action menu/i, /^The .*(Show Legend|Display Settings) link/i,
  /^Tip: Need to type pinyin/i, /^© \d{4}\s+MDBG/i,
  /^每日一字Apps/, /^首頁 \|/, /^中央研究院 版權所有/, /版權所有/,
  /^More information about this dictionary/i,
  // hanziyuan: IDs de imagens de formas antigas (J05524, B19514, S10661, L18500…)
  // — as CONTAGENS ficam nos headers "Oracle characters 甲骨文 (28)"; os IDs são ruído
  /^\s*[JBSL]\d{4,6}\s*$/,
  // hanziyuan: boilerplate do topo (doações, estatísticas do site, instruções de busca)
  /^Please donate/, /^我从1994年开始/, /^Input single Chinese character/i,
  /^输入单个汉字/, /^\s*\d{1,3},000\+\s*$/,
];

const isChrome = l => {
  const t = l.trim();
  if (CHROME.has(t)) return true;
  return CHROME_RE.some(re => re.test(t));
};

// limpar: dropar chrome, colapsar corridas de linhas em branco
const lines = text.split(/\r?\n/);
const out = [];
let blank = 0;
for (const l of lines) {
  if (isChrome(l)) continue;
  if (l.trim() === '') { blank++; if (blank > 1) continue; } else blank = 0;
  out.push(l.replace(/[ \t]+$/, ''));
}
const clean = out.join('\n').replace(/\n{3,}/g, '\n\n').trim() + '\n';

// validação por fonte
const section = name => {
  const m = clean.match(new RegExp(`## ${name.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}([\\s\\S]*?)(?=\\n## |$)`));
  return m ? m[1].trim() : '';
};
const unavailable = body => /FONTE INDISPON[IÍ]VEL/.test(body) || body.length < 30;

const checks = {
  MDBG:        section('MDBG'),
  chardb:      section('chardb (Academia Sinica)'),
  CantoDict:   section('CantoDict (cantonese.org)'),
  CUHK:        section('CUHK (漢語多功能字庫)'),
  hanziyuan:   section('hanziyuan.net'),
  yanbian:     section('小學堂 yanbian (formas)'),
  shangguyin:  section('小學堂 shangguyin (fonologia)'),
};
const present = {}, missing = [];
for (const [k, v] of Object.entries(checks)) {
  present[k] = !unavailable(v);
  if (!present[k]) missing.push(k);
}

// campos-chave
const warnings = [];
if (!/中古音/.test(checks.shangguyin)) warnings.push('sem tabela 中古音 na fonologia');
if (!/(字\s*義|釋義)/.test(checks.chardb)) warnings.push('sem 字義/釋義 no chardb');
if (!/說文/.test(checks.CUHK + checks.yanbian + checks.hanziyuan)) warnings.push('Shuowen (說文) não localizado em nenhuma fonte');

// críticas: MDBG (leituras/def), chardb ou CUHK (definições/Shuowen), shangguyin (fonologia)
const critical = present.MDBG && (present.chardb || present.CUHK) && present.shangguyin;

writeFileSync(`.crawl/clean-${hex}.md`, clean, 'utf8');
const cleanChars = [...clean].length;
const estTokens = Math.round([...clean].reduce((a, ch) => {
  const c = ch.codePointAt(0);
  return a + (c >= 0x2E80 && c <= 0x9FFF ? 1.1 : c < 128 ? 0.26 : 0.5);
}, 0));

console.log(JSON.stringify({
  hex, ok: critical, present, missing, warnings,
  cleanFile: `.crawl/clean-${hex}.md`, estTokens,
}));
process.exit(critical ? 0 : 1);
