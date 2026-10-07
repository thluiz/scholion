---
title: "Tratando problemas de conexão HTTP nos aplicativos Android"
date: '2012-06-25T21:27:52-03:00'
category: webclip
summary: 'O texto sugere dar feedback útil quando a conexão no Android está lenta, usar timeouts e exceções específicas, repetir tentativas com LoopJ e tratar falhas sem prejudicar a experiência do usuário.'
tags: ["android", "http", "timeouts", "network-errors"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Tratando problemas de conexão http nos aplicativos Android"
    url: "http://blog.caelum.com.br/tratando-problemas-de-conexao-http-nos-aplicativos-android/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-06/blog-caelum-com-br--tratando-problemas-de-conexao-http-nos-aplicativos-android.md"
    kind: repo
---

O texto diz que aplicativos Android dependem da internet para buscar dados e que falhas de conexão precisam de feedback claro para o usuário. Quando a rede está lenta, `ProgressDialog`, `ProgressBar` e até `AsyncTask` podem dar a sensação de espera indefinida.

Ele recomenda configurar timeouts no HttpComponents, tratar `SocketTimeoutException` e `ConnectTimeoutException` com mensagens mais explicativas, usar a biblioteca LoopJ para tentativas automáticas e tratar `UnknownHostException` quando não houver conexão ou o servidor não responder. Também sugere usar imagem padrão em falhas que não sejam críticas, como no download de thumbnails.

## Fichamento

- Aplicativos Android dependem da internet para recuperar dados essenciais e precisam informar melhor o usuário quando a conexão falha ou fica lenta.
- `ProgressDialog`, `ProgressBar` e `AsyncTask` podem transmitir a impressão de carregamento infinito quando a rede está lenta.
- No HttpComponents, é possível ajustar `http.socket.timeout` e `http.connection.timeout` para lidar melhor com conexões muito lentas.
- Em vez de tratar a exception mais genérica, vale tratar `SocketTimeoutException` e `ConnectTimeoutException` com mensagens mais claras para o usuário.
- A biblioteca LoopJ já faz requests em uma `Thread` separada, oferece callbacks de sucesso e falha e traz estratégia de tentativas pronta.
- Quando não há conexão ou há problema no servidor, `UnknownHostException` pode ser tratada para informar que o sistema não está respondendo naquele momento.
- Se o request não for essencial, como no download de um thumbnail, o texto propõe mostrar uma imagem padrão e deixar a tentativa de baixar novamente vinculada ao item quebrado.
