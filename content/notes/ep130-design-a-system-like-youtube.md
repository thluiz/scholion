---
title: "EP130: Design a System Like YouTube"
date: "2026-09-23T18:49:10+01:00"
category: webclip
has_commentary: false
summary: "Covers eight Software Development Life Cycle models and a 9-step pipeline for a YouTube-like video system, from upload through transcoding to CDN delivery."
tags:
  - system-design
  - video-streaming
  - sdlc
  - software-architecture
sources:
  - title: "EP130: Design a System Like YouTube"
    url: "https://blog.bytebytego.com/p/ep130-design-a-system-like-youtube?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/blog-bytebytego-com--ep130-design-a-system-like-youtube.md"
    kind: repo
---

A ByteByteGo refresher pairs two topics: eight Software Development Life Cycle models and a 9-step pipeline for a video platform shaped like YouTube.

## Reading notes

- SDLC models: Waterfall runs linear phases (requirements, design, implementation, verification, maintenance); Agile works in sprints under Scrum, Kanban, or XP; V-Model pairs each development phase with its own testing phase; Iterative builds the system incrementally; Spiral combines iteration with Waterfall's risk analysis; Big Bang skips planning and integrates everything at once; RAD prioritizes rapid prototyping; Incremental designs, builds, and tests in stages until the product is done.
- Video upload starts with the user submitting the video file and its details, which go to object storage (S3) while metadata is saved to a database and a cache.
- Raw video moves to a transcoding server that encodes it into the bitrates and formats needed for streaming, then the transcoded output lands in a separate object storage.
- A message queue carries the transcoding-complete notification to a Transcoding Status Handler, which updates the metadata database and cache.
- Playback requests hit a CDN, which pulls the video from object storage and caches it locally so later requests for the same video skip the origin fetch.
