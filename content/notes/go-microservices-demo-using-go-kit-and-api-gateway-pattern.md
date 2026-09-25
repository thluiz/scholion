---
title: "A Go Microservices Demo using Go kit And API Gateway Pattern"
date: '2026-09-25T00:34:03+01:00'
category: webclip
summary: 'The article shows how to turn go-kit stringsvc3 into a more practical demo by adding Consul-based service discovery, an API gateway client, Docker images, and round-robin load balancing.'
tags: ["go-kit","microservices","api-gateway","service-discovery"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "A Go Microservices Demo using Go kit And API Gateway Pattern"
    url: "https://dev.to/maxwellhertz/a-go-microservices-demo-using-go-kit-and-api-gateway-pattern-2321"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--go-microservices-demo-using-go-kit-and-api-gateway-pattern.md"
    kind: repo
---

The article says go-kit is useful but its examples can be hard to follow, so the author combines stringsvc3 with the apigateway example to build a more practical microservices demo. The focus is on implementing the API gateway with Consul-based service discovery, then packaging the services with Docker and testing them through a client that routes requests to multiple service instances.

## Reading notes

- The author says he found go-kit interesting, but with unclear examples, and that the stringsvc tutorial and the stringsvc3 implementation confused him.
- He concludes that the original example only simulated an API gateway, which would be too impractical in the real world.
- To put together a more useful demo, he combines stringsvc3 with the apigateway example.
- The text says the implementation will focus on the API gateway, not on the basic concepts of endpoint, transport, or service.
- The architecture uses service discovery as a central part of the microservices solution.
- The example chooses Consul to perform simple client-side service discovery.
- In the registration, the stringsvc service is registered in Consul with a unique ID, service name, address, and port.
- The text mentions that it is necessary to provide the Consul address through an environment variable or configuration file.
- Before ending the program, the author highlights that it is important to call Deregister.
- To package the application, he creates a Docker image of stringsvc with Go modules and a two-stage build.
- The gateway is another Go modules project, called stringclient.
- In this client, the code creates a Consul instancer to obtain registered service instances.
- The author explains that the fourth parameter of consul.NewInstancer filters services by tags and the last one controls whether only healthy instances should be returned.
- The client creates endpoints for uppercase and count, uses round-robin load balancing, and applies retry.
- The serviceFactoryBuilder function builds a factory that turns an instance into an HTTP endpoint pointing to the correct path.
- The deployment uses Docker Compose with a Consul container, three stringsvc instances, and a stringclient exposed on port 8080.
- The tests show calls to uppercase and count, with FOO and 3 responses.
- In a sequence of calls, the logs show that the three service instances are called one by one.
- The text attributes this behavior to the round-robin policy used when creating the endpoint.
