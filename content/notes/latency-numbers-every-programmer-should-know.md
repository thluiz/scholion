---
title: "Latency Numbers Every Programmer Should Know"
date: '2026-11-25T16:23:42+00:00'
category: webclip
summary: 'Tabulated latency comparison of hardware, networks, disks and modern LLM operations, using nanoseconds and relative factors to show how different operations compare.'
tags: ["performance", "latency", "systems", "llm"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Latency Numbers Every Programmer Should Know"
    url: "https://gist.github.com/jboner/2841832"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/gist-github-com--latency-numbers-every-programmer-should-know.md"
    kind: repo
---

Latency Comparison Numbers (~2012 except when noted) lists typical delays for cache, memory, storage, networking and recent LLM operations, expressed in nanoseconds, microseconds and milliseconds. The table also highlights relative slowdowns between layers, such as cache vs. memory vs. disk, and adds notes on where the newer LLM figures come from.

## Reading notes

- L1 cache access is about 0.5 ns, and an L2 cache reference is 7 ns, which is described as roughly 14 times slower than L1.
- A branch misprediction costs about 5 ns, which is an order of magnitude above a single L1 cache reference but still much cheaper than main memory.
- A mutex lock and unlock operation is listed at 25 ns, placing it between L2 cache access and main memory reference in terms of cost.
- Accessing main memory takes about 100 ns, which is stated as 20 times slower than L2 cache and 200 times slower than L1 cache.
- Compressing 1 KB with Zippy takes about 3,000 ns (3 us), showing that a small compression operation is already tens of times slower than a memory load.
- Sending 1 KB over a 1 Gbps network takes about 10,000 ns (10 us), providing a baseline for local network transfer latency for small payloads.
- A random 4 KB read from an SSD is around 150,000 ns (150 us), with an indicated throughput of about 1 GB/s for such SSDs.
- Reading 1 MB sequentially from memory is given as 250,000 ns (250 us), which provides a comparison point for sequential throughput from RAM.
- A round trip within the same datacenter is listed as 500,000 ns (500 us), giving a typical intra-datacenter network latency.
- Reading 1 MB sequentially from SSD takes about 1,000,000 ns (1 ms), with a note of roughly 1 GB/s SSD bandwidth and about four times the time for the same size read from memory.
- A disk seek is about 10,000,000 ns (10 ms), described as 20 times slower than a datacenter round trip, illustrating the high cost of mechanical movement.
- Reading 1 MB sequentially from disk is 20,000,000 ns (20 ms), marked as roughly 80 times slower than reading from memory and 20 times slower than from SSD.
- Several entries describe local LLM behavior in 2026: generating one token on a small model with a consumer GPU is about 15,000,000 ns (15 ms).
- Hosted frontier LLMs are listed at about 20,000,000 ns (20 ms) per token for generation in 2026, showing similar per-token time to a disk read of 1 MB.
- Local LLM time to first token for a small model with a short prompt in 2026 is 75,000,000 ns (75 ms), separating initial latency from steady-state token generation.
- Local LLM generation on CPU without GPU acceleration is shown at 100,000,000 ns (100 ms) per token for a small model in 2026.
- A packet round trip from California to the Netherlands and back is listed at 150,000,000 ns (150 ms), reflecting typical intercontinental network latency.
- A fast LLM on specialized inference hardware in 2026 has a time to first token around 250,000,000 ns (250 ms), again focusing on startup latency.
- Time to first token for a frontier LLM with a short prompt and no cache in 2026 is around 1,000 ms, making the initial response comparable to a slow human reaction time.
- A frontier LLM short response of roughly 100 output tokens in 2026 is given as about 3,000 ms (3 s), illustrating end-to-end completion time for a small answer.
- A frontier LLM long context prefill of about 100K input tokens without cache in 2026 is about 10,000 ms (10 s), underscoring the cost of large-context setup.
- A frontier LLM reasoning response as a single call with thinking in 2026 is around 30,000 ms (30 s), indicating that complex reasoning runs can be orders of magnitude slower than basic token emission.
- The notes clarify unit conversions: 1 ns is 10^-9 seconds, 1 us is 10^-6 seconds or 1,000 ns, and 1 ms is 10^-3 seconds, equal to 1,000 us or 1,000,000 ns.
- Credit is attributed to Jeff Dean, with a link to his profile, and the original numbers credited to Peter Norvig through a referenced page.
- Additional contributions mention a humanized comparison, a visual comparison chart image, and an interactive Prezi version, providing alternative ways to view the latency data.
