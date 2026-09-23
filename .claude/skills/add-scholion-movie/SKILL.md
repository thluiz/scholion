---
name: add-scholion-movie
description: Cria uma nota de filme no Scholion (E:/scholion/content/notes/). Recebe título e possível diretor, pesquisa ficha técnica, pergunta com quem foi assistido, e cria a nota verificada. Baseada em add-scholion-quote.
argument-hint: "[título do filme] | [diretor presumido]"
---

Cria uma nota de **filme** no **Scholion** em `E:/scholion/content/notes/<slug>.md`.

> **Importante:** notas curtas não vão para silvae. Sempre criar em scholion.

---

## PORTÃO OBRIGATÓRIO — nota NÃO ESTÁ PRONTA sem passar aqui

**Antes** de mostrar preview, **antes** de escrever no disco, **antes** de dizer "passou no ghost-writer", **antes** de qualquer commit:

Rodar o `ghost-audit` no HTTP endpoint sobre o corpo composto (frontmatter + corpo) e mostrar o JSON de findings ao autor.

```powershell
$body = @{ content = '<frontmatter+corpo compostos>'; slug = '<slug>' } | ConvertTo-Json -Depth 5
$r = Invoke-RestMethod -Uri 'http://localhost:8080/api/vox-intelligence/presets/scholion/ghost-audit' -Method Post -ContentType 'application/json; charset=utf-8' -Body ([Text.Encoding]::UTF8.GetBytes($body)) -TimeoutSec 120
$r.'x-parsed' | ConvertTo-Json -Depth 6
```

**Regras rígidas — sem exceção:**

- `verdict: red` → resolver **todos** os findings `block` antes do preview. Nunca declarar pronto com red.
- `verdict: yellow` → mostrar findings ao autor, ele decide caso a caso.
- `verdict: green` → seguir.
- **PROIBIDO substituir por checklist mental.** Aplicar o checklist ghost-writer de cabeça e declarar "corpo limpo" **NÃO é rodar o ghost-audit**. Se a chamada HTTP não foi feita e o JSON não foi visto, a auditoria não aconteceu — diga isso ao autor em vez de fingir que passou.
- **Fail-open**: se o serviço estiver fora, dizer "auditoria estrutural não rodou — vox-intelligence offline" explicitamente. Nunca fingir verde nem simular findings.

Todas as demais checagens (search-first no vault, pesquisa da ficha, checklist ghost-writer em contexto, `/style-test` lexical) **somam** a este portão — nunca substituem.

---

## Parâmetros

Os argumentos vêm em `$ARGUMENTS` em formato livre. Extraia:
- **título** — o nome do filme conforme o usuário lembra. Se não fornecido, pergunte.
- **diretor presumido** — quem o usuário acredita ser o diretor. Se não fornecido, pergunte (pode ser desconhecido).

Se o título estiver ausente, pergunte antes de continuar.

## Processo

### 1. Search-first interativo

**ANTES de compor qualquer texto**, buscar no vault (`Grep`/`Glob` em `E:/scholion/content/notes/` e `E:/scholion/content/research/`) pelo título, diretor presumido, atores principais e temas adjacentes. Mostrar os matches com contexto breve (1 linha por nota: título + slug + 1 frase do conteúdo) e **esperar o autor apontar** quais linkar, expandir, ou ignorar antes de redigir o corpo. Se nada relevante for encontrado, dizer explicitamente ("nenhuma nota relacionada encontrada") antes de seguir.

### 2. Carregar ghost-writer

**ANTES de compor qualquer texto**, ler a skill `ghost-writer` (SKILL.md) para ter a checklist carregada no contexto.

### 3. Pesquisa do filme

Usar `WebSearch` e `WebFetch` para confirmar a ficha. Consultar:

1. **IMDb** (imdb.com) — fonte primária para ficha técnica
2. **Wikipedia** (pt.wikipedia.org / en.wikipedia.org) — sinopse e contexto
3. **Letterboxd** (letterboxd.com) — opcional, para recepção crítica

Investigar e registrar:
- **Título original** — no idioma do país de origem
- **Título de lançamento em português** (BR) — usado no `title` da nota
- **Diretor(es)**
- **Ano de lançamento**
- **País(es) de origem**
- **Sinopse curta** — 1–2 frases factuais para o `summary`

Se algum dado não for verificável, dizer claramente — nunca inventar.

### 4. Pergunta sobre companhia

**OBRIGATÓRIO antes do preview**: perguntar ao usuário com quem assistiu o filme. As respostas viram tags (sem prefixo, apenas nomes em kebab-case).

Exemplos de resposta esperada:
- `claudia` → tag `claudia`
- `claudia, filhos` → tags `claudia`, `filhos`
- `sozinho` → **nenhuma tag de companhia** (caso default, não precisa ser registrado)

Se o usuário responder com nomes próprios, normalizar para kebab-case minúsculo sem acentos.

