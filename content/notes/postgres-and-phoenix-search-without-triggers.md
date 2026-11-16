---
title: "Postgres & Phoenix Search Without Triggers"
date: '2026-11-16T03:00:01+00:00'
category: webclip
summary: 'The post replaces trigger-based materialized-view refreshes with an Elixir GenServer that batches and refreshes search views asynchronously, then adds trigram similarity and saved-search suggestions.'
tags: ["postgresql", "phoenix", "elixir", "search"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Postgres & Phoenix Search Without Triggers"
    url: "https://devrain.io/ecto/phoenix/elixir/postgresql/2020/05/14/postgres-and-phoenix-search-without-triggers.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devrain-io--postgres-and-phoenix-search-without-triggers.md"
    kind: repo
---

The post describes how the author replaced database triggers for search maintenance with an Elixir GenServer. Instead of refreshing materialized views on every insert, update, or delete, the application now queues refreshes and runs them asynchronously, which reduces slow pages caused by repeated refreshes.

## Reading notes

- The initial search setup used materialized views per entity, refreshed by database triggers on insert, update, and delete.
- Some pages became slow because each trigger could recreate a materialized view, and a refresh could take up to 3 seconds.
- Because trigger work happened in the same transaction as the statement, create, update, and delete actions on one table had to wait for each other.
- The author removed the triggers and replaced them with a GenServer.
- Repo insert, update, and delete functions were extended so they call an async callback after the database action is resolved.
- The callback checks which module changed and asks a search interface to refresh the related materialized view.
- The search interface maps a table to its search views and sends refresh requests to the GenServer with `GenServer.cast`.
- The RefresherServer keeps a queue, deduplicates pending views, waits a minimum time before refreshing, and limits refresh concurrency.
- Refreshes are run with `REFRESH MATERIALIZED VIEW CONCURRENTLY` through `Repo.query/3`.
- The solution still uses database connections, so a queue size that matches or exceeds available connections can block other application calls.
- In tests, the callbacks should be skipped or the timeout should be lowered, because search views are generated asynchronously and must be waited on.
- For typo-tolerant search, the post adds trigram similarity with PostgreSQL’s `%` operator and the `similarity` function.
- Search queries combine full-text search with a trigram match on the title.
- Saved searches are used to produce a “Did you mean” suggestion when a typed keyword matches a common previous search.
- The same searches table is also used for typeahead suggestions based on prefixes already searched before.
