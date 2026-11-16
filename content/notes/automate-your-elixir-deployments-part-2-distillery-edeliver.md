---
title: "Automate Your Elixir Deployments - Part 2 - Distillery & eDeliver"
date: '2026-11-16T04:04:15+00:00'
category: webclip
summary: 'The post explains how to build an Elixir release with Distillery and deploy it to production with eDeliver, covering dependencies, production config, release setup, build, and deploy commands.'
tags: ["elixir", "distillery", "edeliver", "deployment"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Automate Your Elixir Deployments - Part 2 - Distillery & eDeliver"
    url: "https://hashrocket.com/blog/posts/automate-your-elixir-deployments-part-2-distillery-edeliver"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/hashrocket-com--automate-your-elixir-deployments-part-2-distillery-edeliver.md"
    kind: repo
---

The post walks through setting up an Elixir release workflow with Distillery and eDeliver. It builds on a previous article about preparing a server with Ansible, and it uses a Phoenix 1.5 app without Ecto as the example project.

## Reading notes

- It starts by adding Distillery and eDeliver to mix.exs and fetching dependencies.
- Production settings load secret_key_base and the port from environment variables in config/prod.secret.exs.
- config/prod.exs is updated with the application URL, static manifest, server startup, code reloader disabled, and origin checks.
- Distillery is initialized with mix distillery.init, then rel/config.exs is changed so the Erlang cookie comes from ERLANG_COOKIE instead of being committed to git.
- eDeliver is configured in .deliver/config with build and production hosts, a deployment path, auto versioning, and callbacks.
- The callbacks symlink prod.secret.exs into the build directory, build static assets on the server, and copy static assets into each release so rollbacks keep them available.
- One callback removes start_erl.data as a workaround for a known Distillery issue.
- The release is built with mix edeliver build release, the generated version is copied from the output, and .deliver/releases is added to .gitignore.
- Deployment uses mix edeliver deploy release to production with the version number, followed by mix edeliver restart production.
- The post says the application should then run on the domain, and it links to the full example repository.
