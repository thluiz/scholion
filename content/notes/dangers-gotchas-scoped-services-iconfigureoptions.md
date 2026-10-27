---
title: "The dangers and gotchas of using scoped services in IConfigureOptions"
date: '2021-02-16T11:42:57-03:00'
category: webclip
summary: 'The post explains how ASP.NET Core options work, why `IOptions<>` and `IOptionsSnapshot<>` differ, and how scoped services can create captive dependencies when used in `IConfigureOptions<>`.'
tags: ["asp-net-core", "options-pattern", "dependency-injection", "scoped-services"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The dangers and gotchas of using scoped services in IConfigureOptions"
    url: "https://andrewlock.net/the-dangers-and-gotchas-of-using-scoped-services-when-configuring-options-in-asp-net-core/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2021-02/andrewlock-net--dangers-gotchas-scoped-services-iconfigureoptions.md"
    kind: repo
---

The post explains how strongly typed settings are configured in ASP.NET Core, including the order in which configuration steps run and the difference between `IOptions<>` and `IOptionsSnapshot<>`. It also shows how `IConfigureOptions<>` can be used to build options from other services.

## Reading notes

- ASP.NET Core binds configuration values to a POCO through the Options pattern, and configuration steps run in sequence.
- `IOptions<>` exposes settings through `Value` and has Singleton lifetime.
- `IOptionsSnapshot<>` supports named options, configuration reloads, and has Scoped lifetime.
- `IConfigureOptions<>` lets options depend on other registered services.
- If a Singleton option depends on a Scoped service through `IConfigureOptions<>`, ASP.NET Core raises a captive dependency error in Development.
- One workaround is to use `IOptionsSnapshot<>` together with a Scoped `IConfigureOptions<>`, so options are rebuilt per request.
- The safer general approach is to inject `IServiceProvider` into `IConfigureOptions<>`, create a new scope with `CreateScope()`, and resolve the Scoped service from that scope.
- The scope created inside `IConfigureOptions<>` is different from the request scope, so the same Scoped service may have different instances within one request.
