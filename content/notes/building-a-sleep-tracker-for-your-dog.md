---
title: "Building a Sleep Tracker for Your Dog"
date: '2014-09-19T18:46:43-03:00'
category: webclip
summary: 'The post shows how to use a Tessel microcontroller, Twilio SMS, and an accelerometer to detect when a dog has been still for more than five minutes and text the owner the sleep duration.'
tags: ["tessel", "twilio", "accelerometer", "dog-hacking"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building A Sleep Tracker For Your Dog"
    url: "https://www.twilio.com/blog/2014/09/building-a-sleep-tracker-for-your-dog-using-tessel-and-twilio.html?utm_source=javascriptweekly&utm_medium=email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-09/twilio-com--building-a-sleep-tracker-for-your-dog.md"
    kind: repo
---

The post walks through building a dog sleep tracker with Tessel and Twilio. It starts by sending an SMS from Tessel, then adds an accelerometer module to watch movement and decide when the dog has likely been sleeping.

The code compares the accelerometer’s x-axis movement over time, rounds small changes, and treats a gap of more than five minutes as sleep. When movement resumes after that interval, it sends a text message with how long the dog slept.

## Reading notes

- Use a Tessel microcontroller with built-in Wi-Fi and connect it to Twilio’s Node module to send SMS messages.
- Install the Twilio library locally and let it sync to the device when pushing code to Tessel.
- Wrap the SMS logic in a sendText() function that posts to the Messages resource and checks for errors.
- Add the accel-mma84 library to work with the accelerometer module on port A.
- Wait for the accelerometer to be ready, then stream acceleration data and log errors if they occur.
- Track last_movement and last_movement_time to measure how much time has passed between movement events.
- Set the accelerometer output rate to 1.56 Hz and the scale range to 8 Gs to fit the use case.
- Compare the current x-axis value with the last recorded value, trim small changes, and treat a pause of more than five minutes as sleep.
- Call sendText() when movement returns after that interval, reporting how long the dog slept.
- Push the finished app to Tessel flash memory so it runs automatically when the device powers up.
