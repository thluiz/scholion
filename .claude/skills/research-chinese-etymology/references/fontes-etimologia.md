# Fontes de etimologia chinesa — referência comum

Lida por `research-chinese-etymology`, `kung-fu-name-etymology` e `transfer-etymology-from-scholion`. Mudança de fonte, URL, bloco `sources` ou convenção de slug entra aqui, não nas skills.

## As fontes (6 sites, 7 consultas)

O crawler (`crawl-radical.mjs`) consulta 6 sites; o 小學堂 entra duas vezes (formas e fonologia), daí "7 fontes" nos dumps e no preset `scholion/etymology-note`.

| # | Fonte | URL de consulta | O que fornece | Acesso |
|---|---|---|---|---|
| 1 | MDBG Chinese Dictionary | `https://www.mdbg.net/chinese/dictionary?wdqb=<CHAR>` | definições em inglês, **pinyin canônico**, jyutping de apoio | crawler; WebFetch funciona |
| 2 | chardb — 教育部異體字字典 (Academia Sinica) | `https://chardb.iis.sinica.edu.tw/search.jsp?stype=1&q=<CHAR>` → `/char/<ID>` | definições chinesas numeradas (字義/釋義), radical, traços, zhuyin, variantes | crawler (já resolve o `/char/<ID>`); WebFetch funciona em 2 passos |
| 3 | CantoDict (cantonese.org) | `https://www.cantonese.org/search.php?q=<CHAR>` | **jyutping canônico** com tom, compostos cantoneses | crawler; WebFetch funciona |
| 4 | Chinese Etymology (hanziyuan.net, Richard Sears) | `https://hanziyuan.net/#<CHAR>` | formas Oracle/Bronze/Seal (contagens nos cabeçalhos), sentido original, Shuowen resumido | **só Playwright** (rota por hash, renderização JS) |
| 5a | 小學堂 yanbian (Academia Sinica) | `https://xiaoxue.iis.sinica.edu.tw/yanbian?char=<CHAR>` | tabela de evolução de formas (período, script, artefato), Shuowen inline, comentários 今按 | **só Playwright** |
| 5b | 小學堂 shangguyin (Academia Sinica) | `https://xiaoxue.iis.sinica.edu.tw/shangguyin?char=<CHAR>` | 中古音 (廣韻: 攝/韻/聲/母/反切/等/開合/清濁), 上古音 (Karlgren, 王力, 董同龢, 周法高, 李方桂, 鄭張尚芳), IPA do mandarim | **só Playwright** |
| 6 | 漢語多功能字庫 (CUHK) | `https://humanum.arts.cuhk.edu.hk/Lexis/lexi-mf/search.php?word=<CHAR>` | Shuowen, etimologia interpretativa (略說/詳解/形義通解), cantonês com tom, índices 甲骨/金文 | crawler; WebFetch funciona |

### Gotchas por fonte

- **chardb**: a busca devolve lista, não ficha. Seguir o link `/char/<ID>` cujo texto é exatamente o caractere (os outros links `/char/` são barra lateral). Variante sem entrada própria devolve só a lista → `(não retornou dados — chardb retornou apenas lista, sem ficha)`. O contador de derivados (部件) é renderizado por JS e o crawler não o captura.
- **hanziyuan**: `常用频率: 99999` é sentinela de "sem ranking", não frequência alta. O fetch nem sempre traz as contagens por tipo de forma; nesse caso usar a tabela do 小學堂. A cauda institucional da página (doações, biografia, notícias) é ruído — `audit-crawl.mjs` corta.
- **小學堂 shangguyin**: a coluna 鄭張尚芳 costuma vir vazia → `(não retornou dados — ausente da tabela do 小學堂)`. Reconstruções vêm em 聲母 + 韻母 separados; concatenar é apresentação fiel.
- **CUHK**: o campo 普通話 chega com diacríticos mutilados pelo crawler (`pn qing` = pán/qiáng); não usar para pinyin. Os rótulos 略說/詳解/形義通解 são da CUHK; 今按 é do 小學堂 — não trocar a atribuição.
- **Shuowen**: vem convergente de hanziyuan + CUHK + 小學堂 (yanbian inline). Conferir que as três batem antes de citar como verbatim. O 段注 (Duan Yucai) não está em nenhuma das seis fontes vivas.

