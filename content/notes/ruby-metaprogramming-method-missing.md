---
title: "Ruby Metaprogramming - Method Missing"
date: '2015-04-10T11:22:57-03:00'
category: webclip
summary: '`method_missing` lets Ruby objects handle calls to undefined methods before raising an exception. The page shows delegation in a presenter and a custom alias system built on a lookup table.'
tags: ["ruby", "metaprogramming", "method-missing", "delegation"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Ruby Metaprogramming - Method Missing"
    url: "http://www.leighhalliday.com/ruby-metaprogramming-method-missing"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-04/leighhalliday-com--ruby-metaprogramming-method-missing.md"
    kind: repo
---

`method_missing` is a Ruby method for handling calls to methods that do not exist. It gives an object one last chance to deal with the call before Ruby raises an exception. The page shows that it receives the missing method name, any arguments, and an optional block.

## Reading notes

- `method_missing` handles undefined method calls inside an object.
- It receives three parameters: the method name, `*args`, and `&block`.
- One use is dealing with repetitive methods that behave the same way, such as generating HTML tags dynamically in a DSL.
- Another use is delegating method calls to another object.
- A `Presenter` example stores an object and forwards missing calls with `send`.
- A `UserPresenter` overrides `last_name` and lets other calls fall through to the wrapped user object.
- The example shows `first_name` and `age` being delegated, while `last_name` uses the presenter’s own implementation.
- The page also recreates `alias` as `mimic` with a class-level lookup table.
- When a missing method matches an entry in the table, the call is redirected to the aliased method.
- If no alias exists, the code raises an `ArgumentError`.
