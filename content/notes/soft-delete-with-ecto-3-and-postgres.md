---
title: "Soft delete with Ecto 3 and Postgres"
date: '2026-11-17T15:01:31+00:00'
category: webclip
summary: 'Article describes a soft delete strategy for Ecto 3 with Postgres using a deleted_at field, Postgres schemas, views, triggers, and a custom Repo.hard_delete to keep normal Ecto usage mostly unchanged.'
tags: ["elixir", "ecto", "postgres", "soft-delete"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Soft delete with Ecto 3 and Postgres"
    url: "https://devonestes.com/soft-delete-with-ecto-3-and-postgres"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devonestes-com--soft-delete-with-ecto-3-and-postgres.md"
    kind: repo
---

The text presents a way to implement soft deletes in applications using Ecto 3 with Postgres. Records get a `deleted_at` timestamp instead of being removed, with normal queries seeing only non-deleted rows while special queries and a hard delete path can access or permanently remove all data. The approach relies on Postgres schemas, triggers, views, and minimal changes to Ecto schemas and the Repo.

## Reading notes

- Soft delete is defined as keeping records in the database while hiding them from the application rather than removing them outright.
- The chosen approach adds a `deleted_at` column to each table; null means active, a timestamp means soft deleted.
- The application is configured so default operations see only non-deleted records, but it remains possible to query all records or perform hard deletes that fully remove rows.
- The term "schema" refers both to Postgres schemas (namespaces like `public` or a custom `filtered`) and to Ecto schemas (modules using `Ecto.Schema`).
- Postgres schemas act as namespaces for relations, letting code refer to tables like `public.users` or `filtered.users`.
- Ecto schemas are modules that `use Ecto.Schema`, and the text distinguishes them from Postgres schemas to avoid confusion.
- Tests exercise a `SoftDelete.Users` module whose public API resembles standard CRUD, plus soft-delete-specific functions such as `list_deleted_users`, `get_deleted_user`, `undelete_user`, and `hard_delete_user`.
- The `delete_user` function differs slightly from a typical implementation because, on success, it must look up and return another record rather than the one directly deleted.
- Functions that work with soft deleted users use the `prefix` option in `Ecto.Query.from/2`, which selects the Postgres schema where the query runs.
- Using `prefix` allows `list_deleted_users` to retrieve data from `public.users`, where all users (including soft deleted ones) live.
- The Ecto schema for `User` defines fields and changesets like a normal app, but instead of `use Ecto.Schema` it uses `use SoftDelete.Schema`.
- `SoftDelete.Schema` sets `@schema_prefix` to `"filtered"`, so Ecto operates against `filtered.users` by default rather than `public.users`.
- With `@schema_prefix` set, `filtered.users` holds users that are not soft deleted, while `public.users` contains every user, including soft deleted ones.
- The migration that creates the `users` table looks like a normal `create table(:users)` call, but also executes custom SQL via `prepare_table_for_soft_delete('users')` on `up` and `reverse_table_soft_delete('users')` on `down`.
- An earlier migration sets up support for soft delete, including creation of the `filtered` Postgres schema and trigger functions.
- The migration uses `CREATE SCHEMA filtered` to create a separate Postgres schema where filtered views will live.
- A trigger is defined that, after a row is deleted, reinserts it into the original table with `deleted_at` set to the current timestamp so deletes become soft deletes.
- The trigger is configured as an `AFTER DELETE` trigger for specific technical reasons, though those details are not elaborated in the text.
- The `prepare_table_for_soft_delete` function takes a table name and adds a `deleted_at` column to that table.
- It also creates an index on `deleted_at` because it will be heavily used in queries filtering by soft delete status.
- The function activates the previously defined trigger on the target table so that delete operations become soft deletes.
- It creates a Postgres view in the `filtered` schema with the same name as the table that only exposes rows where `deleted_at` is null.
- Once `prepare_table_for_soft_delete` has been run, a table is ready for use with soft delete in the application.
- A companion function, `reverse_table_soft_delete`, is provided to undo the changes made by `prepare_table_for_soft_delete`, reversing those four steps.
- Hard deletes are implemented via a `hard_delete` function added to the Repo module.
- The Repo remains mostly standard, with `hard_delete` being the main addition and following typical patterns for Ecto code.
- `hard_delete/1` uses `Ecto.Multi`, first disabling the soft delete trigger in the current transaction so that a real delete occurs.
- After disabling the trigger, it deletes the record normally, then re-enables the trigger so future deletes revert to soft delete behavior.
- Trigger disabling happens only within the transaction scope, which avoids global state issues and race conditions that might accidentally hard delete rows.
- The author characterizes this soft delete approach as minimally invasive to normal Ecto behavior and visible only in a few focused places.
- The method is said to rely on a small amount of custom SQL, but not extensive or hacky changes.
- The article notes there are performance tradeoffs with soft delete, though the implementation should add only a millisecond or two to most operations.
- If performance becomes problematic, the author suggests that the approach can be refined and optimized in various ways without detailing them.
