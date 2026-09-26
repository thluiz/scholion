---
title: "How to reference a .NET Core library in WinForms - Or, .NET Standard Explained"
date: '2026-09-27T00:37:42+01:00'
category: webclip
summary: 'Explains that a WinForms app can reuse a library by targeting .NET Standard, since .NET Standard is an API contract shared by runtimes like .NET Framework and .NET Core.'
tags: ["dotnet-standard", "winforms", "dotnet-core", "dotnet-framework"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to reference a .NET Core library in WinForms - Or, .NET Standard Explained"
    url: "https://www.hanselman.com/blog/HowToReferenceANETCoreLibraryInWinFormsOrNETStandardExplained.aspx?utm_content=buffer58949&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/hanselman-com--how-to-reference-a-net-core-library-in-winforms.md"
    kind: repo
---

The post answers a common setup problem by separating the library target from the app target. The library should usually target .NET Standard, while the WinForms app can stay on .NET Framework. The example shown uses a NETCoreApp 1.1 class library and a WinForms app on .NET Framework 4.6.2, and the fix is to make the library netstandard.

## Reading notes

- The question is about reusing a class library from WinForms, not about running a whole .NET Core app inside WinForms.
- .NET is used for several runtimes, including full .NET Framework, .NET Core, and Xamarin/Mono/Unity.
- .NET Standard is not a runtime or platform; it is a versioned set of APIs that runtimes implement.
- Newer .NET Standard versions expose more APIs, while lower versions are supported by more platforms.
- For reusable libraries, the post recommends targeting the lowest .NET Standard version that still provides the APIs you need.
- The apps that consume the library target a runtime platform, while the library itself targets .NET Standard.
- In the example, changing the library to netstandard solved the problem.
