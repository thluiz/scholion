---
title: "10 Essential Debugging Tools for C# .NET Development"
date: '2020-04-20T21:22:42+00:00'
category: webclip
summary: 'The page lists essential tools for debugging .NET problems, from interactive debugging to profiling, memory analysis, crash dumps, and network inspection, and explains what each one is best for.'
tags: ["dotnet-debugging", "visual-studio", "profiling", "network-debugging"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "10 Essential Debugging Tools for C# .NET Development"
    url: "https://michaelscodingspot.com/dotnet-debugging-tools"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/michaelscodingspot-com--10-essential-debugging-tools-for-csharp-dotnet-development.md"
    kind: repo
---

The page argues that debugging depends on choosing the right tool to extract the right information and reach the root cause of a bug. It groups the tools by the kinds of problems they help with, including performance, memory, third-party code, production issues, and network problems.

## Reading notes

- Visual Studio is presented as the main debugging tool for .NET, with tool windows, exception options, tooltips, and profiling features.
- dnSpy can debug .NET assemblies without symbols or source code, shows decompiled code, and lets you set breakpoints in that code.
- dotPeek is used as a decompiler and can create a symbol server from assemblies without symbols or source code.
- dotTrace records an application run and shows where time is spent in methods, database calls, HTTP requests, and garbage collection.
- SciTech’s .NET Memory Profiler is used to inspect memory snapshots, see what objects use memory, and compare snapshots to find memory leaks.
- OzCode adds Visual Studio debugging features for object visualization, LINQ debugging, improved DataTips, and time travel behavior.
- Sysinternals Suite is presented as a Windows troubleshooting set, with Process Explorer, Process Monitor, and ProcDump as the most useful tools for .NET debugging.
- Performance Monitor visualizes Windows performance counters such as CPU usage, memory usage, exceptions, I/O, ASP.NET requests, and response time.
- PerfView can do performance profiling, memory profiling, ETW analysis, Linux snapshot import, and reports on JIT and garbage collection behavior.
- Fiddler captures HTTP requests and lets you replay or edit them to debug network calls and reproduce server-side problems.
- WinDbg is mentioned as less essential for .NET development now, though still useful for scripting, remoting, and production dump analysis.
- The summary says knowing these tools is part of being a senior developer and that at least one profiler matters for hard performance and memory problems.
