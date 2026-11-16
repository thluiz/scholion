---
title: "The Repository Pattern, Ecto, and Database-less Testing"
date: '2020-07-05T14:10:34+00:00'
category: webclip
summary: 'Explains the repository pattern in Ecto, why it helps separate data from persistence, and how to swap in a mock Repo so tests can run without a database.'
tags: ["ecto", "repository-pattern", "elixir", "testing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Repository Pattern, Ecto, and Database-less Testing"
    url: "https://akoutmos.com/post/ecto-repo-testing"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/akoutmos-com--the-repository-pattern-ecto-and-database-less-testing.md"
    kind: repo
---

The post explains the repository pattern as an abstraction between data models and persistence, then shows how Ecto uses that interface for inserts and queries. It argues that this separation makes the persistence layer swappable, which is useful for testing and for other setups like replicas.

## Reading notes

- The repository pattern sits between data models and the persistence layer, and Ecto uses that interface to perform database operations.
- An insert works by building a changeset, passing it to the repository, and letting the repository decide whether to write it.
- The `User` schema stays separate from the database, while the repository handles database-specific work.
- The pattern is useful because data and persistence remain decoupled while still sharing a common interface.
- Ecto 3 split `ecto` and `ecto_sql`, with `ecto` focused on mapping and validation and `ecto_sql` on database adapters.
- A repository adapter can be swapped as long as it respects the same interface.
- This is helpful in tests when a real database is not practical.
- It also supports use cases like read/write replicas, since the model does not need to know where data comes from or goes to.
- The example app is an inventory system that uses Postgres in development and a mock repository in test.
- In the application supervisor, the Repo is started in non-test environments and skipped in `MIX_ENV=test`.
- Configuration sets `StoreInventory.Repo` in development and `StoreInventory.TestRepo` in test.
- The inventory schema defines `name`, `description`, `price`, and `quantity`, with validations that require all fields and enforce positive `price` and `quantity`.
- The main module uses `Application.get_env(:store_inventory, :repo)` to choose which Repo module to call.
- `insert_item/1` inserts through the configured repo, `all_items/0` fetches all items, and `average_item_price/0` computes the mean price from the returned items.
- The mock repo returns hard-coded items from `all/2` and returns `{:ok, struct(Item, values)}` for valid changesets.
- Invalid changesets are returned as `{:error, changeset}`.
- The tests check invalid insert errors, valid inserts, and the average price from the mocked data.
- The article closes by saying this pattern is useful when tests cannot easily run against a real database, while still recommending Ecto Sandbox for cases where a database is available.
