---
title: "5 commands to check memory usage on Linux"
date: '2015-05-22T12:00:02-03:00'
category: webclip
summary: 'The page lists terminal commands that show RAM and swap usage on Linux, compares their output, and notes that dmidecode reports installed memory hardware details.'
tags: ["linux", "memory-usage", "terminal-commands", "swap"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "5 commands to check memory usage on Linux"
    url: "http://www.binarytides.com/linux-command-check-memory-usage/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/binarytides-com--5-commands-to-check-memory-usage-on-linux.md"
    kind: repo
---

The page collects terminal commands for checking memory usage on Linux when a GUI is unavailable. It focuses on RAM and swap, and shows that these commands can help confirm total, used, free, cached, and buffer memory on a system.

## Reading notes

- free is presented as the simplest command for checking memory usage, with its output explained in terms of total RAM, used RAM, free memory, buffers, cached memory, and swap.
- /proc/meminfo is described as a virtual file that exposes kernel and system information, and the page points to MemTotal, MemFree, Buffers, Cached, SwapTotal, and SwapFree as the key values.
- vmstat -s is shown as another way to display memory statistics, including total memory, used memory, active memory, inactive memory, free memory, buffer memory, and swap.
- top is described as a command for per-process CPU and memory use that also reports total RAM and swap in its header.
- htop is described as similar to top, with the header showing CPU, RAM, and swap usage.
- dmidecode -t 17 is used to retrieve installed RAM hardware information, including size, type, and speed.
- The page ends by contrasting terminal tools with GUI tools such as gnome-system-monitor and ksysguard, which provide graphical resource usage views.
