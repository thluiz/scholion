---
title: "Mastering C# Pattern Matching"
date: '2026-09-25T19:28:36+01:00'
category: webclip
summary: 'The post reduces a lock gate example to a C# switch expression with pattern matching. It shows how underscores replace repeated cases and how invalid states still throw exceptions.'
tags: ["csharp", "pattern-matching", "switch-expression", "state-machine"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Mastering C# – Pattern Matching"
    url: "https://jesseliberty.com/2025/01/16/mastering-c-pattern-matching/?utm_source=newsletter.csharpdigest.net&utm_medium=newsletter&utm_campaign=the-impact-of-locks-and-waits-on-latency&_bhlid=e5606aad9f3e29637bbb5934351f5e4772f95516"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/jesseliberty-com--mastering-csharp-pattern-matching.md"
    kind: repo
---

The post takes Microsoft’s lock example and strips it down to the core idea of pattern matching in a C# switch expression. It models the gate as a state machine and shows how the gate’s next state depends on the requested setting, the current gate state, and the water level.

## Reading notes

- The example uses a gate and water level to model a lock.
- The first three cases all end with the gate closed, so they can be grouped into one pattern.
- When the new state is open and the water level is high, the gate opens.
- When the new state is open and the water level is low, the code throws an exception.
- The underscore matches anything, which makes the default case simpler.
- The final method uses a switch expression instead of a longer set of if statements or switch statements.
