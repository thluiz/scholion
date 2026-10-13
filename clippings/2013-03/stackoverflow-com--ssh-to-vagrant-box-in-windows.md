---
url: "http://stackoverflow.com/questions/9885108/ssh-to-vagrant-box-in-windows"
captured_at: "2013-03-03T19:12:02-03:00"
title: "SSH to Vagrant box in Windows? - Stack Overflow"
domain: "stackoverflow-com"
---

|  |
| --- |
| I use PuTTY to connect to my Vagrant boxes on Windows7.  Make sure you   - convert the `%HOMEPATH%\.vagrant.d\insecure_private_key` to .ppk using PuTTYGen - use the .ppk key in your PuTTY session - configured in Connection > SSH > Auth > Private key file - use port 2222 instead of 22 |
