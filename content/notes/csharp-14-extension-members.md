---
title: "C# 14 Extension Members: Extension Everything"
date: "2026-09-23T17:42:35+01:00"
category: webclip
has_commentary: false
summary: "C# 14 finally ships the long-requested 'extension everything' feature: static extension methods, static and instance extension properties, and eventually operators."
tags:
  - csharp
  - dotnet
sources:
  - title: "C# 14 extension members; AKA extension everything"
    url: "https://andrewlock.net/exploring-dotnet-10-preview-features-3-csharp-14-extensions-members/?utm_source=bonobopress&utm_medium=newsletter&utm_campaign=2096"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-08/andrewlock-net--csharp-14-extension-members.md"
    kind: repo
---

Extension methods have worked the same way since .NET 3.5: a static method with a `this`-modified first parameter, callable either as a static call or, more commonly, as an instance method on the receiver type. Requests for extension properties and static extension methods go back to C# 3.0. An attempt at "extension everything" for C# 4.0 failed outright, and a 2016 language design meeting revisited the idea and shelved it again, until C# 14 finally shipped it, under the name extension members.

The new syntax wraps a method or property in an `extension(){ }` block that takes the receiver type, and for instance members a named receiver parameter, instead of putting `this` on the first argument. It adds three new kinds of member beyond the old instance extension method: static extension methods, static extension properties, and instance extension properties, with extension operators following in a later preview. Lock ported his own NuGet package, NetEscapades.EnumGenerators, to the new syntax and found it trivial: the generator's existing static helper methods just needed wrapping in an `extension(global::MyColours) { }` block to become callable directly on the enum type itself.

## Reading notes

- The extension member syntax is optional. Existing `this`-parameter extension methods keep compiling exactly as before, to the same IL either way.
- Converting one means wrapping it in an `extension<T>(IEnumerable<T> target) { }` block, moving the type parameters and receiver into that block, and dropping `static` from the method itself.
- Static extension methods, such as a `HasValue` added to `string` itself and called as `string.HasValue(someValue)`, don't take a named receiver parameter. The member attaches to the type, not to a variable.
- Instance extension properties keep the receiver parameter and read like ordinary properties (`someValue.IsAscii`), compiling down to `get_`-prefixed methods the same way normal C# properties always have.
- Disambiguating a clash falls back to the same shapes extension methods always used: a static call with the instance as first argument, or a `get_`-prefixed call for properties.
- Porting NetEscapades.EnumGenerators to the new syntax took wrapping its existing static helpers, `IsDefined`, `Parse`, in an `extension(global::MyColours) { }` block, after which they became callable as `MyColours.Parse("Red")` instead of through the generated extensions class name.
