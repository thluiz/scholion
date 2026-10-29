---
title: "Elixir Christmas Tree Puzzle"
date: '2016-01-08T08:44:10-03:00'
category: webclip
summary: 'A coding puzzle asks for an Elixir program that prints a centered Christmas tree made of zeros, with a star on top and a trunk at the bottom, and ranks solutions by character count.'
tags: ["elixir", "coding-puzzle", "string-formatting"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Elixir Christmas Tree Puzzle"
    url: "http://elixirgolf.com/articles/elixir-christmas-tree-puzzle/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-01/elixirgolf-com--elixir-christmas-tree-puzzle.md"
    kind: repo
---

The page sets a short Elixir coding challenge: print a Christmas tree with a 9-row triangle of `0` characters, a `*` at the top, and an `H` trunk at the bottom. The star and trunk must line up with the tree, and the full output is 11 rows high.

## Reading notes

- The triangle has to be properly indented so each row stays centered above the next.
- The top `*` and bottom `H` are separate rows aligned with the tree.
- The shortest solution wins, though creative versions can receive an honourable mention.
- Submissions were requested as GitHub issue comments, together with a Twitter handle.
- The article then presents several submitted solutions and explains how they work.
- The winning solution uses an anonymous function and the Erlang `:string.centre/2` function.
- One solution uses `io.format/2` and `io_lib.format/2` to build the rows.
- Other solutions rely on lists, comprehensions, `List.duplicate/2`, `IO.puts`, or string functions such as `String.rjust/2` and `String.duplicate/2`.
- The bonus section shows more decorative versions, including a colored tree with flashing lights.
