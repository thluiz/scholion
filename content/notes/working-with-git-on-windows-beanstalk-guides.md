---
title: "Working with Git on Windows"
date: '2013-11-17T19:46:56-03:00'
category: webclip
summary: 'The page explains how to create and install SSH keys on Windows for Git access, recommending OpenSSH over PuTTY and showing how to generate a key pair with ssh-keygen and add the public key to Beanstalk.'
tags: ["git", "windows", "ssh-keys", "openssh"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Working with Git on Windows  •  Beanstalk Guides"
    url: "http://guides.beanstalkapp.com/version-control/git-on-windows.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-11/guides-beanstalkapp-com--working-with-git-on-windows-beanstalk-guides.md"
    kind: repo
---

The page says Windows users need SSH keys to access Git repositories. It presents two ways to set them up, with OpenSSH recommended over PuTTY. OpenSSH is included with Git, while PuTTY is described as a free Telnet and SSH client for advanced users.

## Reading notes

- To communicate with remote Git repositories from Windows, an SSH key pair must be generated for that computer.
- The instructions require installing msysGit with the full installer first.
- In Git Bash, the command `ssh-keygen -t rsa` generates the key pair.
- The default key location should be accepted by pressing Enter.
- A strong pass phrase should be set for the key.
- The public key is stored in `id_rsa.pub`.
- The contents of `id_rsa.pub` should be copied and added to the Beanstalk profile under Profile and Settings → Keys.
