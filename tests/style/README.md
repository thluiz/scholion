# style-test — Scholion

Suíte pytest para auditar notas em `content/notes/` contra os padrões catalogados na skill `ghost-writer` (vocabulário banido, PT-EU, Wing Chun, Sifu aglutinado, travessões, frase nominal solta, etc.) e regras de meta (encoding, datas futuras, schema de frontmatter).

## Setup (uma vez)

```bash
pip install -r tests/style/requirements.txt
```

## Uso

```bash
pytest tests/style/                    # todas as notas, todos os checks
pytest tests/style/ -k vi-encontro     # uma nota específica
pytest tests/style/test_lexical.py     # só checks lexicais
pytest tests/style/ -x                 # parar no primeiro erro
pytest tests/style/ --tb=short         # output mais curto
```

## Filosofia

Esta suíte detecta apenas o que pode ser detectado deterministicamente. Os padrões estruturais que exigem leitura (aforismos clever, falsa-experiência, fabricação de autoridade, aforismos de fechamento) ficam para a skill `/style-test --fix` (Phase 2) ou revisão humana.

A suíte NÃO bloqueia commits. Roda on-demand — ver memory: rejeição de pre-commit hooks pra notas (atrito sem saída fácil em commits feitos fora do Claude).

## Cobertura atual

- `test_lexical.py` — vocabulário banido, PT-EU, Wing Chun, Sifu aglutinado, hedges, conectivos burocráticos, advérbios-muleta, preâmbulos vazios, jargões de conclusão
- `test_structural.py` — travessões em excesso, negativa indireta, CTAs, Co-Authored-By no corpo
- `test_meta.py` — encoding UTF-8, datas futuras, frontmatter mínimo

## Adicionando novos checks

Cada teste é parametrizado por nota (`@pytest.mark.parametrize` sobre `ALL_NOTES`). Adicionar nova regra: novo `def test_*` no arquivo apropriado, ou novo arquivo `test_*.py` se for nova categoria.

Para novos padrões de regex, atualizar a lista no início do arquivo. Para padrões estruturais, ver `_helpers.py`.
