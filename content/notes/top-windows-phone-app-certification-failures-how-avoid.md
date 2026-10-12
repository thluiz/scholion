---
title: "Top Windows Phone app certification failures and how to avoid them"
date: '2014-06-19T10:45:23-03:00'
category: webclip
summary: 'The post lists common Windows Phone Store certification failures and the checks that help avoid them, including screenshots, test credentials, crashes, icon assets, Back button behavior, localization, and theme support.'
tags: ["windows-phone", "app-certification", "submission-requirements", "mobile-development"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Top Windows Phone app certification failures and how to avoid them"
    url: "http://blogs.windows.com/windows_phone/b/wpdev/archive/2014/01/10/top-windows-phone-app-certification-failures-and-how-to-avoid-them.aspx"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-06/blogs-windows-com--top-windows-phone-app-certification-failures-how-avoid.md"
    kind: repo
---

The post explains that failing certification can delay release because the app must be corrected and resubmitted. It then groups the most common failures seen by the Windows Phone Store certification and policy teams and pairs each one with a practical check before submission.

## Reading notes

- Incorrect screenshots fail when they include emulator chrome, frame rate counters, debug information, altered images, or photos of the app instead of emulator screenshots.
- Apps that require login need a test account for certification, and the credentials should be included in Certification notes.
- Apps that crash during testing are rejected because unexpected termination counts as a certification failure.
- Default icons and tile images from templates or tools must be replaced with unique assets that match the app.
- Back button behavior is tightly defined: it closes the app on the main page, goes back on other pages, closes dialogs, and closes the soft keyboard.
- Games may pause on Back during play, and apps may show a quit confirmation only when Back is pressed on the main page.
- Each supported language needs a localized description, and the app must display correctly for every supported language.
- The app should work in both light and dark phone themes, and the developer can test theme changes in the emulator and Visual Studio.
