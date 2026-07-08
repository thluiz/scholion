// Usage: node glossary-entry.mjs <char> <radicalNum> <hex> [model]
// Gera UM verbete COMPACTO de glossário (fragmento markdown, sem frontmatter)
// para um radical primitivo de traço, a partir de .crawl/clean-<hex>.md.
// Grava .crawl/gloss/entry-<num>-<hex>.md. Mesmas regras de fonte das notas.
import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'fs';

const [char, numArg, hexArg, model] = process.argv.slice(2);
if (!char || !numArg || !hexArg) { console.error('Usage: node glossary-entry.mjs <char> <radicalNum> <hex> [model]'); process.exit(2); }
const hex = hexArg.toLowerCase();
const MODEL = model || 'openrouter/openai/gpt-5.4';
const VOX_URL = process.env.VOX_INTELLIGENCE_URL || 'http://localhost:8080/api/vox-intelligence';

const dumpFile = existsSync(`.crawl/clean-${hex}.md`) ? `.crawl/clean-${hex}.md`
              : existsSync(`.crawl/crawl-${hex}.md`) ? `.crawl/crawl-${hex}.md` : null;
if (!dumpFile) { console.log(JSON.stringify({ char, ok: false, reason: 'dump inexistente' })); process.exit(1); }
mkdirSync('.crawl/gloss', { recursive: true });

const SYSTEM = `Você é um filólogo que redige UM VERBETE COMPACTO de glossário para um radical Kangxi primitivo (traço/componente gráfico que não é caractere pleno de uso corrente), em PORTUGUÊS BRASILEIRO, a partir de DADOS BRUTOS de 7 fontes.

REGRAS INEGOCIÁVEIS (as mesmas das notas de etimologia do Scholion):
- Source-or-silence: só afirme o que está nos DADOS. Sem dado → omita a linha (verbete compacto NÃO usa "(não obtido)", salvo para o Shuowen, que é obrigatório). NUNCA invente glosa, leitura, datação ou autoria.
- Verbatim: o texto do 說文 em chinês original + tradução PT-BR entre parênteses. Se o dump tiver mais de uma versão, use a mais completa e NÃO as misture.
- Atribuição por seção do dump: 略說/詳解/形義通解 = CUHK; 今按 = 小學堂. Nunca troque.
- Tons: só o número (ex.: gwan2). Nunca descreva contorno/altura.
- Cada fonte fala por si; NÃO escreva "confirmado por X".
- hanziyuan "常用频率: 99999" = sem ranking; não mencione frequência nesse caso.
- PT-BR (não PT-EU). Não traduza termos técnicos (Shuowen, fanqie, 部首).
- NÃO editorialize; registro filológico puro, seco.
- Paleografia e Como radical: redija em PROSA PT-BR (citações chinesas verbatim são bem-vindas, com atribuição). Metadados de indexação NÃO são conteúdo: "Component X", "Stroke type...", "radical in Chinese characters", "Kangxi N", "說文‧X部" sozinho. Se o que sobra da linha é só isso — mesmo entre aspas e com atribuição — OMITA a linha inteira. Verbete raso com só identificação + Glosa + 說文 é um bom verbete.
- Linha de identificação: pinyin com diacríticos como grafado no MDBG; jyutping só com número de tom. Não misture formatos.
- Pontuação ocidental na prosa PT (dois-pontos ":", não "："); a pontuação chinesa fica só dentro das citações verbatim.

FORMATO DO VERBETE (exatamente esta estrutura; omita linha sem dado):
### <char> — radical <num> (<pinyin sem tom se atestado>)

**<char>** — U+<HEX> · 總筆畫 strokes: <n> · 拼音 pinyin: <...> · jyutping: <...>

**Glosa**: <definições curtas do MDBG/chardb, 1 linha>

**說文**: <verbatim chinês>. (<tradução PT-BR>) — ou, se ausente: **說文**: (não obtido — <motivo conforme o dump>)

**Paleografia**: <1-2 frases da CUHK/小學堂 com atribuição, SÓ se atestado>

**Como radical**: <em que caracteres aparece / função, SÓ se os dados trouxerem>

SAÍDA: APENAS o verbete markdown, começando em "### ". Sem comentários, sem cercas de código.`;

const dump = readFileSync(dumpFile, 'utf8');
const user = `CARACTERE-ALVO: ${char} · radical Kangxi nº ${numArg} · U+${hex.toUpperCase()}\n\n===== DADOS BRUTOS (7 fontes) =====\n${dump}`;

async function call(messages) {
  const ctrl = new AbortController();
  const t = setTimeout(() => ctrl.abort(), 600000);
  try {
    const res = await fetch(`${VOX_URL}/v1/chat/completions`, {
      method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ model: MODEL, temperature: 0.2, messages }),
      signal: ctrl.signal,
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data?.error?.message || `HTTP ${res.status}`);
    return data.choices?.[0]?.message?.content?.trim() || '';
  } finally { clearTimeout(t); }
}

const messages = [{ role: 'system', content: SYSTEM }, { role: 'user', content: user }];
let entry;
try {
  entry = await call(messages);
  entry = entry.replace(/^```[a-z]*\n/, '').replace(/\n```$/, '').trim();
  if (!entry.startsWith('### ')) {
    // um repair round-trip
    entry = (await call([...messages,
      { role: 'assistant', content: entry },
      { role: 'user', content: 'Sua resposta violou o contrato: comece exatamente em "### " e envie APENAS o verbete markdown.' },
    ])).replace(/^```[a-z]*\n/, '').replace(/\n```$/, '').trim();
  }
} catch (err) {
  console.log(JSON.stringify({ char, ok: false, reason: err.message })); process.exit(1);
}
if (!entry.startsWith('### ') || !/說文/.test(entry)) {
  console.log(JSON.stringify({ char, ok: false, reason: 'verbete sem contrato (### / 說文)', head: entry.slice(0, 150) })); process.exit(1);
}
const file = `.crawl/gloss/entry-${String(numArg).padStart(3, '0')}-${hex}.md`;
writeFileSync(file, entry + '\n', 'utf8');
console.log(JSON.stringify({ char, ok: true, file, bytes: Buffer.byteLength(entry, 'utf8') }));
