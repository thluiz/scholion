---
name: research-chinese-etymology
description: Pesquisa etimologia de caracteres chineses em 6 fontes (MDBG, chardb e 小學堂 da Academia Sinica, CantoDict, hanziyuan.net, 漢語多功能字庫 da CUHK) via crawler determinístico, um caractere de cada vez. Checa com check-exists.mjs se a nota já existe antes de qualquer fetch. Grava `etimologia-de-<jyutping>-<pinyin>-<hex>.md` no Scholion após preview aprovado, em PT-BR.
argument-hint: "[caracteres] ex: 知友士"
---

# Pesquisa Etimológica de Caracteres Chineses

Recebe um ou mais caracteres, coleta as fontes com o crawler, compõe a nota a partir do dump limpo e grava em `E:/scholion/content/notes/` após preview aprovado. Não comita (o commit fica com o autor ou com a skill orquestradora).

Referências desta skill (ler as que o passo pede):
- `references/fontes-etimologia.md` — fontes, URLs, gotchas, serialização, bloco `sources`, título e slug. Comum a `kung-fu-name-etymology` e `transfer-etymology-from-scholion`.
- `references/formato-nota.md` — template da nota, frontmatter, aberturas, regra editorial.
- `references/traducao.md` — regras de citação, glossários de fonologia e períodos, datação sem fonte.
- `references/scripts.md` — uso de cada `.mjs`.

**cwd = `E:/scholion`** em todos os comandos (os scripts usam caminhos relativos). Todos os comandos abaixo pressupõem `cd E:/scholion`.

## Parâmetros

Extrair os caracteres CJK de `$ARGUMENTS` (1 ou mais, ex.: `德`, `知友士`). Sem caractere CJK, perguntar.

## Passo 0 — pré-verificação (antes de QUALQUER fetch)

```
node .claude/skills/research-chinese-etymology/check-exists.mjs <CHARS>
```

Por caractere:
- `EXISTS <path>` — mostrar ao autor o caminho e o título e perguntar: **retomar** (ler a nota e seguir dali), **atualizar** (refazer a pesquisa e sobrescrever) ou **pular**. Não decidir sozinho; não pesquisar antes da resposta.
- `DUPLICATE` — avisar que há mais de uma nota dedicada e listar as duas; não criar uma terceira. Qual fica é decisão do autor.
- `embedded: …` — o caractere tem seção dentro de uma nota composta; dizer ao autor, que decide se extrai ou se pesquisa do zero.
- `related: …` — candidatos a link na abertura; listar.
- `MISSING` — seguir para o passo 1.

## Passo 1 — contexto

A menos que a skill orquestradora já tenha passado: perguntar de qual nome kung fu, expressão do *Hai Tong* ou radical o caractere vem, e qual a pessoa. Aceitar "nenhum" (registro sem vínculo). Isso define a abertura e as tags (`references/formato-nota.md`).

## Passo 2 — coleta (um caractere de cada vez)

Regra serial (memória `feedback_etimologia_serial_e_completa`): **nunca dois caracteres ao mesmo tempo**, nunca subagents paralelos por caractere. Dentro do caractere, fetches em sequência — o crawler já faz isso. Terminar o caractere em curso (até a gravação) antes de começar o próximo.

```
mkdir -p .crawl
node .claude/skills/research-chinese-etymology/crawl-radical.mjs <CHAR> > .crawl/crawl-<hex>.md
node .claude/skills/research-chinese-etymology/audit-crawl.mjs <hex>
```

`<hex>` = codepoint em minúsculas (`check-exists.mjs` imprime `U+XXXX`). O audit grava `.crawl/clean-<hex>.md` e imprime JSON: `ok`, `present`, `missing`, `warnings`. Se `ok: false` (falta MDBG, chardb/CUHK ou shangguyin), reportar ao autor antes de prosseguir — pode ser indisponibilidade momentânea; repetir o crawl uma vez após alguns minutos antes de aceitar a lacuna.

