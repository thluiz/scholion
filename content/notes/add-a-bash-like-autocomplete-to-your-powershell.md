---
title: "Add a Bash-like autocomplete to your PowerShell"
date: '2019-12-29T16:35:11+00:00'
category: webclip
summary: 'The post shows how to turn on PSReadline in a PowerShell profile so Tab lists completion options and the arrow keys search command history using what you have already typed.'
tags: ["powershell", "psreadline", "autocomplete"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Add a Bash-like autocomplete to your PowerShell"
    url: "https://dev.to/ofhouse/add-a-bash-like-autocomplete-to-your-powershell-4257"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--add-a-bash-like-autocomplete-to-your-powershell.md"
    kind: repo
---

The post says PowerShell can behave more like Bash if you enable PSReadline in your profile. It also adds a small alias for `open` and suggests trying the new Windows Terminal for a better console experience.

## Reading notes

- PowerShell by default completes commands immediately and does not show a menu of matching options
- Bash-style completion can be enabled through the PSReadline module in the PowerShell profile
- `Tab` can be set to show a navigable menu of completion options
- `UpArrow` and `DownArrow` can be set to search command history based on what you have already typed
- The profile can be created if it does not exist and then edited directly from PowerShell
- The post adds `New-Alias open ii` so `open` works like the macOS command and opens the current folder or a file
- It recommends the new Windows Terminal preview because it offers tabs and more customization than the default console
