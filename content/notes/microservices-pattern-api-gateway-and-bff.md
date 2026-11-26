---
title: "Microservices Pattern: API Gateway / Backends for Frontends"
date: '2026-11-25T16:12:08+00:00'
category: webclip
summary: 'Describes the API Gateway and Backends for Frontends patterns for microservices, explaining why clients need them, how they work, and their benefits and drawbacks.'
tags: ["microservices", "api-gateway", "architecture", "backend-for-frontend"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Microservices Pattern: Pattern: API Gateway / Backends for Frontends"
    url: "https://microservices.io/patterns/apigateway"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/microservices-io--microservices-pattern-api-gateway-and-bff.md"
    kind: repo
---

The text presents the API Gateway pattern for microservices, using an online store’s product details page as an example where data is spread across many services. It explains that clients such as web browsers, mobile apps, and third-party consumers often need aggregated and client-specific data, face different network constraints, and should not deal with dynamic service locations or heterogeneous protocols. An API gateway becomes a single entry point that either routes requests directly to services or calls multiple services to assemble responses, and it can expose tailored APIs per client type and handle concerns such as security.

A variation called Backends for Frontends (BFF) assigns a distinct gateway to each type of client (web, mobile, external), letting each gateway provide an interface tuned to that client’s needs. The text lists benefits such as hiding service partitioning and locations, reducing round-trips, simplifying clients, and translating protocols, but also highlights added complexity and a potential extra network hop. It mentions implementation and integration concerns, including scaling with reactive/event-driven technologies, service discovery, authentication with access tokens, use of circuit breakers, and API composition, and points to examples like the Netflix API gateway and a Spring Cloud Gateway implementation.

## Reading notes

- Example scenario is an online store using microservices, where a product details page must be implemented for multiple UIs: HTML5/JavaScript for browsers and native Android/iPhone clients via REST.
- The store must also offer product details through a REST API for third-party applications.
- A product details page can require many kinds of data, illustrated with an Amazon book page: basic info, purchase history, availability, buying options, related items, customer reviews, and seller ranking.
- Because the application uses microservices, product information is split across several services, such as Product Info, Pricing, Order, Inventory, and Review services.
- The product details UI code has to retrieve data from all these services, which raises the question of how clients should access them.
- The core problem is how clients of a microservices-based application access individual services.
- One force is that microservice APIs are usually fine-grained, so clients often need to call multiple services to get all required data, as with product details.
- Different clients need different sets and levels of detail in the data; for example, the desktop product page is usually more elaborate than the mobile version.
- Network performance varies by client type: mobile networks are slower and higher latency than non-mobile networks, and any WAN is slower than a LAN.
- A server-side web application runs on a LAN and can make multiple backend calls without hurting user experience, while a mobile client can only afford a small number of requests.
- The number of service instances and their host/port locations change dynamically over time.
- The way the system is partitioned into services can evolve and should be hidden from clients.
- Services may use diverse, not always web-friendly protocols, which clients should not have to handle directly.
- The proposed solution is to implement an API gateway that acts as a single entry point for all clients.
- The API gateway can simply proxy or route some requests to the appropriate service.
- For other requests, the gateway can fan out to multiple backend services and combine their responses.
- Instead of a single uniform API, the gateway can present different APIs for different clients, with client-specific adapter code providing the best-suited interface.
- The Netflix API gateway is cited as an example where client-specific adapters deliver tailored APIs for differing client requirements.
- The API gateway may also implement security, including verifying that a client is authorized for a given request.
- The Backends for Frontends variation defines a separate API gateway per client type.
- In the BFF example, there are three client types: web application, mobile application, and external third-party application.
- Each client type has its own API gateway, and each gateway exposes an API customized for its particular client.
- Example implementations include the Netflix API gateway and a simple Java/Spring API gateway from a Money Transfer example application.
- One benefit is that the gateway shields clients from how the application is partitioned among microservices.
- Another benefit is that it hides the complexity of discovering the current locations of service instances from clients.
- The gateway can provide an optimal API for each client, aligned with that client’s specific needs.
- It reduces the number of client-to-server requests and round-trips by allowing a client to fetch data from multiple services in a single call.
- Fewer requests decrease overhead and improve user experience, and an API gateway is described as essential for mobile applications.
- The gateway simplifies client implementations by taking over the logic required to call multiple backend services.
- It can translate from a standard, web-friendly public API protocol to whatever internal protocols services use.
- One drawback is increased complexity, since the API gateway itself is another component to develop, deploy, and manage.
- Another drawback is potential increased response time because every request passes through an extra network hop via the gateway.
- The text notes that for most applications the cost of this extra round-trip is small.
- Implementation issues include choosing how to build the API gateway, with an event-driven or reactive approach suggested for high scalability.
- On the JVM, NIO-based libraries such as Netty and Spring Reactor are mentioned as suitable options, and NodeJS is given as another choice.
- The Microservice architecture pattern is described as creating the need for the API gateway pattern.
- The gateway must use either client-side discovery or server-side discovery to route requests to available service instances.
- The API gateway may handle user authentication and pass an access token with user information to downstream services.
- It will often use a circuit breaker mechanism when invoking services to improve reliability.
- An API gateway frequently implements the API Composition pattern to assemble data from multiple services.
- The Netflix API gateway is listed as a known use of this pattern.
- An example application is an API Gateway in the author’s microservices sample, built with Spring Cloud Gateway.
