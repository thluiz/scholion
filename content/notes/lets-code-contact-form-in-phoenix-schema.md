---
title: "Let's Code: Contact Form in Phoenix -- The Schema"
date: '2020-07-05T14:11:15+00:00'
category: webclip
summary: 'The post builds a Phoenix contact form message as a typespec and embedded Ecto schema, then adds a changeset that casts fields, requires them, and validates the email format.'
tags: ["phoenix", "ecto", "changeset", "embedded-schema"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Let's Code: Contact Form in Phoenix -- The Schema"
    url: "https://zachporter.dev/posts/lets-code-contact-form-in-phoenix-part-one"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/zachporter-dev--lets-code-contact-form-in-phoenix-schema.md"
    kind: repo
---

The post walks through the schema used to model a contact form message in a Phoenix 1.4 app. It starts from a typespec, then uses an embedded Ecto schema so the message can be validated and shaped without being stored in the database.

## Reading notes

- It models a support message with email, subject, and body fields inside a Support context.
- The module begins with `@moduledoc false` because it is meant to stay internal to the application.
- The initial `@type t` documents the structure, but the module still needs a schema to compile.
- `embedded_schema` is used because the message is not intended to be persisted anywhere.
- The schema defines `email`, `subject`, and `body` as string fields.
- The author stubs tests first, with cases for valid fields, missing required fields, and invalid email format.
- The first changeset step uses `cast` to allow only `email`, `subject`, and `body` from the input map.
- `validate_required` makes all three fields mandatory.
- `validate_format` checks that the email matches a simple pattern.
- The final result is a `Message` module with an embedded schema and a changeset function that casts, requires, and validates the fields.
