---
title: "How to Start a New .NET Project in 2026"
date: '2026-11-16T04:50:39+00:00'
category: webclip
summary: 'The post recommends setting strict solution-wide standards, adding analyzers, enforcing editor rules, centralizing package versions, using Aspire, enabling OpenTelemetry, and automating build and tests with GitHub Actions.'
tags: ["dotnet", "aspire", "opentelemetry", "github-actions"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to Start a New .NET Project in 2026"
    url: "https://antondevtips.com/blog/how-to-start-a-new-dotnet-project-in-2026"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/antondevtips-com--how-to-start-a-new-dotnet-project-in-2026.md"
    kind: repo
---

Starting a new .NET project works best when the solution is set up with shared standards from the beginning. The post argues for strict build settings, analyzer packages, editor rules, and centralized package versions so quality and consistency are enforced across the whole solution.

It also recommends using Aspire to simplify local development and observability, then adding OpenTelemetry for logs, metrics, and traces. The final step is a GitHub Actions pipeline that restores, builds, tests, and builds Docker images, with a .NET template suggested as a way to skip boilerplate.

## Reading notes

- Use `Directory.Build.props` to apply nullable reference types, implicit usings, the latest analysis level, all analysis rules, and warnings as errors across the solution.
- Add static analyzers such as Meziantou.Analyzer, SonarAnalyzer.CSharp, Roslynator.Analyzers, and xunit.analyzers to catch quality, security, and testing issues during compilation.
- Use `.editorconfig` to define formatting, nullable diagnostics, naming rules, and async method naming conventions for the team.
- Use `Directory.Packages.props` for Central Package Management so package versions stay in one place and project files can reference packages without version numbers.
- Use Aspire to manage dependencies, service discovery, configuration, health checks, and Docker-based local development through AppHost and ServiceDefaults.
- Configure OpenTelemetry through Aspire for logs, metrics, and traces, and add extra instrumentation for PostgreSQL and Redis when needed.
- Use GitHub Actions to run restore, build, tests, and Docker image creation on pushes and pull requests to main.
- Start from a .NET backend project template if you want a preconfigured modular monolith with architecture, tests, logging, and external dependencies already in place.
