---
url: "https://nicksnettravels.builttoroam.com/look-ios-developer-no-mac-required-build-an-ios-application-using-xamarin-and-visual-studio-for-windows-without-using-a-mac"
captured_at: "2026-11-16T04:23:15+00:00"
title: "Look iOS Developer, No Mac Required – Build an iOS Application using Xamarin and Visual Studio for Windows without using a Mac"
domain: "nicksnettravels-builttoroam-com"
---

* * *

**Update 31-01-2022**

Thanks to [BlueRaja](http://www.blueraja.com/blog/) who was prepared to document their experience, here are a bunch of updates/changes/fixes that need to be applied when following this post:

1.  The non-Microsoft-store version of iTunes does NOT work anymore.  You MUST have the Microsoft Store version in order for it to work.
2.  You NEED the latest version of VS 2022. VS 2019 no longer works. And a bug related to Hot Restart was recently fixed in VS 2022.
3.  You need to sign up for  [Apple development](#) program AND wait to be accepted. They say it takes up to 48 hours, but I had to wait 1.5 weeks to become accepted -\_-
4.  If you create the iOS project using Add –> New Project –> “iOS App (Xamarin)”, you won’t see “Local Device” in the dropdown.  Instead the project type needs to be either “iOS XAML App (Xamarin Forms)” or “Mobile App (Xamarin Forms)
5.  If you get stuck at  “Running automatic provisioning” in Step 3 of the wizard, you need to

5.  Right-click iOS project –> Properties –> iOS Bundle Signing –> Manage accounts –> View Details –> Create Certificate –> Create development certificate
6.  Go to [https://developer.apple.com/account/resources/profiles/add](https://developer.apple.com/account/resources/profiles/add) and setup a provisioning profile. It will make you setup a few other things first.
7.  If you get “myProject.iOS is not configured to deploy”, go to Build –> Configuration Manager and click “deploy”

Thanks again to [BlueRaja](http://www.blueraja.com/blog/)

* * *

If you’re a die-hard Windows user, like me, you’ll be excited to know that you can now build iOS application using Xamarin (and Xamarin.Forms) and Visual Studio, **without** having to buy or use a Mac. That’s right for development, you no longer need to invest, or carry around, a Mac. In this post I’ll walk you through how to enable this feature.

ComparePhones

Discover more

Master .NET

Explore macOS

MacOS

I’m working in the latest preview of Visual Studio 2019 and as of now, to use Xamarin Hot Restart (the feature that powers the **no Mac** development experience), you need to check the Enable Xamarin Hot Restart option under Preview Features in the Tools, Options dialog.

TryDev Tools

[![](https://wordpressblogimages.builttoroam.com/blogimages/2021/09/01-300x203.webp)](https://wordpressblogimages.builttoroam.com/blogimages/2021/09/01.webp)

After enabling Xamarin Hot Restart, make sure you restart Visual Studio. Next, set your iOS project to be the startup project by right-clicking the iOS project in Solution Explorer, followed by the Set as Startup Project menu item.

[![](https://wordpressblogimages.builttoroam.com/blogimages/2021/09/02-300x201.webp)](https://wordpressblogimages.builttoroam.com/blogimages/2021/09/02.webp)

Make sure in the toolbar the option next to the play button says Local Device. Click the play button, which will kick off the Setup Hot Restart experience.

[![](https://wordpressblogimages.builttoroam.com/blogimages/2021/09/03-300x44.webp)](https://wordpressblogimages.builttoroam.com/blogimages/2021/09/03.webp)

There are a couple of steps to jump through the first time you want to use Hot Restart. Make sure you follow the instructions to avoid having to redo steps.

[![](https://wordpressblogimages.builttoroam.com/blogimages/2021/09/04-300x291.webp)](https://wordpressblogimages.builttoroam.com/blogimages/2021/09/04.webp)

The first step in the process it to Download iTunes – make sure you click the Download iTunes button. **Do NOT** install iTunes from the Microsoft Store. If you’ve done this previously, make sure you uninstall it, and then install it by clicking the Download iTunes button.

[![](https://wordpressblogimages.builttoroam.com/blogimages/2021/09/05-300x291.webp)](https://wordpressblogimages.builttoroam.com/blogimages/2021/09/05.webp)

Clicking the Download iTunes button will open your default browser but it will attempt to immediately download the file – make sure you check out the downloads so you can launch the file once it’s downloaded.

[![](https://wordpressblogimages.builttoroam.com/blogimages/2021/09/06-300x116.webp)](https://wordpressblogimages.builttoroam.com/blogimages/2021/09/06.webp)

Step through the iTunes installer.

[![](https://wordpressblogimages.builttoroam.com/blogimages/2021/09/08-1-300x227.webp)](https://wordpressblogimages.builttoroam.com/blogimages/2021/09/08-1.webp)

Once iTunes is installed the Setup Hot Restart process will detect the presence of iTunes (note that it will **not** detect iTunes if you’re installed it from the Microsoft Store).

[![](https://wordpressblogimages.builttoroam.com/blogimages/2021/09/09-300x291.webp)](https://wordpressblogimages.builttoroam.com/blogimages/2021/09/09.webp)

Next, make sure you have an iOS device plugged in and that you’ve clicked the Trust option on the device when prompted to trust the connected computer. The Setup Hot Restart process should detect the attached device.

[![](https://wordpressblogimages.builttoroam.com/blogimages/2021/09/10-300x291.webp)](https://wordpressblogimages.builttoroam.com/blogimages/2021/09/10.webp)

Next, sign into your  [Apple Developer](#) account.

[![](https://wordpressblogimages.builttoroam.com/blogimages/2021/09/11-300x291.webp)](https://wordpressblogimages.builttoroam.com/blogimages/2021/09/11.webp)

And select the Development Team you want to use for provisioning.

[![](https://wordpressblogimages.builttoroam.com/blogimages/2021/09/12-300x291.webp)](https://wordpressblogimages.builttoroam.com/blogimages/2021/09/12.webp)

After completing the Setup Hot Restart process you should see that the build process will continue and that in the Output window you’ll see the iPA being created and subsequently pushed to the device.

[![](https://wordpressblogimages.builttoroam.com/blogimages/2021/09/13-300x77.webp)](https://wordpressblogimages.builttoroam.com/blogimages/2021/09/13.webp)

When prompted, you’ll need to launch the installed application on the iOS device – this manual step is required in order for Visual Studio to attach the debugger.

[![](https://wordpressblogimages.builttoroam.com/blogimages/2021/09/14-300x115.webp)](https://wordpressblogimages.builttoroam.com/blogimages/2021/09/14.webp)

And there you have it – you now have an iOS application being debugged using Visual Studio on an actual device with **no  [Mac](#) required**!!!
