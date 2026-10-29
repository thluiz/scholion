---
title: "The UNIX Philosophy and Elixir as an Alternative to Go"
date: '2015-10-20T07:45:34-03:00'
category: webclip
summary: 'The post argues that Go is simple but awkward for web apps, while Elixir fits modern web development better because of its concurrency model, small core, and support for APIs that turn Postgres data into JSON.'
tags: ["elixir", "go", "web-development", "unix-philosophy"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The UNIX Philosophy and Elixir as an Alternative to Go"
    url: "http://lebo.io/2015/06/22/the-unix-philosophy-and-elixir-as-an-alternative-to-go.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-10/lebo-io--the-unix-philosophy-and-elixir-as-an-alternative-to-go.md"
    kind: repo
---

The post compares languages for modern web work and argues that Go is simple and useful, but often awkward for building web apps. It says JavaScript still has limits for CPU-heavy work, and that Elixir is a better fit because it is small, modern, and built on BEAM with strong concurrency.

## Reading notes

- The old request-response model is less dominant, but many frameworks and languages still fit it poorly for modern JSON-focused servers.
- JavaScript is presented as acceptable and fast enough, but syntactically noisy and growing larger through standardization.
- Go is valued for concurrency, speed, binaries, and simplicity, yet the post says web app work in Go becomes verbose and less pleasant.
- The author argues that Go makes more sense for Docker, small command-line tools, and foundational systems work than for web apps.
- Elixir is described as a Ruby-like syntax that runs on BEAM and inherits Erlang’s lightweight processes and concurrency.
- Elixir’s functional style, immutability, pattern matching, and macros are presented as features that keep the language small while still flexible.
- The post favors a polyglot future and says Elixir with Phoenix and Ecto is a strong tool for web development.
- The final claim is that if Elixir mainly connects to Postgres and turns data into JSON, that already matches the UNIX philosophy.
