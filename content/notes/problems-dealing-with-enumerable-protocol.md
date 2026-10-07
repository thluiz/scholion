---
title: "Problems dealing with Enumerable protocol"
date: '2015-05-25T09:20:58-03:00'
category: webclip
summary: 'The thread says Enum.take and Enum.at still reduce the whole collection, so a Redis-backed API should expose explicit limit and offset. José Valim distinguishes database and in-memory behavior and suggests count and member? stay explicit too.'
tags: ["elixir", "enumerable-protocol", "stream", "redis"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "[elixir-talk:8485] Problems dealing with Enumerable protocol - th.luiz@gmail.com - Gmail"
    url: "https://mail.google.com/mail/u/0/?pli=1#label/Listas%2F05+-+Principais/14d5d816ae28e97f"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/mail-google-com--problems-dealing-with-enumerable-protocol.md"
    kind: repo
---

The discussion is about a Redis-backed Elixir library whose queries can be chained and then treated as Enumerable. The author wants Enum.take and Enum.at to pass useful information to Redis so only the needed items are fetched, but the replies say the API should expose limit and offset directly instead of relying on Enum to do that work.

José Valim says the distinction between database and in-memory or stream operations matters because of performance and latency, and he also says count and member? should be explicit. Booker Bense suggests using a Stream if short-circuiting is the goal, and Peter Hamilton recommends providing semantically similar Red functions such as take and at.

## Reading notes

- The library builds Redis queries that can be chained before fetching happens.
- The author wants Enum.take and Enum.at to use the requested position or count when talking to Redis.
- José Valim says explicit limit and offset are the correct approach.
- He separates database behavior from in-memory and stream behavior because their performance and latency differ.
- He says count and member? should also be explicit.
- Booker Bense says short-circuiting via Enum.take requires a Stream rather than an Enumerable.
- He suggests Stream.resource for wrapping the Redis lookup.
- Peter Hamilton suggests Red should provide functions like take and at with similar results but different execution properties.
- José Valim later says laziness is a property of the module chosen, not of the collection itself.
