---
title: "9 Erlang Pitfalls You Should Know About"
date: '2014-07-09T10:03:04-03:00'
category: webclip
summary: 'The post lists nine Erlang mistakes that can slip past compile-time checks and tests, covering state updates, pattern matching, guards, records, process shutdown, and boolean operators.'
tags: ["erlang", "pitfalls", "gen-server", "records"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "9 Erlang pitfalls you should know about | MazenHarake"
    url: "https://mazenharake.wordpress.com/2010/10/31/9-erlang-pitfalls-you-should-know-about/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-07/mazenharake-wordpress-com--9-erlang-pitfalls-you-should-know-about.md"
    kind: repo
---

The post collects nine Erlang mistakes that can stay hidden until runtime and make live systems harder to trust. It argues that careful tests and experience help reduce them, but the main point is to know where Erlang’s syntax and OTP behavior can mislead you.

## Reading notes

- Forgetting the updated state can happen when a value is changed in stages and the last return still uses the old state.
- Reusing a variable name can turn an assignment into pattern matching and hide a mismatch until a real value changes.
- Strings are lists, so list subtraction removes matching elements rather than treating the right-hand value as a substring.
- Guard failures can be silent, including in list comprehensions, so invalid data may be skipped instead of crashing.
- Returning arbitrary `{error, Reason}` tuples can create inconsistency unless the surrounding code clearly defines what to do.
- Record syntax behaves differently in function bodies and function clauses, because clauses compile into guards and do not check every field.
- `gen_server` does not always call `terminate/2`; exit trapping and where the exit signal comes from change the behavior.
- `record_info/2` is expanded at compile time and cannot be used as a runtime lookup.
- `and` and `or` evaluate both sides, while `andalso` and `orelse` short-circuit, so the latter are the safer default.
