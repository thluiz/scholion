---
title: "The Performance Issue „Cartesian Explosion“ Made Its Comeback In Entity Framework Core 3"
date: '2026-11-16T19:42:41+00:00'
category: webclip
summary: 'The article explains how EF Core 3.0/3.1 reintroduced the Cartesian Explosion problem, why JOINs on one-to-many relationships can replicate rows, and why query splitting can reduce database load.'
tags: ["entity-framework-core", "cartesian-explosion", "query-splitting"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Performance Issue „Cartesian Explosion“ Made Its Comeback In Entity Framework Core 3"
    url: "https://www.thinktecture.com/de/entity-framework-core/cartesian-explosion-problem-in-3-1/?utm_medium=twitter&utm_source=social&utm_campaign=The+performance+issue+Cartesian+Explosion+made+its+comeback+in+Entity+Framework+Core+3"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/thinktecture-com--cartesian-explosion-made-its-comeback-in-ef-core-3.md"
    kind: repo
---

EF Core 3.0/3.1 changed SQL generation in a way that removed implicit client-side evaluation and the N+1 query problem, but it also brought back the Cartesian Explosion problem. The article shows how one-to-many JOINs replicate rows, how extra Includes can make the result set grow quickly, and how EF adds ORDER BY clauses that can add load when the result set is large.

## Reading notes

- In EF Core 3.0/3.1, SQL generation changed significantly.
- Those changes removed implicit client-side evaluation and the N+1 query problem.
- The same changes reintroduced the Cartesian Explosion problem.
- In a one-to-many JOIN, rows from the one side are repeated for each matching row on the many side.
- With one ProductGroup and 1000 Products, the result set contains repeated ProductGroup data.
- More Includes can make the result set explode.
- EF also adds an ORDER BY on entity identifiers for internal purposes.
- That ordering adds load when the result set is very large.
- The proposed solution is query splitting, as in EF6.
- The example loads ProductGroups and Products in separate queries.
- The article says the hard part is finding queries that should be split.
- It recommends using database statistics and execution plans to decide how far to split queries.
