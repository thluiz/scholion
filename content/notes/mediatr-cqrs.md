---
title: Por que não uso MediatR para CQRS
date: '2022-02-27T14:16:47Z'
summary: Cezary Piatek argumenta que MediatR é uma boa implementação do padrão mediator — mas o mediator pattern resolve um problema diferente do CQRS. Usar MediatR para CQRS introduz fricção desnecessária em…
tags:
- tecnico
- architecture
- csharp
has_commentary: true
sources:
- title: Why I don't use MediatR for CQRS — Cezary Piatek
  url: https://cezarypiatek.github.io/post/why-i-dont-use-mediatr-for-cqrs/
  kind: article
---

Cezary Piatek argumenta que MediatR é uma boa implementação do padrão *mediator* — mas o *mediator pattern* resolve um problema diferente do CQRS. Usar MediatR para CQRS introduz fricção desnecessária em algo fundamentalmente simples.

O argumento central: o CQRS exige **separação clara entre leitura e escrita**. O MediatR não tem os conceitos de `Command` e `Query` — só tem `Request`. Você pode criar interfaces de marcação por cima, mas aí está recriando as 4 interfaces que o padrão CQRS já define nativamente, enquanto luta contra uma biblioteca que não foi desenhada para isso.

O "Vanilla CQRS" precisa de apenas 4 interfaces:

```csharp
interface IQueryHandler<in TQuery, TQueryResult>
interface IQueryDispatcher
interface ICommandHandler<in TCommand, TCommandResult>
interface ICommandDispatcher
```

Com dispatchers separados para commands e queries, cross-cutting concerns (cache, auditoria, retry, Unit of Work) ficam em decorators limpos — sem `if (request is IQuery<T>)` espalhados pelo pipeline do MediatR.

A popularidade do MediatR em apps CQRS parece ser um cargo cult com raízes em má compreensão do padrão.
