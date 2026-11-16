---
title: "Decomposing domain models based on lifecycles"
date: '2020-07-05T14:10:30+00:00'
category: webclip
summary: 'The article argues that an anemic model makes business rules implicit and hard to test, and proposes splitting a domain model by lifecycle stage, then reconnecting the pieces through an application layer or PubSub.'
tags: ["software-design", "domain-model", "modularity"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Decomposing domain models based on lifecycles"
    url: "https://mkaszubowski.com/2020/06/24/decomposing-models-lifecycle.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/mkaszubowski-com--decomposing-domain-models-based-on-lifecycles.md"
    kind: repo
---

The article uses a logistics flow to show a decomposition strategy based on lifecycle stages. Instead of one large Shipment schema that holds bidding, payment, delivery, and cancellation states, it separates each phase into its own module so the code stays narrower and the rules for each step remain local.

## Reading notes

- A single schema with many fields and a state flag leads to an anemic domain model, where most business logic ends up in create and update operations.
- In that setup, unit tests need large fixtures, the code hides domain rules, and the schema grows as new features are added.
- Decomposing by lifecycle means modeling each step of the flow in isolation, such as bidding as one module and the later payment or delivery steps as others.
- The application layer can then connect these isolated domain modules into a complete flow, for example by authorizing a client, ending bidding, fetching the winning bid, and requesting payment.
- An event-driven or PubSub approach is another way to connect the pieces by passing events between modules.
- The article suggests watching for a state field, shifts in which actor the system interacts with, and nullable database fields that change from null to not null as signs that a model may need decomposition.
