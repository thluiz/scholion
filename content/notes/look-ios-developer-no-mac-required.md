---
title: "Look iOS Developer, No Mac Required"
date: '2020-04-20T21:22:33+00:00'
category: webclip
summary: 'The post explains how to build and debug an iOS app from Windows with Xamarin Hot Restart in Visual Studio, using a real iOS device and no Mac for development.'
tags: ["xamarin", "visual-studio", "ios-development"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Look iOS Developer, No Mac Required – Build an iOS Application using Xamarin and Visual Studio for Windows without using a Mac"
    url: "https://nicksnettravels.builttoroam.com/look-ios-developer-no-mac-required-build-an-ios-application-using-xamarin-and-visual-studio-for-windows-without-using-a-mac"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/nicksnettravels-builttoroam-com--look-ios-developer-no-mac-required.md"
    kind: repo
---

The post shows how to use Xamarin Hot Restart to build and debug an iOS app from Windows without needing a Mac for development. It says to enable the feature in Visual Studio preview options, set the iOS project as the startup project, and choose Local Device before starting the setup.

## Reading notes

- Enable Xamarin Hot Restart under Preview Features in Tools > Options, then restart Visual Studio.
- Set the iOS project as the startup project in Solution Explorer.
- Use Local Device in the toolbar before starting the Hot Restart setup.
- Install iTunes through the Download iTunes button, not from the Microsoft Store.
- Connect an iOS device and trust the computer when prompted.
- Sign in to an Apple Developer account and choose the Development Team for provisioning.
- After setup, Visual Studio continues the build, creates the iPA, and pushes it to the device.
- Launch the installed app on the iOS device when prompted so Visual Studio can attach the debugger.
