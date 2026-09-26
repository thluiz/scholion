# Lote "recovery": falhas de 2026-09-25 recuperadas por Wayback e fxtwitter

Das ~700 falhas do lote dos favoritos, parte tinha conteúdo recuperável por fora do renderizador:

- **Wayback Machine**: páginas mortas, timeouts e vazias (Vida Organizada, Sketchbook, blog do
  Todoist etc.) e parte da família Medium. `recover.ts` baixou a cópia arquivada sem a barra do
  Wayback (`/web/<ts>id_/`), extraiu o artigo com Readability e gravou uma captura `.md`.
- **fxtwitter** (`api.fxtwitter.com`): tweets. Só os com texto ≥ 400 caracteres (threads longas,
  artigos do X) viraram captura; tweet curto ficou como estava.

Resultado em 2026-09-26: **130 itens recuperados** (113 do Wayback, dos quais 23 do medium.com,
18 do Sketchbook e 17 do Vida Organizada, mais 17 tweets). Outros 72 continuaram `failed` com a
tentativa anotada no `reason`: 53 vieram curtos demais, 8 tweets eram privados ou foram apagados, 7
cópias não tinham artigo para o Readability extrair e 1 deu erro de download. As 16 capturas do Vida
Organizada vieram com a acentuação quebrada (charset latin-1 errado no arquivo); foram consertadas no
lugar, e `recover.ts` agora decodifica UTF-8 por conta própria.

Cada captura foi gravada em `C:\Users\conta\OneDrive\MD\<nome>.md` no formato das capturas antigas
(`created` = data do snapshot ou do tweet, `source` = URL original, `archived_copy` /
`fetched_via` no frontmatter). No manifesto, o item que tinha falhado virou `type: "md_file"`,
`status: "pending"`, `pool: "recovery"`, com `recovered_from` e `previous_reason`. A URL original
continua sendo a chave e a fonte da nota.

## Como rodar

Mesma mecânica do `arquivo-kickoff.md` (mesma pasta): orquestrador, três fluxos, `partition.py` e
`merge.py`, o mesmo prompt de worker. Diferenças:

- Particionar com `--pool recovery --type md_file`.
- No prompt do worker, os itens são **md_file**: seguir o pipeline de md_file do playbook (ler a
  captura em `C:\Users\conta\OneDrive\MD\<md_path>`, compor em modo texto com `capturedAt` do
  `created`, **nunca** buscar de novo, mover a captura para `_processed\` ou `_needs_url_review\`).
- A cópia do Wayback pode ter vindo parcial (Medium às vezes corta no "member-only"): se a captura
  for só a introdução de um texto pago, `soft_404`, como sempre.

**Nunca rodar dois orquestradores ao mesmo tempo** (o `merge.py` reescreve o manifesto inteiro). Se
o lote "Arquivo" ainda estiver pendente, rodar os dois pools na mesma sessão, um depois do outro, ou
particionar sem `--pool` para os fluxos pegarem o que houver.

Comando para rodar **os dois pools pendentes (arquivo: 91 url; recovery: 130 md_file) numa sessão só**
(cwd `E:\scholion`), que é o recomendado:

```
Você é o orquestrador dos lotes "arquivo" e "recovery" de webclips. Leia inteiros
E:\scholion\.claude\skills\add-scholion-webclip\parallel\arquivo-kickoff.md (mecânica) e
E:\scholion\.claude\skills\add-scholion-webclip\parallel\recovery-kickoff.md (o que muda para md_file).
Rode os dois pools sem --pool, separando por tipo: fluxos A e B com `--type url`, fluxo C com
`--type md_file` (prompt de md_file). Quando os url acabarem, A e B passam a `--type md_file`.
Comece relatando os pendentes por pool e por tipo.
```

Só o pool "recovery" (cwd `E:\scholion`):

```
Você é o orquestrador do lote "recovery" de webclips. Leia inteiros
E:\scholion\.claude\skills\add-scholion-webclip\parallel\arquivo-kickoff.md (mecânica) e
E:\scholion\.claude\skills\add-scholion-webclip\parallel\recovery-kickoff.md (o que muda) e
orquestre o pool "recovery". Comece relatando quantos itens `pending` com pool "recovery" existem.
```
