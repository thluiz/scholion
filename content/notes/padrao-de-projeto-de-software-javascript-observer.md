---
title: "Padrão de projeto de software - JavaScript: Observer"
date: '2012-04-26T14:57:57-03:00'
category: webclip
summary: 'O texto explica o padrão Observer em JavaScript, compara os modos push e pull, mostra exemplos de código e aponta usos comuns em eventos DOM e plugins jQuery.'
tags: ["observer", "javascript", "design-patterns", "events"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Padrão de projeto de software - JavaScript: Observer"
    url: "http://imasters.com.br/artigo/24164/javascript/padrao-de-projeto-de-software-javascript-observer"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-04/imasters-com-br--padrao-de-projeto-de-software-javascript-observer.md"
    kind: repo
---

O texto apresenta o padrão Observer como uma forma simples de ligar um objeto observável a observers que se inscrevem, cancelam a inscrição e recebem informações quando algo relevante acontece. Também distingue as abordagens push e pull e mostra que, em JavaScript, o observer pode ser uma callback.

Nos exemplos, o texto coloca as rotinas de inscrição, cancelamento e publicação dentro de Observable no caso push. No caso pull, o observer guarda as inscrições e consulta o estado do observable quando precisa verificar se houve mudança. O texto ainda diz que eventos do DOM já usam esse padrão e que plugins jQuery com animação podem usá-lo para permitir inserção de funcionalidade em pontos diferentes.

## Fichamento

- O padrão Observer liga um observer inscrito a um objeto observable que informa quando algo de interesse acontece.
- No modelo push, o observable notifica os observers assim que um evento ocorre.
- No modelo pull, o observer consulta o observable quando precisa verificar se houve mudança.
- No exemplo em JavaScript, o observable reúne as funções de subscribe, unsubscribe e publish.
- Nesse exemplo, o observer é apenas uma função usada como callback.
- O texto compara esse uso com Java, onde o observer seria um objeto que implementa uma interface.
- O exemplo de pull inverte a organização: o observer guarda as inscrições e chama getStatus no observable.
- O texto diz que eventos de elementos DOM são uma implementação do padrão Observer.
- Também afirma que plugins jQuery com animações podem usar Observer para permitir extensões em pontos diferentes da animação.
- O padrão é descrito como útil para separar código e manter aplicações grandes mais organizadas e sustentáveis.
