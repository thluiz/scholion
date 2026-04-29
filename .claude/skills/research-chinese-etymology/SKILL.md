---
name: research-chinese-etymology
description: Pesquisa etimologia de caracteres chineses consultando 7 fontes acadêmicas (MDBG, chardb/xiaoxue Academia Sinica, hanziyuan, shuowen.org, CantoDict). Checa se a nota já existe antes de pesquisar. Salva como `etimologia-de-*.md` no Scholion após preview aprovado, em português brasileiro.
argument-hint: "[caracteres] ex: 知友士"
---

# Pesquisa Etimológica de Caracteres Chineses

Recebe um ou mais caracteres chineses, produz análise etimológica completa de cada um (consultando 7 fontes) e **salva como nota no Scholion** (`E:/scholion/content/notes/etimologia-de-*.md`) após preview aprovado pelo autor.

A skill **checa se a etimologia já existe antes de pesquisar** — pesquisa em 7 fontes é cara e não deve ser repetida.

## Parâmetros

Extrair caracteres CJK de `$ARGUMENTS`. Pode ser 1 ou mais caracteres (ex: `德`, `知友士`).

Se `$ARGUMENTS` não contiver caracteres CJK, perguntar.

## Verificação prévia (ANTES de qualquer fetch)

Para cada caractere, checar se já existe nota:

1. **Por unicode hex** (slug moderno): `Glob` em `E:/scholion/content/notes/etimologia-de-*-<unicode>.md` (4+ dígitos hex minúsculos do codepoint).
2. **Por caractere no título** (notas legadas pré-2026-04-23 sem unicode no slug): `Grep` por `"Etimologia de <CHAR>"` no frontmatter `title:` em `E:/scholion/content/notes/etimologia-de-*.md`.

Se existir nota, perguntar ao autor: **"Já existe `<slug>.md`. Atualizar (refazer pesquisa), pular, ou só ler o conteúdo atual?"** — não decidir sozinho.

Apenas após confirmação de que não existe (ou que deve atualizar), proceder à pesquisa.

## Fontes e como acessar

Processar cada caractere por TODAS as fontes abaixo. Usar Agent com subagents em paralelo quando possível.

### 1. MDBG — definições e pronúncias (WebFetch)

- URL: `https://www.mdbg.net/chinese/dictionary?wdqb=CHAR`
- Extrair: definições inglesas, pinyin, jyutping
- Fonte rápida e fiável para significados modernos

### 2. chardb Academia Sinica — definições chinesas (WebFetch)

- URL: `https://chardb.iis.sinica.edu.tw/search.jsp?stype=1&q=CHAR`
- Extrair: definições chinesas numeradas, tradução inglesa, radical, traços, unicode, zhuyin, pinyin
- **Gotcha**: quando o caractere tem variantes, a busca retorna uma lista em vez de ficha direta. Nesse caso, seguir o link `/char/ID` do primeiro resultado.
- Todas as definições chinesas devem ser preservadas verbatim + tradução inglesa entre parênteses

### 3. CantoDict / cantonese.org — jyutping cantonês (WebFetch)

- URL: `https://www.cantonese.org/search.php?q=CHAR`
- Extrair: leitura jyutping com tons
- Cruzar com MDBG e shangguyin para confirmar

### 4. hanziyuan.net — decomposição e formas antigas (Playwright script)

- Script fixo: `node E:/scholion/.claude/skills/research-chinese-etymology/fetch-hanziyuan.mjs CHAR`
- Extrair: decomposição em componentes, significado original, Shuowen básico, contagem de formas antigas (Oracle/Bronze/Seal)

### 5. xiaoxue yanbian — evolução de formas (Playwright script)

- Script fixo: `node E:/scholion/.claude/skills/research-chinese-etymology/fetch-xiaoxue-yanbian.mjs CHAR`
- Extrair: evolução de formas com períodos/dinastias/artefatos, Shuowen inline + comentários de estudiosos
- **Tudo traduzido**: dinastias, períodos, estados, scripts, artefatos (com pinyin quando relevante)
- Comentários de estudiosos: chinês original + inglês entre parênteses

