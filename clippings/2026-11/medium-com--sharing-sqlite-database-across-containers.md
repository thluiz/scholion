---
url: "https://medium.com/@rbranson/sharing-sqlite-databases-across-containers-is-surprisingly-brilliant-bacb8d753054"
captured_at: "2026-11-16T05:49:44+00:00"
title: "Sharing an SQLite database across containers is surprisingly brilliant | by Rick Branson | Medium"
domain: "medium-com"
---

DevOps
Sqlite
Containers
Distributed Systems
Reliability
Sharing an SQLite database across containers is surprisingly brilliant
Rick Branson
5 min read
·
Jan 7, 2020

This is a graph of latency in milliseconds. It’s the latency of Segment’s streaming pipeline fetching a critical piece of customer-specific configuration. This pipeline often handles north of 500,000 messages per second. Normally when I see a graph like this, it makes me very anxious. How can the exact same work suddenly become over 20X faster?

The story starts two and a half years ago, when it seemed like major incidents were happening all the time at Segment. We knew that very soon customers would begin to lose trust. To stop the bleeding, some extra process¹ was introduced and developers were imbued with a sense of fear of breaking production². We already knew this wasn’t an ideal state, but it was in response to a true existential threat to the business.

The engineering teams were then given a directive. Until there is a reasonable level of certainty — backed by data — that critical service deployments won’t cause a severe incident, engineers would focus on step-by-step architectural and tooling improvements to make it so.

A major reason to take such a bold stance was a pervasive lack of safety. Developers were making a vast number of choices when piecing together their system architecture. Most of their options were mediocre, many would land them in a world of pain, and often only one or two led to Nirvana. Such is the sad state of affairs in modern application development.

Configuration and Consternation

One of these major choices starts with “how do I store the configuration that customers specify in our web app?” This is the stuff that tells the high-throughput streaming pipeline how to treat data on a per-customer basis. We use a specific term for this configuration: control data. Incident after incident pointed to the bespoke architectures used for control data. Engineers really needed a default choice that would always work reliably at scale.

Our control plane is a necessarily complicated beast with layers upon layers of business logic. The data plane has a completely different nature — lean and mean — and it turns out that the data plane only needs a tiny slice of the control plane’s data under management. The mantra became loosen the coupling of the control plane and data plane.

So an admittedly bonkers idea came to me. An idea which didn’t really have a precedent, at least any we could find. What if the control data was actually local to the host? What if it was stored in a file? What if the file was shared by dozens of containers? What if a query meant reading a file? That would mean no service to break or run out of resources. As long as the file is readable, the data is available. No gods, no masters.

Initial reactions were incredulous at best. Just exactly how is a file under constant modification safely shared across dozens of containers, all needing concurrent access? And you’re really going to read this file from completely different pieces of software?

For all practical purposes, there is precisely one solution: SQLite. It turns out that multi-process concurrency is one of the things that separates SQLite from the other best-of-breed embedded databases. It is a practically unique feature — its raison d’être, at least from this perspective.

But containers make us almost instinctively nervous. They have achieved a kind of mythical status now that they are so thoroughly abstracted. Thankfully they mostly boil down to some constraints placed on processes by the kernel and an isolated filesystem with some holes poked in it. Containers are just processes, and SQLite is really good at sharing a database across processes.

Now to answer some questions — does a database on a Docker shared volume in multiple containers even work? Why yes it does. Check. Does this work at all under load? Wait, let me turn on WAL mode. Now it does. ️Check. Do processes block each other under load? No! Check.

It’s not really a database, man

So we built a special-purpose distributed database around this idea called ctlstore, which was open sourced last year. The graph at the beginning of this post shows the team cutting over reads from a networked database to ctlstore. Now that you know about the SQLite database, the massive drop in latency is probably not all that surprising.

Some practicality trade-offs were made, but even I was a bit astonished at how well it works in practice. Aside from the quirk of sharing SQLite across containers, it delivers extremely well on one core idea: the thematic shift of complexity from the data plane read path to the control plane write path.

The team at Segment has definitely made a dent, but I think this space is ripe for innovation. Brilliant minds have built distributed systems that are amazingly resilient to routine failure. However, if you’re privy to the closely-held details, you probably already know that the major outages which take down the titans of the Internet these days very often involve control data errors or unavailability.

If you’re looking to make strides in the Internet reliability space, this seems to me to be the area for focus. Verifying complex, human-originated configuration and then distributing it to the edges of deeply layered compute infrastructures at scale is very far from a solved problem. There are no stacks or bundles of best practices. And it’s as much a human interface challenge as it is an infrastructure one. Purgamentum init, exit purgamentum.

All credit due to my colleagues Alexandra Noonan and Steven van Loben Sels for the truly inspiring work that directly resulted in the beautiful graph at the beginning of this piece.

[1] Change control. I know, scary. Take a few minutes to fill out a short questionnaire describing the expected impact, why there’s a high level of certainty it won’t break production, and how to verify that the change didn’t break things once it is deployed. At first there was a lot of copy-pasta. I kinda found it helpful, like rubber ducking. The carrot at the end of the stick: once a team truly automated their routine deployments, they can move it to a streamlined GitHub Pull Request workflow instead of…. JIRA 😨

[2] Our version of fear is pretty tame. It means that engineers spend more time up front verifying their changes, and they setup processes and tools to conduct multi-stage production rollouts. We didn’t fire anyone or hire a cranky ops team to tell them “NO!” In fact, at Segment, developers carry pagers, so they were quite receptive to help improving their situation!
