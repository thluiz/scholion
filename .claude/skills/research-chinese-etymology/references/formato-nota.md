# Formato da nota de etimologia

Gabarito: `E:/scholion/content/notes/etimologia-de-seoi-shui-6c34.md` (水). Segundo exemplo: `etimologia-de-sau-shou-624b.md` (手). Replicar a estrutura, não resumir.

## Frontmatter

```yaml
---
title: "Etimologia de <CHAR> (<Jyutping sem tom, capitalizado> — <Pinyin com tom> / <jyutping com tom>)"
date: '<timestamp ISO real — `date +"%Y-%m-%dT%H:%M:%S%:z"`>'
summary: '<1 frase, ~150-200 caracteres; aspas simples se tiver `:`>'
toc: true
tags: ["china", "linguagem", "etimologia", "ving-tsun", "ideogramas"]
category: etymology
has_commentary: false
sources:
  # bloco canônico — ver references/fontes-etimologia.md
---
```

- `category: etymology` ativa o tipo visual (ícone no card, borda âmbar, badge na single). Sem isso a nota sai sem identificação de tipo.
- Tags: caractere vindo de nome kung fu ou do *Hai Tong* leva `ving-tsun`; radical Kangxi leva `radicais` no lugar de `ving-tsun` (como no gabarito).
- `summary` com `:` precisa de aspas simples (memória `feedback_yaml_summary_aspas`).

## Abertura (primeiro parágrafo)

Só identifica de onde o caractere vem. Variantes aceitas:

- **Nome kung fu de uma pessoa**: `É o <Pinyin> do nome kung fu de <Pessoa Real> ([Moy X Y Z](/notes/moy-x-y-z/)).` — pessoa primeiro, nome kung fu em parênteses e linkado.
- **Vários nomes**: `É o <Pinyin> de N nomes da linhagem: [Moy A B](/notes/moy-a-b/), [Moy C D](/notes/moy-c-d/)…` — todos linkados às notas `/notes/moy-*/`.
- **Expressão do *Hai Tong* / forma do sistema**: `É o <sílaba> de **<expressão romanizada> <ideogramas>** ("<tradução>"), …` com a fonte do clã nomeada (ex.: *Hai Tong* por Grão-Mestre Moy Yat).
- **Radical Kangxi**: `É o radical Kangxi nº <N> (<CHAR>, <glosa>); o chardb lista <X> caracteres que o contêm como componente. <forma como radical, se houver>. Ver [Os 214 radicais Kangxi](/notes/os-214-radicais-kangxi/).`
- **Sem vínculo**: omitir o parágrafo e abrir direto na linha de dados.

**Não usar** "nome de linhagem" — o termo é "nome kung fu". A frase "Registro filológico, sem vínculo a nome kung fu." foi abolida pelo autor (2026-07-09); não reintroduzir.

## Corpo

```markdown
**<CHAR>** — U+<HEX> · 部首 radical: <RAD> (nº <N>) · 總筆畫 strokes: <N> · 注音 zhuyin: <ㄓㄨㄧㄣ> · 拼音 pinyin: <pinyin> / jyutping: <jyutping>

#### Definições

**MDBG**: <definições, traduzidas para PT-BR>

**CantoDict**: <jyutping> (tom N, <descrição>). <Confirmado pela CUHK, se for o caso.>

**chardb Academia Sinica**:
1. <definição chinesa verbatim> (<tradução PT-BR>)
2. …

#### Decomposição e formas antigas (hanziyuan)

Componentes: <lista ou "pictograma simples, não decomponível">
Significado original: <do hanziyuan>
Formas atestadas: Oracle N · Bronze N · Seal N   ← ou a observação de que as contagens vêm da tabela do 小學堂

#### Shuowen Jiezi completo

**說文**: <chinês verbatim>
(<tradução PT-BR>)

**段注 Duan Yucai**: (não obtido — <motivo>)   ← ver "Marcadores" em fontes-etimologia.md

#### Evolução de formas (xiaoxue yanbian)

| Período | Script | Fonte / Artefato |
|---|---|---|
| <período traduzido> | <script traduzido (chinês)> | <artefato, com pinyin quando houver nome próprio> |

**Shuowen (xiaoxue)**: <texto inline>

**Comentários de estudiosos**:
- <estudioso ou 小學堂 (今按)>: <chinês> (<tradução PT-BR>)

#### Fonologia (xiaoxue shangguyin)

**中古音 Middle Chinese (Guangyun)**:
- 攝 Division: … · 韻 Rhyme: … · 聲 Tone: … · 母 Initial: …
- 反切 Fanqie: … · 等 Grade: … · 開合 Open/Closed: … · 清濁: …

**上古音 Old Chinese** (grupo de rima <X>):
- 高本漢 Karlgren: …
- 王力 Wang Li: …
- 董同龢 Dong Tonghe: …
- 周法高 Zhou Fagao: …
- 李方桂 Li Fanggui: …
- 鄭張尚芳 Zhengzhang Shangfang: …

**國語 Mandarin IPA**: …

#### Divergências entre fontes

**<Tema>.** <parágrafo>
```

### Divergências entre fontes

Ficam **dentro** da nota do caractere (subseção `####`), não numa seção global. Só fatos filológicos cruzando as fontes consultadas:

- contagens de atestações (小學堂 costuma corrigir hanziyuan);
- sentido primário: Shuowen / chardb def. 1 / MDBG / "original meaning" do hanziyuan;
- decomposição fonética vs. semântica;
- acepções exclusivas do chardb;
- comentários de estudiosos (小學堂, CUHK) que contradizem ou expandem o Shuowen;
- leitura cantonesa: jyutping cruzado entre CantoDict, MDBG e CUHK.

Sem inferência fonológica própria; sem interpretação do kung fu. A seção comporta o que o caractere demande — caracteres ricos geram notas longas, tardios geram notas curtas (memória `feedback_etimologia_serial_e_completa`, regra 2). Não comprimir prosa para economizar contexto.

## Não editorializar

As notas de etimologia são referência objetiva. Não inserir bullets ou parágrafos interpretando o ideograma no contexto da linhagem, do nome do discípulo ou do kung fu. A abertura é a única exceção, e só identifica a origem.

Exemplos do que não incluir (incidente 2026-04-23):
- "優 em Moy Yau Lei é o ideograma central do nome — combina excelência com a ressonância do ator ritual."
- "É o mesmo 士 usado em Moy Chi Yau Si e Moy Shan Si."

A seção "Aplicação ao Sistema Ving Tsun" é proibida. Existiu em 117 notas até 2026-10-03; o autor a classificou como perigosa (leitura simbólica sem fonte, ex.: "a escolha do nome 準 por Ip Man marca uma intenção pedagógica") e mandou remover. O teste `test_no_ving_tsun_application_section` em `tests/style/test_structural.py` bloqueia reincidência. O uso atestado de um caractere numa técnica (nome no PMYVTIM ou no Hai Tong) entra, quando entrar, só como linha factual com a fonte, nunca como interpretação.

## Caracteres tardios

Caracteres pós-Reinos Combatentes (ex.: 勣, 奜, 鑰, 讜, 懃) legitimamente têm vários campos sem dado por ausência epigráfica real. Não forçar dados; marcar e seguir. Regras de datação em `references/traducao.md`.
