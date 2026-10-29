---
title: "Writing extensible Elixir with Behaviours"
date: '2016-04-17T17:11:33-03:00'
category: webclip
summary: 'The post explains Elixir Behaviours as explicit public contracts for interchangeable modules, then shows how Swoosh uses them to support multiple email adapters and flexible configuration.'
tags: ["elixir", "behaviours", "adapter-pattern", "swoosh"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Writing extensible Elixir with Behaviours"
    url: "https://www.djm.org.uk/posts/writing-extensible-elixir-with-behaviours-adapters-pluggable-backends/?utm_campaign=elixir_radar_45&utm_medium=email&utm_source=RD+Station"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-04/djm-org-uk--writing-extensible-elixir-with-behaviours.md"
    kind: repo
---

The post presents Behaviours as Elixir’s way to define a common abstraction for modules that achieve the same result in different ways. That lets calling code depend on the shared interface while specific implementations can be swapped without changing the rest of the codebase.

## Reading notes

- A Behaviour is defined as a module with `@callback` specs that adopters must implement.
- Modules that adopt a Behaviour must declare `@behaviour SomeModule`, which lets the compiler warn when they do not match the contract.
- The article uses email delivery, document parsing, and storage engines as examples of problems where interchangeable implementations are useful.
- Swoosh’s `Swoosh.Adapter` defines a delivery contract around `deliver/2`, returning an ok/error tuple.
- An adapter such as `Swoosh.Adapters.Local` adopts the Behaviour and implements the required function, while other module functions may exist as well.
- One way to use a Behaviour is dependency injection through a function argument, with a default parser and an optional parser override.
- Another way is to read the adapter from Mix configuration, so the chosen implementation can vary by environment.
- Swoosh combines both approaches by using a wrapper module with `use Swoosh.Mailer` and configuring the adapter in the application config.
- The article also points to Plug and Ecto as existing examples of Behaviours in the wild.
- The main benefit is loosely coupled code with an explicit contract that is easier to extend and test.
- A limitation is that shared contracts can force implementations toward the lowest common denominator when backends differ in capability.
