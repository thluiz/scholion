---
title: "Deploying Elixir applications with Edeliver"
date: '2026-11-16T03:52:05+00:00'
category: webclip
summary: 'The post explains how Edeliver simplifies Elixir deploys, how its build, staging, and production environments work, and how to add Phoenix asset tasks and environment variables to the release flow.'
tags: ["deployment", "elixir", "phoenix", "config"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Deploying Elixir applications with Edeliver « Plataformatec Blog"
    url: "https://blog.plataformatec.com.br/2016/06/deploying-elixir-applications-with-edeliver"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/blog-plataformatec-com-br--deploying-elixir-applications-with-edeliver.md"
    kind: repo
---

Edeliver is presented as a way to make Elixir release and deploy work more manageable. The post says it builds and deploys through bash scripts, can distribute releases across multiple servers, and can be used with custom hooks for Phoenix asset tasks.

## Reading notes

- Edeliver is introduced as a tool for building and deploying Elixir and Erlang applications and for performing hot-code upgrades.
- The author says the manual deploy process was repetitive, and a simple `script/deploy` using `mix edeliver build release`, `deploy release to production`, `start production`, and `migrate production up` reduced that work.
- Edeliver runs Mix tasks that generate bash instructions; some commands run locally and then send remote instructions through RPC.
- The tool distinguishes build, staging, and production environments.
- The build environment must match the architecture of the server where the release will run, because Exrm builds with local NIFs and cross-compiling can fail.
- To configure environments, the project needs a `.deliver/config` file with build, staging, and production hosts, users, and deploy paths.
- The configuration supports distributing releases across several servers.
- For Phoenix, the post says extra tasks are needed before the release is generated, especially `brunch build --production` and `mix phoenix.digest`.
- These tasks can be added through a hook in `.deliver/config`, such as `pre_erlang_clean_compile`.
- The sample hook installs npm dependencies, builds assets with Brunch, creates `priv/static`, and runs `phoenix.digest` on the build host.
- The post notes that the earlier Exrm approach for environment variables still matters, but `RELX_REPLACE_OS_VARS=true` cannot be set the same way because Edeliver’s start task runs locally.
- One suggested fix is to export `RELX_REPLACE_OS_VARS` in production.
- The conclusion is that Edeliver is an easy-to-use option, but readers should consult its README and docs for implementation details.