### 6. shuowen.org — Shuowen Jiezi completo + 段注 (WebFetch)

- URL: `https://www.shuowen.org/?kw=CHAR`
- Extrair: texto completo do Shuowen Jiezi + 段注 Duan Yucai (comentário Qing dynasty)
- Formato: chinês original verbatim + tradução inglesa entre parênteses
- 段注 é frequentemente longo — incluir na íntegra, traduzido
- **Gotcha comum (2026-04-23)**: esta URL frequentemente retorna só a listagem das 10 primeiras entradas do dicionário (一, 元, 天...) em vez do caractere solicitado. Site paginado, não retorna entrada individual via query string. Quando isso acontecer, usar **fallback zdic.net** e marcar explicitamente na nota:
  ```
  **段注 Duan Yucai** (paráfrase via zdic.net — texto verbatim de shuowen.org não obtido para este caractere): ...
  ```

### 6b. zdic.net — fallback para Shuowen + 段注 (WebFetch)

- URL: `https://www.zdic.net/hans/CHAR`
- Fallback quando shuowen.org falha (frequente)
- Contém 說文解字 + 段玉裁注 em formato estruturado
- Retornado como paráfrase/síntese — marcar como tal na nota

### 7. xiaoxue shangguyin — fonologia (Playwright script)

- Script fixo: `node E:/scholion/.claude/skills/research-chinese-etymology/fetch-xiaoxue-shangguyin.mjs CHAR`
- Extrair:
  - 中古音 Middle Chinese (Guangyun): 攝 division, 韻 rhyme, 聲 tone, 母 initial, 反切 fanqie, 等 grade
  - 上古音 Old Chinese: 5 sistemas de reconstrução (王力 Wang Li, 董同龢 Dong Tonghe, 周法高 Zhou Fagao, 李方桂 Li Fanggui, 鄭張尚芳 Zhengzhang Shangfang)
  - 國語 Mandarin IPA
- Traduzir todos os termos técnicos: 攝→division, 聲→tone, 韻→rhyme, 母→initial, 反切→fanqie, 等→grade, 開→open, 合→closed

### 8. CUHK 漢語多功能字庫 — enriquecimento opcional (WebFetch)

- URL: `https://humanum.arts.cuhk.edu.hk/Lexis/lexi-mf/search.php?word=CHAR`
- Usar quando as outras fontes não bastam ou para cruzar interpretações
- Extrair: Shuowen, cantonês com tons, etimologia interpretativa

## Fontes que NÃO funcionam (não usar)

- `xiaoxue.iis.sinica.edu.tw/shuowen?char=X` — retorna 404, FORA DO AR. O Shuowen está inline no yanbian.
- `xiaoxue.iis.sinica.edu.tw/ccdb` — retorna homepage, dados cobertos pelo shangguyin.
- `xiaoxue.iis.sinica.edu.tw/zhongguyin` — não funciona, dados cobertos pelo shangguyin.

## Formato de output por caractere

Para cada caractere, produzir:

