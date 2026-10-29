---
title: "Elixir in times of microservices"
date: '2015-07-03T15:32:32-03:00'
category: webclip
summary: 'The post argues that Elixir and the Erlang VM already provide the abstractions, process isolation, and communication model needed to manage distributed systems and grow applications without premature microservice splits.'
tags: ["elixir", "microservices", "distributed-systems", "erlang-vm"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Elixir in times of microservices"
    url: "http://blog.plataformatec.com.br/2015/06/elixir-in-times-of-microservices/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-07/blog-plataformatec-com-br--elixir-in-times-of-microservices.md"
    kind: repo
---

Elixir is presented as a language well suited to distributed systems because its runtime was designed for them. The post argues that applications and processes give developers clearer ways to reason about startup, state, crashes, and runtime behavior, even before introducing microservices.

It also explains that communication between nodes is already built in through Distributed Erlang, with location transparency and message passing. For larger systems, umbrella projects let code be split into smaller applications without forcing an immediate move to separate services, so deployment can follow the real need, whether that is complexity, scalability, or multi-tenancy.

## Reading notes

- Elixir runs on the Erlang VM, which was designed in the 1980s for distributed telecommunications systems.
- The post treats premature microservice adoption as a common response to poor code organization.
- Elixir applications start and stop as units, have a unified directory structure, and contain their supervision tree.
- Processes are lightweight, isolated, and communicate through messages.
- Tools like `iex` and `:observer.start()` let developers inspect live applications, memory usage, state, and process trees.
- Applications and processes give a runtime-level way to reason about systems in production.
- Distributed Erlang provides communication and serialization out of the box.
- Two nodes can communicate by naming them and sharing the same secret cookie.
- Location transparency lets processes exchange messages whether they are on the same node or on different nodes.
- The runtime can also communicate with other languages through documented bindings and protocols.
- Large applications can be split into smaller ones by extracting parts of the supervision tree.
- Mix supports umbrella projects, which let multiple applications be compiled, tested, and run together or separately.
- The post says this makes it easier to handle growing code complexity in small steps.
- Microservices are presented as less central than the underlying process and application model.
- Deployment can still vary by need, including separate instances for scalability or multi-tenancy.
- Elixir is also described as useful for long-running systems even when deployed on a single node.
- The language is presented as expressive, and the tooling helps new projects get started.
- The post notes that Distributed Erlang is the most productive option, but other protocols can also be used.
- HTTP and JSON are described as acceptable for cases where they are already the desired choice.