### 5. Hora real do sistema

Rodar `date +"%Y-%m-%dT%H:%M:%S%:z"` para obter o `date` atual. Nunca inventar horários.

### 6. Slug

A partir do título do filme: lowercase, remover acentos, substituir espaços e pontuação por `-`, máx ~50 chars. **Não incluir o ano no slug.**

### 7. Título

Título de lançamento em português + ` (ano)` entre parênteses.
Exemplos:
- `O Som ao Redor (2012)`
- `Cidade de Deus (2002)`
- `Parasita (2019)`

### 8. Tags

Tags em kebab-case, sem prefixos. **Obrigatórias**:
- **Diretor(es)** — ex: `kleber-mendonca-filho`, `bong-joon-ho`
- **Companhia** (apenas se acompanhado) — nomes de quem assistiu junto, sem prefixo: `claudia`, `filhos`. Se `sozinho`, **nenhuma tag de companhia** — esse é o caso default e não vira tag.

Tags temáticas opcionais conforme o conteúdo: gênero, tema, país, etc. (ex: `cinema-brasileiro`, `documentario`, `terror`).

### 9. Summary

Uma frase curta (~150–200 chars) com sinopse factual: o que é o filme, dirigido por quem, ano. Será usada nos cards do mosaico.

### 10. has_commentary

- `false` se a nota é apenas a ficha + companhia
- `true` se o usuário adicionar análise/comentário/conexão própria

### 10b. Escalas de 0 a 5 (opcionais)

Campos de frontmatter com inteiro de 0 a 5, cada um renderizando cinco ícones
com os não-atingidos esmaecidos. O registro canônico é
`E:/scholion/data/scales.yaml` — **consultar o arquivo**, porque escalas novas
entram lá sem passar por esta skill. Hoje:

- `rating` — rótulo "Nota", 🎫. Avaliação geral do filme.
- `morbius` — rótulo "Morbius", 🧛. Escala do autor para filmes ruins-divertidos,
  criada a partir de [Mortal Kombat 2 (2026)](E:/scholion/content/notes/mortal-kombat-2/index.md).
- `laughs` — rótulo "Gargalhadas", 🤣. Para comédias.

São independentes: a nota pode ter as duas, uma só, ou nenhuma.

**Não perguntar os valores.** O campo só entra quando o autor der o número por
conta própria ("põe 4 Morbius nesse", "nota 3"). Sem valor declarado, o campo
fica fora do frontmatter — ausente e `0` são coisas diferentes, e 0 significa
"escala aplicada, deu zero".

No preview, incluir uma linha curta lembrando que as escalas existem e estão
disponíveis caso ele queira usar. Uma linha, sem insistir.

### 11. Sources

Array estruturado no frontmatter. Cada fonte da pesquisa:
```yaml
- title: "Título da fonte"
  author: "Diretor"      # opcional
  year: 2024             # opcional
  url: "https://..."     # opcional
  kind: film | wiki | article | other
```

Fontes típicas para filmes:
- IMDb → `kind: film` (com `url`)
- Wikipedia → `kind: wiki`
- Letterboxd → `kind: article`

### 12. Poster

Cada nota de filme **deve** ter um poster local. Pipeline:

1. Buscar o URL do poster — ordem de preferência:
   - Wikipedia (infobox) — usar `WebFetch` na página do filme com prompt: "Return ONLY the full URL of the poster image (upload.wikimedia.org)". Para a versão em alta, remover `/thumb/.../<size>px-<file>` mantendo apenas o caminho até o filename.
   - Para filmes sem Wikipedia, tentar Cinecartaz (Público), AlloCiné, ou outro site de cinema com infobox de poster.
2. Baixar via curl (Wikipedia exige User-Agent não-vazio):
   ```bash
   curl -sSL -A "Mozilla/5.0 (Scholion-bot)" "<URL>" -o content/notes/<slug>/poster.<ext>
   ```
3. Verificar com `file content/notes/<slug>/poster.<ext>` que é uma imagem real e a proporção é razoável (~2:3 vertical típico de poster). Se for banner-shape (largura > altura), avisar o usuário antes de prosseguir — pode ser logo, não poster.
4. Extensão segue o formato real: `.jpg`, `.png`, `.jpeg`. Se a Wikipedia servir `.jpeg`, salvar como `poster.jpg` para uniformidade só se a renomeação não corromper o conteúdo (curl não corrompe — apenas o sufixo).

### 13. Corpo da nota

Contexto factual em prosa: diretor, ano, país, sinopse curta. Sem resenha, a menos que `has_commentary: true`.

**Estrutura do corpo:**
1. **Sinopse factual em blockquote** (`> ...`) — ficha técnica e premissa. Voz externa, encyclopedic. Um parágrafo único prefixado com `> `.
2. **Linha em branco**.
3. **Comentário do autor** (se `has_commentary: true`) — prosa direta, sem prefixo. Voz do Thiago.
4. **Linha em branco**.
5. **Imagem do poster** — `![Poster de <Título> (<ano>)](poster.<ext>)`.

