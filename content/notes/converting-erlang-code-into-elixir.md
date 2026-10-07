---
title: "Converting Erlang code into Elixir"
date: '2015-01-16T20:51:17-03:00'
category: webclip
summary: 'The post shows a simple port of a Cowboy WebSocket example from Erlang to Elixir, with notes on atoms, modules, string differences, and a few details that can break the code.'
tags: ["elixir", "erlang", "cowboy"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Converting Erlang code into Elixir « Plataformatec Blog"
    url: "http://blog.plataformatec.com.br/2014/11/converting-erlang-code-into-elixir/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-01/blog-plataformatec-com-br--converting-erlang-code-into-elixir.md"
    kind: repo
---

The post walks through a direct conversion of a Cowboy WebSocket example from Erlang to Elixir. It focuses on the simplest translation path, not on idiomatic Elixir, and points out places where Erlang syntax and Elixir syntax can look similar but behave differently.

## Reading notes

- Creates a `ws_cowboy` project and says four files need to be changed or added: `mix.exs`, `lib/ws_cowboy.ex`, `lib/ws_handler.ex`, and `lib/ws_supervisor.ex`
- Copies the `priv` directory from the Cowboy example into the project root
- Adds the Cowboy dependency in `mix.exs` and configures the OTP application module as `WsCowboy`
- In `ws_cowboy.ex`, defines the application behaviour, builds Cowboy routes, starts the HTTP server, and starts `WsSupervisor`
- Explains that Erlang module references become `:<module_name>` in Elixir and that lowercase names in Erlang are atoms, so they become atoms with a colon in Elixir
- Notes that Erlang uppercase names are variables, so they are changed to lowercase during conversion
- Warns that a single-quoted `'_'` in Erlang must become `:_` in Elixir, or Cowboy will compile and run but return 400 responses
- Says function calls are transcribed by replacing `:` with `.`
- In `ws_handler.ex`, keeps the WebSocket handler behaviour, upgrades the HTTP request, starts timers, replies to text messages, and ignores other events
- Says Elixir can use normal double-quoted strings and string interpolation where the Erlang version used binary notation
- In `ws_supervisor.ex`, uses `__MODULE__` instead of Erlang `?MODULE`
- Says the server is run with `mix run --no-halt` and viewed at `http://127.0.0.1:8080`
- Concludes that the translation is straightforward but requires attention to small syntax differences, and mentions that idiomatic Elixir would use the Elixir supervisor instead of the Erlang one
