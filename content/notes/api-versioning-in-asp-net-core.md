---
title: "API Versioning in ASP.NET Core"
date: '2026-09-25T21:18:53+01:00'
category: webclip
summary: 'The page explains how API versioning lets ASP.NET Core APIs evolve without breaking existing clients, and shows how to add it with Asp.Versioning, choose version readers, and manage controllers and Minimal APIs.'
tags: ["api-versioning", "asp-net-core", "dotnet"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "API Versioning in ASP.NET Core"
    url: "https://t.co/CMMkwpYdBM"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/t-co--api-versioning-in-asp-net-core.md"
    kind: repo
---

API versioning lets an API evolve without breaking clients that are already integrated. The page shows how to add versioning in ASP.NET Core with the Asp.Versioning packages, then read versions from the URL, a header, or the query string.

It also explains the main versioning strategies, how to apply them to controllers and Minimal APIs, and how to deprecate older versions while keeping current versions stable.

## Reading notes

- API versioning assigns distinct identifiers to different iterations of an API so clients can target a specific version while the API changes.
- Without versioning, changes such as removing or renaming APIs, changing behavior, changing the response contract, or changing error codes can break existing clients.
- The setup uses Asp.Versioning.Http, Asp.Versioning.Mvc, and Asp.Versioning.Mvc.ApiExplorer.
- AddApiVersioning can set a default version, report supported versions, assume a default when the client does not specify one, and choose how to read the version.
- AddApiExplorer is useful with Swagger because it fixes endpoint routes and substitutes the version route parameter.
- URL versioning puts the version in the request path and is described as explicit and widely used.
- Header versioning sends the version in a custom request header.
- Query string versioning sends the version as a query parameter and is the default in Asp.Versioning.Http.
- The library also supports media type versioning through IApiVersionReader implementations.
- For controllers, ApiVersion marks the supported versions and MapToApiVersion assigns endpoints to concrete versions.
- Deprecated versions can be marked with Deprecated = true and are reported in the api-deprecated-versions response header.
- For Minimal APIs, versioning uses an ApiVersionSet that is attached to endpoints with WithApiVersionSet and mapped with MapToApiVersion.
- Route groups can reduce repetition by applying the ApiVersionSet once and sharing a route prefix.
- The page recommends versioning from day one, defining breaking changes as a team, deprecating before deleting, reporting supported versions, keeping old versions stable, and preferring URL versioning for public APIs.
