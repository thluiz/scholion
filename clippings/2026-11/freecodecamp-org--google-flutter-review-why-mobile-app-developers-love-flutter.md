---
url: "https://www.freecodecamp.org/news/why-mobile-apps-makers-are-in-love-with-flutter/"
captured_at: "2026-11-16T19:52:17+00:00"
title: "Google Flutter Review – Why Mobile App Developers Love Flutter"
domain: "freecodecamp-org"
---

![Google Flutter Review – Why Mobile App Developers Love Flutter](https://www.freecodecamp.org/news/content/images/size/w2000/2020/04/emile-perron-xrVDYZRGdw4-unsplash.jpg)

By Vitaly Kuprenko

Why do app makers love Flutter? Because Flutter is amazing.

Flutter caters to both businesses (by offering reasonable development costs) and developers (by offering great usability and speed). That’s why some big companies have switched to Flutter, such as Google Ads, Alibaba, Reflectly, and many more.

Google has done a great job building Flutter, and they continue making this framework even better.

In this post, I’ll give a quick overview of Flutter and its brand new perks, and I'll talk about why this framework is worth working with. Plus, I'll discuss what may hold big companies back from adopting Flutter.

But first things first.

## What’s the Gist of Flutter?

Here are things about Flutter you may already know:

*   it's an open-source, cross-platform toolkit
*   apps are written in the Dart programming language
*   it has its own graphics engine (Skia)
*   it supports three platforms officially: iOS, Android, and web (in beta)
*   unofficially – it also supports desktop

Google introduced the first version of Flutter at the end of Feb 2018. As of April 2020, 1.12 release is available.

## What's so special about Flutter?

Flutter combines the quality of native apps with the flexibility of cross-platform development.

Actually, many cross-platform tools let you write the code once and use it on both iOS and Android. Yet not all can render the same look like a native app.

But that's exactly what Flutter does: instead of being a wrapper on top of native UI components (like React Native and Xamarin), Flutter draws the UI from scratch.

Flutter maintains the native experience and feel of the app, and you don't have to worry about its performance on any platform.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Mockup1-Copy.png)

Besides, since Flutter's an open-source framework, any dev can make changes to it on [GitHub](https://github.com/flutter/flutter) and send merge requests. And if you take a look at Flutter's popularity – **90.4K** GitHub **stars**, **12k forks**, and **18,445 commits** – you'll get the idea that devs love Flutter and contribute to making it better.

## How Does Flutter Work?

**Flutter isn't compiled directly to iOS or Android apps**. Apps are launched based on a combination of rendering engine (built on C++) and Flutter (built on Dart). All files generated this way attach to each app and SDK assemblies software for a specific platform.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Flutter-Architecture.png)

It's like game development: a game doesn't allocate its framework, and functionality is carried out with the game engine. Same for Flutter software – all apps based on the Flutter SDK replace parts of native frameworks with Flutter elements.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/How-Flutter-interacts-with-native-components.png)

Although it can impact the size of the end app, performance is still quite good – rendering is made with speeds up to **120 FPS**.

Due to native compilation for ARM processors, simple rendering, and a set of integrated widgets and tools, Flutter makes the development process simpler.

Plus, it offers a few very tasty features like **Hot Reload**.

Here’s how it works:

When you click on the Hot Reload button, all changes in code are displayed in gadgets, emulators, and simulators right away. The app continues working from where it was before you hit the hot reload: the code updates, but execution continues.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/How-Flutter-works-Copy.png)

## Why Choose Flutter for Cross-Platform Apps?

New Flutter versions will keep coming out with more advanced features up their sleeves. But there are already a lot of enhanced features that perfectly explain why Flutter is so well-loved.

**First**, cross-platform development with Flutter, contrary to popular belief, doesn't make software worse.

Flutter comes with all native widgets for Android and iOS interfaces like Material Design and Cupertino. Besides, the framework can change the behavior of separate elements to create similar UX for the app's users.

**Second**, Flutter makes it possible to implement discrete file compilation in the dev mode. JiT compilation speeds up development and software debugging.

**Third**, Flutter allows for a flexible and scalable backend.

