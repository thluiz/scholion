---
url: "https://code.msdn.microsoft.com/windowsapps/Personalization-App-sample-9ebfe147"
captured_at: "2015-06-07T20:43:35-03:00"
title: "Windows 8 Lock screen personalization sample exemplo em C#, C++, JavaScript para Visual Studio 2013"
domain: "code-msdn-microsoft-com"
---

# Lock screen personalization sample

This sample demonstrates how a developer can use the [**LockScreen**](http://msdn.microsoft.com/library/windows/apps/br241847) API to set the current user's lock screen image. This sample uses classes from the [**Windows.System.UserProfile**](http://msdn.microsoft.com/library/windows/apps/br241881) namespace. In particular, it uses the **LockScreen** class to set the user's lock screen image. It also demonstrates how to register an RSS feed that can be used as a source for a lock screen slideshow.

The lock screen is the screen shown when you lock your computer, as well as when you reboot the device or wake it from a sleep state. It is a user-customizable surface that both conveys information and protects the computer against unauthorized use.

The sample lets you use the item picker to select an image your Pictures library to use as the lock screen image. If the sample successfully uses the selected image for the lock screen, the image appears in the output area of the sample's main page. You can also select the location of an RSS feed that can supply images for a lock screen slideshow.

Note that to use this sample, your copy of Windows 8.1 must be activated.

To learn more about the lock screen, see [Lock screen overview](http://msdn.microsoft.com/library/windows/apps/hh779720).

To obtain an evaluation copy of Windows 8.1, go to [Windows 8.1](http://go.microsoft.com/fwlink/p/?linkid=301696).

To obtain an evaluation copy of Microsoft Visual Studio 2013, go to [Visual Studio 2013](http://go.microsoft.com/fwlink/p/?linkid=301697).

**Note**  For Windows 8 app samples, download the [Windows 8 app samples pack](http://go.microsoft.com/fwlink/p/?LinkId=301698). The samples in the Windows 8 app samples pack will build and run only on Microsoft Visual Studio 2012.

## Related topics

[**LockScreen**](http://msdn.microsoft.com/library/windows/apps/br241847)

[Windows 8 app samples](http://go.microsoft.com/fwlink/p/?LinkID=227694)

[**Windows.System.UserProfile**](http://msdn.microsoft.com/library/windows/apps/br241881)

## Operating system requirements

|  |  |
| --- | --- |
| Client | Windows 8.1 |
| Server | Windows Server 2012 R2 |

## Build the sample

To build this sample, open the solution (.sln) file titled Personalization.sln from Visual Studio 2013 for Windows 8.1 (any SKU). Press F7 or go to **Build->Build Solution** from the top menu after the sample has loaded.

## Run the sample

To run this sample after building it, press F5 (run with debugging enabled) or Ctrl+F5 (run without debugging enabled) from Visual Studio 2013 for Windows 8.1 (any SKU). (Or select the corresponding options from the **Debug** menu.)
