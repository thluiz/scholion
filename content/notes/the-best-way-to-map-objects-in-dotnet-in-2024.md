---
title: "The Best Way To Map Objects in .Net in 2024"
date: '2025-08-11T15:13:12+01:00'
category: webclip
summary: 'The post compares manual object mapping with AutoMapper and Mapster in .NET, and argues that manual mapping with required properties is safer, clearer, faster, and easier to debug.'
tags: ["dotnet", "object-mapping", "automapper", "mapster"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Best Way To Map Objects in .Net in 2024"
    url: "https://antondevtips.com/blog/the-best-way-to-map-objects-in-dotnet-in-2024?utm_source=email&utm_medium=email&utm_campaign=website"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-08/antondevtips-com--the-best-way-to-map-objects-in-dotnet-in-2024.md"
    kind: repo
---

The post explains object mapping as a transformation between application layers and says it helps with separation of concerns, performance, security, and maintainability. It contrasts manual mapping with mapping libraries and argues that, in 2024, manual mapping is the better choice when combined with required properties.

## Reading notes

- Object mapping transforms objects from one type to another, usually between domain models and public contract models.
- DTOs are described as smaller client-facing models that can combine data from more than one domain model.
- Separate public models let the domain change without breaking API clients.
- The article presents two main mapping approaches: manual mapping and automated mapping with libraries.
- Manual mapping is shown with a `Book` entity and a `BookDto`, where each DTO property is assigned explicitly.
- AutoMapper is presented as a popular library that uses profiles, `AddAutoMapper`, and `IMapper.Map`.
- Mapster is presented as another library, configured through `IRegister`, `AddMapster`, `TypeAdapterConfig.GlobalSettings.Scan`, and `Adapt`.
- The article says mapping libraries can add performance overhead, complex configuration, debugging difficulty, and runtime errors when profiles are not updated.
- For the main example, the article introduces `BlogPost`, `Publisher`, and `BlogHistoryRecord` entities, along with `BlogPostDto` and `PublisherDto`.
- The manual mapping example uses extension methods like `MapToBlogPostDto` and `MapToPublisherDto`.
- `BlogPostDto` maps `Id` to `Url`, converts `PublishedUtc` to `PublishedDate`, maps `Publisher` with another method, and computes `Rating` from history records.
- `PublisherDto` maps `Name`, counts posts for `TotalPosts`, and computes `Rating` from ratings across related blog posts.
- The article shows using these mapping methods in minimal API endpoints for `/api/blogs` and `/api/publishers`.
- All entity and DTO properties are marked `required`, and the article treats this as the key advantage because missing a mapped property becomes a compiler error.
- After adding `Description` and `Category` to `BlogPost`, the article says the application fails to compile until the mapping is updated.
- The conclusion is that manual mapping with required properties is the best approach because it is explicit, compile-time safe, more performant, and easier to debug.
