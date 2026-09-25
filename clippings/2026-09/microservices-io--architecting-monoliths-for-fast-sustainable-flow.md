---
url: "https://microservices.io/post/architecture/2024/08/21/architecting-monoliths-for-fast-flow.html?ref=dailydev"
captured_at: "2026-09-25T17:56:19+01:00"
title: "Architecting monoliths for fast, sustainable flow"
domain: "microservices-io"
---

[architecting](https://microservices.io/tags/architecting)   [fast flow](https://microservices.io/tags/fast%20flow)   [modular monolith](https://microservices.io/tags/modular%20monolith)   [deployment pipeline](https://microservices.io/tags/deployment%20pipeline)  

* * *

* * *

In a previous article [Dissecting ‘architecting for fast, sustainable flow’](https://microservices.io/post/architecture/2024/04/29/dissecting-architecting-for-fast-flow.html), I described how fast, sustainable flow requires an architecture with several key characteristics. In this article, which is based on my workshop [Architecting for fast, sustainable flow: enabling DevOps and Team Topologies](https://chrisrichardson.net/training-architecting-for-fast-flow.html) I’ll describe how to architect monoliths to achieve fast, sustainable flow.

## Architectural requirements for fast, sustainable flow [§](#architectural-requirements-for-fast-sustainable-flow)

As I previously described, fast flow is the continuous delivery of a stream of valuable changes to customers. Sustainable flow is ability to keep the application’s technology stack current. Fast, sustainable flow requires an architecture with several key characteristics:

*   **Team-sized elements** - in order to avoid cognitive overload, the architecture must consist of team-sized elements
*   **Loose (design-time) coupling** - loose coupling was identified by the Accelerate authors as a key enabler of high performance. It’s also a consequence of [Conway’s law](https://en.wikipedia.org/wiki/Conway%27s_law): loosely coupled teams (defined by Team Topologies) need a loosely coupled architecture.
*   **Testability** - the path from development to production must be a fast, automated deployment pipeline. An application must, therefore, be capable of being tested using automated tests. Those tests must be fast. Moreover, a developer must be able to run the tests on their local machine.
*   **Deployability** - the application must support fast, reliable, automated deployments.
*   **Observability** - the deployed application must emit a stream of telemetry - logs, metrics, and distributed traces - which is feedback to the developers about the behavior of application and its users. The telemetry is used to monitor the application’s health and diagnose problems. It’s also used to understand user behavior.
*   **Evolvability** - the architecture must support the continuous upgrading of the application’s technology stack.

## About the monolithic architecture [§](#about-the-monolithic-architecture)

The [monolithic architecture](https://microservices.io/patterns/monolithic.html) is an architectural style that structures the application as a single executable/deployable unit, e.g. a single WAR or executable file. Moreover, there’s a single code base with a single deployment pipeline.

![](https://microservices.io/i/posts/monolith-teams-subdomains.png)

A monolithic architecture is simpler than a microservice architecture. For example, operations can be implemented as ACID transactions. But unfortunately, for some applications, the monolithic architecture can be an obstacle to fast, sustainable flow. To understand why, let’s take a look at how well it satisfies the architectural requirements described earlier.

## Architecting monoliths for fast, sustainable flow [§](#architecting-monoliths-for-fast-sustainable-flow)

With careful design, a monolith architecture is able to satisfy some but not all of the architectural requirements for fast, sustainable flow. Let’s look at the details starting with the biggest drawback of the monolithic architecture: poor evolvability.

### Evolving a monolith’s technology stack is challenging [§](#evolving-a-monoliths-technology-stack-is-challenging)

Sadly, one inherent limitation of the monolithic architecture is that evolving the technology stack can be challenging. Because a monolith has a single technology stack, you must upgrade the entire technology stack at once. While tools such as [OpenRewrite can automate some upgrades](https://microservices.io/post/architecture/2024/08/06/eliminating-tedium-with-openrewrite.html), upgrading a large code base is often a massive task that spans multiple teams. It’s difficult to schedule since it disrupts feature delivery. There are also limited opportunities to experiment with new technologies.

### Monoliths are mostly observable [§](#monoliths-are-mostly-observable)

Observability is mostly unrelated to the architecture style. A monolith can be instrumented so that it emits a stream of telemetry. One inherent limitation, however, is that the telemetry is for the entire application. You cannot, for example, see the resource consumption of an individual subdomain.

### Creating a loosely coupled monolith requires careful design [§](#creating-a-loosely-coupled-monolith-requires-careful-design)

To achieve fast flow the monolith must be structured as a collection of loosely (design-time) coupled, team-sized elements (e.g. modules). Loose (design-time) coupling requires elements to resemble [icebergs](https://microservices.io/post/architecture/2023/03/01/geometry-of-microservices.html). Each element must have small, stable API that encapsulates the much larger implementation.

![](https://microservices.io/i/posts/geometry/iceberg.png)

Unfortunately, however, the traditional monolithic architecture is a technically-oriented, layered architecture, which does not meet these requirements. The layers of a large application’s layers not team-sized. Teams typically work across multiple layers. And to make matters worse, the layers are typically not loosely coupled. Careful design is required to structure the monolith as a collection of loosely coupled, team-sized modules.

### Creating a testable and deployable monolith requires careful design [§](#creating-a-testable-and-deployable-monolith-requires-careful-design)

Designing a monolith that is loosely coupled is not the only challenge. The monolith consists of a single code base and a single deployment pipeline. As a result, the deployment pipeline is potentially a bottleneck and an obstacle to fast flow.

That’s because the larger the code base, the longer the deployment pipeline’s execution time. And to make matters worse, the larger the engineering organization the higher the rate of Git pushes. As a result, Git commits either wait in the deployment pipeline’s queue, which delays feedback, or are batched, which makes it more difficult to troubleshoot production issues.

The throughput of a single deployment pipeline is limited. But, you can minimize its execution time and increase its throughput through careful design. You must use a combination of physical design techniques, and testing strategies, to minimize the deployment pipeline’s execution time.

## Want to learn more? [§](#want-to-learn-more)

As you can see, architecting monoliths for fast flow requires careful design. If you want to learn how to design a fast flow architecture, enroll in my [upcoming public online workshop on architecting for fast, sustainable flow](https://chrisrichardson.net/training-architecting-for-fast-flow.html).

You will learn:

*   Architectural requirements for fast, sustainable flow.
*   The forces that shape an architecture and the trade-offs that you will need to make when designing an architecture.
*   How to decide between the monolithic and microservice architectural styles.
*   How to design a loosely coupled monolith.
*   Physical design techniques and testing strategies to accelerate the deployment pipeline.
*   How to design a microservice architecture.

## Need help with modernizing your architecture? [§](#need-help-with-modernizing-your-architecture)

I help organizations modernize their architecture to enable fast flow and GenAI-powered software delivery. If you’re planning or struggling with a modernization effort, I can help.

[Learn more about my modernization and architecture advisory work →](https://chrisrichardson.net/)
