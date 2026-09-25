---
url: "https://papers.cloudcat.dev/blogs/net-9-exception-overhead?ref=dailydev"
captured_at: "2026-09-25T18:39:42+01:00"
title: "How expensive is exception throwing in .NET 9?"
domain: "papers-cloudcat-dev"
---

Throughout the history of .NET development, a major concern has been the performance overhead associated with throwing exceptions. Best practices have emerged, suggesting that exceptions should be reserved for truly exceptional situations to ensure optimal application efficiency.

But is this practice still relevant today?

In this blog post, we'll explore the performance overhead of using try-catch blocks and throwing exceptions in .NET 9.

![Dimage](https://papers.cloudcat.dev/assets/images/image-cd924275a71ad9375908091e01116203.jpeg "cat looking at metrics")

## Benchmark[​](#benchmark "Direct link to Benchmark")

**Processor Used**: Qualcomm Snapdragon X Elite - X1E-78-100

**Benchmarking Tool**: BenchmarkDotNet v0.14.0

**Operating System**: Windows 11 (10.0.26100.2605)

**.NET SDK**: 9.0.101

[https://github.com/Snazzie/DotNet-TryCatchThrow-Benchmark](https://github.com/Snazzie/DotNet-TryCatchThrow-Benchmark)

```
| Method                   | Mean       | Error    | StdDev   | Gen0   | Allocated ||------------------------- |-----------:|---------:|---------:|-------:|----------:|| TryCatch_NoError         |   448.1 ns |  1.50 ns |  1.33 ns | 0.0095 |      40 B || NoTryCatch_NoError       |   449.9 ns |  1.24 ns |  1.03 ns | 0.0095 |      40 B || TryCatch_WithErrorOption |   442.8 ns |  1.67 ns |  1.56 ns | 0.0095 |      40 B || TryCatch_WithThrow       | 2,256.7 ns | 15.10 ns | 13.38 ns | 0.0839 |     360 B |
```

## Insights[​](#insights "Direct link to Insights")

### Minimal Overhead for Try-Catch[​](#minimal-overhead-for-try-catch "Direct link to Minimal Overhead for Try-Catch")

The mean execution times for Try Catch without exceptions throwing are nearly identical, demonstrating that the presence of a try-catch block itself doesn't add noticeable overhead.

### Exception Throwing Overhead[​](#exception-throwing-overhead "Direct link to Exception Throwing Overhead")

The TryCatch\_WithThrow method shows a relative increase in execution time and memory allocation compared to the other methods. An overhead of ~0.002 milliseconds and additional 320 bytes of memory allocated for throwing and catching an exception, demonstrating that there is still in fact a cost to throwing and catching exceptions.

## Conclusion[​](#conclusion "Direct link to Conclusion")

While throwing and catching exceptions in .NET 9 still have a cost, benchmark result suggests this overhead is minimal and will go un-noticed in most cases. Strictly reserving exceptions for truly exceptional circumstances is not as important as it once was, but is still beneficial for optimizing application efficiency. Depending on the project needs, it is worth weighing the cost of developer time to produce and maintain graceful error handling vs bubbling up exceptions.

It is also important to keep in mind that this is a very simple synthetic benchmark, the cost could be much greater in a large code base where exceptions bubble up from great depths or where hardware resources are limited.

Feel free to dive into the benchmark code and share your thoughts on these findings or any improvements!
