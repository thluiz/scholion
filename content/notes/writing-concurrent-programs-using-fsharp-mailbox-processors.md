---
title: "Writing Concurrent Programs Using F# Mailbox Processors"
date: '2017-06-26T11:20:00-03:00'
category: webclip
summary: 'The article explains F# mailbox processors through the actor model, then shows basic posting, replies, scanning, and a coordinator-worker setup that measures workload and charts per-agent results.'
tags: ["fsharp", "concurrency", "actor-model", "mailbox-processors"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Writing Concurrent Programs Using F# Mailbox Processors"
    url: "http://www.codemag.com/article/1707051"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2017-06/codemag-com--writing-concurrent-programs-using-fsharp-mailbox-processors.md"
    kind: repo
---

The article presents F# mailbox processors as F#’s built-in message-based concurrency mechanism and explains them through the actor model. It shows how a mailbox processor receives messages asynchronously, how replies work with AsyncReplyChannel, how Scan can prioritize messages in the inbox, and how these pieces combine in a coordinator-worker example that distributes jobs and tracks workload.

## Reading notes

- F# mailbox processors are presented as the built-in way to handle message-based concurrency.
- The actor model is described as the theory behind mailbox processors, with lightweight actors that receive and process messages.
- The terms actor, mailbox processor, and agent are treated as interchangeable for most uses.
- A first mailbox processor is started with .Start, receives messages with inbox.Receive, and processes them in a loop.
- Message types are often declared explicitly, though that is described as optional.
- Replying uses AsyncReplyChannel together with PostAndReply or PostAndAsyncReply.
- Scan can look through the inbox for matching messages and process them ahead of others.
- In the scanning example, messages saying "Hello!" are prioritized over other queued messages.
- The longer example builds a coordinating agent and four worker agents.
- Workers request jobs from the coordinator, sleep for the job length, and then request another job.
- The coordinator keeps an internal queue of jobs and replies to workers with the next job length.
- The coordinator first waits for four Ready messages before handling job requests.
- A separate sorting agent groups per-worker job data into separate ResizeArrays.
- The final chart uses compiled cumulative job lengths to compare agents by number of jobs and total time.
