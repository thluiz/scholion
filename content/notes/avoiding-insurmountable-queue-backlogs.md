---
title: "Avoiding insurmountable queue backlogs"
date: '2026-11-26T00:33:51+00:00'
category: webclip
summary: 'Article explains how Amazon designs multitenant asynchronous systems to prevent queue backlogs from becoming unrecoverable using metrics, traffic shaping, prioritization, sidelining, and backpressure.'
tags: ["distributed-systems", "queues", "backpressure", "aws"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Avoiding insurmountable queue backlogs"
    url: "https://aws.amazon.com/builders-library/avoiding-insurmountable-queue-backlogs/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/aws-amazon-com--avoiding-insurmountable-queue-backlogs.md"
    kind: repo
---

Amazon describes how queues, while improving durability and availability for asynchronous systems, can create large backlogs that dramatically extend recovery time after outages or load spikes. Using examples from AWS Lambda and AWS IoT Core, the article explains how Amazon measures availability and latency, identifies backlog risks in multitenant environments, and applies design patterns like shuffle-sharding, sidelining, rate limits, backpressure, and heartbeating to keep queue debt from becoming unrecoverable.

## Reading notes

- Queues increase durability and availability by persisting messages across failures and re-driving them until success, but this comes with extra latency due to retries.
- When processing stops but messages keep arriving, a queue can accumulate a large "message debt" that makes work complete too late to be useful.
- Queue-based systems show bimodal behavior: a fast mode with low latency and no backlog, and a slow mode where arrival rate exceeds processing rate, latency grows, and recovery can be lengthy.
- AWS Lambda uses durable internal queues for asynchronous invocations so it can retry executions without losing data when functions fail or dependencies are slow.
- AWS IoT Core uses PubSub with various persistence mechanisms so devices that go offline can later reconnect, catch up, and then receive subsequent messages.
- Many AWS asynchronous systems leverage SQS for durable, scalable, at-least-once delivery, with one component producing messages and another polling, processing, and deleting them.
- An hour-long outage that stops processing leads to an hour of doubled capacity needed after recovery, and dependent systems might not handle this surge, further stretching recovery time.
- Asynchronous services often appear tolerant of latency, but in practice many are expected to have subsecond processing; hidden risk arises when backlogs spike latency unexpectedly.
- Measuring availability for asynchronous systems is tricky: producer-side metrics mostly reflect the queue’s own availability rather than end-to-end success.
- Consumer-side availability can look worse than reality because failed deliveries may be retried and eventually succeed, hiding transient issues.
- Dead-letter queues (DLQs) capture messages that exhaust retries and provide a useful availability metric, but they reveal problems only after failures have accumulated.
- Producer-observed latency mainly shows queue service latency, so Amazon instead tracks the age of messages in the queue to detect when systems are falling behind.
- SQS includes message enqueue timestamps, letting consumers log and produce metrics on how long messages have been waiting before processing.
- Some backlogs are expected and acceptable, such as in AWS IoT where low-powered or intermittently connected devices may intentionally read slowly or go offline.
- AWS IoT introduced an AgeOfFirstAttempt metric, measuring time from enqueue to the first delivery attempt, to distinguish system-wide backlog from slow or offline devices.
- To further refine latency tracking in PubSub, AWS IoT uses AgeOfFirstSubscriberFirstAttempt, timing the first publish attempt to the first subscriber of a topic while other metrics track the remaining fan-out.
- Separating latency of first attempts from retry attempts is a common pattern at Amazon to get clearer early-warning signals of system-wide issues.
- Debugging asynchronous latency and availability is complicated by requests moving across servers and queues, so systems attach request IDs to messages and use tracing tools like X-Ray.
- Many asynchronous AWS services are multitenant, processing work for multiple customers, which complicates latency and availability guarantees while enabling higher resource utilization.
- Internal service queues are not exposed directly to customers; instead, lightweight APIs authenticate calls, annotate messages with caller info, and then enqueue them, similar to Lambda’s async invocation model.
- These APIs also support fairness by enforcing per-customer rate limits, sometimes with burst allowances, and scaling limits as customers grow.
- Fairness throttling in asynchronous systems is viewed as especially critical because unbounded spikes can quickly fill queues and create long-lasting backlogs.
- Without noisy neighbor protections, a single customer spike that goes unthrottled can build a backlog far larger than consumer capacity, leading to multi-hour recovery even for short surges.
- Amazon analyzes queueing behavior independently of compensating mechanisms like autoscaling, to design systems that remain robust even when multiple layers must cooperate.
- They emphasize protection at every layer in asynchronous systems, since backlogs can form behind admission control and front-door throttles.
- Using a single shared queue can conflict with multitenancy goals because once work is in that queue, isolating and prioritizing per-tenant workloads is difficult.
- Real-time systems often operate over FIFO-like queues but prefer to treat fresh messages preferentially, approximating LIFO behavior while relegating older data to background processing.
- One simple isolation pattern is giving each customer or workload its own queue so a single tenant’s spike does not delay others, though polling many queues can become expensive.
- Per-customer queues are practical only when there are few customers or adjacent systems; services with very large numbers of entities, like AWS IoT devices, cannot scale this approach.
- AWS Lambda adopts shuffle-sharding: it maintains a fixed set of queues and hashes each customer to a small subset, then enqueues into the least-loaded of those queues.
- With shuffle-sharding, a busy customer backs up only the queues in its shard, while other customers are automatically directed toward less loaded shards, giving useful isolation without per-customer queues.
- Some Amazon systems implement spillover queues where consumers throttle by customer; when a customer exceeds its configured rate, additional dequeued messages are moved to spillover queues and removed from the main queue.
- This spillover pattern lets the primary queue prioritize in-band traffic while still preserving excess messages to be processed later when resources free up.
- Similar sideline logic can be implemented on the producer side so that large bursts from one workload are queued separately and do not block other workloads on the main path.
- Systems can also sideline old messages: consumers check message age on dequeue and move very old messages to a backlog queue to focus main resources on fresher traffic.
- By quickly re-enqueuing older spike-era messages into a backlog queue, consumers free themselves to restore real-time service on new messages, approximating LIFO ordering.
- Some architectures allow dropping very old messages instead of sidelining them, especially when periodic full synchronization (anti-entropy sweepers) will eventually correct system state.
- In systems with periodic full sweeps, old delta messages that predate the most recent sweep can be safely discarded, reducing wasted effort on stale work.
- AWS IoT includes a rules engine that forwards device messages into customer-controlled destinations such as Elasticsearch or Kinesis, which can introduce latency beyond AWS’s control.
- If downstream customer-owned endpoints slow down while incoming message rates stay high, concurrency grows and can exhaust limited resources like threads.
- Little’s Law is used to reason about this: concurrency equals arrival rate multiplied by average latency, so sudden latency spikes can multiply concurrent work dramatically.
- For example, a server handling 100 messages per second with 100 ms latency uses about 10 threads; if latency jumps to 10 seconds, concurrency rises to around 1,000 threads, which may exhaust pools.
- To prevent thread exhaustion, AWS IoT’s rules engine uses non-blocking I/O and additional guards like semaphores that limit concurrency per workload.
- The rules engine also applies rate-based fairness limiting, automatically adjusting limits as workloads evolve, and uses its underlying queues as buffers between devices and scaled backend resources.
- Across Amazon services, separate thread pools per workload are used so one customer cannot consume all available threads.
- Systems maintain per-workload counters (for example, AtomicInteger) to cap concurrent work per tenant and apply rate-based throttling for shared rate-limited resources.
- When a workload causes an excessive backlog that consumers cannot process promptly, Amazon systems may push back by rejecting new work more aggressively at the producer side.
- Without backpressure, isolated workloads can silently accumulate day-long backlogs that are expensive to process and may have been unwanted in the first place.
- A straightforward backpressure design periodically measures per-workload queue depth (where isolation allows this) and dynamically tightens inbound throttles as backlogs grow.
- This per-workload backpressure becomes harder when multiple tenants share a single SQS queue, because SQS does not expose per-attribute or per-tenant queue depths.
- While total queue depth can still drive a general throttle, this would unfairly restrict all workloads sharing that queue, not just the noisy one.
- Other systems like Amazon MQ provide more granular backlog visibility, which makes targeted backpressure easier to implement.
- In some domains, like amazon.com order processing, applying strict backpressure is avoided; the system prefers to accept orders even if a backlog forms, then prioritize urgent work internally.
- When a system concludes that a workload’s throughput must be reduced, it can re-enqueue messages into a surge queue with SQS delay enabled so they remain hidden for a while.
- Delay queues let the system postpone less urgent or problematic work, freeing capacity to process fresher messages and giving backends time to recover.
- Some queue services such as SQS impose limits on the number of in-flight messages, meaning messages delivered but not yet deleted, distinct from unlimited total queued messages.
- Bugs that fail to delete messages after exceptions can inflate in-flight counts, as messages remain hidden until their VisibilityTimeout expires and then get redelivered.
- To avoid hitting in-flight limits, overload and error-handling strategies often move excess messages into secondary queues rather than leaving them visible or partially processed.
- With SQS FIFO queues, only the most recent unprocessed 20,000 messages are actively polled; if a subset of message groups accumulates more than that, fresher messages in other groups can be starved.
- Messages that can never be processed, for example due to input validation edge cases, add useless load; SQS DLQs automatically move repeatedly failing messages out of the main queue.
- Amazon alarms whenever messages appear in DLQs, treating them as indicators of bugs that require investigation and later reprocessing once fixed.
- To retain capacity for bursts, systems provision extra polling threads beyond what is strictly needed at steady state, avoiding states where polling threads are saturated.
- A monitoring signal for polling headroom is how often poll attempts return empty; if every poll yields work, the system either matches demand exactly or may lack enough polling capacity for spikes.
- When processing SQS messages, SQS grants a limited visibility window before assuming the consumer failed and redelivering the message to another consumer.
- If processing continues past the VisibilityTimeout without extension, multiple consumers may work on the same message concurrently, compounding overload.
- Amazon mitigates this by either stopping work when a message is close to expiring or by heartbeating (extending visibility) to signal that processing is still in progress.
- Overloads tend to raise latency, so if visibility timeouts are static, systems risk self-amplifying overload where messages time out, get redelivered, and multiple workers churn on the same items.
- This SQS behavior can effectively "fork-bomb" an already stressed service if message processing routinely runs longer than the visibility window during peak load.
- For complex asynchronous workflows involving more than simple queues, teams often use services like AWS Step Functions to gain explicit workflow visibility and simplify distributed debugging.
- The article argues that ignoring latency in asynchronous systems is dangerous because outages, dependency slowdowns, or unexpectedly expensive workloads can create huge backlogs that resist timely recovery.
- To build resilient asynchronous systems, Amazon designs for backlog scenarios up front, applying techniques like prioritization, sidelining old or excess messages, and backpressure to keep queues manageable.

## Related notes

- [Message Queues in System Design](/notes/message-queues-in-system-design/)
- [Message Queues & Message Brokers](/notes/message-queues-and-message-brokers/)
- [Building Distributed Systems in Elixir: Part 9 - Backpressure](/notes/building-distributed-systems-in-elixir-part-9-backpressure/)
- [Heartbeats in Distributed Systems](/notes/heartbeats-in-distributed-systems/)
- [Catalog of Patterns of Distributed Systems](/notes/catalog-of-patterns-of-distributed-systems/)
- [Notes on Distributed Systems](/notes/notes-on-distributed-systems/)
- [Why Distributed Systems Are Hard](/notes/why-distributed-systems-are-hard/)
