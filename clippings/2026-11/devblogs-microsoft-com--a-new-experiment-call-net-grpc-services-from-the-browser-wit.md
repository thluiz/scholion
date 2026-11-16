---
url: "https://devblogs.microsoft.com/aspnet/grpc-web-experiment"
captured_at: "2026-11-16T02:31:25+00:00"
title: "A new experiment: Call .NET gRPC services from the browser with gRPC-Web"
domain: "devblogs-microsoft-com"
---

January 27th, 2020

0 reactions

![](https://secure.gravatar.com/avatar/080a69d01ff7bdd95b5892c85aaf20be?s=96&r=g)

Principal Software Engineer

I’m excited to announce experimental support for gRPC-Web with .NET. gRPC-Web allows gRPC to be called from browser-based apps like JavaScript SPAs or Blazor WebAssembly apps.

gRPC-Web for .NET promises to bring many of gRPC’s great features to browser apps:

*   Strongly-typed code-generated clients
*   Compact Protobuf messages
*   Server streaming

## What is gRPC-Web

It is impossible to implement the gRPC HTTP/2 spec in the browser because there is no browser API with enough fine-grained control over HTTP requests. [gRPC-Web](https://github.com/grpc/grpc/blob/master/doc/PROTOCOL-WEB.md) solves this problem by being compatible with HTTP/1.1 and HTTP/2.

gRPC-Web is not a new technology. There is a stable [gRPC-Web JavaScript client](https://github.com/grpc/grpc-web), and a [proxy for translating between gRPC and gRPC-Web](https://blog.envoyproxy.io/envoy-and-grpc-web-a-fresh-new-alternative-to-rest-6504ce7eb880) for services. The new experimental packages allow an ASP.NET Core gRPC app to support gRPC-Web **without** a proxy, and allow the .NET Core gRPC client to call gRPC-Web services. (great for Blazor WebAssembly apps!)

## New opportunites with gRPC-Web

*   **Call ASP.NET Core gRPC apps from the browser** – Browser APIs can’t call gRPC HTTP/2. gRPC-Web offers a compatible alternative.
    *   JavaScript SPAs
    *   .NET Blazor Web Assembly apps
*   **Host ASP.NET Core gRPC apps in IIS and Azure App Service** – Some servers, such as IIS and Azure App Service, currently can’t host gRPC services. While this is actively being worked on, gRPC-Web offers an interesting alternative that works in every environment today.
*   **Call gRPC from non-.NET Core platforms** – Some .NET platforms `HttpClient` doesn’t support HTTP/2. gRPC-Web can be used to call gRPC services on these platforms (e.g. Blazor WebAssembly, Xamarin).

Note that there is a small performance cost to gRPC-Web, and two gRPC features are no longer supported: client streaming and bi-directional streaming. (server streaming is still supported!)

## Server gRPC-Web instructions

If you are new to gRPC in .NET, there is a [simple tutorial to get you started](https://docs.microsoft.com/aspnet/core/tutorials/grpc/grpc-start).

gRPC-Web does not require any changes to your services, the only modification is startup configuration. To enable gRPC-Web with an ASP.NET Core gRPC service, add a reference to the _Grpc.AspNetCore.Web_ package. Configure the app to use gRPC-Web by adding `AddGrpcWeb(...)` and `UseGrpcWeb()` in the startup file:

_Startup.cs_

```
public void ConfigureServices(IServiceCollection services)
{
    services.AddGrpc();
}

public void Configure(IApplicationBuilder app)
{
    app.UseRouting();

    // Add gRPC-Web middleware after routing and before endpoints
    app.UseGrpcWeb();

    app.UseEndpoints(endpoints =>
    {
        endpoints.MapGrpcService<GreeterService>().EnableGrpcWeb();
    });
}
```

Some additional configuration may be required to call gRPC-Web from the browser, such as configuring the app to support CORS.

## Client gRPC-Web instructions

The JavaScript gRPC-Web client has [instructions](https://github.com/grpc/grpc-web/tree/master/net/grpc/gateway/examples/helloworld#write-client-code) for setting up a gRPC-Web client to use in browser JavaScript SPAs.

Calling gRPC-Web with a .NET client is the same as regular gRPC, the only modification is how the channel is created. To enable gRPC-Web, add a reference to the _Grpc.Net.Client.Web_ package. Configure the channel to use the `GrpcWebHandler`:

```
// Configure a channel to use gRPC-Web
var handler = new GrpcWebHandler(GrpcWebMode.GrpcWebText, new HttpClientHandler());
var channel = GrpcChannel.ForAddress("https://localhost:5001", new GrpcChannelOptions
    {
        HttpClient = new HttpClient(handler)
    });

var client = Greeter.GreeterClient(channel);
var response = await client.SayHelloAsync(new GreeterRequest { Name = ".NET" });
```

To see gRPC-Web with .NET in action, take a moment to read a great blog post written by Steve Sanderson that uses [gRPC-Web in Blazor WebAssembly](https://blog.stevensanderson.com/2020/01/15/2020-01-15-grpc-web-in-blazor-webassembly/).

## Try gRPC-Web with ASP.NET Core today

Preview packages are on NuGet:

*   [Grpc.AspNetCore.Web](https://www.nuget.org/packages/Grpc.AspNetCore.Web) – Add gRPC-Web support to an ASP.NET Core gRPC service.
*   [Grpc.Net.Client.Web](https://www.nuget.org/packages/Grpc.Net.Client.Web) – Call gRPC-Web endpoints from .NET

Documentation for using gRPC-Web with .NET Core can be found [here](https://docs.microsoft.com/aspnet/core/grpc/browser).

gRPC-Web for .NET is an experimental project, not a committed product. We want to test that our approach to implementing gRPC-Web works, and get feedback on whether this approach is useful to .NET developers compared to the traditional way of setting up gRPC-Web via a proxy. Please add your feedback here or at the [https://github.com/grpc/grpc-dotnet](https://github.com/grpc/grpc-dotnet) to ensure we build something that developers like and are productive with.

Thanks!

## Author

![James Newton-King](https://secure.gravatar.com/avatar/080a69d01ff7bdd95b5892c85aaf20be?s=96&r=g)

Principal Software Engineer

I build Aspire, web servers, and APIs with .NET
