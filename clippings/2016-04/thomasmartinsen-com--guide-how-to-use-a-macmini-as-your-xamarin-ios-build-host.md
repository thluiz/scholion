---
url: "https://thomasmartinsen.com/2015/08/30/how-to-use-a-macmini-as-your-xamarin-build-host/"
captured_at: "2016-04-13T11:40:28-03:00"
title: "Guide: How to use a MacMini as your Xamarin.iOS Build Host"
domain: "thomasmartinsen-com"
---

# Guide: How to use a MacMini as your Xamarin.iOS Build Host

This guide describes how to setup your Windows PC and your MacMini so you can use your MacMini as Xamarin.iOS Build Host and continue to develop on your Windows PC – even if you’re traveling.

If you develop iOS apps based on Xamarin you will most likely be using a MacBook Pro (or something similar) running Windows in some form. If you’re a Windows developer working on a Windows PC and for good reasons wants to stick to this setup, you have an alternative to buying a MacBook Pro. To be able to compile your Xamarin.iOS apps you will need a Mac – but you can actually settle with a MacMini costing less than 25% of a MacBook Pro.

**Xamarin**

First of all you will need to have [Xamarin](http://xamarin.com/platform "Xamarin") installed on your Windows PC and on your MacMini. When you install Xamarin on your MacMini it will automatically install *Xamarin.iOS Build Host*. If you install Visual Studio 2015 on your Windows PC you can choose to install Xamarin during the setup process.

**The network**

Your Windows PC and your MacMini needs to be on the same network for Visual Studio to be able to find the Xamarin.iOS Build Host. The MacMini is designed to work as a static machine in an office or a home. If you’re working from your office this is not an issue – you will most likely be on the same network.

However if you travel or work from different locations it is not an option to bring your MacMini all the time. For the Windows PC and the MacMini to be on the same network all the time you can use a simple VPN tool. I have good experience with [Hamachi](https://secure.logmein.com/products/hamachi/ "Hamachi") from LogMeIn – it is really simple to create a network and have your Windows PC and your MacMini to join the network.

To connect Visual Studio and your Xamarion.iOS Build Host you will need the IP address of our Xamarin.iOS Build Host – it is revealed in the Hamachi client. I have experienced that in some cases you will need to restart Visual Studio have you connected for the first time to be able to maintain the connection.

Now that you’re on the same network the connection and have setup the connection between Visual Studio and your Xamarin.iOS Build Host, the connection will remain even if you’re on different locations.

**Remote access**

When you debug a Xamarion.iOS app from Visual Studio you will have it running either in a simulator (on the MacMini) or on a device (connected to your MacMini). If you’re working right next to your MacMini you can easily see the simulator or use a device.

However if you’re on a different location you will need to have remote access to your MacMini.

On your Windows PC you will need to have a viewer installed. I have tried [TeamViewer](https://www.teamviewer.com/en/index.aspx) and [UltraVNC](http://www.uvnc.com/docs/uvnc-viewer.html) and found UltraVNC to be the best tool for me as it is the most simple tool (if you choose UltraVNC beaware of the many ads on their homepage – the viewer is ad free).

On your MacMini you just need to enable remote access as it already have a VNC server included. Graham Miln wrote a [post](http://www.dssw.co.uk/blog/2007-05-14-a-vnc-server-is-included-in-mac-os-x-104/) on how to enable it.

Using the client viewer you can now easily debug and run your Xamarin.iOS app even if you’re not sitting next to your MacMini.

**MacMini startup**

For the above setup to work it is crucial that your MacMini is available at all times. By default the MacMini will go sleep after a few minutes if not used. I bought a small app to keep the MacMini awake called [Stay Awake](https://itunes.apple.com/us/app/stay-awake/id553214148?mt=12) – I’m sure there are several app like it.

I setup Stay Awake and Xamarin.iOS to start automatically when the MacMini starts – and finally I set up the MacMini to auto login during startup to ensure that it will be availble even if it for some reason reboots.

// thomas

Notice: I have experienced that the connection between Visual Studio and Xamarin.iOS Build Host becomes unavailable on some company guest networks and on some mobile networks.
