---
title: "Boosting Performance With Sealed Classes in .NET"
date: '2026-09-24T23:20:41+01:00'
category: webclip
summary: 'The article compares open and sealed classes in C# and shows gains in performance in method calls, casting, type checking, and arrays, with an exception for static methods. It also points out the cost for mocking in tests.'
tags: ["sealed-classes","performance","csharp","dotnet"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Boosting Performance With Sealed Classes in .NET - Code Maze"
    url: "https://code-maze.com/improve-performance-sealed-classes-dotnet/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/code-maze-com--boosting-performance-with-sealed-classes-in-dotnet.md"
    kind: repo
---

The article compares sealed and open classes in C# and shows that sealed classes are faster in most measured operations, including void methods, methods with return values, casting, type checks, and array insertion. Static method calls are an exception, and the JIT can make open-class calls as fast as sealed ones when the actual type is known inside the method.

## Reading notes

- Sealed classes block inheritance, and the article uses them to improve performance in .NET projects.
- The benchmark compares an open `Bear` class with a sealed `Husky` class that both inherit from `Animal`.
- Sealed classes are faster when calling overridden void methods and methods that return `int`.
- Calling the static `Walk()` method from the parent class produces similar results for sealed and open classes.
- `ToString()` is faster on the sealed class, though the difference is small.
- Casting with `as` is faster on the sealed class.
- Type checks with `is` are also faster on the sealed class.
- Adding objects to arrays is faster with the sealed class because it avoids a covariance check.
- The article explains that sealed-class calls can be more direct, while open-class calls may use virtual dispatch.
- When the JIT knows the concrete type inside a method, sealed and open classes can perform almost the same.
- Sealed classes make mocking harder, and Moq throws an error for a sealed type.
- The suggested workaround is to code to an interface instead of the concrete sealed class.
- Sealed classes can help detect unreachable code when a conversion is invalid.
- The article says sealed classes are useful when inheritance does not make sense and when performance matters.
