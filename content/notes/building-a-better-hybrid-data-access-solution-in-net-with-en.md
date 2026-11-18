---
title: "Building a Better Hybrid Data Access Solution in .NET with Entity Framework + RepoDb"
date: '2020-08-26T19:31:20+00:00'
category: webclip
summary: 'The article argues that Entity Framework works well for many cases, but RepoDb fills gaps such as targeted updates, deletes, upserts, bulk operations, caching, and dynamic raw-SQL handling.'
tags: ["entity-framework", "repodb", "dotnet", "data-access"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building a Better Hybrid Data Access Solution in .NET with Entity Framework + RepoDb"
    url: "https://blog.devgenius.io/building-a-better-hybrid-data-access-solution-in-net-with-entity-framework-repodb-d1039a648301"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/blog-devgenius-io--building-a-better-hybrid-data-access-solution-in-net-with-en.md"
    kind: repo
---

The article argues that Entity Framework is useful, but that it becomes limited when the application needs targeted data access, bulk work, caching, or more dynamic SQL handling. RepoDb is presented as a hybrid micro-ORM that complements EF by covering those cases with less friction.

## Reading notes

- Entity Framework is described as a common ORM in .NET, but one that adds abstractions over the database and reduces direct access to RDBMS capabilities.
- For inline updates, EF is said to update all columns of a row, while RepoDb can update only the key and the target columns.
- For deletes, EF requires loading the referenced object first, while RepoDb supports a more direct delete operation.
- For upsert or merge scenarios, EF is presented as requiring a database round-trip, while RepoDb offers a Merge operation without that round-trip.
- Bulk insert, merge, update, and delete are described as out of scope for EF by default and available in RepoDb out of the box for SQL Server.
- The article says EF is tightly bound to DbSet<T>, which makes dynamic targeted operations difficult.
- RepoDb is presented as supporting dynamic insert and update operations for specific columns, including reuse of a model across multiple tables.
- The article says developers often fall back to raw SQL, but EF’s FromSqlRaw and FromSqlInterpolated remain tied to the DbSet<T> model and the result shape.
- RepoDb is described as able to execute raw SQL more dynamically, including result sets with extra columns or extra properties.
- EF is said not to support second-layer caching by default, while RepoDb is described as supporting cache keys for repeated reads.
- The article says this can reduce round-trips for scenarios such as lookup tables and client-side joins.
- RepoDb is also presented as useful when a solution must work across multiple RDBMS data sources and combine data from different systems.
- The article closes by recommending that developers avoid overusing EF where it is not practical and consider combining it with RepoDb.
