---
title: "Thoughts About Elixir"
date: '2015-01-28T09:31:37-03:00'
category: webclip
summary: 'The author argues that Elixir is now a viable choice for server software because it keeps Erlang''s runtime and OTP while offering clearer syntax, easier nested data handling, better tooling, documentation, and seamless Erlang interop.'
tags: ["elixir", "erlang", "server-software", "functional-programming"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Thoughts About Elixir | blog.teemu.im"
    url: "http://blog.teemu.im/2015/01/25/thoughts-about-elixir/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-01/blog-teemu-im--thoughts-about-elixir.md"
    kind: repo
---

The author says Elixir has become a serious option for server software now that it reached version 1.0. He values that it runs on the Erlang VM, keeps access to OTP, and makes everyday programming easier through Ruby-like syntax, better tools, documentation, and simple Erlang interop.

## Reading notes

- Elixir runs on the Erlang VM and can use OTP, so the author sees it as a practical server-language choice.
- The syntax feels close to Ruby, which he finds increasingly pleasant, even though he still likes Erlang's recursive pattern-matching style better.
- Elixir makes nested data access and updates easier with keyword lists, `put_in`, and `get_in`.
- The pipe operator makes chained data processing more readable than the equivalent Erlang code.
- `mix` is presented as a strong built-in tool for bootstrapping, testing, packaging, and dependency handling, though releases need `exrm`.
- Documentation is described as easy to reach from the website and from `iex`.
- Erlang code can be called directly from Elixir, with attention to the difference between Elixir binaries and Erlang char lists.
- The author closes by saying his team is building a server in Elixir at Ministry of Games while still relying on Erlang libraries like ranch and locker.
