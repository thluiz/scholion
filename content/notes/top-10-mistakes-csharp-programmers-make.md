---
title: "Top 10 Mistakes that C# Programmers Make"
date: '2014-04-28T21:50:28-03:00'
category: webclip
summary: 'The article lists ten common C# pitfalls, from value versus reference types and string comparison to LINQ, extension methods, resource disposal, exceptions, and compiler warnings.'
tags: ["c-sharp", "programming-mistakes", "linq", "dotnet"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "10 Most Common C# Mistakes | Toptal"
    url: "http://www.toptal.com/c-sharp/top-10-mistakes-that-c-sharp-programmers-make"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-04/toptal-com--top-10-mistakes-csharp-programmers-make.md"
    kind: repo
---

The article collects ten common mistakes C# programmers make and explains why they happen. It focuses on language details and runtime behavior that can lead to wrong assumptions, unexpected results, and harder debugging.

## Reading notes

- C# is a strongly typed language on the CLR, and its type checking can catch many errors early, but programmers can still lose those benefits by using the language carelessly.
- Value types and reference types behave differently, so assigning and modifying objects can produce surprising results if you do not know which kind of type you are using.
- Uninitialized value types do not become null; they take a default value, so null checks can be misleading.
- String comparison should be explicit, with `Equals` and a `StringComparison` value, because different comparison modes can produce different results.
- LINQ can replace iterative collection manipulation, but performance trade-offs may still matter.
- The result of a LINQ query can change depending on the underlying objects, such as in-memory collections versus `DbSet` data translated to SQL.
- Extension methods are static methods brought into scope through `using` and marked by a `this` parameter on the first argument.
- Choosing the right collection type matters for performance and type safety, and generic collections are usually preferable to non-generic ones.
- Objects that wrap resources should be disposed deterministically, and `using` ensures `Dispose()` is called when a block ends.
- Sometimes the exception-throwing form of an operation is the right choice, especially when failure should be surfaced immediately.
- Compiler warnings should be fixed instead of ignored, because they can point to real defects even when the program still runs.
