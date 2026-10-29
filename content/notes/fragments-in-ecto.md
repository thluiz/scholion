---
title: "Fragments in Ecto"
date: '2016-02-29T10:53:30-03:00'
category: webclip
summary: 'The post shows how to query date ranges in Ecto by using `fragment/1` with Postgres `OVERLAPS`, plus `type/2` to tell Ecto the date types it cannot infer.'
tags: ["ecto", "elixir", "postgresql", "date-ranges"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Fragments in Ecto"
    url: "http://learningelixir.joekain.com/fragments-in-ecto/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-02/learningelixir-joekain-com--fragments-in-ecto.md"
    kind: repo
---

The post uses date ranges as an example to show how custom SQL can be added to an Ecto query. It starts from a failing test for an `overlapping/1` function, then builds a query that can be passed to `Repo.all/2`.

## Reading notes

- The example is based on Elixir 1.2.1 and Ecto 1.1.3.
- The project uses a `DateRange` schema with `start` and `end` fields.
- The database table is created with a migration for `date_ranges`.
- The tests run inside a database transaction.
- The test setup uses the SQL Sandbox adapter.
- A `setup/1` function restarts the test transaction for each test.
- The test seeds a list of date ranges into the database.
- The failing test expects an `overlapping/1` function on `DateRange`.
- `overlapping/1` is meant to return an `Ecto.Query.t` value.
- The query uses `fragment/1` to call Postgres `OVERLAPS`.
- The fragment uses placeholders that are filled by query arguments.
- `type/2` is used because Ecto does not know the types inside the fragment.
- The post says `target.start` and `target.end` are described as `Ecto.Date`.
- The conclusion says the main point is injecting custom SQL into a composable Ecto query.
