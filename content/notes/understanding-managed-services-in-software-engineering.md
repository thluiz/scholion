---
title: "Understanding Managed Services in Software Engineering"
date: '2025-07-17T03:10:51+00:00'
category: webclip
summary: 'The post contrasts managed and unmanaged infrastructure as a tradeoff between control and convenience, then uses IaaS, PaaS, and FaaS to frame how that choice affects cost, scaling, security, and team focus.'
tags: ["managed-services", "cloud-computing", "infrastructure", "iaas-paas-faas"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Understanding Managed Services in Software Engineering"
    url: "https://machine-learning-made-simple.medium.com/understanding-managed-services-in-software-engineering-606804469fa3"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-07/machine-learning-made-simple-medium-com--understanding-managed-services-in-software-engineering.md"
    kind: repo
---

The post presents managed and unmanaged infrastructure as a spectrum of responsibility and control. It links that choice to convenience, operational burden, scalability, security, and development speed, then places IaaS, PaaS, and FaaS on the same spectrum.

## Reading notes

- Unmanaged infrastructure gives the user control over hardware, network, operating system, middleware, runtime, data, and applications, but also full responsibility for maintenance, updates, security, and scaling.
- Managed infrastructure shifts responsibility to the provider, which lowers operational burden while reducing control over the environment.
- The post maps infrastructure choices to a broader convenience-versus-control spectrum.
- Moving from left to right on that spectrum means giving up control in exchange for convenience.
- The post links this shift to a move from CapEx toward OpEx, while noting that maintenance can increase OpEx when the team must handle everything.
- IaaS offers virtualized computing resources over the internet and gives engineers access to operating systems, network settings, and storage configurations.
- IaaS supports virtual machines, storage volumes, VPCs, and load balancers, but requires expertise in hardening, network security, and scaling.
- PaaS provides pre-configured environments for deployment, letting developers focus on code rather than infrastructure.
- PaaS abstracts away operating system management, patching, and some scaling concerns, while sometimes restricting versions, libraries, and deployment processes.
- The post treats platforms as a strong business model because they let other people build on top of what the company provides.
- FaaS and serverless computing let developers deploy individual functions that run on demand and scale automatically with traffic.
- FaaS is described as event-driven, stateless computing with pay-per-execution pricing.
- The post says unmanaged infrastructure is useful for performance optimization, strict compliance, and legacy system support.
- It also says unmanaged infrastructure brings operational complexity, performance tuning overhead, and a heavier security and compliance burden.
- Managed services are presented as useful for rapid deployment, automatic scaling, high availability, and built-in security features.
- The main drawbacks of managed services are vendor lock-in, some performance overhead, and limited visibility into the underlying infrastructure.
- The decision framework weighs application architecture, scalability needs, performance requirements, security and compliance, and team expertise.
- The post closes by saying that both approaches can be combined.
