---
title: "Bluesky and Decentralization -- Dustycloud Brainstorms"
date: '2026-09-25T08:28:25+01:00'
category: webclip
summary: 'The post argues that Bluesky uses useful decentralization techniques and credible exit, but is not decentralized or federated under the author’s definitions, and that full self-hosting would create quadratic scaling costs.'
tags: ["bluesky","decentralization","activitypub","atproto"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Bluesky and Decentralization -- Dustycloud Brainstorms"
    url: "https://dustycloud.org/blog/re-re-bluesky-decentralization/?utm_source=tldrnewsletter"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dustycloud-org--bluesky-and-decentralization-dustycloud-brainstorms.md"
    kind: repo
---

The post responds to Bryan Newbold’s reply and says the exchange was generally polite and worthwhile. It also frames the larger disagreement as one of terminology, because the author thinks Bluesky’s use of decentralization language moves the goalposts and hides the role of power distribution in the network.

A central claim is that ATProto’s public shared-heap model does not scale well toward meaningful self-hosting. The author argues that message-passing systems can keep per-node costs flat while a fully decentralized shared-heap system makes each node receive all messages, producing quadratic whole-network costs. The post also contrasts Bluesky’s goals with ActivityPub and Spritely, and says credible exit is valuable but not enough to make the system decentralized.

## Reading notes

- The text responds to Bryan Newbold’s reply and says that the exchange was respectful, but maintains the technical and conceptual criticisms of Bluesky.
- The author maintains that the definitions used by Bryan and by Mark Nottingham weaken “decentralization” and “federation” too much because they leave out the distribution of power.
- The discussion of Paul Baran appears to show that the definition Bryan cited came from a context in which “decentralized” was still a type of hierarchical centralization.
- The post states that “credible exit” is useful, but not enough to call the system decentralized.
- The author argues that ActivityPub and message passing systems scale better when the network grows and when more nodes enter the system.
- For ATProto, he argues that the shared heap architecture with a public firehose imposes quadratic costs when one tries to take decentralization all the way to full user participation.
- The text says that real self-hosting would require fundamental changes to the architecture, bringing the system closer to something more like ActivityPub.
- There is a distinction between the values and stated goals of Bluesky, ActivityPub, and Spritely, with emphasis on data control, agency, collaboration, and healthy communities.
- The closing states that the author does not want to continue an endless back-and-forth and prefers to collaborate on solutions that build the future.
