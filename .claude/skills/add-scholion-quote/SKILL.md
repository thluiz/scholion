---
name: add-scholion-quote
description: "Cria uma nota de citação (category: quote) no Scholion a partir de uma frase e autor presumido: rastreia autoria em Quote Investigator/Wikiquote, documenta paráfrases e atribuições erradas, gera nota com tag do autor. Use quando o usuário colar uma frase/citação e perguntar quem disse ou pedir para guardar."
argument-hint: "[frase] | [autor presumido]"
---

Cria uma nota de **citação verificada** (`category: quote`) no **Scholion** em `E:/scholion/content/notes/<slug>.md`.

Pipeline comum em `add-scholion-note/references/note-pipeline.md` (passos 1–14). Aqui só o que é específico da citação.

## Parâmetros

`$ARGUMENTS` em formato livre. Extrair:
- **frase** — a citação ou paráfrase que o usuário passou.
- **autor presumido** — quem o usuário acredita ser o autor.

Se algum dos dois faltar, perguntar antes de continuar.

## Processo

### 1. Search-first interativo

Pipeline passo 6: buscar pela frase, pelo autor presumido e por temas adjacentes; listar; esperar o autor apontar.

### 2. Carregar ghost-writer

Ler `ghost-writer/SKILL.md` antes de compor o contexto de autoria.

### 3. Pesquisa de autoria

Usar `WebSearch` e `WebFetch`. Consultar obrigatoriamente:

1. **Quote Investigator** (quoteinvestigator.com) — fonte primária para rastreio de citações.
2. **Wikiquote** (en.wikiquote.org / pt.wikiquote.org) — se consta e sob qual autor.
3. **Busca geral** — a frase entre aspas + "quote" ou "citação".

Registrar:
- **Texto original exato** — a formulação mais antiga encontrada (pode diferir do que o usuário passou).
- **Autor real** — quem disse/escreveu primeiro, com obra e data se possível.
- **Atribuições errôneas** — se a frase costuma ser atribuída a outra pessoa.
- **Paráfrases notáveis** — quem reformulou ou popularizou.
- **Contexto** — obra/discurso/carta onde apareceu.

Se a autoria for **não verificável**, avisar o autor no chat; na nota, escrever "atribuída a X" sem narrar a busca.

### 4. Hora real e slug

Pipeline passos 1 e 2. O slug sai do conteúdo da citação (ou do título escolhido).

### 5. Título

A frase completa da citação, sem o nome do autor (o autor vai nas tags e no corpo). Sem limite rígido: o CSS do card trunca em 3 linhas, a página individual mostra inteira. Exemplos:
- `It always seems impossible until it's done`
- `A ship in harbor is safe, but that is not what ships are built for`
- `Antes só do que mal acompanhado`

Título longo com `:` ou `"` exige o cuidado do pipeline passo 3.

### 6. Tags

2–4 em kebab-case. **Obrigatório**: tag(s) com o nome do(s) autor(es) (`nelson-mandela`, `epictetus`, `john-a-shedd`). Tags temáticas conforme o conteúdo. Idioma das tags acompanha o idioma predominante da nota.

### 7. Summary

Uma frase (~150–200 chars) que contextualize a citação: quem disse, onde, e se há controvérsia de atribuição.

### 8. has_commentary

- `false` se a nota é só a citação + contexto factual de autoria.
- `true` se o usuário adicionar análise/conexão própria.

### 9. Sources

Pipeline passo 4. Fontes típicas:
- Quote Investigator → `kind: article`
- Wikiquote → `kind: wiki`
- Obra original onde a frase aparece → `kind: book | paper | article` conforme o caso

Só incluir o que foi efetivamente consultado.

### 10. Corpo

**A citação não vai no corpo**: ela já é o título, renderizado como citação pelo CSS. O corpo é só o contexto de autoria em prosa: quem disse, onde, quando; atribuição errônea comum, se houver; paráfrases notáveis, se houver.

- Sem blockquote.
- Factual e seco; sem "é uma frase fascinante".
- Regras de `ghost-writer`; links internos conforme pipeline passo 5.

### 11. Formato do arquivo

```markdown
---
title: "<citação completa>"
date: <YYYY-MM-DDTHH:MM:SS±HH:MM>
category: quote
summary: "<frase curta>"
tags: ["autor-tag", "tema-tag"]
has_commentary: <true|false>
sources:
  - title: "..."
    url: "..."
    kind: "..."
---

Contexto de autoria.
```

### 12. Portão, preview, write, commit

Pipeline passos 7 → 8 → 9 → 10 → 11 → 13 (build: passo 12, uma vez por sessão).

## Regras

- **`category: quote` é obrigatório** — aciona o layout/ícone de citação.
- **Tag de autor é obrigatória.**
- **Nunca inventar atribuição**; **nunca fabricar fontes.**
- Sem `Co-Authored-By` no commit (pipeline passo 11).
- Silvae congelado para notas (pipeline passo 14).
