---
name: add-scholion-webclip
description: Captura uma página web (Playwright, com Claude in Chrome como fallback) como matéria-prima em E:/scholion/clippings/, e gera uma nota category:webclip no Scholion com resumo e fichamento. Opcionalmente cria notas de citação a partir de frases da mesma página.
argument-hint: "[url ou caminho .md] | [frase1] | [frase2] | ..."
---

Captura uma página web e cria uma nota `category: webclip` no **Scholion** em
`E:/scholion/content/notes/<slug>.md`, apoiada num clipping bruto salvo em
`E:/scholion/clippings/<YYYY-MM>/<dominio>--<slug-titulo>.md`. Opcionalmente
cria notas `category: quote` a partir de frases da mesma página.

---

## PORTÃO OBRIGATÓRIO — nota NÃO ESTÁ PRONTA sem passar aqui

Aplica-se à nota `webclip` e a cada nota `quote` gerada nesta skill — **não**
ao clipping bruto (esse é extração automática, ver Processo/passo 3).

**Antes** de mostrar preview, **antes** de escrever no disco, **antes** de
dizer "passou no ghost-writer", **antes** de qualquer commit:

Rodar o `ghost-audit` no HTTP endpoint sobre o corpo composto (frontmatter + corpo) e mostrar o JSON de findings ao autor.

```powershell
$body = @{ content = '<frontmatter+corpo compostos>'; slug = '<slug>' } | ConvertTo-Json -Depth 5
$r = Invoke-RestMethod -Uri 'http://localhost:8080/api/vox-intelligence/presets/scholion/ghost-audit' -Method Post -ContentType 'application/json; charset=utf-8' -Body ([Text.Encoding]::UTF8.GetBytes($body)) -TimeoutSec 120
$r.'x-parsed' | ConvertTo-Json -Depth 6
```

**Regras rígidas — sem exceção:**

- `verdict: red` → resolver **todos** os findings `block` antes do preview.
- `verdict: yellow` → mostrar findings ao autor, ele decide caso a caso.
- `verdict: green` → seguir.
- **PROIBIDO substituir por checklist mental.** Sem chamada HTTP, sem JSON visto, a auditoria não aconteceu.
- **Fail-open**: se o serviço estiver fora, dizer isso explicitamente. Nunca fingir verde.

---

## Parâmetros

Os argumentos vêm em `$ARGUMENTS` em formato livre, separados por ` | `:

- **Primeiro argumento** — URL (`http://` ou `https://`) **ou** caminho de um arquivo `.md` já existente. Se nenhum dos dois, pergunte.
- **Argumentos seguintes** (opcionais) — frases da página para virar notas de citação (`category: quote`). Podem vir agora ou numa invocação futura contra a mesma URL/clipping.

## Processo

### 1. Captura

**Modo URL (padrão)**: rodar `node fetch-webclip.mjs <url>` (script nesta skill). Retorna JSON `{title, text}` no stdout.

- **Fallback automático para Claude in Chrome** se o script falhar (exit ≠ 0, timeout, erro de navegação): `tabs_context_mcp` → `tabs_create_mcp` → `navigate(url)` → `get_page_text(tabId)` → capturar título da tab → `tabs_close_mcp`.
- **Fallback manual**: mostrar ao autor um trecho do texto capturado antes de seguir. Se ele apontar que está errado (login wall, paywall, captcha, SPA que não renderizou o conteúdo real), reprocessar via Claude in Chrome (mesmo caminho acima) — usa a sessão real e logada do Chrome do autor, que o Playwright headless não tem.

**Modo arquivo `.md`**: pular captura. Ler o arquivo. Se já tiver frontmatter de clipping (`url`/`title`/`domain`/`captured_at`), reaproveitar. Se não tiver, perguntar a URL de origem (obrigatória — sem ela não há como citar a fonte) e o título.

### 2. Hora real do sistema

`date +"%Y-%m-%dT%H:%M:%S%:z"` para `captured_at`. Nunca inventar horário. (Modo arquivo com frontmatter próprio: usar o `captured_at` que já vem no arquivo, não gerar um novo.)

### 3. Salvar o clipping bruto

Em `E:/scholion/clippings/<YYYY-MM>/<dominio>--<slug-do-titulo>.md` (mês da captura), frontmatter:

```yaml
---
url: "<url original>"
captured_at: "<timestamp>"
title: "<título capturado>"
domain: "<dominio sem www.>"
---
```

Corpo = texto extraído **verbatim**, sem edição. **Sem ghost-writer/ghost-audit neste passo** — é extração automática, não composição (o conteúdo vem pronto, não passa pela voz do autor). `<dominio>` = host sem `www.`, pontos trocados por `-` (ex.: `martinfowler.com` → `martinfowler-com`).

Se modo arquivo `.md` e o arquivo já está dentro de `clippings/`, pular este passo (já está salvo).

### 4. Search-first interativo

