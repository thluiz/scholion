---
title: "Having Fun with Microsoft IoC Container for .NET Core"
date: '2026-11-16T01:56:38+00:00'
category: webclip
summary: 'The post shows how to set up Microsoft’s default DI container in a console app, register services, resolve them through a provider, and inspect how single and multiple implementations are handled.'
tags: ["dependency-injection", "ioc-container", "dotnet-core", "service-provider"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Having Fun with Microsoft IoC Container for .NET Core"
    url: "https://dev.to/sahan/having-fun-with-microsoft-ioc-container-for-net-core-1if8"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--having-fun-with-microsoft-ioc-container-for-net-core.md"
    kind: repo
---

The post walks through Microsoft’s default dependency injection container in .NET Core using a simple console app. It shows how to register services in `ServiceCollection`, build a `ServiceProvider`, and let the container create dependencies through constructor injection.

It also examines the container’s internals, including `ServiceDescriptor`, `GetService()`, and the resolution path for `IEnumerable` when multiple implementations are registered for the same interface.

## Reading notes

- The post aims to configure and use Microsoft’s default dependency injection container from scratch in a console application.
- It assumes the reader already understands Dependency Injection and Inversion of Control.
- The container lives in the `Microsoft.Extensions.DependencyInjection` namespace.
- The basic steps are adding the NuGet package, registering types with `ServiceCollection`, and retrieving them from `ServiceProvider`.
- `MyService` depends on `MyDependency` through constructor injection.
- Instantiating `MyService` directly with `new MyDependency()` is presented as a poor approach because it makes the caller manage dependencies and lifetimes.
- The example registers both services with scoped lifetime.
- `BuildServiceProvider()` returns a `ServiceProvider` from the registrations stored in `ServiceCollection`.
- The post says the container resolves and instantiates services when `GetService()` is called.
- `ServiceCollection` stores `ServiceDescriptor` entries that describe each registration.
- `AddScoped` adds a `ServiceDescriptor` to the collection.
- The post recommends using interfaces instead of concrete classes for registrations.
- When multiple implementations are registered for the same interface, the last registered one is the one resolved by default.
- To access multiple implementations, the consumer can inject `IEnumerable<IMyDependency>`.
- Only `IEnumerable` is resolved this way, not `IList`, arrays, or other collection types.
- The post notes that multiple implementations can also be handled with `TryAddEnumerable`.
- The resolution path uses internal call-site logic and caches inside the service provider engine.
- The container resolves an `IEnumerable` by visiting each registered implementation and constructing each one.
- The post mentions that Microsoft’s container covers the essentials but lacks features such as assembly scanning and decorators found in Autofac and Scrutor.
