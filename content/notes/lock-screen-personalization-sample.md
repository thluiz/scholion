---
title: "Lock screen personalization sample"
date: '2015-06-07T20:43:35-03:00'
category: webclip
summary: 'This sample shows how to use the LockScreen API in Windows.System.UserProfile to set the current user’s lock screen image and register an RSS feed for a lock screen slideshow.'
tags: ["lockscreen", "windows-system-userprofile", "rss-feed"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Windows 8 Lock screen personalization sample exemplo em C#, C++, JavaScript para Visual Studio 2013"
    url: "https://code.msdn.microsoft.com/windowsapps/Personalization-App-sample-9ebfe147"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-06/code-msdn-microsoft-com--lock-screen-personalization-sample.md"
    kind: repo
---

This sample shows how to use the LockScreen API to set the current user’s lock screen image. It also shows how to register an RSS feed as a source for a lock screen slideshow, and it uses classes from the Windows.System.UserProfile namespace.

The sample lets you choose an image from the Pictures library with the item picker. If the image is accepted for the lock screen, it appears in the sample’s output area. It also lets you choose the location of an RSS feed that can supply images for a slideshow.

## Reading notes

- Uses the LockScreen class to set the user’s lock screen image.
- Demonstrates registering an RSS feed as a source for a lock screen slideshow.
- Uses classes from the Windows.System.UserProfile namespace.
- Lets you pick an image from the Pictures library with the item picker.
- Shows the chosen image in the output area when the lock screen image is set successfully.
- Requires an activated copy of Windows 8.1.
- The solution file is Personalization.sln.
- Build the sample in Visual Studio 2013 for Windows 8.1.
- Run the sample with F5 or Ctrl+F5 in Visual Studio 2013 for Windows 8.1.
