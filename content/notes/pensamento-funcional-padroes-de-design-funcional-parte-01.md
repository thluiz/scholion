---
title: "Pensamento funcional: padrões de design funcional - Parte 01"
date: '2012-05-08T10:27:59-03:00'
category: webclip
summary: 'O texto mostra como padrões de design aparecem na programação funcional: às vezes são absorvidos pela linguagem, às vezes mantêm a semântica com outra implementação, e às vezes dependem de recursos exclusivos.'
tags: ["programacao-funcional", "padroes-de-design", "groovy", "scala"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Pensamento funcional: padrões de design funcional - Parte 01"
    url: "https://imasters.com.br/back-end/pensamento-funcional-padroes-de-design-funcional-parte-01"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-05/imasters-com-br--pensamento-funcional-padroes-de-design-funcional-parte-01.md"
    kind: repo
---

O texto apresenta três formas de manifestação dos padrões de design na programação funcional. Eles podem ser absorvidos pela linguagem ou pelo tempo de execução, podem manter a mesma semântica com outra implementação, ou podem usar recursos que outras linguagens não oferecem.

## Fichamento

- O conceito de padrão de design continua válido na programação funcional, embora alguns padrões tradicionais desapareçam e outros sejam resolvidos de modo diferente.
- Em programação funcional, padrões tradicionais costumam ser absorvidos pela linguagem, reaparecer com outra implementação, ou depender de recursos exclusivos.
- Currying pode funcionar como um factory para funções, criando uma função a partir de outra mais geral.
- Em Scala, a função dividesBy() aparece como exemplo de currying usada como predicado em filter().
- Funções de primeira classe simplificam o Command, porque eliminam a necessidade de um wrapper de objeto para funcionalidade móvel.
- O Método Template pode ser reescrito com blocos de código atribuídos a propriedades, em vez de métodos abstratos em subclasses.
- O uso de chamadas protegidas permite que algumas etapas do processamento fiquem em branco sem quebrar a execução.
- O padrão Strategy também fica mais simples com funções de primeira classe, reduzindo a estrutura de interfaces e classes concretas.
- No exemplo de exponenciação, blocos de código substituem estratégias nomeadas e reduzem a cerimônia do código.
- O padrão Flyweight preserva sua semântica quando o cache de objetos canônicos passa a ser tratado como memoização.
- Em Groovy, o método memoize() cria uma versão em cache de uma função e simplifica a implementação do flyweight.
- O texto conclui que a programação funcional pode absorver padrões, mudar sua implementação ou resolver problemas de outro modo com recursos próprios.
