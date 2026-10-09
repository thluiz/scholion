---
title: "Why Dart is not the language of the future"
date: '2014-05-01T21:40:44-03:00'
category: webclip
summary: 'Rafaël Garcia-Suarez argues that Dart combines weak static checking, awkward typing, and heavy isolates without gaining the flexibility of dynamic languages, so it looks like a step backward.'
tags: ["dart", "language-design", "typing", "concurrency"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why Dart is not the language of the future | Rafaël Garcia-Suarez [blogs.perl.org]"
    url: "http://blogs.perl.org/users/rafael_garcia-suarez/2011/10/why-dart-is-not-the-language-of-the-future.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-05/blogs-perl-org--why-dart-is-not-the-language-of-the-future.md"
    kind: repo
---

Rafaël Garcia-Suarez reads the Dart 0.01 specification and finds a language that borrows familiar object-oriented syntax from Java but adds features he thinks do not pay off. He questions factories, interfaces, function types, generics, boolean rules, exceptions, isolates, and the way Dart is meant to compile to JavaScript.

## Reading notes

- Dart's syntax looks close to Java, with classes, interfaces, single inheritance, factories, and the usual punctuation of blocks and statements.
- The use of design-pattern ideas at the syntax level feels like an admission that the language design has weaknesses.
- Roles would have been a more modern OO choice, but Dart relies on interfaces that only share method prototypes.
- Static checking is optional and does not stop execution, so type declarations can be wrong without changing program semantics.
- Without type enforcement, the runtime cannot use typing information to optimize execution.
- Interfaces lose much of their point if the language remains effectively dynamic at runtime.
- Function types seem unclear in purpose because there is no visible way to manipulate function pointers.
- Named functions and anonymous functions are treated as different entities, which the author finds disturbing.
- Generic types also seem pointless without real type checking.
- Only the literal true is true, and values like 1 are false unless compared explicitly.
- Boolean coercion is not provided, even though operator overloading is.
- == can be overloaded and is not required to return a boolean, so even (a==a) could be false in pathological cases.
- There is no implicit conversion among numeric, string, and boolean types.
- Integer and floating-point numbers are distinct types.
- String interpolation and parseInt or parseDouble are the main conversion tools described in the spec.
- The overloaded + operator can be used for both addition and concatenation, but without strong typing this is seen as a bad fit.
- The spec encourages exception-based control flow with many exception classes.
- Catch-all handlers and exceptions such as NoMoreElementsException suggest control flow being pushed into exceptions.
- Dart uses isolates instead of shared-state threading, so concurrency is actor-like and heavy.
- Spawning an isolate clones objects and data structures, which makes the model costly in memory.
- The model may fit browser security, but the spec does not discuss that much.
- The author thinks isolates are poorly suited to browser UI work that needs event handling, loading, and animation.
- The spec is clear on lexical scoping, private names, imports, and the removal of a global namespace.
- The conclusion is that Dart gives up the strengths of static languages without getting the flexibility of dynamic ones.
- The post ends by saying Dart already looks obsolete beside Node.js and Coffeescript.
