---
title: "(Ab)using Ecto as Elixir data casting and validation library"
date: '2026-11-16T04:14:20+00:00'
category: webclip
summary: 'The article shows how to use Ecto changesets outside database-backed models to cast user input, validate it, and return either an action-ready changeset or typed data for service modules and forms.'
tags: ["ecto", "changesets", "validation", "elixir"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "(Ab)using Ecto as Elixir data casting and validation library"
    url: "https://amberbit.com/blog/2017/12/27/ecto-as-elixir-data-casting-and-validation-library"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/amberbit-com--abusing-ecto-as-elixir-data-casting-and-validation-library.md"
    kind: repo
---

The article argues that Ecto can be used as a general-purpose casting and validation layer, not only as a database access library. It starts from the usual schema-backed pattern, then shifts to tableless forms and service modules that accept user input, validate it, and either return errors or proceed with business logic.

## Reading notes

- Ecto changesets can be used without `Ecto.Schema`, so casting and validations are available for use cases beyond database tables.
- A changeset represents the changes made from submitted params against an existing struct, and it only tracks fields that were actually changed.
- In a schema-backed example, `App.User.changeset/2` casts `full_name` and `email`, validates required fields, and returns a changeset that can be inserted or updated through `Repo`.
- Validation errors are not rendered automatically unless the changeset has an `action` set, which can happen through `Repo.insert`, `Repo.update`, or `apply_action/2`.
- For a contact form, the controller can call a custom service module instead of `Repo.insert`, and the service returns `:ok` on success or `{:error, changeset}` on failure.
- The service module casts params against a schema map, validates required fields and checkbox acceptance, and uses `apply_action(:insert)` to turn valid params into typed data.
- The form template uses Phoenix form helpers with the changeset so it can show field errors when required values are missing.
- An update shows how `embedded_schema` can replace the earlier tableless pattern.
- The article ends by extracting the shared casting and validation behavior into an `App.Service` macro so individual services only define schema, validations, and business logic.
