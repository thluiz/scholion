---
title: "The era of the .csproj is over: How Microsoft Just Simplified C# Forever"
date: '2026-10-26T12:29:38+00:00'
category: webclip
summary: '.NET 10 lets you run a single C# file directly, without creating a .csproj, bin, or obj folders, while still compiling and JIT-optimizing the code. When needed, you can convert the file into a full project.'
tags: ["dotnet", "csharp", "project-files"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The era of the .csproj is over: How Microsoft Just Simplified C# Forever."
    url: "https://daily.dev/posts/vLDFW0kZC"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-10/daily-dev--the-era-of-the-csproj-is-over.md"
    kind: repo
---

The post says .NET 10 adds file-based apps for running a single C# file directly from the terminal. It removes the need to create a .csproj, bin, or obj structure for small scripts and prototypes, while keeping the code fully compiled and JIT-optimized.

It also says the workflow stays open for growth, because `dotnet project convert app.cs` can scaffold a complete project from the file when the script becomes larger.

## Reading notes

- Run a single C# file with `dotnet run app.cs` or `dotnet app.cs`.
- No .csproj, bin, or obj folders are needed for this file-based workflow.
- The code is still compiled and JIT-optimized, not interpreted like the older `.csx` format.
- `dotnet project convert app.cs` turns file-level directives into a proper .csproj.
- The change removes scaffolding for quick scripts and prototypes while keeping a path to a full project.
