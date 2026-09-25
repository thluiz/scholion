---
url: "https://theburningmonk.com/2024/12/cohesion-vs-coupling/?ref=dailydev"
captured_at: "2026-09-25T21:16:41+01:00"
title: "Cohesion vs. Coupling"
domain: "theburningmonk-com"
---

![](https://res.cloudinary.com/theburningmonk/image/upload/f_auto,c_scale,w_90/theburningmonk.com/mugshot.png)

[

Yan Cui

](https://theburningmonk.com/about)

I help clients go faster for less using serverless technologies.

[![](https://theburningmonk.com/wp-content/uploads/2024/03/connect-the-dots-variant-3-1.png)](https://productionreadyserverless.com/?utm_campaign=connect-the-dots&utm_source=blog&utm_medium=image-banner&utm_content=variant3)

“High cohesion, low coupling” is one of the most misunderstood principles in software engineering.

So, let’s clear things up!

### TL;DR

Cohesion is about the internal focus of a thing – how well its components work together to fulfil a single purpose.

Coupling is about the external relationships between things – how much they depend on one another.

### Cohesion

When applied to a code module, cohesion measures how closely related its functions are.

An _Authenticator_ module will likely have high cohesion because all its functions are related to handling authentication.

On the other hand, a _Utils_ module is likely a dumping ground for unrelated helper functions and will, therefore, have low cohesion.

When applied to a system, cohesion measures how well its components (services, subsystems, etc.) work together to achieve a single goal.

![](https://theburningmonk.com/wp-content/uploads/2024/12/img_676f5e8766ee6.png)

A service with well-defined boundaries and responsibilities will have high cohesion.

Conversely, a system has low cohesion if its components are poorly aligned and have overlapping or unrelated responsibilities. For example, a User service that handles authentication, account management and sending notifications about account updates.

### Coupling

A good way to think about coupling is in terms of change propagation. That is, how much does System B need to change if we change System A.

![](https://theburningmonk.com/wp-content/uploads/2024/12/img_676f5f033b41a.png)

Coupling is everywhere and comes in [many different forms](https://www.enterpriseintegrationpatterns.com/ramblings/coupling_facets.html).

Some coupling (e.g. data format dependency) requires coordinated changes between systems.

Other forms of couplings are less obvious but more problematic to deal with.

For example, temporal coupling links the availability of one service to another. This often leads to cascade failures and necessitates other practices (e.g. retries, exponential backoff, fallbacks, chaos engineering and so on) to mitigate.

![](https://theburningmonk.com/wp-content/uploads/2024/12/img_676f5f47a611f.png)

So there you have it, the difference between “Cohesion” and “Coupling”.

They measure similar but, ultimately, different qualities in software.

Hope you learn something new!

**Whenever you’re ready, here are 3 ways I can help you:**

1.  [**Production-Ready Serverless**](https://productionreadyserverless.com/?utm_campaign=3-ways-I-can-help&utm_source=blog&utm_content=text-link): Join 20+ AWS Heroes & Community Builders and 1000+ other students in levelling up your serverless game. This is your one-stop shop for **quickly levelling up your serverless skills**.
2.  I help clients **launch product ideas**, **improve their development processes** and **upskill their teams**. If you’d like to work together, then let’s [**get in touch**](https://theburningmonk.com/hire-me/).
3.  [**Join my community on Discord**](https://discord.gg/Ucc9nZBA8H), ask questions, and join the discussion on all things AWS and Serverless.
