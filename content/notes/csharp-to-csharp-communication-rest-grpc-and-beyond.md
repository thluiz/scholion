---
title: "C# to C# Communication: REST, gRPC and everything in between"
date: '2020-09-07T19:40:38-03:00'
category: webclip
summary: 'The article compares REST, ReFit, Swagger, and gRPC for C# client-server communication, focusing on contracts, IntelliSense, payload size, performance, and versioning tradeoffs.'
tags: ["csharp", "rest", "grpc", "swagger"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "C# to C# Communication: REST, gRPC and everything in between - Michael's Coding Spot"
    url: "https://michaelscodingspot.com/rest-vs-grpc-for-asp-net/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-09/michaelscodingspot-com--csharp-to-csharp-communication-rest-grpc-and-beyond.md"
    kind: repo
---

The article surveys common ways for a C# client to communicate with a C# server. It starts from an ideal of stateless, strongly typed, IntelliSense-friendly calls, then compares REST, ReFit, Swagger, and gRPC against that goal.

## Reading notes

- REST is the most common approach and uses GET, POST, PUT, and DELETE with JSON payloads.
- ReFit builds on REST and lets client calls look like method calls through a shared interface.
- Swagger defines a REST contract in JSON and can generate C# clients from that schema.
- Swagger tools mentioned include Swashbuckle.AspNetCore on the server and AutoRest or swagger-codegen on the client.
- The author says Swagger JSON is created at runtime, which makes CI/CD automation harder.
- gRPC uses .proto files as the contract and generates clients from them.
- gRPC uses Protobuf binary serialization, HTTP/2, multiplexed streams, and bidirectional streaming.
- The article says gRPC is usually faster than REST, especially for large payloads, but ASP.NET support still feels less mature.
- The author says moving a large ASP.NET app from REST to gRPC is hard, while a microservices setup makes gradual adoption easier.
- Other communication options mentioned are GraphQL, SignalR, TcpClient, UdpClient, and WCF.
