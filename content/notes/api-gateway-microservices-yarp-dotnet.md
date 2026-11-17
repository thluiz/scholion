---
title: "Don't build Microservices without an API Gateway"
date: '2023-12-14T12:25:06+00:00'
category: webclip
summary: 'Thread argues that an API Gateway is essential in microservice systems, outlines its functions, and highlights YARP as a performant .NET-based reverse proxy with rate limiting and integration features.'
tags: ["microservices", "api-gateway", "dotnet", "yarp"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Thread by @mjovanovictech: Don't build Microservices without an API Gateway. An API Gateway is a critical component o…"
    url: "https://x.com/mjovanovictech/status/1734487378461335582"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2023-12/x-com--api-gateway-microservices-yarp-dotnet.md"
    kind: repo
---

The thread argues that microservice-based systems should not be built without an API Gateway, describing it as a critical component. An API Gateway is presented as a reverse proxy that routes client requests to the proper services while hiding internal implementation details so clients only interact with the gateway. The author lists key uses such as request routing, load balancing, authentication, authorization, rate limiting, and caching.

The author highlights that an API Gateway can be built in .NET using YARP (Yet Another Reverse Proxy), a level 7 HTTP proxy that integrates easily with existing .NET features like built-in authentication and rate limiting. YARP is said to provide excellent performance by default, with support for configuring rate-limit policies in C# code and for multiple rate limiting algorithms. The thread also promotes the author's .NET and software architecture newsletter and notes that Microsoft replaced nginx with YARP.

## Reading notes

- The author states that an API Gateway is a critical part of any microservice-based system and advises against building microservices without one.
- An API Gateway is described as a reverse proxy that routes client requests to the appropriate backend services.
- The gateway hides internal implementation details so that clients only need to call the gateway endpoint.
- The thread lists several uses for an API Gateway: request routing, load balancing, authentication, authorization, rate limiting, and caching.
- The author notes that developers can build an API Gateway in .NET.
- YARP is introduced as a level 7 HTTP proxy whose name stands for Yet Another Reverse Proxy.
- YARP is described as easy to integrate with existing .NET features, including built-in authentication and rate limiting.
- The author claims YARP delivers excellent performance out of the box.
- The framework supports configurable rate-limit policies that can be defined in C# code.
- The author says the framework supports multiple rate limiting algorithms.
- The thread includes a promotion for the author's newsletter, The .NET Weekly, focused on .NET and software architecture.
- In a later reply, the author mentions that Microsoft replaced nginx with YARP.
