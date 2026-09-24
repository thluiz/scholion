---
title: "Secret Productivity Tips for Visual Studio 2017"
date: '2026-09-25T00:50:18+01:00'
category: webclip
summary: 'The post lists Visual Studio 2017 features that are disabled by default, showing where to enable them and how they help with search, analysis, unit testing, style enforcement, and shortcuts.'
tags: ["visual-studio-2017", "productivity", "csharp", "editorconfig"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Secret Productivity Tips for Visual Studio 2017"
    url: "https://dev.to/rionmonster/secret-productivity-tips-for-visual-studio-2017"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--secret-productivity-tips-for-visual-studio-2017.md"
    kind: repo
---

The post collects Visual Studio 2017 features that are disabled by default and shows how to turn them on locally or globally. It focuses on tools that help with package suggestions, search, solution analysis, loading, unit testing, style enforcement, and keyboard shortcuts.

## Fichamento

- Most of the features in the post are disabled by default, so they must be enabled locally per project or globally.
- The NuGet-based using suggestion recommends a NuGet package when the editor finds an unrecognized type.
- Go To All supports query prefixes for files, types, members, and symbols, which narrows searches inside a solution.
- Full Solution Analysis shows errors, messages, and warnings across the whole solution instead of only open files.
- Lightweight Solution Load opens only the minimum needed for each project and delays loading files and dependencies until they are requested.
- Live Unit Testing runs affected tests automatically after code changes and marks code with icons that show coverage and test status.
- EditorConfig support helps teams keep a consistent coding style across a codebase.
- The suggestion ellipsis color can be adjusted in the IDE to make style suggestions easier to see.
- Mads Kristensen's EditorConfig extension adds autocompletion and syntax highlighting for .editorconfig files.
- The HotKeys Keyboard Shortcuts extension lets Visual Studio 2017 use shortcuts from editors and tools such as IntelliJ and Eclipse.
