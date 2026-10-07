---
title: "Understanding .NET 2015"
date: '2015-02-26T12:08:55-03:00'
category: webclip
summary: 'The post maps the main parts of .NET 2015, centered on .NET Core, open source engineering, and cross-platform support, and explains how frameworks, compilers, and app models fit together.'
tags: ["dotnet-core", "open-source", "cross-platform", "compilers"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Understanding .NET 2015 - Beth Massi - Sharing the goodness - Site Home - MSDN Blogs"
    url: "http://blogs.msdn.com/b/bethmassi/archive/2015/02/25/understanding-net-2015.aspx"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-02/blogs-msdn-com--understanding-net-2015.md"
    kind: repo
---

The post gives a high-level map of .NET 2015 and treats .NET Core as the main foundation for three investment areas: platform innovation, open source development, and cross-platform support. It also places .NET Framework 4.6, Roslyn, RyuJIT, .NET Native, ASP.NET 5, and Universal Windows apps into that larger picture.

## Reading notes

- .NET 2015 is presented as a set of related components rather than a single release.
- The three key investment areas for .NET Core are innovation, open source, and cross-platform support.
- .NET Framework 4.6 adds new APIs, event tracing improvements, and bug fixes, and ships with Windows 10 and Windows Update.
- .NET Core 5 is described as modular, open source, side-by-side deployable, and supported on Windows, Linux, and Mac OSX.
- .NET Core includes refactored base class libraries and runtime components, including RyuJIT, the garbage collector, and native interop.
- Roslyn is the open-source compiler platform for C# and Visual Basic, with code analysis APIs and platform-independent IL output.
- RyuJIT is the default x64 JIT compiler and is described as reducing startup time and adding SIMD support.
- .NET Native compiles C# ahead of time to native machine code, uses a minimal CLR runtime, and is described as improving startup time and memory use for Windows Store apps.
- Windows Forms, WPF, ASP.NET Web Forms, and MVC 5 remain part of .NET Framework 4.6.
- ASP.NET 5 is described as a lean app model that can run on .NET Framework 4.6 or .NET Core 5.
- Universal Windows apps share source code across Windows Phone and Windows apps and run on .NET Native.
- .NET Core uses modular references, shared BCL implementation, NuGet packages, and app-local deployment.
- The post explains that in ASP.NET 5, code changes can be saved and refreshed in the browser without an explicit rebuild.
- Many .NET 2015 pieces are open source and stewarded by the .NET Foundation, while the full .NET Framework is only source-open.
- The post says contributing can also mean filing issues, commenting on proposals, answering questions, or watching activity.
