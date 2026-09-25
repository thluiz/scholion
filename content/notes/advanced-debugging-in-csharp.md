---
title: "Advanced Debugging in C#"
date: '2026-09-24T23:16:26+01:00'
category: webclip
summary: 'The article shows advanced debugging techniques in Visual Studio 2022 for C#: conditional breakpoints, tracepoints, hit count, filters, code editing, execution pointer, object IDs and string visualizer.'
tags: ["csharp","visual-studio","debugging"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Advanced Debugging in C#"
    url: "https://code-maze.com/csharp-advanced-debugging/?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/code-maze-com--advanced-debugging-in-csharp.md"
    kind: repo
---

The article walks through advanced debugging in C# using Visual Studio 2022. It starts with a simple loop-based example and then shows how breakpoints can be made conditional, turned into tracepoints, limited by hit count, filtered by thread or process, moved to a different line, and combined with code edits during a debugging session.

It also covers function breakpoints, dependent breakpoints, object IDs for tracking reference types across scope changes, and the string visualizer for formatted text such as HTML, JSON, or XML.

## Reading notes

- Uses a simple example with a list of strings, a loop and the `PrintPart()` method to demonstrate debugging techniques in Visual Studio 2022.
- Shows how to configure conditional breakpoints to pause only when an expression is true, such as when the length of `txt` is less than 12.
- Explains tracepoints as breakpoints that write messages in the Output window without interrupting execution, with support for conditions and keywords such as `$FUNCTION` and `$CALLER`.
- Presents hit count to make a breakpoint stop only after a defined number of occurrences, including the option to act on multiples of a value.
- Describes the Filter condition to restrict breakpoints to machine, thread or process, using fields such as `ThreadId`, `ProcessName`, `ProcessId` and `MachineId`.
- Shows that it is possible to change the location of a breakpoint during debugging by changing the line number.
- Says that code can be edited in the middle of a debugging session and that execution continues from the changes made.
- Explains the execution pointer as the yellow arrow that indicates the next line to execute and can be moved to alter the execution flow.
- Presents function breakpoints to make the debugger stop at a specific function.
- Shows dependent breakpoints, in which a breakpoint is only hit after another breakpoint has already been hit.
- Explains object IDs as a way to track a reference object even after it goes out of scope.
- Shows the string visualizer as a tool to view formatted strings, including HTML, JSON and XML, using the Immediate window to assign a complex value.
