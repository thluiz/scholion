---
title: "Evitando complexidade acidental ao estruturar sua aplicação Redux"
date: '2016-10-13T11:24:21-03:00'
category: webclip
summary: 'O texto defende que o estado em Redux deve ser mínimo, normalizado e livre de duplicação ou derivados, tratando-o como um banco de dados em memória para evitar complexidade futura.'
tags: ["redux", "state-management", "normalization", "selectors"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Evitando complexidade acidental ao estruturar sua aplicação Redux – Medium"
    url: "https://medium.com/@oieduardorabelo/evitando-complexidade-acidental-ao-estruturar-sua-aplica%C3%A7%C3%A3o-redux-6823d2cdcfaf?ct=t(BrazilJS_Weekly_468_9_2013)#.sg7j0h9uj"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-10/medium-com--evitando-complexidade-acidental-ao-estruturar-aplicacao-redu.md"
    kind: repo
---

O texto reúne dicas para modelar o estado de uma aplicação Redux com menos complexidade futura. A orientação central é manter o estado mínimo, separar o que vem da API do que faz sentido guardar no cliente e tratar o estado como um banco de dados em memória.

## Fichamento

- Evitar modelar o estado a partir da estrutura da API do servidor, porque as preocupações de rede não são as mesmas da aplicação.
- Preferir objetos em vez de arrays para guardar entidades, usando a chave primária como índice.
- Se a ordem precisar ser preservada, guardar um array só com os IDs.
- Não modelar o estado com base na estrutura das páginas, porque páginas diferentes podem consumir os mesmos dados de formas diferentes.
- Não guardar dados duplicados no estado; se um dado aparece em mais de um lugar, isso exige atualizações em múltiplos pontos.
- Usar selectors para derivar dados na hora do consumo, em vez de persistir versões repetidas no estado.
- Não guardar dados derivados no estado, porque eles também criam risco de inconsistência.
- Se o cálculo do selector for pesado, aplicar memoização e considerar bibliotecas como Reselect.
- Normalizar objetos aninhados, separando entidades relacionadas em estruturas próprias e ligando-as por IDs.
- Tratar o estado da aplicação como um banco de dados em memória, já que os mesmos cuidados de modelagem ajudam a manter consistência e simplicidade.
