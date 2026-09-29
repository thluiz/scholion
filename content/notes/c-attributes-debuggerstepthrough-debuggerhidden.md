---
title: "C# attributes you should know #2: [DebuggerStepThrough] and [DebuggerHidden]"
date: '2022-04-20T18:13:33-03:00'
category: webclip
summary: 'The post explains how [DebuggerStepThrough] lets code run without being debugged, how [DebuggerHidden] hides code from the debugger, and how they differ in the Call Stack.'
tags: ["csharp", "debugging", "attributes", "call-stack"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "C# attributes you should know #2: [DebuggerStepThrough] and [DebuggerHidden] – A Girl Among Geeks"
    url: "https://agirlamonggeeks.com/2017/12/12/c-attributes-you-should-know-2-debuggerstepthrough-and-debuggerhidden/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-04/agirlamonggeeks-com--c-attributes-debuggerstepthrough-debuggerhidden.md"
    kind: repo
---

The post compares two C# debugging attributes. [DebuggerStepThrough] lets code execute without being debugged and can be applied to a class, struct, constructor, or method. [DebuggerHidden] also keeps code from being debugged, but it applies only to constructors, methods, and properties.

The main difference shown is in the Call Stack. Code marked with [DebuggerStepThrough] appears as external code, while code marked with [DebuggerHidden] does not appear there at all. The post also notes that with JMC enabled, breakpoints can still be hit even when [DebuggerStepThrough] is present.

## Reading notes

- [DebuggerStepThrough] executes code without debugging it, even if a breakpoint is set inside the block.
- It can be applied to a class, struct, constructor, or method.
- Breakpoints in code with this attribute are shown as non-hitable in debugging mode, except when JMC is enabled.
- [DebuggerHidden] is similar, but it can be applied only to a constructor, method, or property.
- [DebuggerStepThrough] still shows the code in the Call Stack as external code.
- [DebuggerHidden] removes the code from the Call Stack display entirely.
- The example uses a Car object and a DriveThroughMud() method to show the difference.
- The author prefers [DebuggerStepThrough] because it still provides Call Stack information and can be used on an entire class.
