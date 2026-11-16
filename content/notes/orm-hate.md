---
title: "Orm Hate"
date: '2020-02-22T12:11:52+00:00'
category: webclip
summary: 'Martin Fowler argues that ORM tools solve a hard in-memory/relational mapping problem, so complaints about complexity and leakage miss context. He favors using them with realistic expectations, or avoiding the problem when the model fits other approaches.'
tags: ["orm", "relational-database", "nosql", "cqrs"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "bliki: Orm Hate"
    url: "https://martinfowler.com/bliki/OrmHate.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/martinfowler-com--orm-hate.md"
    kind: repo
---

Martin Fowler argues that ORM tools are often criticized without enough context. The mapping problem is hard because it synchronizes two different representations of data, and that complexity brings learning costs, leakage, and concurrency issues.

He says the real question is what to do instead. Writing your own ORM usually leads to more pain, while open source tools already remove a large part of the work. ORM criticism often comes from expecting it to do everything, when it really handles most of the repetitive mapping and still leaves the hardest cases to someone who understands the database. He also says the domain model sometimes needs to be more relational to keep the mapping simpler, and that reading-only workloads can be a good fit for CQRS. When the mapping problem can be avoided, he suggests either using relational thinking all the way through the application or choosing a NoSQL model that fits the problem well.

## Reading notes

- ORM tools are criticized because they are complex and provide only a leaky abstraction over relational storage.
- The object/relational mapping problem is hard because it synchronizes in-memory data structures with relational data.
- The problem is harder because changes can happen on both sides and concurrency must be handled.
- Fowler asks critics to state the alternative instead of only attacking ORMs.
- Rolling your own ORM usually becomes a quagmire, even if it looks promising at first.
- Open source ORMs such as iBatis, Hibernate, and Active Record removed much of the burden of building that machinery from scratch.
- A common frustration is inflated expectations that the ORM should handle everything.
- An ORM can cover most mapping work, but the last part still needs someone who understands relational databases.
- He accepts the leaky abstraction criticism, but treats it as a reason to use ORMs with the right expectations, not a reason to reject them.
- Active Record is presented as an approach that handles boring work and still leaves room for SQL when needed.
- Sometimes a more relational domain model is reasonable because it reduces mapping complexity.
- In some cases, Row Data Gateways are a better fit than a behavior-rich domain model.
- One exception to using an ORM is read-only access, where a one-way mapping problem is simpler.
- Another route is to avoid the problem by using relations in memory throughout the application.
- If the application fits a NoSQL model well, mapping can sometimes be avoided entirely.
- NoSQL still only works well when the fit between application model and storage model is good.
- Some problems still require a relational model, whether because of technical fit or organizational constraints.
- ORMs deserve more respect and understanding because they address a real problem in enterprise software.
