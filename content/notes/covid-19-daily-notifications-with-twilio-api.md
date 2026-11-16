---
title: "COVID-19 Daily Notifications with Twilio API"
date: '2026-11-16T01:20:35+00:00'
category: webclip
summary: 'The project lets users submit a state in an online form, stores the data in Google Sheets, and sends daily COVID-19 status updates through Twilio text messages.'
tags: ["covid-19-communications", "twilio", "wayscript", "google-sheets"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "COVID-19 Daily Notifications with Twilio API - Twiliohackathon finish"
    url: "https://dev.to/derricksherrill/covid-19-daily-notifications-with-twilio-api-twiliohackathon-finish-cme"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--covid-19-daily-notifications-with-twilio-api.md"
    kind: repo
---

The project aims to give users a convenient way to receive daily notifications about their state's COVID-19 status. A user fills out an online form, selects a state, and the app pulls data from a COVID tracking API and sends it back daily through a Twilio text message.

## Reading notes

- The hosted form sends submitted data into Google Sheets through an API.
- The form was built with WayScript, and the script is available on WayScript.
- The Python code used in the script is available in a GitHub repository.
- The stack uses WayScript on AWS, Google Sheets API, a daily CRON trigger, Python requests, and the Twilio API.
- The CRON job reads the saved Google Sheets values, requests data from the COVID tracking API, filters the data by user, and sends it back by text message.
- A demo video on YouTube shows how to build the project with WayScript.
