---
title: "The Obligatory “Why Elixir?” Personal Take"
date: '2015-12-09T11:39:59-03:00'
category: webclip
summary: 'The author argues that Elixir is appealing because it exposes Erlang’s fault tolerance, isolation, and concurrency model in a more approachable language, while fitting web development alongside Rails and Phoenix.'
tags: ["elixir", "erlang", "fault-tolerance", "web-development"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Obligatory &quot;Why Elixir?&quot; Personal Take | AkitaOnRails.com"
    url: "http://www.akitaonrails.com/2015/12/01/the-obligatory-why-elixir-personal-take"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-12/akitaonrails-com--the-obligatory-why-elixir-personal-take.md"
    kind: repo
---

The author frames Elixir as a practical way to reach Erlang’s strengths without giving up the comfort of a more modern language. He argues that web developers do not need to choose a single language for every problem, and that Rails plus Phoenix can be a useful combination for normal sites, real-time features, and efficient background work.

## Reading notes

- The author says he focuses on web applications and does not want to treat the move toward Elixir as an exclusive switch away from Ruby.
- He argues that Rails still has a large, mature ecosystem, while Phoenix can be added for WebSockets, real-time notifications, chatting, and more efficient background jobs.
- He compares languages and toolchains across desktop, mobile, games, and tools development, saying different domains require different languages and trade-offs.
- He presents immutability and opaque message passing as key to concurrency, and says Erlang enforces these by default.
- He describes Erlang processes as isolated, communicating only through immutable messages and managed by schedulers.
- He contrasts this with shared state, mutable data, threads, and callback-heavy reactor patterns.
- He treats coroutines, schedulers, and OTP as a better foundation than ad hoc fibers, promises, or futures for highly concurrent systems.
- He argues that dynamic typing gives more flexibility, while static typing and type inference can make hot code swapping harder.
- He says fault tolerance depends on letting bad code fail in isolation, then letting supervisors restart the affected process without corrupting the rest of the system.
- He presents OTP supervision trees, ports, and restart strategies as the core of Erlang’s reliability story.
- He says Erlang is well suited to distributed web systems with heavy concurrency, real-time communication, and throughput.
- He presents Elixir as the missing piece that makes Erlang’s model more comfortable for programmers coming from Ruby, Python, or Groovy.
- He highlights Elixir features such as macros, protocols, a modern standard library, and testable code.
- He says Erlang and Elixir are not the best fit for raw computation, data science, desktop toolkits, or embeddable libraries, where other languages may be better.