**ANTES de compor qualquer texto**, buscar no vault (`Grep`/`Glob` em `E:/scholion/content/notes/` e `E:/scholion/content/research/`) por temas relacionados ao conteúdo da página. Mostrar matches com contexto breve (1 linha: título + slug + 1 frase) e **esperar o autor apontar** o que linkar antes de redigir. Se nada relevante, dizer isso explicitamente.

### 5. Carregar ghost-writer

**ANTES de compor** resumo/fichamento, ler a skill `ghost-writer` (SKILL.md). Isso É composição na voz do autor — Claude sintetiza conteúdo de terceiros em prosa, igual ao "contexto de autoria" das notas `quote` — diferente do passo 3, que é extração pura.

### 6. Língua da nota

**Exceção deliberada ao padrão PT-BR do Scholion**: resumo, fichamento, `summary` e `tags` seguem a **língua da página capturada**. Página em inglês → nota em inglês. Página em PT → nota em PT. Preserva fidelidade ao fichamento como referência da fonte original; não traduzir.

### 7. Slug e título

Slug a partir do título da página: lowercase, sem acentos, espaços/pontuação → `-`, máx ~50 chars. Título = título da página (ajustar só se estiver truncado/genérico demais).

### 8. Tags

2–4 kebab-case, incluindo tema(s) do search-first (passo 4). Idioma acompanha a língua da nota (passo 6).

### 9. Summary

~150–200 chars, na língua da nota: o que a página argumenta, não uma descrição genérica ("artigo sobre...").

### 10. has_commentary

`false` por padrão — o fichamento é síntese do conteúdo de terceiros, não análise própria do autor. `true` só se o autor pedir para acrescentar comentário/conexão original além do fichamento.

### 11. Sources

Uma entrada:
```yaml
sources:
  - title: "<título da página>"
    url: "<url original>"
    kind: article   # inferir do domínio como em add-scholion-note (blog→article, youtube→video, arxiv/.pdf→paper, etc.)
```

### 12. Corpo da nota

```markdown
<Resumo em prosa, 1–2 parágrafos: o argumento central da página.>

## Fichamento

- <ponto-chave 1, parafraseado>
- <ponto-chave 2, parafraseado>
- ...
```

Regras do fichamento:
- **Parafraseado, não verbatim** — trechos citáveis ficam reservados ao passo 14 (notas `quote`), para não duplicar conteúdo literal em dois lugares.
- **Source-or-silence**: cada ponto precisa vir do texto extraído no passo 1/3. Nada inventado — se um ponto não está claramente no texto, omitir.
- Segue **todas** as regras de `ghost-writer` (vocabulário banido, estrutura banida, tom banido).
- Sem `Fonte:` no corpo — fontes ficam só no frontmatter.

### 13. Auditoria e preview

`/style-test` (lexical) + `ghost-audit` HTTP (portão obrigatório no topo) sobre o corpo composto. Mostrar findings + nota completa ao autor, aguardar confirmação antes de escrever.

### 14. Notas de citação (se houver frases)

Para cada frase recebida, gerar uma nota `category: quote` reaproveitando `add-scholion-quote`, **exceto**:
- **Pular a pesquisa externa de autoria** (Quote Investigator/Wikiquote/web search) — autor e URL já são conhecidos, vêm do clipping desta mesma página.
- `sources`: mesma URL do webclip, `kind` igual ao inferido no passo 11.

Mantém do `add-scholion-quote`: tag do autor obrigatória, ghost-writer, ghost-audit, preview, commit próprio por nota.

### 15. Escrita e commits

Um commit por artefato — nunca bundle:

1. Clipping bruto (se novo, passo 3): `git add clippings/<YYYY-MM>/<arquivo>.md && git commit -m "clip: <título>"`.
2. Nota `webclip`: build check (`cd /e/scholion && hugo --quiet`, abortar se exit ≠ 0) → `git add content/notes/<slug>.md` → marcador do commit-gate:
   ```powershell
   $o = git -C E:\scholion rev-parse ":content/notes/<slug>.md"
   New-Item -ItemType Directory -Force E:\scholion\.ghost-audit | Out-Null
   Set-Content "E:\scholion\.ghost-audit\$o.ok" $o
   ```
   → `git commit -m "note: <título>"` → `git push` (se houver remoto).
3. Cada nota `quote` gerada no passo 14: mesmo procedimento do item 2, um commit por nota.

## Regras

- **Voz e estilo**: resumo e fichamento seguem `ghost-writer` — vocabulário banido, estrutura banida, tom banido.
- **`captured_at`/`date` são OBRIGATÓRIOS** com timestamp real do sistema — nunca inventar.
- **`category: webclip` é OBRIGATÓRIO** na nota principal — aciona ícone/cor no site.
- Clipping bruto nunca é colado verbatim na nota — a nota é sempre prosa composta.
- Sem `Co-Authored-By Claude` em nenhum commit.
- Não tocar em `E:/silva/src/content/note/`.
- **Nunca inventar** conteúdo do fichamento além do que está no texto capturado.
- Build sanity check (`hugo --quiet`) antes de cada commit de nota.
