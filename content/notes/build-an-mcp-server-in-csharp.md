---
title: "Build a Model Context Protocol (MCP) Server in C#"
date: "2026-09-23T17:31:42+01:00"
category: webclip
has_commentary: false
summary: "James Montemagno walks through the C# SDK for MCP, from a two-line echo tool to a real Monkey MCP server with data, container publishing, and SSE transport."
tags:
  - mcp
  - csharp
  - ai-tooling
sources:
  - title: "Build a Model Context Protocol (MCP) server in C# - .NET Blog"
    url: "https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-04/devblogs-microsoft-com--build-an-mcp-server-in-csharp.md"
    kind: repo
---

Montemagno builds a minimal MCP server with the new C# SDK: a console app hosting `AddMcpServer().WithStdioServerTransport().WithToolsFromAssembly()`, with tools defined as static methods tagged `[McpServerTool]` inside a class marked `[McpServerToolType]`. The SDK scans the assembly for those attributes and registers the methods automatically, using each method's `Description` to tell a connecting client what the tool does.

He registers a `MonkeyService` (querying a small HTTP API for monkey data) via dependency injection and exposes it as `GetMonkeys`/`GetMonkey` tools returning JSON. In the walkthrough, GitHub Copilot's Agent mode calls those tools to render the results as a table, a Mermaid diagram, or the XAML for a .NET MAUI screen. The post closes with packaging: containerizing the server with the .NET SDK's built-in support, publishing to a registry, and a note on SSE transport for streaming server-to-client communication in remote MCP servers.

## Fichamento

- An MCP server built with the SDK is a console app: `AddMcpServer().WithStdioServerTransport().WithToolsFromAssembly()` sets up the transport and scans the assembly for tools.
- Tools are static methods marked `[McpServerTool]` inside a class marked `[McpServerToolType]`. The `Description` attribute on each becomes what a connecting client, GitHub Copilot's Agent mode in the walkthrough, reads to decide which tool to call.
- The example grows from a toy echo tool into a `MonkeyService` that fetches real data over HTTP, registered via dependency injection and exposed as `GetMonkeys`/`GetMonkey` tools that return JSON.
- Once wired up, Copilot's Agent mode can call the tools directly, asking for a monkey list as a table, a Mermaid diagram of the data type, or the XAML for a .NET MAUI screen built from it.
- Publishing is built into the .NET SDK: setting `EnableSdkContainerSupport` and target runtime identifiers, then running `dotnet publish /t:PublishContainer`, produces per-architecture container images that can be pushed to a registry.
- SSE transport streams server-to-client data over HTTP for remote MCP servers, with the SDK samples showing an SSE Monkey server and a deployment via Azure Functions.
