---
title: "[SOLVED] CentOS 6 networking and Hyper-V"
date: '2014-03-22T21:27:02-03:00'
category: webclip
summary: 'Describes a CentOS 6.2 minimal VM on Hyper-V, a boot-time checksum-offload warning, and the files and commands used to set a static IP, hostname, gateway, and DNS.'
tags: ["centos-6", "hyper-v", "networking", "dns"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "[SOLVED] CentOS 6 networking and Hyper-V. | pwrusr.com"
    url: "http://www.pwrusr.com/system-administration/solved-centos-6-networking-and-hyper-v"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-03/pwrusr-com--centos-6-networking-and-hyper-v.md"
    kind: repo
---

The post describes a CentOS 6.2 minimal setup running on Hyper-V and mentions a boot-time warning about `eth0` dropping `NETIF_F_SG` because no checksum feature is available. It treats that warning as a virtual-interface issue and moves on to the network setup itself.

The configuration uses a single `ifcfg-eth0` file with a static IP, then hard links are created in the other CentOS network directories to match how the scripts work. After that, the hostname is set, `/etc/sysconfig/network` is edited with `NETWORKING=yes`, `HOSTNAME`, and `GATEWAY`, permissions are set to 644, the system is rebooted, and `/etc/resolv.conf` is updated with a nameserver.

## Reading notes

- The lab uses Windows Server 2008 R2 SP1 with Hyper-V enabled, CentOS 6.2 x64 minimal ISO, and Linux Integration Services for Hyper-V 3.2.
- A boot message appears in `dmesg` and `messages` saying `eth0` is dropping `NETIF_F_SG` because no checksum feature is available.
- The post treats the missing checksum offload feature as a virtual hardware limitation rather than a blocking problem.
- A static interface file is created at `/etc/sysconfig/network-scripts/ifcfg-eth0` with `DEVICE`, `BOOTPROTO=static`, `ONBOOT=yes`, `NETWORK`, `NETMASK`, and `IPADDR`.
- The earlier copy-and-permissions method is replaced by hard links to `/etc/sysconfig/networking/devices/ifcfg-eth0` and `/etc/sysconfig/networking/profiles/default/ifcfg-eth0`.
- The machine name is set with `hostname my-system-name`.
- `/etc/sysconfig/network` is filled with `NETWORKING=yes`, `HOSTNAME=my-system-name`, and `GATEWAY=192.168.1.1`.
- The file `/etc/sysconfig/network` is set to permission 644.
- The system is rebooted after the network files are in place.
- `/etc/resolv.conf` gets `nameserver 192.168.1.1` for name resolution.
