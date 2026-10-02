---
title: "Jitsi Videobridge Performance Evaluation"
date: '2020-05-03T10:14:16-03:00'
category: webclip
summary: 'The page reports load tests on Jitsi Videobridge, showing that a single conference with 1056 streams reached about 550 Mbps while using about 20% CPU on a Xeon server.'
tags: ["jitsi-videobridge", "performance-testing", "sfu", "bitrate"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Jitsi Videobridge Performance Evaluation | Performance Testing"
    url: "https://jitsi.org/jitsi-videobridge-performance-evaluation/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-05/jitsi-org--jitsi-videobridge-performance-evaluation.md"
    kind: repo
---

The page presents performance tests for Jitsi Videobridge on an unmodified Jitsi Meet installation running on a dedicated Xeon server. It measures conferences, endpoints, CPU usage, and network throughput, and says the system handled more than 1000 video streams at about 550 Mbps with low CPU use.

## Reading notes

- The tests were run on a dedicated server with nginx, prosody, and Jitsi Videobridge, using a quad-core Intel Xeon E5-1620 v2 CPU.
- The measured variables were conferences, endpoints, CPU usage, network in, and network out.
- The extracted values included bitrate and streams.
- The test used one Chrome instance as the conference focus, with camera and microphone muted.
- The other endpoints used Jitsi Hammer and streamed pre-recorded audio and video at about 515 Kbps per endpoint.
- The setup used a full-star topology so that incoming traffic from each endpoint was propagated to every other endpoint.
- The page says this creates K*(K-1) streams leaving the videobridge.
- Tests were run with K = 10, 15, 20, 25, 29, and 33.
- The page says that in practice large conferences would use Last N mode so only the most recent speakers are distributed and shown.
- In one run, 33 load generators caused Jitsi Videobridge to distribute 1056 streams and bandwidth use went above 550 Mbps.
- The same run used about 20% CPU.
- The page says CPU usage increases nearly linearly with total bitrate.
- It compares 1056 video streams to 528 one-to-one conferences, 176 3-person conferences, or 53 conferences with 5 people.
- The JVM was run with a 3 GB memory limit and did not exceed it.
- The Jitsi Videobridge process RSS never exceeded 1500 MB.
- A later run increased the stream count from 90 to 812 and then to 1056, with CPU usage staying stable in the intervals used for averaging.
- The reported averages are 90 streams at 47.6 Mbps and 3.1% CPU, 380 streams at 199.4 Mbps and 8.0% CPU, 600 streams at 314.7 Mbps and 11.7% CPU, 812 streams at 425.5 Mbps and 15.7% CPU, and 1056 streams at 550.4 Mbps and 20.3% CPU.
