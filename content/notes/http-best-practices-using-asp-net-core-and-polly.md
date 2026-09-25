---
title: "HTTP Best Practices Using ASP.NET Core And Polly"
date: '2026-09-25T21:53:25+01:00'
category: webclip
summary: 'The page explains HTTP resiliency in ASP.NET Core with Polly, focusing on transient errors. It shows retry, circuit breaker, and bulkhead policies and how they are combined with HttpClientFactory.'
tags: ["asp-net-core", "polly", "httpclientfactory", "resiliency"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "HTTP Best Practices Using ASP.NET Core And Polly"
    url: "https://www.c-sharpcorner.com/article/http-best-practices-using-asp-net-core-and-polly/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/c-sharpcorner-com--http-best-practices-using-asp-net-core-and-polly.md"
    kind: repo
---

The page says HTTP resiliency should be designed during the SDLC to handle load, bugs, attacks, and component failures. For HTTP calls, it focuses on transient errors such as network failures, HTTP 5XX responses, and HTTP 408 timeouts, and it says Polly is used to express policies like retry, circuit breaker, timeout, bulkhead isolation, and fallback.

It then shows how to add Polly to a typed HttpClient with `Microsoft.Extensions.Http.Polly`, using `WaitAndRetryAsync(3, TimeSpan.FromSeconds(2))` for retries, `CircuitBreakerAsync(5, TimeSpan.FromSeconds(10))` for circuit breaking, and a bulkhead policy with parallelism and queue limits to reduce cascading failures.

## Reading notes

- Resiliency is presented as handling faults without crashing the application.
- The article limits the discussion to HTTP operations.
- Polly is introduced as the library used to implement resiliency policies.
- Transient errors listed are network failures, HTTP 5XX status codes, and HTTP 408.
- Retry is shown with three attempts and a two-second interval.
- The circuit breaker is described with closed, open, and half-open states.
- The sample circuit breaker opens after five failures and waits ten seconds before half-open.
- Bulkhead is used to limit concurrent work and queue actions.
- The bulkhead example sets max parallelism to 3 and max queued actions to 5.
- The conclusion says the series covered HttpClientFactory, named and typed clients, and resiliency patterns.
