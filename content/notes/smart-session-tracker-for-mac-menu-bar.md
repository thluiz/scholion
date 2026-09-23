---
title: "Building a Smart Session Tracker for Your Mac's Menu Bar"
date: "2026-09-23T17:35:17+01:00"
category: webclip
has_commentary: false
summary: "A bash script that lives in the macOS menu bar via xbar, tracking work sessions, detecting sleep and reboot gaps, and nudging a break after an hour of continuous work."
tags:
  - bash
  - macos
  - productivity
sources:
  - title: "Building a Smart Session Tracker for Your Mac's Menu Bar - DEV Community"
    url: "https://dev.to/ravgeetdhillon/building-a-smart-session-tracker-for-your-macs-menu-bar-41km?context=digest"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-07/dev-to--smart-session-tracker-for-mac-menu-bar.md"
    kind: repo
---

The script runs as an xbar plugin, refreshing every minute. It stores the current session's start time in a temp file and compares it against the system's boot time, read from `sysctl kern.boottime`, to detect whether the Mac has rebooted since the last check, and against a separate "last check" timestamp to detect whether more than two minutes passed since the previous run, its proxy for the user having stepped away or the Mac having slept. Either case starts a new session and logs the previous one, as long as it lasted over a minute, to a daily log file keyed by date.

Once running, it totals the day's logged sessions plus the current one, and prints the current session length and daily total to the menu bar, switching to a warning icon past an hour. It fires a native notification, via `terminal-notifier` if installed, falling back to `osascript`, once per hour of continuous work, tracked separately so it doesn't repeat mid-hour.

## Fichamento

- Reboot detection compares the stored session file against `sysctl kern.boottime`. If the session predates the last boot, it's logged as ending at boot time and a fresh session starts.
- Sleep or away detection uses a separate "last check" timestamp file: any gap over 120 seconds between runs is treated as the user having stepped away, closing out the previous session.
- Completed sessions only get logged to the daily file if they lasted more than 60 seconds, filtering out noise from very short gaps.
- The break notification fires once per elapsed hour of the current session, tracked via a separate file so it doesn't repeat within the same hour, using `terminal-notifier` if installed and `osascript` otherwise.
- The whole thing is a single portable bash script plus xbar, formerly BitBar, as the menu bar host. No app to install beyond the plugin file itself.
