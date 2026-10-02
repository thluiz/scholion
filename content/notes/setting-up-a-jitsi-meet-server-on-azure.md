---
title: "Setting up a Jitsi Meet Server on Azure"
date: '2020-05-03T10:14:16-03:00'
category: webclip
summary: 'The page explains why someone might host Jitsi Meet themselves and outlines the basic Azure setup, Jitsi installation steps, and SSL setup with Let’s Encrypt.'
tags: ["jitsi-meet", "azure", "video-chat", "letsencrypt"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Setting up A Jitsi Meet Server on Azure"
    url: "https://dfar.io/setting-up-a-jitsi-meet-server-on-azure/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-05/dfar-io--setting-up-a-jitsi-meet-server-on-azure.md"
    kind: repo
---

The page says Jitsi Meet can be used through a public cloud version or hosted on your own server. It gives three reasons to self-host: security, more control over server specs for performance, and control over hardware location.

It then lists the setup steps for Azure and SSL. Create an Ubuntu VM, open ports 80, 443, and 22, and use SSH key access. After installing the Jitsi full suite, configure jitsi-videobridge2 with the URL you plan to use, create a self-signed certificate for now, and verify the install by visiting the IP address with HTTPS. For SSL, the server needs a domain name, either through Azure public IP setup or by creating an A or CNAME record for a purchased domain, and then a cert can be created automatically.

## Reading notes

- Jitsi Meet offers both a public cloud version and a version you can host yourself.
- Self-hosting is suggested for security because no third party is involved.
- Self-hosting also lets you adjust server specs for performance.
- Hosting your own server lets you choose the hardware location, which may improve performance.
- The Azure setup calls for an Ubuntu VM with inbound ports 80, 443, and 22 open.
- SSH key access is recommended.
- During installation, jitsi-videobridge2 should be configured with the URL intended for the instance.
- A self-signed certificate is created first, with Let’s Encrypt used later.
- Installation is checked by visiting the IP address in a browser using HTTPS.
- SSL setup requires a domain name, either from Azure public IP configuration or from an A or CNAME record pointing to the server IP.
