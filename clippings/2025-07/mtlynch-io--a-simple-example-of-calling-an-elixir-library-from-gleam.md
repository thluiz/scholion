---
url: "https://mtlynch.io/notes/gleam-call-elixir/"
captured_at: "2025-07-17T13:30:40+01:00"
title: "A Simple Example of Calling an Elixir Library from Gleam · mtlynch.io"
domain: "mtlynch-io"
---

I've been experimenting a bit with Gleam and Elixir lately as part of my search for a new programming language.

One of Gleam's flagship features is that it can call Elixir code and libraries, but I couldn't find any examples of how to do that. I wrote a simple example of calling an Elixir library from a Gleam project, based on my beginner's understanding of the Gleam/Elixir/Erlang ecosystem.

## Install dependencies

For this example, I'm using

- Gleam 1.10.0
- Erlang 27.3.4
- Elixir 1.18.3

You can install these dependencies however you want. I use Nix to manage my dependencies, so I install everything by creating a flake.nix.

If I run `nix develop`, I see that erlang and Gleam are available in my shell.

## Create the project

I create a project using `gleam new`. I'm hosting the project outside of Github, so I add `--skip-github` to skip the Github-specific files Gleam adds by default.

## Sidequest: Working around a Gleam package bug

From here, I try to run the boilerplate code that `gleam new` generated for me, but it fails. The issue is that `gleam new` added `gleeunit` 1.4.0 as a dependency, but that package depends on Gleam 1.11.0, which is newer than my local version of Gleam (1.10.0).

Someone else ran into this same issue and filed a bug on Github just an hour before I hit this.

I can work around this by forcing Gleam to downgrade to gleeunit 1.3.1. And then `gleam run` and `gleam test` work as expected.

## Install an Elixir package

I want to pick a package that has simple semantics, so how about a CSV library?

The hex package manager shows that the most popular CSV package is called CSV, so I install that.

Sidenote: There's a Gleam-native CSV library called gsv, but I'm using an Elixir library instead so I can practice calling a non-Gleam library.

## Testing the CSV package with Elixir

First, I need to understand how to call the CSV package APIs at all, and then I can write an Elixir wrapper for the APIs I need.

I want to call the `CSV.encode` function, which has this signature: `@spec encode(Enumerable.t(), [encode_options()]) :: Enumerable.t()`

So, `encode` has two parameters: an object that implements the `Enumerable` protocol, and an optional `encode_options()` type. It returns an object that implements the `Enumerable` protocol.

I don't know Elixir, so I start `iex`, the interactive Elixir shell, to understand the semantics. Then, I install the CSV package within `iex` with `Mix.install([:csv])`.

Now, I try one of the examples from the CSV package documentation: `[~w(a b), ~w(c d)] |> CSV.encode |> Enum.take(2)` returns `["a,b\r\n", "c,d\r\n"]`.

I don't understand Elixir's sigil syntax yet, and I don't like examples with "a" and "b", so here's a rewrite that feels more intuitive to me: `CSV.encode([["movie", "rating"], ["The Godfather", 10], ["Gigli", 2]]) |> Enum.to_list() |> IO.puts()` prints the movie/rating rows as CSV lines.

Okay, so it looks like `CSV.encode` takes in a list of list of strings and returns an `Enumerable` of strings.

## Create a Gleam wrapper for the Elixir package

Now that I understand the semantics of `CSV.encode`, I need to write a wrapper function to call it from Gleam.

The main challenge of writing a Gleam wrapper for an Elixir function is that the two languages don't have matching types. Gleam uses more strict static typing, whereas Elixir uses more flexible dynamic typing.

### Wrapping CSV.encode

It doesn't look like the Gleam standard library has any equivalent of Elixir's `Enumerable`, so I need to use another Elixir API to convert from `Enumerable` to something Gleam understands.

`Enum.to_list` seems like the best option, as it returns an Elixir built-in `list` type, and Gleam has an equivalent `List` type.

So, first, I'll define a Gleam wrapper function for the Elixir `CSV.encode` API using a custom Gleam type `ElixirEnumerable` and the `@external(erlang, "Elixir.CSV", "encode")` attribute.

The `@external` attribute allows me to call Elixir code from Gleam. Gleam, Elixir, and Erlang all can compile to bytecode that runs on the BEAM virtual machine. Within BEAM, the `CSV.encode` function appears under the namespace `Elixir.CSV`, so that's why I need to specify `Elixir` in the `@external` attribute.

I define the input paramater as a Gleam list of list of strings (`List(List(String))`), which is compatible with Erlang's `Enumerable` type.

`CSV.encode` returns an Elixir `Enumerable`, but I don't know a Gleam equivalent to that, so I define a custom type of `ElixirEnumerable`.

Gleam code can't do anything with `ElixirEnumerable` because it doesn't have any data that Gleam knows how to access natively, so I need a way to convert `ElixirEnumerable` to a Gleam-native type.

### Converting an Elixir Enumerable to a Gleam List

To convert from Elixir's `Enumerable` type to a Gleam `List`, I declare another external function for converting the result, using Elixir's `Enum.to_list` function to convert the `ElixirEnumerable` to an Elixir List type, which seems to match the Gleam `List` type.

### Creating a Gleam-friendly wrapper

Now that I've written functions that can wrap the Elixir APIs I want, it's time to tie it all together with a function I'll expose to my Gleam app from this module: `pub fn encode(data: List(List(String))) -> List(String) { data |> csv_encode |> enum_to_list }`

The function is simple. It takes data in the form of a list of list of strings, then uses the Gleam pipe operator to pass it to `csv_encode`, then uses the pipe operator again to convert the result to a Gleam-compatible list of strings.

This is the only function in my `csv` module that I declare as public, as the other wrappers are too low-level to be useful to Gleam clients of this module.

## Calling my wrapper function

Now that I have a Gleam-native wrapper for the `CSV.encode` function, I can write a simple Gleam app to call my wrapper, passing in a list of book titles, authors and release years, piping through `csv.encode()`, `string.concat()`, and `io.print()`.

Running it prints the CSV rows to the console.

It works! I successfully called the Elixir CSV library from my simple Gleam application.

## Source code

The full source of this example is available at https://codeberg.org/mtlynch/gleam-call-elixir-simple

Thanks to Louis Pilford and DisguisedPigeon for their helpful feedback on this post.
