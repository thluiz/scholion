---
title: "Padrão de projeto de software - JavaScript: Facade"
date: '2012-04-03T12:50:28-03:00'
category: webclip
summary: 'O texto define Facade como um código que simplifica uma interface complexa e mostra exemplos em bibliotecas JavaScript, atalhos do sistema e funções que encapsulam detecção de navegador e aplicação de estilos.'
tags: ["design-patterns", "javascript", "facade"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Padrão de projeto de software - JavaScript: Facade"
    url: "https://web.archive.org/web/20120717074812/http://imasters.com.br/artigo/24004/javascript/padrao-de-projeto-de-software-javascript-facade"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-04/web-archive-org--padrao-de-projeto-de-software-javascript-facade.md"
    kind: repo
---

O texto apresenta o padrão Facade como um trecho de código que simplifica uma interface mais complexa. A ideia aparece em bibliotecas como jQuery, Prototype e YUI, que escondem detecção de recursos e expõem uma chamada mais simples, e também em atalhos do desktop.

## Fichamento

- Facade é definido como um pedaço de código que simplifica uma interface mais complexa.
- O autor diz que qualquer forma de abstração pode ser vista como um Facade.
- Bibliotecas JavaScript como jQuery, Prototype e YUI funcionam como Facades ao reunir código complexo em uma única chamada de função.
- Um atalho no desktop também exemplifica Facade, porque um duplo clique aciona uma sequência interna de pastas e execução.
- O texto mostra uma função addEvent que encapsula a detecção entre addEventListener, attachEvent e atribuição direta de handler.
- O texto mostra primeiro código repetido para aplicar os mesmos estilos a vários elementos.
- Depois propõe setStyle para aplicar uma propriedade a vários elementos em uma chamada.
- Em seguida propõe setStyles para aplicar várias propriedades de uma vez a vários elementos.
- O ganho descrito é economizar tempo quando muitos elementos precisam receber os mesmos estilos.
