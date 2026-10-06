---
title: "An intro to OTP in Elixir"
date: '2015-05-07T13:16:51-03:00'
category: webclip
summary: 'The post explains OTP as Erlang’s development environment for concurrent programming, then builds a FizzBuzz server with GenServer, client APIs, callbacks, caching, and process-based I/O.'
tags: ["elixir", "otp", "genserver", "concurrency"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Oozou Blog - An intro to OTP in Elixir"
    url: "http://blog.oozou.com/an-intro-to-otp-in-elixir/?utm_campaign=Elixir+Radar&utm_source=hs_email&utm_medium=email&utm_content=17534844&_hsenc=p2ANqtz--QoQiBcY8hxtHp3pvhd5ay__j4rIb7R3J5I3BXhOPojC6CerYXava_T3sLO4m9td-lPMY5Y4r-d1gKUh-V_OMdEE2f1A&_hsmi=17534844"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/blog-oozou-com--an-intro-to-otp-in-elixir.md"
    kind: repo
---

The post introduces OTP as the set of Erlang libraries and tools used for concurrent programming, then shows how an Elixir FizzBuzz server can be turned into an OTP app. It focuses on application behaviours, where Elixir supplies default callback implementations and the developer overrides only what is needed.

## Reading notes

- OTP is described as the Open Telecom Platform and as a complete development environment for concurrent programming, with the libraries as the part people usually mean by OTP.
- Erlang/OTP behaviours define generic implementations for common tasks, such as a generic server module.
- Elixir provides default implementations for these callback functions, so only needed ones must be overridden.
- The example starts a new Mix project with a CamelCase module name by passing `--module FizzBuzz`.
- The server implements the `GenServer` behaviour and uses `Logger` for debugging.
- `FizzBuzz.start_link/0` wraps `GenServer.start_link/3` and starts the server as a linked process, often in a supervision tree.
- The module name is used as the server name so other functions do not need to address it by PID.
- `FizzBuzz.get/1` and `FizzBuzz.print/1` form the client API, with `get` using a synchronous call and `print` using an asynchronous cast.
- Wrapping the GenServer interface in client APIs is presented as a common pattern.
- The callbacks `handle_call/2` and `handle_cast/2` pattern match on `{:print, n}` and delegate to `fetch_or_calculate/2`.
- `fetch_or_calculate/2` checks whether the FizzBuzz value was already computed, fetches it from the dictionary if present, or calculates it and stores it in the state.
- The state is a simple Elixir map.
- The complete example is run in `iex -S mix`, and the output shows asynchronous requests interleaving logs, function return values, and `IO.puts` output.
- The post notes that `IO.puts` output appears in the `iex` session because it uses the current group leader.
- Fetching an already computed value returns it from the cache.
- The summary says OTP makes it easy to implement server applications and that the FizzBuzz server can be deployed in a larger Elixir application with supervision and hot code swapping.
