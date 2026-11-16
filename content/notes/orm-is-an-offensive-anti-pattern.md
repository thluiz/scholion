---
title: "ORM Is an Offensive Anti-Pattern"
date: '2026-11-16T02:41:35+00:00'
category: webclip
summary: 'The article argues that ORM breaks object-oriented design by splitting data from behavior, exposing SQL throughout the app, and making tests harder. It proposes SQL-speaking objects as the alternative.'
tags: ["orm", "object-oriented-programming", "sql-speaking-objects", "database"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "ORM Is an Offensive Anti-Pattern"
    url: "https://yegor256.com/2014/12/01/orm-offensive-anti-pattern.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/yegor256-com--orm-is-an-offensive-anti-pattern.md"
    kind: repo
---

The article argues that ORM violates object-oriented principles by tearing objects apart into passive data holders and database-handling machinery. It says ORM exposes the relational model across the application, does not really hide SQL, and makes testing awkward because objects depend on session factories and database wiring.

It proposes SQL-speaking objects as the alternative: separate interfaces for plural and singular concepts, immutable objects, and database interaction encapsulated inside those objects. It also shows how decorators can cache data for performance and how transactions can be wrapped in a callable object.

## Reading notes

- ORM is presented as an anti-pattern that splits one cohesive object into data on one side and persistence logic on the other.
- The article says ORM does not hide SQL; it spreads SQL or SQL-like queries through the application.
- Testing becomes difficult because objects depend on SessionFactory and database-backed integration tests.
- The suggested alternative is SQL-speaking objects that encapsulate persistence inside the object boundary.
- The design uses two interfaces, Posts and Post, to represent the table and a row.
- Posts lists rows and adds a new row, while Post exposes id, date, and title through methods.
- The implementation examples use JDBC-style code inside PgPosts and PgPost, so the database access stays inside the objects.
- Performance concerns are handled by a decorator that caches date and title values.
- Transactions are wrapped in a Txn class that accepts a callable and commits or rolls back around it.
