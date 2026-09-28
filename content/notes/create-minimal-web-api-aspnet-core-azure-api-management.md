---
title: "Create a Minimal Web API With ASP.NET Core and Publish To Azure API Management With Visual Studio"
date: '2022-07-27T12:23:14-03:00'
category: webclip
summary: 'The tutorial shows how to create a minimal ASP.NET Core Web API with .NET CLI or Visual Studio 2022, then publish it to Azure App Service and import it into Azure API Management.'
tags: ["aspnet-core", "minimal-web-api", "visual-studio", "azure-api-management"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "ASP.NET, Visual Studio: Create a Minimal Web API - DZone Web Dev"
    url: "https://dzone.com/articles/create-a-minimal-web-api-with-aspnet-core-and-publ"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-07/dzone-com--create-minimal-web-api-aspnet-core-azure-api-management.md"
    kind: repo
---

The page explains that Minimal Web API is a new way to build APIs with only a CSPROJ and Program.cs, without an MVC structure or controllers. It says this approach is less complex, easier to learn and use, uses minimal code, runs faster, and takes advantage of .NET 6 and C# 10 improvements.

It then shows two ways to create the project, one with the .NET CLI and one with Visual Studio 2022. In Visual Studio, the tutorial says to choose the API template, set the project details, select .NET 6, keep authentication as None, uncheck Use Controller, and optionally enable OpenAPI. It compares the project structure with a controller-based app and says Minimal APIs use less code.

## Reading notes

- Minimal Web API is presented as an API approach that keeps only the essential parts needed for HTTP APIs.
- The project can be created with either the .NET CLI or Visual Studio 2022.
- With the .NET CLI, the tutorial uses dotnet new webapi -minimal -o sampleAPI.
- The created folder is smaller than a controller-based Web API project and contains only Program.cs.
- The app runs on two local ports, and the page says the root link returns 404 unless Swagger is added.
- In Visual Studio 2022, the API template is chosen after searching with the keyword API.
- The project setup keeps authentication as None and disables controllers for minimal APIs.
- The article says OpenAPI support can be enabled for Swagger, but it is disabled in the example.
- The tutorial compares the minimal project with a controller-based project and says minimal APIs are simpler.
- To publish, the article first uses Azure App Service and then adds the API to Azure API Management.
- In Azure API Management, the example deletes Echo API and creates a new HTTP API with Display Name WeatherForecasts, Name weatherforecasts, and API Url suffix v1.
- The last step is to return to Visual Studio and publish the earlier web API to Azure API Management so the operations appear in the service.
