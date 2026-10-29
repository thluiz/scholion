---
title: "Debugging techniques in Elixir"
date: '2016-04-11T14:21:57-03:00'
category: webclip
summary: 'The post compares simple printing with two Elixir debugging options: IEx.pry/0 for inspecting a running process and :debugger for breakpoints, variable inspection, and step-by-step navigation.'
tags: ["elixir", "debugging", "iex", "erlang-debugger"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Debugging techniques in Elixir"
    url: "http://blog.plataformatec.com.br/2016/04/debugging-techniques-in-elixir-lang/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-04/blog-plataformatec-com-br--debugging-techniques-in-elixir.md"
    kind: repo
---

The post says Elixir debugging can start with printing values, but it also offers two other options: `IEx.pry/0` and `:debugger`. `IEx.pry/0` works inside the caller process, blocks execution, lets you inspect bindings, lexical information, and process information, and can be ended with `respawn`.

`:​debugger` is presented as the option for breakpoints. The post shows how to start the debugger, prepare a module with `:int.ni(Example)`, set a breakpoint with `:int.break(Example, 3)`, and then inspect the paused process in the GUI. It also notes a troubleshooting case where `:int.ni(Example)` can fail with an invalid beam file error on older Erlang versions, and suggests updating `int.erl` manually.

## Reading notes

- Elixir debugging can begin with `IO.puts/2` and `IO.inspect/2`, but the post focuses on `IEx.pry/0` and `:debugger` as additional options.
- `IEx.pry/0` runs in the caller process, blocks it, and gives access to bindings, lexical information, and process information.
- `IEx.pry/0` is described as useful for non-production debugging, even though it is not a traditional step-through debugger.
- The `respawn` command ends a pry session and opens a new IEx shell.
- `:debugger` is the Erlang module used when a breakpoint feature is needed.
- The example uses `:debugger.start()`, `:int.ni(Example)`, and `:int.break(Example, 3)` before calling `Example.double_sum/2`.
- After the breakpoint is hit, the process appears in the debugger with break status, and the monitor window can be used to inspect code, variables, and step through execution.
- The post mentions a problem with `:int.ni(Example)` on older Erlang versions and points to manually updating `int.erl` as a workaround.
- The article ends by saying the next post will cover a tracing technique that does not block the caller process.
