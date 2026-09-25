---
title: "How to Build a Url Shorter with C# Minimal APIs and Azure"
date: '2026-09-25T21:49:27+01:00'
category: webclip
summary: 'Describes a small URL shortener built with C# minimal APIs and Azure Table Storage, using 301 redirects, a custom 404 page, a static home page, and managed identity access.'
tags: ["c-sharp", "minimal-apis", "azure-table-storage", "url-shortener"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to Build a Url Shorter with C# Minimal APIs and Azure"
    url: "https://www.blueboxes.co.uk/how-to-build-a-url-shorter-with-c-minimal-apis-and-azure"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/blueboxes-co-uk--how-to-build-a-url-shorter-with-c-minimal-apis-and-azure.md"
    kind: repo
---

The post outlines a simple URL shortener built with C# minimal APIs and Azure resources. It keeps the first version small, with 301 redirects, a home page, a custom 404 page, and low-cost hosting on Azure.

## Reading notes

- The redirect lookup uses Azure Table Storage because it is described as one of the cheapest and quickest storage options in Azure.
- The code uses `DefaultAzureCredential` instead of a connection string, so it can authenticate locally with Azure CLI and in Azure with a system-assigned managed identity.
- A storage account with a table named `UrlLookup` is required, and the `StorageUri` setting must point to that table endpoint.
- The account needs `Storage Table Data Reader` permission, because contributor or owner roles are not enough to read table values.
- New links are added as table entries with partition key `url`, row key set to the token, and a `TargetUrl` property for the destination.
- The minimal API route captures any path token with `MapGet("/{id}")` and queries the table for a matching row.
- If no row is found, the code returns a 404 status and serves a custom `404.html` file from the web root.
- `UseDefaultFiles` and `UseStaticFiles` serve `index.html` from `wwwroot` as the home page.
- The complete example combines redirects, the static home page, and the custom 404 page in one minimal API app.
- The post suggests future additions such as a secure page to manage URLs and output caching to reduce costs.
- For random short codes, it points to the `hashids` libraries.
- The hosting example uses Azure Container Apps with continuous deployment from GitHub and Azure Container Registry.
- The app needs a `StorageUri` environment variable in Container Apps.
- Azure Container Apps do not currently support free managed SSL certificates, so the post links to a Let’s Encrypt workaround.
- To let the Container App access storage, the system-assigned managed identity must be granted `Storage Table Data Reader` on the storage account.
