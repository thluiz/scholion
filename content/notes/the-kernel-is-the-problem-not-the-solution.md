---
title: "The Secret to 10 Million Concurrent Connections: The Kernel Is the Problem, Not the Solution"
date: '2013-05-15T18:06:53-03:00'
category: webclip
summary: 'The article argues that 10 million concurrent connections require moving packet handling, scheduling, and memory management out of the kernel and into application code, while Linux stays on the control plane.'
tags: ["c10m", "kernel", "data-plane", "scalability"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "High Scalability - High Scalability - The Secret to 10 Million Concurrent Connections -The Kernel is the Problem, Not the Solution"
    url: "http://highscalability.com/blog/2013/5/13/the-secret-to-10-million-concurrent-connections-the-kernel-i.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-05/highscalability-com--the-kernel-is-the-problem-not-the-solution.md"
    kind: repo
---

The article says the C10M challenge is met by treating Unix as control plane and moving data-plane work into the application. Kernel scheduling, packet handling, and memory management become bottlenecks, so the software must take over those tasks directly.

It then breaks scalability into packet, multi-core, and memory problems. The proposed approach uses custom drivers, user-mode packet processing, per-core data, lock-free or atomic coordination where needed, careful memory layout, and hugepages so the application can keep up with millions of connections.

## Reading notes

- Unix was originally framed as a control system, but it is now being used as part of the data plane.
- The kernel is presented as the problem because it should not do all the heavy lifting for packet handling, memory management, and processor scheduling.
- For 10 million concurrent connections, Linux should handle the control plane while the application handles the data plane.
- The article contrasts control-plane-oriented systems with data-plane-oriented systems and says the latter can process more packets per second.
- The C10K problem is described as having been solved by fixing kernels and shifting from thread-per-connection servers to event-driven servers like Nginx and Node.
- Apache is used as the example of a model where more connections mean worse performance.
- Performance and scalability are described as different concepts.
- The article says the next scale jump requires packet scalability, multi-core scalability, and memory scalability.
- Packet scaling is framed as bypassing the Unix network stack with custom drivers such as PF_RING, Netmap, or Intel DPDK.
- Multi-core scaling is treated as different from multi-threading, with emphasis on per-core data, atomics, lock-free structures, threading model, and processor affinity.
- Memory scaling focuses on cache misses, co-locating data, preallocating memory, paging-table overhead, NUMA effects, memory pools, hyper-threading, and hugepages.
- The closing summary says Linux should keep the first two CPUs and the application should manage the remaining CPUs, with the data plane running in application code and not interacting with the kernel.
