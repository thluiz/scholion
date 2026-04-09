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

A maioria dos projetos que diz usar DDD usa pasta chamada `Domain/` com classes anêmicas dentro. Isso não é DDD — é organização de diretório.

## O livro que pouca gente leu

O livro do Eric Evans (2003) tem quase 600 páginas. As primeiras 200 tratam dos building blocks táticos: Entity, Value Object, Aggregate, Repository, Service. É a parte que todo mundo conhece. As outras 400 — a parte que Evans considera mais relevante — tratam de **design estratégico**: Bounded Contexts, Context Maps, relações entre times. Quase ninguém chega lá.

O resultado é previsível: projetos cheios de `ValueObject<T>` genéricos e nenhuma conversa sobre onde um contexto termina e outro começa.

## Aggregate: a fronteira que ninguém respeita

Um Aggregate não é um objeto grande que contém outros objetos. É uma **fronteira de consistência transacional**. Tudo que precisa ser consistente junto vive dentro do mesmo Aggregate. Tudo que pode ser eventualmente consistente vive fora.

Na prática: um `Pedido` com seus `ItensDoPedido` forma um Aggregate porque não faz sentido salvar o pedido sem os itens. O `Cliente` que fez o pedido é outro Aggregate — referenciado por ID, não por navegação de objeto. Se seu ORM carrega o grafo inteiro de `Pedido → Cliente → Endereços → Preferências`, você não tem Aggregates. Tem um grafo de objetos com características de banco relacional.

Vaughn Vernon destila isso numa regra: Aggregates pequenos. Uma Entity raiz, o mínimo de estado interno, referências externas só por identidade.

## Bounded Context ≠ microsserviço

Um Bounded Context é um perímetro linguístico e de modelo. Dentro dele, "Conta" significa uma coisa. No contexto ao lado, "Conta" significa outra. A fronteira é semântica, não técnica.

Microsserviço é uma decisão de deploy. Você pode ter dois Bounded Contexts no mesmo monólito (módulos separados, modelos distintos) e pode ter um microsserviço que viola fronteiras de contexto por todo lado. Confundir os dois é o erro mais caro que eu vejo em projetos que "adotam DDD".

## Domain Events: o que aconteceu, não o que você quer que aconteça

Um Domain Event registra um fato consumado: `PedidoConfirmado`, `PagamentoRecusado`, `EstoqueReservado`. Tempo passado. Aconteceu, não tem como desfazer o fato — só reagir a ele.

Isso muda a arquitetura. Em vez de um serviço orquestrador que chama dez outros na sequência certa, cada contexto publica o que aconteceu e os interessados reagem. O acoplamento cai. O preço é aceitar consistência eventual e lidar com a complexidade de eventos fora de ordem, duplicados ou perdidos.

## O que Wlaschin muda na conversa

Scott Wlaschin, em *Domain Modeling Made Functional*, argumenta que tipos algébricos fazem mais pelo DDD do que qualquer framework OO. O ponto dele:

- Um `EmailVerificado` e um `EmailNaoVerificado` são **tipos distintos**, não um `Email` com flag booleana. O compilador impede que você mande newsletter para email não verificado — não por validação em runtime, mas porque a assinatura da função não aceita o tipo errado.
- Um workflow é uma função: `PedidoNaoValidado → Result<PedidoValidado, ErroDeValidacao>`. O pipeline inteiro do domínio se lê como uma sequência de transformações tipadas. Sem surpresas, sem exceções voando.
- O modelo vira documentação. Quem lê a definição de tipos entende o domínio sem precisar de diagrama UML.

## Onde DDD não cabe

DDD tem custo. Exige investimento em conversa com especialistas, modelagem iterativa e refatoração constante do modelo. Se o domínio é um CRUD com regras triviais — cadastro de produto com nome, preço e estoque — DDD adiciona cerimônia sem retorno. Evans é explícito sobre isso: DDD é para **domínios complexos** onde a lógica de negócio é o problema, não a infraestrutura.

A pergunta antes de adotar não é "como implemento DDD?" — é "meu domínio justifica esse investimento?"
