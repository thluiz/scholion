---
title: "Clean Architecture With .NET 6 Using Entity Framework"
date: '2022-03-28T18:13:58-03:00'
category: webclip
summary: 'The article shows how to add Entity Framework to a .NET 6 clean architecture solution, define an AppSetting entity, wire an application DB context through dependency injection, and create the database with migrations.'
tags: ["clean-architecture", "entity-framework", "dotnet-6", "aspnet-core-web-api"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Clean Architecture With .NET 6 Using Entity Framework"
    url: "https://www.c-sharpcorner.com/article/clean-architecture-with-net-6-using-entity-framework/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-03/c-sharpcorner-com--clean-architecture-with-dotnet-6-using-entity-framework.md"
    kind: repo
---

The article continues a previous clean architecture walkthrough and focuses on adding Entity Framework to a .NET 6 solution with ASP.NET Core Web API. It introduces an `AppSetting` entity, places the database context interface in the Application layer, and implements the context in Infrastructure so persistence stays outside the core.

It also lists the packages needed for each project, shows how to register the persistence services, add the connection string in the Web API host, and run migration commands to create the database. The article ends by saying the next step will be a CRUD implementation.

## Reading notes

- The article is a continuation of a previous clean architecture post and keeps the same solution structure.
- The business case is an `AppSetting` entity for storing application variables and configuration data such as SMTP details.
- A generic `BaseEntity<T>` holds the `Id` property so entities can reuse it.
- `AppSetting` inherits from `BaseEntity<int>` and includes `ReferenceKey`, `Value`, `Description`, and `Type`.
- The Application layer defines `IApplicationDBContext` with a `DbSet<AppSetting>` and `SaveChangesAsync`.
- The Infrastructure layer implements `ApplicationDBContext` by inheriting from `DbContext` and `IApplicationDBContext`.
- The solution uses SQL Server through Entity Framework Core packages installed in the Application, Infrastructure, and Web API projects.
- The Infrastructure `DependencyInjection` class registers `ApplicationDBContext` with `UseSqlServer` and maps `IApplicationDBContext` to it.
- The Web API host stores the `RijsatDatabase` connection string in `appsettings.json`.
- The article instructs running `Add-Migration "DB Initialize"` and `Update-Database` with Infrastructure as the default project and Web API as the startup project.
- It says the database is created successfully and the next article will cover CRUD operations and Swagger testing.
