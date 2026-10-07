---
title: "Writing assertive code with Elixir"
date: '2015-02-03T16:22:25-03:00'
category: webclip
summary: 'The post argues that Elixir code should be written assertively: use pattern matching, explicit polymorphism, and strict map or struct access to catch bad assumptions early and keep code simpler.'
tags: ["elixir", "pattern-matching", "polymorphism", "structs"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Writing assertive code with Elixir « Plataformatec Blog"
    url: "http://blog.plataformatec.com.br/2014/09/writing-assertive-code-with-elixir/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-02/blog-plataformatec-com-br--writing-assertive-code-with-elixir.md"
    kind: repo
---

The post argues that assertive code in Elixir is clearer, faster, and easier to maintain. It recommends making assumptions explicit so unexpected input fails early instead of creating hidden complexity.

## Reading notes

- Pattern matching is the preferred way to extract the token from a query-like string, because it asserts that each split pair has exactly two elements.
- The less strict version can accept malformed values by accident, such as a token value with extra equals signs.
- Using pattern matching turns unexpected shapes into crashes, which makes corner cases visible and easier to discuss.
- Polymorphism in Elixir is opt-in through protocols, so a function should only be opened to many data types when that is truly intended.
- Calling to_string before replacement makes dasherize work with many more types and therefore less specific.
- If the function should support only atoms and strings, the post recommends handling those cases directly instead of opening it to all protocol implementations.
- When a protocol is really desired, tests should cover at least a couple of supported types.
- For maps, strict field access is preferred over dynamic access because it catches bugs early.
- The same idea applies to structs, where user.first_name is preferred over user[:first_name].
- Deriving Access for a struct should be reserved for cases where dynamic access is truly needed.
- The overall claim is that assertive style postpones incidental or accidental complexity until it is actually required.
