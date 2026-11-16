---
title: "A new experiment: Call .NET gRPC services from the browser with gRPC-Web"
date: '2026-11-16T02:31:25+00:00'
category: webclip
summary: 'Microsoft announces experimental gRPC-Web support for .NET, letting browser apps call ASP.NET Core gRPC services and .NET clients reach gRPC-Web endpoints without a proxy.'
tags: ["grpc-web", "dotnet", "aspnet-core", "blazor-webassembly"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "A new experiment: Call .NET gRPC services from the browser with gRPC-Web"
    url: "https://devblogs.microsoft.com/aspnet/grpc-web-experiment"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devblogs-microsoft-com--a-new-experiment-call-net-grpc-services-from-the-browser-wit.md"
    kind: repo
---

Microsoft announces experimental gRPC-Web support for .NET. It lets browser-based apps, including JavaScript SPAs and Blazor WebAssembly apps, call gRPC services, and it also lets .NET clients reach gRPC-Web endpoints.

## Reading notes

- gRPC-Web makes browser access possible because browsers cannot implement the gRPC HTTP/2 spec directly.
- The .NET packages support ASP.NET Core gRPC apps without a proxy and let .NET Core clients call gRPC-Web services.
- The article lists three main uses: browser calls to ASP.NET Core gRPC apps, hosting gRPC apps in IIS and Azure App Service, and calling gRPC from platforms where HttpClient does not support HTTP/2.
- gRPC-Web keeps server streaming, but client streaming and bi-directional streaming are not supported.
- To enable server-side support, the app adds the Grpc.AspNetCore.Web package and configures AddGrpcWeb(...) and UseGrpcWeb().
- The browser-side setup may also need CORS configuration.
- For .NET clients, the Grpc.Net.Client.Web package is added and the channel is created with GrpcWebHandler.
- The post says the project is experimental and invites feedback on whether this approach is useful compared with a proxy-based setup.
