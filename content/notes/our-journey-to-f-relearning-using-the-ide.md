---
title: "Our journey to F#: Relearning using the IDE"
date: '2026-11-16T04:38:56+00:00'
category: webclip
summary: 'The author describes how switching to F# changed IDE habits in Rider, from file navigation and code organization to IntelliSense and solution-wide analysis, with some features working less smoothly than in C#.'
tags: ["f-sharp", "jetbrains-rider", "intellisense", "solution-wide-analysis"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Our journey to F#: Relearning using the IDE"
    url: "https://planetgeek.ch/2020/07/17/our-journey-to-f-relearning-using-the-ide"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/planetgeek-ch--our-journey-to-f-relearning-using-the-ide.md"
    kind: repo
---

The author says that after a month of programming in F#, using Rider started to feel different. The main changes were in how to read files, how to group code into modules, how to trigger IntelliSense, and how much the IDE could help with solution-wide analysis.

## Reading notes

- In F#, the important code is often at the end of the file, after earlier function and type definitions.
- The Structure tool window helped the author adapt to that reversed reading order.
- In C#, each class usually lived in its own file, but in F# closely related code was grouped into the same module and the same file.
- Because F# code was shorter and the Structure view gave a better overview, switching files became less necessary.
- At first, calling functions from another module was difficult because Rider did not immediately help with IntelliSense.
- Typing the module name followed by a dot let Rider show the module’s functions and add the module to the list of opened modules.
- `Ctrl+Space` worked better than `Alt+Enter` for including modules, even when the module name was already correct.
- The author was very satisfied with solution-wide analysis in Rider/ReSharper for C#, but less so for F#.
- It was not always clear when Rider would detect errors after a code change, so the author built the code more often.
- The issue may have been related to using F# together with C# through inter-op.
- Rider could not show F# changes that depended on changes in C# without a build.
- The author expects this to matter less when writing complete features in F# with less inter-op.