```
### X

**X** — U+XXXX · 部首 radical: X · 總筆畫 strokes: N · 注音 zhuyin: X · 拼音 pinyin: X / jyutping: X

#### Definições

**MDBG**: [definições inglesas]

**CantoDict**: jyutpingX (tom)

**chardb Academia Sinica**:
1. [definição chinesa verbatim] ([tradução inglesa])
2. ...

#### Decomposição e formas antigas (hanziyuan)

Componentes: [lista]
Significado original: [do hanziyuan]
Shuowen (hanziyuan): [texto]
Formas atestadas: Oracle N · Bronze N · Seal N

#### Shuowen Jiezi completo (shuowen.org)

**說文**: [texto chinês original] ([tradução inglesa])

**段注 Duan Yucai**: [texto chinês original] ([tradução inglesa])

#### Evolução de formas (xiaoxue yanbian)

| Período | Script | Fonte/Artefato | Forma |
|---------|--------|----------------|-------|
| [período traduzido] | [script traduzido] | [fonte traduzida] | [descrição] |

**Shuowen (xiaoxue)**: [texto inline] ([tradução])

**Comentários de estudiosos**:
- [estudioso]: [chinês] ([inglês])

#### Fonologia (xiaoxue shangguyin)

**中古音 Middle Chinese (Guangyun)**:
- 攝 Division: X · 韻 Rhyme: X · 聲 Tone: X · 母 Initial: X
- 反切 Fanqie: X · 等 Grade: X · 開合 Open/Closed: X

**上古音 Old Chinese**:
- 王力 Wang Li: X
- 董同龢 Dong Tonghe: X
- 周法高 Zhou Fagao: X
- 李方桂 Li Fanggui: X
- 鄭張尚芳 Zhengzhang Shangfang: X

**國語 Mandarin IPA**: X

#### Divergências entre fontes

[Para cada divergência encontrada NESTE caractere, um parágrafo curto identificando:]
- Contagens de atestações: xiaoxue frequentemente corrige hanziyuan (mais preciso em Oracle/Bronze/Seal)
- Significado primário: Shuowen/chardb def.1 vs MDBG vs hanziyuan "original meaning"
- Decomposição: fonética vs semântica — fontes podem divergir
- Acepções exclusivas do chardb (definições que MDBG não tem)
- Comentários de estudiosos do xiaoxue e 段注 do shuowen.org que contradizem ou expandem o Shuowen
- Leitura cantonesa: confirmar jyutping entre MDBG, cantonese.org e shangguyin
```

IMPORTANTE: as divergências ficam DENTRO da secção de cada caractere (como `####` subsecção), não numa secção global separada. Isto centraliza a leitura — o leitor vê tudo sobre um caractere sem ter de saltar para o fim do documento.

## Regras de tradução obrigatórias

1. **Definições chardb**: chinês verbatim + inglês entre parênteses
2. **Shuowen e comentários**: chinês original + inglês entre parênteses
3. **段注 Duan Yucai**: chinês original completo + inglês entre parênteses
4. **Evolução de formas**: TUDO traduzido — dinastias, períodos, estados, scripts, artefatos (com pinyin)
5. **Fonologia**: termos técnicos traduzidos (攝→division, 聲→tone, 韻→rhyme, 母→initial, 反切→fanqie, 等→grade, 開→open, 合→closed, 平→level, 上→rising, 去→departing, 入→entering)

## Português brasileiro

A prosa da nota — texto explicativo, divergências, decomposição, descrições de fontes — deve estar em **português brasileiro**. Glossário rápido das trocas mais comuns:

| ❌ PT-PT | ✅ PT-BR |
|---------|---------|
| registado / regista / registam | registrado / registra / registram |
| registo | registro |
| polissémica | polissêmica |
| icónico/a | icônico/a |
| anatómico/a | anatômico/a |
| carácter (sentido tipográfico) | caractere |
| dialectologia | dialetologia |
| ficheiro | arquivo |
| secção / subsecção | seção / subseção |
| standard (anglicismo) | padrão |
| "o seu vocabulário" (artigo + possessivo) | "seu vocabulário" |
| consoante | conforme |

Não traduzir termos técnicos chineses (Shuowen, fanqie, 段注, etc.) nem o vocabulário linguístico de origem latina universal (radical, fonético, semântico, dialeto, fonossemântico).

## Datação sem fonte

Para caracteres ausentes do corpus filológico clássico (Shuowen, Guangyun, Kangxi), **não atribuir datação histórica como fato** ("Ming–Qing", "atestação mais antiga é tardia", "criação recente") a menos que uma fonte concreta consultada o sustente. Quando a inferência for razoável mas não verificada, marcá-la explicitamente como tal.

- ❌ "A atestação mais antiga de uso escrito é tardia (Ming–Qing em textos cantoneses regionais)."
- ❌ "É composto semântico puro de criação recente."
- ✅ "Atestação mais antiga datável: requer estudo de corpus cantonês vernacular (não verificada nas fontes consultadas)."
- ✅ "Provavelmente criação letrada cantonesa tardia — inferência a partir do registro 方言, sem datação direta nas fontes."

