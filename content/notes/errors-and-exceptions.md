---
title: "Errors and Exceptions"
date: '2015-02-15T18:39:22-03:00'
category: webclip
summary: 'The chapter classifies compile-time, logical, run-time, and generated errors, then explains when Erlang code should raise, throw, exit, or handle exceptions with try/catch and after.'
tags: ["errors", "exceptions", "try-catch", "run-time-errors"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Errors and Exceptions | Learn You Some Erlang for Great Good!"
    url: "http://learnyousomeerlang.com/errors-and-exceptions"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-02/learnyousomeerlang-com--errors-and-exceptions.md"
    kind: repo
---

The chapter separates errors into compile-time mistakes, logical bugs, run-time crashes, and generated exceptions, then focuses on the functional subset of Erlang. It explains common compiler messages, the main run-time errors, and why some failures should be left to crash while others should be returned as tuples or handled with exceptions.

## Reading notes

- Compile-time errors usually come from syntax problems, wrong function arity, mismatched module names, unused variables, or clauses that can never match.
- Logical errors are harder to find because they do not crash the program; tests, TypEr, Dialyzer, debugging, and tracing are suggested tools.
- Common run-time errors include `function_clause`, `case_clause`, `if_clause`, `badmatch`, `badarg`, `undef`, `badarith`, `badfun`, `badarity`, and `system_limit`.
- `erlang:error/1` ends the current process and can produce a stack trace.
- `exit/1` also stops the current process, but it is tied to process-level intent and does not return a stack trace.
- `throw/1` is used for cases the programmer is expected to handle and can support non-local returns.
- `try ... catch` can handle `throw`, `error`, and `exit`, with patterns that behave like `case` clauses.
- `after` always runs, even when an exception is raised, and is mainly useful for side effects such as closing a file.
- `catch` is shorter but less precise, because it wraps errors and exits as `{'EXIT', Reason}` and can hide whether a value is an exception or a normal result.
- In the tree example, throws are used to stop a recursive search early when a value is found, avoiding repeated result checks.
