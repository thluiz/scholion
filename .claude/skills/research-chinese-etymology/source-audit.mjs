// Usage: node source-audit.mjs <hex> [hex...] [--model NAME] [--concurrency N]
// Audita notas de etimologia CONTRA o dump das fontes (.crawl/clean-<hex>.md):
// fabricação, atribuição errada, glosa interpretativa, tradução distorcida,
// PT-EU. Chama a vox-intelligence (/v1/chat/completions; default gpt-5.4 —
// escolha do autor, sucessor do gpt-5.2 validado no ghost-audit para
// source-or-silence). Grava .crawl/audit-note-<hex>.json e imprime um resumo.
// Read-only sobre as notas: NÃO edita, NÃO comita.
import { readFileSync, writeFileSync, existsSync, readdirSync } from 'fs';

const argv = process.argv.slice(2);
const opt = (flag, def = null) => { const i = argv.indexOf(flag); return i >= 0 ? argv[i + 1] : def; };
const MODEL = opt('--model', 'openrouter/openai/gpt-5.4');
const CONCURRENCY = +opt('--concurrency', '3');
const hexes = argv.filter(a => /^[0-9a-f]{4,5}$/i.test(a)).map(h => h.toLowerCase());
if (!hexes.length) { console.error('Usage: node source-audit.mjs <hex> [hex...] [--model NAME] [--concurrency N]'); process.exit(2); }

const VOX_URL = process.env.VOX_INTELLIGENCE_URL || 'http://localhost:8080/api/vox-intelligence';
const noteFiles = readdirSync('content/notes').filter(f => /^etimologia-de-.*\.md$/.test(f));

const SYSTEM = `Você é auditor de source-or-silence do Scholion. Recebe UMA nota de etimologia chinesa (markdown) e o DUMP bruto das 7 fontes de onde ela DEVE ter saído. Sua tarefa: verificar se cada afirmação factual da nota está sustentada pelo dump.

Reporte APENAS estes tipos de problema:
1. FABRICACAO — afirmação factual (glosa, datação, autoria, reconstrução, número, leitura, forma atestada) que NÃO consta do dump.
2. ATRIBUICAO — dado que existe no dump mas é atribuído à fonte errada (ex.: comentário da CUHK atribuído ao 小學堂; rótulos 略說/詳解/形義通解 são da CUHK, 今按 é do 小學堂).
3. GLOSA_INTERPRETATIVA — interpretação apresentada como dado (ex.: glosar "常用频率: 99999" como frequência "muito alta" — 99999 é sentinela de SEM ranking; inferências fonológicas que nenhuma fonte afirma).
4. TRADUCAO_DISTORCIDA — tradução PT-BR de trecho chinês que muda o sentido do original de forma relevante (traduções fiéis são esperadas e NÃO são problema).
5. PT_EU — português europeu ("facto", "utilizador", "registar", sintaxe lusitana).

NÃO são problemas (NÃO reporte):
- a frase-padrão de abertura ("É o radical Kangxi nº ... Registro filológico...") e o número do radical Kangxi (vem do índice do projeto, não do dump);
- marcadores "(não obtido — ...)" e "(não retornou dados — ...)", inclusive quando a Divergências reformula essa ausência em prosa ("a coluna de X não retornou");
- o bloco sources do frontmatter; links internos; parafrasear/resumir o dump com fidelidade; omissões (a nota não precisa usar tudo do dump);
- reconstruções do 上古音 apresentadas como sílaba única quando o dump separa 聲母 e 韻母 — concatenar os dois campos é apresentação fiel, não fabricação;
- afirmações cross-fonte ("X e Y registram", "confirmado pela CUHK"): verifique na seção da OUTRA fonte; se o dado está lá, não é problema — só reporte se o dado NÃO estiver na fonte invocada;
- rótulos editoriais da nota ("Shuowen (xiaoxue)", "**MDBG**:") — são formatação do verbete, não citação de rótulo do dump.

Para cada problema: quote VERBATIM da nota (copie exatamente), tipo, explicação de 1-2 frases apontando o que o dump diz (ou que nada diz), severity "block" (fabricação/atribuição clara) ou "warn" (caso ambíguo).

Não invente problema para parecer rigoroso; um relatório honesto pode vir vazio.

Responda APENAS com JSON válido, sem cercas de código:
{"verdict":"green"|"yellow"|"red","findings":[{"quote":"...","tipo":"FABRICACAO","severity":"block","detalhe":"..."}],"summary":"1 frase"}
verdict: red se houver qualquer "block"; yellow se só "warn"; green se vazio.`;

