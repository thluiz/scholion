---
title: "Timeouts, retries, and backoff with jitter"
date: '2026-11-26T00:33:14+00:00'
category: webclip
summary: 'Explains how Amazon designs timeouts, retries, exponential backoff, and jitter to handle transient and partial failures without overloading struggling services.'
tags: ["distributed-systems", "timeouts", "retries", "resiliency-patterns"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Timeouts, retries, and backoff with jitter"
    url: "https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/aws-amazon-com--timeouts-retries-backoff-jitter-amazon-practices.md"
    kind: repo
---

Amazon describes how distributed services inevitably experience partial and transient failures, and how they use timeouts, retries, backoff, and jitter to keep small issues from turning into full outages. The text focuses on choosing and implementing timeouts carefully, limiting and shaping retries with exponential backoff and token-based throttling, and adding jitter to both retries and scheduled work to prevent synchronized load spikes.

## Reading notes

- Distributed services fail for many reasons, including servers, networks, load balancers, software, operating systems, and operator mistakes.
- Amazon aims to tolerate failures and prevent a small fraction of failed calls from cascading into full service outages.
- Three primary tools for resilience are timeouts, retries, and backoff, with jitter added to avoid correlated bursts.
- Slow or never-completing requests hold resources such as memory, threads, connections, and ephemeral ports for longer, which can exhaust server capacity.
- Timeouts bound how long a client waits for a request, limiting how long resources stay tied up.
- Many failures are partial (only some requests fail) or transient (fail for a short period), which makes retrying useful.
- Retries let clients ride out random partial and short-lived transient failures by resending the same request.
- Retries can be unsafe when a backend is failing because of overload, since extra requests increase load.
- Backoff increases the time between retries, helping keep backend load more even.
- Some calls have side effects; a timeout does not guarantee that side effects did not occur.
- To make retries safer, APIs are designed to be idempotent so that repeating a request does not cause unwanted repeated side effects.
- Traffic into Amazon services often arrives in bursts, driven by client behavior, failure recovery, or periodic jobs.
- When errors are caused by load, synchronized retries can be ineffective if all clients retry at once.
- Jitter adds random delay before sending or retrying requests to spread arrivals over time.
- Amazon treats setting a timeout on any remote call, including inter-process calls on the same host, as a best practice.
- Timeouts usually involve both a connection timeout and a request timeout, often using client libraries that already support them.
- Choosing a timeout value is difficult: too high reduces protection, too low increases retries and can cause an outage by triggering mass retries.
- For calls within an AWS Region, Amazon bases timeouts on downstream latency metrics, picking a target false-timeout rate (for example 0.1%).
- Given a false-timeout rate, they choose the corresponding latency percentile of the downstream service (such as p99.9) as a starting point for the timeout.
- This percentile-based approach fails when clients have significant network latency, such as internet clients, so they add a reasonable worst-case network component.
- The same approach also struggles with services that have very tight latency distributions where high percentiles are close to median.
- In tight-latency services, they add padding to prevent minor latency increases from causing a wave of timeouts.
- Linux's SO_RCVTIMEO can be used for timeouts but is considered unsuitable as an end-to-end socket timeout due to subtle behavior.
- Some languages, like Java, expose low-level socket timeout options, whereas others, like Go, provide higher-level timeout abstractions.
- Timeouts sometimes fail to cover all remote work, such as DNS resolution or TLS handshakes, leading to unexpected delays.
- Amazon prefers well-tested client libraries for timeouts and, when implementing their own, pays attention to what operations are actually covered.
- An example system saw timeouts immediately after deployments because the request timeout included TLS connection setup.
- In that system, a low timeout (around 20 ms) was usually fine, but new secure connections after deployments occasionally exceeded it.
- Some timed-out requests in that case succeeded on retry, revealing that connection setup was the cause.
- They initially mitigated by increasing the timeout when establishing a new connection.
- Later, they improved behavior by establishing secure connections during process startup before handling traffic.
- The article characterizes retries as "selfish" because each retry demands more backend resources to improve a single client's success probability.
- When failures are rare or brief, retries work well because few requests are retried and apparent availability increases.
- When failures are due to overload, extra retries can worsen overload and slow down recovery.
- Exponential backoff is Amazon's preferred pattern instead of rapid-fire retries: the delay grows exponentially after each attempt.
- Because exponential backoff can grow very large, implementations usually cap the maximum backoff delay.
- Capped exponential backoff introduces a risk that all clients retry repeatedly at the maximum rate once the cap is reached.
- Amazon typically limits the number of retries and propagates failure earlier in the service stack rather than retrying indefinitely.
- Most clients will eventually give up because of their own overall request timeouts, even if they keep retrying internally.
- Multi-layer distributed systems can magnify load if every layer retries independently.
- A five-deep service stack with three retries at each layer can increase database load by 243x when the database starts failing under load.
- Multiplicative retry behavior across layers makes it difficult for a struggling dependency to recover.
- Retrying only at the highest layer wastes work already done in lower layers but avoids compounding retries.
- For low-cost control-plane and data-plane operations, Amazon's best practice is to perform retries at a single point in the call stack.
- Even with a single retrying layer, error conditions can still cause large traffic increases, so additional controls are needed.
- Circuit breakers halt calls to a failing downstream service after an error threshold, but introduce modal behavior that is hard to test.
- Circuit breakers can also add significant recovery time because reopening them and restoring traffic happens in distinct modes.
- Amazon mitigates retry overload by limiting retries locally with a token bucket.
- With the token bucket approach, calls can retry freely while tokens remain and then only retry at a fixed rate once tokens are depleted.
- AWS added token-bucket-based retry throttling to the AWS SDK in 2016 so that SDK users automatically benefit from controlled retries.
- Amazon generally considers APIs with side effects unsafe to retry unless they support idempotency.
- Idempotent APIs ensure that side effects occur only once, regardless of how many times a client retries the same logical request.
- Read-only APIs are usually idempotent, whereas resource-creation APIs might not be unless designed for it.
- Some services, such as Amazon EC2 RunInstances, offer explicit token mechanisms to guarantee idempotency during retries.
- Good API design and careful client implementation are needed to prevent duplicate side effects when using retries.
- HTTP status codes distinguish between client errors and server errors, guiding which failures should be retried.
- Client errors generally should not be retried as-is, while server errors might succeed on subsequent attempts.
- Eventual consistency blurs the simple HTTP guideline because a client error can become a success shortly later as state converges.
- Despite complexity and risk, retries remain a core technique for high availability in the presence of random transient failures.
- Engineers must apply judgment to balance availability gains from retries against the risks of overload.
- Amazon recommends remembering that retries are a way for clients to assert the importance of their requests and demand more resources.
- Overly aggressive client retries can cause widespread impact on shared services.
- Backoff can be less effective when failures are caused by overload because of correlation in retry timing.
- If many clients back off for the same duration, they may retry at nearly the same time and recreate the overload.
- Jitter introduces randomness into backoff delays to decorrelate retries in time and reduce contention.
- Amazon refers readers to separate material on how to choose jitter amounts and algorithms for exponential backoff.
- Jitter also helps with non-retry traffic, such as periodic tasks and scheduled work, which can otherwise create hidden load spikes.
- Per-second traffic often shows sharp spikes that are obscured when looking only at aggregated metrics.
- Amazon considers adding jitter to timers, periodic jobs, and delayed work as part of system design.
- Spreading scheduled work with jitter makes it easier for downstream services to scale to the workload.
- For scheduled work, Amazon avoids selecting jitter randomly on each run per host.
- Instead, they use a consistent method that returns the same jitter value every time on a given host.
- Consistent jitter makes patterns repeatable, which helps humans spot and debug overload or race conditions.
- Fully random jitter can make overload or race-induced problems appear sporadically, complicating troubleshooting.
- In systems such as Amazon EBS and AWS Lambda, Amazon observed that many clients send periodic requests at fixed intervals.
- Multiple servers using the same schedule can synchronize and send their periodic traffic at nearly the same time.
- This synchronization commonly clusters requests in the first seconds of a minute or just after midnight for daily jobs.
- By examining per-second load and collaborating with clients to jitter periodic workloads, Amazon delivered the same work with lower server capacity.
- Customer-generated spikes are harder to control, but jitter can still be introduced where it does not worsen user experience.
- In distributed systems, transient failures and remote latency are treated as unavoidable realities.
- Timeouts prevent clients from waiting excessively long, retries help absorb transient failures, and backoff plus jitter smooth resource usage.
- Amazon emphasizes cautious retry strategies, especially when dependencies are overloaded and calls are timing out.
- Retrying only when a dependency appears healthy, and stopping when retries stop helping availability, reduces the chance of overload amplification.

## Related notes

- [Retries Have an Evil Twin: Duplicates](/notes/retries-have-an-evil-twin-duplicates/)
- [Semantic equivalence and support for default retry strategies](/notes/semantic-equivalence-and-idempotent-retries/)
- [Why Ruby’s Timeout is dangerous (and Thread.raise is terrifying)](/notes/why-rubys-timeout-is-dangerous-thread-raise-terrifying/)
- [Automated Fault Tolerance using the Circuit Breaker Pattern](/notes/automated-fault-tolerance-circuit-breaker-pattern/)
- [Must-Known Resiliency Patterns for Distributed Systems](/notes/must-known-resiliency-patterns-for-distributed-systems/)
- [Scaling your API with rate limiters](/notes/scaling-your-api-with-rate-limiters/)
- [Design a Rate Limiter](/notes/design-a-rate-limiter/)
- [Catalog of Patterns of Distributed Systems](/notes/catalog-of-patterns-of-distributed-systems/)
- [Notes on Distributed Systems](/notes/notes-on-distributed-systems/)
- [Why Distributed Systems Are Hard](/notes/why-distributed-systems-are-hard/)
