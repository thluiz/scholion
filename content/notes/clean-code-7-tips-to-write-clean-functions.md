---
title: "Clean Code: 7 tips to write clean functions"
date: '2026-09-24T23:24:13+01:00'
category: webclip
summary: 'The post argues that clean functions are small, easy to understand, well named, limited in parameters, free of nested conditionals and booleans, and preferably pure.'
tags: ["clean-code", "functions", "refactoring", "testing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Clean Code: 7 tips to write clean functions"
    url: "https://craftbettersoftware.com/p/clean-code-7-tips-to-write-clean?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/craftbettersoftware-com--clean-code-7-tips-to-write-clean-functions.md"
    kind: repo
---

The post says functions should be easy to understand quickly, because complex code causes errors, slows changes, and makes onboarding harder. It recommends small functions, but also says size should depend on context and judgment.

It also suggests naming functions after the business domain, using verbs, keeping team naming conventions, and using one word per concept. For structure, it prefers few parameters, guard clauses instead of nested ifs, pure functions, enums instead of booleans, and descriptive names instead of comments.

## Fichamento

- Funções devem ser compreensíveis em poucos segundos; quando isso demora, o texto defende refatoração.
- Funções complexas aumentam erros, dificultam mudanças e atrasam a entrada de novos desenvolvedores.
- O ideal é fazer funções pequenas e pragmáticas, sem virar dogma nem encher o código de funções demais.
- Nomes de função devem refletir a linguagem do domínio e dizer claramente o que a função faz.
- O texto recomenda usar verbos, seguir convenções do time e manter um termo só para cada conceito.
- O número ideal de argumentos é zero, e o texto sugere no máximo três parâmetros, agrupando dados relacionados quando necessário.
- Em vez de IFs aninhados, o texto propõe inverter as condições e usar guard clauses.
- Funções puras têm o mesmo resultado para a mesma entrada e não têm side effects; isso as torna mais previsíveis, fáceis de testar e paralelizáveis.
- Booleanos como parâmetro deixam a chamada ambígua; o texto prefere enums para tornar o código autoexplicativo.
- Quando uma função não fica clara, o texto diz para priorizar bons nomes em vez de recorrer a comentários, que envelhecem mal e muitas vezes repetem o código.
