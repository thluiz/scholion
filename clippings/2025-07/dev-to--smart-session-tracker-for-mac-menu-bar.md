---
url: "https://dev.to/ravgeetdhillon/building-a-smart-session-tracker-for-your-macs-menu-bar-41km?context=digest"
captured_at: "2025-07-17T13:23:45+01:00"
title: "Building a Smart Session Tracker for Your Mac's Menu Bar - DEV Community"
domain: "dev.to"
---

# Building a Smart Session Tracker for Your Mac's Menu Bar - DEV Community

> ## Excerpt
> Picture this: You sit down at your Mac with a coffee, planning to "quickly check a few emails." Next...

---
Picture this: You sit down at your Mac with a coffee, planning to "quickly check a few emails." Next thing you know, it's 3 PM, your coffee has achieved room temperature, and you're wondering if you've entered some sort of time vortex. Sound familiar?

If you're nodding your head (and possibly rubbing your stiff neck), you're not alone. In our hyper-connected world, time has a sneaky way of slipping through our fingers like sand – or like that last slice of pizza when you're not paying attention.

That's why I built a session tracker that lives right in your Mac's menu bar. It's like having a gentle, persistent friend who reminds you to take breaks, tracks your work patterns, and occasionally judges your life choices (in the nicest possible way).

## What Does This Digital Time Wizard Do?

Our session tracker is basically a sophisticated time-keeping ninja that:

1.  **Tracks Your Current Work Session** - It knows when you start working and keeps a running timer
2.  **Detects Sleep/Wake Cycles** - Smartly figures out when you've been away from your computer
3.  **Logs Daily Activity** - Keeps a record of all your work sessions throughout the day
4.  **Sends Gentle Reminders** - Politely suggests you take a break after an hour (because your eyes and back will thank you)
5.  **Shows Beautiful Stats** - Displays your current session time and daily totals right in your menu bar

Think of it as a Fitbit for your productivity, but instead of counting steps, it's counting the minutes you spend glued to your screen.

## The Magic Behind the Curtain

This isn't just any ordinary timer script – it's a surprisingly sophisticated piece of bash wizardry that handles all sorts of edge cases.

### Smart Session Detection

The script doesn't just start counting from when you run it. It's smart enough to detect when your Mac has been rebooted, figure out when you've been away (sleeping, lunch break, or that inevitable YouTube rabbit hole), and resume tracking seamlessly when you return.

### Intelligent Time Gap Detection

The script monitors for gaps in activity longer than 2 minutes. If it detects you've been away, it logs your previous session and starts a new one.

### Cross-Reboot Persistence

Even if you restart your Mac, the script remembers your previous session and can estimate when it ended, using boot time to figure out if the session file is from before a reboot.

## Setting Up Your New Digital Productivity Buddy

Requires **xbar** (formerly BitBar), installed via `brew install xbar`, and optionally `terminal-notifier` for prettier notifications (`brew install terminal-notifier`) — the script falls back to macOS's built-in notification system if it's skipped.

Setup: create the xbar plugins directory (`~/Library/Application Support/xbar/plugins`), create the script file `current-session.1m.sh`, paste in the bash script, make it executable (`chmod +x`), then launch xbar and refresh.

The script itself stores session data in `/tmp/current_session_start` and a daily log file `/tmp/daily_activity_YYYYMMDD`, checks `sysctl kern.boottime` to detect reboots, tracks a `last_session_check` file to detect sleep/wake gaps over 120 seconds, logs completed sessions (over 60 seconds) to the daily log, and fires a notification via `terminal-notifier` or `osascript` once the current session passes an hour, once per hour of continued work. It totals the day's sessions, formats durations as hours/minutes, and prints the current session, daily total, and session count to the menu bar dropdown, with a break reminder appended if the current session exceeds an hour.

## Customization Ideas

Change the break reminder interval (the `3600` seconds constant), swap notification sounds (`funk`, `glass`, `ping`), modify the 120-second gap threshold, or add more detailed logging (timestamps, session names, project tags).

## The Philosophical Side: Why This Matters

In our always-on world, this simple script serves a deeper purpose. It's not just about tracking time – it's about being mindful of how we spend our most precious resource. By making our work patterns visible, we can recognize unhealthy patterns (like those 4-hour coding binges), celebrate productivity, build better habits, and understand our rhythms.

## Wrapping Up

Building this session tracker was a fun exercise in bash scripting and practical problem-solving. It started as a simple "how long have I been working?" question and evolved into a surprisingly sophisticated time-tracking system. The best part: it's taught the author to actually take breaks.
