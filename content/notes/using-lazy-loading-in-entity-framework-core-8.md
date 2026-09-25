---
title: "Using lazy loading in Entity Framework Core 8"
date: '2026-09-25T21:38:11+01:00'
category: webclip
summary: 'The article shows how EF Core 8 can delay loading related data until a navigation property is accessed, using ILazyLoader, Fluent API configuration, or manual Entry loading.'
tags: ["entity-framework-core", "lazy-loading", "ilazyloader", "fluent-api"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Using lazy loading in Entity Framework Core 8"
    url: "https://toreaurstad.blogspot.com/2024/09/using-lazy-loading-in-entity-framework.html?_bhlid=efd39774a29b3493b98805aa251f5eb60eb7366e&m=1"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/toreaurstad-blogspot-com--using-lazy-loading-in-entity-framework-core-8.md"
    kind: repo
---

The article shows how to opt into lazy loading in EF Core 8 so related data is not loaded until it is needed. It uses a Customer example with navigation properties and explains that, without eager loading or lazy loading, those properties stay null. It also notes that the debugger can make lazy-loaded data appear loaded before the application code accesses it.

## Reading notes

- EF Core 8 does not populate related navigation properties automatically unless eager loading or lazy loading is enabled.
- A Customer entity is used as the example, with CustomerRank and AddressCustomers as related properties.
- The ILazyLoader service from Microsoft.EntityFrameworkCore.Infrastructure can be injected into the entity through a private constructor.
- A navigation property can call LazyLoader.Load in its getter so the related value is loaded on access.
- If injecting behavior into entities feels unclean, the article shows using Fluent API in DbContext configuration instead.
- AutoInclude is used on Customer.AddressCustomers and Customer.CustomerRank in the shown modelBuilder configuration.
- The article also shows manual loading with DbContext.Entry, then Reference or Collection, followed by Load.
- Lazy loading still happens only when the navigation property is accessed.
- In Visual Studio debugging, data may look loaded because the debugger can read lazy-loaded fields too.
- In the example, the private field _customerRank is initially null and is loaded when CustomerRank is accessed.
