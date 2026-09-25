---
title: "We replaced passwords with something worse"
date: '2025-08-08T00:28:58+01:00'
category: webclip
summary: 'The post argues that email-or-phone login codes weaken account security because users cannot tell whether a code prompt is legitimate, and password managers do not help against this phishing pattern.'
tags: ["account-security", "phishing", "login-codes"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "We replaced passwords with something worse | Blog - Daniel Huang"
    url: "https://blog.danielh.cc/blog/passwords"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-08/blog-danielh-cc--we-replaced-passwords-with-something-worse.md"
    kind: repo
---

The post argues that the common login flow based on an email address or phone number plus a 6-digit code is a bad replacement for passwords. It says this setup makes account security worse because users cannot tell whether the code is being requested by the real service or by an attacker.

It also says password managers do not help against this kind of phishing. The author points to Microsoft’s Minecraft account login as an example of the method being used in the wild, and says many accounts have already been stolen.

## Reading notes

- Many services now use a login flow where the user enters an email address or phone number, receives a 6-digit code, and uses that code to log in.
- The author says this should stop because it is terrible for account security.
- An attacker can send the victim’s email address to a legitimate service and trigger a 6-digit code prompt.
- The user cannot know for sure whether the code belongs in the right place.
- Password managers, which usually help against phishing, do not help here.
- Microsoft’s Minecraft account login uses this method.
- The post says many accounts have already been stolen through this attack method.
