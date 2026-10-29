---
title: "Mocks and explicit contracts"
date: '2016-01-02T13:57:17-03:00'
category: webclip
summary: 'The post argues that mocks are useful, but only when they replace a real dependency through an explicit contract. That keeps tests isolated, makes boundaries visible, and avoids coupling to implementation details.'
tags: ["mocks", "testing", "contracts", "elixir"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Mocks and explicit contracts"
    url: "http://blog.plataformatec.com.br/2015/10/mocks-and-explicit-contracts/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-01/blog-plataformatec-com-br--mocks-and-explicit-contracts.md"
    kind: repo
---

The post argues that mocks are useful, but they should be treated as replacements for a real dependency, not as a way to alter existing modules globally. For external APIs, the better approach is to depend on an explicit contract and swap implementations by environment, which keeps application tests isolated from the HTTP client and the external service.

## Reading notes

- Mocks are simulated entities that mimic real ones in controlled ways, and the author treats “mock” as a noun rather than a verb.
- Mocking the underlying HTTP client couples tests to that client’s mechanics, so changing the client can break tests even when application behavior stays the same.
- In Elixir, the Twitter client can be configured per environment, with a sandbox in development, an in-memory implementation in tests, and the HTTP client in production.
- The in-memory implementation is itself a mock, but it is created as a separate module instead of replacing a global dependency.
- Explicit contracts matter because a mock only works well when the behavior of the real component is defined in advance.
- Elixir behaviours make those contracts explicit through callback functions, and modules that implement them can declare `@behaviour`.
- The post says boundaries should be chosen carefully: too many isolated boundaries can make tests brittle, while too few can make suites slow and hard to debug.
- For the HTTP implementation, the author prefers tests that reach the Twitter API directly and are tagged so they can be excluded by default and run when needed.
- If direct API tests are impractical because of rate limiting or similar constraints, a mock HTTP client can still be used as long as it does not break the earlier contract boundaries.
- Another option is to run a dummy webserver that emulates the Twitter API, such as Bypass.
- The article rejects the idea that this is about making code merely “testable”; the deeper point is to improve design and decouple complex parts of the system.
- Passing a dependency as an argument is presented as a simpler alternative when the dependency surface is small.
- An anonymous function can be passed for a tiny dependency, or a module can be passed when a contract is useful.
- A protocol is mentioned as another way to define a contract for a data-structured dependency.
- The author recommends passing dependencies directly when possible, and using application configuration as a fallback.
- The noun-versus-verb distinction is central: create a mock object or module, but do not mock an existing module in place.
- Mock libraries are acceptable when they help define mock objects passed into tests, but they are a problem when they encourage global replacement or other anti-patterns.
- Defining contracts helps expose complexity in dependencies, makes new required functions visible, and isolates interactions between complex components.
