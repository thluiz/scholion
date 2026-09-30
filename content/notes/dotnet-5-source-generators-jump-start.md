---
title: ".NET 5 Source Generators Jump Start"
date: '2021-02-08T08:16:26-03:00'
category: webclip
summary: 'The post walks through setting up a .NET 5 solution with a separate netstandard2.0 generator library, adding Roslyn packages, writing a simple ISourceGenerator, and consuming the generated code from a console app.'
tags: ["dotnet-5", "source-generators", "roslyn", "csharp"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: ".NET 5 Source Generators Jump Start | Khalid Abuhakmeh"
    url: "https://khalidabuhakmeh.com/dotnet-5-source-generators-jump-start"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2021-02/khalidabuhakmeh-com--dotnet-5-source-generators-jump-start.md"
    kind: repo
---

The post shows how to start with an empty .NET 5 solution and build a source-generator setup from scratch. It keeps the generator in a separate class library targeting netstandard2.0, adds Roslyn packages, and then uses a console app to consume the generated code.

## Reading notes

- Start from an empty solution and install the latest .NET 5 SDK first.
- Put the source generator in a separate class library for reuse.
- Target the generator project to netstandard2.0.
- Add Microsoft.CodeAnalysis.Analyzers and Microsoft.CodeAnalysis.CSharp.Workspaces to the generator project.
- Implement ISourceGenerator with Initialize and Execute.
- Use context.AddSource to emit a Hello.World class with a Name constant and a Hi method.
- Create a console app to consume the generator.
- Add Microsoft.Net.Compilers.Toolset so the build can find source generators in referenced projects and packages.
- Reference the generator project with OutputItemType set to Analyzer and ReferenceOutputAssembly set to false.
- After building, call Hello.World.Hi() from Main and the generated code prints "Hi, Khalid!".
