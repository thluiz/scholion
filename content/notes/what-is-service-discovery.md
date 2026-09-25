---
title: "What Is Service Discovery?"
date: '2026-09-25T21:18:19+01:00'
category: webclip
summary: 'The article explains service discovery as the process of finding healthy service instances in a microservice system, compares implementation options, and recommends using a replicated service registry for scalable setups.'
tags: ["service-discovery", "microservices", "service-registry", "load-balancing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "What Is Service Discovery?"
    url: "https://systemdesign.one/what-is-service-discovery/?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/systemdesign-one--what-is-service-discovery.md"
    kind: repo
---

Service discovery is presented as the mechanism that lets service consumers find the current locations of service provider instances in a microservice architecture. The article frames it around dynamic service locations, runtime endpoint resolution, registration on startup, deregistration on shutdown, and health checks for reliability.

## Reading notes

- Microservices communicate over the network, so service location and binding have to be identified before a consumer can interact with a provider instance.
- The core requirements listed are CRUD on service information, search, a RESTful API, service-level checks, high availability, low memory and CPU footprint, reliability, and low latency.
- A service registry stores service locations and provides runtime service endpoint resolution.
- Service instances register on startup and deregister on shutdown; missing heartbeats can mark an instance as dead.
- The article describes REST or RPC APIs for the registry, including PUT for registration, DELETE for deregistration, and GET for fetching service instances.
- The data model should stay flexible, with metadata extended through key-value pairs.
- Pub-sub can be used so registry changes are pushed to subscribed consumers.
- Hard-coding service locations does not scale and tightly couples consumers to providers.
- External configuration files are simple but do not scale well and make heartbeats harder to implement.
- DNS works at large scale and has replication and cache support, but it handles only static service instances and can serve stale data.
- Load balancers add another hop, complexity, and a possible single point of failure.
- The article recommends building service discovery with a service registry in scalable microservice architectures.
- Client-side service discovery has lower latency and better fault tolerance through cached service information, but it increases client complexity.
- Server-side service discovery keeps consumers loosely coupled, while the load balancer looks up healthy instances in the registry and forwards the request.
- Zookeeper, Consul, Eureka, and Etcd are listed as common registry implementations, with different consistency models and APIs.
- Zookeeper uses ephemeral nodes and a filesystem-like API; Consul uses agents, servers, Raft, gossip, and can also expose DNS and HTTP interfaces.
- Eureka favors availability over consistency, caches the registry on the client, and relies on periodic heartbeats.
- Service registration can be done by self-registration or by a third party, with the tradeoff between lower system complexity and lower coupling.
