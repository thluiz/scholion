---
title: "Build and test a blazing fast JSON API with Phoenix, an Elixir framework"
date: '2015-05-07T13:16:46-03:00'
category: webclip
summary: 'The article shows how to build a Phoenix JSON API for contacts, starting with a test, then adding an Ecto model, migration, route, controller, and view until the test passes.'
tags: ["phoenix", "elixir", "ecto", "testing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Build and test a blazing fast JSON API with Phoenix, an Elixir framework"
    url: "https://robots.thoughtbot.com/testing-a-phoenix-elixir-json-api?utm_campaign=Elixir+Radar&utm_source=hs_email&utm_medium=email&utm_content=17534844&_hsenc=p2ANqtz--_LEJbU9r6PN_QggZlPemtrA5uvuSiDn1CHFDBaYTmcGahTVGq3PaQ8592P4uC1_etr4w8Hcl2O-N-b15BNkLwn9M7Iw&_hsmi=17534844"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/robots-thoughtbot-com--build-and-test-a-blazing-fast-json-api-with-phoenix.md"
    kind: repo
---

The post walks through building a JSON API for contacts with Elixir and Phoenix. It starts from a failing test, adds an Ecto model and migration, then wires the route, controller, and view so Phoenix returns JSON and the test passes.

## Reading notes

- Phoenix is presented as an Elixir framework for fast, low-latency web applications, with response times often measured in microseconds.
- The example app is called HelloPhoenix and serves a list of contacts through `/api/contacts`.
- The first step is a controller test that wraps Ecto calls in a transaction so the database stays empty for each test run.
- The test inserts a `Contact`, sends a request, and checks that the response status is 200 and the body matches the encoded JSON.
- Running the test reveals that the `Contact` struct does not exist yet, so the model must be created.
- Ecto is used with Postgres through a repository, and the article says to verify the database settings in `config/dev.exs` and `config/test.exs`.
- The article creates the development and test databases with `mix ecto.create` and `env MIX_ENV=test mix ecto.create`.
- The `Contact` schema defines `name` and `phone`, and the migration creates a `contacts` table with those fields and timestamps.
- The route is added under `/api`, using JSON acceptance and `resources "/contacts", ContactController`.
- The controller fetches all contacts with `Repo.all(Contact)` and renders them with `render conn, contacts: contacts`.
- A `ContactView` defines `render("index.json", %{contacts: contacts})` and returns the contacts array so Phoenix can encode it as JSON.
- The article then moves some shared aliases and test helpers into `HelloPhoenix.ExUnit.CaseTemplate` so tests can reuse them through `HelloPhoenix.Case`.
- It ends by noting that the app can be deployed to Heroku with the Elixir buildpack.