## Fontes mortas ou inúteis — não consultar, não listar em `sources`

- `https://www.zdic.net/hans/<CHAR>` — HTTP 404 via WebFetch (observação recorrente no projeto dos radicais Kangxi). Era o fallback do 段注; sem ela, o 段注 fica sem fonte.
- `https://www.shuowen.org/?kw=<CHAR>` — devolve só a listagem das 10 primeiras entradas do dicionário (一, 元, 天…), nunca a entrada pedida.
- `xiaoxue.iis.sinica.edu.tw/shuowen`, `/ccdb`, `/zhongguyin` — 404 / homepage / sem retorno; tudo coberto por yanbian e shangguyin.

Notas antigas citam zdic.net e shuowen.org no `sources`; não repetir em notas novas. Citar fonte não consultada fere source-or-silence.

## Serialização (memória `feedback_etimologia_serial_e_completa`)

- **Um caractere de cada vez.** Nunca subagents paralelos por caractere, nunca dois crawlers ao mesmo tempo.
- **Dentro de um caractere, fetches em sequência.** O crawler já faz isso (loop `for … await`). No fallback manual (WebFetch / `fetch-*.mjs`), também em sequência; a única concorrência tolerada é entre scripts node de **sites distintos** (ex.: `fetch-hanziyuan.mjs` com um dos `fetch-xiaoxue-*.mjs`), nunca os dois xiaoxue juntos.
- As fontes são projetos acadêmicos e comunitários sustentados por doação; a cadência serial é comportamento responsável de cliente, não otimização.

## Bloco `sources` canônico (= gabarito `content/notes/etimologia-de-seoi-shui-6c34.md`)

```yaml
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
- title: 漢語多功能字庫 (CUHK)
  url: https://humanum.arts.cuhk.edu.hk/Lexis/lexi-mf/
  kind: wiki
```

Se uma fonte ficou `(FONTE INDISPONÍVEL)` no dump e nada dela entrou na nota, tirar a entrada correspondente do bloco.

## Leituras

- **Pinyin**: só do MDBG (com tom na prosa e no título; sem diacrítico no slug). Nunca do campo 普通話 da CUHK.
- **Jyutping**: só do CantoDict (com tom). MDBG e CUHK servem para cruzar, não como fonte da leitura.
- **Nunca** o `Trasliterações.csv` nem a romanização interna do clã como pronúncia (memória `feedback_pronuncias_ideogramas`). A romanização do clã (mordente) só aparece onde é dado do clã: título da nota de discípulo e campo `mordente` do dicionário — e vem dos documentos oficiais em `C:/Users/conta/OneDrive/Kung Fu` (`TRANSLITERAÇÃO_OFICIAL_MYVTMI.pdf`, `Trasliterações.csv`, `HAI TONG por MOY YAT.txt`).

## Título e slug

Título:

```
title: "Etimologia de <CHAR> (<Jyutping sem tom, capitalizado> — <Pinyin com tom> / <jyutping com tom>)"
```

Ex.: `Etimologia de 水 (Seoi — Shuǐ / seoi2)`.

Slug único por caractere:

```
etimologia-de-<jyutping-sem-tom>-<pinyin-sem-diacrítico-sem-tom>-<hex-do-codepoint>.md
```

Ex.: 水 seoi2 / shuǐ / U+6C34 → `etimologia-de-seoi-shui-6c34.md`. Hex em minúsculas, 4+ dígitos (`ch.codePointAt(0).toString(16)`).

O primeiro token é **jyutping do CantoDict**, não a romanização do autor nem a do clã. Foi a romanização livre que gerou as duplicatas conhecidas (握 `aak-wo` + `ak-wo-63e1`; 馬 `ma-ma` + `maa-ma-99ac`; 山 `shan-shan` + `saan-shan-5c71`). Notas legadas sem hex não são renomeadas em massa; `check-exists.mjs` as encontra pelo título.

## Marcadores de ausência (convenção atual)

Campo sem dado: `(não obtido — <motivo>)` ou `(não retornou dados — <motivo>)`. O preset `scholion/etymology-note` e `source-audit.mjs` reconhecem esses marcadores e não os flagram. A revisão de 2026-10-03 apontou tensão com a regra do CLAUDE.md (não narrar processo na nota); a decisão é do autor e, até ela, a convenção fica como está.
