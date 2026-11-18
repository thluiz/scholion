---
title: "Build MCP Remote Servers with Azure Functions"
date: '2025-04-18T14:26:07+00:00'
category: webclip
summary: 'Explains how to turn Azure Functions into remote MCP servers using an experimental MCP extension, then connect and use them from VS Code GitHub Copilot to save and retrieve code snippets.'
tags: ["azure-functions", "model-context-protocol", "github-copilot", "serverless"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Build MCP Remote Servers with Azure Functions"
    url: "https://devblogs.microsoft.com/dotnet/build-mcp-remote-servers-with-azure-functions"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devblogs-microsoft-com--build-mcp-remote-servers-with-azure-functions.md"
    kind: repo
---

The article introduces the Model Context Protocol (MCP) as a specification that lets AI applications call external tooling, and focuses on building *remote* MCP servers with Azure Functions. It uses an experimental preview of the `Microsoft.Azure.Functions.Worker.Extensions.Mcp` package and attributes such as `[McpToolTrigger]` and `[McpToolProperty]` to expose Azure Functions as MCP tools, then shows how to deploy them with `azd`, configure VS Code’s GitHub Copilot extension to talk to the remote server over SSE, and use Copilot to save and retrieve code snippets stored in Azure Blob Storage.

## Reading notes

- MCP is described as a spec that standardizes how AI applications interact with tooling that exposes business functionality, for example APIs that read and write data in Azure Blob Storage.
- A common MCP setup today uses a local client like VS Code or Claude Desktop, with an extension acting as the MCP client talking to a locally hosted MCP server, often running in a Docker container.
- Maintaining MCP servers locally across multiple machines and team members is compared to managing desktop apps, which becomes tedious, motivating the use of remote MCP servers.
- Remote MCP servers only need an endpoint that supports server-sent events (SSE) in order to work with MCP clients.
- Azure Functions is presented as an event-based serverless platform whose strength is easy integration with other Azure services by adding binding attributes to function definitions.
- As an example of Azure Functions integration, the text shows that decorating a function with `[BlobOutput(blobPath)]` causes the function’s return value to be written to a blob at the specified path.
- An experimental preview extension, `Microsoft.Azure.Functions.Worker.Extensions.Mcp`, lets a function app act as an MCP server using a `[McpToolTrigger]` attribute.
- The sample project `Remote MCP Functions Sample` is used as a starting point to explore how an Azure Functions MCP server is structured.
- The sample app lets a user highlight text in VS Code and instruct GitHub Copilot to save it with a name, later retrieving the text by the same name.
- In the sample’s `.csproj` file, adding the `Microsoft.Azure.Functions.Worker.Extensions.Mcp` NuGet package is the step that introduces MCP support into the function app.
- In `Program.cs`, calling `builder.EnableMcpToolMetaData()` configures the app to expose tool metadata, such as name and description, so the MCP client’s LLM can decide when to invoke a given function.
- The `SnippetsTool.cs` file contains two core functions: `SaveSnippet`, which stores text as a blob in Azure Storage, and `GetSnippet`, which reads back the stored text.
- The `SaveSnippet` function is defined with `[Function(nameof(SaveSnippet))]` and `[BlobOutput(BlobPath)]`, so whatever it returns is written to blob storage at the `BlobPath` location.
- The `SaveSnippet` parameters include a `ToolInvocationContext` decorated with `[McpToolTrigger(SaveSnippetToolName, SaveSnippetToolDescription)]` to expose the function as an MCP tool, and two `[McpToolProperty]` parameters for the snippet name and snippet content.
- For the properties in `SaveSnippet`, constant values in `ToolsInformation.cs` provide the tool’s name, description, property names, property descriptions, and a `PropertyType` indicating string values.
- Because of `[BlobOutput]`, returning the `snippet` string from `SaveSnippet` causes that text to be persisted into Azure Blob Storage at the configured path.
- The article notes that the `GetSnippet` function is wired differently to illustrate configuring MCP properties without using `[McpToolProperty]` attributes.
- In `Program.cs`, the MCP configuration for `GetSnippet` is done with `builder.ConfigureMcpTool(GetSnippetToolName).WithProperty(...)`, which attaches a property definition to the tool by name, type, and description.
- The `GetSnippet` function itself uses `[Function(nameof(GetSnippet))]` and a `[McpToolTrigger(GetSnippetToolName, GetSnippetToolDescription)]` parameter, along with a `[BlobInput(BlobPath)]` string parameter that reads content from storage.
- `GetSnippet` returns the `snippetContent` parameter, which is populated from the blob at the given path via the Blob input binding.
- The shared `BlobPath` constant is defined as `"snippets/{mcptoolargs." + SnippetNamePropertyName + "}.json"`, so the blob’s location in the container depends on the `SnippetNamePropertyName` argument value.
- The article explains that using this path format means each snippet is stored and retrieved under a name-based key in the `snippets` folder with a `.json` extension.
- For deployment, the example relies on the Azure Developer CLI (`azd`) to provision resources and publish the function app with minimal manual steps.
- After cloning the sample repository, running `azd up` from the project root triggers a workflow that asks for an Azure subscription, a deployment name, and a region, then automatically creates Azure resources and deploys the code.
- The text notes that `azd up` handles provisioning and deployment but does not configure VS Code, which must be set up separately.
- A note indicates that deployment to Azure is optional, and links to steps for running the function app locally using the Azure Functions Core Tools.
- To connect the MCP client, the article uses VS Code with the GitHub Copilot extension as the front-end for calling the remote MCP server.
- Two pieces of information are required from the Azure portal for the deployed function app: its default domain and the system key for the `mcp_extension`.
- In the portal, the function app’s default domain appears in the **Overview** tab under the **Essentials** section.
- The `mcp_extension` system key is found under the **App Keys** tab, from which its value can be copied for later use.
- In VS Code, the process starts by opening a new instance, loading a .NET project to work with, and using the command palette entry `MCP: Add Server...`.
- When prompted in VS Code’s MCP Add Server flow, the user selects `HTTP (server-sent events)` as the connection type.
- The MCP server URL that must be entered follows the format `https://{default-function-domain}/runtime/webhooks/mcp/sse`, including the `/runtime/webhooks/mcp/sse` suffix.
- VS Code then asks for a local name for the server, and the article notes that any chosen name is acceptable.
- When asked where to store the server configuration, the user should choose `Workspace`, causing VS Code to create an `mcp.json` file under the `.vscode` folder.
- The initial `mcp.json` file contains a `servers` section that maps the chosen server name to a configuration with `type: "sse"` and the function app URL.
- Because Azure Functions requires the `mcp_extension` key to be passed via headers, the article suggests using VS Code input prompts instead of hardcoding the key in `mcp.json`.
- The `mcp.json` file is updated to add an `inputs` array defining a `promptString` input with an ID like `functions-mcp-extension-system-key`, a description, and `password: true` so VS Code hides the entered value.
- The server configuration is also updated to include a `headers` section with `"x-functions-key": "${input:functions-mcp-extension-system-key}"`, wiring the user-entered key into the HTTP requests.
- Once `mcp.json` is updated, VS Code shows a **Start** link above the server entry, which the user clicks to start the MCP server connection.
- VS Code then prompts for the `mcp_extension` system key, using the input definition from `mcp.json`, and the user pastes in the value copied from the Azure portal.
- On successful connection, VS Code shows that the MCP client has three tools available from the Azure Functions remote MCP server.
- To exercise the tools, the user opens a code file and activates Copilot, ensuring it is running in **Agent** mode.
- Within Copilot’s chat interface, there is an icon with two wrenches that, when selected, displays the list of MCP tools that Copilot can call.
- The article instructs the reader to highlight code in the editor and then ask Copilot via chat to save the highlighted code under a chosen name.
- Copilot analyzes the request and eventually prompts the user to confirm running the `save_snippet` tool exposed by the remote MCP server.
- Later, from another location in the editor, the user can ask Copilot to insert the previously named snippet at the cursor position.
- In response to this second prompt, Copilot offers to run the `get_snippets` tool and, upon confirmation, inserts the snippet content where the user’s cursor is located.
- The closing summary states that MCP simplifies adding tooling to LLM-based applications and expands the range of tooling that can be integrated.
- Azure Functions is highlighted as one of these tooling options, where marking a function with `McpToolTrigger` is the key step to turning it into an MCP tool.
- The article provides a link to the sample code repository so readers can explore the full implementation and mentions a video walkthrough titled "Build MCP Remote Servers with Azure Functions".
- The author, Matt Soucoup, is identified as a Principal DevRel Lead for .NET at Microsoft, focusing on helping .NET developers use Azure, AI, and GitHub Copilot, with recent emphasis on agentic AI and running Copilot as an agent in production applications.
