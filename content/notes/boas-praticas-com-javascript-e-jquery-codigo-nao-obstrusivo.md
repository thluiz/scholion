---
title: "Boas práticas com JavaScript e jQuery: código não-obstrusivo"
date: '2012-06-04T15:34:22-03:00'
category: webclip
summary: 'A página defende separar HTML, CSS e JavaScript, ligar comportamento por eventos da DOM ou do jQuery e evitar onclick inline e links com href="#".'
tags: ["javascript", "jquery", "eventos", "codigo-nao-obstrusivo"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Boas práticas com JavaScript e jQuery: código não-obstrusivo"
    url: "http://blog.caelum.com.br/boas-praticas-com-javascript-e-jquery-codigo-nao-obstrusivo/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-06/blog-caelum-com-br--boas-praticas-com-javascript-e-jquery-codigo-nao-obstrusivo.md"
    kind: repo
---

A página explica que o front-end fica mais fácil de manter quando marcação, apresentação e interação permanecem separadas. O texto tira o estilo do HTML, depois mostra como o JavaScript deve ligar comportamento por meio da DOM ou do jQuery, em vez de usar atributos de evento no próprio markup.

Também diz que o jQuery simplifica diferenças entre navegadores, que os manipuladores podem receber um objeto event e que os links devem evitar href="#" quando outro URL pode oferecer o mesmo comportamento sem JavaScript.

## Fichamento

- O HTML não deve carregar informação visual nem detalhes de interação que pertencem ao CSS ou ao JavaScript.
- O exemplo limpo usa um id na marcação e leva a regra de font-size para o CSS.
- Em JavaScript puro, o elemento é obtido com document.getElementById e o manipulador de clique é ligado com addEventListener.
- Esse padrão é descrito como JavaScript não-obstrusivo porque adiciona comportamento sem atributos extras no HTML.
- O texto diz que as APIs dos navegadores não são totalmente consistentes, especialmente no IE, que usa attachEvent no lugar de addEventListener.
- O jQuery esconde essas diferenças e permite ligar o manipulador com $('#additem').on('click', adicionaItem).
- Em versões antigas do jQuery, a função on() deve ser substituída por bind().
- Se o manipulador precisar de argumentos, o jQuery deve receber uma função anônima que chama adicionaItem com esses argumentos.
- O objeto event passado ao manipulador pode trazer dados como timestamp e coordenadas do mouse.
- Em links, event.preventDefault() impede que o navegador siga href="#" depois que o manipulador executa.
- O texto recomenda evitar links que apontam para "#" a menos que esse seja o objetivo real, e usar uma URL de verdade como fallback para acessibilidade e para dispositivos sem JavaScript.
- Qualquer elemento pode receber um event listener, e nem todo elemento precisa de preventDefault porque nem todo clique altera a navegação da página.
