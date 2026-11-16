---
title: "Configuring i3 Window Manager: a Complete Guide"
date: '2020-04-20T21:22:42+00:00'
category: webclip
summary: 'The article presents i3 as a light, flexible window manager for Linux, shows its tree-based layout model, and walks through key config changes for shortcuts, workspaces, floating windows, the bar, locking, and screen setup.'
tags: ["i3", "linux", "window-manager", "configuration"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Configuring i3 Window Manager: a Complete Guide"
    url: "https://thevaluable.dev/window-manager-mouseless-i3"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/thevaluable-dev--configuring-i3-window-manager-complete-guide.md"
    kind: repo
---

The article argues that i3 is a lighter alternative to full desktop environments, especially for people who use the terminal often and want more control without relying on the mouse. It explains that i3 uses a tree structure of workspaces, containers, and windows, and that its behavior can be shaped through a config file.

## Reading notes

- i3 is presented as a Linux-only window manager that can be tried on top of an existing desktop or in a virtual machine.
- It is described as light, minimalist, flexible, and usable without a mouse.
- The article suggests keeping a personal cheatsheet for i3 shortcuts while learning and changing them.
- Workspaces are treated as virtual desktops, and containers organize windows with split, stacked, or tabbed layouts.
- Windows can be fixed or floating, and floating windows are meant for pop-ups and similar tools.
- The default modifier key is `mod4`, and the article uses `$mod` to refer to it.
- The default shortcut examples cover opening terminals, focusing windows, moving them, changing layouts, reloading the config, restarting i3, and quitting.
- i3 loads config files in a specific order, with `~/.config/i3/config` or `~/.i3/config` as the main user config.
- The config uses variables with `set`, and commands are bound with `bindsym` or `bindcode`.
- `dmenu` is used as the program launcher instead of a start menu.
- The article rewrites focus and move bindings to use Vim-style `hjkl` keys.
- It also shows how to rebind container splitting keys and how to name workspaces with custom labels.
- `workspace_auto_back_and_forth yes` makes the same workspace key switch back to the last workspace.
- Applications can be assigned to a specific workspace using `assign` together with `class` and `instance` values from `xprop | grep WM_CLASS`.
- Window resizing is also mapped to `hjkl`, and resize mode must be entered first.
- `focus_follows_mouse` can be set to `no` to prevent focus from changing on hover.
- The screen lock setup uses `i3lock`, and the article shows both a simple wallpaper option and a script that pixelizes a screenshot before locking.
- A custom system menu is built with `dmenu` to lock, log out, suspend, hibernate, reboot, or power off.
- `feh` is used to set a wallpaper when switching to empty workspaces.
- Floating rules can be set by `window_role`, `class`, or `instance` so that certain windows open as floating automatically.
- Colors can be reused from Xresources with `set_from_resource`, and the status bar can be customized with `i3status` and bar color settings.
- ARandR is used to configure monitors, save an `xrandr` script, and launch different screen layouts from an i3 mode menu.
