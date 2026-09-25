---
title: "How Discord Reduced Websocket Traffic by 40%"
date: '2026-09-25T08:01:36+01:00'
category: webclip
summary: 'Discord reduced gateway bandwidth by replacing zlib with tuned zstandard, then cutting passive session snapshots with PASSIVE_UPDATE_V2, reaching almost 40% less traffic overall.'
tags: ["discord","websocket","compression","bandwidth"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How Discord Reduced Websocket Traffic by 40%"
    url: "https://discord.com/blog/how-discord-reduced-websocket-traffic-by-40-percent?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/discord-com--how-discord-reduced-websocket-traffic-by-40-percent.md"
    kind: repo
---

Discord first tested plain zstandard against zlib and found it worse, because zlib was using streaming compression while zstandard was not. After adding streaming support, tuning compression settings, and rolling it out across clients, zstandard outperformed zlib on ratio and compression time.

The team also tried zstandard dictionaries, but the gains were small or mixed and not worth the added complexity. A separate optimization, PASSIVE_UPDATE_V2, replaced full snapshots in passive sessions with deltas and cut that traffic from 35% to 5%, bringing the combined bandwidth reduction to almost 40%.

## Reading notes

- The text describes the attempt to reduce the bandwidth used by clients, especially on iOS and Android, to make the experience more responsive.
- The gateway was already using zlib with compression since the end of 2017.
- The team evaluated zstandard as a replacement, because it offers better compression ratios, lower compression time, and support for dictionaries.
- The initial test used a dark launch of zstandard without streaming and the result was worse than zlib.
- The main difference was that zlib used streaming compression and zstandard did not.
- Since the loads were small, the lack of history hurt zstandard.
- The team chose ezstd, added streaming support by forking, and later contributed the change back to the original project.
- With zstandard in streaming, the compression ratio and payload sizes improved, and compression time dropped.
- The team then adjusted chainlog, hashlog, and windowlog, choosing level 6, chainlog 16, hashlog 16, and windowlog 18.
- The group also tested zstandard dictionaries with anonymized data from 120 thousand messages, separated between JSON and ETF.
- The dictionaries brought small gains in READY and mixed results in other payloads.
- Because of the extra complexity, the team gave up on the dictionaries.
- There was also a test of increasing buffers during times of lower usage, but the strategy was reverted because of memory fragmentation and tuning cost.
- The final rollout brought zstandard to desktop, iOS, and Android users, with platform-specific bindings and an experiment to allow quick rollback.
- In another front, the text explains that PASSIVE_UPDATE_V1 sent large snapshots for passive sessions, even when little changed.
- The new PASSIVE_UPDATE_V2 started sending only the delta and reduced that traffic from 35% to 5%.
- Combining zstandard and PASSIVE_UPDATE_V2, the text says that bandwidth usage dropped by almost 40%.
