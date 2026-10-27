---
title: "Padrão de projeto de software - JavaScript: Adapter"
date: '2012-04-10T11:39:04-03:00'
category: webclip
summary: 'O texto explica o Adapter como uma camada que adapta a interface de um objeto novo à interface esperada pelo código existente, usando factory e exemplos com logger.'
tags: ["javascript", "adapter", "design-patterns", "factory"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Padrão de projeto de software - JavaScript: Adapter"
    url: "https://web.archive.org/web/20120910200331/http://imasters.com.br/artigo/24070/javascript/padrao-de-projeto-de-software-javascript-adapter"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-04/web-archive-org--padrao-de-projeto-de-software-javascript-adapter.md"
    kind: repo
---

O texto apresenta o Adapter como um padrão para uso em código já existente quando se quer trocar um objeto ou função por outro com interface diferente. A ideia é envolver o novo objeto, ou mediar suas chamadas, para que ele corresponda ao que o código atual sabe usar.

## Fichamento

- O Adapter serve para substituir um objeto ou função sem mudar o código que já depende da interface antiga.
- Quando o objeto é instanciado com `new`, o Adapter o envolve e repassa as chamadas para a instância interna.
- Quando o objeto é estático, o Adapter pode apenas mediar o acesso, sem encapsular uma nova instância.
- Um caso comum aparece na troca de bibliotecas, como substituir chamadas de jQuery por outra biblioteca em uma aplicação grande.
- Outro uso citado é a troca de bibliotecas de logger, inclusive em aplicações JavaScript com `console` disponível no navegador.
- No exemplo, `LoggerFactory.getLogger()` retorna `window.console` e a aplicação chama `logger.log(...)`.
- Em seguida, um `AjaxLogger` envia logs ao servidor via AJAX e usa uma interface diferente da do `console`.
- O `AjaxLoggerAdapter` expõe `log(arg)` e repassa a chamada para `AjaxLogger.sendLog(arg)`.
- A mudança no código existente fica concentrada no factory, que passa a retornar o adapter em vez do logger original.
- O texto observa que alguns adapters são simples, mas outros exigem mapear funções com argumentos muito diferentes ou ignorar parâmetros que o novo objeto não usa.
- Se o mapeamento ficar difícil demais, a recomendação é procurar outra alternativa em vez de alterar o uso do objeto original em todo o código.
- O texto conclui que adapters são úteis e fáceis de implementar quando um factory cria o objeto substituído.
