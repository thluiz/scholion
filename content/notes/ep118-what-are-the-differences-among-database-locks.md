---
title: "EP118: What are the differences among database locks?"
date: "2026-09-23T18:46:15+01:00"
category: webclip
has_commentary: false
summary: "A five-topic system design refresher: database lock types, six pagination techniques, MVC-family architecture patterns, what happens on a URL request, and QR code payments."
tags:
  - system-design
  - databases
  - api-design
  - software-architecture
sources:
  - title: "EP118: What are the differences among database locks?"
    url: "https://blog.bytebytego.com/p/ep118-what-are-the-differences-among?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/blog-bytebytego-com--ep118-what-are-the-differences-among-database-locks.md"
    kind: repo
---

A ByteByteGo weekly refresher covering five unrelated system design topics in quick succession: database lock types, pagination technique tradeoffs, the MVC family of UI architecture patterns, the sequence of events behind a URL request, and how QR code payments move between merchant, payment gateway, and consumer wallet.

## Fichamento

- Database locks: shared locks allow concurrent reads, exclusive locks block all other access, update locks prevent deadlocks during an intended update, and separate lock types exist for schema, bulk inserts, key ranges, rows, pages, and whole tables.
- Pagination techniques compared on tradeoffs: offset-based is simple but slow on large offsets, cursor-based and keyset-based scale better but add implementation complexity, page-based mirrors offset's weaknesses, time-based suits time-ordered data, and hybrid approaches combine techniques for flexibility.
- MVC, MVP, MVVM, MVVM-C, and VIPER all share a view for display and input and, except VIPER, a model for business data. They differ in the translator between the two: controller, presenter, or view-model (entity, in VIPER), each proposed to make that translator layer more maintainable than the last.
- A URL request breaks into DNS lookup (cached at browser, OS, network, and ISP layers before falling back to a recursive lookup), a TCP connection to the resolved IP, an HTTP request/response exchange, and final HTML rendering.
- QR code payments split into two sequences: the merchant side generates and stores an order ID with the payment service provider, gets back a QR code, and displays it, all in under a second; the consumer side scans, confirms, and pays, after which the payment gateway marks the code paid and notifies the merchant.
