---
title: "Handling failures in background workers with Elixir and supervisors"
date: '2020-08-26T19:31:20+00:00'
category: webclip
summary: 'The article shows how a worker that can raise during payment verification may restart too often and bring down the app, and how a separate supervisor with tuned restart limits keeps the rest of the system up.'
tags: ["elixir", "supervisors", "background-workers"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Handling failures in background workers with Elixir and supervisors"
    url: "https://patrykbak.com/2020/07/07/handling-failures-in-background-workers-with-elixir-and-supervisors.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/patrykbak-com--handling-failures-in-background-workers-with-elixir-and-supe.md"
    kind: repo
---

The article explains that an Elixir system can still fail when a background worker raises an error. In the example, a payment worker checks whether a driver is being paid more than allowed, and a bad release can make that verification raise and trigger restarts.

To keep the rest of the application running, the article proposes placing the worker under its own supervisor instead of under the main one. That supervisor uses a restart limit based on the worker interval, and the main supervisor watches the worker supervisor rather than the worker directly.

## Reading notes

- Elixir runs on the Erlang VM and supports highly available systems, but that does not remove the need to plan for failures.
- The example worker pays drivers in the background by fetching completed jobs, calling `Payment.pay_the_driver/1`, and deleting paid jobs in a transaction.
- `Payment.pay_the_driver/1` compares the amount to be paid with the amount already paid, and `verify_payment/1` raises if the payment is over the limit.
- If `verify_payment/1` raises, the worker is restarted by its supervisor.
- With the default supervision behavior, too many restarts in five seconds can make the main supervisor crash too.
- The proposed fix is to add a separate supervisor for the worker so the rest of the application can stay up while the issue is investigated.
- The worker interval is exposed through a public `interval()` function so the supervisor can calculate an appropriate restart limit.
- The worker supervisor is configured with a `max_restarts` value that allows the periodic worker to restart without crashing the supervisor.
- The main supervisor is changed to supervise the worker supervisor instead of the worker itself.
- The closing point is that temporary failures are hard to avoid, so the system needs a plan for what happens when part of it stops working correctly.
