---
title: "Building a web framework from scratch in Elixir"
date: '2015-12-21T15:29:45-03:00'
category: webclip
summary: 'The article shows how to build a small Sinatra-like web framework in Elixir with Plug, covering requests, routing, macros, templates, Ecto models, testing, and performance.'
tags: ["elixir", "plug", "web-framework", "ecto"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building a web framework from scratch in Elixir"
    url: "https://codewords.recurse.com/issues/five/building-a-web-framework-from-scratch-in-elixir"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-12/codewords-recurse-com--building-a-web-framework-from-scratch-in-elixir.md"
    kind: repo
---

The article walks through building a simple web framework on top of Plug and Cowboy in Elixir. It starts with a basic module that handles requests through init/1 and call/2, then adds response headers, pattern matching on paths and methods, composable plugs, templates, and Ecto-backed user lookup.

## Reading notes

- Plug modules respond to web requests through init/1 and call/2, with init/1 running once at startup and call/2 running for each request.
- The connection object is immutable, so functions like put_resp_header return a modified copy of conn that must be passed along the chain.
- Pattern matching on conn.path_info and method lets one router handle different routes and extract values such as user_id from the URL.
- A macro can wrap the common call logic so routers can share the same routing syntax without repeating code.
- Plugs can be composed, so one plug can call another, which makes it possible to layer routing, logging, authentication, and other behavior.
- EEx templates can render HTML, and templates can be precompiled with EEx.function_from_file to avoid parsing the file on every request.
- Ecto is used to define a User schema, create the users table through a migration, and fetch a record from the database in the user route.
- The example inserts a User record in IEx and then serves the user’s first and last name from the template.
- Testing is done by passing a fake conn to the router’s call function and checking the returned state, status, and response body with ExUnit and Plug.Test.
- The article says routing based on pattern matching is fast because the Erlang VM optimizes it, and it argues that this thin layer over Plug and Cowboy keeps performance high.
- Suggested next steps include organizing code into submodules, adding more macros, and using module reloading tools during development.
