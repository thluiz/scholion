---
title: "Goodhart's Law in Software Engineering"
date: '2026-09-24T23:07:08+01:00'
category: webclip
summary: 'O texto defende a versão forte da lei de Goodhart: quando uma métrica vira alvo, ela começa a desviar do valor que pretendia representar. Em engenharia, isso aparece em cobertura de testes, complexidade, benchmarks e métricas de produtividade.'
tags: ["goodhart", "software-engineering", "metrics"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Goodhart's Law in Software Engineering"
    url: "https://buttondown.com/hillelwayne/archive/goodharts-law-in-software-engineering/?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/buttondown-com--goodharts-law-in-software-engineering.md"
    kind: repo
---

O texto argumenta que métricas são aproximações de valores que não podem ser medidos diretamente. Quando a métrica passa a orientar a ação, o foco se desloca da meta para o indicador, e isso pode piorar o resultado que se queria alcançar. O autor trata essa dinâmica como parte central da lei de Goodhart.

Ele aplica essa ideia a exemplos de engenharia de software, como cobertura de testes, complexidade ciclomática, tamanho de função, benchmarks e tempo gasto em pair programming, revisão e depuração. Também menciona o relatório DORA como um caso de métricas usadas como proxies de metas mais difusas, e conclui que a saída prática é usar julgamento de engenharia, ainda que isso não seja uma orientação escalável.

## Fichamento

- A versão fraca da lei fala de incentivos para manipular métricas; a versão forte diz que perseguir uma métrica honestamente também pode afastar o objetivo real.
- Métricas existem porque o que realmente importa costuma ser não quantificável, então elas funcionam como aproximações imperfeitas do valor desejado.
- No exemplo de confiabilidade de software, o número de bugs no tracker mede só de forma aproximada a confiabilidade, e corrigir bugs pode até reduzir a confiabilidade sem mudar o registro de bugs.
- A seleção sexual é apresentada como exemplo de Goodhart em ação: plumagem mais chamativa começa como proxy de fitness e vira o próprio alvo ao longo das gerações.
- Em engenharia, cobertura de testes, complexidade ciclomática, tamanho de função e benchmarks são proxies úteis, mas podem divergir do objetivo quando outros aspectos do sistema passam a importar mais.
- O tempo gasto em pairing, code review e debugging também aparece como proxy de produtividade.
- O relatório DORA é descrito como um caso em que métricas funcionam como proxies de metas como elite performance e satisfação dos empregados, além de incentivar commit size menor para melhorar métricas proxy.
- A combinação de métricas pode ajudar a revelar tensões entre objetivos, mas também pode virar outro alvo sujeito à mesma distorção.
- A solução prática proposta é usar o melhor julgamento de engenharia, porque a lei de Goodhart pode afetar qualquer métrica usada como alvo.
