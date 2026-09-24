---
title: "Dynamically Change the ServiceLifetime of a Registered Service in .NET"
date: '2026-09-24T23:18:52+01:00'
category: webclip
summary: 'O artigo mostra como substituir uma inscrição no IServiceCollection por outra com ServiceLifetime diferente, usando Replace e métodos de extensão para trocar implementação e ambiente.'
tags: ["dotnet", "dependency-injection", "service-lifetime", "servicecollection"]
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

## Fichamento

- A DI do .NET normalmente mantém a inscrição do serviço como foi feita, mas há casos em que é preciso mudar o ServiceLifetime depois do registro.
- A mudança de lifetime pode servir para ajustar comportamento em testes, feature flags e configurações específicas de ambiente.
- O texto propõe métodos de extensão para substituir a inscrição por Singleton, Scoped ou Transient.
- Esses métodos usam Replace() do namespace Microsoft.Extensions.DependencyInjection.Extensions para atualizar o registro.
- Há sobrecargas para lidar tanto com registro por interface quanto com a própria implementação concreta.
- No exemplo, IService é registrado como Scoped com DefaultService.
- Em ambiente de desenvolvimento, a inscrição é trocada por Singleton com LocalDevelopmentService.
- O teste do exemplo consiste em resolver IService numa minimal API e observar, pelo log do construtor, qual implementação foi usada.
- O texto alerta para captive dependencies, especialmente quando um Singleton passa a depender de um serviço Scoped.
