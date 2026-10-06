---
title: "What is the difference between DAO and Repository patterns?"
date: '2015-06-02T18:11:23-03:00'
category: webclip
summary: 'The page contrasts DAO as a data-persistence abstraction, often closer to the database, with Repository as a collection-like abstraction tied to domain objects and aggregate roots, usually with a narrower interface.'
tags: ["dao", "repository-pattern", "data-access-layer", "domain-driven-design"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "What is the difference between DAO and Repository patterns?"
    url: "http://stackoverflow.com/questions/8550124/what-is-the-difference-between-dao-and-repository-patterns"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-06/stackoverflow-com--dao-vs-repository-patterns.md"
    kind: repo
---

DAO is described as an abstraction of data persistence, while Repository is described as an abstraction of a collection of objects. The accepted answer says DAO is often closer to the database and table-centric, while Repository is closer to the Domain and deals with Aggregate Roots. It also says a Repository can be implemented using DAOs, but not the other way around.

## Reading notes

- DAO abstracts persistence and is often closer to the database.
- Repository abstracts a collection of objects and stays closer to the Domain.
- A Repository is described as a narrower interface, with operations like Get, Find, and Add.
- Update is presented as suitable for DAO, while entity changes in a Repository are usually tracked by a separate UnitOfWork.
- Some comments say the terms are often used loosely, and implementations called Repository may really behave like DAO.
- One answer frames both as ways of implementing the Data Access Layer, with Repository behaving like a collection from the client perspective.
- Another answer says the key difference is access to aggregate roots for Repository and to entities for DAO.
