// Usage: node style-audit.mjs [--limit N] [--model NAME] [--concurrency N]
// Passe de NATURALIDADE do português (sem dump — só a nota): calques travados
// ("ao deitarem espiga"), PT-EU gramatical que regex não pega, typos,
// concordância, CJK colado em prosa. NÃO audita conteúdo/fontes (isso é o
// source-audit) e NÃO edita nada — grava relatório em .crawl/style/.
import { readFileSync, writeFileSync, mkdirSync, readdirSync, existsSync } from 'fs';

const argv = process.argv.slice(2);
const opt = (flag, def = null) => { const i = argv.indexOf(flag); return i >= 0 ? argv[i + 1] : def; };
const MODEL = opt('--model', 'openrouter/openai/gpt-5.4');
const CONCURRENCY = +opt('--concurrency', '4');
const LIMIT = opt('--limit') ? +opt('--limit') : Infinity;
const VOX_URL = process.env.VOX_INTELLIGENCE_URL || 'http://localhost:8080/api/vox-intelligence';

mkdirSync('.crawl/style', { recursive: true });

const SYSTEM = `Você é revisor de PORTUGUÊS BRASILEIRO das notas filológicas do Scholion (etimologia de caracteres chineses). Recebe UMA nota markdown. Aponte APENAS problemas de língua, nunca de conteúdo:

1. PT_EU — gramática ou vocabulário de português europeu que soa lusitano ("dever-se ao", mesóclise, "utilizador", ênclise carregada). EXCEÇÃO: "estar a + infinitivo" é válido no idioleto do autor — NÃO aponte.
2. CALQUE_TRAVADO — construção artificial em prosa PT que trava a leitura: calco palavra-a-palavra do chinês/inglês, verbo literário deslocado (ex.: "ao deitarem espiga" para 吐穗), ordem sintática estrangeira.
3. TYPO — erro de ortografia ou acentuação (ex.: "cantonêsas").
4. CONCORDANCIA — erro de concordância ou regência.
5. ESPACO_CJK — caractere chinês colado em palavra latina DENTRO DE PROSA PT (ex.: "sem韻部 preenchido"). NÃO aponte quando o colamento está dentro de citação chinesa verbatim (entre 「」, “”, aspas ou em linha de dados da fonte).

NÃO aponte: escolha de estilo, formatação markdown, terminologia técnica não traduzida (Shuowen, fanqie, 段注, jyutping), traduções fiéis que sejam português gramatical, nem os marcadores padrão "(não obtido — ...)".

Cada achado: "quote" VERBATIM (copie exatamente da nota), "tipo", e "sugestao" com a reescrita mínima. Não invente problema; relatório vazio é um bom relatório.

Responda APENAS com JSON válido, sem cercas:
{"findings":[{"quote":"...","tipo":"CALQUE_TRAVADO","sugestao":"..."}]}`;

async function auditOne(file) {
  const note = readFileSync(`content/notes/${file}`, 'utf8');
  const ctrl = new AbortController();
  const t = setTimeout(() => ctrl.abort(), 600000);
  let res, data;
  try {
    res = await fetch(`${VOX_URL}/v1/chat/completions`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        model: MODEL, temperature: 0,
        messages: [{ role: 'system', content: SYSTEM }, { role: 'user', content: note }],
      }),
      signal: ctrl.signal,
    });
    data = await res.json();
  } catch (err) { return { file, ok: false, reason: err.message }; }
  finally { clearTimeout(t); }
  if (!res.ok) return { file, ok: false, reason: data?.error?.message || `HTTP ${res.status}` };

  let content = (data.choices?.[0]?.message?.content || '').trim()
    .replace(/^```(?:json)?\s*\n?/, '').replace(/\n?```\s*$/, '');
  let parsed;
  try { parsed = JSON.parse(content); }
  catch { return { file, ok: false, reason: 'resposta não-JSON', head: content.slice(0, 150) }; }

  // validar quotes verbatim (anti-alucinação do próprio revisor)
  const findings = (parsed.findings || []).map(f => ({ ...f, verbatim: note.includes(f.quote) }));
  const out = { file, ok: true, model: data.model, findings };
  writeFileSync(`.crawl/style/style-${file}.json`, JSON.stringify(out, null, 2), 'utf8');
  return out;
}

const files = readdirSync('content/notes')
  .filter(f => /^etimologia-de-.*\.md$/.test(f))
  .filter(f => !existsSync(`.crawl/style/style-${f}.json`))  // resumível
  .slice(0, LIMIT);

console.error(`style-audit: ${files.length} notas (${MODEL})`);
const queue = [...files]; const results = [];
async function worker() {
  while (queue.length) {
    const f = queue.shift();
    const r = await auditOne(f);
    results.push(r);
    const tag = !r.ok ? `ERRO (${r.reason})` : r.findings.length ? `${r.findings.length} achados` : 'limpa';
    console.error(`[${results.length}/${files.length}] ${r.file}: ${tag}`);
  }
}
await Promise.all(Array.from({ length: Math.min(CONCURRENCY, files.length) }, worker));

const withFindings = results.filter(r => r.ok && r.findings.length);
console.log(JSON.stringify({
  total: results.length,
  limpas: results.filter(r => r.ok && !r.findings.length).length,
  comAchados: withFindings.length,
  totalFindings: withFindings.reduce((a, r) => a + r.findings.length, 0),
  erros: results.filter(r => !r.ok).map(r => `${r.file}:${r.reason}`),
}, null, 1));
