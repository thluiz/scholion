---
title: "Folding Window Functions Into Ecto"
date: '2016-02-29T10:49:59-03:00'
category: webclip
summary: 'The post shows how to rank trips by category with PostgreSQL window functions, then reproduce the query in Ecto 2.0 using raw SQL and tests, comparing it with a naive in-memory approach.'
tags: ["ecto", "postgresql", "window-functions", "elixir"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Folding Window Functions Into Ecto"
    url: "http://sorentwo.com/2016/02/08/folding-window-functions-into-ecto.html?utm_campaign=elixir_radar_38&utm_medium=email&utm_source=RD+Station"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-02/sorentwo-com--folding-window-functions-into-ecto.md"
    kind: repo
---

The article starts from a trip-booking app that needs to highlight the two most popular trips in each category. It first solves the task in naive Elixir by loading all trips, grouping them in memory, sorting them by favorites and name, and taking the top results, then moves the same logic into PostgreSQL with a window function using `row_number()` partitioned by category.

It then shows how, in Ecto 2.0, the window query is built with `Ecto.Adapters.SQL.query` and a subquery that filters rows by `row_number`, because Ecto does not yet support `OVER` clauses or arbitrary `FROM` clauses. The benchmark section reports that the naive approach is only about 2x slower even with 20,000 trips, and the post ends by noting a hybrid join-based approach suggested by José Valim.

## Reading notes

- The example app needs to surface the top two trips in each category.
- The first implementation loads trips into memory, groups them by category, sorts them by favorites and name, and takes the requested number from each group.
- The article treats that in-memory approach as too inefficient for production use when the goal is only a few results.
- PostgreSQL window functions are introduced as a way to calculate across related rows.
- `row_number()` with `PARTITION BY category` assigns positions within each category.
- Adding `ORDER BY favorites DESC, name ASC` makes the ranking deterministic.
- Ecto 2.0 does not provide built-in `OVER` support or arbitrary `FROM` clauses.
- The working Ecto version uses a raw SQL query with a subquery and filters rows where `row_number` is at most the requested limit.
- The benchmark compares the naive in-memory version with the window-function version across 5,000, 10,000, and 20,000 trips.
- The post says the naive strategy ends up only about 2x slower at 20,000 records.
- A later edit adds a hybrid join-based approach suggested by José Valim.
