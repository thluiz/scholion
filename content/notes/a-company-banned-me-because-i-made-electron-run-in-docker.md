---
title: "A Company banned me because I made their Electron App running inside Docker"
date: '2022-08-11T15:20:17-03:00'
category: webclip
summary: 'The article tells how the author got Tinkerwell running inside Docker on Linux, then describes a support dispute with BeyondCode after he asked questions about indexing and auto-completion.'
tags: ["docker", "electron", "php", "support"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "A Company banned me because I made their Electron App running inside Docker | by Michael Bladowski | Geek Culture | Jul, 2022 | Medium"
    url: "https://medium.com/geekculture/a-company-banned-me-because-i-made-their-electron-app-running-inside-docker-3f45a713904f"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-08/medium-com--a-company-banned-me-because-i-made-electron-run-in-docker.md"
    kind: repo
---

The author says he wanted to run Tinkerwell, an Electron app for PHP developers, inside Docker on Linux because his daily workflow depends on Docker and he does not want a local PHP binary on the host. He first tried a wrapper around his PHP alias, then moved to running Electron in a Debian-based container with the needed display and X11 setup.

He says the setup eventually worked: Tinkerwell opened, the language server ran, Docker integration worked, and he could browse projects and use existing containers. The article also recounts a support conflict with BeyondCode after he asked three questions about indexing and auto-completion, and says he was offered a refund and told not to contact support again.

## Reading notes

- The author prefers Docker-based PHP workflows and argues that tools should not assume a local PHP binary on the host.
- A wrapper around his PHP alias did not work for Tinkerwell.
- He found that Electron can be run inside Docker on Linux with the right display and X11 configuration.
- The container runs as a matching local user and group to avoid permission problems.
- The Docker image also includes Docker itself so Tinkerwell can use an existing container as a PHP source.
- He says Tinkerwell’s language server and Docker access worked after the setup.
- He reports that BeyondCode’s CEO refused support after several emails and offered a refund instead.
- He says he asked whether Tinkerwell should keep its index between starts and whether auto-completion for Laravel symbols such as config() and User:: would work.
- He suggests JetBrains users can avoid this setup by using the Laravel Tinker plugin, since JetBrains supports Docker-based PHP interpreters.
