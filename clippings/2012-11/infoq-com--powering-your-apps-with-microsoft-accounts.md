---
url: "http://www.infoq.com/news/2012/11/Microsoft-Accounts"
captured_at: "2012-11-01T12:34:59-03:00"
title: "Powering Your Apps with Microsoft Accounts"
domain: "infoq-com"
---

A central theme with Windows 8 is the Microsoft Account. This is another attempt to offer a single sign-on system for both Microsoft and third-party services. We’ve seen Microsoft attempt to do this before with products such as Microsoft Wallet, Microsoft Passport, .NET Passport, Microsoft Passport Network, and Windows Live ID. The relationship between these products is murky with various branding and technology changes, but the goal is the same for each: to not lose potential customers who don’t want yet another username and password.

When a Windows 8 application starts it may request and authentication and access tokens. The authentication token verify the user’s account while the access token allows for retrieval of information about the user. The user will also be automatically signed into any website that implements the Microsoft Account SDK.

There are some benefits even for websites that already have their own authentication system. While there is no personal information available at this point, a user id is provided. By tracking the user using this id, it will be easier to personal the site for that user when they do officially sign up.

For advanced scenarios, the [Live SDK](http://msdn.microsoft.com/en-us/live/) can be used to access the user’s SkyDrive, profile, and social network. Access is granted using either OAuth 2.0 or the Live Connect REST API. Client side SDKs for Windows 8, Windows Phone, Android, iOS, and .NET make this process easier. Like other OAuth-based services, users will need to give explicit permission for your application to access their Microsoft data.

Another feature common with OAuth systems is the need for a “secret” that only the application knows. This is used to decrypt the information coming from Microsoft’s servers. Mobile developers may be tempted to put this in the application, but that is very risky. Instead, it should be stored in a server that the mobile application can access.

Microsoft Accounts does not federate with other single sign-on providers such as Windows Active Directory or Facebook Connect.

Watch the Build session [Powering your apps with Microsoft Accounts](http://channel9.msdn.com/Events/Build/2012/3-138) with Shelly Guo on Channel 9.
