---
title: "Improvements in .NET Core 3.0 for troubleshooting and monitoring distributed apps"
date: '2020-10-19T17:16:55-03:00'
category: webclip
summary: 'The post shows how ASP.NET Core 3.0 correlates logs across services, propagates distributed trace context, supports W3C Trace Context, and integrates with OpenTelemetry and baggage.'
tags: ["dotnet-core", "aspnet-core", "distributed-tracing", "opentelemetry"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Improvements in .NET Core 3.0 for troubleshooting and monitoring distributed apps | ASP.NET Blog"
    url: "https://devblogs.microsoft.com/aspnet/improvements-in-net-core-3-0-for-troubleshooting-and-monitoring-distributed-apps/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-10/devblogs-microsoft-com--improvements-dotnet-core-3-0-troubleshooting-monitoring-dist.md"
    kind: repo
---

ASP.NET Core 3.0 improves troubleshooting and monitoring for distributed apps by propagating trace context across components, correlating logs through the same TraceId, and supporting W3C Trace Context. The post also shows how Activity starts distributed tracing in any .NET Core app, how OpenTelemetry can collect the same trace, and how baggage can carry extra context such as app version.

## Reading notes

- Distributed apps are harder to operate because a single request spans multiple components, often owned by different teams, which makes it difficult to trace the root cause and correlate logs.
- ASP.NET Core 3.0 initializes distributed trace context on incoming requests and passes it along so logs from separate apps share the same TraceId.
- In a .NET Core app outside ASP.NET Core, creating and starting an Activity is enough to propagate distributed trace context through HttpClient.
- The app can switch to W3C Trace Context by setting Activity.DefaultIdFormat to ActivityIdFormat.W3C in Main.
- With W3C Trace Context enabled, incoming requests carry a traceparent header, and ASP.NET Core uses that format for outgoing calls.
- OpenTelemetry can collect distributed traces and metrics, and the same TraceId appears in both logs and tracing tools such as Zipkin.
- Even if one ASP.NET Core service in the middle does not use telemetry SDKs, it still propagates distributed trace context and keeps the trace connected.
- In service mesh setups, ASP.NET Core apps can propagate the headers that proxies need to stitch spans into one trace.
- Activity.Baggage can carry extra context such as appVersion across requests.
- That baggage can be read on the server and added to logging scope so logs include the extra context.
