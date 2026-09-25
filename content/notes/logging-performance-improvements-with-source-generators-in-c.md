---
title: "Logging Performance Improvements with Source Generators in C# .NET"
date: '2025-07-17T13:23:10+01:00'
category: webclip
summary: 'The post explains how source-generated logging in .NET uses `LoggerMessage` on partial methods to reduce overhead, improve type safety, cut boilerplate, and keep log messages consistent.'
tags: ["source-generators", "dotnet-logging", "csharp", "performance"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Logging Performance Improvements with Source Generators in C# .NET - DEV Community"
    url: "https://dev.to/rmaurodev/logging-performance-improvements-with-source-generators-in-c-net-531c?context=digest"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-07/dev-to--logging-performance-improvements-with-source-generators-in-c.md"
    kind: repo
---

The post shows how source generators can be used for logging in .NET through `Microsoft.Extensions.Logging`. It presents partial static logging methods marked with `LoggerMessage`, then shows how the generated code is compiled with the project and used in application code.

## Reading notes

- Source-generated logging in .NET can streamline logging calls, reduce overhead, and provide more efficient, type-safe logging.
- The setup uses `Microsoft.Extensions.Logging` and `Microsoft.Extensions.Logging.Abstractions` packages.
- Logging methods are defined in a static partial class with the `LoggerMessage` attribute.
- The examples include an informational log for item processing and an error log for failed processing.
- The generated code is compiled with the project as part of the partial class.
- The generated methods check whether the log level is enabled before continuing.
- The generated methods build structured log state and then call `logger.Log(...)`.
- The article says source-generated logging is more performant because it avoids reflection and dynamic code generation at runtime.
- It says the approach gives compile-time errors when parameters or message templates do not match.
- It says the generator reduces repetitive logging code and keeps messages consistent in one place.
- The practical tips are to use descriptive names, keep related methods in the same partial class, assign unique event IDs, choose log levels carefully, and match templates to parameters exactly.
- The example keeps logging methods grouped in a `Log` partial class and calls them from a `Todo` class with an injected `ILogger<Todo>`.
