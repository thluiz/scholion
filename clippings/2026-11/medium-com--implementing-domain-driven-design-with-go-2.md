---
url: "https://medium.com/@TonyBologni/implementing-domain-driven-design-and-hexagonal-architecture-with-go-2-efd432505554"
captured_at: "2026-11-16T05:56:06+00:00"
title: "Implementing Domain-Driven Design with Go (2) | Medium"
domain: "medium-com"
---

Member-only story

Domain Driven Design
Golang
Aggregates
Value Objects
Domain Events
Implementing Domain-Driven Design and Hexagonal Architecture with Go (2)
Part 2 — How I implement tactical DDD patterns — the Domain layer
Anton Stöckl
19 min read
·
May 4, 2020

Also, see:

Part 1 — Introduction to the domain, the bounded context, and the business use-cases

Disclaimer

Target audience for the articles in this series are people who are interested in Domain-Driven Design and Go with any knowledge level. I try to highlight where I deviate from idomatic Go or do things differently than in usual Go projects. In general I consider higher level concepts like Domain-Driven Design and Hexagonal Architecture to be “stronger” than “how most people implement things” in a programming language. Still I am always trying to balance both concerns and try to find a good compromise in cases. I will also describe simpler alternatives where applicable.

If you are religious about idiomatic Go and are not interested in different ways of doing things in Go — especially going the extra mile for defensive code and separation of concerns like Domain and Infrastructure — the articles in this series might not be for you!

Please be aware that the solutions I picked are just my decisions for the implementation of this playground project. I don’t want to suggest this as a…