**Fallback manual** (só se o crawler ou o Playwright falharem): `fetch-hanziyuan.mjs`, `fetch-xiaoxue-yanbian.mjs`, `fetch-xiaoxue-shangguyin.mjs` e WebFetch nas URLs de `references/fontes-etimologia.md`, nas mesmas regras de serialização. Não fazer WebFetch manual quando o crawler funcionou.

## Passo 3 — composição

Ler `.crawl/clean-<hex>.md` inteiro (não amostrar) e redigir a nota conforme `references/formato-nota.md` e `references/traducao.md`:

- dados só do dump; fonte marcada `(FONTE INDISPONÍVEL)` é fonte não consultada — sai do `sources`;
- pinyin do MDBG, jyutping do CantoDict; nunca a romanização do clã como pronúncia;
- "Divergências entre fontes" dentro da nota, com o tamanho que o caractere pedir — não comprimir prosa para economizar contexto;
- sem interpretação do kung fu fora da frase de abertura.

`generate-note.mjs` (preset `scholion/etymology-note`) só serve para radicais Kangxi — exige número do radical e gera abertura de radical. Para os demais caracteres, a composição é aqui.

## Passo 4 — preview e gravação

1. Mostrar a nota completa (frontmatter + corpo) ao autor. Aguardar aprovação explícita (memória `feedback_preview_antes_de_salvar`).
2. Timestamp real: `date +"%Y-%m-%dT%H:%M:%S%:z"`. Nunca inventar hora.
3. Slug: `etimologia-de-<jyutping-sem-tom>-<pinyin-sem-tom>-<hex>.md` (regra completa em `references/fontes-etimologia.md`). Rodar `check-exists.mjs` de novo se a sessão for longa — outra sessão pode ter criado a nota.
4. `Write` em `E:/scholion/content/notes/<slug>.md`; confirmar com `ls` ou `Read` antes de dizer que gravou.
5. `node .claude/skills/research-chinese-etymology/lint-notes.mjs --quiet` e corrigir o que apontar na nota nova.
6. Não comitar. Se o autor pedir commit: um commit por nota, mensagem `note: etimologia de <CHAR>`, sem `Co-Authored-By`. O gate ghost-audit vai rodar; findings se mostram ao autor, override consciente só com decisão dele (memória `feedback_ghost_audit_gate_estrito`).

## Anti-alucinação

Nada inventado. Campo sem dado leva `(não obtido — <motivo>)` ou `(não retornou dados — <motivo>)` — convenção atual, ver "Marcadores" em `references/fontes-etimologia.md`. Identificadores de corpus (甲903, 璽彙1598) e reconstruções copiados dígito a dígito. Datação histórica só com fonte (`references/traducao.md`). Caracteres tardios têm lacunas legítimas; não forçar.

## Regra editorial

Nota de etimologia é referência objetiva: sem bullets interpretando o ideograma no contexto da linhagem, do nome do discípulo ou do kung fu. A abertura só identifica a origem. Exemplos do que não entra em `references/formato-nota.md`.

## Interativo vs. batch

- **Interativo (esta skill)**: caracteres de nomes kung fu, do *Hai Tong* ou avulsos; 1 a poucos caracteres; preview por nota; composição no contexto.
- **Batch (`run-radicals.mjs`)**: só para a worklist dos radicais Kangxi (índice `os-214-radicais-kangxi.md`); geração via vox-intelligence com `gpt-5.4`, commit por nota e push por dentro do script. Depois do batch: `source-audit.mjs` como triagem e `lint-notes.mjs`. Nunca `claude -p` nem deepseek (memória `feedback_modelos_etimologia`). Detalhes em `references/scripts.md`.

## Notas

- Pode ser invocada por `kung-fu-name-etymology`; com contexto já fornecido, não perguntar de novo.
- Lint de língua: não há glossário PT-EU aqui — a lista está em `lint-notes.mjs`.
- Playwright global em `C:\Users\conta\AppData\Local\ms-playwright\`; se faltar, avisar e cair no fallback WebFetch-only (MDBG, chardb, CantoDict, CUHK), marcando no preview quais fontes ficaram de fora.
