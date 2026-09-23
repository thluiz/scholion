---
title: "Avoiding Identity Obsession in .NET with Entity Framework Core"
date: "2026-09-23T19:35:55+01:00"
category: webclip
has_commentary: false
summary: "Peter Ritchie shows how to configure EF Core shadow properties so a database-required primary key never leaks into a Domain-Driven Design entity's own model."
tags:
  - dotnet
  - entity-framework-core
  - domain-driven-design
  - software-architecture
sources:
  - title: "Peter Ritchie's Blog - Avoiding Identity Obsession in .NET with Entity Framework Core"
    url: "https://blog.peterritchie.com/posts/avoiding-identity-obsession-in-dotnet-with-entity-framework-core"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/blog-peterritchie-com--avoiding-identity-obsession-in-dotnet-with-entity-framework-core.md"
    kind: repo
---

Peter Ritchie follows up an earlier post on Identity Obsession (the practice of pushing a database-required primary key into a Domain entity that doesn't otherwise need one) with a worked example in EF Core. A `Client` entity has its own local identity as an object; the SSN the database wants as a primary key is a persistence detail, not part of the domain model, and he shows how to keep it that way.

The mechanism is EF Core's shadow properties: identifiers configured on the entity type without existing as properties on the C# class itself. The `DbContext` owns the responsibility of generating and reading that shadow key; the repository owns the domain concern of allocating the actual SSN.

## Fichamento

- `IEntityTypeConfiguration<Client>` declares a shadow `Id` property (GUID stored as `varchar(36)`) as the primary key, and a shadow `Ssn` property with a `HasConversion` mapping between the `Ssn` value type and its string column representation.
- The `Client` class itself carries no identifier property. It only exposes domain behavior, in this example a `ChangeName` method.
- `DatabaseContext` reads and writes the shadow properties through `Entry(client).Property(...)`, including `GetClientBySsnAsync`, `GetClientByIdAsync`, and `AddClientAsync`, which sets the shadow `Id` via `Guid.NewGuid()` and the shadow `Ssn` before calling `SaveChangesAsync`.
- `ClientRepository` implements `IClientRepository` (`FindBySsnAsync`, `SaveAsync`, `AddAsync`, `FindClientsAsync`) using the Result Pattern instead of exceptions, and is where SSN allocation happens through an `ISsnRegistry` that reserves a value and commits it only after a successful save.
- `SaveAsync` branches on EF's `EntityState` (`Detached` triggers an add, `Modified` triggers a save) to route persistence without the caller needing to know which case applies.
- Caveat noted in the post: storing raw SSNs is bad practice; the example keeps them in plain text only for clarity, and a real implementation should hash or encrypt the value before persisting it.
