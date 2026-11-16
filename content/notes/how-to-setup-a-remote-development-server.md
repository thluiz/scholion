---
title: "How to setup a Remote Development Server"
date: '2020-07-05T14:11:18+00:00'
category: webclip
summary: 'The article shows how to secure a remote development server on CentOS 8, limit access to SSH, disable IPv6, install fail2ban, and work through Vim or VS Code with port forwarding.'
tags: ["remote-development", "ssh", "firewall", "port-forwarding"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to setup a Remote Development Server"
    url: "https://web.archive.org/web/20200521080947id_/https://dev.to/codingsafari/how-to-setup-a-remote-development-server-46ln"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--how-to-setup-a-remote-development-server.md"
    kind: repo
---

The article describes a remote development setup on a non-production server. It creates a regular user with sudo access, installs an SSH key, hardens sshd, blocks incoming traffic with firewalld, disables IPv6, and installs fail2ban to reduce attack surface.

It also describes two ways to work on the server. One uses Vim, tmux, and zsh on the remote machine. The other uses VS Code with remote SSH support. For running apps locally in a browser, it forwards a remote port to the local machine through an SSH tunnel.

## Reading notes

- Use a non-root user with wheel access and keep root out of the normal workflow.
- Copy a public SSH key to the remote host and use key-based login instead of passwords.
- In sshd_config, disable root login and password authentication after confirming key login works.
- Set firewalld to block incoming traffic by default and allow only the local machine’s IP for SSH.
- Disable IPv6 through sysctl to reduce the exposed attack surface.
- Install fail2ban and configure it to ban repeated failed SSH login attempts.
- A remote dev setup can be used either through Vim, tmux, and zsh or through VS Code remote development.
- Use SSH port forwarding so a service running on the remote server can be opened in the local browser.
