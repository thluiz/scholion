---
name: add-scholion-note
description: Cria uma nova nota no Scholion (E:/scholion/content/notes/) com schema completo (sources estruturadas, has_commentary). Recebe título, corpo e fonte(s). Pergunta o que faltar.
argument-hint: "[título] | [corpo] | [fonte]"
---

Cria uma nota genérica no **Scholion** em `E:/scholion/content/notes/<slug>.md`.

Pipeline comum em `references/note-pipeline.md` (passos 1–14). Esta skill só descreve o que é específico da nota genérica.

## Parâmetros

`$ARGUMENTS` em formato livre. Extrair:
- **título** — string curta (idealmente ≤ 72 chars).
- **corpo** — markdown.
- **fonte(s)** — URL(s) ou referência(s); várias separadas por linha ou ` · `.

Se algum dos três faltar, perguntar antes de continuar.

## Processo

1. **Search-first interativo** — pipeline passo 6 (buscar → listar → esperar).
2. **Carregar ghost-writer** — ler `ghost-writer/SKILL.md` antes de compor; a checklist é filtro durante a escrita, não revisão posterior.
3. **Hora real** — pipeline passo 1.
4. **Slug** — pipeline passo 2.
5. **Tags** — 2–4, kebab-case, no idioma da nota.
6. **Summary** — uma frase (~150–200 chars) com o ponto da nota; aparece nos cards.
7. **has_commentary** — `true` se há texto/análise/conexão original do autor; `false` se é só excerto/glosa de fonte externa. Na dúvida, `false`.
8. **sources** — pipeline passo 4. Nota genérica **sem** `category`.
9. **Compor o draft** no formato abaixo, com YAML conforme pipeline passo 3 e links conforme passo 5.
10. **Portão** — pipeline passo 7 (`/ghost-audit <scratchpad>/<slug>.md`).
11. **Preview** — pipeline passo 8, sem exceção.
12. **Write → `/style-test`** — pipeline passo 9.
13. **Marcador, commit, push** — pipeline passos 10, 11 e 13 (build: passo 12, uma vez por sessão).

## Formato do arquivo

```markdown
---
title: "<título>"
date: <YYYY-MM-DDTHH:MM:SS±HH:MM>
summary: "<frase curta>"
tags: ["tag1", "tag2"]
has_commentary: <true|false>
sources:
  - title: "..."
    url: "..."
    kind: "..."
---

<corpo em markdown>
```

## Regras

- **Voz e estilo**: corpo segue todas as regras de `ghost-writer` (vocabulário, estrutura e tom banidos, checklist). Notas são curtas; o filtro se aplica igual.
- **Source-or-silence**: toda afirmação factual precisa de fonte inline. Sem fonte atestada, omitir e avisar o autor no chat; nunca escrever na nota que a fonte não foi encontrada.
- Sem `Co-Authored-By` no commit (pipeline passo 11).
- Silvae congelado para notas (pipeline passo 14).
