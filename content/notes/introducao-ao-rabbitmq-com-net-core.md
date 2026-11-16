---
title: "Introdução ao RabbitMQ com .NET Core"
date: '2020-02-22T12:12:01+00:00'
category: webclip
summary: 'O texto apresenta os conceitos básicos do RabbitMQ, explica exchange, filas, binds e vhosts, e mostra um exemplo simples de publisher e consumer em .NET Core.'
tags: ["rabbitmq", "net-core", "mensageria", "sistemas-distribuidos"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "(pt-BR) Introdução ao RabbitMQ com .NET Core"
    url: "https://dev.to/mviegas/pt-br-introducao-ao-rabbitmq-com-net-core-15oc"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--introducao-ao-rabbitmq-com-net-core.md"
    kind: repo
---

O texto introduz o RabbitMQ como message broker para desacoplamento e comunicação entre aplicações. Ele explica a motivação de arquiteturas distribuídas, descreve o fluxo entre publisher, broker, exchange, filas e consumidores, e mostra um exemplo básico com duas aplicações console em .NET Core.

## Fichamento

- O artigo quer dar uma visão introdutória, objetiva e em português sobre RabbitMQ e seu uso como recurso de mensageria para desacoplamento entre aplicações.
- Arquiteturas distribuídas trazem vantagens como desacoplamento, maior coesão e autonomia das partes, mas também exigem mais resiliência, confiabilidade e escalabilidade.
- RabbitMQ é apresentado como um message broker que recebe mensagens publicadas por uma aplicação e as encaminha para filas acessadas por consumidores.
- O texto cita suporte a AMQP, MQTT e STOMP e indica materiais externos para aprofundamento.
- A escalabilidade aparece como uma vantagem do modelo, com entrega única da mensagem a um consumidor.
- O broker também atua como mediador quando a mesma mensagem precisa ser roteada para consumidores diferentes por meio de várias filas.
- O envio assíncrono reduz a carga da aplicação que publica, mas introduz novos pontos de falha, como rede e consumidor.
- Uma exchange é descrita como o artefato de roteamento que usa routing key para decidir o destino da mensagem.
- O texto lista quatro tipos de exchange no RabbitMQ: direct, fanout, topic e header.
- As filas armazenam mensagens até que um consumidor as receba e podem ser durable, exclusive ou auto-delete.
- Bind é a associação necessária entre exchange e fila para que a entrega aconteça.
- Vhosts são descritos como separações lógicas das entidades do RabbitMQ, funcionando como tenants.
- O texto trata o padrão fire and forget como um caso em que quem publica não acompanha o caminho da mensagem depois do envio.
- Quando um consumidor recebe uma mensagem, ele emite um acknowledgement para informar ao broker que a mensagem já foi processada.
- O autor cita RPC como um dos padrões de consumo e aponta a documentação do RabbitMQ para esse assunto.
- Para começar a testar, o texto sugere uma conta free no CloudAMQP ou um container Docker com a imagem rabbitmq:3-management.
- No exemplo em .NET Core, o publisher cria a fila tests, lê mensagens do console e publica no broker.
- No exemplo de consumer, a aplicação escuta a fila tests e imprime as mensagens recebidas no console.
- O fechamento ressalta que o broker vira parte vital da infraestrutura e que o RabbitMQ não deve ser usado como solução automática para qualquer cenário.
