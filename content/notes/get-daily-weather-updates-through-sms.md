---
title: "Get daily weather updates through SMS"
date: '2020-04-20T21:22:21+00:00'
category: webclip
summary: 'The project, called Weather Me, sends daily SMS weather summaries based on a user''s location, with forecasts in 3-hour intervals and a demo, code link, and noted limits.'
tags: ["sms", "weather", "twilio", "firebase"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Get daily weather updates through SMS"
    url: "https://dev.to/shimphillip/get-daily-weather-updates-through-sms-ohp"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--get-daily-weather-updates-through-sms.md"
    kind: repo
---

Weather Me is a text message service that lets a user sign up and receive daily weather summary updates based on location. The message arrives around 8 AM and includes forecast information in 3-hour intervals until midnight. The post also gives a demo link, code link, and notes a few limitations of the app.

## Reading notes

- Weather Me is a text message service where a user can sign up and receive weather summary updates daily based on the user's location.
- The text comes around 8 AM and contains forecast by 3-hour intervals until midnight.
- Users can visit the demo, sign up, and fill out the form with a zip code and phone number.
- Sending texts costs money, so the author is using free Twilio credits from a promotion code.
- The demo is only available in the U.S., and scheduled texts use Central Time.
- Firebase lambda functions can take 5 to 20 seconds to wake up if they have not been used for a long time.
- The stack includes Vanilla JS, a snippet of Vuejs, Twilio SMS API, OpenWeather API, Firebase serverless functions, Firestore, and Bootstrap sketchy theme.
- The project took about 6 days, with 1 to 2 hours of work each day.
- The author says Twilio's documentation is almost flawless and pleasant to explore.
- The author says Vanilla JS can be harder to organize than frameworks with modules.
- The author says VueJS recalled Angular JS 1.x and made data binding appealing, but framework-specific directives were less appealing.
- The author chose OpenWeather API over DarkSky API because he did not want to rely on geolocation or reverse geo lookup.
- The author says Bootstrap 4 offers better control and responsiveness than earlier versions.
- The author has mixed feelings about serverless, since it removes server management but reduces backend flexibility and can add latency.
