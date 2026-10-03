---
title: "Issues with VirtualBox provisioner `private_network` mode in cloud ubuntu 14.04 box"
date: '2016-03-13T21:04:28-03:00'
category: webclip
summary: 'The issue reports long boot delays and connection failures when Vagrant adds a `private_network` to Ubuntu cloud images, and several comments trace the cause to network configuration, `cloud-init-nonet`, and a failing `post-up` route command.'
tags: ["vagrant", "virtualbox", "ubuntu-cloud-init"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Issues with virtualbox provisioner `private_network` mode in cloud ubuntu 14.04 box · Issue #3860 · mitchellh/vagrant"
    url: "https://github.com/mitchellh/vagrant/issues/3860"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-03/github-com--issues-with-virtualbox-provisioner-private-network-mode.md"
    kind: repo
---

The thread reports that Ubuntu Trusty and related cloud images can take several minutes to boot when Vagrant configures a `private_network` with DHCP or a static address. The delays are tied to `cloud-init-nonet`, and multiple users describe failed SSH connections, repeated timeouts, or missing network connectivity after reboot.

Several comments focus on Vagrant’s generated network setup and the line `post-up route del default dev $IFACE`. One explanation says that if this command fails, `ifup` leaves the interface unconfigured, which blocks DHCP. Suggested workarounds include removing that line, adding `|| true`, disabling auto config, creating the interface file manually, or editing `/etc/network/interfaces` and `/etc/network/interfaces.d/` so there are no duplicate or extra `ethX` entries.

## Reading notes

- The issue is triggered when a VM from `ubuntu/trusty64` gets a `private_network` and is reloaded after reboot.
- `cloud-init-nonet` waits 120 seconds, then another startup script waits 60 seconds, which makes booting take at least 3 minutes.
- Some users say the problem appears on Trusty, Precise, Ubuntu 12.04, and bridged adapters too.
- One workaround is to put `auto eth1` and `iface eth1 inet dhcp` in `/etc/network/interfaces.d/eth1.cfg` instead of letting Vagrant write the same configuration into the main interfaces file.
- A comment identifies `post-up route del default dev $IFACE` as the line that causes the interface setup to fail.
- One explanation says `ifup` aborts when that `post-up` command fails, leaving the interface unconfigured.
- A workaround is to change the line to `post-up route del default dev $IFACE || true`.
- Other comments propose deleting that line from `/etc/network/interfaces` before boot, then letting it be recreated later.
- Another thread says the issue can happen when `/etc/network/interfaces` contains duplicate or extra `ethX` entries.
- One user reports success after removing old VirtualBox networking settings and extra host-only adapters.
- Another user reports that Ubuntu 14.04 32-bit with VirtualBox 5.0.12 worked after changing the NIC type to `Am79C973` and writing the interface config in `/etc/network/interfaces.d/`.
- A later comment says an NFS mount problem could also cause a similar cloud-init hang after the first reboot.
