---
title: "Apache Cordova: after 10 months, I won't be using it anymore"
date: '2015-07-06T19:04:35-03:00'
category: webclip
summary: 'The author says Apache Cordova has advantages, but argues it is often too slow, harder to match native behavior, and dependent on plugins that vary by platform and maintenance quality.'
tags: ["apache-cordova", "cross-platform", "mobile-development"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Apache Cordova: after 10 months, I won't be using it anymore"
    url: "http://geekcoder.org/apache-cordova-after-10-months-i-wont-using-it-anymore/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-07/geekcoder-org--apache-cordova-after-10-months-i-wont-be-using-it-anymore.md"
    kind: repo
---

The author says Apache Cordova is a good project with many strengths, but not a fit for every use case. After 10 months using it on mindup.io, he says he will not use it for future projects because of performance limits, the effort needed to reproduce native behavior, and the burden of plugin maintenance.

## Reading notes

- Cordova can feel slow because everything runs in one WebView thread, which makes UI updates, scrolling, database access, and data serialization less smooth.
- Accessing the file system also adds overhead because data must be serialized between the native layer and the JavaScript WebView layer.
- Recreating native UI behavior in HTML5 and CSS3 can take days, and support must then be checked across Android and iOS versions.
- Cordova has many plugins for native features such as GPS, push notifications, and sensors, but each OS needs special handling.
- Some plugins depend on extra work or extra plugins on specific platforms, and support can vary by OS version.
- The author says mobile OSes evolve quickly, while Cordova plugins are often not maintained fast enough to keep up.
- He also says many plugins lack tests, may have bugs, or may not support features such as background jobs for push notifications.
- He argues that a cross-platform app is not always the best starting point and that early projects should focus on validating the concept quickly.
- He says time is the most limited resource at the beginning of a project, and that a native approach can sometimes achieve in one month what Cordova would take six months to do.
- He adds an edit noting that newer devices and newer webviews can change the performance picture, especially on iOS and Android 5.0+.
