---
title: "Web Service Integrations Using Hangfire in ASP.NET Core"
date: '2020-10-30T08:38:06-03:00'
category: webclip
summary: 'The post shows how to split an incoming and outgoing web service integration into synchronous validation and async Hangfire jobs, so RPC work becomes retryable, durable, and non-blocking.'
tags: ["hangfire", "asp-net-core", "web-service-integration", "async-jobs"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Web Service Integrations Using Hangfire in ASP.NET Core"
    url: "https://www.michaelgmccarthy.com/2016/12/09/web-service-integrations-using-hangfire-in-asp-net-core/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-10/michaelgmccarthy-com--web-service-integrations-using-hangfire-in-asp-net-core.md"
    kind: repo
---

The post argues that RPC-style web service work should be broken into smaller steps instead of handled in one synchronous controller action. Basic field validation stays synchronous, while database-heavy checks and outbound callbacks move into Hangfire jobs so the caller can get a quick 202 response.

## Reading notes

- The article treats RPC-style communication as something that needs careful handling because network calls and distributed systems can fail in transient ways.
- True asynchronicity is framed as using a queue or service bus with durable storage, not just using async and await.
- Hangfire is presented as a way to run fire-and-forget, scheduled, or recurring jobs with SQL Server durability and retry support.
- For incoming requests, basic model validation and a status check happen synchronously and return 400 when they fail.
- Duplicate request detection is also kept synchronous because the sender cannot be notified later about that kind of failure.
- The request import itself is moved to a Hangfire job through IBackgroundJobClient.Enqueue, which lets the controller return 202 immediately.
- The job that creates the Request entity is written to be idempotent because Hangfire may retry it.
- After the request is stored, a notification handler decides whether the request is serviceable and enqueues another job for the outbound callback.
- The outbound job uses HttpClient and EnsureSuccessStatusCode so failures can be retried by Hangfire.
- The final flow separates inbound processing, internal work, and outbound status updates into multiple transactions instead of one long synchronous operation.
