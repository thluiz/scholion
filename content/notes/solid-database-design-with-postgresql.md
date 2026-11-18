---
title: "SOLID Database Design With PostgreSQL"
date: '2020-02-22T12:12:03+00:00'
category: webclip
summary: 'The piece summarizes Chris Travers’s ideas on applying SOLID principles to relational databases, especially PostgreSQL table inheritance, functions, triggers, and views to shape flexible database APIs.'
tags: ["postgresql", "database-design", "solid-principles", "table-inheritance"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "SOLID Database Design With PostgreSQL"
    url: "https://www.infoq.com/news/2013/02/solid-database-design/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/infoq-com--solid-database-design-with-postgresql.md"
    kind: repo
---

Chris Travers’s series on “Building SOLID Databases” applies several OOP principles to data models and database code. The article focuses on PostgreSQL features such as table inheritance and shows how they can support extension points, shared structure, and database interfaces.

## Reading notes

- Normalization is usually enough to satisfy single responsibility in a purely relational database, but table inheritance can help when fields commonly appear together and depend on other fields.
- For notes, a purely relational design may use many separate notes tables or one global notes table with join tables, while an object-relational design can use multiple notes tables inheriting from a common notes table.
- Open/Closed can be supported with table inheritance, as in pg_message_queue 0.2, where separate tables handle different data types while inheriting from one common table.
- Liskov Substitution can break under table inheritance, as shown by a square inheriting from a rectangle and failing when an update on the parent changes height without preserving the square constraint.
- One way to handle that problem is to avoid updates and keep rows immutable; another is to use triggers that move rows between tables when updates occur.
- Interface Segregation in databases mainly concerns user-defined functions and stored procedures, which Chris treats as interfaces to the underlying data.
- He suggests that a function or stored procedure should usually contain one large query with minimal surrounding logic, and that many optional parameters or more than five queries may indicate unnecessary complexity.
- Dependency Inversion can reduce leaky abstractions when application logic is tightly bound to stored procedures, and possible tools include a service locator pattern, views, functions, custom datatypes, triggers, and notifications.
- The main design advice is to treat the database as an application that exposes an appropriate API.
