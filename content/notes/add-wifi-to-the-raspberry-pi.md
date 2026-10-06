---
title: "How-To: Add WiFi to the Raspberry Pi"
date: '2015-06-07T11:21:09-03:00'
category: webclip
summary: 'The guide says to use a cheap USB WiFi adapter with Linux support, confirm that the Raspberry Pi recognizes it, edit /etc/network/interfaces with the SSID and password, then reload networking and check for an IP address.'
tags: ["raspberry-pi", "wifi", "linux"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How-To: Add WiFi to the Raspberry Pi | Raspberry Pi HQ"
    url: "http://raspberrypihq.com/how-to-add-wifi-to-the-raspberry-pi/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-06/raspberrypihq-com--add-wifi-to-the-raspberry-pi.md"
    kind: repo
---

The page explains that the Raspberry Pi normally uses a network cable, so a USB WiFi adapter is the practical way to connect it to a wireless home network. It also warns that the adapter should mention Linux support, because not every device works plug and play.

## Reading notes

- Use a cheap USB WiFi adapter in one of the Raspberry Pi USB ports.
- Choose an adapter that mentions Linux in the product description or package.
- After booting, run `dmesg | more` to check whether the operating system found the adapter.
- Edit `/etc/network/interfaces` with `sudo nano /etc/network/interfaces`.
- Set `wlan0` to DHCP and add `wpa-ssid` and `wpa-psk` with the network name and password.
- Save the file with Ctrl+O and exit nano with Ctrl+X.
- Reload networking with `sudo service networking reload`.
- Run `ifconfig` and look for a valid IP address under `inet addr`.
