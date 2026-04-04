---
title: "SOLID Principles"
date: 2026-04-04T08:14:15+01:00
summary: "Five object-oriented design principles introduced by Robert C. Martin (2003); the acronym was coined by Michael Feathers around 2004."
tags: ["software-engineering", "object-oriented", "design-principles"]
has_commentary: false
sources:
  - title: "SOLID"
    url: "https://en.wikipedia.org/wiki/SOLID"
    kind: "wiki"
  - title: "Agile Software Development, Principles, Patterns, and Practices"
    author: "Robert C. Martin"
    year: 2003
    kind: "book"
---

SOLID is a mnemonic for five object-oriented design principles introduced by Robert C. Martin in his 2003 book Agile Software Development, Principles, Patterns, and Practices. The acronym itself was coined by Michael Feathers around 2004.

- **S — Single Responsibility Principle**: a class should have only one reason to change.
- **O — Open/Closed Principle**: classes should be open for extension, but closed for modification.
- **L — Liskov Substitution Principle**: objects of a derived class must be usable in place of the base class without breaking the program.
- **I — Interface Segregation Principle**: clients should not be forced to depend on interfaces they do not use.
- **D — Dependency Inversion Principle**: depend upon abstractions, not concretes.

The principles aim to make software more understandable, flexible, and maintainable. They are guidelines, not laws — applying them dogmatically can lead to over-engineering, but ignoring them tends to produce rigid, fragile code.
