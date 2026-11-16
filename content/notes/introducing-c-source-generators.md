---
title: "Introducing C# Source Generators"
date: '2020-07-05T14:11:25+00:00'
category: webclip
summary: 'Microsoft introduces Source Generators as a preview C# compiler feature that inspects user code during compilation and emits additional source, aiming to improve startup, build performance, and AOT compatibility.'
tags: ["csharp", "source-generators", "roslyn", "aot"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Introducing C# Source Generators"
    url: "https://devblogs.microsoft.com/dotnet/introducing-c-source-generators"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devblogs-microsoft-com--introducing-c-source-generators.md"
    kind: repo
---

Microsoft introduces Source Generators as a new C# compiler feature in preview. A source generator runs during compilation, inspects user code, and adds generated C# files back into the same compilation. The post frames this as a way to move work from runtime to compile time and to better support scenarios that depend on reflection today.

## Reading notes

- Source Generators are a new component type for C# developers to write.
- They can inspect the full Compilation object and use syntax and semantic models during compilation.
- They can generate C# source files that are added to the compilation while it is running.
- The post compares them to Roslyn analyzers that can also emit source code.
- One goal is to improve startup time by moving work such as ASP.NET Core controller discovery from runtime to compile time.
- Another goal is to reduce build overhead in scenarios that call CSC multiple times.
- They can also replace some stringly typed APIs with strongly typed generated code.
- Source Generators may help with linker-based and AOT compilation by reducing reliance on reflection and reflection emit.
- The article gives a Hello World example that reads syntax trees from the compilation and generates a helper class.
- To try them, users need the .NET 5 preview and Visual Studio preview.
- A source generator is a .NET Standard 2.0 assembly loaded by the compiler.
- The sample setup uses a .NET Standard library, the Microsoft.CodeAnalysis packages, and a ProjectReference added as an Analyzer.
- Visual Studio support is still early, and generated code may require restarting Visual Studio before IntelliSense and errors update.
- The feature is preview only, with API and tooling changes expected before C# 9 GA.
- Source Generators do not rewrite user code; they only add new source files.
- They are C# only for now, and the post does not plan support for Visual Basic at this stage.
