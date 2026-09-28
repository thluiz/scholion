---
title: "Header propagation using ASP.NET Core"
date: '2022-03-21T15:08:19-03:00'
category: webclip
summary: 'The post shows how to propagate a custom request header from one ASP.NET Core Web API to another by using Microsoft.AspNetCore.HeaderPropagation and wiring it into HttpClient and middleware.'
tags: ["aspnet-core", "httpclient", "header-propagation"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Header propagation using ASP.NET Core"
    url: "https://craftbakery.dev/http-header-propagation-aspnet-core/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-03/craftbakery-dev--header-propagation-using-aspnet-core.md"
    kind: repo
---

The page explains a simple ASP.NET Core setup with two Web API projects. One API receives a request, sends a call to an external API, and returns the headers that the external API received. By default, a custom header like `sample-header` is not forwarded.

It then shows how to add `Microsoft.AspNetCore.HeaderPropagation`, register the headers to propagate, attach the propagation handler to the named `HttpClient`, and enable the middleware in `Startup`. After that, the custom header is forwarded to the external API, which can be useful when passing an authorization header from a backend call.

## Reading notes

- The article starts from a case where one REST API calls another REST API and needs to pass through selected HTTP headers.
- A manual approach is described first: read headers from `Request.Headers` and add them to the outgoing `HttpRequestMessage`.
- The suggested library is `Microsoft.AspNetCore.HeaderPropagation`, which handles this scenario.
- The example uses two Web API projects, one named `ExternalApi` and one named `SimpleApi`.
- `ExternalApi` exposes a GET endpoint that returns `Request.Headers` so the received headers can be inspected.
- `SimpleApi` creates an `HttpClient` named `externalapi-client` and calls `/externalapi` on the external service.
- Without extra configuration, the custom header `sample-header` is not propagated.
- The package is added with `dotnet add SimpleApi.csproj package Microsoft.AspNetCore.HeaderPropagation --version 3.1.6`.
- In `ConfigureServices`, the code registers `sample-header` with `AddHeaderPropagation` and adds `.AddHeaderPropagation()` to the `HttpClient` registration.
- In `Configure`, the app enables the middleware with `app.UseHeaderPropagation()`.
- The article says the feature works only when both parts are configured: the headers to propagate and the handler on the `HttpClient`.
- The final test shows the custom header reaching the external API.
- The post mentions a useful case where a SPA sends an authorization token to a backend, and the backend must pass that token to an external API.
