---
title: "gRPC: 5 Years Later, Is It Still Worth It?"
date: '2026-09-25T17:12:54+01:00'
category: webclip
summary: 'The author says gRPC remained the right choice for Torq because it preserved compatibility, enforced standards, and shared generated code, while Buf, BSR, ConnectRPC, and Linkerd improved the stack.'
tags: ["grpc", "protobuf", "buf", "service-mesh"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "gRPC: 5 Years Later, Is It Still Worth It?"
    url: "https://kostyay.com/grpc-5-years-later-is-it-still-worth-it-b181a3b2b73b"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/kostyay-com--grpc-5-years-later-is-it-still-worth-it.md"
    kind: repo
---

The author looks back on five years using gRPC at Torq and says the decision to standardize on gRPC and Protobuf paid off. The main reasons were backward compatibility, lint-based standards, shared generated code for clients and servers, and built-in middleware for authentication, authorization, and observability.

He also says the ecosystem improved a lot since then. Buf simplified code generation and dependency management, BSR made proto sharing and API evolution easier, ConnectRPC offers a better frontend option than gRPC-web, and Linkerd solves service-to-service load balancing for gRPC in Kubernetes.

## Reading notes

- The team chose to avoid OpenAPI/Swagger with Go because earlier experience at Luminate showed weak tooling and inconsistent client generation.
- Torq committed to gRPC and Protobuf for service communication.
- Choosing gRPC as the only communication protocol helped keep backward compatibility as the system changed.
- Linting was used to enforce standards and keep code quality consistent.
- Clients and servers use the same generated code, which reduces mismatches.
- Shared code also supports standardized authentication, authorization, and observability middleware.
- The author would still choose gRPC for a new project.
- Buf improved the gRPC ecosystem and the overall tooling experience.
- Early gRPC work required using protoc directly, which had a steep learning curve.
- The team wrapped protoc in a Docker container so engineers could generate Go or TypeScript assets with one command.
- Today, buf generate replaces much of that setup with buf.yaml and buf.gen.yaml.
- Buf Schema Registry helps manage Protobuf APIs, dependencies, compatibility, client generation, and documentation.
- Proto reuse across repositories was difficult before BSR and sometimes required protodep.
- In the frontend, gRPC-web is harder to debug because traffic is encoded in base64 and does not work well with the browser Network Inspector.
- gRPC-web also needs backend translation to regular gRPC, and the setup can affect security checks and caching.
- ConnectRPC is presented as an alternative that supports grpc-web and its own JSON protocol with caching.
- Kubernetes load balancing is not effective out of the box with gRPC because HTTP/2 keeps one long-lived connection pinned to a pod.
- The team uses Linkerd for proper gRPC load balancing, top-line metrics, mTLS, and traffic authorization.
- The final recommended stack is buf.build, BSR, gRPC over Linkerd for service-to-service communication, and ConnectRPC with JSON payloads for frontend to backend.
