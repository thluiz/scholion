---
url: "https://web.archive.org/web/20200812092316id_/https://devblogs.microsoft.com/xamarin/xamarin-essentials-now-with-permissions-app-theme-authentication/"
captured_at: "2026-11-18T11:20:32+00:00"
title: "Get Permissions, App Theme, & Authentication | Xamarin Blog"
domain: "web-archive-org"
---

## Xamarin.Essentials: Now with Permissions, App Theme, & Authentication

![Avatar](https://secure.gravatar.com/avatar/048050ef65ec9aa188c662ae1895ecc7?s=58&d=mm&r=g)

James

April 23rd, 2020

Since the first release of [Xamarin.Essentials](http://docs.microsoft.com/xamarin/essentials), developers have enjoyed the simplification of complex native features into a single cross-platform library. They can do this across iOS, Android, UWP, Tizen, watchOS, and even tvOS! No matter what type of app you are writing, there is absolutely something in Xamarin.Essentials for you. With the recent release of Xamarin.Essentials 1.5, even more cross-platform capabilities are unlocked for developers. Let us review just a few features that you can access right now.

![Logo for Xamarin.Essentials](https://devblogs.microsoft.com/xamarin/wp-content/uploads/sites/44/2018/12/Essentials.png)

Just about every operating system has fully embraced dark mode for apps. Checking what the user has selected as their device default should be easy. Which is why we included a new way to select the requested theme.

```

AppTheme appTheme = AppInfo.RequestedTheme;
```

When using this new API and dynamic themes, easily enable your app to react to light/dark mode changes:

Checkout the [MyContacts sample on GitHub](https://github.com/xamarin/app-contacts) for a real-world sample. Then watch the Xamarin.Essentials API of the Week on App Theme:

## Permissions

Want to use geolocation, contacts, or the camera? You will need to ask for permission from your users. Xamarin.Essentials makes this easier than ever with just a few lines of code. Simply add the permissions into your application configuration, then check and request permissions from your shared code:

```

public async Task CheckAndRequestLocationPermission()
{
    var status = await Permissions.CheckStatusAsync();
    if (status != PermissionStatus.Granted)
    {
        status = await Permissions.RequestAsync();
    }

    // Additionally could prompt the user to turn on in settings

    return status;
}
```

Want more? Checkout the full Xamarin.Essentials API of the Week video:

## [Web Authentication](https://docs.microsoft.com/xamarin/essentials/web-authenticator)

Looking to add authentication to your mobile app? Xamarin.Essentials has you covered! It pairs beautifully with ASP.NET Core.

[Jon Dick](https://twitter.com/redth) just did a [full blog post](https://devblogs.microsoft.com/xamarin/authentication-xamarin-essentials-aspnet/) on how to setup web authentication with Xamarin.Essentials. If needed, read through Jon’s blog to get set up and then come back to this post.

## What is Next?

We are glad that you asked! At the [.NET Conf – Focus on Xamarin](https://channel9.msdn.com/Events/dotnetConf/Focus-on-Xamarin/Spectacular-Components-for-Xamarin-Apps) event, we announced our plans for Xamarin.Essentials 1.6. This release will include official support for macOS. Additionally, there will be integration of amazing community pull requests. PRs including [File Picker](https://github.com/xamarin/Essentials/pull/975), [Haptic Feedback](https://github.com/xamarin/Essentials/pull/1138), [App Actions](https://github.com/xamarin/Essentials/pull/1190), [Calendar](https://github.com/xamarin/Essentials/pull/1010), and more! Be sure to Like and Follow [Xamarin.Essentials on GitHub](https://github.com/xamarin/essentials).

## Get Started

Xamarin.Essentials is included with every project template! Make sure you upgrade to the latest version in NuGet today. Integrate Xamarin.Essentials into an existing app through our [getting started documentation](http://docs.microsoft.com/xamarin/essentials/get-started).
