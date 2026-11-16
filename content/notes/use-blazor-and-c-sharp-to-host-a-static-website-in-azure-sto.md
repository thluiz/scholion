---
title: "Use Blazor and C# to host a static website in Azure Storage"
date: '2026-11-16T00:29:33+00:00'
category: webclip
summary: 'The post walks through creating a Blazor WebAssembly app, publishing its dist folder, enabling Azure Storage static website hosting, and uploading the files to the $web container to serve the site.'
tags: ["blazor", "azure-storage", "static-website", "c-sharp"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Use Blazor and C# to host a static website in Azure Storage"
    url: "https://dev.to/azure/use-blazor-and-c-to-host-a-static-website-in-azure-storage-b1d"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--use-blazor-and-c-sharp-to-host-a-static-website-in-azure-sto.md"
    kind: repo
---

The page shows how to create a Blazor WebAssembly app in Visual Studio, run it locally, publish it to a folder, and use the published dist files as the website contents. It then creates an Azure Storage account, enables the static website feature, and uses the storage account's primary endpoint as the site URL.

## Reading notes

- Create a Blazor app with the Blazor WebAssembly template in Visual Studio 2019, or use Visual Studio Code with the .NET Core 3.1 SDK and the Blazor templates installed.
- The sample Counter.razor page shows UI events calling C# methods, such as incrementing an int.
- Run the app locally with F5 and debug C# code with breakpoints.
- Publish the Blazor project to a folder and use the contents of the dist directory as the files for the website.
- Create an Azure Storage account as a StorageV2 account, then enable the static website feature.
- Set index.html as the index document name and use the Primary endpoint URL to reach the site.
- Use Azure Storage Explorer to open the $web container and upload the published dist files into it.
- The page says the deployment can also be automated with DevOps Pipelines.
