---
title: "10 Blazor Features You Probably Didn't Know"
date: '2021-02-24T08:08:59-03:00'
category: webclip
summary: 'The article lists Blazor capabilities that go beyond common assumptions, including HTML and CSS support, JavaScript interop, MVC integration, SignalR, gRPC, lazy loading, and reuse of existing .NET libraries.'
tags: ["blazor", "dotnet", "webassembly", "javascript-interoperability"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Top 10 Blazor Features You Probably Didn't Know"
    url: "https://www.telerik.com/blogs/10-blazor-features-you-probably-didnt-know?utm_source=csharpdigest&utm_medium=cpm&utm_campaign=blazor-blog-10-features"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2021-02/telerik-com--10-blazor-features-you-probably-didnt-know.md"
    kind: repo
---

The article presents Blazor as a .NET web framework with broader capabilities than many people expect. It says Blazor can work with standard HTML and CSS, use form components and CSS isolation, and also access browser JavaScript APIs through interop.

## Reading notes

- Blazor renders HTML in the browser, so valid HTML and CSS can be used in a Blazor application, including media queries, CSS variables, and Sass.
- Built-in Form and Input components help build forms with validation while still rendering standard HTML.
- CSS isolation is generated at build time and appends a unique identifier to selectors to reduce styling conflicts.
- Blazor can call JavaScript from .NET methods and .NET methods from JavaScript functions through JavaScript interop.
- Blazor can be mixed with MVC or Razor Pages using the component tag helper, which also supports server prerendering.
- Blazor can use SignalR without JavaScript through the Microsoft.AspNetCore.SignalR.Client package.
- .NET 5.0 added integrated gRPC support for ASP.NET Core and Blazor WebAssembly, with clients generated from protobuf files.
- Razor Class Libraries can share components, routes, CSS, JavaScript, static files, and services.
- Blazor WebAssembly can lazy load .NET assemblies and JavaScript modules to reduce initial load time.
- Existing .NET libraries and NuGet packages that target .NET Standard or .NET Core can often be reused in Blazor.
- The article also points to full stack testing and QA as a strength of Blazor applications.
