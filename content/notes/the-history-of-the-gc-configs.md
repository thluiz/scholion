---
title: "The history of the GC configs"
date: '2019-11-04T15:32:47+00:00'
category: webclip
summary: 'The post traces how .NET GC configuration grew from a few supported app configs and startup flags to a larger set in .NET 4.x and Core 3.0, while arguing that supported configs should stay usable without deep internal GC knowledge.'
tags: ["dotnet", "gc", "runtime-config", "performance"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The history of the GC configs"
    url: "https://devblogs.microsoft.com/dotnet/the-history-of-the-gc-configs/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devblogs-microsoft-com--the-history-of-the-gc-configs.md"
    kind: repo
---

The post traces how GC configuration in .NET moved from a very small set of officially supported options to a broader set across .NET 4.x and Core 3.0. It also explains why some settings were added only for specific workloads, why env vars and startup flags were used, and why supported configs should stay understandable with general performance knowledge rather than internal GC details.

## Reading notes

- Early .NET exposed very few public GC configs, mainly gcServer and gcConcurrent, plus a startup flag for retaining the VM.
- App configs under the runtime element were the main official way to configure the CLR.
- COMPlus environment variables existed, but they were used mostly for internal testing and were not documented as app configs.
- Startup flags through the hosting API were rare, and many customers avoided them.
- For app-configurable settings, the runtime could read values from app config, env vars, or registry values.
- In .NET 4.x, new public configs were added for cases such as CPU groups and objects larger than 2 GB.
- Around .NET 4.6, more configs were added for stressful workloads, including GCHeapCount, GCNoAffinitize, and GCHeapAffinitizeMask.
- After coreclr was open sourced, the split between internal and officially supported configs remained, though the boundary became easier to see.
- Core changed how config values were read, so runtimeconfig.json and environment variables use different lookup paths.
- Core 3.0 unified the source, making .NET GC configs available on Core as well.
- Later additions included GCHeapHardLimit, GCLargePages, and GCHeapAffinitizeRanges.
- Values passed through env vars are interpreted as hexadecimal, not decimal.
- The author argues that supported configs should be based on general memory and CPU knowledge, not on detailed internal GC behavior.
- The author does not want configs that require users to choose collection behavior based on generation-specific internal heuristics.
