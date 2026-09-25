---
title: "How to Implement Multitenancy in ASP.NET Core with EF Core"
date: '2025-08-11T15:25:57+01:00'
category: webclip
summary: 'The post explains multitenancy with a discriminator column, then shows how EF Core query filters and SaveChanges can isolate tenant data, set TenantId automatically, and support login and header-based tenant selection.'
tags: ["multitenancy", "ef-core", "aspnet-core", "discriminator-column"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to Implement Multitenancy in ASP.NET Core with EF Core"
    url: "https://antondevtips.com/blog/how-to-implement-multitenancy-in-asp-net-core-with-ef-core?utm_source=email&utm_medium=email&utm_campaign=website"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-08/antondevtips-com--how-to-implement-multitenancy-aspnet-core-ef-core.md"
    kind: repo
---

The post presents multitenancy as a way for one application instance to serve multiple tenants while keeping each tenant’s data isolated. It focuses on a discriminator column approach and shows how ASP.NET Core and EF Core can apply tenant filtering and tenant assignment across the application.

## Reading notes

- Multitenancy lets one application instance serve multiple customers while keeping each tenant’s data isolated and invisible to others.
- The article compares database-per-tenant, schema-per-tenant, table-per-tenant, and discriminator-column approaches, then chooses the discriminator column as the main implementation.
- The example uses Books, Authors, Users, and Tenants, with Book, Author, and User entities implementing `ITenantEntity` and carrying a nullable `TenantId`.
- Tenant-related entities can also have a foreign key relationship with `Tenant`, although the post notes that a plain `TenantId` column is also possible.
- A `TenantProvider` reads `user-id` and `tenant-id` from claims in the current HTTP request and exposes them through `GetCurrentTenantInfo`.
- The provider and `IHttpContextAccessor` are registered in dependency injection, and `ApplicationDbContext` receives `ITenantProvider` through its constructor.
- `HasQueryFilter` is used in `OnModelCreating` for `User`, `Author`, and `Book` so read queries only return rows whose `TenantId` matches the current tenant.
- The post says `HasQueryFilter` should be set before `base.OnModelCreating(modelBuilder)` and that the tenant provider must be exposed through a public property for the filters to work correctly per request.
- `SaveChangesAsync` is overridden to find added or modified `ITenantEntity` entries and assign `TenantId` from the current tenant info.
- If no tenant id is available during write operations, the code throws an exception and aborts the operation.
- On login, `IgnoreQueryFilters` is used so a user can be found across all tenants, and the generated JWT includes a `tenant-id` claim.
- The book creation endpoint checks that the author exists, then adds the book and saves changes without tenant-specific code in the endpoint itself.
- The book lookup endpoint uses normal EF Core queries with `Include`, and the global filter keeps it within the current tenant automatically.
- For users who can access multiple tenants, the post shows a version of `TenantProvider` that also reads an `X-TenantId` header.
- A `TenantCheckerMiddleware` can compare the requested tenant header with the tenant claim and return `403 Forbidden` when access is not allowed.
- The post also discusses a conditional global query filter for super-admin access, but notes that EF Core model caching prevents per-request conditionals from working normally.
- To support conditional filters, it shows a `DynamicModelCacheKeyFactory` that forces EF Core to rebuild the model per context instance.
- The article warns that this dynamic cache key approach hurts database-call performance and should be used carefully and benchmarked.
