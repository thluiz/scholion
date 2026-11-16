---
title: "Deploying with Releases — Phoenix v1.8.16"
date: '2020-07-05T14:10:39+00:00'
category: webclip
summary: 'Explains how to package a Phoenix app as a self-contained release, run migrations and custom commands from the release, build Docker images, and configure clustering.'
tags: ["phoenix", "elixir-releases", "docker", "clustering"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Deploying with Releases — Phoenix v1.8.16"
    url: "https://hexdocs.pm/phoenix/releases.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/hexdocs-pm--deploying-with-releases-phoenix-v1-8-16.md"
    kind: repo
---

The guide shows how to turn a Phoenix application into a self-contained release that can be copied to a production machine. It also covers how to run database migrations and other commands from inside the release, how to build container images from the release artifacts, and how to set up clustering.

## Reading notes

- The goal is to package a Phoenix app with the Erlang VM, Elixir, code, and dependencies in one directory that can be deployed to production.
- To prepare a release, the guide uses environment variables, installs production dependencies, compiles code and assets, and then runs `mix phx.gen.release` followed by `mix release`.
- `phx.gen.release` creates overlay scripts for starting the server and running migrations, plus a `release.ex` file for invoking Ecto migrations without `mix`.
- The generated release can be started, opened remotely, stopped, or inspected through the release’s command scripts.
- For migrations, the guide defines `MyApp.Release.migrate/0` and `rollback/2`, then calls them through the release `eval` command.
- The same pattern can be used for custom production commands, with `load_app` for loading the app and `ensure_all_started` when the command needs the full supervision tree.
- Docker support comes from `mix phx.gen.release --docker`, which generates a Dockerfile that builds the release inside a builder image and copies the result into a smaller runtime image.
- Runtime configuration should be kept in `config/runtime.exs`, especially secrets and environment-specific values, so images stay reusable across environments.
- The clustering section explains two needs for node clustering: node connection and service discovery.
- For DNS-based clustering, the guide suggests configuring ports and node names in `rel/env.sh.eex` and setting `DNS_CLUSTER_QUERY` to find peer instances.
- If DNS discovery is not available, the guide points to `libcluster` and `libcluster_postgres` as alternative discovery mechanisms.
- For `epmd`-less deployment, the guide replaces the default port setup with `rel/vm.args.eex` and `rel/remote.vm.args.eex`, exposing only a fixed distribution port besides HTTP.
