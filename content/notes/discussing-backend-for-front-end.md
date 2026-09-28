---
title: "Discussing Backend For Front-end"
date: '2022-07-26T14:27:44-03:00'
category: webclip
summary: 'The post explains why mobile clients and microservices make over-fetching expensive, and presents Backend For Front-end as a client-specific layer that fetches, filters, aggregates, and returns the needed data.'
tags: ["backend-for-front-end", "microservices", "api-gateway"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Discussing Backend For Front-end | Foojay.io Today"
    url: "https://foojay.io/today/backend-for-front-end/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-07/foojay-io--discussing-backend-for-front-end.md"
    kind: repo
---

The post argues that simple webapp architectures break down when mobile clients and multiple integrations need different data shapes. Returning everything is inefficient because clients have limited screens and bandwidth, while microservices make client-specific filtering costly across many services and many client types.

BFF is presented as a dedicated layer that fetches data from the needed microservices, extracts only what matters, aggregates it, and returns it in the format each client needs. The same team owns the client and its BFF, and the implementation can be a separate deployment unit or part of an API gateway.

## Reading notes

- Mobile clients and integrations increase architectural complexity because each client needs a different subset of data.
- Over-fetching is a poor fit for phones because screen space and bandwidth are limited.
- With microservices, making every service adapt responses for every client becomes expensive and hard to manage.
- BFF moves filtering and aggregation into a dedicated layer between clients and microservices.
- The team responsible for the front-end is also responsible for its BFF.
- A BFF can be deployed separately or implemented inside an API gateway configuration.
- BFF reduces coupling between microservices and clients, although it adds system complexity.