**Regras do corpo:**
- Sem floreio, sem "filme imperdível", sem juízo crítico (a não ser que o usuário tenha pedido com `has_commentary: true`)
- Seguir **todas** as regras da skill `ghost-writer` (especialmente no parágrafo de comentário)
- Sem `Fonte:` no final — fontes ficam só no frontmatter
- **Sem spoilers no summary nem no corpo**: revelações centrais (twist, reviravolta, identidade do assassino, motivação oculta, etc.) **não** entram. Falar do gancho/premissa, não do ponto de virada. Se a Wikipedia entrega o spoiler na sinopse, traduzir o que é setup; cortar o que é payoff.

### 14. Formato final do arquivo

A nota vai num **folder** `content/notes/<slug>/` com `index.md` + `poster.<ext>`. Estrutura:

```
content/notes/<slug>/
├── index.md
└── poster.jpg   (ou .png, .jpeg conforme original)
```

Conteúdo do `index.md`:

```markdown
---
title: "<Título do filme> (<ano>)"
date: <YYYY-MM-DDTHH:MM:SS±HH:MM>
category: movie
summary: "<sinopse curta, sem spoilers>"
tags: ["diretor", "companhia1", "companhia2", "tema"]   # companhias só se acompanhado
has_commentary: <true|false>
rating: <0-5>                                           # opcional — escala "Nota"; só se o autor declarar
morbius: <0-5>                                          # opcional — escala "Morbius"; só se o autor declarar
laughs: <0-5>                                           # opcional — escala "Gargalhadas"; só se o autor declarar
sources:
  - title: "..."
    url: "..."
    kind: "..."
---

> Sinopse factual em blockquote, voz externa. Diretor, ano, país, premissa. Sem spoilers.

Comentário do autor em prosa direta (omitir se has_commentary é false).

![Poster de <Título> (<ano>)](poster.<ext>)
```

### 15. Auditoria de voz

Executar as duas auditorias sobre o corpo composto e mostrar os findings no preview:

- **Lexical** — `/style-test <slug>` (regex, grátis, ~1s).
- **Estrutural/semântica** — chamada HTTP ao `ghost-audit` conforme o **PORTÃO OBRIGATÓRIO** no topo desta skill. Não há atalho: rodar o comando, ver o JSON, reportar o verdict. Sem chamada, sem "passou".

### 16. Preview e confirmação

Mostrar a nota completa ao usuário e aguardar confirmação antes de escrever.

### 17. Escrita e commit

Após confirmação:
1. Criar o folder: `mkdir -p content/notes/<slug>`
2. Escrever em `E:/scholion/content/notes/<slug>/index.md`
3. Confirmar que o `poster.<ext>` já está no folder (baixado no passo 12)
4. Build sanity check: `cd /e/scholion && hugo --quiet` — abortar se exit ≠ 0
5. `git add content/notes/<slug>/`
6. Gravar o marcador do commit-gate (a nota já foi auditada no passo 15 — evita re-auditoria no portão):
   ```powershell
   $o = git -C E:\scholion rev-parse ":content/notes/<slug>/index.md"
   New-Item -ItemType Directory -Force E:\scholion\.ghost-audit | Out-Null
   Set-Content "E:\scholion\.ghost-audit\$o.ok" $o
   ```
7. `git commit -m "note: <título>"`
8. `git push` (se houver remoto configurado)

## Regras

- **Voz e estilo**: corpo segue as regras da skill `ghost-writer`.
- **`date` é OBRIGATÓRIO** com formato ISO 8601 + offset.
- **`category: movie` é OBRIGATÓRIO** — aciona o ícone 🎦 e a cor azul-céu.
- **Tags de diretor são OBRIGATÓRIAS**.
- **Sempre perguntar com quem assistiu** antes do preview. Se acompanhado, gerar uma tag por pessoa (kebab-case, sem prefixo). Se sozinho, **nenhuma tag de companhia** — sozinho é o caso default e não vira tag.
- **Poster local é OBRIGATÓRIO**: a nota vai num folder `<slug>/` com `index.md` + `poster.<ext>`. Nunca embedar URL externo, sempre baixar o arquivo.
- **Sem spoilers**: summary e corpo descrevem premissa, não revelam reviravoltas.
- **Escalas de 0 a 5** (`rating`, `morbius`, e o que houver em `data/scales.yaml`): nunca perguntar o valor. Só registrar se o autor der o número. Mencionar no preview que estão disponíveis.
- Sem campo `lang`.
- Sem `Co-Authored-By Claude` no commit.
- Não tocar em `E:/silva/src/content/note/`.
- **Nunca inventar ficha técnica** — só registrar dados verificados.
- Build sanity check antes do commit.
