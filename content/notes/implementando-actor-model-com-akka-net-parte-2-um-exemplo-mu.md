---
title: "Implementando “Actor Model” com Akka.net – Parte 2 – Um exemplo muito simples"
date: '2015-05-29T20:24:12-03:00'
category: webclip
summary: 'Mostra um exemplo mínimo de Akka.net com um chat de console entre UserInterfaceActor e SimpleBotActor, explicando o bootstrapping, o envio de mensagens e o uso de Sender.'
tags: ["akka-net", "actor-model", "csharp", "concurrency"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Implementando “Actor Model” com Akka.net – Parte 2 – Um exemplo muito simples"
    url: "http://elemarjr.net/2015/05/29/implementando-actor-model-com-akka-net-parte-2-um-exemplo-muito-simples/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/elemarjr-net--implementando-actor-model-com-akka-net-parte-2-um-exemplo-mu.md"
    kind: repo
---

O texto apresenta um exemplo bem simples de Akka.net: um chat de console em que o usuário conversa com um bot. A aplicação cria um ActorSystem, instancia os atores e inicia a interação com uma mensagem "start". O autor usa esse exemplo para mostrar que o modelo de execução é assíncrono e que a aplicação espera a terminação do sistema.

## Fichamento

- O exemplo implementa um chat simples em aplicação console, com um usuário conversando com um bot.
- São criados dois atores, UserInterfaceActor para a interação com o usuário e SimpleBotActor para a lógica do bot.
- O bootstrapping cria o ActorSystem, instancia os atores e envia "start" para o ator de interface.
- O texto explica que o sistema funciona como um contexto maior de execução e que uma aplicação costuma ter apenas um ActorSystem.
- O modelo de execução do Akka é assíncrono, o que justifica a chamada para AwaitTermination.
- As duas classes de ator herdam de UntypedActor.
- O método OnReceive é apontado como o ponto central, porque recebe e trata as mensagens enviadas ao ator.
- UserInterfaceActor guarda uma referência ao bot para poder se comunicar com ele.
- O envio de mensagens é feito com Tell.
- O ator que recebe a mensagem pode responder ao remetente por meio da propriedade Sender.
- SimpleBotActor responde a entradas como hello, hi, bye e restart com mensagens de texto e sinais como continue, exit e start.
- Quando recebe bye, o bot manda exit; quando recebe restart, manda start.
