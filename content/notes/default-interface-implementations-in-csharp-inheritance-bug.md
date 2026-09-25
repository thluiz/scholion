---
title: "Default Interface Implementations in C#: Where Inheritance Goes to Troll You"
date: '2026-09-25T00:07:07+01:00'
category: webclip
summary: 'Default interface implementations in C# can change behavior when a class gains a base class. The article shows why a service starts returning the interface default and suggests ways to avoid it.'
tags: ["csharp", "default-interface-implementations", "inheritance", "dependency-injection"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Default Interface Implementations in C#: Where Inheritance Goes to Troll You"
    url: "https://dev.to/hypercodeplace/default-interface-implementations-in-c-where-inheritance-goes-to-troll-you-2djf?"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--default-interface-implementations-in-csharp-inheritance-bug.md"
    kind: repo
---

Default interface implementations in C# let interfaces ship methods with default bodies, which helps API evolution but can hide tricky behavior when inheritance enters the picture. The article shows a service that returns the interface default after a base class is added, even though the concrete class still defines the method.

## Reading notes

- Default interface implementations were introduced in C# 8.0 and let interfaces define methods with default bodies.
- The feature helps add methods without breaking existing implementations and improves interoperation with platforms like Android and iOS.
- The article focuses on a case where this behavior becomes subtle when combined with inheritance and dependency injection.
- A service named `MyService` receives an `IFoo` and calls `GetValue()` to print the result.
- `IFoo` provides a default `GetValue()` that returns `"IFoo"`.
- `Foo` defines its own `GetValue()` that returns `"Foo"`, and a unit test against `Foo` passes.
- The console app also prints `"Foo"` before any refactor.
- After introducing `FooBase : IFoo` and making `Foo` inherit from it, the tests still pass but the program output changes to `"IFoo"`.
- The explanation given is that the CLR builds a method table for type resolution and follows the inheritance chain when resolving interface calls.
- Once `Foo` no longer directly implements `IFoo`, the runtime looks to `FooBase`, finds no `GetValue()` there, and falls back to the interface default implementation.
- The article recommends understanding how default methods behave with inheritance and avoiding unnecessary inheritance.
- It suggests preferring composition over inheritance when shared logic is needed.
- It also recommends explicitly declaring the interface on derived classes and providing overrides when needed.
- The article advises testing through the interface instead of relying on a concrete class or `var`.
- It mentions static analysis tools such as Roslyn analyzers and SonarAnalyzer for .NET.
- It ends by recommending documentation and careful review for changes involving default methods.
