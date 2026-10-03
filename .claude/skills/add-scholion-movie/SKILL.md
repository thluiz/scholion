---
name: add-scholion-movie
description: "Cria uma nota de filme (category: movie, page bundle com poster local) no Scholion: confirma ficha técnica em IMDb/Wikipedia, pergunta com quem foi assistido (vira tag), registra escalas 0-5 só se o autor der o número. Use quando o usuário disser que viu/assistiu um filme ou pedir para registrar um filme."
argument-hint: "[título do filme] | [diretor presumido]"
---

Cria uma nota de **filme** (`category: movie`) no **Scholion**, como page bundle em `E:/scholion/content/notes/<slug>/index.md` + `poster.<ext>`.

Pipeline comum em `add-scholion-note/references/note-pipeline.md` (passos 1–14). Aqui só o que é específico do filme.

## Parâmetros

`$ARGUMENTS` em formato livre. Extrair:
- **título** — como o usuário lembra. Se faltar, perguntar.
- **diretor presumido** — pode ser desconhecido.

## Processo

### 1. Search-first interativo

Pipeline passo 6: buscar pelo título, diretor, atores principais e temas adjacentes; listar; esperar o autor apontar.

### 2. Carregar ghost-writer

Ler `ghost-writer/SKILL.md` antes de compor (vale sobretudo para o parágrafo de comentário).

### 3. Pesquisa do filme

Usar `WebSearch` e `WebFetch`:

1. **IMDb** — ficha técnica.
2. **Wikipedia** (pt / en) — sinopse e contexto.
3. **Letterboxd** — opcional, recepção crítica.

Registrar: título original; título de lançamento em português (BR), usado no `title`; diretor(es); ano; país(es); sinopse curta (1–2 frases factuais). Dado não verificável fica de fora; avisar o autor.

### 4. Companhia

**Obrigatório antes do preview**: perguntar com quem assistiu. Respostas viram tags sem prefixo, kebab-case sem acentos (`claudia`, `filhos`). `sozinho` = nenhuma tag de companhia (caso default).

### 5. Hora real e slug

Pipeline passos 1 e 2. Slug a partir do título em português, **sem o ano**. É bundle: `content/notes/<slug>/index.md`.

### 6. Título

Título em português + ` (ano)`: `O Som ao Redor (2012)`, `Parasita (2019)`.

### 7. Tags

Kebab-case, sem prefixos. Obrigatórias: diretor(es) (`kleber-mendonca-filho`); companhia, se houver (passo 4). Opcionais: gênero, tema, país (`cinema-brasileiro`, `documentario`).

### 8. Summary

Uma frase (~150–200 chars): o que é o filme, dirigido por quem, ano. Sem spoilers.

### 9. has_commentary

- `false` se é só ficha + companhia.
- `true` se o autor adicionar comentário próprio.

### 10. Escalas de 0 a 5 (opcionais)

Campos inteiros 0–5, renderizados como cinco ícones. O registro canônico é `E:/scholion/data/scales.yaml` — **consultar o arquivo**, escalas novas entram lá sem passar por esta skill. Hoje:

- `rating` — "Nota", 🎫.
- `morbius` — "Morbius", 🧛. Escala do autor para filmes ruins-divertidos, criada a partir de [Mortal Kombat 2 (2026)](E:/scholion/content/notes/mortal-kombat-2/index.md).
- `laughs` — "Gargalhadas", 🤣. Comédias.

Independentes entre si. **Não perguntar os valores**: o campo só entra quando o autor der o número ("põe 4 Morbius", "nota 3"). Ausente e `0` são coisas diferentes. No preview, uma linha lembrando que as escalas existem; sem insistir.

### 11. Sources

Pipeline passo 4. Típicas: IMDb → `kind: film` (com `url`); Wikipedia → `kind: wiki`; Letterboxd → `kind: article`.

### 12. Poster

