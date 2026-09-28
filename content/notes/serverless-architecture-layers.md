---
title: "Serverless Architecture Layers"
date: '2022-04-12T15:10:12-03:00'
category: webclip
summary: 'The article proposes five serverless architecture layers for enterprises: experience, cross-cutting, domain, data, and platforms. It argues that clear boundaries, versioned interfaces, and shared governance reduce duplicated logic, cognitive load, and distributed monoliths.'
tags: ["serverless", "enterprise-architecture", "domain-driven-design", "platforms"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Serverless Architecture Layers 🚀 | by Lee James Gilmore | Apr, 2022 | Level Up Coding"
    url: "https://levelup.gitconnected.com/serverless-architecture-layers-a9dc50e9b342"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-04/levelup-gitconnected-com--serverless-architecture-layers.md"
    kind: repo
---

The article maps serverless systems to five layers for enterprise use: experience, cross-cutting, domain, data, and platforms. It argues that these layers help keep business logic inside domains, keep thin APIs stateless, and make shared concerns, events, and infrastructure easier to govern across teams.

## Reading notes

- The article recommends thinking about serverless architecture as a set of patterns, templates, and guardrails to avoid lambda pinball, duplicated business logic, and a distributed monolith.
- It connects the approach to Eric Evans’ domain-driven design and uses a fictitious company, Lee James Mountain Wear, to show what happens when teams do not follow the layering approach.
- The experience layer combines presentation and application concerns, such as micro-frontends, websites, mobile apps, Alexa apps, and thin BFF APIs.
- Thin APIs in the experience layer should coordinate work through the domain layer and should not contain shared business logic.
- The article says different experiences may need different authentication methods, such as Azure AD SSO for an internal app and Cognito for mobile or Alexa apps.
- The cross-cutting layer covers shared concerns such as component libraries, email and SMS sending, logging, tracing, and authentication.
- The article warns that if cross-cutting concerns are not handled early, teams will repeat the same work, choose different SaaS products, and raise cognitive load.
- The domain layer is presented as the most important layer, responsible for business concepts, business situation, and business rules.
- Domain services should use well-defined, versioned APIs and events, often through private APIs, Lambda or Fargate, DynamoDB, EventBridge, and schema registry support.
- The domain internals should stay encapsulated so other teams do not reach directly into data stores, queues, or topics.
- The data layer groups the enterprise service bus, reporting and BI, and data storage, with examples such as EventBridge or MSK, QuickSight and Athena, and Redshift or S3 data lakes.
- The article says an enterprise service bus helps teams coordinate through versioned events, and it can support reporting and aggregation of events into data lakes.
- The platforms layer corresponds to infrastructure in the book and covers authentication platforms, pipelines and accounts, security, and API and event definitions.
- The article argues that platforms should remove differentiated heavy lifting so teams can move faster and use shared templates and reference architectures.
