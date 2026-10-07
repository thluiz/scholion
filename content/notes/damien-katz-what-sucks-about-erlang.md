---
title: "Damien Katz: What Sucks About Erlang"
date: '2015-01-24T06:58:54-03:00'
category: webclip
summary: 'Damien Katz argues that Erlang’s syntax, control flow, string handling, records, memory failure behavior, code organization, and uneven libraries make it awkward for some application work, even though it shines in systems like CouchDB.'
tags: ["erlang", "programming-languages", "couchdb", "syntax"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Damien Katz: What Sucks About Erlang"
    url: "http://damienkatz.net/2008/03/what_sucks_abou.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-01/damienkatz-net--damien-katz-what-sucks-about-erlang.md"
    kind: repo
---

Damien Katz says Erlang works very well for CouchDB and other network servers, but he finds it awkward for tests and front-end application work. He points to context-sensitive syntax, restrictive `if` expressions, string handling as integer lists, verbose records, brittle memory failure behavior, and limited code organization.

## Reading notes

- Erlang’s syntax uses expression separators that vary by context, which makes editing and refactoring harder than in languages with more uniform terminators.
- `if` expressions must match at least one branch or they throw `if_clause`, and they cannot call user-defined functions in conditional expressions.
- `case` is presented as a better substitute for many `if` uses, but it shares the same requirement to match at least one branch.
- Erlang has no string type; strings are lists of integers, which makes string handling less direct and makes strings hard to distinguish from integer lists.
- Katz says Erlang fits recursive, functional code and shared-nothing concurrency well, especially for servers and database internals.
- For test code and other changing application code, immutable variables and repeated rebinding can require more edits than equivalent code in C or JavaScript.
- Records are described as verbose and limited, because record type syntax must be repeated where members are accessed and the feature compiles down to tuples.
- He says records are hard to use from the REPL and in debugging, where they appear as tuples instead of records.
- When the VM cannot get memory from the OS, Katz reports that Erlang can terminate the whole VM rather than only the failing process.
- He says automatic restart is not built in and may need a separate watchdog process, while the built-in `heart` process also dies with the VM.
- Erlang’s main organizational unit is the source file module, so creating something like a class means creating another file and adding it to build and source control.
- Katz finds several bundled libraries and tools uneven in quality, including Inets httpd, Xmerl, GUI tools on Windows and OS X, and the OTP build and versioning system.
- He ends by saying Erlang has major strengths and real-world value, but that its weaknesses are not discussed enough.