Toda nota de filme tem poster local. O download acontece **antes** do preview, mas no scratchpad; a pasta da nota só é criada depois da aprovação.

1. URL do poster, em ordem de preferência: infobox da Wikipedia (`WebFetch` com prompt "Return ONLY the full URL of the poster image (upload.wikimedia.org)"; para a versão em alta, tirar `/thumb/.../<size>px-<file>` e manter o caminho até o filename). Sem Wikipedia: Cinecartaz, AlloCiné ou outro site com infobox.
2. Baixar para o scratchpad (Wikipedia exige User-Agent não-vazio):
   ```bash
   curl -sSL -A "Mozilla/5.0 (Scholion-bot)" "<URL>" -o "<scratchpad>/<slug>-poster.<ext>"
   ```
3. Verificar: `file "<scratchpad>/<slug>-poster.<ext>"` deve ser imagem real, proporção ~2:3 vertical. Se for mais largo que alto, avisar o autor (pode ser logo, não poster).
4. Extensão segue o formato real (`.jpg`, `.png`, `.jpeg`); `.jpeg` pode virar `poster.jpg` (só muda o sufixo).

### 13. Corpo

Prosa factual: diretor, ano, país, premissa. Sem resenha, a menos que `has_commentary: true`.

1. **Sinopse em blockquote** (`> ...`): um parágrafo, voz externa, enciclopédica.
2. Linha em branco.
3. **Comentário do autor** (só se `has_commentary: true`): prosa direta, voz do Thiago.
4. Linha em branco.
5. **Poster**: `![Poster de <Título> (<ano>)](poster.<ext>)`.

Sem floreio ("imperdível"), sem juízo crítico fora do comentário. **Sem spoilers** no summary nem no corpo: premissa, não reviravolta; se a Wikipedia entrega o twist, traduzir o setup e cortar o payoff.

### 14. Formato do `index.md`

```markdown
---
title: "<Título do filme> (<ano>)"
date: <YYYY-MM-DDTHH:MM:SS±HH:MM>
category: movie
summary: "<sinopse curta, sem spoilers>"
tags: ["diretor", "companhia1", "tema"]   # companhias só se acompanhado
has_commentary: <true|false>
rating: <0-5>      # opcional; só se o autor declarar
morbius: <0-5>     # opcional; só se o autor declarar
laughs: <0-5>      # opcional; só se o autor declarar
sources:
  - title: "..."
    url: "..."
    kind: "..."
---

> Sinopse factual em blockquote. Diretor, ano, país, premissa. Sem spoilers.

Comentário do autor (omitir se has_commentary é false).

![Poster de <Título> (<ano>)](poster.<ext>)
```

### 15. Portão e preview

Pipeline passos 7 e 8. No preview, mencionar o poster verificado (dimensões) e a linha das escalas.

### 16. Escrita e commit

Após a aprovação:

1. Criar a pasta e mover o poster:
   ```bash
   mkdir -p E:/scholion/content/notes/<slug> && mv "<scratchpad>/<slug>-poster.<ext>" E:/scholion/content/notes/<slug>/poster.<ext>
   ```
2. `Write` em `E:/scholion/content/notes/<slug>/index.md`, depois `/style-test` (pipeline passo 9).
3. Marcador, commit e push: pipeline passos 10, 11 e 13 na forma bundle (`rev-parse ":content/notes/<slug>/index.md"`; `commit --only ... -- content/notes/<slug>/`). Build: passo 12, uma vez por sessão.

## Regras

- **`category: movie` é obrigatório** — aciona o ícone 🎦 e a cor azul.
- **Tag de diretor é obrigatória.** Companhia só se acompanhado.
- **Poster local é obrigatório**; nunca embedar URL externo.
- **Escalas**: nunca perguntar o valor; só registrar se o autor der o número.
- **Nunca inventar ficha técnica.**
- Sem `Co-Authored-By` no commit (pipeline passo 11).
- Silvae congelado para notas (pipeline passo 14).
