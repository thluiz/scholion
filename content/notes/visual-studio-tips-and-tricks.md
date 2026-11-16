---
title: "Visual Studio tips and tricks"
date: '2026-11-16T18:44:49+00:00'
category: webclip
summary: 'A collection of Visual Studio shortcuts, debugger, solution, editor, and extension tips drawn from the #vstip hashtag, aimed at making common workflows faster and easier.'
tags: ["visual-studio", "productivity", "debugger", "extensions"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Visual Studio tips and tricks"
    url: "https://devblogs.microsoft.com/visualstudio/visual-studio-tips-and-tricks/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devblogs-microsoft-com--visual-studio-tips-and-tricks.md"
    kind: repo
---

A collection of Visual Studio tips gathered from the #vstip hashtag, organized around debugging, solution management, editor use, miscellaneous settings, and extensions. It presents specific shortcuts and features that help speed up common development tasks.

## Reading notes

- F10 starts build, run, and debugger attachment and breaks on the first execution of your own code without breakpoints.
- Reattach to process with Shift+Alt+P is useful when you need to attach to the same process repeatedly.
- A blue dot in the margin marks a thread switch while stepping through debugging.
- Disabling restore of node expansions and Reopen documents on solution load reduces visual noise and improves solution load performance.
- Ctrl+T helps find files, classes, and other items in a solution through keyboard navigation.
- A keyboard shortcut can be assigned to run git pull without using CLI or Team Explorer.
- Solution Explorer can automatically select the current active document so its location in the project is easier to track.
- Shift+Alt+W surrounds HTML elements with a div, selects the inserted tag, and auto-matches the closing tag.
- Copying a JSON fragment can paste it as strongly typed .NET classes into C# or VB files.
- Visual Studio inserts quotation marks for JSON property names after you type a colon.
- Holding Control makes IntelliSense and tooltips semi-transparent.
- Ctrl+Shift+Space shows the current overload instead of retyping an opening parenthesis for parameter info.
- Visual Studio can play sounds for certain events.
- Custom window layouts can be created for different development scenarios or monitor setups.
- Visual Studio can prompt users to install required components for a solution when they are missing.
- Visual Studio Spell Checker checks comments, strings, and plain text as you type or across a solution, project, or selected items.
- Add New File lets you create a new file quickly with Shift+F2.
- Git Diff Margin shows live Git changes of the current file in the margin and scroll bar.
- The post points readers to the Visual Studio Marketplace for more extensions and invites people to share more tips with #vstip.
