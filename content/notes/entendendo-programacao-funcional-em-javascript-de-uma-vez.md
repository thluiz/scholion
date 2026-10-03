---
title: "Entendendo Programação Funcional em JavaScript de uma vez"
date: '2016-03-10T15:20:38-03:00'
category: webclip
summary: 'O artigo apresenta a programação funcional em JavaScript por meio de funções puras, higher-order functions, map, filter, reduce, currying e compose, com exemplos em ES5 e ES6.'
tags: ["programacao-funcional", "javascript", "higher-order-functions", "currying"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Entendendo Programação Funcional em JavaScript de uma vez — Medium"
    url: "https://medium.com/@matheusml/entendendo-programa%C3%A7%C3%A3o-funcional-em-javascript-de-uma-vez-c676489be08b#.oqkcv8r51"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-03/medium-com--entendendo-programacao-funcional-em-javascript-de-uma-vez.md"
    kind: repo
---

O texto explica a programação funcional a partir da ideia de funções com entradas e saídas bem definidas e da redução de side-effects. Em seguida, mostra como esses princípios aparecem em JavaScript com funções puras, higher-order functions e operações comuns sobre arrays.

## Fichamento

- Funções com entradas e saídas ocultas podem gerar side-effects e dificultar manutenção e testes.
- Funções puras declaram entradas e saídas e retornam sempre o mesmo resultado para o mesmo parâmetro.
- Remover side-effects e escrever funções puras é apresentado como a base da programação funcional.
- Higher-order functions são funções que recebem outras funções ou retornam funções.
- O texto usa calculate, Jasmine, Mocha, jQuery e AngularJS como exemplos de higher-order functions.
- map retorna um novo array aplicando um callback a cada item do array original.
- filter retorna um novo array com os itens que atendem à condição do callback.
- reduce combina um array em um único valor usando um callback e um valor inicial.
- reduce aparece em exemplos de soma e de abreviação de meses, com uma condição para evitar um separador no início.
- Currying é descrito como transformar uma função com múltiplos parâmetros em uma sequência de funções com um parâmetro cada.
- O texto diz que currying pode tornar o código mais expressivo e reutilizável.
- compose é apresentado como forma de combinar funções pequenas para gerar funções mais complexas e reaproveitáveis.
