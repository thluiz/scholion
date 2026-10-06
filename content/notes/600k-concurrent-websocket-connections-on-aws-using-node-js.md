---
title: "600k concurrent websocket connections on AWS using Node.js"
date: '2015-04-16T15:30:24-03:00'
category: webclip
summary: 'The post explains how to push an AWS EC2 instance toward 600k persistent websocket connections by choosing Node.js, using ws and sticky-session, and raising V8 and system limits.'
tags: ["nodejs", "websocket", "aws-ec2", "performance-tuning"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "600k concurrent websocket connections on AWS using Node.js - Jayway"
    url: "http://www.jayway.com/2015/04/13/600k-concurrent-websocket-connections-on-aws-using-node-js/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-04/jayway-com--600k-concurrent-websocket-connections-on-aws-using-node-js.md"
    kind: repo
---

The post describes how to squeeze as much capacity as possible out of an AWS EC2 instance at the lowest cost by using concurrent persistent websockets. It says Node.js fits this use case because it is event-driven and non-blocking, then narrows the stack to lighter tools and higher system limits.

## Reading notes

- Socket.io was the first choice, but ws was preferred because it is lighter and Socket.io v1.0 no longer works with the cluster module.
- ws needs manual keepalive handling with ping methods, and AWS load balancer timeouts must stay above the keepalive interval.
- sticky-session is used so Node.js can run across all CPUs, which is needed for a high connection count.
- An M3.xlarge EC2 instance is presented as the choice for reaching about 620k connections, with 4 CPUs and 15 GB of memory.
- At that scale, CPU load stays at 100% and V8 garbage collection becomes the main limiting factor.
- The recommended stable limit is 600k connections before scaling to another instance.
- A larger M3.2xlarge instance can reach 800k connections, but cost and Linux network handling become limiting factors.
- The Node.js flags listed are --nouse-idle-notification, --expose-gc, --max-old-space-size=8192, and --max-new-space-size=2048.
- The EC2 setup also raises nofile limits to 1000000 and increases fs.file-max, fs.nr_open, netfilterip_conntrack_max, and nf_conntrack_max.
- The conntrack limit matters because the default value of 65536 would prevent higher connection counts.
