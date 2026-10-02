---
url: "https://dfar.io/setting-up-a-jitsi-meet-server-on-azure/"
captured_at: "2020-05-03T10:14:16-03:00"
title: "Setting up A Jitsi Meet Server on Azure"
domain: "dfar-io"
---

With the COVID-19 pandemic going on, video chat is on the rise, with people using tools like Zoom, WebEx, and others. One option is to use an open-source solution like [Jitsi Meet](https://jitsi.org/jitsi-meet/), which provides both a [public cloud version you can use easily](https://jitsi.org/jitsi-meet/), and a version you can host on your own.

Why host on your own? You should consider hosting on your own if:

*   You’re concerned with security – hosting the software on your own ensures a third part is uninvolved.
*   You want more hands on capability to change the specs on the server for performance based on when you’re using video software.
*   You can control the location of the hardware, which depending on where everyone is located, may improve performance.

## Server Creation and Jitsi Installation

First, create an Azure VM with the following:

*   Running Ubuntu
*   Open inbound ports 80, 443, and 22.
*   SSH key access _(recommended)_

Once the VM is created, SSH into the server and install the Jitsi full suite:

when installing, you’ll be asked to configure `jitsi-videobridge2`, use the URL you plan to use for this Jitsi instance. Afterwards, generate a self-signed certificate _(we’ll create one with Let’s Encrypt later)_.

To verify installation worked successfully, visit the IP address in a browser, **making sure you use HTTPS**.

## Set up SSL with Let’s Encrypt

To set up SSL, you’ll need to set up a domain name for the server in place – you can either:

*   Configure the Public IP assigned by Azure to create a domain name.
*   Using the process above, but also creating an A or CNAME record for a purchase domain pointing to the server IP

Once this is done, you can run the following to automatically create a cert:

## Reference

[https://github.com/jitsi/jitsi-meet/blob/master/doc/quick-install.md#advanced-configuration](https://github.com/jitsi/jitsi-meet/blob/master/doc/quick-install.md#advanced-configuration)
