# Scripts da skill `research-chinese-etymology`

Todos em `E:/scholion/.claude/skills/research-chinese-etymology/`. **cwd obrigatório: `E:/scholion`** — os scripts usam caminhos relativos (`content/notes/`, `.crawl/`). `.crawl/` é ignorado pelo git; criar com `mkdir -p .crawl` na primeira vez.

Dependências: Node (sem pacotes) para os determinísticos; Playwright global (`npm install -g playwright`, browsers em `C:\Users\conta\AppData\Local\ms-playwright\`) para os que abrem navegador; vox-intelligence (`http://localhost:8080/api/vox-intelligence`, override por `VOX_INTELLIGENCE_URL`) para os que chamam LLM. Modelo para gerar/auditar: `openrouter/openai/gpt-5.4` (memória `feedback_modelos_etimologia`; deepseek e `claude -p` rejeitados).

## Pipeline principal (um caractere)

| Passo | Comando | O que faz | Precisa de |
|---|---|---|---|
| 0 | `node .claude/skills/research-chinese-etymology/check-exists.mjs <CHAR…> [--json]` | Diz se já existe nota dedicada (`EXISTS`/`MISSING`), avisa `DUPLICATE`, lista `embedded` (seções em notas compostas) e `related` (títulos que citam o caractere) em `content/notes/` e `content/research/`. Sempre antes de qualquer fetch. | Node |
| 1 | `node .claude/skills/research-chinese-etymology/crawl-radical.mjs <CHAR> > .crawl/crawl-<hex>.md` | Coleta as 7 consultas (6 sites) em **sequência** num dump markdown com cabeçalho `## <fonte>`. Fonte que falhou vem marcada `(FONTE INDISPONÍVEL — …)`. Determinístico, sem LLM. Apesar do nome, serve para qualquer caractere. | Playwright |
| 2 | `node .claude/skills/research-chinese-etymology/audit-crawl.mjs <hex>` | Limpa ruído de navegação do dump e grava `.crawl/clean-<hex>.md`; imprime veredito JSON (`present`, `missing`, `warnings`, `estTokens`). Exit 1 se faltar fonte crítica (MDBG, chardb ou CUHK, shangguyin). | Node |
| 3a | compor a nota a partir de `.crawl/clean-<hex>.md` | Fluxo interativo (caractere de nome kung fu, *Hai Tong*, avulso): ler o dump limpo e redigir conforme `references/formato-nota.md`. | — |
| 3b | `node .claude/skills/research-chinese-etymology/generate-note.mjs <CHAR> <radicalNum> <hex> [model]` | Só para **radicais Kangxi**: envia dump + gabarito ao preset `scholion/etymology-note` e grava `content/notes/<slug>.md`. Exige número do radical; a abertura gerada é a de radical. Não builda nem comita. | vox-intelligence |
| 4 | `node .claude/skills/research-chinese-etymology/lint-notes.mjs [--fix] [--quiet]` | Lint determinístico de todas as `etimologia-de-*`: léxico PT-EU → PT-BR (corrige com `--fix`), "cantonêsa", CJK colado em prosa e "note-se" (só reporta). | Node |

## Batch de radicais

| Comando | O que faz |
|---|---|
| `node .claude/skills/research-chinese-etymology/run-radicals.mjs [--limit N] [--only 字字] [--model NAME] [--no-commit]` | Driver dos radicais Kangxi: worklist = radicais do índice `os-214-radicais-kangxi.md` sem nota (audit por título) menos os primitivos parqueados (`PARK`); por caractere, crawl → audit → generate; um `hugo` build; commit por nota e push. Resumível. Log em `.crawl/run.log`. O `git commit` roda por dentro do node, fora do gate ghost-audit do Bash tool. |
| `node .claude/skills/research-chinese-etymology/regen-notes.mjs <hex…> [--model NAME] [--no-commit]` | Regenera notas de radicais existentes (pós-auditoria): audit → generate; se o slug mudou, `git rm` do antigo no mesmo commit `fix:`. Log em `.crawl/regen.log`. |

## Auditoria (read-only, LLM)

| Comando | O que faz |
|---|---|
| `node .claude/skills/research-chinese-etymology/source-audit.mjs <hex…> [--model NAME] [--concurrency N]` | Nota **contra o dump** (`.crawl/clean-<hex>.md`): fabricação, atribuição errada, glosa interpretativa, tradução distorcida, PT-EU. Grava `.crawl/audit-note-<hex>.json`. É triagem, não veredito: conferir amostra contra o dump antes de agir (falsos positivos conhecidos: marcador de Zhengzhang, campo 普通話 da CUHK, concatenação 聲母+韻母). |
| `node .claude/skills/research-chinese-etymology/style-audit.mjs [--limit N] [--model NAME] [--concurrency N]` | Naturalidade do PT-BR (sem dump): calques, PT-EU gramatical, typos, concordância, CJK colado. Relatório em `.crawl/style/`. Usar como minerador de padrões para o `LEXICON` do lint, não como lista de fixes; nunca "corrigir" citação chinesa verbatim. |

## Glossário dos primitivos de traço

| Comando | O que faz |
|---|---|
| `node .claude/skills/research-chinese-etymology/glossary-entry.mjs <CHAR> <radicalNum> <hex> [model]` | Um verbete compacto (fragmento sem frontmatter) em `.crawl/gloss/entry-<num>-<hex>.md`, a partir de `.crawl/clean-<hex>.md`. |
| `node .claude/skills/research-chinese-etymology/glossary-batch.mjs [--force 字字]` | Gera os verbetes de todos os primitivos `PARK` sem fragmento; sequencial. |
| `node .claude/skills/research-chinese-etymology/assemble-glossary.mjs [--out <path>]` | Monta `content/notes/glossario-dos-radicais-primitivos.md` a partir dos fragmentos. Determinístico. |

## Fallback manual (só se o crawler ou o Playwright falharem)

| Comando | Fonte |
|---|---|
| `node .claude/skills/research-chinese-etymology/fetch-hanziyuan.mjs <CHAR>` | hanziyuan.net |
| `node .claude/skills/research-chinese-etymology/fetch-xiaoxue-yanbian.mjs <CHAR>` | 小學堂 yanbian |
| `node .claude/skills/research-chinese-etymology/fetch-xiaoxue-shangguyin.mjs <CHAR>` | 小學堂 shangguyin |
| WebFetch nas URLs de `references/fontes-etimologia.md` | MDBG, chardb (2 passos), CantoDict, CUHK |

Os três scripts cospem o `innerText` da página inteira. Regra de serialização: os dois xiaoxue nunca juntos; hanziyuan pode correr com um deles; WebFetches um de cada vez. Não gerar scripts novos em runtime.
