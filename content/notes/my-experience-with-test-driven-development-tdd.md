---
title: "My Experience With Test Driven Development (TDD)"
date: '2026-11-16T00:51:33+00:00'
category: webclip
summary: 'The author defines TDD, describes its three rules, and explains how writing tests first exposed gaps in schema design and reduced manual testing while refactoring a backend to SQL.'
tags: ["test-driven-development", "sql", "postgres", "schema-design"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "My Experience With Test Driven Development (TDD)"
    url: "https://dev.to/russ/my-experience-with-test-driven-development-tdd-3fb5"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--my-experience-with-test-driven-development-tdd.md"
    kind: repo
---

The author defines test-driven development as writing a test before the code, then refactoring after the code passes. They also restate Uncle Bob’s three rules and frame TDD as a way to keep code modular, flexible, and focused on what is needed to pass tests.

## Reading notes

- The author was refactoring a project from NoSQL to SQL and decided to rewrite the backend.
- At first, they did not know where to start because the files and references they needed did not exist yet.
- They created basic files and SQL schema files before having tests that asked for them, which they later saw as breaking rule #1.
- Their first test checked that an empty database returned an empty array, and it passed easily.
- Their second test inserted data and returned it, but failed because the schema had circular references between the business and address tables.
- The failure showed that the schema design was flawed and led them to rewrite and rethink the database structure.
- After the schema was corrected, writing later tests became easier and required less research.
- The author says TDD would have saved time by reducing manual testing and by showing failures immediately.
- They also say TDD helped reveal what they still needed to learn about Postgres responses and data insertion.
- They see TDD as especially useful for entry-level developers and plan to keep using it in their projects.
