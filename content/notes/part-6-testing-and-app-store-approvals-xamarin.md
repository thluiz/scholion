---
title: "Part 6 - Testing and App Store Approvals | xamarin"
date: '2013-08-05T13:52:18-03:00'
category: webclip
summary: 'The page says testing should cover multiple platforms, devices, edge cases, and beta feedback, because store approval processes often reject apps for crashes, slow startup, bad metadata, or guideline violations.'
tags: ["testing", "app-store-approval", "beta-testing", "mobile-development"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Part 6 - Testing and App Store Approvals | xamarin"
    url: "http://docs.xamarin.com/guides/cross-platform/application_fundamentals/building_cross_platform_applications/part_6_-_testing_and_app_store_approvals"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-08/docs-xamarin-com--part-6-testing-and-app-store-approvals-xamarin.md"
    kind: repo
---

Testing is presented as a critical step because many apps must pass an approval process before publication. The page recommends testing across platforms, operating system versions, simulators, emulators, and physical devices, and it also points to cloud device services, beta management tools, automation, and unit testing frameworks.

## Reading notes

- Many apps must pass an approval process before publication, so testing is needed to help the app reach the market.
- Testing can include unit tests, beta testing, and testing across a wide range of hardware.
- Code should be tested on multiple platforms during development or refactored later for platform differences and iOS limitations.
- Simulators and emulators should be used for different OS versions and device configurations.
- Physical devices should also be used, since cloud services can help when too many devices exist to test directly.
- Beta testing brings two main challenges: distribution and feedback.
- Test automation on iOS can record and replay user interface tests with Test Studio and Xamarin.iOS references.
- Xamarin.iOS includes Touch.Unit, and Andr.Unit is the Android equivalent.
- Apple and Microsoft use strict review processes, while Android stores vary from no review to approval-based distribution.
- Rejection can delay launches, miss marketing windows, and create long waits with limited feedback.
- App launches should be planned in advance, including time for account creation, approval, and possible resubmission.
- Apps are often rejected for quality issues, especially crashes, so they should be tested for network problems and memory or storage limits.
- Apps should start quickly, stay responsive, and show user feedback when background work is happening.
- Edge cases should be tested, including denied permissions, location and locale differences, slow or absent network access, and older hardware.
- Apple and Microsoft also review apps against design guidelines and platform conventions, including icons, back-button behavior, and consistent use of UI metaphors.
- iOS rules are stricter for features such as in-app purchases, iCloud backup, Newsstand, and map credits.
- Metadata can cause rejection too, including imagery, trademarks, the use of the word beta, references to other platforms, and claims that do not match the app.
- Some apps are meant for closed distribution instead of app stores, and support for this varies by platform.
- The section ends by saying success depends on planning, guideline compliance, thorough testing, and accurate metadata.
