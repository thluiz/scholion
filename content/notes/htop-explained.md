---
title: "htop explained"
date: '2016-12-26T16:00:55-03:00'
category: webclip
summary: 'Explains the fields shown by htop and top on Linux, using /proc, strace, and system tools to show uptime, load average, process states, users, memory, and boot services.'
tags: ["htop", "linux-processes", "procfs", "system-administration"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "htop explained"
    url: "https://peteris.rocks/blog/htop"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-12/peteris-rocks--htop-explained.md"
    kind: repo
---

The page explains what htop and top display on Linux by tracing each field back to the kernel and `/proc`. It covers uptime, load average, process counts, PIDs, process trees, owners, states, time sharing, niceness, memory columns, and startup services.

## Reading notes

- Uptime comes from `/proc/uptime`, and `uptime` formats that data for humans.
- Load average comes from `/proc/loadavg`, where the first three numbers reflect 1, 5, and 15 minute periods.
- Load average counts running and uninterruptible processes, so it is not the same as CPU usage.
- `htop` shows tasks, threads, and kernel threads, and those views can be toggled with keyboard shortcuts.
- PIDs identify processes, and `/proc/<pid>/` exposes command line, current directory, executable link, and other process details.
- Process hierarchies come from parent and child relationships created by `fork` and `exec`.
- Process ownership is based on user IDs, with names resolved through NSS and files such as `/etc/passwd`, `/etc/group`, and `/etc/shadow`.
- `sudo` and setuid binaries change which user a command runs as.
- Process states include running, interruptible sleep, uninterruptible sleep, zombie, stopped, and traced.
- Signals such as `SIGINT`, `SIGTERM`, `SIGKILL`, `STOP`, and `CONT` are used to interrupt, stop, resume, or kill processes.
- Time slicing lets one CPU appear to run several processes at once.
- Niceness affects scheduler priority, and the article relates that to htop color indicators.
- Memory columns in htop distinguish virtual memory, resident memory, shared memory, and memory percentage.
- The post also lists several Ubuntu server services and discusses which ones might be unnecessary on a minimal machine.
- The appendix shows how to use `strace`, `dpkg -S`, and source code to learn what programs do.
