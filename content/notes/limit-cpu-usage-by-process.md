---
title: "Limit CPU Usage by Process"
date: '2012-06-25T19:14:16-03:00'
category: webclip
summary: 'The post explains how cpulimit can throttle a process such as Handbrake, keeping CPU use under control and lowering core temperatures. It includes install commands and an example of limiting a process by name and percentage.'
tags: ["cpulimit", "cpu-usage", "handbrake", "linux"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Limit CPU Usage by Process | nwlinux"
    url: "http://nwlinux.com/limit-cpu-usage-by-process/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-06/nwlinux-com--limit-cpu-usage-by-process.md"
    kind: repo
---

cpulimit is presented as a daemon for limiting a process’s CPU usage. The post says it worked well with Handbrake, which otherwise uses as many resources as needed and can max out the CPU. It also contrasts cpulimit with Trickle, which the author says is better suited to bandwidth limiting.

The post gives installation commands with apt-get and shows an example using the process name ghb with -l80. It explains that the limit value is relative to the number of cores and says that, on a four-core machine, -l80 means about 20% of total CPU for that process.

## Reading notes

- cpulimit is a daemon that limits a process’s CPU usage.
- Handbrake is described as using whatever resources it needs and maxing out the CPU.
- Trickle is mentioned as being more suited to bandwidth-intensive operations than CPU limiting.
- The author says cpulimit reduced Xeon core temperatures from 70C-85C to about 43C.
- Installation is shown with `sudo apt-get update` and `sudo apt-get install cpulimit`.
- The example command is `sudo cpulimit -e ghb -l80`.
- The post says the percentage limit depends on the number of cores and should be divided by the number of cores on a multi-core machine.
