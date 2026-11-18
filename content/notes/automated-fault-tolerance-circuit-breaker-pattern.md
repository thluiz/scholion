---
title: "Automated Fault Tolerance using the Circuit Breaker Pattern"
date: '2020-05-13T06:01:40+00:00'
category: webclip
summary: 'Article describes how Teachers Pay Teachers uses a circuit breaker pattern on top of feature flags to detect failing dependencies and gracefully degrade pages instead of fully breaking.'
tags: ["fault-tolerance", "circuit-breaker", "microservices", "graceful-degradation"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Automated Fault Tolerance using the Circuit Breaker Pattern"
    url: "https://medium.com/teacherspayteachers/automated-fault-tolerance-using-the-circuit-breaker-pattern-3884f6e99133"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-05/medium-com--automated-fault-tolerance-circuit-breaker-pattern.md"
    kind: repo
---

The article explains how Teachers Pay Teachers uses the circuit breaker pattern to improve fault tolerance when external dependencies fail. Their web stack involves Node.js front-end servers and an Elixir/Phoenix API that relies on databases, caches, and third‑party APIs. Rather than only reacting manually with feature flags when failures occur, they augment feature flags with automated circuit breakers that detect unhealthy services and temporarily block calls, allowing the site to degrade gracefully instead of showing full error pages.

They store per‑request success/failure status in Cachex, compute error rates over a bounded history window, and break the circuit once a configured threshold is exceeded. While the circuit is open, the API returns downgraded content that lets the front‑end continue to render partial pages. The post discusses concrete examples (sponsored items on search, Wordpress content on mobile), clarifies how this reduces load on stressed systems, and notes trade‑offs around cache choice, synchronization between servers, and threshold tuning. It closes by noting that circuit breakers are not appropriate for core functionality where failure must still surface as an error page.

## Reading notes

- The site architecture routes educator requests through Node.js front‑end servers to an Elixir/Phoenix API, which depends on multiple external systems including databases, caches, and third‑party APIs.
- Real production conditions include dependency failures like slow or overloaded databases and breaking changes in external APIs, which can cause whole pages (e.g., search results or mobile homepage) to fail.
- Manual mitigation uses feature flags to disable failing features after humans detect an incident; at TpT these deploy in under 30 seconds, but total MTTR also includes human reaction time.
- The automated approach uses circuit breakers so the system itself detects failures and degrades functionality without human involvement.
- Circuit breakers are implemented by extending existing feature flag logic, enabling or disabling calls to particular services based on their recent health.
- Each service’s recent request outcomes are stored in Cachex as a list of 1s (success) and 0s (failure), with a default TTL of 60 seconds that can be configured per feature.
- For incoming requests, the system retrieves the status history from Cachex, calculates the error rate as failures divided by total history size, and compares it to a predefined error threshold.
- If the error rate is below the threshold, the circuit remains closed, the service call proceeds, and the outcome is recorded in cache; if it exceeds the threshold, the circuit opens and subsequent calls to that service are blocked until the cache entry expires.
- Each feature defines minimum and maximum history sizes so the circuit does not react to too few data points and does not accumulate unbounded status lists in cache.
- When a circuit is open, the API returns downgraded content to the front‑end, which can still load the page using the available data instead of failing outright.
- Graceful degradation is illustrated with the search results page: under normal conditions it shows sponsored items above results, but when the sponsored items query times out under heavy DB load, the page used to return an error.
- With circuit breakers, high error rates on the sponsored items feature cause that circuit alone to open, and the system serves the rest of the search results content without the sponsored block.
- Conceptually, when a user requests multiple content pieces (X, Y, Z) and one component (Y) is unstable, the response now includes only the healthy components (X and Z) rather than failing the entire response.
- Circuit breakers are also applied to Wordpress requests on the mobile homepage and other features deemed likely to fail, reducing full‑page outages from single dependency issues.
- The pattern is described as an optimization of exception handling because it turns off problematic features proactively, avoiding repeated failing calls against overloaded systems such as databases.
- Reducing repeated calls to a degraded dependency helps that system recover faster by lowering unnecessary load.
- Initial implementation using Cachex led to cache contention issues, prompting a move to ETS for local storage of request status data on each API server.
- Local storage per server can cause inconsistent behavior because different servers may see different error histories and thus make different circuit decisions.
- Using shared external storage like Memcached or Redis could synchronize circuit breaker state across servers, but would itself become another external dependency with potential failures.
- A shared external store might also cause all servers to block a feature when only one server is degraded and the configured error threshold is low.
- Error thresholds are currently chosen heuristically, which risks being misaligned with real‑world behavior for some features.
- A suggested improvement is to derive dynamic error thresholds per feature based on historical patterns and detect anomalous error rates relative to comparable prior time windows.
- Such anomaly‑based thresholds could reduce false negatives in circuit breaking, but implementing this would require substantial time and resource investment.
- Circuit breakers are described as unsuitable for very core site capabilities where graceful degradation is not practical, such as when the transactional database cluster is down and no user or product data can be fetched.
- In cases where critical data is unavailable, the system must still serve error pages rather than attempting partial responses.
- The basic circuit breaker mechanism described has already improved resilience, reducing user impact from unexpected dependency failures even though the implementation is not considered final.
- The author credits coworker Jeff Martin for partnering on the implementation and invites feedback and ideas on improving fault tolerance.
