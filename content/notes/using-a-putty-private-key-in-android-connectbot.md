---
title: "Using a Putty private key in Android ConnectBot"
date: '2015-05-01T14:16:41-03:00'
category: webclip
summary: 'Explains how to convert a PuTTY .ppk private key into an OpenSSH key with PuTTYgen, move it to Android, and import it into ConnectBot so the loaded key can be used for SSH access.'
tags: ["puttygen", "openssh", "connectbot", "android"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Using a Putty private key in Android ConnectBot"
    url: "http://blog.oracle48.nl/using-a-putty-private-key-in-android-connectbot/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/blog-oracle48-nl--using-a-putty-private-key-in-android-connectbot.md"
    kind: repo
---

The post explains that a private key that works in PuTTY must be converted to an OpenSSH key before ConnectBot can use it on Android. It gives a simple workflow: export the key with PuTTYgen, copy the OpenSSH file to the phone, import it in ConnectBot, and load it into memory before connecting.

## Reading notes

- A key that works in PuTTY may not work in ConnectBot until it is converted to OpenSSH format.
- PuTTYgen can load a .ppk private key, accept a passphrase if needed, and export an OpenSSH key.
- The OpenSSH key must be copied to the Android /sdcard folder.
- In ConnectBot, the key is imported through Manage Pubkeys, then loaded by clicking the red lock icon.
- If a passphrase exists, it is entered after loading the key.
- The connection is then made by disconnecting the current session and connecting again.
- The post says ConnectBot does not assign a private key to a connection; it tries any loaded key instead.
- A comment adds that on Linux, ssh-keygen -i -f input_keyfile > output_keyfile can generate an OpenSSH keyfile.
