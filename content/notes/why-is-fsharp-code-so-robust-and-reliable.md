---
title: "Why is F# code so robust and reliable?"
date: '2026-09-25T07:58:14+01:00'
category: webclip
summary: 'The post argues that F# reduces bugs through immutability, exhaustive matching, no nulls by default, explicit errors, typed primitives, and explicit dependencies in functional code.'
tags: ["fsharp", "code-robustness", "functional-programming", "dotnet"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why is F# code so robust and reliable?"
    url: "https://devblogs.microsoft.com/dotnet/why-is-fsharp-code-so-robust-and-reliable/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/devblogs-microsoft-com--why-is-fsharp-code-so-robust-and-reliable.md"
    kind: repo
---

The post says Access Softek used F# for EasyCoin after years of bugs in C# and .NET work. It attributes the low bug count in production to language features that make state, errors, dependencies, and concurrency more explicit.

## Reading notes

- Values and records are immutable by default, which helps with code predictability and concurrency safety.
- Discriminated unions with exhaustive `match` make the compiler warn when a case has not yet been handled.
- The use of `null` is not the default; missing values are handled with `Option<'T>`, which forces explicit handling of `Some` and `None`.
- Errors in business logic should be handled with `Result<'T>` or with specific DUs, instead of custom exceptions in the middle of the transaction.
- In F#, variables, functions, types, and files can only depend on what was defined before, which avoids circular dependencies and makes clear what depends on what.
- The compiler warns about unused expression results, which draws attention to cases that could go unnoticed.
- Typed primitives with units of measure help distinguish similar types, such as different IDs, at no runtime cost.
- Implicit conversions are not accepted; explicit conversions reduce type errors and problems in string interpolation.
- Concurrency can be modeled with actors and messages, using `MailboxProcessor<'Msg>` or Channels.
- Dependency injection is done through explicit arguments, which allows compile-time checking and makes testing easier.
- The text also mentions SQL, HTML, IaC, and typed route parameters, as well as transpilers from the Fable project to JavaScript and Python.
