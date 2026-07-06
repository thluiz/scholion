// Usage: node generate-note.mjs <char> <radicalNum> <hex> [model]
// Lê .crawl/clean-<hex>.md (fallback crawl-<hex>.md), monta o prompt com as
// regras + o modelo (nota de 水) + o dump, chama `claude -p` isolado, e grava
// content/notes/<slug>.md. Emite veredito JSON. NÃO builda nem comita.
import { readFileSync, writeFileSync, existsSync } from 'fs';
import { spawnSync } from 'child_process';
import { tmpdir } from 'os';

// timestamp local com offset (ex.: 2026-07-05T14:03:22+01:00), sem shell
function isoWithOffset(d = new Date()) {
  const pad = n => String(n).padStart(2, '0');
  const off = -d.getTimezoneOffset();
  const sign = off >= 0 ? '+' : '-';
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}` +
         `T${pad(d.getHours())}:${pad(d.getMinutes())}:${pad(d.getSeconds())}` +
         `${sign}${pad(Math.floor(Math.abs(off) / 60))}:${pad(Math.abs(off) % 60)}`;
}

const [char, numArg, hexArg, model] = process.argv.slice(2);
if (!char || !numArg || !hexArg) {
  console.error('Usage: node generate-note.mjs <char> <radicalNum> <hex> [model]');
  process.exit(2);
}
const N = numArg, hex = hexArg.toLowerCase();

const dumpFile = existsSync(`.crawl/clean-${hex}.md`) ? `.crawl/clean-${hex}.md`
              : existsSync(`.crawl/crawl-${hex}.md`) ? `.crawl/crawl-${hex}.md` : null;
if (!dumpFile) { console.log(JSON.stringify({ char, ok: false, reason: 'dump inexistente' })); process.exit(1); }
const dump = readFileSync(dumpFile, 'utf8');
const gabarito = readFileSync('content/notes/etimologia-de-seoi-shui-6c34.md', 'utf8');
const ts = isoWithOffset();

const prompt = `Você é um filólogo que redige UMA nota de etimologia de caractere chinês para o Scholion, em PORTUGUÊS BRASILEIRO, a partir de DADOS BRUTOS de 7 fontes. Replique EXATAMENTE o formato do MODELO (mesmas seções ####, tabela de evolução, bloco de fonologia, seção final "Divergências entre fontes").

REGRAS INEGOCIÁVEIS:
- Source-or-silence: só afirme o que está nos DADOS. Campo sem dado → "(não obtido — <motivo>)". NUNCA invente datação, glosa, autoria ou reconstrução fonológica.
- Verbatim: definições do chardb (字義) e o texto do 說文 (Shuowen) em chinês original + tradução PT-BR entre parênteses. Transcreva TODAS as acepções numeradas do chardb.
- PT-BR (não PT-EU): registrar, seção, arquivo, caractere, tênue. Não traduza termos técnicos (Shuowen, fanqie, 段注, 中古音, 上古音).
- NÃO editorialize e NÃO vincule a kung fu/linhagem: registro filológico puro.
- Traduza dinastias/scripts/artefatos na tabela de formas. Traduza fonologia: 攝→division, 韻→rhyme, 聲→tone, 母→initial, 反切→fanqie, 等→grade, 開→open, 合→closed, 平→level, 上→rising, 去→departing, 入→entering, 全清→totalmente surda, 次清→aspirada surda, 次濁→sonorante, 全濁→sonora plena.
- Contagem de caracteres derivados: se os DADOS não a trazem, OMITA essa cláusula da abertura (não escreva "não obtido" para ela).
- 段注 (Duan Yucai) quase nunca vem no dump: marque "(não obtido — shuowen.org retornou listagem; zdic.net retornou HTTP 404)".
- 鄭張尚芳 (Zhengzhang) ausente da tabela → "(não retornou dados — ausente da tabela do 小學堂)".

FRONTMATTER: idêntico ao MODELO, com date: '${ts}' exatamente. summary sempre entre aspas simples.
ABERTURA: "É o radical Kangxi nº ${N} (${char}, <glosa curta>). <variante do radical, se houver, ex.: 'Como radical à esquerda, assume a forma X.'> Registro filológico, sem vínculo a nome kung fu. Ver [Os 214 radicais Kangxi](/notes/os-214-radicais-kangxi/)."
Linha de identificação após a abertura: "**${char}** — U+${hex.toUpperCase()} · 部首 radical: ... · 總筆畫 strokes: ... · 注音 zhuyin: ... · 拼音 pinyin: ... / jyutping: ..." (preencha com os DADOS).

CARACTERE-ALVO: ${char} · radical Kangxi nº ${N} · U+${hex.toUpperCase()}

SAÍDA (CRÍTICO — obedeça):
- NÃO use ferramentas. NÃO explique. NÃO comente antes nem depois.
- 1ª linha, exatamente: SLUG: etimologia-de-<jyutping-sem-tom>-<pinyin-sem-diacrítico-sem-tom>-${hex}
- 2ª linha: em branco.
- Da 3ª linha em diante: a nota completa, começando em "---" (frontmatter) e terminando na seção "#### Divergências entre fontes". Nada além da nota.

===== MODELO (replicar o formato EXATAMENTE) =====
${gabarito}

===== DADOS BRUTOS (7 fontes; texto verbatim) =====
${dump}`;

const args = ['-p'];
if (model) args.push('--model', model);
const res = spawnSync('claude', args, {
  input: prompt, encoding: 'utf8', cwd: tmpdir(), shell: true,
  maxBuffer: 32 * 1024 * 1024, timeout: 600000,
});
if (res.status !== 0 || !res.stdout) {
  console.log(JSON.stringify({ char, ok: false, reason: `claude -p falhou (status ${res.status})`, stderr: (res.stderr || '').slice(0, 400) }));
  process.exit(1);
}
const raw = res.stdout;

// parse: SLUG na 1ª linha; nota a partir do primeiro "---"
const slugMatch = raw.match(/SLUG:\s*(etimologia-de-[a-z]+-[a-z]+-[0-9a-f]+)/i);
const fmStart = raw.indexOf('\n---');
const firstDash = raw.startsWith('---') ? 0 : (fmStart >= 0 ? fmStart + 1 : -1);
if (!slugMatch || firstDash < 0) {
  console.log(JSON.stringify({ char, ok: false, reason: 'saída sem SLUG válido ou sem frontmatter', head: raw.slice(0, 300) }));
  process.exit(1);
}
const slug = slugMatch[1].toLowerCase();
let note = raw.slice(firstDash).trim();
// remover cercas de código acidentais
note = note.replace(/^```[a-z]*\n/, '').replace(/\n```$/, '').trim() + '\n';

// validações mínimas
const errs = [];
if (!note.startsWith('---')) errs.push('não começa com frontmatter');
if (!/#### Divergências entre fontes/.test(note)) errs.push('sem seção Divergências');
if (!/^title:\s*"/m.test(note)) errs.push('sem title');
if (!/^date:\s*'/m.test(note)) errs.push('sem date com aspas simples');
if (!/^summary:\s*['"]/m.test(note)) errs.push('summary sem aspas');
if (errs.length) {
  console.log(JSON.stringify({ char, slug, ok: false, reason: 'validação falhou: ' + errs.join('; '), head: note.slice(0, 300) }));
  process.exit(1);
}

const file = `content/notes/${slug}.md`;
writeFileSync(file, note, 'utf8');
console.log(JSON.stringify({ char, slug, ok: true, file, bytes: Buffer.byteLength(note, 'utf8') }));