async function auditOne(hex) {
  const noteFile = noteFiles.find(f => f.endsWith(`-${hex}.md`));
  if (!noteFile) return { hex, ok: false, reason: 'nota não encontrada' };
  const dumpFile = existsSync(`.crawl/clean-${hex}.md`) ? `.crawl/clean-${hex}.md`
                : existsSync(`.crawl/crawl-${hex}.md`) ? `.crawl/crawl-${hex}.md` : null;
  if (!dumpFile) return { hex, ok: false, reason: 'dump não encontrado' };

  const note = readFileSync(`content/notes/${noteFile}`, 'utf8');
  const dump = readFileSync(dumpFile, 'utf8');
  const user = `===== NOTA (${noteFile}) =====\n${note}\n\n===== DUMP DAS FONTES =====\n${dump}`;

  const ctrl = new AbortController();
  const t = setTimeout(() => ctrl.abort(), 600000);
  let res, data;
  try {
    res = await fetch(`${VOX_URL}/v1/chat/completions`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        model: MODEL,
        temperature: 0,
        messages: [{ role: 'system', content: SYSTEM }, { role: 'user', content: user }],
      }),
      signal: ctrl.signal,
    });
    data = await res.json();
  } catch (err) {
    return { hex, note: noteFile, ok: false, reason: `gateway: ${err.message}` };
  } finally { clearTimeout(t); }
  if (!res.ok) return { hex, note: noteFile, ok: false, reason: data?.error?.message || `HTTP ${res.status}` };

  let content = (data.choices?.[0]?.message?.content || '').trim();
  content = content.replace(/^```(?:json)?\s*\n?/, '').replace(/\n?```\s*$/, '');
  let verdict;
  try { verdict = JSON.parse(content); }
  catch { return { hex, note: noteFile, ok: false, reason: 'resposta não-JSON', head: content.slice(0, 200) }; }

  const out = { hex, note: noteFile, ok: true, model: data.model, ...verdict };
  writeFileSync(`.crawl/audit-note-${hex}.json`, JSON.stringify(out, null, 2), 'utf8');
  return out;
}

// pool de concorrência simples
const queue = [...hexes];
const results = [];
async function worker() {
  while (queue.length) {
    const hex = queue.shift();
    const r = await auditOne(hex);
    results.push(r);
    const tag = !r.ok ? `ERRO (${r.reason})` : r.verdict.toUpperCase() + (r.findings?.length ? ` (${r.findings.length} findings)` : '');
    console.error(`[${results.length}/${hexes.length}] ${r.note || r.hex}: ${tag}`);
  }
}
await Promise.all(Array.from({ length: Math.min(CONCURRENCY, hexes.length) }, worker));

// resumo agregado
const byVerdict = { red: [], yellow: [], green: [], erro: [] };
for (const r of results) (byVerdict[r.ok ? r.verdict : 'erro'] ||= []).push(r);
console.log(JSON.stringify({
  total: results.length,
  red: byVerdict.red.map(r => r.note),
  yellow: byVerdict.yellow.map(r => r.note),
  green: byVerdict.green.length,
  erro: byVerdict.erro.map(r => `${r.hex}:${r.reason}`),
}, null, 2));
