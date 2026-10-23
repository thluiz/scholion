---
title: "API Versioning In ASP.NET Core"
date: '2020-09-10T12:34:15-03:00'
category: webclip
summary: 'The article explains why API versioning matters in ASP.NET Core Web API and shows three approaches to route requests by version: query string, URL, and HTTP header.'
tags: ["asp-net-core", "api-versioning", "web-api"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "API Versioning In ASP.NET Core - DEV"
    url: "https://dev.to/sumitkharche/api-versioning-in-asp-net-core-1m91"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-09/dev-to--api-versioning-in-asp-net-core-dev.md"
    kind: repo
---

The article explains why API versioning is needed when an application grows and existing clients still depend on older behavior. It then shows how to set up ASP.NET Core Web API versioning with a NuGet package and a default version in Startup.cs.

## Reading notes

- API versioning helps add new functionality to existing Web APIs without breaking current consumers.
- The setup uses the Microsoft.AspNetCore.Mvc.Versioning package.
- ConfigureServices sets a default API version, makes the default apply when the client does not specify one, and reports versions in response headers.
- The article uses EmployeeV1Controller and EmployeeV2Controller to show separate versions of the same endpoint.
- Query string versioning passes the version as api-version in the request URL.
- URL versioning places the version in the route, such as api/1.0/employee and api/2.0/employee.
- Header versioning reads the version from an x-api-version header through HeaderApiVersionReader.
- The article closes by restating that the three methods covered are query string, URL, and HTTP header versioning.
