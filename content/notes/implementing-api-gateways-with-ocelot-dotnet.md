---
title: "Implementing API Gateways with Ocelot - .NET"
date: '2026-09-25T17:16:31+01:00'
category: webclip
summary: 'The page explains how Ocelot forwards upstream requests to downstream microservices, how configuration.json defines routes, and why multiple API gateways and BFFs can better fit autonomous teams.'
tags: ["ocelot", "api-gateway", "microservices", "bff"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Implementing API Gateways with Ocelot - .NET"
    url: "https://learn.microsoft.com/en-us/dotnet/architecture/microservices/multi-container-microservice-net-applications/implement-api-gateways-with-ocelot"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/learn-microsoft-com--implementing-api-gateways-with-ocelot-dotnet.md"
    kind: repo
---

The page describes Ocelot as a lightweight API gateway for ASP.NET Core that forwards incoming HTTP requests to downstream services through ReRoutes defined in configuration.json. It also shows how the eShopOnContainers sample uses separate gateways and BFF-style boundaries so different teams can manage their own routes and deploy the same Docker image with different configuration files.

## Reading notes

- Ocelot is presented as middleware for ASP.NET Core, with routing defined in configuration.json through ReRoutes and optional GlobalConfiguration.
- API Gateway routing maps an upstream path and method to a downstream host, port, and path template.
- In containers, the internal service port is used between gateway and microservice, while external published ports are kept only for local development and debugging.
- The Catalog microservice is shown as a typical ASP.NET Core Web API that can be reached directly through Swagger during development.
- The guide recommends avoiding direct client-to-microservice access in the application and routing through the API Gateway instead.
- eShopOnContainers reuses one Ocelot Docker image to create multiple API Gateway containers, each with its own configuration.json mounted from a volume.
- Splitting gateways by business area or BFF helps development teams stay autonomous and reduces coupling to a single central gateway.
- Ocelot can require authentication with AuthenticationProviderKey and supports claims-based authorization with RouteClaimsRequirement.
- The page notes that secured routes return 401 without a valid token and 403 when claim requirements are not met.
- In Kubernetes, an ingress tier sits in front of the web apps and API gateways and routes traffic to the right endpoints.
- The page also points to Ocelot features such as service discovery, caching, logging, QoS, rate limiting, and Swagger integration.
