---
title: "Elixir Streams"
date: '2015-06-09T08:57:09-03:00'
category: webclip
summary: 'The post contrasts eager `Enum` operations with lazy `Stream` operations, then shows how streams handle large or infinite data, file and stdin input, and paginated GitHub API results.'
tags: ["elixir", "streams", "lazy-evaluation", "api-pagination"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Elixir Streams"
    url: "http://blog.drewolson.org/elixir-streams/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-06/blog-drewolson-org--elixir-streams.md"
    kind: repo
---

The post explains that `Enum` performs eager collection operations, while `Stream` describes lazy computations that are only realized when an `Enum` function forces them. It uses ranges, file and stdin streams, and stream constructors such as `repeatedly`, `iterate`, `unfold`, and `resource` to show how lazy composition works on large or infinite data.

## Reading notes

- `Enum` transforms collections immediately, while `Stream` stores future computations.
- Streams still work with `Enum` because they implement `Enumerable`.
- `Enum.to_list` and `Enum.take` force a stream to run.
- A large range can be mapped lazily, and only the requested items are computed.
- Streams can be composed with `filter` and `map` without realizing the whole collection.
- `File.stream!` returns file lines or bytes as a stream.
- `IO.stream` gives the same kind of interface for standard input.
- `GenEvent.stream` creates a stream of events from a `GenEvent` manager.
- `Stream.repeatedly` builds an infinite stream by calling a function each time an item is requested.
- `Stream.iterate` starts from an initial value and generates each next value from the previous one.
- `Stream.unfold` uses an accumulator and a generator function that returns `{next_element, new_accumulator}`.
- `Stream.resource` is suited to streams that wrap external resources.
- The GitHub example uses `Stream.resource` to fetch paginated API results lazily.
- `process_page` handles the end of pagination, the need to fetch another page, and the normal case that yields items.
- The resulting API lets users query repositories with a stream-like interface and combine organizations with `Stream.flat_map`.
