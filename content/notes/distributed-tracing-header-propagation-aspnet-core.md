---
title: "Distributed Tracing using Header Propagation Middleware in ASP.NET Core"
date: '2022-03-21T15:07:49-03:00'
category: webclip
summary: 'Explains how ASP.NET Core header propagation middleware forwards selected headers from an incoming request to outgoing HTTP client calls, with examples for custom headers, B3 trace headers, and correlation IDs.'
tags: ["aspnet-core", "header-propagation", "distributed-tracing", "correlation-id"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Distributed Tracing and Header Propagation Middleware in ASP.NET Core | TheCodeBuzz"
    url: "https://www.thecodebuzz.com/header-propagation-middleware-net-core/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-03/thecodebuzz-com--distributed-tracing-header-propagation-aspnet-core.md"
    kind: repo
---

Header propagation in ASP.NET Core is presented as a middleware-based way to forward request headers to outbound HTTP client calls. The article frames it as useful for distributed tracing, logging, passing secured tokens, and custom details, and shows that the behavior can be set per request or per client.

## Reading notes

- Header propagation is an ASP.NET Core middleware available as NuGet packages for passing HTTP headers from one request to outgoing HTTP client requests.
- The article says distributed tracing in API development is commonly implemented by propagating generic or custom headers from one request to another.
- It lists use cases such as forwarding headers as-is when present, generating new headers conditionally, performing distributed tracing, and passing secured tokens or custom details.
- The middleware centralizes header propagation logic, and the behavior can be controlled per request or per client request.
- The example uses the `x-test-features` header, forwarding it when present and generating a new value with a GUID when it is missing.
- `services.AddHeaderPropagation(...)` is used to register headers for propagation, and `services.AddHttpClient("AccountClient").AddHeaderPropagation()` applies it to a named client.
- `app.UseHeaderPropagation()` is added in the pipeline so the header propagation values are initialized during the HTTP request.
- The article says header propagation only works within the context of an HTTP request.
- It notes that receivers can choose which headers to propagate to the next outgoing request.
- It gives B3 header examples using `x-b3-traceid`, `x-b3-spanid`, and `x-b3-parentspanid`.
- It also shows propagating `X-Correlation-Id` for correlation tracking.