A observação positiva que sempre pode ser feita com segurança: "ausente do *Shuowen* (Han), *Guangyun* (Song), *Kangxi Zidian* (Qing); presente apenas em referência moderna como o *Hanyu Da Zidian*, sob etiqueta 方言."

## Playwright — scripts e infra

- Playwright instalado globalmente (`npm install -g playwright`), browsers em `C:\Users\conta\AppData\Local\ms-playwright\`
- **Scripts fixos** na pasta da skill (NÃO gerar scripts em runtime):
  - `fetch-hanziyuan.mjs CHAR` — hanziyuan.net
  - `fetch-xiaoxue-yanbian.mjs CHAR` — xiaoxue yanbian
  - `fetch-xiaoxue-shangguyin.mjs CHAR` — xiaoxue shangguyin
- Executar via Bash: `node E:/scholion/.claude/skills/research-chinese-etymology/fetch-*.mjs CHAR`
- Os 3 scripts podem rodar em paralelo para o mesmo caractere
- **Se Playwright não estiver disponível**: avisar e continuar com fontes WebFetch-only (MDBG, chardb, cantonese.org, shuowen.org), sinalizando no output quais fontes ficaram pendentes

## Estratégia de execução

1. **Extrair** caracteres de `$ARGUMENTS`.
2. **Verificação prévia**: para cada caractere, checar se já existe nota (ver secção acima). Se existir, perguntar ao autor antes de prosseguir.
3. **Coletar contexto kung fu** (a menos que invocada por outra skill que já passe o contexto): perguntar ao autor de qual nome kung fu o caractere vem e qual a pessoa. Aceitar "nenhum" para registro filológico sem vínculo.
4. **Pesquisar** (apenas para caracteres sem nota ou que devem ser atualizados): para cada caractere, lançar buscas em paralelo (Agent subagents ou tool calls paralelos):
   - WebFetch: MDBG, chardb, cantonese.org, shuowen.org (4 em paralelo)
   - Playwright: hanziyuan, xiaoxue yanbian, xiaoxue shangguyin (podem ser paralelos se infra permitir)
5. **Formatar** output por caractere no formato acima.
6. **Cruzar fontes** e listar divergências.
7. **Preview**: montar a nota completa (frontmatter + corpo) e mostrar ao autor antes de gravar. Aguardar aprovação explícita.
8. **Salvar** após aprovação (ver secção "Salvamento da nota" abaixo).

## Salvamento da nota

Após preview aprovado pelo autor, gravar em `E:/scholion/content/notes/<slug>.md`:

1. **Timestamp real** — capturar via `Bash`: `date +"%Y-%m-%dT%H:%M:%S%:z"`. Nunca inventar hora.
2. **Write** o ficheiro completo (frontmatter + corpo).
3. **Verificar** com `Glob` ou `Read` que o ficheiro existe — só então confirmar ao autor com path resultante.
4. **Não comitar automaticamente** — esta skill apenas grava. Commit fica a cargo do autor (ou da skill orquestradora, ex: `/kung-fu-name-etymology`).

### Slug

```
etimologia-de-<cantonês-autor>-<pinyin>-<unicode-hex>.md
```

- `<cantonês-autor>` — romanização usada pelo autor (do nome kung fu ou contexto onde o caractere aparece)
- `<pinyin>` — pinyin sem diacrítico e sem tom
- `<unicode-hex>` — codepoint em 4+ dígitos hex minúsculos (ex: `738b` para 王, `4f9d` para 依)

Exemplo: `etimologia-de-wong-wang-738b.md` (王).

**Motivação**: elimina colisões de slug entre caracteres com mesmo cantonês+pinyin. Notas anteriores a 2026-04-23 mantêm slugs legados (`lou-lao.md`/`lou-lao2.md` com sufixo numérico) — não renomear em massa.

### Frontmatter obrigatório

```yaml
---
title: "Etimologia de <CHAR> (<Cantonês> — <Pinyin> / <jyutping>)"
date: '<timestamp ISO>'
summary: "..."
toc: true
tags: ["china", "linguagem", "etimologia", "ving-tsun", "ideogramas"]
category: etymology
has_commentary: false
sources:
- title: MDBG Chinese Dictionary
  url: https://www.mdbg.net/chinese/dictionary
  kind: wiki
