---
title: "Why I still self host my servers (and what I've recently learned)"
date: '2026-09-24T23:13:41+01:00'
category: webclip
summary: 'The author explains why self-hosting still remains worthwhile: independence, practical learning, and a better understanding of complex systems, despite the work and recent failures.'
tags: ["self-hosting","linux","distributed-systems","sysadmin"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why I still self host my servers (and what I've recently learned)"
    url: "https://chollinger.com/blog/2024/08/why-i-still-self-host-my-servers-and-what-ive-recently-learned/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/chollinger-com--why-i-still-self-host-my-servers-and-what-ive-recently-learn.md"
    kind: repo
---

The post argues that self-hosting still pays off because it supports independence and forces hands-on learning. The author ties that learning to better reasoning about complex systems and to work on distributed infrastructure.

It also lists recent problems and fixes from the last six months, including power and UPS failures, redundant DNS, Proxmox on ARM, ZFS memory tuning, hardware crashes, VPS outages, storage performance, object storage tradeoffs, and CrowdSec for intrusion prevention.

## Reading notes

- Keeps almost everything at home, except email, in a Proxmox cluster with several services and an external VPS.
- Defends self-hosting for two central reasons: autonomy from big companies and practical learning.
- Links the experience of operating one’s own infrastructure to the ability to understand distributed systems at work.
- Uses examples of Linux, networking, Kubernetes, Kafka, Flink, and other components to show this overlap between hobby and profession.
- Reports recent failures such as power outages, dead UPS batteries, DNS without redundancy, a Proxmox host that went down every night, and a VPS that was offline for days.
- Says it is possible to self-host VS Code in the browser with code-server, useful on devices such as an iPad or Mac.
- Notes that home UPS batteries die silently and quickly, and started testing the UPS monthly.
- Reorganized DHCP and DNS to have two Pi-hole caches available to clients and map IPs and physical devices.
- Put a Raspberry Pi 5 as a Proxmox node with help from a GitHub project, although the solution is unsupported.
- Adjusted ZFS memory consumption in Proxmox to avoid OOM kills in VMs during backups.
- Discovered that a nightly failure came from an old, non-redundant disk used for backup; replacing the drive fixed it.
- Started using LibreNMS with SNMPv3 for network monitoring and mapping.
- Became suspicious of Contabo’s VPS after days of unavailability and support that blamed the issue on DNS without evidence.
- Migrated to a Hetzner VPS, which benchmarking showed to be faster than the previous one.
- Tested remote storage via CIFS and SSHFS and concluded that both were slow, especially with transatlantic latency.
- Evaluates object storage as a cheap solution for Nextcloud files, but recognizes slowness with lists and small files.
- Uses Wasabi for Nextcloud data via external storage, accepting the cost and S3 limitations.
- Adopts CrowdSec as an intrusion prevention tool and highlights the bans and metrics shown by the CLI.
