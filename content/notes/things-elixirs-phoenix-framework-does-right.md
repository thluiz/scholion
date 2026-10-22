---
title: "Things Elixir's Phoenix Framework Does Right"
date: '2020-10-05T08:42:59-03:00'
category: webclip
summary: 'The article argues that Phoenix sits near the middle between flexible and strict frameworks, stands out in persistent communication, benefits from BEAM-based concurrency, and handles failures and clusters with built-in supervision.'
tags: ["phoenix-framework", "elixir", "web-frameworks", "concurrency"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Things Elixir's Phoenix Framework Does Right · Scorpil"
    url: "https://scorpil.com/post/things-elixirs-phoenix-framework-does-right/?utm_source=elixirdigest&utm_medium=email&utm_campaign=275"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-10/scorpil-com--things-elixirs-phoenix-framework-does-right.md"
    kind: repo
---

Phoenix is presented as a framework that balances flexibility and strictness. It gives a strong idea of how applications should be structured, but it still lets developers understand and swap out internal pieces. The article also says Phoenix is especially strong when an app needs persistent client-server communication.

## Reading notes

- Phoenix sits close to the middle between DIY frameworks and strict batteries-included ones.
- It is built on Elixir’s functional style, with a clear request context and an MVC-inspired structure.
- It does not hide its internals and encourages developers to learn its conventions.
- It ships with many tools by default, but most of them can be replaced or disabled.
- It works well for classical HTTP, but channels, PubSub, Presence, and LiveView make persistent communication a strong fit.
- Its performance comes mainly from Elixir, Erlang, and the BEAM VM, not only from Phoenix itself.
- Lightweight processes and BEAM scheduling support concurrent work efficiently.
- Elixir is described as fast enough for typical web apps, though not faster than Go or Rust on purely CPU-bound tasks.
- Phoenix handles failures through supervision, so one component can fail without taking down the rest.
- It also assumes multi-node deployment and can communicate over the network in the same style used between processes.
- The article notes drawbacks: Elixir and functional programming are still less mainstream, and some third-party SDKs are missing, such as an official AWS client library.
