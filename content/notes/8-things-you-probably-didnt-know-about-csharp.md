---
title: "8 things you probably didn’t know about C#"
date: '2012-10-30T18:18:36-03:00'
category: webclip
summary: 'A list of lesser-known C# behaviors: params indexers, string interning, leaking underlying types through IEnumerable, brace scoping, enum extensions, static initialization order, cross-instance access to private fields, and the language spec location.'
tags: ["csharp", "dotnet", "language-features", "tips"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "8 things you probably didn’t know about C# » DamienG"
    url: "http://damieng.com/blog/2012/10/29/8-things-you-probably-didnt-know-about-csharp"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-10/damieng-com--8-things-you-probably-didnt-know-about-csharp.md"
    kind: repo
---

The post collects eight C# details that many developers may miss. It shows how some features work in practice, including indexers with params, string interning, enum extension methods, brace-only local scopes, static initialization order, and access rules for private fields between instances.

It also warns that exposing a value as IEnumerable does not stop callers from casting back to the underlying list, and points out that the C# language specification is already installed with Visual Studio. One extra note at the end lists related spec facts about atomic variable references, nullable booleans, and Conditional("DEBUG").

## Reading notes

- Indexers can accept params, so a class can offer both a single-key indexer and a multi-key version side by side.
- Repeated string literals are folded into one interned instance at compile time.
- Returning IEnumerable does not prevent callers from casting back to the underlying List.
- Braces alone can create a nested scope for local variables.
- Enums can be extended with extension methods.
- The order of static field declarations can change program behavior.
- One instance can read another instance’s private fields if both are the same class.
- The C# language specification is available in the Visual Studio installation folder.
