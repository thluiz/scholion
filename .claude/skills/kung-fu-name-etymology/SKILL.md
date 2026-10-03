---
name: kung-fu-name-etymology
description: Pesquisa etimologia de um nome kung fu chinês (nome Moy Yat / Ving Tsun) e cria nota de discípulo no Scholion com decomposição de ideogramas e etimologia das traduções em português. Confere existência (check-exists.mjs, moy-<slug>.md) e ideogramas nos documentos do clã antes de qualquer fetch.
argument-hint: "[ideogramas] [romanização] [traduções] [nome da pessoa se houver]"
---

# Etimologia de Nome Kung Fu

Recebe um nome kung fu em chinês e monta uma nota de discípulo (`moy-*.md`) no Scholion com:

- Decomposição de cada ideograma em radicais/componentes
- Etimologia chinesa (Shuowen Jiezi, formas antigas, fonologia)
- Etimologia das traduções em português/latim/grego
- **Cross-link** para a nota individual de cada ideograma (`etimologia-de-*.md`)

Fontes, URLs, gotchas, serialização, bloco `sources` e slug das notas de caractere: `E:/scholion/.claude/skills/research-chinese-etymology/references/fontes-etimologia.md`. Esta skill não repete isso.

## Parâmetros

`$ARGUMENTS` em formato livre. Extrair:
- **Ideogramas** (ex: 梅知友士)
- **Romanização** (ex: Moy Chi Yau Si)
- **Traduções de cada caractere** (ex: Chi = Saber, Conhecimento)
- **Nome da pessoa** (opcional, ex: Si Hing Vladimir Anchieta)

Se faltar ideograma ou romanização, perguntar.

## Passo 0 — pré-verificação (antes de QUALQUER fetch)

1. **Nota do discípulo**: `ls E:/scholion/content/notes/moy-<slug>.md`. Se existir, mostrar ao autor e perguntar: retomar, atualizar ou pular. Não redigir por cima sem resposta.
2. **Ideogramas e romanização na fonte primária do clã** (memórias `feedback_verificar_ideogramas`, `reference_kung_fu_docs`): conferir o nome em `C:/Users/conta/OneDrive/Kung Fu` — `TRANSLITERAÇÃO_OFICIAL_MYVTMI.pdf`, `Trasliterações.csv`, `MYVT/NOMES KUNG FU.pptx`, `membros.json`. Se o que o autor passou diverge do documento (ideograma, grafia da romanização), mostrar a divergência e esperar. Só depois ir às fontes acadêmicas.
3. **Notas de caractere**: `cd E:/scholion && node .claude/skills/research-chinese-etymology/check-exists.mjs <ideogramas sem 梅>`. Por caractere: `EXISTS` → linkar a nota existente, não pesquisar; `DUPLICATE` → avisar e perguntar qual linkar; `MISSING` → entra na lista de pesquisa.

## Duas etapas

1. **Para cada ideograma `MISSING`** (nunca 梅 — sobrenome, nota própria), invocar `research-chinese-etymology` com o contexto já em mãos (nome kung fu, pessoa) e criar a nota individual `etimologia-de-<jyutping>-<pinyin>-<hex>.md`. Um caractere de cada vez, preview por nota. Regras completas nessa skill.
2. **Criar a nota do discípulo** `moy-<slug>.md` com a estrutura abaixo.

## Slug da nota do discípulo

```
moy-<cantonês-todas-as-sílabas-hifenizadas>.md
```

Ex: `moy-chi-yau-si.md`, `moy-lei-wong.md`. A nota **não** leva codepoint — é identificação pessoal, não filológica. As sílabas são a romanização do clã (conferida no passo 0), não jyutping.

## Estrutura da nota do discípulo

```markdown
---
title: "<ideogramas> <Romanização>"
date: <timestamp ISO via `date +"%Y-%m-%dT%H:%M:%S%:z"`>
summary: "Etimologia do nome kung fu de <Pessoa>: <Char1> (<ideograma1>) <tradução curta>, <Char2> (<ideograma2>) <tradução curta>..."
tags: ["ving-tsun", "etimologia", "kung-fu", "moy-jo-lei-ou"]
toc: true
category: disciple
has_commentary: true
sources:
  # bloco canônico de fontes-etimologia.md (MDBG, chardb, CantoDict, hanziyuan, 小學堂, CUHK) — só as consultadas — mais:
  - title: "Priberam Dicionário"
    url: "https://dicionario.priberam.org"
    kind: wiki
---

**<ideogramas>**
*<Romanização>*

Nome kung fu de <Pessoa Real>.

梅 (Moy) é o sobrenome da linhagem — ver [Etimologia de 梅](/notes/etimologia-de-moy-mei/).

**<Char1>** (<ideograma1> <pinyin> / <jyutping>) – <traduções curtas>.

**<Char2>** (<ideograma2> <pinyin> / <jyutping>) – <traduções curtas>.

## Etimologia no Chinês

### <ideograma1> (<pinyin> / <jyutping>)

> Ver etimologia completa: [Etimologia de <ideograma1>](/notes/etimologia-de-<slug-do-char>/)

<Componente1> (<pinyin componente>) – <significado>
<Componente2> (<pinyin componente>) – <significado>

<Parágrafo curto com a imagem do caractere — como as fontes leem a decomposição. Seco, sem interpretar o kung fu.>

### <ideograma2> (<pinyin> / <jyutping>)

> Ver etimologia completa: [Etimologia de <ideograma2>](/notes/etimologia-de-<slug-do-char>/)

<mesmo formato>

### Divergências entre fontes

**<Char1>.** <Parágrafo comparando fontes — só o que importa para a leitura do nome; o detalhe está na nota do caractere.>

**<Char2>.** <idem>

## Etimologia do Português

**<Tradução 1>** – do <Lat./Gr./Fr.> *<étimo>*: <definições do Priberam>.

**<Tradução 2>** – <idem>.
```

