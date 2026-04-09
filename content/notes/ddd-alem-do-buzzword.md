---
title: "DDD além do buzzword"
date: 2026-04-09T16:10:18+01:00
summary: "O que Domain-Driven Design realmente pede de quem programa — e por que a maioria dos projetos que dizem usar DDD não usa."
tags: ["ddd", "arquitetura", "software"]
has_commentary: true
sources:
  - title: "Domain-Driven Design: Tackling Complexity in the Heart of Software"
    author: "Eric Evans"
    year: 2003
    publisher: "Addison-Wesley"
    kind: book
  - title: "Domain Modeling Made Functional"
    author: "Scott Wlaschin"
    year: 2018
    publisher: "Pragmatic Bookshelf"
    kind: book
  - title: "Implementing Domain-Driven Design"
    author: "Vaughn Vernon"
    year: 2013
    publisher: "Addison-Wesley"
    kind: book
---

A maioria dos projetos que diz usar DDD tem uma pasta chamada `Domain/` com classes anêmicas dentro. Isso é organização de diretório, não DDD.

## As 400 páginas que ninguém leu

O livro do Eric Evans (2003) tem quase 600 páginas. Todo mundo conhece as primeiras 200: Entity, Value Object, Aggregate, Repository, Service — os building blocks táticos. As outras 400 tratam de **design estratégico**: Bounded Contexts, Context Maps, relações entre times. Evans considera essa a parte que importa.

Aí você olha os projetos e encontra `ValueObject<T>` genérico por todo lado. Nenhuma conversa sobre onde um contexto termina e outro começa.

## Aggregates

Um Aggregate não é um objeto grande que contém outros. É uma **fronteira de consistência transacional**: o que precisa ser consistente junto vive dentro; o que pode ser eventualmente consistente vive fora.

`Pedido` com seus `ItensDoPedido` — Aggregate, porque não faz sentido salvar um sem o outro. `Cliente` que fez o pedido — outro Aggregate, referenciado por ID. Se seu ORM carrega `Pedido → Cliente → Endereços → Preferências` num grafo só, você não tem Aggregates. Tem um banco relacional disfarçado de objetos.

A regra do Vaughn Vernon: Aggregates pequenos. Entity raiz, mínimo de estado interno, referências externas por identidade.

## Bounded Context não é microsserviço

Bounded Context é perímetro semântico. Dentro dele, "Conta" significa uma coisa. No contexto vizinho, outra. A fronteira é de linguagem, não de deploy.

Dois Bounded Contexts podem viver no mesmo monólito, em módulos separados. Um microsserviço pode violar fronteiras de contexto por todo lado. Confundir um com o outro sai caro.

## Domain Events

Um Domain Event registra fato consumado: `PedidoConfirmado`, `PagamentoRecusado`, `EstoqueReservado`. Tempo passado. Não tem como desfazer — só reagir.

Muda o desenho da comunicação entre contextos. Em vez de um orquestrador que chama dez serviços na sequência certa, cada contexto publica o que aconteceu e quem se interessa reage. Acoplamento cai. O custo: consistência eventual, eventos fora de ordem, duplicatas.

## Wlaschin e os tipos algébricos

Scott Wlaschin argumenta em *Domain Modeling Made Functional* que tipos algébricos fazem mais pelo DDD do que qualquer framework OO.

`EmailVerificado` e `EmailNaoVerificado` são **tipos distintos** — não um `Email` com flag booleana. A função que dispara newsletter aceita `EmailVerificado` e ponto. Não é validação em runtime; é o compilador recusando o código errado antes de rodar.

Um workflow do domínio vira `PedidoNaoValidado → Result<PedidoValidado, ErroDeValidacao>`. Lê-se como pipeline. Quem lê a definição de tipos lê o domínio — sem diagrama UML, sem documentação paralela que envelhece no primeiro sprint.

## Quando não usar

DDD exige conversa com especialistas, modelagem iterativa, refatoração constante do modelo. Se o domínio é CRUD com regras triviais — cadastro de produto com nome, preço, estoque — a cerimônia não se paga. Evans é direto: DDD serve para domínios onde a lógica de negócio é o problema, não a infraestrutura.

Antes de adotar: meu domínio justifica esse investimento?
