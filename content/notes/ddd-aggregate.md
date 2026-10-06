---
title: "DDD Aggregate"
date: '2015-05-14T21:02:39-03:00'
category: webclip
summary: 'A DDD aggregate is a cluster of domain objects treated as one unit, with a single aggregate root handling outside references and integrity. Data is loaded and saved as whole aggregates, and transactions should not cross aggregate boundaries.'
tags: ["domain-driven-design", "aggregate-root", "transactions"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "DDD_Aggregate"
    url: "http://martinfowler.com/bliki/DDD_Aggregate.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/martinfowler-com--ddd-aggregate.md"
    kind: repo
---

A DDD aggregate is a cluster of domain objects that is treated as a single unit. The page gives an order and its line items as an example, where the objects stay separate but are handled together as one aggregate.

An aggregate has one component object as its aggregate root. References from outside should point only to the root, which protects the integrity of the whole aggregate. The page also says aggregates are the basic unit for loading and saving data, and that transactions should not cross aggregate boundaries. It distinguishes DDD aggregates from collection classes and notes that the same term is used in other contexts with a different meaning.

## Reading notes

- A DDD aggregate is a cluster of domain objects treated as a single unit.
- An order and its line items are given as an example of separate objects handled together.
- One component object acts as the aggregate root.
- Outside references should go only to the aggregate root.
- The root ensures the integrity of the aggregate as a whole.
- Aggregates are the basic unit for loading and saving data.
- Transactions should not cross aggregate boundaries.
- DDD aggregates are domain concepts, unlike generic collection classes.
- An aggregate often contains multiple collections and simple fields.
- The term "aggregate" is used in other contexts, such as UML, with a different meaning.
