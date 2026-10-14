---
title: "O que é e o que não é refatoração – de acordo com Kent Beck e Martin Fowler"
date: '2013-02-19T18:57:01-03:00'
category: webclip
summary: 'O texto define refatoração como mudança interna segura, feita em pequenos passos e com testes. Também separa essa prática de correções, otimizações, reescritas e redesigns maiores.'
tags: ["refatoracao", "kent-beck", "martin-fowler", "design-de-software"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "O que é e o que não é refatoração – de acordo com Kent Beck e Martin Fowler"
    url: "http://imasters.com.br/desenvolvimento/o-que-e-e-o-que-nao-e-refatoracao-de-acordo-com-kent-beck-e-martin-fowler/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-02/imasters-com-br--o-que-e-e-o-que-nao-e-refatoracao.md"
    kind: repo
---

O texto retoma a definição de Martin Fowler e Kent Beck para refatoração como uma mudança na estrutura interna do software que facilita entender e modificar o código sem alterar seu comportamento observável. A prática aparece como limpeza disciplinada de código, feita em passos pequenos, com testes após cada etapa, para reduzir riscos e tornar mudanças futuras mais seguras.

Também delimita o que fica fora desse conceito. Corrigir bugs, otimizar, reforçar tratamento de erros, adicionar defensive code ou tornar o código mais testável não são refatoração, embora possam acompanhar o trabalho. O texto ainda distingue a refatoração cotidiana de reescritas, redesigns e mudanças em larga escala, que exigem tempo, risco e planejamento diferentes.

## Fichamento

- Refatoração é alteração interna do software para facilitar compreensão e manutenção sem mudar o comportamento observável.
- Ela serve para eliminar atalhos, duplicação e código legado, deixando design e lógica mais claros.
- O trabalho deve ocorrer em passos pequenos, independentes e seguros, com testes depois de cada etapa.
- Corrigir bugs, otimizar, endurecer o tratamento de erros e adicionar defensive code não entra na definição de refatoração.
- Melhorar a testabilidade pode ser um efeito da refatoração, mas não define a prática.
- A refatoração apoia uma mudança já necessária e não deve ser feita pelo bem da refatoração.
- Em código legado, pode-se “refatorar para compreender”, limpando nomes, condicionais e rotinas para entender melhor o sistema.
- Mudanças simples como remover duplicação, extrair métodos, trocar nomes e substituir números mágicos trazem ganho rápido de entendimento.
- Refatoração em larga escala se aproxima de redesign, reescrita ou reengenharia, com riscos e custos maiores.
- Se o trabalho exige blocos explícitos de tempo, um sprint inteiro ou justificativa de negócio, o texto diz que isso já não é refatoração cotidiana.
