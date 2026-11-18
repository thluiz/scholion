---
title: "Dependency Injection in Crystal"
date: '2019-07-30T02:35:30+00:00'
category: webclip
summary: 'The article shows how DI in Crystal and Athena makes code easier to test, extend, and reuse through manager objects, swappable writers, and shared request-scoped data.'
tags: ["dependency-injection", "crystal", "athena"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Dependency Injection in Crystal"
    url: "https://dev.to/blacksmoke16/dependency-injection-in-crystal-2d66"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--dependency-injection-in-crystal.md"
    kind: repo
---

The article presents dependency injection as a way to make Crystal applications easier to test, more flexible, and less tied to concrete classes. It walks through three uses: managing multiple partner instances, swapping writer implementations through abstractions, and sharing current-user data across services in the same request.

## Reading notes

- DI is described as a tool for making applications easier to test, more expandable, and more flexible.
- The article uses Crystal and Athena, and notes that Athena’s DI component is also available as a standalone shard.
- In the manager example, a `PartnerManager` resolves a partner ID into a `Partner` instance, which lets new partners be added by registering another service.
- The manager approach keeps partner-specific logic out of the controller and avoids hard-coding an array of partner objects.
- In the plug-and-play example, a `Worker` depends on a `WriterInterface` instead of a concrete writer class.
- When there are multiple writers, the article shows two resolution options: a service alias for the default implementation or the initializer argument name to pick a specific service.
- DI is used to support testing by injecting a mock writer into `Worker` so the class can be tested in isolation.
- The article says this approach lets services depend on abstractions and makes it easier to reuse services that have a single responsibility.
- In the sharing-data example, a `UserStorage` service holds the current user, and a `SecurityListener` sets that user during request handling.
- The listener also adds log context with the user’s information, so later logs in the same fiber include that data.
- The article notes that the DI container is fiber-specific, which makes per-request sharing possible without manual cleanup.
- It contrasts this with storing `current_user` on `HTTP::Server::Context`, using a class variable, or storing the user in a database, and argues those options are less flexible in some scenarios.
- The conclusion says DI reduces coupling, improves testing, and encourages reuse, but should be applied where the problem fits.
