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

Pasta `Domain/` cheia de classes anêmicas e a equipe jurando que "usa DDD". Isso é organização de diretório, não DDD.

## As 400 páginas que ninguém leu

O livro do Eric Evans (2003) tem quase 600 páginas. Todo mundo leu as primeiras 200: Entity, Value Object, Aggregate, Repository, Service. As outras 400 tratam do que Evans considera o que importa de verdade: **design estratégico**. Bounded Contexts, Context Maps, como times se relacionam através de modelos. Quase ninguém chega lá.

`ValueObject<T>` genérico espalhado pelo projeto e zero conversa sobre onde um contexto termina e outro começa.

Tem a variação com `Repository/`. Um repositório por tabela, `GetById`, `Save`, `Delete`. Wrapper do ORM que não encapsula nada que o ORM já não faça. Repository no Evans é abstração de coleção sobre Aggregates, não espelho de `DbContext` com nomes bonitos.

E tem o `PedidoService` que recebe `PedidoRepository` e repassa tudo. `service.Save(pedido)` chama `repository.Save(pedido)`. Uma camada inteira que não toma nenhuma decisão. Evans distingue três tipos de Service (Domain, Application, Infrastructure), cada um com papel próprio. Se o seu não contém lógica de domínio nem orquestra workflow, é cerimônia.

## Aggregates

Aggregate é **fronteira de consistência transacional**. O que precisa ser consistente junto vive dentro. O que pode ser eventualmente consistente, fora. `Pedido` com seus `ItensDoPedido`, junto, porque não faz sentido salvar um sem o outro. `Cliente`, fora, referenciado por ID. Se o ORM carrega `Pedido → Cliente → Endereços → Preferências` num grafo só, não tem fronteira nenhuma. É um banco relacional disfarçado de objetos.

Vaughn Vernon bate nessa tecla: Aggregates pequenos. Entity raiz, mínimo de estado, referências externas só por identidade. Quando o Aggregate cresce, geralmente a fronteira está errada.

## Bounded Context

"Conta" no módulo de abertura: nome, CPF, documentos. "Conta" no módulo de transações: saldo, extrato, limite. Mesma palavra, dois modelos. Bounded Context é esse perímetro semântico. A fronteira é de linguagem, não de deploy.

Dois Bounded Contexts podem viver no mesmo monólito, em módulos separados. Um microsserviço pode violar fronteiras de contexto por todo lado. Ter 12 serviços não significa ter DDD. Pode significar 12 pedaços de domínio incoerente.

## Domain Events

`PedidoConfirmado`, `PagamentoRecusado`, `EstoqueReservado`. Tempo passado, fato consumado. O que os outros contextos fazem é reagir ao fato.

Em vez de um orquestrador que chama dez serviços na ordem certa (e quebra quando o sexto falha), cada contexto publica o que aconteceu. Quem se interessa, escuta. Acoplamento cai. O custo é consistência eventual, eventos fora de ordem, duplicatas.

## Wlaschin e os tipos

Tipos algébricos fazem mais pelo modelo de domínio do que qualquer framework OO. `EmailVerificado` e `EmailNaoVerificado` não são o mesmo tipo com flag booleana. São **tipos distintos**. A função que dispara newsletter aceita `EmailVerificado`. Ponto. Não é validação em runtime. É o compilador dizendo "isso aqui não passa".

Workflow vira pipeline tipado: `PedidoNaoValidado → Result<PedidoValidado, ErroDeValidacao>`. Quem lê a definição de tipos lê o domínio. O diagrama UML que ninguém atualiza depois do segundo sprint vira desnecessário.

Scott Wlaschin desenvolve isso em *Domain Modeling Made Functional*.

## Quando não usar

DDD tem custo. Conversa com especialistas, modelagem iterativa, refatoração constante. Num CRUD de cadastro de produto a cerimônia não se paga.

O erro mais comum é o oposto: aplicar DDD em tudo e depois reclamar que "é burocrático". É burocrático mesmo, quando não precisa estar lá.
