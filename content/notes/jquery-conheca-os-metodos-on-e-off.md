---
title: "jQuery: conheça os métodos on() e off()"
date: '2012-03-13T20:34:35-03:00'
category: webclip
summary: 'O texto apresenta on() e off() como a forma padronizada de associar e remover eventos no jQuery 1.7, cobrindo eventos diretos, delegados, namespaces, dados e o uso de one().'
tags: ["jquery", "eventos", "delegacao-de-eventos", "namespaces"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "jQuery: conheça os métodos on() e off()"
    url: "https://tableless.com.br/jquery-conheca-os-metodos-on-e-off/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-03/tableless-com-br--jquery-conheca-os-metodos-on-e-off.md"
    kind: repo
---

O texto explica que, com o jQuery 1.7, os métodos on() e off() passam a concentrar a associação e a remoção de eventos, com o objetivo de substituir a confusão entre bind(), live() e delegate(). Também mostra que on() serve tanto para eventos diretos quanto para múltiplos eventos, delegação, namespaces e envio de dados ao evento.

## Fichamento

- on() faz associação direta quando não há seletor, como em elementos únicos ou poucos elementos, com comportamento equivalente ao bind().
- on() também aceita um mapa de eventos, permitindo ligar click, dblclick e mouseenter ao mesmo elemento com funções diferentes.
- off() remove todas as associações de um elemento ou apenas um evento específico, como click.
- Na delegação, on() recebe um seletor e dispara para elementos descendentes compatíveis, inclusive os criados depois no DOM.
- Para remover só eventos delegados, o texto mostra o uso do parâmetro especial "**" ou a remoção com base na função.
- on() permite usar namespaces, o que facilita controlar eventos ligados a uma funcionalidade ou plugin.
- on() também aceita dados associados ao evento, acessados depois pelo objeto event.
- one() segue as regras de on(), mas executa o evento apenas uma vez e remove a associação depois disso.
- O texto conclui que on() e off() devem substituir live() e delegate() e padronizar a associação de eventos no jQuery.
