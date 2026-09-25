---
title: "Dynamically Change the ServiceLifetime of a Registered Service in .NET"
date: '2026-09-24T23:18:52+01:00'
category: webclip
summary: 'The article shows how to replace a registration in IServiceCollection with another one with a different ServiceLifetime, using Replace and extension methods to swap implementation and environment.'
tags: ["dotnet","dependency-injection","service-lifetime","servicecollection"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Dynamically Change the ServiceLifetime of a Registered Service in .NET - Code Maze"
    url: "https://code-maze.com/dotnet-dynamically-change-the-servicelifetime-of-a-registered-service/?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/code-maze-com--dynamically-change-service-lifetime-registered-service-dotne.md"
    kind: repo
---

The article explains that .NET dependency injection usually keeps a service registration as it was first added, but that there are cases where the ServiceLifetime needs to change after registration. It presents this as useful for different environments, feature flags, and testing, where the implementation or lifetime can vary.

It then shows extension methods built on top of Replace() to swap an existing registration for Singleton, Scoped, or Transient, either for an interface mapping or for a concrete type. In the example, IService is registered as scoped with DefaultService, but in development the app replaces it with a singleton LocalDevelopmentService. The article also notes that changing lifetimes can cause captive dependencies if a Singleton depends on a Scoped service.

## Reading notes

- .NET DI usually keeps the service registration as it was made, but there are cases where it is necessary to change the ServiceLifetime after registration.
- The lifetime change can be useful to adjust behavior in tests, feature flags, and environment-specific settings.
- The text proposes extension methods to replace the registration with Singleton, Scoped, or Transient.
- These methods use Replace() from the Microsoft.Extensions.DependencyInjection.Extensions namespace to update the registration.
- There are overloads to handle both interface registration and the concrete implementation itself.
- In the example, IService is registered as Scoped with DefaultService.
- In the development environment, the registration is changed to Singleton with LocalDevelopmentService.
- The example test consists of resolving IService in a minimal API and observing, through the constructor log, which implementation was used.
- The text warns about captive dependencies, especially when a Singleton starts depending on a Scoped service.
