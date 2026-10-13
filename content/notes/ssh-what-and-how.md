---
title: "SSH: What and How"
date: '2012-05-24T11:19:19-03:00'
category: webclip
summary: 'The article explains SSH as a way to open a terminal session on another computer, then shows how to install it, connect to a server, set up keys and shortcuts, and use it for Git and SFTP.'
tags: ["ssh", "terminal", "git", "sftp"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "SSH: What and How | Nettuts+"
    url: "http://net.tutsplus.com/tutorials/tools-and-tips/ssh-what-and-how/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-05/net-tutsplus-com--ssh-what-and-how.md"
    kind: repo
---

SSH is presented as a secure way to reach the terminal of another machine over a network. The article gives a short history of SSH, then walks through basic setup on Mac, Windows, and Linux, along with a simple login to a remote server and the kinds of server tasks that become possible after connecting.

## Reading notes

- SSH is described as using a network connection to get into Terminal on another computer.
- The article says SSH was developed in 1995 as the first secure way to administrate a remote UNIX system.
- It notes that older tools sent passwords in clear text.
- It explains how to check whether SSH is installed with `which ssh`.
- It assumes OpenSSH and shows a Mac-to-MediaTemple setup.
- It says SSH usually runs over port 22 and suggests `nmap` to check whether the port is open.
- It shows logging in with `ssh root@primarydomain.com` for a MediaTemple server.
- It says shared hosting often uses a user account name instead of root.
- It says that after logging in you can run commands, navigate the file system, manage Apache, edit config files, view logs, clear caches, and inspect files on the server.
- It shows how to generate SSH keys, keep them in `~/.ssh`, and set permissions with `chmod`.
- It explains that a public key can be copied to `authorized_keys` on the server.
- It says `known_hosts` helps protect against man-in-the-middle attacks.
- It shows adding `Host`, `HostName`, and `User` entries to `~/.ssh/config` so you can log in with a short alias.
- It says SSH can be used to host Git repositories on your own server.
- It outlines a workflow where you create a staging branch locally, push it to the server, and merge it there.
- It says SFTP is an encrypted FTP alternative that runs over port 22.
- It says SSH is useful from almost anywhere as long as you have a computer, a terminal, and SSH installed.
- It mentions using SSH locally for file transfer and for repos that enforce a staging process before production.
- It ends with links to the OpenSSH manual and a Linux Journal introduction to SSH.
