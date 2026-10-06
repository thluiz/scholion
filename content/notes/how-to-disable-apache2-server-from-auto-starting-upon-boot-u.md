---
title: "how to disable apache2 server from auto starting upon boot up"
date: '2015-05-22T11:59:10-03:00'
category: webclip
summary: 'The page explains how apache2 starts through init scripts and runlevel links, and gives update-rc.d commands to remove, disable, or re-enable those startup links.'
tags: ["apache2", "update-rc-d", "init-scripts"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "how to disable apache2 server from auto starting upon boot up"
    url: "http://askubuntu.com/questions/170640/how-to-disable-apache2-server-from-auto-starting-upon-boot-up"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/askubuntu-com--how-to-disable-apache2-server-from-auto-starting-upon-boot-u.md"
    kind: repo
---

The page says apache2 starts at boot through init scripts in /etc/init.d and symlinks in runlevel directories such as rc0.d to rc6.d. It points to update-rc.d as the tool for changing those links instead of renaming files by hand.

## Reading notes

- apache2 starts from init scripts linked into runlevel directories
- `sudo update-rc.d -f apache2 remove` removes apache2 from startup links
- `sudo update-rc.d apache2 disable` can disable it, and `sudo update-rc.d apache2 enable` can turn it back on
- one comment notes that `chkconfig {service_name} off` may also help
- one comment says the disable and enable API may not be stable on Ubuntu Trusty
- one comment links to a GUI tool for managing startup services
