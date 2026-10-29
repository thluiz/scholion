---
title: "Introduction to Parallel Computing with Elixir"
date: '2015-06-01T10:07:37-03:00'
category: webclip
summary: 'The article shows how Elixir supports concurrent and parallel computing, then walks through a Fibonacci example that uses tail recursion, spawned processes, message passing, and an escript build.'
tags: ["elixir", "parallel-computing", "concurrency", "escript"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Introduction to Parallel Computing with Elixir - Reactive.TIPS - The Official Blog of Reactive.IO"
    url: "http://www.reactive.io/tips/2015/02/03/introduction-to-parallel-computing-with-elixir/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-06/reactive-io--introduction-to-parallel-computing-with-elixir.md"
    kind: repo
---

Elixir is presented as a language for real-time software because it runs on Erlang’s virtual machine, reuses Erlang libraries, and adds syntax, metaprogramming, and fault-tolerance tools. The post first builds a Fibonacci example with Mix and then turns it into a parallel version using spawned processes and message passing so results can be gathered and ordered.

It also shows how to package the project as an escript by adding a main function and configuring Mix, which makes the tool runnable from the command line without installing Elixir on the target machine.

## Reading notes

- Elixir is described as compiled, built on Erlang’s virtual machine, and able to use Erlang libraries.
- The language is introduced as useful for concurrency, parallel computing, fault tolerance, and real-time software.
- A new Mix project is created with `mix new fibex`.
- A Fibonacci module is implemented using tail recursion, public functions with `def`, private functions with `defp`, and the `|>` operator.
- The sequential version is run from the terminal with `mix run` and returns the expected Fibonacci results.
- The parallel version uses `spawn` to run Fibonacci work in new lightweight processes.
- Message passing is used to return results when they are ready.
- The code carries each input’s index so the results can be sorted after concurrent execution.
- The code also carries the input length and decrements it in the receive loop to know when computation is finished.
- An `escript` is built by adding a `main` function and configuring `mix.exs`.
- The command-line executable is built with `mix escript.build` and run with numeric arguments.
- The summary says the result is a command-line utility that uses multiple CPUs efficiently and points readers to deeper Elixir and Erlang study.
