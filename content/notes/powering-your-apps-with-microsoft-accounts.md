---
title: "Powering Your Apps with Microsoft Accounts"
date: '2012-11-01T12:34:59-03:00'
category: webclip
summary: 'Windows 8 uses Microsoft Account as a single sign-on system for Microsoft and third-party services. The text explains tokens, SDK access, and the risks of storing the app secret on the client.'
tags: ["microsoft-account", "windows-8", "oauth", "single-sign-on"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Powering Your Apps with Microsoft Accounts"
    url: "http://www.infoq.com/news/2012/11/Microsoft-Accounts"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-11/infoq-com--powering-your-apps-with-microsoft-accounts.md"
    kind: repo
---

Windows 8 centers on Microsoft Account as another attempt at single sign-on for Microsoft and third-party services. The text says the goal is to avoid forcing users to create yet another username and password, and it notes that Microsoft has tried similar ideas before under several product names.

For Windows 8 apps, the sign-in flow can return an authentication token and an access token. The authentication token verifies the account, while the access token allows retrieval of user information. Websites that implement the Microsoft Account SDK can also sign the user in automatically. The text adds that even sites with their own login system may receive a user id that can later help personalize the site when the user signs up.

## Reading notes

- Windows 8 uses Microsoft Account as a single sign-on system for Microsoft and third-party services.
- Microsoft has tried similar sign-on products before, including Microsoft Wallet, Microsoft Passport, .NET Passport, Microsoft Passport Network, and Windows Live ID.
- A Windows 8 app may request an authentication token and an access token when it starts.
- The authentication token verifies the user’s account, and the access token allows retrieval of information about the user.
- Websites that implement the Microsoft Account SDK can automatically sign the user in.
- Sites with their own authentication system may still receive a user id, which can later help personalize the site when the user officially signs up.
- The Live SDK can access SkyDrive, profile, and social network data.
- Access uses OAuth 2.0 or the Live Connect REST API.
- Client-side SDKs are available for Windows 8, Windows Phone, Android, iOS, and .NET.
- Users must give explicit permission for applications to access their Microsoft data.
- The application secret should not be stored in the mobile app itself; it should be kept on a server the app can reach.
- Microsoft Accounts does not federate with Windows Active Directory or Facebook Connect.