It supports plugins like Firebase, SQLite, and so on ([pub.dev](https://pub.dev/flutter/packages) will help you find the one you require). Firebase makes the app's infrastructure scalable, serverless, and redundant.

So if you're working on apps that require real-time databases or cloud functions, Flutter's got your back.

And the last one: Flutter is very **easy to learn**.

From the very beginning, Google devs set a goal to lower the entry barrier. They carefully worked out documentation and resources developers can use. It even has special sections you can use to start learning the framework depending on your specialization:

*   Flutter for [Android](https://flutter.dev/docs/get-started/flutter-for/android-devs) devs
*   Flutter for [iOS](https://flutter.dev/docs/get-started/flutter-for/ios-devs) devs
*   Flutter for [React Native](https://flutter.dev/docs/get-started/flutter-for/react-native-devs) devs
*   Flutter for [Xamarin.Forms](https://flutter.dev/docs/get-started/flutter-for/xamarin-forms-devs) devs
*   Flutter for [web](https://flutter.dev/docs/get-started/flutter-for/web-devs) devs

Because of Flutter's detailed documentation, you'll figure out how to write code in Dart even if you only have experience with Unity graphic tools for making Android games.

## Flutter 1.12 (Latest Version) and Its Perks

Let's see what hot features Flutter introduced in its latest [1.12](https://flutter.dev/docs/development/tools/sdk/release-notes/release-notes-1.12.13) version:

### iOS Dark mode

From now on, Flutter supports the iOS 13 look and feel, including complete dark mode support in the Cupertino widgets. And it isn’t just about swapping out the background but adapting the rest of the colors to be a good match.

### Add-to-app support

Another big improvement is the Add-to-App update, which is for integrating Flutter into already existing iOS/Android apps.

The new version of Flutter supports adding one fullscreen Flutter instance to the app, along with:

*   Stabilized [APIs integration](https://flutter.dev/docs/development/add-to-app#api-usage) in Java, Kotlin, Objective-C and Swift
*   Support for using plugins in Flutter modules
*   Additional integration mechanisms via Android AARs and iOS frameworks

### Beta web support

New Flutter master, dev, and beta channels provide improved support for the web. Want some examples?

Here’s **Rivet**, an education project that used Flutter and Firebase to create a web version of their app.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Mockup1-Copy-2.png)

### Dart 2.7

The new version of the framework introduces Dart 2.7.

This update enhances the experience of functioning with Dart 2.5 in how safe strings handles abilities and extension processes. This helps developers prevent errors when variables get a zero value and parse integers in a string.

And here are some other features of the latest Flutter version:

*   macOS desktop support (alpha)
*   multi-device debugging
*   golden image testing
*   Android build improvements
*   updated DartPad

## It's Good, But Not Without Problems: What’s Holding Devs Back?

Flutter is really cool: easy to start, simple to work with, and presented by a huge tech company. Yet here are the reasons why your Senior Developer may not share your optimism.

### Dart’s (low) popularity

Unlike Java/Kotlin for Android or Swift/Objective-C for iOS, Dart doesn't have high popularity yet. And it's highly unlikely it will.

Dart isn't too hard to learn, and there are tons of tutorials (like this [one](https://dart.dev/guides/language/language-tour)), but some devs keep sticking to Java and other familiar tools.

At the same time, you can't use Flutter and not use Dart: even Flutter's killer feature – Hot Reload – won't work without Dart.

### Doesn't support all devices

You can't make apps for 32-bit iOS devices like those older than iPhone 5s. Same for Windows desktops: you can't run Flutter on your 32-bit laptop.

And Flutter devs have no plans on fixing it as "this would involve a very significant amount of work."

So if you want to code with Flutter, you'll have to own an x64-bit device or upgrade the one you use now.

### Limited number of libraries

Although there are many Flutter libs like **fl\_chart** (for drawing graphics in Flutter), **path\_provider** (used to locate a file on Android/iOS), [**flutter\_sliding\_tutorial**](https://github.com/Cleveroad/flutter_sliding_tutorial) and many more, the number is still limited.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/-------1-.gif) _Flutter Sliding Tutorial_

This isn't hard to explain: Flutter is a relatively new framework, and developers haven't had enough time to develop as many libs as native languages offer.

Still, the most important libraries are already there, and new ones are coming out all the time.

### Flutter apps are bigger in size

...compared to native developed applications. Flutter's team [measured](https://flutter.dev/docs/resources/faq#how-big-is-the-flutter-engine) the minimal app size (with no Material Components, just a single Center widget, built with flutter build apk --split-per-abi), bundled and compressed, to be 4.3 MB for ARM, and 4.6 MB for ARM 64.

The basic app now is ~**4MB** in Android and ~**10MB** in iOS.

### Little proven expertise

Flutter may be loved by developers, but large companies haven't hurried to stop making native (or React Native) apps and turn to Flutter.

For most companies, the biggest issue is Flutter's novelty. Dart is newer than Java or C#, and Flutter itself is brand new.

Of course, there are many [Flutter open-source apps](https://www.cleveroad.com/blog/open-source-flutter-apps), including big ones like Google Ads or Hamilton (check the full list [here](https://itsallwidgets.com/)), yet not too many.

And no one wants to be the person who adopts a brand new framework only to have to switch to native development a few months later.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Flutter-vs-React-Native-Copy.png)

But what’s even more important is that Flutter is the path you walk alone:

*   there aren’t many confirmed best practices (at least at large-scale projects)
*   always a chance you're the first one facing this particular problem
*   little hope someone will help you out – you'll have to take each step carefully and be ready to face the consequences

## Where to Use Flutter

First of all, it's better to use Flutter for MVP startups when you have limited time and often money to verify the business model.

A Flutter app is **cheaper\***:

*   \*compared to the cost of two native apps
*   the development team is 40% smaller
*   linear processes
*   you can spend more time working on the app’s features

By opting for a Flutter project, you’re cutting down the number of development hours. Flutter development doesn't take as much time compared to native.

Here’s an example. Let’s say you’re making an Instagram-like app for two platforms. iOS development is going to take, roughly, about **700** hours, Android – also **700h**.

With Flutter, you’ll cover both platforms and save time: **700h Android + 700h iOS vs. 700h Flutter.**

You’re saving tons of time you can spend on something else, like polishing the features.

## Wrapping Up

If you're building apps in limited time with a limited budget, Flutter is definitely worth trying.

It's just as good as it seems to be, and with each new update, Google devs add more even tools for cross-platform development.

Of course, this framework may seem unusual for C# and Java lovers, but it does not mean it'll force you out of your comfort zone. Having mastered the small syntax differences, you will soon see that UI development goes a few times faster compared to native development.

And if you're successful, and if Flutter sticks around, it could bring you some exciting mobile development experience and opportunities in the future.

* * *

Learn to code for free. freeCodeCamp's open source curriculum has helped more than 40,000 people get jobs as developers. [Get started](https://www.freecodecamp.org/learn)
