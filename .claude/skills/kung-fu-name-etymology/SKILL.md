---
name: kung-fu-name-etymology
description: Pesquisa etimologia de um nome kung fu chinês (nome Moy Yat / Ving Tsun) e cria nota de discípulo no Scholion com decomposição de ideogramas e etimologia das traduções em português.
argument-hint: "[ideogramas] [romanização] [traduções] [nome da pessoa se houver]"
---

# Etimologia de Nome Kung Fu

Recebe um nome kung fu em chinês e monta uma nota de discípulo (`moy-*.md`) no Scholion com:

- Decomposição de cada ideograma em radicais/componentes
- Etimologia chinesa (Shuowen Jiezi, formas antigas, fonologia)
- Etimologia das traduções em português/latim/grego
- Divergências entre fontes
- **Cross-link** para a nota individual de cada ideograma (`etimologia-de-*.md`)

## Parâmetros

`$ARGUMENTS` em formato livre. Extrair:
- **Ideogramas** (ex: 梅知友士)
- **Romanização** (ex: Moy Chi Yau Si)
- **Traduções de cada caractere** (ex: Chi = Saber, Conhecimento)
- **Nome da pessoa** (opcional, ex: Si Hing Vladimir Anchieta)

Se faltar ideograma ou romanização, perguntar.

## Duas etapas

1. **Para cada ideograma** (exceto 梅 — sobrenome, já tem nota), invocar a skill `research-chinese-etymology` e, se ainda não existir, criar a nota individual `etimologia-de-<cantonês>-<pinyin>-<unicode-hex>.md` em `E:/scholion/content/notes/`. Ver regras completas nessa skill.
2. **Criar a nota do discípulo** `moy-<slug>.md` com estrutura abaixo.

## Slug da nota do discípulo

```
moy-<cantonês-todas-as-sílabas-hifenizadas>.md
```

Ex: `moy-chi-yau-si.md`, `moy-lei-wong.md`. Note que a nota **não** leva codepoint — é identificação pessoal, não filológica.

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
  - title: "MDBG Chinese Dictionary"
    url: "https://www.mdbg.net/chinese/dictionary"
    kind: wiki
  - title: "chardb — Academia Sinica"
    url: "https://chardb.iis.sinica.edu.tw"
    kind: wiki
  - title: "CantoDict (cantonese.org)"
    url: "https://www.cantonese.org"
    kind: wiki
  - title: "Chinese Etymology (hanziyuan.net)"
    author: "Richard Sears"
    url: "https://hanziyuan.net"
    kind: wiki
  - title: "小學堂 — Academia Sinica"
    url: "https://xiaoxue.iis.sinica.edu.tw"
    kind: wiki
  - title: "說文解字 (via zdic.net)"
    url: "https://www.zdic.net"
    kind: wiki
  - title: "Priberam Dicionário"
    url: "https://dicionario.priberam.org"
    kind: wiki
---

**<ideogramas>**
*<Romanização>*

Nome kung fu de <Pessoa Real>.

**<Char1>** (<ideograma1> <pinyin> / <jyutping>) – <traduções curtas>.

**<Char2>** (<ideograma2> <pinyin> / <jyutping>) – <traduções curtas>.

## Etimologia no Chinês

### <ideograma1> (<pinyin> / <jyutping>)

> Ver etimologia completa: [`/notes/etimologia-de-<slug-do-char>/`](/notes/etimologia-de-<slug-do-char>/)

<Componente1> (<pinyin componente>) – <significado>
<Componente2> (<pinyin componente>) – <significado>

<Parágrafo curto com imagem do caractere — como as fontes leem a decomposição. Seco, sem interpretar o kung fu.>

### <ideograma2> (<pinyin> / <jyutping>)

> Ver etimologia completa: [`/notes/etimologia-de-<slug-do-char>/`](/notes/etimologia-de-<slug-do-char>/)

<mesmo formato>

### Divergências entre fontes

