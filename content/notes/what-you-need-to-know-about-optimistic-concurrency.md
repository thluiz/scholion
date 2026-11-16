---
title: "What You Need to Know About Optimistic Concurrency"
date: '2026-11-16T01:29:52+00:00'
category: webclip
summary: 'Explains optimistic concurrency as a way to detect conflicting updates after they happen, usually with version numbers or etags, and contrasts it with pessimistic concurrency and optimistic updating.'
tags: ["optimistic-concurrency", "version-numbers", "etag", "web-applications"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "What You Need to Know About Optimistic Concurrency"
    url: "https://dev.to/harri_etty/what-you-need-to-know-about-optimistic-concurrency-1g3l"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--what-you-need-to-know-about-optimistic-concurrency.md"
    kind: repo
---

Optimistic concurrency is presented as a way to handle simultaneous updates without locking records for long periods. The article uses a books order example to show how conflicting saves can overwrite each other, then explains that the system should detect the conflict and ask the user what to do.

## Reading notes

- The lost update problem happens when two people open the same record and make different changes, and the later save can overwrite the earlier one.
- Optimistic concurrency assumes these conflicts are uncommon, so it lets updates proceed and asks for a human decision when a conflict is detected.
- Pessimistic concurrency instead tries to prevent conflicts by locking the record while it is being updated.
- In web applications, long-lived locks are impractical because the app does not stay continuously connected to the server or database.
- Git merge conflicts are given as an example of optimistic concurrency, since multiple people can edit concurrently and conflicts are resolved at submit time.
- A common implementation uses version numbers or timestamps stored with each record and compared when an update is submitted.
- The example shows one request updating version 1 to version 2, while a second request with version 1 is rejected because the stored version has changed.
- DynamoDB conditional updates, Rails optimistic locking, CosmosDB _etag values, and HTTP ETag headers are listed as implementations or related mechanisms.
- On the frontend, a conflict can lead to a message asking the user to reload, or to a more interactive conflict-resolution flow.
- Optimistic concurrency is distinguished from optimistic updating, which updates the UI before the server confirms the database write.
