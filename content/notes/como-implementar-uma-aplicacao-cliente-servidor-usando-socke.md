---
title: "Como implementar uma aplicação cliente-servidor usando Sockets em Ruby"
date: '2012-03-19T11:28:34-03:00'
category: webclip
summary: 'O texto apresenta Sockets como canais de comunicação bidirecional e mostra um exemplo simples em Ruby em que um cliente envia uma mensagem a um servidor TCP, que responde e fecha a conexão.'
tags: ["ruby", "sockets", "tcp", "cliente-servidor"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Como implementar uma aplicação cliente-servidor usando Sockets em Ruby"
    url: "http://imasters.com.br/artigo/23877/ruby/como-implementar-uma-aplicacao-cliente-servidor-usando-sockets-em-ruby"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-03/imasters-com-br--como-implementar-uma-aplicacao-cliente-servidor-usando-socke.md"
    kind: repo
---

O artigo explica o que são Sockets como extremidades de um canal de comunicação bidirecional e usa esse conceito para mostrar uma aplicação cliente-servidor em Ruby com TCP. O exemplo faz o cliente enviar uma mensagem ao servidor, o servidor ler a mensagem, responder e encerrar a conexão.

## Fichamento

- Sockets são apresentados como extremidades de um canal de comunicação bidirecional, úteis para comunicação entre processos de uma máquina, de máquinas diferentes ou entre processos de máquinas diferentes.
- O artigo diz que vai direto ao ponto e mostra, de forma simples, como implementar uma aplicação cliente-servidor em que o cliente envia uma mensagem e o servidor responde via Socket usando TCP.
- No servidor, o código usa `TCPServer.open(3001)` para abrir a porta 3001, aceita a conexão com `accept`, recebe até 10000 bytes com `recvfrom`, imprime a mensagem e envia uma resposta ao cliente antes de fechar a conexão.
- No cliente, o código usa `TCPSocket.open('localhost', 3001)` para se conectar ao servidor, envia uma mensagem, recebe a resposta com `recvfrom` e fecha a conexão.
- Para rodar a aplicação, o texto orienta salvar os códigos em arquivos `.rb`, executar o servidor primeiro e depois executar o cliente em outro terminal para que ambos funcionem ao mesmo tempo.
