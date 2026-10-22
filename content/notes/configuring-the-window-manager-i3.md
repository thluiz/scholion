---
title: "Configuring The Window Manager i3"
date: '2020-11-17T09:59:36-03:00'
category: webclip
summary: 'The article presents i3 as a lightweight, keyboard-driven alternative to a desktop environment and walks through installation, core concepts, shortcuts, and config options such as workspaces, layouts, launchers, locking, bars, and screens.'
tags: ["i3", "window-manager", "linux", "keyboard-shortcuts"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Configuring The Window Manager i3"
    url: "https://thevaluable.dev/i3-config-mouseless/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-11/thevaluable-dev--configuring-the-window-manager-i3.md"
    kind: repo
---

The article introduces i3 as a Linux window manager that replaces the usual desktop environment with a lighter, more flexible setup. It explains that i3 is designed for keyboard use, gives more control over window placement, and can be customized through a config file.

## Reading notes

- i3 is presented as a Linux-only alternative to desktop environments, especially useful for people who already use the terminal often.
- The article argues that i3 uses fewer resources, stays out of the way, and lets users add only the functions they need.
- i3 organizes the screen as a tree with workspaces, containers, and windows.
- Containers can use split, stacked, or tabbed layouts, and windows can be fixed or floating.
- The default modifier key is the Windows or Cmd key, stored as `$mod` in the config.
- The default shortcuts shown in the article include opening terminals, changing focus, moving windows, switching layouts, reloading the config, and quitting i3.
- i3 config files are loaded in a fixed order, and the article points to `~/.i3/config` when a generated config is used.
- The config can redefine key bindings with `bindsym`, launch a terminal with `i3-sensible-terminal`, and kill a window with `$mod+Shift+q`.
- Without a start menu, i3 uses launchers such as `dmenu_run`.
- The article shows how to remap focus and movement keys to `hjkl`.
- It also shows how to change split orientation, define named workspaces, and move containers between them.
- `workspace_auto_back_and_forth yes` makes `$mod+number` return to the previous workspace when pressed again.
- Applications can be assigned to specific workspaces with `assign`, using `class` and `instance` values from `xprop | grep WM_CLASS`.
- Window resizing uses a resize mode, and the article suggests disabling `focus_follows_mouse`.
- Screen locking can be done with `i3lock`, and the article gives a script that builds a pixelized screenshot for the lock screen.
- A `dmenu`-based system menu can handle lock, logout, suspend, hibernate, reboot, and shutdown actions.
- `feh` can set a wallpaper on startup.
- Floating windows are recommended for pop-ups, task dialogs, and selected applications such as Keepassx.
- The article shows how to reuse colors from Xresources with `set_from_resource`.
- The i3 status bar can be configured through a separate `i3status.conf` file.
- `arandr` is presented as a way to configure multiple screens, with layouts saved as `xrandr` commands and recalled through a `dmenu` menu.
