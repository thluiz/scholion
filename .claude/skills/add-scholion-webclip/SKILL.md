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

**ANTES de compor qualquer texto**, buscar no vault (`Grep`/`Glob` em `E:/scholion/content/notes/` e `E:/scholion/content/research/`) por temas relacionados ao conteúdo da página. Mostrar matches com contexto breve (1 linha: título + slug + 1 frase) e **esperar o autor apontar** o que linkar antes de redigir. Se nada relevante, dizer isso explicitamente. Guardar os itens aprovados (slug + title + por que conecta) para o passo 5 — é o `relatedNotes` do endpoint.

### 5. Compor via endpoint `webclip-summary`

A composição (resumo, fichamento, slug, título ajustado, summary, tags) roda **server-side** no vox-intelligence — não ler o texto bruto inteiro no próprio contexto nem redigir à mão. O endpoint já aplica as regras de voz do `ghost-writer` (fechos aforísticos, travessão de efeito, paralelismo mecânico, vocabulário banido PT-BR, source-or-silence) no prompt, então a primeira resposta já deve vir limpa — o portão `ghost-audit` do passo 8 continua rodando depois, como auditor independente (não pular por causa disso).

```powershell
$body = @{
  text = '<texto bruto capturado no passo 1/3, verbatim>'
  title = '<título capturado>'
  url = '<url original>'
  domain = '<dominio sem www.>'
  relatedNotes = @(  # opcional — itens aprovados no passo 4; omitir o array se nada foi aprovado
    @{ slug = '<slug>'; title = '<título>'; hint = '<por que conecta, opcional>' }
  )
} | ConvertTo-Json -Depth 6
$r = Invoke-RestMethod -Uri 'http://localhost:8080/api/vox-intelligence/presets/scholion/webclip-summary' -Method Post -ContentType 'application/json; charset=utf-8' -Body ([Text.Encoding]::UTF8.GetBytes($body)) -TimeoutSec 180
```

`$r` traz `slug`, `title`, `summary`, `tags`, `language`, `body` (resumo + `## Fichamento`), `lexicalWarnings`. Usar esses campos diretamente:

- **Língua da nota**: `$r.language` confirma a exceção deliberada ao padrão PT-BR do Scholion — resumo, fichamento, `summary` e `tags` seguem a língua da página capturada, não forçar PT-BR.
- **Slug e título**: usar `$r.slug` / `$r.title` como vêm (título só é ajustado pelo modelo se veio truncado/genérico na captura).
- **Tags**: `$r.tags` (2–4 kebab-case, já na língua da nota).
- **Summary**: `$r.summary`.
- **has_commentary**: `false` por padrão — o fichamento é síntese do conteúdo de terceiros, não análise própria do autor. `true` só se o autor pedir para acrescentar comentário/conexão original além do fichamento (nesse caso, o comentário é escrito à parte, não pelo endpoint).
- **Fail-open**: se o serviço estiver fora ou `$r.lexicalWarnings` vier não-vazio, dizer isso explicitamente ao autor antes de seguir — nunca fingir que a composição passou limpa.

### 6. Sources

**Duas entradas, sempre**:
```yaml
sources:
  - title: "<título da página>"
    url: "<url original>"
    kind: article   # inferir do domínio como em add-scholion-note (blog→article, youtube→video, arxiv/.pdf→paper, etc.)
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/<YYYY-MM>/<arquivo>.md"
    kind: repo
```

A segunda entrada é o link GitHub pro clipping bruto (passo 3) — cobertura se a página original mudar ou sair do ar. Só resolve depois do commit+push do clipping (passo 10, item 1); se a skill ainda não pushou quando monta a nota, montar a URL mesmo assim (o padrão é fixo: `blob/main/clippings/<YYYY-MM>/<arquivo>.md`) — ela passa a resolver no momento em que o push do passo 10 acontecer.

### 7. Corpo da nota

Vem pronto em `$r.body` (passo 5): `<resumo em prosa, 1–2 parágrafos>` + `## Fichamento` com bullets parafraseados. Usar como veio; só editar se o autor apontar algo no preview do passo 8.

**Modo de contingência** (endpoint fora do ar, ver fail-open no passo 5): compor à mão, carregando `ghost-writer` (SKILL.md) antes de escrever. Regras do fichamento nesse caso:
- **Parafraseado, não verbatim** — trechos citáveis ficam reservados ao passo 9 (notas `quote`), para não duplicar conteúdo literal em dois lugares.
- **Source-or-silence**: cada ponto precisa vir do texto extraído no passo 1/3. Nada inventado — se um ponto não está claramente no texto, omitir.
- Segue **todas** as regras de `ghost-writer` (vocabulário banido, estrutura banida, tom banido).
- Sem `Fonte:` no corpo — fontes ficam só no frontmatter.

### 8. Auditoria e preview

`/style-test` (lexical) + `ghost-audit` HTTP (portão obrigatório no topo) sobre o corpo composto. Mostrar findings + nota completa ao autor, aguardar confirmação antes de escrever.

### 9. Notas de citação (se houver frases)

Para cada frase recebida, gerar uma nota `category: quote` reaproveitando `add-scholion-quote`, **exceto**:
- **Pular a pesquisa externa de autoria** (Quote Investigator/Wikiquote/web search) — autor e URL já são conhecidos, vêm do clipping desta mesma página.
- `sources`: mesma URL do webclip, `kind` igual ao inferido no passo 6.

Mantém do `add-scholion-quote`: tag do autor obrigatória, ghost-writer, ghost-audit, preview, commit próprio por nota.

### 10. Escrita e commits

Um commit por artefato — nunca bundle:

1. Clipping bruto (se novo, passo 3): `git add clippings/<YYYY-MM>/<arquivo>.md && git commit -m "clip: <título>"`.
2. Nota `webclip`: build check (`cd /e/scholion && hugo --quiet`, abortar se exit ≠ 0) → `git add content/notes/<slug>.md` → marcador do commit-gate:
   ```powershell
   $o = git -C E:\scholion rev-parse ":content/notes/<slug>.md"
   New-Item -ItemType Directory -Force E:\scholion\.ghost-audit | Out-Null
   Set-Content "E:\scholion\.ghost-audit\$o.ok" $o
   ```
   → `git commit -m "note: <título>"` → `git push` (se houver remoto).
3. Cada nota `quote` gerada no passo 9: mesmo procedimento do item 2, um commit por nota.

## Regras

- **Voz e estilo**: resumo e fichamento vêm do endpoint `webclip-summary` (passo 5), que já aplica as regras de `ghost-writer` — vocabulário banido, estrutura banida, tom banido. Modo de contingência (endpoint fora do ar): compor à mão seguindo as mesmas regras (ver passo 7).
- **`captured_at`/`date` são OBRIGATÓRIOS** com timestamp real do sistema — nunca inventar.
- **`category: webclip` é OBRIGATÓRIO** na nota principal — aciona ícone/cor no site.
- Clipping bruto nunca é colado verbatim na nota — a nota é sempre prosa composta.
- Sem `Co-Authored-By Claude` em nenhum commit.
- Não tocar em `E:/silva/src/content/note/`.
- **Nunca inventar** conteúdo do fichamento além do que está no texto capturado.
- Build sanity check (`hugo --quiet`) antes de cada commit de nota.
