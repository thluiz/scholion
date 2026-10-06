---
title: "How To Set Up an OpenVPN Server on Ubuntu 14.04"
date: '2015-05-01T14:22:36-03:00'
category: webclip
summary: 'The tutorial shows how to install and configure an OpenVPN server on Ubuntu 14.04, set up certificates and packet forwarding, create client profiles, and test that traffic and DNS go through the VPN.'
tags: ["openvpn", "ubuntu-14-04", "vpn", "networking"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How To Set Up an OpenVPN Server on Ubuntu 14.04 | DigitalOcean"
    url: "https://www.digitalocean.com/community/tutorials/how-to-set-up-an-openvpn-server-on-ubuntu-14-04"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/digitalocean-com--how-to-set-up-an-openvpn-server-on-ubuntu-1404.md"
    kind: repo
---

The tutorial walks through setting up an OpenVPN server on Ubuntu 14.04, including server configuration, packet forwarding, ufw rules, and a certificate authority for server and client keys. It then shows how to build a unified client profile, install it on Windows, OS X, iOS, or Android, and verify the connection with DNSLeakTest.

## Reading notes

- Update Ubuntu, install OpenVPN and Easy-RSA, extract the sample server config, and edit it to use 2048-bit Diffie-Hellman, redirect client traffic through the VPN, push OpenDNS resolvers, and run OpenVPN as nobody and nogroup.
- Enable IPv4 packet forwarding at runtime and in sysctl so client traffic can leave the server after reboot.
- Configure ufw to allow SSH and UDP port 1194, change DEFAULT_FORWARD_POLICY to ACCEPT, add NAT and masquerading rules in before.rules, then enable the firewall and check its status.
- Copy Easy-RSA scripts into /etc/openvpn, edit vars for certificate details, generate dh2048.pem, initialize the PKI, clean old keys, and build the certificate authority.
- Build the server certificate and key with build-key-server, then copy server.crt, server.key, and ca.crt into /etc/openvpn and start the OpenVPN service.
- Build a separate client certificate and key for each device, copy client.conf to client.ovpn, and transfer client1.crt, client1.key, client.ovpn, and ca.crt to the client device through SFTP or SCP.
- Merge the CA, client certificate, and client key into a unified .ovpn profile, change the remote host to the server IP, and comment out the separate ca, cert, and key lines in the template.
- Install the client application on Windows, OS X, iOS, or Android, import the .ovpn profile, and use the app’s connect and disconnect controls.
- Test the VPN by comparing the browser IP address and DNS servers before and after connecting, using DNSLeakTest and its Extended Test.
