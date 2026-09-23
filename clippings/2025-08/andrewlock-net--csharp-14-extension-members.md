---
url: "https://andrewlock.net/exploring-dotnet-10-preview-features-3-csharp-14-extensions-members/?utm_source=bonobopress&utm_medium=newsletter&utm_campaign=2096"
captured_at: "2025-08-06T14:15:36+01:00"
title: "C# 14 extension members; AKA extension everything"
domain: "andrewlock.net"
---

# C# 14 extension members; AKA extension everything

> ## Excerpt
> Hi, my name is Andrew, or 'Sock' to most people. This blog is where I share my experiences as I journey into ASP.NET Core.

---
This is the third post in a series, Exploring the .NET 10 preview, written using the features available in .NET 10 preview 5 (many things may change before the final release).

## Background: Extension methods

Extension methods arrived in 2007 with .NET Framework 3.5, as a supporting feature for LINQ. They emulate adding an instance method to a type by writing a `static` method with a `this`-modified first parameter, e.g. `public static bool IsEmpty<T>(this IEnumerable<T> target) => !target.Any();`. The `this` modifier lets the method be called either as a static method (`EnumerableExtensions.IsEmpty(values)`) or as an instance method (`values.IsEmpty()`) — the instance-method form is used almost everywhere, with static invocation reserved for disambiguating naming clashes.

## Extension members and extension everything

Shortly after extension methods appeared in C# 3.0, developers asked for extension properties and static extension methods too. An attempt at "extension everything" for C# 4.0 failed, and periodic revivals came to nothing — until C# 14.0, where extension everything finally arrives as a feature called extension members.

The new syntax is optional; existing extension methods keep working unchanged. To convert one to the new syntax: wrap it in an `extension(){ }` block, move the receiver parameter and generic type arguments into that block, and drop the `static` modifier, turning `public static bool IsEmpty<T>(this IEnumerable<T> target) => !target.Any();` into an `extension<T>(IEnumerable<T> target) { public bool IsEmpty() => !target.Any(); }` block. It compiles to the exact same thing — there's no compelling reason to convert if that's all you're doing.

## Adding other extension members

The feature that shipped in .NET 10 preview 3 adds three new types of extension member: static extension methods, static extension properties, and instance extension properties (extension operators arrived later, in preview 7).

A static extension method looks similar but is marked `static` and doesn't need (or allow use of) a receiver parameter name — e.g. `extension(string) { public static bool HasValue(string value) => !string.IsNullOrEmpty(value); }`, called as `string.HasValue(someValue)`. The method is added to the `string` type itself, not to a variable.

An instance extension property, by contrast, does use the receiver parameter — e.g. `extension(string target) { public bool IsAscii => target.All(x => char.IsAscii(x)); }` — and is accessed like a normal property (`someValue.IsAscii`). A static operator can also be defined this way, e.g. a `/` operator on `string` that behaves like `Path.Combine`.

## Disambiguating extension members

Direct invocation, needed when extension methods clash, follows the same shape as always: instance extension methods are called statically with the instance as the first parameter; static extension methods as a zero-parameter static call; instance extension properties via a `get_`-prefixed method with the instance as first parameter; static extension properties via a `get_`-prefixed static call. This mirrors how properties are implemented behind the scenes in C# generally — visible in a decompiler as `get_`/`set_`-prefixed methods.

## A case study: NetEscapades.EnumGenerators

The author's own NuGet package generates extension methods and helpers for enums (via an `[EnumExtensions]` attribute), producing a mix of instance extension methods (`ToStringFast()`, `AsUnderlyingType()`) and static methods (`IsDefined()`, `Parse()`) that previously had to be called via the generated type name (`MyColoursExtensions.Parse("Red")`). Targeting C# 14, the generator now wraps the static methods in an `extension(global::MyColours) { }` block, making them callable directly on the enum type itself (`MyColours.Parse("Red")`) — a trivial change to the generator that the author found reassuring evidence the new syntax, however unusual it looks, was well thought out.

## Summary

The post covers the new extension members feature in C# 14 and .NET 10: background on extension methods, converting to the new extension member syntax, the new member types (static extension methods, static and instance extension properties, and the extension operators coming in preview 7), and how adding C# 14 support to NetEscapades.EnumGenerators improved the experience of using its generated extensions.
