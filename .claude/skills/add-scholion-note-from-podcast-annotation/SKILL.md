---
name: add-scholion-note-from-podcast-annotation
description: Cria nota no Scholion (E:/scholion/content/notes/) a partir de anotações de um episódio Vox. Recebe URL do episódio e timestamps. Busca as anotações no JSON, sugere título e comentários, confirma antes de criar.
argument-hint: "<url-vox> <HH:MM:SS,HH:MM:SS,...>"
---

Cria uma nota no **Scholion** baseada em anotações de um episódio publicado no Vox.

> **Importante:** notas curtas (incluindo as derivadas de podcast) **não vão mais para silvae**. Sempre criar em `E:/scholion/content/notes/`. O silvae está congelado para notas — só recebe textos longos.

## Parâmetros

Extraia de `$ARGUMENTS`:
- **url** — URL do episódio Vox (ex: `https://vox.thluiz.com/2026/03/W14/slug`). Se ausente, pergunte.
- **timestamps** — lista separada por vírgula (ex: `58:54,01:01:02`). Se ausente, pergunte.
- **título** — opcional. Se não fornecido, será sugerido com base nas anotações.
- **comentário** — opcional. Texto adicional do usuário a incluir na nota (sinaliza `has_commentary: true`).

## Processo

### 1. Extrair path do episódio

Da URL `https://vox.thluiz.com/YYYY/MM/WXX/slug`, extraia o path relativo: `YYYY/MM/WXX/slug`.

### 2. Ler o JSON do episódio

```bash
wsl -d HermesTools -u hermes -- bash -c "cat ~/vox-content/YYYY/MM/WXX/slug.json"
```

O JSON tem:
- `annotations`: lista de `{ts: "HH:MM:SS", title: "...", description: "..."}`
- `title`: título do episódio
- `metadata.podcast`: nome do podcast
- `tags`: tags do episódio (referência; filtrar pelas anotações selecionadas)

### 3. Encontrar anotações pelos timestamps

Para cada timestamp fornecido, normalizar para `HH:MM:SS` e encontrar a anotação mais próxima (±90s) em `annotations[].ts`.

Se nenhuma anotação for encontrada próxima de um timestamp, avisar e perguntar se deseja prosseguir sem ela.

### 4. Sugerir links cruzados

Para cada anotação selecionada, rodar `Grep` em `E:/scholion/content/` por 2-3 termos centrais (substantivos próprios, conceitos-chave extraídos do `title`/`description` da anotação). Apresentar os matches numa lista compacta por anotação:

```
Anotação: 58:54 — "Si Fu sobre 彳"
Possíveis links:
  - etimologia-de-bin-pessoa-em-movimento.md
  - chines-instrumental-iv.md
```

Perguntar ao usuário **quais linkar**. Os links escolhidos entram no corpo como markdown inline dentro da descrição da anotação (ex: `...sobre [彳](../etimologia-de-bin-pessoa-em-movimento.md) segundo Si Fu...`).

Se nenhum match relevante, seguir sem links — não forçar.

### 5. Construir proposta de nota

- **Título sugerido**: se há uma anotação, usar o `title` dela; se há várias, compor um título que as una. Idealmente ≤ 72 chars. Perguntar ao usuário se aceita ou quer outro.

- **Summary** — frase única (~150–200 chars) capturando o ponto central das anotações. Será exibido nos cards do mosaico.

- **has_commentary** — `true` se o usuário adicionou comentário próprio; `false` se a nota é só transcrição/excerto das anotações.

- **Tags** — começar pelas `tags` do episódio, filtrar as que têm relação direta com o conteúdo das anotações selecionadas. Idioma das tags segue idioma do episódio (PT ou EN). 2–4 tags temáticas, kebab-case.
  - **Tag de programa (obrigatória):** identifica o podcast/programa de origem, permitindo listar todas as notas vindas daquele programa. Derivar de `metadata.podcast` em kebab-case sem acentos (ex: "É tudo culpa da cultura" → `e-tudo-culpa-da-cultura`; "Pragmatic Engineer" → `pragmatic-engineer`). Se já existir nessa forma no array `tags` do episódio, reutilizar. Vem **após** as tags temáticas.
  - **Tag de episódio (obrigatória):** identifica o episódio específico, para que todas as notas do mesmo episódio possam ser listadas juntas. Derivar do título do episódio: slug curto em kebab-case (ex: "É Tudo Culpa da Cultura #03: Universo Sugar" → `universo-sugar`; "Why Great Developers Still Google Their Errors" → `devs-google-errors`). Vem **após** a tag de programa.

- **sources** — array com **uma** entrada para o episódio Vox:
  ```yaml
  sources:
    - title: "<título do episódio> — <nome do podcast>"
      url: "<url-vox>#HH:MM:SS"  # âncora para o primeiro timestamp
      kind: podcast
  ```
  Se a primeira anotação tem timestamp `00:58:54`, a URL fica `<url-vox>#00:58:54`.

- **Corpo**: para cada anotação encontrada, incluir o timestamp em **bold** seguido do título e a `description`. Se o usuário forneceu comentário, incluir em itálico após as anotações.

  Formato sugerido:

  ```markdown
  **HH:MM:SS** — Título da anotação

  Descrição da anotação.

  **HH:MM:SS** — Próxima anotação

  Descrição.

  *Comentário do usuário, se houver.*
  ```

  **Não incluir `Fonte:` ou `Fontes:` no corpo** — as fontes ficam só no frontmatter (renderizadas pelo template).

### 6. Confirmar antes de criar

Mostrar preview completo do arquivo `.md` (frontmatter + corpo) e aguardar confirmação explícita.

### 7. Criar nota e publicar

Após confirmação:
1. Gerar slug a partir do título (lowercase, sem acentos, hífens, máx ~50 chars).
2. Escrever `E:/scholion/content/notes/<slug>.md`.
3. Sanity check: `cd /e/scholion && hugo --quiet` — abortar se exit ≠ 0.
4. `git add content/notes/<slug>.md` + `git commit -m "note: <título>"` + `git push`.

## Regras

- **`date` é OBRIGATÓRIO** com formato ISO 8601 + offset real do sistema: `YYYY-MM-DDTHH:MM:SS±HH:MM` (nunca copiar offset de exemplo). **NUNCA inventar a hora.** Antes de gerar o frontmatter, rodar:
  ```bash
  pwsh -NoProfile -Command "Get-Date -Format 'yyyy-MM-ddTHH:mm:sszzz'"
  ```
  e usar o output exato. Se forem várias notas em sequência, incrementar 1 minuto por nota.
- Título ideal ≤ 72 chars (mantém os cards consistentes).
- Sem campo `lang`.
- **Nunca tocar em `E:/silva/src/content/note/`** — silvae está congelado para notas.
- Commit sem `Co-Authored-By Claude` (conteúdo é do usuário/episódio).
- Se o JSON não existir no caminho esperado, avisar e sugerir verificar se o episódio está publicado no Vox.

## Schema final do arquivo

```markdown
---
title: "<título>"
date: <YYYY-MM-DDTHH:MM:SS±HH:MM>
category: podcast
summary: "<frase curta>"
tags: ["tag1", "tag2"]
has_commentary: <true|false>
sources:
  - title: "<título do episódio> — <podcast>"
    url: "<url-vox>#<primeiro-ts>"
    kind: podcast
---

**HH:MM:SS** — <título da anotação>

<descrição>

*<comentário opcional do usuário>*
```
