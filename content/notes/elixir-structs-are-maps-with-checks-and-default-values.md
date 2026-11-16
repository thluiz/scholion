---
title: "Elixir Structs are maps with checks and default values"
date: '2026-11-16T19:21:43+00:00'
category: webclip
summary: 'Structs are built on top of maps, give default values, and add compile-time checks. They can enforce required keys, reject invalid keys, and still be pattern-matched by struct type.'
tags: ["elixir", "structs", "maps", "compile-time"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Elixir Structs are maps with checks and default values"
    url: "https://dev.to/logicmason/elixir-structs-are-maps-with-checks-and-default-values-135m"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--elixir-structs-are-maps-with-checks-and-default-values.md"
    kind: repo
---

Structs are presented as an extension of maps in Elixir. They keep key-value storage, add default values, and let code rely on a known set of fields when creating and matching data.

## Reading notes

- Structs extend maps and add compile-time checks plus default values.
- Dot syntax raises an error when a key is missing, while bracket syntax returns nil.
- Dot syntax assumes atom keys; when keys are strings, bracket syntax is the option shown.
- A struct defined with defstruct can supply defaults, such as age and name in User.
- Creating %User{} fills in default values for unspecified fields.
- Matching on %User{} or %Admin{} in case checks the struct type through the hidden __struct__ field.
- If a struct used in a match is not defined, Elixir raises a compile-time error.
- @enforce_keys can require that certain fields be given when building a struct.
- Keys not listed in the struct cause a KeyError when used with %User{}.
- Required keys and optional keys can coexist, with defaults used for optional fields.
- Directly setting __struct__ can bypass the usual struct checks, although the text says this should not be abused.
