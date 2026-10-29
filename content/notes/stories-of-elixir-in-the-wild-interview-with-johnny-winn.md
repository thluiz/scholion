---
title: "Stories of Elixir in the Wild: Interview with Johnny Winn"
date: '2015-07-09T15:12:43-03:00'
category: webclip
summary: 'Interview with Johnny Winn about his Elixir projects, a company move toward microservices, what he values in Elixir, the main difficulty he hit, and resources he recommends.'
tags: ["elixir", "microservices", "functional-programming", "interview"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Stories of Elixir in the Wild: Interview with Johnny Winn"
    url: "http://blog.jordan-dimov.com/stories-of-elixir-in-the-wild-interview-with-johnny-winn/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-07/blog-jordan-dimov-com--stories-of-elixir-in-the-wild-interview-with-johnny-winn.md"
    kind: repo
---

Johnny Winn says his open-source Elixir projects grew from learning the language and from missing Ruby features. He describes chronos as a time-formatting library for working with datetimes, inflex as a pluralize/singularize library that was once used in Phoenix, and calliope as a Haml parser that he is overhauling with Elixir's AST.

He also says his company is moving a monolithic Rails application toward microservices and that smaller parts can be written and tested with Elixir. He values Elixir for its simplicity, pattern matching, recursion, and ability to express intent without losing performance. The hardest part for him was immutability, and he would like hot-swapping code changes while debugging. He recommends Functional Programming for the Object-Oriented Developer and Learn You Some Erlang For Great Good.

## Reading notes

- His Elixir projects were part of learning the language and replacing Ruby functionality he missed.
- Chronos was built because working with datetimes as tuples was tedious, and he wanted helpers for testing.
- Inflex started as a small pluralize/singularize library, then gained parameterization and camel casing support.
- Calliope is his largest project, a Haml parser requested by a designer he had worked with.
- He is rewriting Calliope to move away from regular expressions and use Elixir's AST format.
- He sees the move from a Rails monolith to services and microservices as a chance to add Elixir.
- He expects smaller Elixir segments to be written and tested more easily than their Ruby counterparts.
- He describes Elixir as simple, powerful, and good at expressing intent without hurting performance.
- Pattern matching and recursion are the features he misses most when he returns to Ruby.
- His biggest struggle was immutability, especially when passing conn to a function that expected it to be updated.
- He would like the ability to hot-swap code changes while debugging.
- He recommends Functional Programming for the Object-Oriented Developer for people coming from OO backgrounds.
- He also recommends Learn You Some Erlang For Great Good as a useful Erlang resource.
