---
url: "https://github.com/joken-elixir/joken"
captured_at: "2026-11-16T03:06:03+00:00"
title: "GitHub - joken-elixir/joken: Elixir JWT library"
domain: "github-com"
---

[![CI](https://github.com/joken-elixir/joken/actions/workflows/ci.yml/badge.svg)](https://github.com/joken-elixir/joken/actions/workflows/ci.yml) [![Module Version](https://camo.githubusercontent.com/cb09578c2a491a0ec67676644aa6a1ad1c51097befd6c7cf9d1108540b9f734a/68747470733a2f2f696d672e736869656c64732e696f2f686578706d2f762f6a6f6b656e2e737667)](https://hex.pm/packages/joken) [![Hex Docs](https://camo.githubusercontent.com/c334fd82259369a9c0198393d1631036b34a1b00f1adb581924eef30718e6ac7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6865782d646f63732d6c69676874677265656e2e737667)](https://hexdocs.pm/joken/) [![Total Download](https://camo.githubusercontent.com/335ae14b0ac5168decb80f786fa1589cd3dd325cf03c3c185bb0039b35941a36/68747470733a2f2f696d672e736869656c64732e696f2f686578706d2f64742f6a6f6b656e2e737667)](https://hex.pm/packages/joken) [![License](https://camo.githubusercontent.com/17f4b309d784e893fcf7878463ef4965266051f4c6561e347e328dd458e76f5b/68747470733a2f2f696d672e736869656c64732e696f2f686578706d2f6c2f6a6f6b656e2e737667)](https://github.com/joken-elixir/joken/blob/main/LICENSE) [![Last Updated](https://camo.githubusercontent.com/060adadca1c5752b23864c6f8f3adde077372b5133db120d56bc04a0e749dd23/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6173742d636f6d6d69742f6a6f6b656e2d656c697869722f6a6f6b656e2e737667)](https://github.com/joken-elixir/joken/commits/main)

A JSON Web Token (JWT) Library.

Please, do read our comprehensive documentation and guides:

*   [Changelog](https://hexdocs.pm/joken/changelog.html)
*   [Joken Overview](https://hexdocs.pm/joken/introduction.html)
*   [Configuration](https://hexdocs.pm/joken/configuration.html)
*   [Signers](https://hexdocs.pm/joken/signers.html)
*   [Asymmetric cryptography signers](https://hexdocs.pm/joken/asymmetric_cryptography_signers.html)
*   [Testing your app with Joken](https://hexdocs.pm/joken/testing.html)
*   [JWT Common use cases](https://hexdocs.pm/joken/common_use_cases.html)
*   [Migrating from Joken 1.0](https://hexdocs.pm/joken/migration_from_1.html)
*   [Custom header arguments](https://hexdocs.pm/joken/custom_header_arguments.html)

## Usage

[](#usage)

Add `:joken` to your list of dependencies in `mix.exs`:

def deps do
  \# .. other deps
  {:joken, "~> 2.8"},
  \# Recommended JSON library
  {:jason, "~> 1.4"}
end

All set! (don't forget to take a look at our comprehensive [documentation and guides](https://hexdocs.pm/joken/introduction.html)!)

## Benchmarking

[](#benchmarking)

Just run the benchmark script based on the supported algorithm:

mix run benchmarks/hs\_benchmark.exs
mix run benchmarks/jose\_hs\_benchmark.exs
mix run benchmarks/pem\_rs\_benchmark.exs
mix run benchmarks/rs\_benchmark.exs

## License

[](#license)

Copyright (c) 2014 Bryan Joseph & Victor Nascimento

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at [http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

## Disclaimer

[](#disclaimer)

This library would not be possible without the work of @potatosalad (Andrew Bennet). Specifically his library [erlang-jose](https://github.com/potatosalad/erlang-jose/).
