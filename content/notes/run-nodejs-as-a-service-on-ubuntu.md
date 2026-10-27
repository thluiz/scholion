---
title: "Run Node.js as a Service on Ubuntu"
date: '2013-04-15T11:21:46-03:00'
category: webclip
summary: 'The post explains why running Node in the background with `&` is fragile and shows how to use Upstart on Ubuntu to restart a Node program, log output, and run it with limited privileges.'
tags: ["nodejs", "ubuntu", "upstart"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Run Node.js as a Service on Ubuntu - Kevin van Zonneveld"
    url: "http://kvz.io/blog/2009/12/15/run-nodejs-as-a-service-on-ubuntu-karmic/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-04/kvz-io--run-nodejs-as-a-service-on-ubuntu.md"
    kind: repo
---

The post argues that sending a Node.js program to the background with `&` is not enough for a real service, because the process can die when STDOUT disappears or when the server crashes or reboots. It recommends using Ubuntu’s Upstart so the system recognizes the program as a daemon, can restart it, and can manage it more cleanly.

## Reading notes

- Running `node ./yourprogram.js &` only backgrounds the process, but it is still vulnerable if the console closes, STDOUT disappears, or the machine reboots.
- The suggested approach is to create an Upstart script in `/etc/init/yourprogram.conf` for each Node program.
- The example script sets a description, starts on mountall, stops on shutdown, respawns the process, and logs output to `/var/log/node.log`.
- The script can run Node as a limited user by using `sudo -u www-data`.
- Restarting and stopping the daemon is done with `start yourprogram` and `stop yourprogram`.
- The post says `initctl` is behind those shortcuts and can also show status, reload a job, and start it directly.
- A later update shows a production Upstart script with `respawn limit`, a higher `nofile` limit, a FIFO used for logging, and a post-start notification script.
- The post ends by saying Node can be used for very fast server-side JavaScript programs, including chat, key-value stores, and HTTP servers.
