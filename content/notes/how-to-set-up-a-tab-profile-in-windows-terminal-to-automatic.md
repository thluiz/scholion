---
title: "How to set up a tab profile in Windows Terminal to automatically SSH into a Linux box"
date: '2026-11-16T04:26:50+00:00'
category: webclip
summary: 'Shows how to add a Windows Terminal profile that runs ssh, how to install OpenSSH on Windows, and how to use an ssh key and authorized_keys so a tab can log into a Linux machine automatically.'
tags: ["windows-terminal", "ssh", "openssh", "linux"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to set up a tab profile in Windows Terminal to automatically SSH into a Linux box"
    url: "https://hanselman.com/blog/HowToSetUpATabProfileInWindowsTerminalToAutomaticallySSHIntoALinuxBox.aspx"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/hanselman-com--how-to-set-up-a-tab-profile-in-windows-terminal-to-automatic.md"
    kind: repo
---

The post explains how to add a custom profile to Windows Terminal by editing the profiles array in the settings file. A profile can set a name, tab title, command line, and icon, and Windows Terminal will launch whatever command is specified.

It then shows how to use the Windows OpenSSH client to make a profile that runs ssh against a Linux machine. For automatic login, it uses ssh-keygen on Windows, copies the public key to the remote machine, and appends it to the user's authorized_keys file. With that in place, clicking the profile opens an SSH session directly.

## Reading notes

- Windows Terminal can generate a fresh settings file, and Visual Studio Code is recommended for editing it because of JSON Schema autocomplete.
- A basic profile entry can be added inside the profiles array with only a name.
- If no command line is set, the profile launches cmd.exe by default.
- Adding tabTitle changes the tab label while the menu entry keeps the profile name.
- Windows Terminal can call any command in the PATH, so ssh can be used directly.
- OpenSSH client apps are available on Windows after installing the OpenSSH.Client capability.
- The post uses a profile with commandline set to ssh pi@hanselpi4.
- If WSL is used, the command line can be wsl ssh pi@hanselpi4 or wsl -d Ubuntu-18.04 ssh pi@hanselpi4.
- Automatic login requires a key on the Windows machine and the public key added to ~/.ssh/authorized_keys on the Linux machine.
- The public key is piped from id_rsa.pub over ssh and appended to authorized_keys with cat >> .ssh/authorized_keys.
- A profile can also set an icon, such as a Raspberry Pi image, to make the SSH entry easier to identify.
