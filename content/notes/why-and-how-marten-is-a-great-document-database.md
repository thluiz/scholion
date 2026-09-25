---
title: "Why and How Marten is a Great Document Database"
date: '2026-09-25T17:05:55+01:00'
category: webclip
summary: 'The post shows how Marten stores and loads C# objects as JSON in PostgreSQL, creates missing database objects on demand, and fits the .NET host model while keeping ACID transactions and rich document features.'
tags: ["marten", "postgresql", "document-database", "dotnet"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why and How Marten is a Great Document Database"
    url: "https://jeremydmiller.com/2024/08/29/why-and-how-marten-is-a-great-document-database/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/jeremydmiller-com--why-and-how-marten-is-a-great-document-database.md"
    kind: repo
---

Marten is presented as a document database option built on PostgreSQL and aimed at .NET applications. The post shows a simple flow where a `Customer` object is stored and loaded without manual mapping or prior database structure, and it also shows Marten being added through `AddMarten()` in a web application.

The post also says Marten inherits PostgreSQL’s ACID transactional model, so multiple document operations can happen inside the same boundary without relying on eventual consistency for immediate queries. It then lists built-in features such as multi-tenancy, LINQ support, batch querying, indexing, soft delete, control over identity map and dirty checking, and optimistic concurrency.

## Reading notes

- Stores C# objects as JSON in PostgreSQL, so the type must be serializable both ways.
- Creates missing database objects for a document type on demand in default settings.
- Integrates with the .NET host through `IServiceCollection.AddMarten()`.
- Uses PostgreSQL’s ACID model, so inserts, patches, and queries can run within transactional boundaries.
- Includes multi-tenancy with conjoined and database-per-tenant models.
- Includes LINQ provider support, batch querying, indexing, soft delete, and optimistic concurrency.
- Emphasizes that PostgreSQL is widely available, cloud friendly, and Docker friendly.
