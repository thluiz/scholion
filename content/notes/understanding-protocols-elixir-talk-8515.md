---
title: "Understanding Protocols"
date: '2015-05-25T09:24:21-03:00'
category: webclip
summary: 'A question about turning a generic reduce function into an Elixir protocol leads to an explanation of lexical import and why protocol calls must be made explicitly to dispatch across implementations.'
tags: ["elixir", "protocols", "import", "dispatch"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "[elixir-talk:8515] Understanding Protocols - th.luiz@gmail.com - Gmail"
    url: "https://mail.google.com/mail/u/0/?pli=1#label/Listas%2F05+-+Principais/14d6a51460661099"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/mail-google-com--understanding-protocols-elixir-talk-8515.md"
    kind: repo
---

The thread asks why a `reduce` function that works inside a VM module stops behaving as expected after being moved into a protocol. The example shows nested `Num`, `Add`, and `Mul` structs, and the failure appears when `reduce` is called from inside `defimpl` code without qualifying the protocol.

Peter Hamilton suggests calling `Reduce.reduce(...)` explicitly inside each implementation. José Valim explains that `import` is purely lexical in Elixir, so it only makes the function name available in the current file. It does not change how a module resolves calls, and Elixir normally invokes other modules directly instead of coupling behavior to data as in Ruby.

## Reading notes

- The discussion starts from a `KeyError` raised while reducing nested arithmetic structs in Elixir.
- The user expected `import Reduce` inside `VM` or inside the protocol implementations to make all `reduce` versions visible.
- Peter’s fix is to qualify recursive calls with `Reduce.reduce(...)`.
- José says `import` only affects name lookup in the current lexical scope.
- He contrasts Ruby’s coupling of data and behavior with Elixir’s separation of the two.
- In Elixir, calling another module explicitly is the normal pattern, and `import` is only a shortcut for omitting the module name.
