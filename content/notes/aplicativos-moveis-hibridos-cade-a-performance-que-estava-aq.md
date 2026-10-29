---
title: "Aplicativos móveis híbridos: cadê a performance que estava aqui?"
date: '2015-10-09T09:18:06-03:00'
category: webclip
summary: 'O autor relata a decepção com a performance de um app feito com Ionic e lista ajustes para reduzir lentidão, como imagens menores, menos watchers e mais cuidado com listas e CSS.'
tags: ["ionic", "angularjs", "performance"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Aplicativos móveis híbridos: cadê a performance que estava aqui?"
    url: "http://isaquedias.com.br/aplicativos-moveis-hibridos-cade-a-perfomance-que-estava-aqui/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-10/isaquedias-com-br--aplicativos-moveis-hibridos-cade-a-performance-que-estava-aq.md"
    kind: repo
---

O texto conta a experiência de desenvolver um app híbrido com Ionic e descobrir, na primeira build no aparelho, que a fluidez vista no browser não se sustentava no dispositivo. A partir dessa frustração, o autor reúne medidas práticas para aliviar a lentidão em apps AngularJS.

## Fichamento

- O autor escolheu Ionic para um app móvel após comparar com a opção nativa.
- O app pareceu fluido no browser, mas ficou decepcionante quando instalado no Moto G.
- Reduzir o tamanho das imagens das listas melhorou o desempenho.
- Muitos watchers deixam o AngularJS mais lento porque aumentam o custo do ciclo de digest.
- O uso de bind once remove ouvintes depois da renderização inicial.
- ng-show e ng-hide mantêm o elemento no DOM, enquanto ng-if remove e recria o nó quando preciso.
- ng-repeat pesa na performance, e o Ionic oferece collection-repeat como alternativa para listas grandes.
- collection-repeat só renderiza os itens visíveis, mas exige itens com a mesma altura e tamanho.
- Native scrolling dispensa o $ionicScrollDelegate e usa o scroll nativo do browser.
- track by id evita criar hash keys e reduz manipulações no DOM.
- CSS também interfere no desempenho, então o autor recomenda remover regras não usadas e escrever CSS de forma eficiente.
- A conclusão é que o Ionic entrega componentes úteis, mas o Angular ainda tem problemas sérios de performance, especialmente em listas.
