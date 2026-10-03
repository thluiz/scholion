---
name: add-scholion-note-from-podcast-annotation
description: Cria nota no Scholion (E:/scholion/content/notes/) a partir de anotações de um episódio Vox. Recebe URL do episódio e timestamps. Busca as anotações no JSON, sugere título e comentários, confirma antes de criar.
argument-hint: "<url-vox> <HH:MM:SS,HH:MM:SS,...>"
---

Cria uma nota `category: podcast` no **Scholion** em `E:/scholion/content/notes/<slug>.md` a partir de anotações de um episódio publicado no Vox.

Pipeline comum em `add-scholion-note/references/note-pipeline.md` (passos 1–14). É extração automática: o texto das anotações vem pronto do Vox e **não** passa por search-first nem ghost-writer (pipeline passo 6, segundo parágrafo); só se sugerem cross-links.

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

Fonte de verdade é `origin/main` do clone `/home/hermes/vox-content` (HermesTools), nunca a working tree. O script da skill faz `git fetch` + `git show` e imprime só os campos necessários (o transcript, que é a maior parte do arquivo, não entra no contexto):

```bash
cat E:/scholion/.claude/skills/add-scholion-note-from-podcast-annotation/scripts/read-episode.py | wsl -d HermesTools -u hermes -- bash -c "python3 - YYYY/MM/WXX/slug"
```

Se sair `NOT_FOUND`, o episódio não está em `origin/main`: avisar e sugerir verificar se foi publicado no Vox.

A saída tem:
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
  - etimologia-de-bin-pessoa-em-movimento
  - chines-instrumental-iv
```

Perguntar ao usuário **quais linkar**. Os links escolhidos entram no corpo como markdown inline dentro da descrição da anotação, no formato do pipeline passo 5: `...sobre [彳](/notes/etimologia-de-bin-pessoa-em-movimento) segundo Si Fu...`. Nunca `../x.md` (gera href cru no site).

Se nenhum match relevante, seguir sem links — não forçar.

### 5. Construir proposta de nota

- **Hora real e slug** — pipeline passos 1 e 2 (slug a partir do título escolhido; o caminho entra no preview).

- **Título sugerido**: se há uma anotação, usar o `title` dela; se há várias, compor um título que as una. Idealmente ≤ 72 chars. Perguntar ao usuário se aceita ou quer outro.

- **Summary** — frase única (~150–200 chars) capturando o ponto central das anotações. Será exibido nos cards do mosaico. YAML conforme pipeline passo 3.

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

### 6. Portão (só se houver comentário do autor)

O texto das anotações é do Vox e não é reescrito. Se o usuário forneceu **comentário** (`has_commentary: true`), esse trecho é voz autoral: gravar o draft em `<scratchpad>/<slug>.md` e rodar `/ghost-audit <scratchpad>/<slug>.md` (pipeline passo 7), tratando findings só sobre o comentário.

### 7. Confirmar antes de criar

Pipeline passo 8: mostrar preview completo do arquivo `.md` (frontmatter + corpo, mais os findings do passo 6 se houve) e aguardar confirmação explícita.

### 8. Criar nota e comitar

Após confirmação:
1. Escrever `E:/scholion/content/notes/<slug>.md`, depois `/style-test` (pipeline passo 9). Fixes só no frontmatter; o texto das anotações não é reescrito.
2. Build: pipeline passo 12 (uma vez por sessão).
3. Commit-gate (seção abaixo), commit e push: pipeline passos 10, 11 e 13 (`git -C E:/scholion commit --only -m "note: <título>" -- content/notes/<slug>.md`; relatar "pushed `<hash>`").

## Commit-gate

O hook `ghost-audit-gate` vai auditar o texto do Vox no commit e pode dar `red` (afirmação sem fonte, PT-EU da transcrição). Esse texto **não é reescrito** para agradar o gate:

- Mostrar os findings ao autor.
- Liberar via marcador `.ghost-audit/<oid>.ok` (pipeline passo 10), registrado como override consciente.
- Se houve comentário do autor, o `/ghost-audit` do passo 6 já rodou antes; findings sobre o comentário seguem o tratamento normal do pipeline passo 7 (só correções com mérito).

## Regras

- **`date`** com hora real do sistema: pipeline passo 1, rodado de novo para cada nota.
- Título ideal ≤ 72 chars (mantém os cards consistentes).
- Sem campo `lang`.
- Commit sem `Co-Authored-By` (conteúdo é do usuário/episódio).
- Silvae congelado para notas (pipeline passo 14).
- Se o JSON não existir no caminho esperado, avisar e sugerir verificar se o episódio está publicado no Vox.

## Schema final do arquivo

```markdown
---
title: "<título>"
date: <YYYY-MM-DDTHH:MM:SS±HH:MM>
category: podcast
summary: "<frase curta>"
tags: ["tag1", "tag2", "programa", "episodio"]
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
