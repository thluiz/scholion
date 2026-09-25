---
url: "https://www.blueboxes.co.uk/how-to-build-a-url-shorter-with-c-minimal-apis-and-azure"
captured_at: "2026-09-25T21:49:27+01:00"
title: "How to Build a Url Shorter with C# Minimal APIs and Azure"
domain: "blueboxes-co-uk"
---

On this page

*   [Lookup Storage](#lookup-storage)
*   [Adding New Links](#adding-new-links)
*   [Initial Redirect Code](#initial-redirect-code)
*   [404 Page](#404-page)
*   [Home Page](#home-page)
*   [Completing the Code](#completing-the-code)
*   [Hosting Options](#hosting-options)
*   [Setting Permissions](#setting-permissions)
*   [Summary](#summary)

This page was published 3 years ago. While the content may still be relevant there is a high chance things may have changed and the content may no longer be accurate.

For some time now I have wanted to create a URL shortener of my own, and although there are many third-party services that offer this there’s an appeal to owning it yourself.

This post covers how we can create a URL shortener using minimal APIs and Azure resources in around 20 lines of code. For the initial minimum viable product, the plan is for the URL shortener to support 301 redirects, a basic home page and a friendly 404 page. It should also be run as cheaply as possible ideally leveraging the free tier of Azure.

If you are interested in seeing the code you can skip further down in this post or the latest version of the code is available on [GitHub](https://github.com/blueboxes/minimal-api-url-shortener). A deployed version of the code can be seen at [https://goto42.dev](https://goto42.dev/)

## Lookup Storage

The first and most essential feature is that of the redirect. When a user goes to a URL we need to look it up and if there is a corresponding full URL, redirect to it.

We will use table storage for the look up of the short urls to the target values as this is one of the cheapest and quickest storage mechanisms in Azure.

By using table storage, we can also make use of the `DefaultAzureCredential` object rather than a connection string for added security. The [DefaultAzureCredential](https://learn.microsoft.com/en-us/dotnet/api/azure.identity.defaultazurecredential?view=azure-dotnet) will look in a range of places, each in turn for credentials. This means we can login using the as Az CLI on the local machine and once deployed into Azure it can use a system assigned managed identity.

For this code to work we need to first create a storage account with a table named `UrlLookup` before placing the Url of the account in our configuration file under the key `StorageUri` in the format `https://xxxxxxx.table.core.windows.net/` We also need to add permission to our account to read the data in the table. It is worth noting that the `contributor` or `owner` role is not enough to read the values and you must set your account to have `Storage Table Data Reader` permissions against the storage account.

## Adding New Links

To add any new links we just need to add a new entry to the table. As we do this we need to set the partition key is `url`, the row key as the Url token and a new property of `TargetUrl` with the value of the destination Url.

![Screen shot of Azure Blob storage explorer](https://www.blueboxes.co.uk/_astro/add_link.duALZyhH_ZgQuqs.webp)

## Initial Redirect Code

To keep the Urls as short as possible we want the short code to be directly off the route of the domain. With minimal APIs we do away with the start-up class and various other boilerplate code jumping straight into creating the builder. We then catch any Url off the route using an ID root parameter and then process it in the async lambda.

```
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/{id}", async (string id, HttpContext context, IWebHostEnvironment env) => {

    var tableClient = new TableClient(new Uri(builder.Configuration["StorageUri"]), "UrlLookup", new Azure.Identity.DefaultAzureCredential());

    var url = tableClient.Query<TableRow>(ent => ent.PartitionKey.Equals("url") && ent.RowKey.Equals(id)).SingleOrDefault();
        
    if(url is null){ 
        return Results.NotFound();
    }else{
        return Results.Redirect(url.TargetUrl, true, false);
    }
}); 

app.Run();
```

.

## 404 Page

If we run the above code you will see that we are shown a 404 page provided by the web browser. To give it a custom look lets load in our own HTML page while still keeping the `404` status code.

```
...
if(url is null){ 
    context.Response.StatusCode = 404;
    return Results.Bytes(await File.ReadAllBytesAsync(System.IO.Path.Combine(env.WebRootPath,"404.html")),"text/html");
}else{
    return Results.Redirect(url.TargetUrl, true, false);
}
...
```

## Home Page

With the current configuration all roots that have a value are handled by the `MapGet` method. This however will mean the root url will not be caught by this and return a `404` status code.

We can enable the `UseStaticFiles` method to serve files from the `wwwroot` folder along with the `UseDefaultFiles` method to set the `index.html` as a homepage.

For now this is the only static page that will be able to be accessed as all of the other pages will get captured by our single `MapGet` method. This is something we can address at another point potentially with the use of route filters.

```
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.UseDefaultFiles(new DefaultFilesOptions { DefaultFileNames = new  List<string> { "index.html" }}); 
app.UseStaticFiles();
...
```

## Completing the Code

Putting it all together we can see that the code supports all the features we set out in our minimal viable product (MVP).

This is a basic start and there is more we could add to this project. At the moment all the Urls have to be manually added to table storage. In the future to make it easier to use we could add a secure page to manage the Urls and output caching to reduce the costs.

If you are building out a UI and want to create random short Urls like those in bit.ly or YouTube then have a look at the [https://hashids.org/](https://hashids.org/) set of libraries.

```
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.UseDefaultFiles(new DefaultFilesOptions { DefaultFileNames = new  List<string> { "index.html" }}); 
app.UseStaticFiles();

app.MapGet("/{id}", async (string id, HttpContext context, IWebHostEnvironment env) => {

    var tableClient = new TableClient(new Uri(builder.Configuration["StorageUri"]), "UrlLookup", new Azure.Identity.DefaultAzureCredential());
    var url = tableClient.Query<TableRow>(ent => ent.PartitionKey.Equals("url") && ent.RowKey.Equals(id)).SingleOrDefault();
        
    if(url is null){ 
        context.Response.StatusCode = 404;
        return Results.Bytes(await File.ReadAllBytesAsync(System.IO.Path.Combine(env.WebRootPath,"404.html")),"text/html");
    }else{
        return Results.Redirect(url.TargetUrl, true, false);
    }
}); 

app.Run();
```

## Hosting Options

As this project will build into a docker container there were a number of hosting options however for this post we will host it inside Azure Container Apps.

After setting up a new Container Apps Environment and Container App, we can select continuous deployment. From here it can automatically generate a GitHub workflow, building then pushing the new image to Azure Container Registry. It will also configure a webhook that then deploys the docker image.

![Screen shot of Azure Container Apps Continuous Deployment](https://www.blueboxes.co.uk/_astro/build_and_deploy.BJnT2uyf_ZXYv5E.webp)

We need to ensure when we create the application we set the environment variable for `StorageUri` to point to our table storage.

At the time of writing Azure Container Apps do not currently support free managed SSL certificates. If you are in need of this shibayan has a great [easy-to-follow post](https://dev.to/shibayan/how-to-quickly-setup-a-lets-encrypt-certificate-in-azure-container-apps-3nd7) on binding and then auto-renewing Lets Encrypt certificates to your Azure Container Apps as an alternative.

## Setting Permissions

In order for the Azure Container App to talk to BLOB storage we need to enable a system assigned managed identity.

![Screen shot of Azure Container Apps Managed Id](https://www.blueboxes.co.uk/_astro/system_id.DoxBqRBX_ZKEuwM.webp)

Once enabled switch over to the storage account and grant the permission `Storage Table Data Reader` to the managed identity.

![Screen shot of Azure Blob storage permissions](https://www.blueboxes.co.uk/_astro/table_reader.DC7LYS21_ZkPjOG.webp)

Once this is complete you will have a fully setup Url shortner.

## Summary

In this post we had a brief look how we could implement a simple Url shortener using minimal APIs and Azure table storage. We covered how we can add redirects a basic homepage and a custom 404 page.

If you would like to look at the latest code you can find it on [GitHub](https://github.com/blueboxes/minimal-api-url-shortener). A deployed version fo the code can be seen at [https://goto42.dev](https://goto42.dev/)

Title Photo by [henry perks](https://unsplash.com/es/@hjkp?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/links?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
