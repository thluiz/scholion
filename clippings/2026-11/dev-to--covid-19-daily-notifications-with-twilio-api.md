---
url: "https://dev.to/derricksherrill/covid-19-daily-notifications-with-twilio-api-twiliohackathon-finish-cme"
captured_at: "2026-11-16T01:20:35+00:00"
title: "COVID-19 Daily Notifications with Twilio API - Twiliohackathon finish"
domain: "dev-to"
---

[![Derrick Sherrill](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F185410%2Fb7540d7f-8da5-4650-b080-7152160d6b1e.png)](https://dev.to/derricksherrill)

## [](#covid19-notification-project)COVID-19 Notification Project

The aim of the project was to give users a convenient way to receive daily notifications about their state's status in regards to COVID-19.  
The idea was a user could fill out an online form, select their state, and the app would automatically pull from a covid tracking API and send state based data back daily through a twilio powered text message.

#### [](#category-submission)Category Submission:

COVID-19 Communications

## [](#the-hosted-form)The Hosted Form

The [form](https://18547.wayscript.io/) takes some data and inputs it into a google sheet using their API.

I built this using [WayScript](https://www.wayscript.com/) and the script can be found [here](https://wayscript.com/user/derricks/6FKUD7gg).

## [](#links-to-code)Links to Code

The Python code used throughout the script can be found in this [GitHub Repo](https://github.com/wayscript/code_snippets/tree/master/Trigger%20Notifications%20%26%20Alerts/Twilio%20Covid%20Informer).

## [](#whats-the-stack)What's The Stack?

I used WayScript to build this. The form is therefore hosted on an AWS server which connects to the google sheets API to be written.

From there, a daily CRON trigger activates which reads in these google sheet values using their API again. The API request to the covid tracking API was done using python and the requests library.

Data was filtered conditionally to the user and then passed back to them using the twilio API.

## [](#additional-resourcesinfo)Additional Resources/Info

We made a demo on how to build this with WayScript over on [YouTube](https://youtu.be/2Da892bYLMk).

Thanks for any and all feedback! It was a fun project to build and a great opportunity to showcase Twilio.
