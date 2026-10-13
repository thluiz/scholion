---
url: "https://nader.substack.com/p/engineering-for-agents-that-never?utm_source=tldrnewsletter"
captured_at: "2026-10-13T09:26:28+01:00"
title: "Engineering for Agents That Never Sleep"
domain: "nader-substack-com"
---

> Originally [posted on X](https://x.com/dabit3/status/2038608435105726862?s=20).

At Cognition, 70% of all Devin sessions are currently kicked off by a person (through [the webapp](https://app.devin.ai/), Slack, or Linear). The other 30% start automatically via [API](https://docs.devin.ai/api-reference/overview), [scheduled sessions](https://docs.devin.ai/product-guides/scheduled-sessions), [scheduled Devins](https://cognition.ai/blog/devin-can-now-schedule-devins), and other automations.

That ratio will continue to invert. Within a few months [it will likely be 30/70](https://x.com/ScottWu46/status/2035106171984773508). Within a year, 10/90.

[

![](https://substackcdn.com/image/fetch/$s_!_8Kw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6c416574-d685-476d-8029-f9d1d862db17_3264x1312.png)

](https://substackcdn.com/image/fetch/$s_!_8Kw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6c416574-d685-476d-8029-f9d1d862db17_3264x1312.png)

The reason is simple: most signals that create engineering work are already readable by software.

Most engineering work starts from signals that systems already produce. Today, a person reads those signals, switches context, opens Devin, and writes a prompt that repeats information the system already had.

That person is acting as a relay between two systems that could talk directly.

That manual handoff can go away.

The alert can start Devin. The failing test can start Devin. The approved spec can start Devin. The latency spike can start Devin.

The engineer’s job shifts to setting up the triggers, constraints, and quality gates that let those sessions run safely and produce usable work.

That requires agents that run in the cloud. An incident pipeline needs to be able to start an agent whether or not someone has an IDE open.

It also requires the basics: comprehensive unit tests, clear documentation, reproducible dev environments, and enough system context for the agent to understand architecture, conventions, dependencies, and service interactions across repos.

That setup determines how useful the agent is. With the right tests, docs, environments, and context, Devin can open PRs, validate changes, and handle real operational work.

The prompt box will still be there. On strong engineering teams, more of the work will already be started before anyone opens it.

> With [Devin](https://devin.ai/), this is where we think the puck is headed. If you’d like to learn more, [reach out](https://cognition.ai/contact).
