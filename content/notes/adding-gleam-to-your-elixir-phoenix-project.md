---
title: "Adding Gleam to your Elixir project"
date: '2026-11-16T20:09:00+00:00'
category: webclip
summary: 'Step‑by‑step guide to integrating a Gleam (rebar3) app into a Phoenix umbrella, wiring Mix to compile it, avoiding umbrella warnings, and calling Gleam from Elixir.'
tags: ["elixir", "gleam", "phoenix", "beam"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Adding Gleam to your Elixir project"
    url: "https://devonestes.com/adding-gleam-to-your-elixir-project"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devonestes-com--adding-gleam-to-your-elixir-phoenix-project.md"
    kind: repo
---

The page explains how to integrate Gleam, a strongly typed BEAM language built with rebar3, into an Elixir project by using a Phoenix umbrella. It walks through creating an umbrella app, replacing one Mix app with a Gleam app, configuring Mix to compile it via rebar3, fixing umbrella warnings by explicitly listing apps, and finally calling a Gleam function from a Phoenix controller. It also notes how to run tests for both Mix and rebar3 projects with a single shell command.

## Reading notes

- Gleam is a new BEAM language focused on strong type safety and is described as worth experimenting with.
- Gleam compiles to Erlang and uses rebar3 as its build tool, which Mix can work with without extra tooling.
- The setup uses a Phoenix umbrella application, where one app is Elixir and the other is Gleam.
- A new Phoenix umbrella app is generated with `mix phx.new --umbrella gleam_example`.
- The generated `apps/gleam_example` Mix app is removed so that a fresh Gleam application can be created in its place.
- Gleam and rebar3 should be installed, and `asdf` is suggested as an easy way to install them.
- A new Gleam application is created with `gleam new gleam_example`, which generates a standard Gleam project structure.
- After creating the Gleam app, you can change into its directory and run tests using `rebar3 eunit` to confirm the setup works.
- To connect the Gleam app to the umbrella, Mix must be told to use rebar3 for that dependency in `apps/gleam_example_web/mix.exs`.
- In the web app’s `deps` function, the umbrella dependency `{:gleam_example, in_umbrella: true}` is extended with `manager: :rebar3` so Mix compiles it via rebar3.
- Starting the Phoenix server at this point works but triggers a Mix warning that `apps/gleam_example` is a directory without a `mix.exs` file.
- Mix assumes all directories under `apps` are Mix projects because of the `apps_path: "apps"` configuration in the top‑level `mix.exs`.
- To silence the warning, the project configuration is updated to include an explicit `apps: [:gleam_example_web]` key.
- With `apps: [:gleam_example_web]`, Mix compiles only the Elixir web application and ignores the Gleam app as a Mix project.
- After configuration, the server can be started with `mix phx.server` without warnings, while still using the Gleam code.
- The example integrates Gleam into the Phoenix app by calling a Gleam function from `GleamExampleWeb.PageController`.
- The controller’s `index/2` action uses `text(conn, :gleam_example.hello_world())`, showing how a Gleam function compiled to Erlang can be invoked from Elixir.
- This setup results in a Phoenix application that successfully calls Gleam code at runtime.
- Mix does not automatically run tests for rebar3 projects when executing `mix test` in the umbrella.
- To run all tests with one command, the author suggests a shell or Makefile command: `mix test && (cd apps/gleam_example && rebar3 eunit)`.
- The completed example project demonstrating this integration is available on GitHub at `devonestes/gleam_example`.
