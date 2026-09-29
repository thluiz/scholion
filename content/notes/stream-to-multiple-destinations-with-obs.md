---
title: "Stream to multiple destinations with OBS"
date: '2020-04-15T13:09:04-03:00'
category: webclip
summary: 'The page explains that OBS streams to one service by default, and shows how a local nginx RTMP server in Docker can relay one OBS stream to multiple services such as Facebook and YouTube.'
tags: ["obs", "rtmp", "docker", "nginx"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Stream to multiple destinations with OBS - B Saravana"
    url: "https://iamsaravana.com/stream-to-multiple-destinations-with-obs/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-04/iamsaravana-com--stream-to-multiple-destinations-with-obs.md"
    kind: repo
---

The page says OBS can stream and record, but by default it sends a stream to only one service at a time. It presents a workaround using a local RTMP server with nginx, run in Docker, so OBS can send one stream to that server and the server can forward it onward.

## Reading notes

- OBS supports major streaming services, but the page says it can stream to only one service simultaneously.
- A local RTMP server with nginx can receive the OBS stream and route it to multiple destinations.
- The page uses the tiangolo/nginx-rtmp Docker image instead of plain nginx because it includes RTMP support.
- The setup steps include pulling the image, running the container, and configuring OBS with a custom streaming server URL and stream key.
- To send the stream to multiple external services, the page says to edit nginx.conf inside the container and add push directives for each service.
- After updating the nginx configuration, the page says to restart nginx.
