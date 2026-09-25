---
title: "Enhancing Your Elixir Codebase with Gleam"
date: '2025-07-17T14:47:15+01:00'
category: webclip
summary: 'The article shows how to add Gleam to an Elixir/Phoenix project, move core enrollment logic into Gleam, call it from Elixir, and extend the setup to handle a waitlist.'
tags: ["gleam", "elixir", "phoenix", "typed-business-logic"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Enhancing Your Elixir Codebase with Gleam | AppSignal Blog"
    url: "https://blog.appsignal.com/2024/07/23/enhancing-your-elixir-codebase-with-gleam.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-07/blog-appsignal-com--enhancing-your-elixir-codebase-with-gleam.md"
    kind: repo
---

The article explains how Gleam can be added to an Elixir codebase as a typed business-logic layer without rewriting the whole application. It uses a university enrollment example to show the setup, the Gleam domain types, and the boundary between Gleam code and Elixir glue code.

It first implements enrollment checks in Gleam, then calls those functions from Elixir and maps the results back into Elixir idioms. It later extends the model with a waitlist, updates the Gleam types and tests, and then persists the waitlist from Elixir. The article also notes that cancellation and uniqueness are left for further work.

## Reading notes

- Gleam can run on the BEAM and be added to an Elixir codebase as an enhancement without rewriting everything.
- The example project is a Phoenix and Ecto application for managing university course enrollments.
- The business rules include seat limits, a finite waitlist, cancellation that moves the first waitlisted person into a seat, and age limits for some courses.
- `mix_gleam` is used to integrate Gleam into the Elixir project, including `erlc_path`, Gleam dependencies, and a `src` directory.
- The first Gleam version defines `Student`, `Course`, `EnrollmentDecision`, and `RejectionReason` types, then an `enroll` function that checks age before seats.
- Gleeunit tests are written in Gleam, and `gleeunit/should` is introduced to make the output easier to read.
- Elixir calls compiled Gleam modules by prefixing the module name with `:` and passes tuples that Gleam can interpret as its types.
- The Elixir side converts Gleam results back into `{:ok, term()} | {:error, term()}`.
- The waitlist is later modeled as an actual list instead of a number.
- The Gleam `Course` type and enrollment decision type are extended to include waitlist handling.
- Elixir is updated to persist the waitlist when Gleam returns a `:waitlisted` result.
- The article says cancellation and uniqueness handling are still open topics.
- The setup is presented as worthwhile when you want typed modeling, growing business logic, or a strong separation between pure logic and stateful application code.
