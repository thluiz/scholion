---
title: "Building and configuring a Phoenix app with Umbrella for releasing with Docker"
date: '2020-07-05T14:10:38+00:00'
category: webclip
summary: 'The post walks through creating an Elixir umbrella project with Phoenix and a second app, adding Distillery for releases, wiring runtime environment variables, and packaging everything into a Docker image for production.'
tags: ["elixir", "phoenix", "umbrella-project", "docker"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building and configuring a Phoenix app with Umbrella for releasing with Docker"
    url: "https://cultivatehq.com/posts/elixir-distillery-umbrella-docker"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/cultivatehq-com--building-configuring-phoenix-app-umbrella-docker.md"
    kind: repo
---

The tutorial builds an Elixir umbrella project, adds a Phoenix app and a separate Greeter app, then connects them through umbrella dependencies and a Phoenix channel. It also adds basic_auth to the web app, configures Distillery for releases, and prepares the project for production with runtime environment variables.

It then shows how to containerize the release with Docker, using one image to build the release and another minimal image to run it. The post also introduces vm.args so configuration values can be passed as non-string environment variables at runtime.

## Reading notes

- Umbrella projects split a project into smaller isolated applications, and Mix supports them with the `--umbrella` option.
- Phoenix can be created inside `paraguas/apps` with `mix phx.new phoenix_app --no-ecto`.
- The example adds `basic_auth` to the Phoenix app and configures it differently for development, test, and production.
- The router uses a BasicAuth pipeline before the root route.
- A second app, `greeter`, is created inside the umbrella and added to the Phoenix app with `in_umbrella: true`.
- Distillery is added as a release tool so the project can be deployed independently of dependencies and Erlang or Elixir installations.
- The Phoenix app needs `server`, `root`, and `version` options in production configuration to run inside a Distillery release.
- Static assets must be built and digested before creating the production release.
- The production release expects runtime environment variables such as `PORT`, `COOKIE`, and the BasicAuth settings.
- Docker is used with a builder image and a smaller runtime image to package the release for deployment.
- `vm.args` is introduced so configuration can use `${VAR}` placeholders when a value needs to be treated as something other than a string.
