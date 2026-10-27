---
title: "Linux: emergency reboot or shutdown with magic commands"
date: '2013-12-09T15:53:33-03:00'
category: webclip
summary: 'The post explains how Linux SysRq magic commands can force an immediate reboot or shutdown on a misbehaving server, and contrasts that with a safer reboot sequence that tries to sync and unmount first.'
tags: ["linux", "sysrq", "reboot", "shutdown"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Linux: emergency reboot or shutdown with magic commands | major.io"
    url: "http://major.io/2009/01/29/linux-emergency-reboot-or-shutdown-with-magic-commands/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-12/major-io--linux-emergency-reboot-or-shutdown-with-magic-commands.md"
    kind: repo
---

The post describes how most Linux distributions try to stop daemons and unmount storage cleanly during reboot or shutdown, but a badly behaving remote server can make a normal reboot impossible. In that situation, SysRq magic commands let you force a reboot or shut the machine down directly from `/proc/sysrq-trigger`.

## Reading notes

- Most Linux distributions use scripts to stop daemons and unmount storage volumes gracefully during reboot or shutdown.
- If a remote server is misbehaving, a plain `reboot` command may fail before SSH stops running.
- Writing `1` to `/proc/sys/kernel/sysrq` enables SysRq access.
- `echo b > /proc/sysrq-trigger` forces an immediate reboot with no graceful shutdown, no filesystem sync, and possible filesystem damage.
- The post mentions a safer reboot sequence from Wikipedia using the mnemonic “Reboot Even If System Utterly Broken”.
- The safer sequence is `unRaw`, `tErminate`, `kIll`, `Sync`, `Unmount`, `reBoot`.
- The author says they cannot vouch for that sequence actually working and adds an update warning that it is a very bad idea with ReiserFS.
- `echo o > /proc/sysrq-trigger` shuts the machine down entirely.
- SysRq can be kept enabled all the time with `kernel.sysrq = 1` in `sysctl.conf`.
