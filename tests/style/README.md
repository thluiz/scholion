# style-test — Scholion

Suíte pytest para auditar notas em `content/notes/` contra o subconjunto **detectável por regex** das regras de voz consolidadas em `~/.claude/skills/ghost-writer/references/voz.md` (vocabulário banido, PT-EU, Wing Chun, termos aglutinados, romanização Moy Yat, hedges, conectivos, CTAs, travessões em excesso, negativa indireta, uniformidade de parágrafos) e regras de integridade do arquivo (encoding, datas futuras, frontmatter, markup alucinado).

## Setup (uma vez)

```bash
pip install -r tests/style/requirements.txt
```

## Uso

Sempre com `PYTHONIOENCODING=utf-8` no Windows (cp1252 corrompe o output silenciosamente).

```bash
PYTHONIOENCODING=utf-8 pytest tests/style/                    # todas as notas, todos os checks
PYTHONIOENCODING=utf-8 pytest tests/style/ -k vi-encontro     # uma nota específica
PYTHONIOENCODING=utf-8 pytest tests/style/test_lexical.py     # só checks lexicais
PYTHONIOENCODING=utf-8 pytest tests/style/ -x                 # parar no primeiro erro
PYTHONIOENCODING=utf-8 pytest tests/style/ --tb=short         # output mais curto
```

Filtro por slug: env var `STYLE_TEST_FILTER` (vírgula-separada). A skill `/style-test` usa isso para rodar só nas N últimas notas modificadas (default 1, via `E:/scholion/.claude/scripts/last-modified-notes.ps1`).

## Filosofia

Esta suíte detecta apenas o que pode ser detectado deterministicamente. O que exige leitura (aforismos de fechamento, afirmações sem fonte, falsa-experiência, listas paralelas vazias, cross-links) fica para `/ghost-audit` (endpoint LLM, portão obrigatório) e `/verify-note` (auditoria semântica opcional). Pipeline: `/style-test` → `/ghost-audit` → `/verify-note`.

A suíte NÃO bloqueia commits. Roda on-demand (o hook de commit é o ghost-audit, não esta suíte).

## Cobertura atual

- `test_lexical.py`
  - `test_no_banned_vocab`: subconjunto conservador do vocabulário banido (ver comentário no topo do arquivo sobre os termos excluídos por falso-positivo em citações e notas em inglês)
  - `test_no_jargon_fecho`: jargão de conclusão só como abertura de parágrafo
  - `test_no_pt_eu`: marcadores PT-EU; "estar a + infinitivo" não entra (válido no estilo do autor)
  - `test_no_wing_chun`
  - `test_no_agglutinated_terms`: Sifu, Sihing, Sigung, Sitaaigung, Todai(s), Sije
  - `test_no_wrong_moy_yat_romanization`: Moy Lima, Moy Quelo (Si), Moy Joleu/Joleou
  - `test_no_bureaucratic_openers`
  - `test_no_hedges`
  - `test_no_cta`
- `test_structural.py`
  - `test_dash_overuse`: densidade de travessões (skipa etimologias e bookmarks de podcast)
  - `test_no_negativa_indireta`
  - `test_no_co_authored_by`
  - `test_no_hallucinated_markup`: âncoras de citação de ChatGPT/Grok
  - `test_paragraph_uniformity`: coeficiente de variação do tamanho dos parágrafos
  - `test_transition_density`: parágrafos abrindo com conectivo brando
  - desativados (comentados no arquivo): travessão individual "X — Y" e three-beat, por falso-positivo
- `test_meta.py`
  - `test_utf8_decodable`, `test_no_orphan_cp1252_chars`
  - `test_frontmatter_required_fields`, `test_frontmatter_types`
  - `test_date_not_in_future`

## Adicionando novos checks

Cada teste é parametrizado por nota (`pytest_generate_tests` em `conftest.py` sobre `ALL_NOTES`). Nova regra: novo `def test_*` no arquivo apropriado, ou novo arquivo `test_*.py` se for nova categoria. Helpers (`find_lines`, `strip_quotes_and_code`, `fail_if_hits`) vivem em `conftest.py`.

Para novos padrões de regex, atualizar a lista no início do arquivo e citar o item de `voz.md` que o teste implementa. Para heurísticas estruturais, calibrar sobre o corpus inteiro antes (ver os comentários de calibração em `test_structural.py`).
