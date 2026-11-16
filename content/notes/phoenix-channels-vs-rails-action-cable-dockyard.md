---
title: "Phoenix Channels vs Rails Action Cable"
date: '2016-08-25T21:25:32+00:00'
category: webclip
summary: 'The article compares Phoenix Channels and Rails Action Cable with chat-app benchmarks, reporting a Rails memory leak and slower broadcasts under load, while Phoenix keeps steady latency as traffic grows.'
tags: ["phoenix-channels", "rails-action-cable", "benchmarking", "real-time"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Phoenix Channels vs Rails Action Cable - DockYard"
    url: "https://dockyard.com/blog/2016/08/09/phoenix-channels-vs-rails-action-cable"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dockyard-com--phoenix-channels-vs-rails-action-cable-dockyard.md"
    kind: repo
---

The article compares Phoenix Channels and Rails Action Cable through chat-app benchmarks built in both frameworks. It reports a memory leak in the Rails app and shows Action Cable slowing down as room counts and subscribers increase, while Phoenix keeps similar broadcast latency under higher load.

## Reading notes

- DockYard says it moved from Ruby and Rails to Elixir and Phoenix because Phoenix better fit client needs for modern web work.
- The team built the same chat application in both frameworks and used tsung to open WebSocket connections, join rooms, and publish messages under different workloads.
- On the Rails side, they immediately observed a memory leak when refreshing the browser and watching memory grow.
- They found a reported Action Cable issue about failing to call socket.close during cleanup, applied the unreleased stable branch patch, and still saw the leak.
- With 50 users per room, Rails stayed responsive at 50 rooms but fell behind at 75 rooms, where average broadcast latency reached 8 seconds.
- With the same 50 users per room test, Phoenix handled 1100 rooms and 55,000 users, with average latency around 0.25 seconds.
- The article says Action Cable’s performance under this load suggests horizontal scaling needs and a central Redis bottleneck for PubSub.
- With 200 users per room, Rails started with acceptable latency, then quickly fell behind as broadcast latency passed 10 seconds.
- At 200 users per room, Rails supported 9 rooms before messages stopped arriving or subscriptions failed, with more consistent performance at 7 rooms.
- Phoenix handled 275 rooms and 55,000 users in the 200 users per room test, with average latency around 0.24 seconds.
- The article concludes that Action Cable is best suited to small workloads with few subscribers per topic, while Phoenix keeps steadier performance as demand grows.
