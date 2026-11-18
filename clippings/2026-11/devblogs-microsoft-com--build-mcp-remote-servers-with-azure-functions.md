---
url: "https://devblogs.microsoft.com/dotnet/build-mcp-remote-servers-with-azure-functions"
captured_at: "2026-11-18T11:02:26+00:00"
title: "Build MCP Remote Servers with Azure Functions"
domain: "devblogs-microsoft-com"
---

April 16th, 2025

![heart](https://devblogs.microsoft.com/dotnet/wp-content/themes/devblogs-evo/images/emojis/heart.svg)![like](https://devblogs.microsoft.com/dotnet/wp-content/themes/devblogs-evo/images/emojis/like.svg)9 reactions

![](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2025/11/matt-soucoup-96x96.webp)

Principal Cloud Developer Advocate

You can’t run to the grocery store these days without hearing about the Model Context Protocol (MCP)! Well, I hope the grocery store is your safe haven from AI, but the fact is that MCP is one of the hottest and most talked about topics in software development. And I’m going to keep talking about it because I want to show you a brand new experimental preview feature of Azure Functions that takes a ton of work out of creating remote MCP Servers and brings all the goodness of Azure Functions to the equation too.

## What’s MCP anyway?

The Model Context Protocol is nothing more than a specification that makes it easier for AI applications to talk to tooling of some sort.

And generally speaking, that tooling will provide/expose some core business functionality. Like maybe an API of sorts that stores and returns data from Azure Blob Storage.

So here’s the situation: you’re going to have a chat interface of some sort that uses an LLM. How do you get it so that when the LLM is responding to a prompt it knows to invoke the tooling? That’s where MCP comes in.

But MCP is a spec – and that means you have to implement it yourself. And plumbing code is no fun. So that’s what I’m _really_ here to show you today, how to create a remote MCP server using Azure Functions.

### Remote vs local MCP servers

You may have noticed I’m being very intentional to specify _remote MCP server_. And there’s a reason for that.

Right now the most common scenario that involves MCP is a client running locally, like VS Code or Claude Desktop, that has an extension that acts the MCP client (think GitHub Copilot for VS Code) that uses an LLM to call a MCP server also running locally. The MCP server is usually hosted in a Docker container.

But it gets old pretty quickly to install the same MCP server locally everywhere you may need it. Much less making sure people on your team have the same version installed – it’s like taking care of a desktop app.

Remote MCP servers run remotely. As long as the endpoint supports server-side events (SSE), you’re good to go.

## Azure Functions remote MCP servers

Azure Functions is an event-based serverless product. To me, the defining feature of Functions is its ability to seamlessly integrate with other Azure services just be adding attributes to the function definition.

For example, if you want to write to a blob in Azure Storage just decorate your function definition with `[BlobOutput(blobPath)]` and whatever value you return from the function gets written to the blob specified in `blobPath`.

The Functions team recently released an experimental preview that turns a function app into a MCP Server via a `[MCPToolTrigger]` attribute. So now it’s amazingly simple to build an MCP server by using the straightforward development experience of Azure Functions _and_ you still get all the great Azure integration you’ve come to expect too!

### Let’s explore an Azure Functions MCP server

Instead of doing a file->new sample, let’s start from one that’s already ready to go and explore its defining characteristics. Head over to the [Remote MCP Functions Sample](https://aka.ms/cadotnet/mcp/functions/remote-sample) repo to fork/clone/download or just follow along with the code.

This function app lets users highlight text in the editor of VS Code and ask GitHub Copilot to save it with a name. You can then retrieve it using the name you saved it as.

First things first. If you open up the **FunctionsMcpTool.csproj** you’ll see that there’s a NuGet package called **Microsoft.Azure.Functions.Worker.Extensions.Mcp**. This is the one that adds all the MCP-ness to the Function app.

Now checkout **Program.cs**. See the line `builder.EnableMcpToolMetaData()`? That’s going to expose the metadata of each function, like name and description, to the client so the LLM is able to figure out when to invoke it.

Head on over to **SnippetsTool.cs**. There are 2 functions here. **SaveSnippet** adds text as a blob to Azure Storage. And the other, **GetSnippet** returns the text stored in the blob.

Let’s see how to save some text as a blob:

```
[Function(nameof(SaveSnippet))]
[BlobOutput(BlobPath)]
public string SaveSnippet(
    [McpToolTrigger(SaveSnippetToolName, SaveSnippetToolDescription)]
        ToolInvocationContext context,
    [McpToolProperty(SnippetNamePropertyName, PropertyType, SnippetNamePropertyDescription)]
        string name,
    [McpToolProperty(SnippetPropertyName, PropertyType, SnippetPropertyDescription)]
        string snippet
)
{
    return snippet;
}
```

Let’s explain this a bit as there’s a lot of constants being passed in to the properties.

*   `[McpToolTrigger]`: This defines the function as a something that can be invoked from the MCP client. `SaveSnippetToolName` and `SaveSnippetToolDescription` are constants from the **ToolsInformation.cs** that the `builder.EnableMcpToolMetaData()` uses to help the client’s LLM know when to invoke this function.
*   `[McpToolProperty]`: There are 2 of these in this function. One is for taking in the name of the snippet from the user so it can later be retrieved and the other is of the snippet itself. `SnippetNamePropertyName` and `SnippetNamePropertyDescription` are used as metadata. The `PropertyType` in this case indicates we can expect a `string`.

Then because this function is decorated with `BlobOutput` anything we return from it will be written to blob storage. And in this case that is the snippet that was sent from the MCP client.

Cool? Cool.

We return the blob just a little bit differently because we wanted to show off how to do it without using the `[McpToolProperty]` attributes.

Open up **Program.cs** again and checkout:

```
builder
    .ConfigureMcpTool(GetSnippetToolName)
    .WithProperty(SnippetNamePropertyName, PropertyType, SnippetNamePropertyDescription);
```

So that’s saying: for the function defined with the name `GetSnippetTool` (which is a constant in the **ToolsInformation.cs**) add a MCP property to its definition. The property is named `SnippetNamePropertyName` has a description of `SnippetNamePropertyDescription` and it’s a string type.

The function definition looks like:

```
[Function(nameof(GetSnippet))]
public object GetSnippet(
    [McpToolTrigger(GetSnippetToolName, GetSnippetToolDescription)]
        ToolInvocationContext context,
    [BlobInput(BlobPath)] string snippetContent
)
{
    return snippetContent;
}
```

So it’s returning whatever is in the `BlobPath`. That is defined as:

```
private const string BlobPath = "snippets/{mcptoolargs." + SnippetNamePropertyName + "}.json";
```

Well look at that, `SnippetNamePropertyName` makes an appearance. So the path of where the blob is stored within the storage container is defined by its name!

### Deploy to Azure

The real reason we started with this pre-baked sample is because it’s super easy to deploy it to Azure thanks to the Azure Developer CLI (azd).

Assuming you have azd already installed. Open up a terminal, change to the base directory of the repository and run:

```
azd up
```

That’s it. After asking a couple of questions like which Azure subscription you want to use, a name to use, and which region to deploy in, azd will take care of everything. It will provision all the Azure resources. It will deploy the code. It’s going to do everything except setup VS Code.

**Note**

You don’t need to deploy to Azure! Follow [these steps](https://github.com/Azure-Samples/remote-mcp-functions-dotnet?tab=readme-ov-file#prepare-your-local-environment) to run the Function app locally with the Functions Core CLI.

## Consuming the MCP remote server

We’re going to use VS Code, and specifically the GitHub Copilot extension, to test out the remote MCP server. (Find out more about [Copilot plans](https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/getting-started-with-copilot-on-your-personal-account/about-individual-copilot-plans-and-benefits)).

### Grabbing the Functions info

There are 2 pieces of information we’ll need about the Azure function we just deployed. The default domain and the system key for the **mcp\_extension**.

Go to the Azure portal and open the Function app you just deployed with `azd up`. The default domain will be listed in the **Overview** tab under the **Essentials** section.

[![Screenshot from the Azure portal showing where to get the function's default domain from](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2025/04/default-domain.png)](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2025/04/default-domain.png)

Next open up the **App Keys** tab. (It may be easiest to search for it.) And copy the value from the **mcp\_extension** key.

[![Screenshot from the Azure portal showing where to get the function's mcp\_extension system key from.](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2025/04/app-keys.png)](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2025/04/app-keys.png)

### Setting up VS Code

Open up a brand new instance of VS Code and open or create a .NET project (this way we have some code to save ![😉](https://s.w.org/images/core/emoji/17.0.2/svg/1f609.svg)).

1.  In VS Code’s command palette, type (and select): `> MCP: Add Server...`
2.  Next select `HTTP (server-sent events)`
    
    [![Screenshot of VS Code's add MCP server dialog for server sent events](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2025/04/server-sent-events-picker.png)](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2025/04/server-sent-events-picker.png)
    
3.  Now you’ll have to enter the server URL. That’s going to be `https://{default-function-domain}/runtime/webhooks/mcp/sse`. Don’t forget the `/runtime/webhooks/mcp/sse` part!
    
    [![Screenshot of VS Code's add MCP server dialog specifying the URL of the function app](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2025/04/server-url.png)](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2025/04/server-url.png)
    
4.  You’ll get prompted for a local name – you can use the default one or any name you’d like.
5.  Then when asked about where you want to save this, pick `Workspace`.
    
    [![Screenshot of VS Code's add MCP server dialog and picking where to save the server](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2025/04/workspace.png)](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2025/04/workspace.png)
    
6.  A file named **mcp.json** will be created in the **.vscode** folder for you. It will look like this:
    
    ```
    {
        "servers": {
            "my-mcp-server-f84232fb": {
                "type": "sse",
                "url": "https://YOUR-DEFAULT-DOMAIN-URL/runtime/webhooks/mcp/sse"
            }
        }
    }
    ```
    
7.  Almost there! Functions is going to require the **mcp\_extension** key we copied earlier to be sent in the header. We could hardcode it in, but let’s instead make VS Code prompt us for it. Update the **mcp.json** file so it looks like this:
    
    ```
    {
        "inputs": [
            {
                "type": "promptString",
                "id": "functions-mcp-extension-system-key",
                "description": "Azure Functions MCP Extension System Key",
                "password": true
            }
        ],
        "servers": {
            "my-mcp-server-f84232fb": {
                "type": "sse",
                "url": "https://YOUR-DEFAULT-DOMAIN-URL/runtime/webhooks/mcp/sse",
                "headers": {
                    "x-functions-key": "${input:functions-mcp-extension-system-key}"
                }
            }
        }
    }
    ```
    
8.  There should be a **Start** text link right above the server definition. Click it. VS Code will prompt you for the key.
    
    [![VS Code prompting for the Azure Function's mcp\_extension\_key](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2025/04/prompt-for-key.png)](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2025/04/prompt-for-key.png)
    
9.  If all goes well, you should be connected to your Azure Functions remote MCP server and see that you have 3 tools available.
    
    [![VS Code showing a running MCP remote server connected to Azure Functions](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2025/04/running-with-tools.png)](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2025/04/running-with-tools.png)
    

### Using the MCP server

Now for the fun stuff – getting the LLM to invoke the MCP server (or the tools) just by kinda sorta telling it to.

Open up a code file and then Copilot. Make sure Copilot is set to be in **Agent** mode.

[![GitHub Copilot in Agent mode](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2025/04/agent-mode.png)](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2025/04/agent-mode.png)

You’ll notice on top of the text box where you chat with Copilot is a little icon that looks like 2 wrenches. If you click on that a listing of all the tools that Copilot (our MCP client) has access to will appear.

[![Listing of the MCP tools that Copilot has access to](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2025/04/available-tools.png)](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2025/04/available-tools.png)

So highlight some code in the editor. Then in the Copilot chat window say something like:

> Save the highlighted code and call it best-snippet-in-the-world

Copilot will start to figure out what to do and it should eventually ask you if you want to run the **save\_snippet** tool.

[![Copilot prompting if it should run the save\_snippet tool](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2025/04/save-snippet.png)](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2025/04/save-snippet.png)

Then somewhere else – a new file or wherever, prompt Copilot with something like the following:

> Put the best-snippet-in-the-world at the cursor

Copilot will do running and then prompt if you want to perform the **get\_snippets** tool. If you say yes, it will put the snippet you saved before where your cursor was!

## Summary

Adding tooling to LLM-based applications was possible before MCP, but the Model Context Protocol has made it much simpler and also opened the world up to a greater variety of tooling you can add.

Azure Functions is one of those and all it takes is creating a function that’s a `McpToolTrigger` and away you go.

Don’t forget to [check out the code for this sample](https://aka.ms/cadotnet/mcp/functions/remote-sample) and watch the complete walkthrough in this video:

Build MCP Remote Servers with Azure Functions

## Author

![Matt Soucoup](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2025/11/matt-soucoup-96x96.webp)

Principal Cloud Developer Advocate

Matt Soucoup is a Principal DevRel Lead for .NET at Microsoft, where he leads the team that helps .NET developers build with Azure, AI, and GitHub Copilot. He's spent years writing code, giving talks, and building demos that help them make the most of the tooling, lately focused on agentic AI and running Copilot as an agent in production apps.
