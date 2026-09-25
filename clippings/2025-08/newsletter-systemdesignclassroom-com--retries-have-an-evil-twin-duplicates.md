---
url: "https://newsletter.systemdesignclassroom.com/p/retries-have-an-evil-twin-duplicates?utm_source=substack&utm_medium=email"
captured_at: "2025-08-11T22:13:21+01:00"
title: "Retries Have an Evil Twin: Duplicates - by Raul Junco"
domain: "newsletter-systemdesignclassroom-com"
---

---
You've built retries.  
You've added queues.  
You think you've made everything '**resilient**.'

And then a payment went through twice.  
Two orders shipped.  
The same email got sent three times.

Welcome to the ugly side of retries no one warns you about: **duplication.**

[

![](https://substackcdn.com/image/fetch/$s_!s9me!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F78b377b0-2afe-4543-933c-973b1c60f9a0_1036x684.png)

](https://substackcdn.com/image/fetch/$s_!s9me!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F78b377b0-2afe-4543-933c-973b1c60f9a0_1036x684.png)

In distributed systems, **At-Least-Once delivery is the default**. Messages get retried. Requests get replayed. But if your app isn't ready for it, you end up with corrupted data, angry customers, and incomprehensible logic

This post breaks down **four battle-tested strategies** to handle duplication at the application level, so your systems stay correct, even when the same work shows up more than once.

Thanks to our partners who keep this newsletter free for the reader.

**CodeRabbit** → Free AI Code Reviews in VS Code

> [
> 
> ![](https://substackcdn.com/image/fetch/$s_!RyNd!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fec8eb9be-1200-4e2c-9727-41d36fdd4a6c_1291x649.png)
> 
> ](https://substackcdn.com/image/fetch/$s_!RyNd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fec8eb9be-1200-4e2c-9727-41d36fdd4a6c_1291x649.png)

CodeRabbit brings AI-powered code reviews directly into VS Code, Cursor, and Windsurf. Get free, real-time feedback on every commit, before the PR, helping you catch bugs, security vulnerabilities, and performance issues early.

-   **Per-commit reviews:** Identify issues faster and avoid lengthy PR reviews
    
-   **Context-aware analysis:** Understand code changes deeply for more accurate feedback
    
-   Fix with AI and get AI-driven suggestions to implement code changes
    

**Multi-Layered Reviews:** Benefit from code reviews both in your IDE (free) and in your PR (paid subscription)

[Install in VS Code](https://coderabbit.link/raul)

## The Problem: Same Message, Twice the Effect

Let's say a user submits a payment. The request goes through your API, but the backend crashes right before saving the result.

Your retry logic kicks in.

Now the same request is processed again. And you've:

-   Charged the user twice.
    
-   Created two payment records.
    
-   Triggered two downstream events.
    

This isn't just bad luck. It's **by design**.

> ⚠️ **At-least-once delivery is the default.**  
> Most systems, especially queues, retries, and distributed APIs, guarantee that a message will arrive **at least once**, but may arrive **multiple times**.

Why? Because retries are safer than data loss.  
It's your job to make sure duplicates don't break your system.

## What's at Stake?

Without duplication control:

-   **Your data becomes unreliable.** Systems that rely on exact state, like billing or inventory, get corrupted.
    
-   **Your code becomes defensive.** Every handler needs if-checks, patches, or compensating logic.
    
-   **Your operations team burns out.** They spend hours deduplicating rows, refunding customers, and triaging inconsistencies.
    

You don't just lose trust. You will lose time.

## 4 Ways to Stop Duplication at the Application Layer

These approaches aren't theoretical. They show up in real production systems, depending on scale, latency tolerance, and system design.

#### 1\. Database Unique Constraints

**Concept:** Use a `UNIQUE` constraint in the database to prevent duplicate operations, backed by an **idempotency key**.

Let's say a user places an order.  
The client generates a unique `idempotency_key` and sends it with the request:

```
CREATE TABLE orders (
  id UUID PRIMARY KEY,
  idempotency_key TEXT UNIQUE,
  ...
);
```

The server attempts to insert the order using this key. If the same request is retried (e.g. due to a timeout), the database will reject the duplicate with a constraint violation.

You catch that error and fetch the original order.

[

![](https://substackcdn.com/image/fetch/$s_!ABZT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4f113684-5150-48b2-9fe2-c3b52f9be86a_771x797.png)

](https://substackcdn.com/image/fetch/$s_!ABZT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4f113684-5150-48b2-9fe2-c3b52f9be86a_771x797.png)

#### ✅ Pros

-   Ensures **only one successful insert** per key. Potential performance impact from high-concurrency insert conflicts or deadlocks.
    
-   Clean fallback path for retries, return the existing result.
    
-   Ideal for operations like **checkout, registration, or payment initiation**.
    

#### ⚠️ Cons

-   Adds write pressure to the database. In
    
-   Doesn't protect downstream effects unless guarded (e.g. emails, inventory).
    
-   Needs good **key generation hygiene** on the client or gateway.
    

📌 **Key insight:** The database isn't just for persistence. It's a **gatekeeper** that protects your system from replayed requests, _as long as you give it something to gate on._

#### 2\. In-Memory Deduplication

**Concept:** Track processed request IDs in memory using a `Set`, Map, or LRU cache. On each request, check if the ID was seen before.

[

![](https://substackcdn.com/image/fetch/$s_!dbX9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faec29802-c453-45f0-ad76-14be6b29e45a_651x307.png)

](https://substackcdn.com/image/fetch/$s_!dbX9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faec29802-c453-45f0-ad76-14be6b29e45a_651x307.png)

It's fast. It's simple. But it's **only safe if your service is single-instance** and doesn't restart frequently.

**Why it works:** The process itself remembers what it's already done, no I/O needed.

#### ✅ Pros

-   Blazing fast.
    
-   No infrastructure dependency.
    
-   Great for **short-lived** tools and **batch processes.**
    

#### ⚠️ Cons

-   **Volatile memory**: everything is wiped on restart or crash.
    
-   Doesn't work in **multi-threaded** or **multi-node** systems without coordination.
    
-   You need to **manually clean up** old keys or use a TTL mechanism.
    

📌 **Best for:** One-off scripts, CLI tools, test environments, or internal utilities where reliability isn't mission-critical, monoliths with low/moderate operation frequency.

#### 3\. Distributed Cache (Redis)

**Concept:** Use Redis to track processed operations across distributed nodes. Store a key for each request ID with a TTL:

```
SETNX request:&lt;id&gt; "processed"    # Only set if not exists
EXPIRE request:&lt;id&gt; 600           # Auto-expire in 10 minutes
```

This ensures:

-   Only one node processes the request.
    
-   Future retries are blocked.
    
-   The de-dup record eventually expires to free memory.
    

**Why it works:** Redis becomes a **shared memory layer** across services and instances.

[

![](https://substackcdn.com/image/fetch/$s_!xx_f!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F34094780-0221-4b47-8879-e2a6e58928b5_1189x668.png)

](https://substackcdn.com/image/fetch/$s_!xx_f!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F34094780-0221-4b47-8879-e2a6e58928b5_1189x668.png)

#### ✅ Pros

-   Fast lookup and write.
    
-   Survives restarts and horizontal scaling.
    
-   TTL provides automatic cleanup.
    

#### ⚠️ Cons

-   TTL tuning is **non-trivial**. Too short and legit retries slip through; too long and Redis bloats.
    
-   **Network partitioning or Redis downtime** means you may process duplicates.
    
-   You'll need to deploy and monitor Redis reliably. It can become a single point of failure.
    

📌 **Tradeoff tip:**  
Pair Redis deduplication with a **fallback to DB uniqueness** to catch any misses due to cache failures or TTL gaps.

📌 **Best for:** API services, job processors, microservices with retry logic.

#### 4\. Message Broker Deduplication

**Concept:** Some brokers (e.g., Azure Service Bus, Pulsar) support built-in duplicate detection.

You assign a `MessageId` to each message. The broker keeps a **deduplication window** (e.g. 10 minutes). If the same ID appears again, it discards the message.

[

![](https://substackcdn.com/image/fetch/$s_!SbUr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b748136-9766-4025-b99f-dafc8a116bed_1043x676.png)

](https://substackcdn.com/image/fetch/$s_!SbUr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b748136-9766-4025-b99f-dafc8a116bed_1043x676.png)

**Why it works:** The **message infrastructure** becomes the gatekeeper; duplicates don't even hit your app.

#### ✅ Pros

-   **No application logic** required.
    
-   Prevents duplicate **delivery**, not just processing.
    
-   Works great with **at-least-once** brokers.
    

#### ⚠️ Cons

-   Requires proper configuration (de-dup window, clock sync).
    
-   Doesn't help if your app publishes **duplicate downstream events**.
    
-   Broker-specific — not portable across infra.
    

📌 **Best for:** Event-driven architectures, high-throughput pipelines, or systems with built-in broker support.

### Trade-Off Comparison

[

![](https://substackcdn.com/image/fetch/$s_!iivI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F01a8b22e-709a-43b0-a52d-c5b0225b7ec9_801x209.png)

](https://substackcdn.com/image/fetch/$s_!iivI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F01a8b22e-709a-43b0-a52d-c5b0225b7ec9_801x209.png)

### Final Takeaways

-   **Duplication is a design reality**, not a bug. Plan for it.
    
-   **At-least-once delivery** means your systems will get the same input more than once. Act accordingly.
    
-   **Use the database for strong guarantees**, Redis for fast coordination, and brokers for message-level protection.
    
-   **TTL-based deduplication** is usually good enough. Start there.
    
-   **Combine layers** (e.g., broker de-dup + Redis + DB constraint) for critical flows.
    

> You can't prevent retries, but you can prevent rework.
> 
> Resilience without deduplication is just chaos with retries.

Until next time,  
— Raul

System Design Classroom is a reader-supported publication. To receive new posts and support my work, consider becoming a paid subscriber.
