---
title: "An Alternative to Outbox Pattern for Microservices Architecture"
date: '2022-05-31T17:35:31-03:00'
category: webclip
summary: 'The article proposes a 2-phase message built on DTM as an alternative to Outbox. It uses Prepare and Submit plus a check-back service to keep business execution and message submission atomic.'
tags: ["microservices", "outbox-pattern", "distributed-transactions", "dtm"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "An Alternative to Outbox Pattern for Microservices Architecture | by dtm | Apr, 2022 | Better Programming"
    url: "https://betterprogramming.pub/an-alternative-to-outbox-pattern-7564562843ae"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-05/betterprogramming-pub--alternative-to-outbox-pattern-for-microservices.md"
    kind: repo
---

The article proposes a 2-phase message pattern as an alternative to Outbox for distributed transactions in microservices. It is based on DTM rather than a message queue, and it targets the dual-writes problem by making business execution and message submission atomic.

## Reading notes

- It illustrates an inter-bank transfer where one balance is increased and another is decreased, and explains that a crash between the two updates leaves the system inconsistent.
- The 2-phase message uses `DoAndSubmitDB` to tie local business execution and message submission together, so both succeed or both fail.
- If the process crashes after the local business update but before submission, DTM later calls a check-back URL to query whether the local transaction committed.
- If the local transaction committed, DTM submits the global transaction and continues; if it rolled back, the global transaction fails and stops.
- The article contrasts this with Outbox, which needs a local message table, polling or CDC, and message consumption.
- It lists 2-phase message advantages as avoiding message queues, polling tasks, and message consumers, while supporting synchronous or asynchronous downstream calls.
- It says the check-back mechanism uses a separate table keyed by `gid`, with inserted reasons such as `COMMITTED` and `ROLLBACKED`, to determine transaction state.
- It also notes that a direct `Submit` call can replace the normal message pattern and support asynchronous work without a queue.
