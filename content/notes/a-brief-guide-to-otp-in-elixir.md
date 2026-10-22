---
title: "A Brief Guide to OTP in Elixir"
date: '2020-10-05T08:43:01-03:00'
category: webclip
summary: 'The article introduces OTP as Elixir’s process-based toolkit, then shows basic processes, receive loops, GenServer callbacks, and a Supervisor for restarting a treasury process.'
tags: ["elixir", "otp", "genserver", "supervisor"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "A Brief Guide to OTP in Elixir"
    url: "https://serokell.io/blog/elixir-otp-guide?utm_source=elixirdigest&utm_medium=email&utm_campaign=275"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-10/serokell-io--a-brief-guide-to-otp-in-elixir.md"
    kind: repo
---

The article explains OTP as the set of Erlang tools and libraries that Elixir inherits, and focuses on the actor model built on lightweight processes. It shows how processes receive messages, keep private state, and can be used to model a simple treasury.

## Reading notes

- OTP is presented as the Erlang toolkit Elixir inherits, especially the actor model based on lightweight processes.
- A process can receive messages, create new processes, send messages, and modify private state.
- A basic process can be spawned with `spawn`, but it ends after completing its work.
- A `receive do` loop can keep a process alive and maintain state while handling `store`, `withdraw`, and `balance` messages.
- The example treasury stores balance in the loop argument and replies with the current balance when asked.
- The article says production code would need more than raw `receive do` loops, such as corner-case handling, tracing, and reporting.
- Behaviours are described as abstract code plus a callback module that supplies the implementation.
- `GenServer` is introduced as a common behaviour for server-like processes.
- The article lists `init`, `handle_cast`, and `handle_call` as the basic callbacks used in the example.
- `init(balance)` starts the server with a state value.
- `handle_cast` is used for asynchronous updates like storing and withdrawing funds.
- `handle_call` is used for synchronous balance queries and returns both a reply and the unchanged state.
- Client functions in the same module wrap the server API with `GenServer.start_link`, `GenServer.cast`, and `GenServer.call`.
- The treasury can be named with its module name when started, which makes later calls simpler.
- A supervisor is introduced as a way to start and shut down applications and restart crashed processes.
- The example supervisor starts the treasury as a child and uses the `:one_for_one` strategy so only the crashed child is restarted.
- The article notes that a supervision tree can include several processes and that state can also be duplicated or persisted to avoid loss on crash.
