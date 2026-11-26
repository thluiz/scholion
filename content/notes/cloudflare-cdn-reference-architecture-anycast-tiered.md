---
title: "Content Delivery Network (CDN) Reference Architecture"
date: '2026-11-25T16:10:24+00:00'
category: webclip
summary: 'Cloudflare explains how its anycast CDN, tiered caching, Argo Smart Routing, and Cache Reserve improve performance, resiliency, security, and cost for web applications.'
tags: ["cdn", "cloudflare", "anycast-network", "caching-strategy"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Content Delivery Network (CDN) Reference Architecture"
    url: "https://developers.cloudflare.com/reference-architecture/architectures/cdn/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/developers-cloudflare-com--cloudflare-cdn-reference-architecture-anycast-tiered.md"
    kind: repo
---

Cloudflare describes how CDNs solve latency, performance, resiliency, security, and cost issues faced by web applications hosted on centralized origin servers. It contrasts traditional direct-to-origin delivery with a globally distributed anycast CDN that caches content at the edge, offloads origin traffic, mitigates DDoS, and delivers more consistent user experience worldwide. The document details Cloudflare’s SaaS CDN model, anycast-based routing, tiered caching topologies, Argo Smart Routing, Cache Reserve, and options for latency-sensitive regions such as China.

## Reading notes

- The document targets IT and network professionals familiar with infrastructure concepts like caching, DNS, and firewalls, and outlines how Cloudflare’s CDN architecture addresses common web delivery challenges.
- Growing Internet traffic, accelerated by remote work and COVID-19, makes efficient traffic management, latency reduction, and performance gains more urgent.
- Companies running applications on-premises or in the cloud must balance performance improvements, scalability for availability and redundancy, security against growing threats, and rising costs.
- Traditional architectures often deploy a central origin server replicated to another region or spread across several data centers, which still leaves users far from the origin and creates latency and scaling issues.
- Origin servers handle many HTTP requests for each page view (HTML, CSS, images, video, etc.), and while HTTP/2 and HTTP/3 multiplexing reduces TCP overhead, compute and network load at the origin still grow with more clients.
- Increased client traffic can overload origin servers, raise latency, make user experience dependent on distance to the origin, drive up bandwidth and compute costs, and leave infrastructure exposed to DDoS attacks.
- Without a CDN, DNS resolution typically happens at the user’s ISP, after which HTTP traffic goes directly to the origin, leading to lower latency near the origin’s region and higher RTT for distant users.
- Direct exposure of the origin to the Internet increases vulnerability to infrastructure- and application-layer DDoS attacks that can exhaust resources and block legitimate users.
- If the origin server goes offline in a non-CDN setup, its content becomes inaccessible because no intermediate cache is available.
- A CDN’s main goal is to reduce latency and improve performance by caching content in many data centers worldwide, as close to end users as possible at the provider’s network edge.
- Serving content from nearby CDN nodes improves load times, smooths performance across geographies, and reduces dependence on the origin’s physical location relative to users.
- By answering many requests from local caches, CDNs reduce load on the origin, increase availability and redundancy, and perform load balancing across local nodes, contacting the origin only when required.
- Acting as a reverse proxy in front of origins allows the CDN to provide DDoS mitigation, certificate handling, and other security optimizations.
- Since fewer requests reach the origin due to caching, organizations can significantly lower bandwidth and egress costs.
- The document contrasts DNS unicast routing with anycast routing as two approaches for steering users to CDN nodes.
- DNS-based CDNs rely on recursive resolvers and authoritative nameservers, making routing decisions based on the resolver’s location instead of the client’s IP and depending on DNS TTLs for changes.
- DNS unicast routing sends traffic to specific nodes, which can be stressed during traffic spikes such as DDoS attacks and can fail over less gracefully, sometimes requiring new sessions.
- Cloudflare uses anycast routing, with the same IP announced from multiple locations via BGP, so traffic flows to the nearest suitable data center.
- Anycast-based CDNs route incoming traffic to the closest data center with capacity, naturally provide redundancy when nodes fail, and distribute load across many sites, improving DDoS resilience.
- Cloudflare delivers CDN as SaaS, so customers gain performance and protection benefits without managing infrastructure or software themselves.
- Two pillars underpin Cloudflare’s CDN benefits: caching content near users and a distinctive architecture that integrates multiple services into a single global network.
- Cloudflare runs one global anycast network where every service is available on every server in every data center, giving users nearby access to all capabilities at scale and with high resiliency.
- As a reverse proxy, Cloudflare terminates client requests at the edge and forwards them to customer origins; because the edge is hardened, this setup shields origins from infrastructure-level and volumetric DDoS attacks.
- Requests are routed to and answered by the Cloudflare node nearest to the user, leveraging the anycast network for reduced latency and consistent performance.
- Cloudflare’s anycast network spans hundreds of cities and aims to reach 95% of the world’s Internet-connected population within 50 ms, while providing hundreds of Tbps of capacity and DDoS protection.
- Edge nodes cache origin content and also host services like Cloudflare DNS, DDoS protection, WAF, and other performance and security features using the same architecture.
- Argo uses optimized routing and caching across the network, including Smart Routing and Tiered Cache, to deliver responses more quickly, reliably, and securely, forming part of Cloudflare’s enhanced CDN solution.
- After onboarding a site, Cloudflare enables standard caching where each data center directly proxies to the origin; any cache miss results in that ingress location contacting the origin.
- Standard caching can lead to suboptimal behavior because content may already be cached in another data center, and origins may handle unnecessary duplicate requests.
- Tiered Cache, included with all plans, introduces upper-tier data centers that fetch from the origin on behalf of other locations, increasing cache hits and improving response times.
- When a cache miss occurs in a data center with Tiered Cache, it first checks designated upper-tier data centers for the content before going to the origin.
- The network path between Cloudflare data centers is typically shorter and faster than paths between Cloudflare and customer origins, so inter-data-center fetching is more efficient.
- Argo Smart Routing data informs the choice of optimal upper-tier data centers for Tiered Cache, and Argo can also be enabled to optimize paths between Cloudflare and origin for cache misses and dynamic traffic.
- Tiered caching is disabled by default but can be enabled in the caching section of the dashboard, with different topologies offered depending on plan level.
- Smart Tiered Cache Topology is available on all plans and recommended for most deployments when Tiered Cache is enabled.
- Generic Global Tiered Topology is an Enterprise feature recommended for globally distributed high-traffic sites that want maximum cache usage and performance.
- Custom Tiered Cache Topology, also for Enterprise, fits customers who know their user distribution and want to focus on specific geographic regions.
- Smart Tiered Cache is ideal for minimizing origin requests and bandwidth between Cloudflare and origins by funneling cache misses through a single chosen upper tier.
- Generic Global Tiered Topology balances cache efficiency and latency by designating all Tier 1 data centers as upper tiers.
- Custom Tiered Topology lets customers define specific upper-tier locations (for example, in particular regions) and requires engagement with a Cloudflare account team.
- In the Smart Tiered flow, an initial request that hits a lower-tier data center and misses its cache will query the upper-tier, which, if also missing, fetches from the origin, caches the content, and returns it to the lower tier.
- When subsequent requests for the same resource arrive at other lower-tier data centers, they can obtain the content from the upper-tier cache without additional origin trips.
- This funneling effect raises cache hit ratios, accelerates responses, reduces bandwidth between Cloudflare and the origin, and lessens origin load.
- A key tradeoff in Smart Tiered Cache is that the single upper tier selected by Argo may be geographically distant from some lower tiers, potentially adding latency even when the cache is hit at the upper tier.
- Smart Tiered Cache prioritizes higher cache hit percentages and fewer origin requests, accepting the possibility of higher inter-data-center latency in some cases.
- Generic Global Tiered Cache uses large, globally distributed data centers as upper tiers so that upper tiers are generally close to lower tiers, reducing latency on cache misses that travel upwards.
- Because more upper tiers fetch directly from the origin in Generic Global Tiered Cache, origin servers see more requests and heavier load compared with Smart Tiered Cache.
- Regional Tiered Cache introduces an additional cache layer between lower and upper tiers to blend Smart and Global strategies by placing regional hubs closer to lower-tier data centers.
- With Regional Tiered Cache and Smart or Custom Tiered configurations, lower tiers first query a regional tier for cache, then escalate to a single upper tier if needed, improving latency for global applications.
- Regional Tiered Cache is not recommended when many upper tiers already exist across regions, such as in Generic Global Tiered deployments.
- When Regional Tiered Cache is enabled, lower tiers on a cache miss send requests to a nearby regional hub, which, if it also misses, forwards to the upper tier and origin as necessary.
- Argo Smart Routing underpins Tiered Cache by determining optimal upper tiers and can additionally optimize the path between upper-tier data centers and origin servers.
- Even without Argo enabled, Cloudflare still routes traffic sensibly to maintain origin reachability, though not necessarily along the fastest possible paths.
- Argo Smart Routing relies on real-time data derived from routing roughly 50 million HTTP requests per second, using metrics like congestion, latency, and RTT to select the best paths.
- Cloudflare reports that Argo Smart Routing typically delivers about 30% faster performance for web assets.
- Without Tiered Cache or Argo, on a cache miss the nearest data center sends requests directly to the origin along a reliable but potentially suboptimal Internet path.
- With both Tiered Cache and Argo enabled, a miss at a lower tier triggers a lookup at its upper tier; if another origin fetch is required, Argo chooses the fastest route from the upper tier to the origin.
- Argo Smart Routing is used for origin-bound traffic when cache misses require retrieving content and for inherently non-cacheable content like many API-driven or dynamic responses.
- Cache Reserve extends the Tiered Cache concept by adding a higher, persistent cache tier built on R2 object storage to hold content longer and cut origin egress fees.
- Cache Reserve aims to further reduce origin load and improve availability by maintaining long-lived cached content that can refill upper and lower tiers.
- While Cache Reserve can operate without Tiered Cache, Cloudflare recommends combining them so Tiered Cache reduces redundant reads and storage in Cache Reserve, preventing unnecessary egress and storage costs.
- When enabling Cache Reserve via the dashboard, Cloudflare warns if Tiered Cache is not turned on to encourage the combined configuration.
- Cache Reserve retains cached content for 30 days regardless of headers or TTL settings, though TTL still governs freshness and triggers revalidation against the origin on expiry.
- TTL can be set through mechanisms such as Cache-Control, CDN-Cache-Control, Edge Cache TTL, status-code-based TTL, or Cache Rules, and each read from Cache Reserve resets the 30-day retention window.
- If cached content in Cache Reserve is not accessed for 30 days, it is deleted from that tier.
- For content to be eligible for Cache Reserve, it must be cacheable according to Cloudflare’s cache rules, have a TTL of at least 10 hours, and include a Content-Length header in the origin response.
- Responses using chunked transfer encoding without a Content-Length header cannot be stored in Cache Reserve.
- In combination with Tiered Cache and Argo Smart Routing, Cache Reserve can significantly boost cache hit rates, further shield origin servers, and keep content close to users.
- The architecture with Cache Reserve allows upper and lower tiers to repopulate from this persistent layer instead of the origin, reducing origin traffic and stabilizing performance.
- Some latency is tied to specific regions, and traffic involving locations like China can face additional delays beyond raw distance to origin or cache.
- To address in-region latency, Cloudflare offers China Network, which uses JD Cloud’s data centers to provide in-China caching irrespective of where the origin is hosted.
- Global Acceleration complements China Network by securing and optimizing connectivity between origins and JD Cloud data centers, particularly for dynamic content such as web apps and API calls.
- Overall, Cloudflare positions its CDN as a SaaS solution that uses a global anycast network, Tiered Cache, Argo Smart Routing, and Cache Reserve to handle performance, availability, redundancy, security, and cost challenges for modern web applications.
