---
title: "Making Complex Streams Easier to Understand"
date: '2015-10-02T07:49:46-03:00'
category: webclip
summary: 'The post says complicated Elixir pipe chains can become hard to read, and suggests wrapping a Stream composition in a function or variable to make the code easier to understand and reuse.'
tags: ["elixir", "streams", "pipes", "readability"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Curse the Darkness: Making Complex Streams Easier to Understand"
    url: "http://www.cursingthedarkness.com/2015/08/making-complex-streams-easier-to.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-10/cursingthedarkness-com--making-complex-streams-easier-to-understand.md"
    kind: repo
---

The post argues that long Elixir pipe sequences can be hard to reason about when they build a Stream from multiple function compositions. It recommends favoring readability and maintainability, and points out that the same Stream can be wrapped in a function or stored in a variable for reuse.

## Reading notes

- A complicated Stream built from pipes can become inscrutable.
- Elixir is expression-based, so any result can be replaced by a function.
- Streams are compositions of functions.
- A clearer approach is to move the Stream logic into a function like `station_stream(file)`.
- The Stream can also be stored in a variable and used elsewhere in the program.
- As long as the underlying file does not change, the enumerated values do not change.
- `File.stream` enumerates through the whole file each time it is evaluated.
- Pipes are useful in Elixir, but they can be overused.
- The author says readability and maintainability should come first.
- The author’s personal limit for a pipe sequence seems to be about 3-4 steps.
