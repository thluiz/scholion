// Usage: node crawl-radical.mjs <character>
// Coleta os dados brutos de todas as fontes etimológicas para UM caractere e
// emite um dump estruturado (markdown) em stdout. Determinístico, sem LLM.
// Fonte indisponível é marcada, não interrompe o crawl (source-or-silence).
import { chromium } from 'playwright';

const char = process.argv[2];
if (!char) { console.error('Usage: node crawl-radical.mjs <character>'); process.exit(1); }

const cp = char.codePointAt(0).toString(16);
const NAV = { waitUntil: 'networkidle', timeout: 30000 };
const SETTLE = 2500;

const browser = await chromium.launch();
const ctx = await browser.newContext({
  userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36',
});

async function grab(url, { settle = SETTLE, selector = 'body' } = {}) {
  const page = await ctx.newPage();
  try {
    await page.goto(url, NAV);
    await page.waitForTimeout(settle);
    const text = await page.innerText(selector);
    return text.trim();
  } catch (e) {
    return `(FONTE INDISPONÍVEL — ${e.message.split('\n')[0]})`;
  } finally {
    await page.close();
  }
}

// chardb: 2 passos — busca → 1º link /char/<ID> → página do caractere
async function chardb() {
  const page = await ctx.newPage();
  try {
    await page.goto(`https://chardb.iis.sinica.edu.tw/search.jsp?stype=1&q=${char}`, NAV);
    await page.waitForTimeout(SETTLE);
    // O link do resultado é o anchor cujo texto é exatamente o caractere buscado
    // (os outros /char/ links são barra lateral de caracteres comuns/similares).
    const href = await page.$$eval('a[href*="/char/"]', (as, ch) => {
      const exact = as.find(a => a.textContent.trim() === ch);
      return exact ? exact.getAttribute('href') : null;
    }, char);
    if (!href) { await page.close(); return '(chardb: nenhum resultado com texto == caractere na busca)'; }
    const id = href.match(/\/char\/([^/?#]+)/)?.[1];
    const abs = href.startsWith('http') ? href : `https://chardb.iis.sinica.edu.tw/char/${id}`;
    await page.goto(abs, NAV);
    await page.waitForTimeout(SETTLE);
    const text = await page.innerText('body');
    await page.close();
    return `charID: ${id}\nURL: ${abs}\n\n${text.trim()}`;
  } catch (e) {
    await page.close().catch(() => {});
    return `(FONTE INDISPONÍVEL — ${e.message.split('\n')[0]})`;
  }
}

const sources = {
  'MDBG':               () => grab(`https://www.mdbg.net/chinese/dictionary?wdqb=${char}`),
  'chardb (Academia Sinica)': chardb,
  'CantoDict (cantonese.org)': () => grab(`https://www.cantonese.org/search.php?q=${char}`),
  'CUHK (漢語多功能字庫)':   () => grab(`https://humanum.arts.cuhk.edu.hk/Lexis/lexi-mf/search.php?word=${char}`),
  'hanziyuan.net':      () => grab(`https://hanziyuan.net/#${char}`, { settle: 3500 }),
  '小學堂 yanbian (formas)': () => grab(`https://xiaoxue.iis.sinica.edu.tw/yanbian?char=${char}`),
  '小學堂 shangguyin (fonologia)': () => grab(`https://xiaoxue.iis.sinica.edu.tw/shangguyin?char=${char}`),
};

// Serial — nunca paralelizar fetches (evita abuso dos mesmos sites)
const out = [`# Crawl: ${char} (U+${cp.toUpperCase()})`, ''];
for (const [name, fn] of Object.entries(sources)) {
  const body = await fn();
  out.push(`## ${name}`, '', body, '');
}
await browser.close();
console.log(out.join('\n'));
