---
title: "Dependency Injection in Elixir"
date: '2020-06-13T17:47:19-03:00'
category: webclip
summary: 'The post compares two ways to apply dependency injection in Elixir: through application config with Application.get_env/3, or by passing collaborators as function parameters, with trade-offs in visibility and flexibility.'
tags: ["elixir", "dependency-injection", "testing", "functional-programming"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Dependency Injection in Elixir"
    url: "https://joebew42.github.io/2020/05/16/dependency-injection-in-elixir/"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-06/joebew42-github-io--dependency-injection-in-elixir.md"
    kind: repo
---

The post explains dependency injection as passing objects or functions to another object or function, then shows how it can be used in Elixir through two approaches. It uses a birthday greetings example with Employees, GreetingMessage, and GreetingMessageSender to show why different collaborators may be swapped.

## Reading notes

- Dependency injection is presented as passing objects or functions to another object or function.
- The birthday greetings example uses Employees, GreetingMessage, and GreetingMessageSender as separate collaborators.
- One option is to read collaborators from Application.get_env/3, which makes it easy to switch configuration by environment.
- The author notes that this approach can reduce visibility in tests because the collaborator lives in configuration files.
- Another option is to pass collaborators as function parameters, making dependencies explicit.
- With function parameters, tests keep collaborators in the same file and need fewer moving parts.
- The downside of the parameter approach is that switching configuration between environments may be less quick.
- The post ends by treating the choice as a trade-off and mentions macros, home-made implementations, and full-fledged frameworks as other possibilities.
