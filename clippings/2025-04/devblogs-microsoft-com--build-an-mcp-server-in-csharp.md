---
url: "https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/"
captured_at: "2025-04-16T00:55:36-03:00"
title: "Build a Model Context Protocol (MCP) server in C# - .NET Blog"
domain: "devblogs.microsoft.com"
---

# Build a Model Context Protocol (MCP) server in C# - .NET Blog

> ## Excerpt
> Learn how to build a Model Context Protocol (MCP) server using the C# SDK to enable seamless communication between AI models and applications.

---
In the rapidly evolving world of AI and machine learning, effective communication between models and applications is critical. The Model Context Protocol (MCP) is a standardized protocol designed to facilitate this communication by providing a structured way to exchange context and data between AI models and their clients. Whether you're building AI-powered applications or integrating multiple models into a cohesive system, MCP ensures interoperability and scalability. For developers using tools like Visual Studio Code, you can now integrate and leverage MCP servers in your development flow and it makes it easy to build and test MCP servers on your local machine.

With the release of the MCP C# SDK, developers can now easily build both servers and clients that leverage this protocol. This SDK simplifies the implementation process, allowing you to focus on your application's unique features rather than the complexities of protocol handling. Additionally, the SDK includes support for consuming MCP servers, enabling developers to create robust client applications that interact seamlessly with MCP servers.

In this blog post, we'll explore how you can use the C# SDK to create your own MCP server and client applications.

**Note**: The MCP C# SDK is in preview and APIs may change. We will continuously update this blog as the SDK evolves.

## Getting Started Building an MCP server

The MCP C# SDK is distributed as NuGet packages that you can integrate into a simple console application: `dotnet new console -n MyFirstMCP`.

Add a few basic NuGet packages for the MCP C# SDK and to host the server with `Microsoft.Extensions.Hosting`: `dotnet add package ModelContextProtocol --prerelease` and `dotnet add package Microsoft.Extensions.Hosting`.

The `ModelContextProtocol` package gives access to new APIs to create clients that connect to MCP servers, creation of MCP servers, and AI helper libraries to integrate with LLMs through `Microsoft.Extensions.AI`.

## Starting up our server

Update `Program.cs` with scaffolding to create the MCP server, configure standard server transport, and tell the server to search for Tools (available APIs) from the running assembly, using `AddMcpServer().WithStdioServerTransport().WithToolsFromAssembly()`.

Create a basic tool class with `[McpServerToolType]` and expose methods with `[McpServerTool, Description(...)]`, for example an `Echo` and `ReverseEcho` tool. `WithToolsFromAssembly` scans the assembly for classes with the `McpServerToolType` attribute and registers all methods with the `McpServerTool` attribute. The `Description` on `McpServerTool` is fed into any client connecting to the server, helping the client determine which tool to call.

## Configure and run in VS Code

With this minimal code, the MCP server is ready for testing. To run the project locally, add a new server in the `mcp.json` file in the `.vscode` folder or user settings, specifying `type: stdio`, `command: dotnet`, and args pointing to the project. In GitHub Copilot's Agent mode, the new tool appears, and calling it prompts for permission to execute.

## Integrating with our own data and APIs

MCP servers show their power when they integrate into an existing API or service to query real data used by clients. There is a growing list of servers available including Git, GitHub, Playwright, and Filesystem. The post extends the server with a Monkey MCP server: a `MonkeyService` that queries a monkey database (via `HttpClient`) to return a list of monkeys or details about a specific one, registered with `AddHttpClient()` and `AddSingleton<MonkeyService>()`. A new `McpServerToolType` (`MonkeyTools`) defines `GetMonkeys` and `GetMonkey` tool methods that call into this service and return JSON.

Once registered, GitHub Copilot combined with the running MCP server can request a list of monkeys and display it as a table, generate a Mermaid diagram for the data type, or generate XAML and code for a .NET MAUI app using the data.

## Publish your MCP server

.NET makes it simple to create container images for a .NET app: add `EnableSdkContainerSupport`, `ContainerRepository`, `ContainerFamily` (e.g. `alpine`), and `RuntimeIdentifiers` (e.g. `linux-x64;linux-arm64`) to the project file, then run `dotnet publish /t:PublishContainer`. Multiple runtime identifiers produce multiple local images; passing `-p ContainerRegistry=docker.io` pushes a combined image to a registry, and the correct image is pulled automatically based on the user's machine type. The resulting image can then be configured as an MCP server command (e.g. `docker run -i --rm jamesmontemagno/monkeymcp`).

## Server-Sent Events (SSE)

SSE transport enables server-to-client streaming with HTTP POST requests for client-to-server communication. The MCP C# SDK supports configuring server transports to handle streaming data efficiently to connected clients, with example implementations of an SSE MonkeyMCP server and in the MCP C# SDK samples, plus remote MCP servers via Azure Functions support.

## Go even further with MCP

From here, developers can continue building new functionality into MCP servers for their company, community, and services, usable in GitHub Copilot or other clients. The MCP C# SDK has samples for creating MCP servers, clients, and advanced tutorials.

## Author

James Montemagno is a Principal Lead Program Manager for Developer Community at Microsoft. He has been a .NET developer since 2005, working across game development, printer software, and web services. Prior to becoming a Principal Program Manager, James was a professional mobile developer and has been crafting apps since 2011 with Xamarin.
