---
title: "That string concatenation frisson"
date: '2026-09-25T20:21:19+01:00'
category: webclip
summary: 'Concatenating strings with a delimiter can create collisions or make the original values impossible to recover. If the delimiter is unavoidable, the text says to send values separately or escape and unescape them rigorously.'
tags: ["string-concatenation", "delimiter-escaping", "data-collisions"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "That string concatenation frisson"
    url: "https://qntm.org/concat"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/qntm-org--that-string-concatenation-frisson.md"
    kind: repo
---

The page warns that concatenating strings with a delimiter like `:` can be unsafe when the result is used as an identifier or later split back into parts. Different input pairs can produce the same combined string, and a split cannot always recover the original values.

It says this becomes especially risky when one field may be used to inject a value such as `horse:admin`. If colons are unavoidable, the text recommends either sending the values separately or using a rigorous escaping and unescaping procedure.

## Reading notes

- Concatenating `application` and `endpoint` with `:` can create collisions such as `a:b` plus `c` matching `a` plus `b:c`.
- If the combined string must be split later, the original two strings may no longer be recoverable.
- This is presented as especially worrying for fields like `username` and `role`, where an injected colon can change meaning.
- If colons must be allowed, the text advises sending the values separately.
- If concatenation is still used, the delimiter needs proper escaping before joining and unescaping afterward.
