---
title: "Starting Xamarin Android application development with F#"
date: '2016-05-02T08:13:57-03:00'
category: webclip
summary: 'The post describes setting up a Xamarin Android project in F#, using a PCL to share app logic, and the emulator and device deployment issues the author had to solve.'
tags: ["xamarin-android", "f-sharp", "pcl", "android-emulator"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Starting Xamarin Android application development with F# | marisks # code"
    url: "http://marisks.net/2016/04/19/starting-xamarin-android-application-development-with-fsharp/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-05/marisks-net--starting-xamarin-android-application-development-with-fsharp.md"
    kind: repo
---

The author says Xamarin Android was a natural choice because he needed to build an Android app as a .NET developer. He had earlier managed a simple F# app, but had trouble with PCL libraries until Visual Studio 2015 Update 2 added new F# project templates for Android, iOS, and PCL.

Project setup still needed an extra step because the Android template would not load until F# SDK 3.0 was installed. After that, the author could use a PCL to keep application logic separate from the UI and reuse it in iOS or Windows Phone versions if needed.

## Reading notes

- Visual Studio 2015 Update 2 adds F# templates for Android, iOS, and PCL
- A PCL lets the app keep logic separate from the UI and reuse it across platforms
- The Android project template would not load until F# SDK 3.0 was installed
- The default Android Emulator did not run correctly for the author
- Visual Studio Android Emulator did not work on his machine because of Hyper-V and a Windows 10 upgrade issue
- Genymotion worked after Hyper-V was disabled
- Deploying to a phone required enabling developer options, turning on USB debugging, and connecting the device to Visual Studio
- The post closes by saying setup is not smooth, but once the project and deployment work, starting app development is easy for a .NET developer