- title: chardb — Academia Sinica
  url: https://chardb.iis.sinica.edu.tw
  kind: wiki
- title: CantoDict (cantonese.org)
  url: https://www.cantonese.org
  kind: wiki
- title: Chinese Etymology (hanziyuan.net)
  author: Richard Sears
  url: https://hanziyuan.net
  kind: wiki
- title: 小學堂 — Academia Sinica
  url: https://xiaoxue.iis.sinica.edu.tw
  kind: wiki
- title: 說文解字 (via zdic.net)
  url: https://www.zdic.net
  kind: wiki
---
```

**category: etymology** ativa o tipo visual 📜 no Scholion (ícone no card, borda âmbar, badge na single). Sem isso, a nota sai sem identificação de tipo.

### Nome kung fu de origem (primeiro parágrafo)

Formato: **"É o \<Pinyin\> do nome kung fu de \<Pessoa Real\> ([Moy X Y Z](/notes/moy-x-y-z/))."** — pessoa primeiro, nome kung fu em parênteses e linkado.

Quando o caractere aparece em múltiplos nomes: **"É o \<Pinyin\> de N nomes da linhagem: [Moy A B](/notes/moy-a-b/), [Moy C D](/notes/moy-c-d/)..."** — todos os nomes kung fu linkados às respectivas notas de discípulo em `/notes/moy-*/`.

**NÃO usar** "nome de linhagem" — é invenção, o termo correto é "nome kung fu".

## Regra de integridade (anti-alucinação)

**NADA de invenção.** Quando uma fonte não retorna dados para um campo, marcar explicitamente:

```
**<Campo>**: (não retornou dados — <motivo curto>)
```

Exemplos vistos na prática:
- `(não retornou dados — script fetch-hanziyuan timeout persistente)` — hanziyuan offline
- `(não retornou dados — ausente da tabela xiaoxue)` — coluna OC vazia
- `(não retornou dados — 勣 não tem entrada própria no Shuowen)` — caractere raro/tardio
- `(não retornou dados — chardb retornou apenas lista, sem ficha)` — variante sem entrada
- `(paráfrase via zdic.net — texto verbatim de shuowen.org não obtido)` — fallback

Caracteres tardios (pós-Warring States, ex: 勣, 奜, 鑰, 讜, 懃) legitimamente têm 5+ "não retornou dados" por ausência epigráfica real. Não forçar dados.

## Não editorializar

As notas de etimologia são referência objetiva. **Não inserir** bullets ou parágrafos interpretando o significado do ideograma no contexto da linhagem Moy Yat, no nome do discípulo, ou no kung fu. A frase de abertura ("É o X do nome kung fu de Pessoa (Moy ...)") é exceção legítima — apenas identifica de qual nome o caractere vem.

Exemplos do que NÃO incluir (incidente 2026-04-23):
- "優 em Moy Yau Lei é o ideograma central do nome — combina excelência com a ressonância do ator ritual."
- "É o mesmo 士 usado em Moy Chi Yau Si e Moy Shan Si."

## Notas

- Esta skill **cria a nota** em `E:/scholion/content/notes/etimologia-de-*.md` após preview aprovado, mas **não comita** — o commit fica com o autor ou a skill orquestradora.
- Pode ser invocada por outras skills (ex: `kung-fu-name-etymology`) para a parte chinesa. Quando invocada com contexto kung fu já fornecido, não perguntar de novo.
- Caracteres raros podem não ter entrada em todas as fontes — sinalizar quando uma fonte não retorna dados.
