---
title: "I can do all things through Postgres: Lessons for the Elixir programmer"
date: '2020-07-05T14:10:41+00:00'
category: webclip
summary: 'The post argues that some application logic is better handled by Postgres than by Elixir code, using examples like constraints, citext, nearby rows, CTEs, and fuzzy search.'
tags: ["postgres", "elixir", "ecto", "sql"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "I can do all things through Postgres: Lessons for the Elixir programmer | by Todd Resudek | Medium"
    url: "https://medium.com/@toddresudek/i-can-do-all-things-through-postgres-lessons-for-the-elixir-programmer-400fd805c23a"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/medium-com--i-can-do-all-things-through-postgres-lessons-for-the-elixir-.md"
    kind: repo
---

The post argues that Postgres can solve some development problems more effectively than application code. It says the database has strengths in validation, querying, ordering, and text matching, and that moving selected logic into Postgres can also help redistribute load when the application is under heavier CPU pressure than the database.

## Reading notes

- The article’s goal is to show another way to think about development problems, especially cases that could be solved in Elixir but are better handled by the database.
- It says Postgres is often better at certain tasks because it has gained features and performance improvements over many years.
- It notes that some projects have application CPUs under constant load while the DB server stays mostly idle.
- The examples assume Ecto, but the ideas can be used in other systems.
- It says moving logic into Postgres does not require abandoning the ORM, because migrations and fragments let you use SQL sparingly.
- For complex constraints, it describes a car schema with engine_type, mpg, and kwh, and says a car should not have data in all three fields.
- It shows using a database check constraint together with check_constraint/3 in the changeset so the database enforces the rule and the changeset returns a useful error.
- It says this also validates all data in the database, including data imported outside the changeset.
- For citext, it describes a Postgres extension that adds a case-insensitive string type.
- It says Postgres handles this by converting both sides of the query to lowercase, while the Elixir version is more complex and would require migrating existing data.
- For adjacent rows, it describes finding cars around a target price and says window functions like lag and lead let Postgres return nearby rows from the indexed order.
- It explains that CTEs are temporary result sets that can be referenced inside another SQL statement, including SELECT, INSERT, UPDATE, and DELETE.
- It says CTEs are useful when a recursive query is needed.
- For string searches, it says fuzzy matching can be inefficient in Elixir when searching by make and model and when returning near matches for misspellings.
- It says the Elixir approach may require loading every car, iterating twice, and using jaro_distance from the String module.
- It says Postgres can handle this logic with built-in functions, including Levenshtein distance without plugins.
- It concludes that Postgres has strong tools for organizing, querying, and transforming data, while still leaving room for application logic when appropriate.
