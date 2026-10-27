---
title: "Preparando-se para o desenvolvimento JavaScript moderno"
date: '2013-01-29T08:53:52-03:00'
category: webclip
summary: 'O artigo reúne padrões básicos de JavaScript para preparar código maior: IIFEs, namespaces, o revealing module pattern, construtores, protótipos e herança.'
tags: ["javascript", "modulos", "namespaces", "prototipos"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Preparando-se para o desenvolvimento JavaScript moderno | iMasters"
    url: "http://imasters.com.br/linguagens/javascript/preparando-se-para-o-desenvolvimento-javascript-moderno/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-01/imasters-com-br--preparando-se-para-o-desenvolvimento-javascript-moderno.md"
    kind: repo
---

O artigo diz que, antes de usar ferramentas mais avançadas de JavaScript, o desenvolvedor precisa entender alguns padrões básicos. Ele foca em tirar código do namespace global, agrupar funcionalidades em módulos, expor só o que deve ser público e usar construtores e protótipos para criar objetos e compartilhar métodos.

## Fichamento

- O texto parte do problema de código JavaScript espalhado em um arquivo e diz que esse estilo polui o namespace global.
- Apresenta o IIFE como uma forma simples de criar escopo de função e reduzir colisões com outro código.
- Mostra que window, jQuery e undefined podem ser passados ao IIFE para manter referências locais mais seguras.
- Explica namespaces como objetos ligados a window, para que funções fiquem agrupadas em vez de soltas no escopo global.
- Observa que namespaces muito aninhados ficam difíceis de chamar e podem exigir aliases dentro do módulo.
- Descreve o revealing module pattern como uma forma de manter variáveis privadas e retornar um objeto com métodos públicos.
- Diz que JavaScript não tem classes, então a criação de objetos acontece por funções construtoras.
- Usa prototype para compartilhar métodos como fullName entre instâncias, em vez de repetir o método em cada objeto.
- Mostra herança ao definir Spy.prototype como uma instância de Person, permitindo que objetos Spy usem métodos de Person.
- Fecha dizendo que essas técnicas não são, por si só, JavaScript moderno e sugere empacotamento e minimização como próximo passo.
