---
title: "Elixir | Why Linked Lists?"
date: '2026-11-16T01:41:16+00:00'
category: webclip
summary: 'The article argues that Elixir uses linked lists because immutability makes array copying costly, while linked lists support recursive structure and structural sharing with low memory overhead.'
tags: ["elixir", "linked-lists", "immutability", "structural-sharing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "[ Elixir | Why Linked Lists? ]"
    url: "https://dev.to/edisonywh/-elixir--why-linked-lists--1e9d"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--elixir-why-linked-lists.md"
    kind: repo
---

The article explains why linked lists fit Elixir’s linear data structure. Its main points are that immutable data makes repeated array copying impractical, that linked lists are recursive by nature, and that tail sharing lets multiple lists reuse the same stored tail.

## Reading notes

- In Elixir and most functional languages, data is immutable, so adding or deleting from an array would require copying the whole array each time.
- With arrays, enforcing true immutability would double memory use when a new version is created, and it also affects time cost.
- Linked lists avoid that constraint because their nodes are stored separately in memory.
- A linked list is recursive by definition, since `A -> B -> C -> D` contains sublists like `B -> C -> D` and `C -> D`.
- The recursive structure and immutability make functional languages rely on recursion.
- Because linked lists cannot change, different lists can share the same tail without redefining the same data.
- In the example `list = [5,6,7,8]`, `list_one = [1 | list]`, and `list_two = [2 | list]`, all three lists share the same tail and differ only in the head pointer.
- The article says this keeps memory cost low while preserving immutability.
- It briefly mentions that linked lists may be good for garbage collection and that tail sharing may help caching, but the author is unsure about those claims.
- The closing note says the topic is really about Erlang and functional programming more broadly, even though Elixir prompted the question.
