---
title: "Everything You Know About Latency Is Wrong"
date: '2016-01-02T12:20:04-03:00'
category: webclip
summary: 'The post argues that latency must be understood as a full distribution, not as averages or a few percentiles, and that coordinated omission makes many benchmarks and monitors lie about response time.'
tags: ["latency", "benchmarking", "percentiles", "coordinated-omission"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Everything You Know About Latency Is Wrong"
    url: "http://bravenewgeek.com/everything-you-know-about-latency-is-wrong/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-01/bravenewgeek-com--everything-you-know-about-latency-is-wrong.md"
    kind: repo
---

The post says latency should be treated as the time for each operation, so it has to be understood as a full distribution. Averages, medians, and even a small set of percentiles hide hiccups, tail behavior, and the maximum values that often matter most.

## Reading notes

- Latency is one operation’s time, so one million operations produce one million latencies.
- Latency almost never follows a normal, Gaussian, or Poisson distribution.
- Hiccups can come from GC pauses, hypervisor pauses, context switches, interrupts, database reindexing, or disk flushes.
- Looking only at the 95th percentile hides bad behavior.
- Averaging percentiles is mathematically meaningless.
- The maximum value should not be discarded, because it can be the signal.
- The 99th percentile is not rare in real web page loads.
- The median is not a useful description of typical response time.
- Monitoring systems often stop at the 95th or 99th percentile because the data is stored in short windows.
- Coordinated omission happens when measurement skips the periods when the system is slow.
- Load generators and monitoring code can end up measuring service time instead of response time.
- A stall can make a system look much better than it is.
- Better changes can look worse if the measurement has coordinated omission.
- Latency has to be measured in the context of load, not only when the system is idle or fully saturated.
- The post recommends HdrHistogram for high-resolution latency capture and correction for coordinated omission.