Não há seção "Fontes Consultadas": os dados crus por caractere vivem nas notas `etimologia-de-*` linkadas. Se o autor quiser algo na própria nota, no máximo uma linha por caractere com MDBG + CantoDict (definição curta + jyutping).

## Regras críticas

### Voz e estilo
- Voz seca, sem floreio. Seguir `ghost-writer`.
- Os comentários sobre cada caractere ("Flecha e boca. Saber é acertar com a palavra.") devem soar como o autor: assertivos, sem mistificar.
- **NÃO editorializar** o significado do nome no contexto do kung fu ou da linhagem. A nota é referência, não comentário interpretativo.
- **NÃO comparar** com outros discípulos (ex: "é o mesmo 士 de Moy Chi Yau Si") — o cross-link para a etimologia individual já faz esse trabalho.

### Ideogramas e leituras
- 梅 nunca é decomposto nem reetimologizado aqui: uma linha linkando `/notes/etimologia-de-moy-mei/` (memória `feedback_link_moy_nao_duplicar`).
- Pinyin só do MDBG; jyutping só do CantoDict (nunca o `Trasliterações.csv` como pronúncia). A romanização do clã aparece só no título, no slug e nos rótulos **Chi**/**Yau**/**Si**.
- `(não retornou dados — <motivo>)` quando fonte falhar. NADA de invenção. zdic.net e shuowen.org estão mortos — não consultar nem listar (ver fontes-etimologia.md).

### Frontmatter
- **category: disciple** (obrigatório, ativa ícone 🙇 e borda violeta no Scholion)
- **has_commentary: true** — a nota tem comentário do autor no texto em português
- Tag `moy-jo-lei-ou` para aparecer na listagem da linhagem
- `sources`: só as fontes efetivamente consultadas (bloco canônico) + Priberam

### Cross-links
- Sob cada `### <ideograma> (<pinyin> / <jyutping>)` dentro de `## Etimologia no Chinês`, inserir o link completo para a nota do caractere (`[Etimologia de X](/notes/etimologia-de-…/)`), nunca só o slug em backticks (memória `feedback_links_internos_clicaveis`).
- O slug vem do `check-exists.mjs` (nota existente) ou da nota recém-criada; não deduzir.

### Preview e gravação
- Preview completo (frontmatter + corpo) antes de escrever cada nota. Aguardar confirmação.
- Timestamp real. Após confirmar: `Write` em `E:/scholion/content/notes/`, conferir que existe.
- Build check: `cd E:/scholion && hugo --quiet` uma vez antes do primeiro commit.

### Commit
- **Um commit por nota** (memória `feedback_commit_por_nota`): cada `etimologia-de-*` nova tem o seu (`note: etimologia de <CHAR>`), e a nota do discípulo tem o seu (`note: etimologia de <ideogramas> <Romanização>`). Sem bundle.
- **Sem `Co-Authored-By`**.
- O gate ghost-audit (hook PreToolUse em `git commit`) audita cada nota. Se bloquear: mostrar os findings ao autor, corrigir só o que melhora o texto por mérito próprio, e para o resto liberar com o override consciente — decisão do autor, comunicada como override (memória `feedback_ghost_audit_gate_estrito`):
  ```
  New-Item -ItemType Directory -Force E:\scholion\.ghost-audit | Out-Null
  $o = git rev-parse ":content/notes/<nota>.md"; Set-Content "E:\scholion\.ghost-audit\$o.ok" $o
  ```
  Nunca reescrever em loop para agradar o gate; nunca gravar o marcador sem o autor decidir.
- Push depois do último commit.

## Fluxo completo (pseudo-código)

```
0. Pré-verificação:
   - ls moy-<slug>.md → se existe, perguntar
   - conferir ideogramas/romanização em OneDrive/Kung Fu → divergência? perguntar
   - check-exists.mjs <ideogramas sem 梅> → EXISTS/DUPLICATE/MISSING por caractere
1. Extrair ideogramas, romanização, pessoa
2. Para cada ideograma MISSING (um de cada vez):
   - research-chinese-etymology com contexto → preview → Write → commit próprio
3. Draftar a nota do discípulo moy-<slug>.md (links para as notas de caractere)
4. Preview ao autor
5. Após confirmação: Write, hugo --quiet, commit próprio, push
```
