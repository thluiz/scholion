---
title: "Developing a Basic C# Application for the iPad Using Monotouch"
date: '2012-02-16T14:17:48-03:00'
category: webclip
summary: 'The article explains how MonoTouch lets C# developers build iPad apps, what setup is needed on Mac OS X, and how to create a basic UIKit interface with rotation support.'
tags: ["monotouch", "c-sharp", "ipad", "ios-development"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Developing a Basic C# Application for the iPad Using Monotouch - CodeGuru"
    url: "http://www.codeguru.com/csharp/csharp/cs_misc/article.php/c17923/Developing-a-Basic-C-Application-for-the-iPad-Using-Monotouch.htm"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-02/codeguru-com--developing-a-basic-c-sharp-application-for-ipad-using-monoto.md"
    kind: repo
---

MonoTouch is presented as a way for C# developers to build iOS apps without switching to Objective-C. The article also says the workflow feels closer to Visual Studio when using MonoDevelop, while still requiring Apple tools and the iOS SDK for testing and deployment.

## Reading notes

- MonoTouch brings C# to iPhone, iPod Touch, and iPad development, which can be easier for Microsoft developers than moving to Objective-C.
- It provides bindings for CocoaTouch form elements, including standard controls such as buttons and text boxes, plus touch-oriented elements for small screens.
- Testing and debugging require an Intel-based Mac, Apple’s SDK, Xcode, and registration in Apple’s developer program.
- A trial version is available, but it does not allow deployment to a physical device.
- Installation order matters, and MonoTouch depends on the latest Mono runtime for OS X and a special MonoDevelop version.
- The article points to tutorials, sample code, screencasts, blogs, and the book *iPhone Programming with MonoTouch and .NET/C#* as learning resources.
- Sample projects may need their target SDK version adjusted in project options if the installed SDK does not match.
- Apple UI guidelines matter for App Store approval, and screen rotation support is required.
- The article describes MVC as a common pattern in iPhone development and recommends the Cocoa Fundamentals Guide.
- A basic UIViewController can support autorotation by overriding `ShouldAutorotateToInterfaceOrientation` and returning true.
- An iPad app is described as fundamentally similar to an iPhone app, with hardware differences such as screen size and device-specific capabilities.
- A basic MonoTouch solution includes `Main.cs` and `MainWindow.xib`, with the XIB opened in Interface Builder to build the UI.
- The demo uses a text label and a button, then runs the app in the simulator.
- The trial version is meant for trying things out, while the Professional Edition costs $399 for deployment to a device.
