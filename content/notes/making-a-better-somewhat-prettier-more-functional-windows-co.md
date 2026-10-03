---
title: "Making a better, somewhat prettier, but definitely more functional Windows Command Line"
date: '2016-07-24T19:14:51-03:00'
category: webclip
summary: 'Scott Hanselman lists Windows command-line tools that add editing, completion, tabs, SSH, and better terminal handling, arguing that Windows still needs a more polished console experience.'
tags: ["windows-command-line", "terminal-tools", "powershell", "ssh"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Making a better, somewhat prettier, but definitely more functional Windows Command Line - Scott Hanselman"
    url: "http://www.hanselman.com/blog/MakingABetterSomewhatPrettierButDefinitelyMoreFunctionalWindowsCommandLine.aspx"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-07/hanselman-com--making-a-better-somewhat-prettier-more-functional-windows-co.md"
    kind: repo
---

Scott Hanselman argues that Windows still lacks a polished command-line experience and points to tools that improve usability, editing, tab completion, tabs, and SSH workflows. He values both function and appearance, and repeatedly compares Windows options to the elegance he sees in other terminal environments.

## Reading notes

- Clink adds Readline-style editing inside cmd.exe, better TAB completion, clipboard paste, undo/redo, searchable command history, and history expansion.
- PowerShell ISE is already included with Windows, can be used as a console, and provides auto-completion, coloring, aliases, and a debugger.
- ConEmu adds tabs, status details, admin tabs, taskbar progress bars, and support for FarManager.
- Git for Windows and Cygwin are presented as ways to get a Linux-like shell on Windows, with Git Bash often enough for many users.
- Bitvise SSH Client includes a command-line version, and the post describes using a batch file so typing ssh can launch it directly.
- Kitty is presented as a PuTTY fork with portable use, tray handling, transparency, session launching, and browser integration for ssh:// links.