**<Char1>.** <Parágrafo comparando fontes — chardb acepções exclusivas, hanziyuan leitura alternativa, 段注 refinamento. Fatos filológicos, não interpretação.>

**<Char2>.** <idem>

## Etimologia do Português

**<Tradução 1>** – do <Lat./Gr./Fr.> *<étimo>*: <definições do Priberam>.

**<Tradução 2>** – <idem>.

## Fontes Consultadas

### MDBG

<dados crus MDBG por caractere>

### Chinese Etymology

<dados crus hanziyuan por caractere>

### CantoDict

<jyutping por caractere>

### Academia Sinica — 教育部異體字字典 (chardb)

<acepções chardb por caractere>

### 小學堂

<dados xiaoxue (yanbian + shangguyin) por caractere>
```

## Regras críticas

### Voz e estilo
- Voz seca, sem floreio. Seguir `ghost-writer` skill.
- Os comentários sobre cada caractere ("Flecha e boca. Saber é acertar com a palavra.") devem soar como o autor: assertivos, sem mistificar.
- **NÃO editorializar** o significado do nome no contexto do kung fu ou da linhagem. A nota é referência, não comentário interpretativo.
- **NÃO comparar** com outros discípulos (ex: "é o mesmo 士 de Moy Chi Yau Si") — o cross-link para a etimologia individual já faz esse trabalho.

### Ideogramas e fontes
- O primeiro ideograma do nome (梅/Moy) é o sobrenome — não decompor a menos que o usuário peça.
- Consultar as 7 fontes via `research-chinese-etymology` para cada ideograma (exceto 梅).
- `(não retornou dados — <motivo>)` quando fonte falhar. NADA de invenção.
- Se `shuowen.org` falhar, usar `zdic.net` e marcar como `(paráfrase via zdic.net)`.

### Frontmatter
- **category: disciple** (obrigatório, ativa ícone 🙇 e borda violeta no Scholion)
- **has_commentary: true** — a nota tem comentário do autor no texto em português
- Tag `moy-jo-lei-ou` para aparecer na listagem da linhagem
- 7 sources (6 chinesas + Priberam)

### Cross-links
- Sob cada `### <ideograma> (<pinyin> / <jyutping>)` dentro de `## Etimologia no Chinês`, inserir:
  ```
  > Ver etimologia completa: [`/notes/etimologia-de-<slug>/`](/notes/etimologia-de-<slug>/)
  ```
- Se a nota individual do caractere ainda não existir, criá-la primeiro via `research-chinese-etymology` (seguindo a convenção `etimologia-de-<cant>-<pinyin>-<hex>.md`).

### Commit
- Um commit por fluxo: a nota do discípulo + eventuais notas individuais novas. (Exceção consciente à regra geral de um commit por nota — `feedback_commit_por_nota` — porque as notas de etimologia individuais nascem como dependência da nota do discípulo neste fluxo.)
- Mensagem: `note: etimologia de <ideogramas> <Romanização>`.
- **Sem `Co-Authored-By Claude`**.
- Build check: `cd E:/scholion && hugo --quiet` antes de comitar.
- O hook global `ghost-audit` audita as notas staged no commit. Se bloquear (verdict red), resolver os findings — nunca gravar o marcador `.ghost-audit/*.ok` só para furar o bloqueio sem o autor decidir.

### Preview
- Preview antes de escrever. Aguardar confirmação do usuário.
- Após confirmar: criar em `E:/scholion/content/notes/`, commit e push.

## Fluxo completo (pseudo-código)

```
1. Extrair ideogramas, romanização, pessoa
2. Para cada ideograma (exceto 梅):
   a. Determinar slug do caractere (<cant>-<pinyin>-<hex>)
   b. Se nota etimologia-de-<slug>.md não existe:
      - Invocar research-chinese-etymology
      - Criar nota individual com category: etymology
3. Draftar a nota do discípulo moy-<slug>.md
4. Preview ao usuário
5. Após confirmação:
   - Write nota(s)
   - hugo --quiet
   - git add + commit + push
```
