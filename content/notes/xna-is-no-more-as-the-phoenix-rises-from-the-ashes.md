---
title: "XNA is no more, as the phoenix rises from the ashes"
date: '2015-03-27T08:05:42-03:00'
category: webclip
summary: 'The post says MonoGame has broken its ties to XNA, can now be developed and build content on Windows, MacOS, or Linux, and remains an active project with broad platform support.'
tags: ["monogame", "xna", "game-development", "cross-platform"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "XNA is no more, as the phoenix rises from the ashes - CodeProject"
    url: "http://www.codeproject.com/Articles/889025/XNA-is-no-more-as-the-phoenix-rises-from-the-ashes"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-03/codeproject-com--xna-is-no-more-as-the-phoenix-rises-from-the-ashes.md"
    kind: repo
---

MonoGame’s 3.3 release is presented as a break from XNA, with the project now standing on its own. The post says developers can build MonoGame content on Windows, MacOS, or Linux, and that old XNA 4.0 projects should still work in MonoGame with a few possible hiccups.

## Reading notes

- MonoGame has broken its ties to the old XNA framework.
- The 3.3 release lets developers build content on Windows, MacOS, or Linux.
- Before 3.3, a Windows host was needed to compile content.
- New MonoDevelop or Xamarin Studio plugins and templates are available.
- Supported platforms listed include Android, iOS, Linux, MacOS, Windows OpenGL, Windows DirectX, Windows 8 / 8.1, Windows Phone 8 / 8.1, and Windows Universal apps.
- The experimental 3.3 PCL platform release is still a work in progress.
- MonoGame supports most consoles, but access depends on having contracts in place.
- WindowsGL users need to remove SDL.DLL before installing the NuGet package.
- Windows Phone 8.0 projects may need MonoGame.Framework references removed from the .csproj file before installing NuGet.
- XNA is described as still living on in universities and on Xbox 360 publishing.
- The author says MonoGame is a very active project and expects more frequent releases and NuGet updates.
- The Universal App template targets both Windows Phone 8.1 and Windows 8.1.
- Tom Spilman says MonoGame expects to support Win10 universal apps when the SDK is available.
