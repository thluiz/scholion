---
title: "A sneak peek at Ecto 3.0: breaking changes"
date: '2026-11-16T20:07:59+00:00'
category: webclip
summary: 'Overview of the main breaking changes in Ecto 3.0: repo split into ecto and ecto_sql, switch to Elixir calendar types, and new JSON handling via adapters.'
tags: ["ecto", "elixir", "breaking-changes", "ecto-3-0"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "A sneak peek at Ecto 3.0: breaking changes « Plataformatec Blog"
    url: "http://blog.plataformatec.com.br/2018/10/a-sneak-peek-at-ecto-3-0-breaking-changes/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/blog-plataformatec-com-br--ecto-3-0-breaking-changes-overview.md"
    kind: repo
---

This post introduces a blog series about Ecto 3.0 and focuses on the user-facing breaking changes. It explains the split of Ecto into `ecto` and `ecto_sql`, the removal of deprecated Ecto date/time types in favor of Elixir’s calendar types, adjustments to microsecond handling, and the shift of JSON library configuration from Ecto to database adapters.

## Reading notes

- The authors have been working on Ecto 3.0 for about three months and will publish a series of posts detailing upcoming features and changes.
- Although 3.0 is a major version, the number of user-visible breaking changes was kept small and concentrated in three areas: repository split, calendar types, and JSON handling.
- Since Ecto 2.0, many teams use Ecto only for data mapping and validation without needing a database, but including Ecto still pulled in SQL-related components some considered unnecessary.
- Ecto 3.0 separates functionality into two repositories: `ecto` for schemas, changesets, queries and repos, and `ecto_sql` for SQL adapters and related features.
- For applications using Ecto with SQL databases, upgrading involves replacing the dependency `{:ecto, "~> 2.2"}` with `{:ecto_sql, "~> 3.0"}`.
- For applications using Ecto only for data manipulation without database access, upgrading generally consists of bumping the Ecto version.
- The previous custom date and time modules `Ecto.Date`, `Ecto.Time` and `Ecto.DateTime` have been removed.
- Developers should now use the Elixir built-in types `Date`, `Time`, `DateTime` and `NaiveDateTime`, which have been the recommended types since Ecto 2.1.
- Microsecond handling has been unified across databases: the types `:time`, `:naive_datetime` and `:utc_datetime` now drop microsecond information.
- New types `:time_usec`, `:naive_datetime_usec` and `:utc_datetime_usec` are available for those who need to preserve microseconds.
- To keep microseconds in migrations, the repo configuration can set `migration_timestamps: [type: :naive_datetime_usec]`.
- Schemas that should store microseconds in timestamps can use `@timestamps_opts [type: :naive_datetime_usec]`.
- Database adapters have been standardized to work with Elixir types and no longer return tuples when executing raw queries.
- In Ecto 3.0, the responsibility for choosing the JSON library moved from Ecto itself to the individual adapters.
- Adapters are expected to default to the `Jason` JSON library.
- Configuring `config :ecto, :json_library, CustomJSONLib` now produces a warning and should be replaced by adapter-specific configuration.
- For PostgreSQL, the JSON library is configured with `config :postgrex, :json_library, CustomJSONLib`.
- For MySQL, the JSON library is configured with `config :mariaex, :json_library, CustomJSONLib`.
- To continue using Poison, developers must set the adapter configuration to use `Poison` as the `:json_library` for Postgres or MySQL.
- The authors recommend migrating to Jason and mention that built-in Poison support will be removed in future 3.x releases.
- With unified data types, the `Ecto.DataType` protocol is no longer needed and has been removed.
- If a codebase implemented `Ecto.DataType`, those implementations can be deleted without affecting behavior.
- `Ecto.Multi.run/5` now receives the repo module where the transaction runs as its first argument.
- Functions passed as `module-function-args` to `Ecto.Multi` need to be updated to accept the repo as their first parameter.
- The authors expect the `Ecto.Multi` change to lead to cleaner, less coupled code.
- Prefix support (called schemas in PostgreSQL) received major improvements in Ecto 3.0 and will be discussed in later posts.
- Previously, a prefix could only be set for an entire query, but Ecto 3.0 will allow more granular prefix control.
- When using the `@schema_prefix` attribute in a schema, it will now only affect that specific schema instead of the entire query.
- The authors express enthusiasm about Ecto 3.0 and indicate that future posts will cover new features and performance improvements after these breaking changes.
