---
title: "Why I Built Things-Kit: A Spring Boot Alternative for Go"
date: '2025-10-22T11:19:51+01:00'
category: webclip
summary: 'The author explains how repetitive Go microservice setup led to Things-Kit, a modular framework on Uber Fx that packages configuration, logging, HTTP, database, cache, and lifecycle handling.'
tags: ["go", "microservices", "dependency-injection", "uber-fx"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why I Built Things-Kit: A Spring Boot Alternative for Go - DEV Community"
    url: "https://dev.to/noxymon/why-i-built-things-kit-a-spring-boot-alternative-for-go-3ip4?"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-10/dev-to--why-i-built-things-kit-spring-boot-alternative-go.md"
    kind: repo
---

The post presents Things-Kit as a modular microservice framework for Go that aims to bring a Spring Boot-like developer experience without abandoning Go’s emphasis on simplicity, explicitness, and composition. It grows out of repeated friction with setting up HTTP servers, dependency wiring, configuration, and shutdown logic in every new service.

## Reading notes

- The author says new Go microservices kept leading to the same setup work for server bootstrapping, dependency wiring, configuration, and graceful shutdown.
- Copying boilerplate between services produced divergent patterns, uneven error handling, and duplicated maintenance across more than 15 microservices.
- Spring Boot is held up as the model for a streamlined startup path, with conventions, escape hatches, and replaceable dependencies.
- The Go version of that idea had to avoid magic, reflection-heavy frameworks, and enterprise complexity.
- Uber Fx is presented as the dependency injection base because it uses Go’s type system and reflection to wire dependencies and lifecycle hooks.
- Things-Kit packages common patterns into reusable modules for configuration, logging, SQL/PostgreSQL, Gin HTTP, gRPC, Redis, Kafka, and testing utilities.
- The framework is described through five principles: modularity first, interfaces instead of concrete implementations, convention over configuration, no magic, and lifecycle awareness.
- The post shows a user-service example where business logic, HTTP handling, module wiring, and the main function are separated into small pieces.
- The author claims this reduces a service’s main file to about 10 lines while keeping dependency injection and graceful lifecycle management built in.
- The project is described as feature-complete for the initial release, with two production-like example projects already built.
- The post ends by asking for feedback on the approach, on future modules, and on how people handle dependency injection in their own Go projects.
