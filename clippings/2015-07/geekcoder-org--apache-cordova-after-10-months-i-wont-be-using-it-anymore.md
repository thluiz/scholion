---
url: "http://geekcoder.org/apache-cordova-after-10-months-i-wont-using-it-anymore/"
captured_at: "2015-07-06T19:04:35-03:00"
title: "Apache Cordova: after 10 months, I won't be using it anymore"
domain: "geekcoder-org"
---

At the time of I wrote these lines, it's been 10 months I'm using Apache Cordova on the app [http://mindup.io](http://mindup.io/), and I explain why I will not use it for my next projects.

I want to be clear here, cordova is a beautiful project and has a lot of pros, but you must think carefuly before using it. It does not fit all the usecases and I would like to quickly describe some cons.

## Can have bad performances.

Doing your app with Cordova can be slow, and this is absolutely normal. On iOS for example, there is one thread which drives UI and handles all the touch events. Then the other threads can be used to access a file or a db, or to do some other processing. If you use Cordova, you have only one thread dedicated to your WebView, and this is in it you will do everything. If you want to display some loaders in the UI while you're are accessing the db or serializing data for the web, you will quickly see that is not smooth. This is the same if you want to scroll elements for example.

Also, there is no way to store or get data very efficiently, because as soon as you are accessing an element in the file system, you have a big overhead for serialization between the native layer and the js web view layer.

## You spend weeks to try to reproduce some native behavior, and you're not even close.

The SDK of Android or iOS are pretty nice. You have a lot of UI element you can use out of the box. In few lines of code or just dragging and dropping it. To do such of easy thing with Cordova in html5/css3, you can spend days and days. First, you have to find how to do it, but this is only the beginning. Then you have to make it works on all version of Android you want to support, then you have to make it work on iOS and all versions you want to support. So, this means you have you handle a lot of different versions of browser, with some which are a bit buggy for old versions of OSes. This is a lots of work for something that take you few minutes or seconds with the native way.

## There is a lot of plugins to interface.

Thanks to the community of Apache Cordova! They did a lot of plugins to interface some native elements like the GPS, the push notifications, all the captors, etc. That's nice but there is some points:

### - There is special case to handle for each OSes.

Cordova aim to give you the ability of developing one app for all platforms, but you will have to know the behavior of each element on each platform your using. For example, for the geolocation on iOS you can easily know if the geolocation is allowed by the user or not. On android to do it you have to install another plugins which only do that, and it only works with some versions of the OS. It is just one example among many, but it is just to point out that this aspect is far to be perfect.

### - OSes are growing quickly but the community is not active enough to maintain it.

Mobiles OSes are growing very fast, there is alway new features or new way to use the sdk. This is great because it allows you to develop your apps quicker and quicker and in a more robust way. With Apache Cordova, just forget that. If you wait on someone to maintain a plugin to have the same advantages, you can wait long time. You would better do it yourself, but yes! It is very time consuming and you must be able to code in every languages of the OSes you are using and you must be able to use the SDK of each of them too.

### - There is bug and problems.

Nobody is really maintaining plugins and nobody is controlling the quality of code. A lot of plugins are not shipped with test and you will experience some bugs.   
Sometime, the plugins are just too young or not maintained, so you will not able to use all the power. For example, at the moment I'm writing this post, the push notification plugin do not give a way to do a background job when you receive a notification and your app is in background or closed.

## Do you really need a cross platform app ?

We all want our work accessible to a maximum potential number of user, of course. But trying to do it doing a cross platform app, is not a good idea. There is no sens to spend time trying to do your app multi-platform from the beginning. If your app do not works on iOS, it will not works on android neither. Spend time on what is important: find what concept is working, iterate over it as quickly as possible again and again, make it working, make it growing. Then, of course this is a good idea to think about other platforms, because your app is mature enough and you will not spend time on duplicate (and some time wrong) modifications. When you begin a project you often have very limited ressources and budget. The most precious ressource you have is time, do not waste it! I think something you can do in six month with Apache Cordova can be done in one in native.

## I want more ?

Facebook wrote a good article when they have decided to switch from a web app to a native one. This is not about Apache Cordova, but the points are the same: <https://www.facebook.com/notes/facebook-engineering/under-the-hood-rebuilding-facebook-for-ios/10151036091753920>

## Edit

Someone pointed me out that what I said about perfomences is not always true for new devices. I wanted to quote his comment (<https://news.ycombinator.com/user?id=AshleysBrain>):

> On performance, the new WKWebView on iOS (with Nitro JS + GPU rendering, including WebGL), and the Chromium webview on Android 5.0+ (or Crosswalk for Android 4.0+, similar features all round), radically changes the performance story. It's almost identical to the system browsers now. Facebook's comments about HTML5 were back in the dark ages when the webviews generally used horribly slow software rendering and didn't have JIT for Javascript on iOS. It's a completely different picture today. In fact, our performance-sensitive HTML5 game engine[1] targets the iOS 8 webview and Crosswalk for Android for making native apps, and they generally work as well as in the browser, which is very good, especially on newer devices. Modern web APIs are also asynchronous which helps offload work from the UI thread, and Web Workers can do that for arbitrary JS code too. For example our game engine runs A\* pathfinding in a web worker, offloading any performance impact from the CPU intensive algorithm and running it in parallel to the game.
