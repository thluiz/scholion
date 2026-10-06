---
title: "SSH tricks"
date: '2012-03-16T19:56:08-03:00'
category: webclip
summary: 'The page collects practical SSH uses: passwordless key-based login, remote command execution, file transfer, per-host client settings, server hardening, port forwarding, SOCKS proxying, sshfs, and client tools for Windows and iOS.'
tags: ["ssh", "remote-access", "port-forwarding", "file-transfer"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "SSH tricks"
    url: "http://matt.might.net/articles/ssh-hacks/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-03/matt-might-net--ssh-tricks.md"
    kind: repo
---

The page explains why SSH replaced telnet by encrypting and authenticating connections. It then shows how to configure it well, how to use key-based authentication, how to run remote commands, how to copy files, and how to set per-host client options in `~/.ssh/config`.

It also covers server settings in `sshd_config`, local and remote port forwarding, SOCKS proxying for Firefox, mounting a remote filesystem with sshfs, and SSH clients for Windows and iOS.

## Reading notes

- SSH encrypts and authenticates connections, unlike telnet, which sent passwords in the clear.
- Per-user client configuration lives in `~/.ssh/config`; system-wide client settings live in `/etc/ssh/ssh_config`; daemon settings live in `/etc/ssh/sshd_config`.
- Key-based authentication uses public-key cryptography to prove ownership of the private key without revealing it.
- `ssh-keygen` creates a private/public key pair, and the public key goes into the remote account’s `~/.ssh/authorized_keys`.
- The private key should be protected like a password, and it should not be copied to the remote machine.
- A remote command can be run by placing it after the host name, as in `ssh host df`.
- File transfer can be done with `cat`, `scp`, or `sftp`, and `-C` enables compression for large files.
- `~/.ssh/config` can set options per host, including `User`, `IdentityFile`, `BatchMode`, `EscapeChar`, `HostName`, and wildcard host rules.
- `sshd_config` settings highlighted on the page are `Port`, `PermitRootLogin`, and `PasswordAuthentication`.
- Local port forwarding uses `ssh -L localport:B:remoteport` and can route traffic through another server.
- Remote port forwarding uses `ssh -R remoteport:A:targetport` and can expose a local service through a remote machine.
- SSH can provide a SOCKS proxy with `ssh -D localport host`, and Firefox can use it as a SOCKS5 proxy.
- `sshfs` mounts a remote filesystem over SSH with FUSE.
- The page mentions PuTTY for SSH from Windows and iSSH for SSH from iOS.
