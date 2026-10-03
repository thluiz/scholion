---
title: "Guide: How to use a MacMini as your Xamarin.iOS Build Host"
date: '2016-04-13T11:40:28-03:00'
category: webclip
summary: 'The guide explains how to pair a Windows PC with a MacMini for Xamarin.iOS builds, keep the machines on the same network with Hamachi, and use remote access so development can continue from anywhere.'
tags: ["xamarin-ios", "macmini", "windows-pc", "remote-access"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Guide: How to use a MacMini as your Xamarin.iOS Build Host"
    url: "https://thomasmartinsen.com/2015/08/30/how-to-use-a-macmini-as-your-xamarin-build-host/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-04/thomasmartinsen-com--guide-how-to-use-a-macmini-as-your-xamarin-ios-build-host.md"
    kind: repo
---

The page explains how to use a MacMini as a Xamarin.iOS build host while continuing to develop on a Windows PC. It says this setup can be a cheaper alternative to buying a MacBook Pro, and it works even when you travel if the machines stay connected.

## Reading notes

- Install Xamarin on both the Windows PC and the MacMini, which automatically installs Xamarin.iOS Build Host on the MacMini.
- Keep the Windows PC and MacMini on the same network so Visual Studio can find the build host.
- Use a VPN tool such as Hamachi to make both machines join the same network from different locations.
- In some cases, restart Visual Studio after connecting for the first time to keep the connection stable.
- Use remote access when you are not near the MacMini, because debugging may run in the simulator on the MacMini or on a device connected to it.
- The author tried TeamViewer and UltraVNC and preferred UltraVNC for simplicity.
- Enable remote access on the MacMini, since macOS already includes a VNC server.
- Keep the MacMini awake with an app such as Stay Awake, and set Xamarin.iOS to start automatically.
- Configure the MacMini to auto login during startup so it stays available after a reboot.
- The author notes that the connection can become unavailable on some company guest networks and some mobile networks.
