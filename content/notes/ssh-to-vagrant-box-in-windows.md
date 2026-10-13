---
title: "SSH to Vagrant box in Windows?"
date: '2013-03-03T19:12:02-03:00'
category: webclip
summary: 'The note says Windows users can use PuTTY with Vagrant boxes by converting Vagrant’s insecure private key to a .ppk file, loading that key in PuTTY, and connecting on port 2222.'
tags: ["vagrant", "putty", "ssh"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "SSH to Vagrant box in Windows? - Stack Overflow"
    url: "http://stackoverflow.com/questions/9885108/ssh-to-vagrant-box-in-windows"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-03/stackoverflow-com--ssh-to-vagrant-box-in-windows.md"
    kind: repo
---

The page says Windows 7 users can connect to Vagrant boxes with PuTTY. It gives three setup steps: convert `%HOMEPATH%\.vagrant.d\insecure_private_key` to a `.ppk` file with PuTTYGen, select that `.ppk` in PuTTY’s SSH authentication settings, and use port 2222 instead of 22.

## Reading notes

- Use PuTTY on Windows 7 to connect to Vagrant boxes.
- Convert `%HOMEPATH%\.vagrant.d\insecure_private_key` to `.ppk` with PuTTYGen.
- Set the `.ppk` file in PuTTY under Connection > SSH > Auth > Private key file.
- Connect through port 2222, not 22.
