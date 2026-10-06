---
title: "Number Verification And Two Factor Authentication in Android/Ruby on Rails"
date: '2015-04-05T19:59:58-03:00'
category: webclip
summary: 'Tutorial that shows how to build a two factor system in Ruby on Rails with Sinch SMS, including code generation, verification, Postman testing, and hosting on Heroku for later Android use.'
tags: ["two-factor-authentication", "ruby-on-rails", "sms", "sinch"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Two Factor Authentication in Android/Ruby on Rails - Pt. 1 | Sinch"
    url: "https://www.sinch.com/tutorials/two-factor-authentication-rails/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-04/sinch-com--number-verification-and-two-factor-authentication-in-android.md"
    kind: repo
---

This tutorial explains how to build a two factor system in about 30 minutes using Ruby on Rails and Sinch SMS. It creates a backend that generates OTP codes, stores them with a phone number, sends them by SMS, and checks them during verification. The article also points to later parts where the same system is used in an Android app and in the Rails login flow.

## Reading notes

- The tutorial assumes good Ruby on Rails and REST API knowledge, plus a Sinch account.
- It sets up a new Rails project, a Verifications controller, routes for generating and verifying codes, and a database table for phone numbers and OTP codes.
- The model keeps a phone number and validates that it is present.
- The app adds the sinch_sms gem to send SMS messages with OTP codes.
- generate_code creates a random code, stores a verification entry, and sends an SMS with the code.
- verify_code looks up a verification entry by phone number and code, destroys it when found, and returns verified true or false.
- The article says production apps would likely verify the phone number format before sending and wait for Sinch to confirm delivery to the operator.
- It suggests testing the REST API with Postman and running the Rails server locally.
- For the next part of the tutorial, the backend should be hosted somewhere, and Heroku is the platform chosen in the article.
