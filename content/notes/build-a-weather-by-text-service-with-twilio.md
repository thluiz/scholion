---
title: "Build A Weather by Text Service With Twilio"
date: '2016-03-04T07:39:34-03:00'
category: webclip
summary: 'The page shows how to connect Twilio and Stamplay so an SMS with a city name returns current weather or a 5-day forecast from OpenWeather through a Code Block and two Tasks.'
tags: ["twilio", "sms", "stamplay", "weather"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Build A Weather By SMS Service With Twilio and NodeJS"
    url: "https://blog.stamplay.com/build-a-weather-by-sms-service-with-twilio-and-nodejs/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-03/blog-stamplay-com--build-a-weather-by-text-service-with-twilio.md"
    kind: repo
---

The page explains how to build an SMS weather service with Twilio, Stamplay, and OpenWeather. A user texts a Twilio number with a city name, Stamplay catches the message, a Code Block fetches weather data and formats the reply, and a second Task sends the SMS back.

## Reading notes

- The service starts when a user sends an SMS with a city name to a Twilio number.
- A Stamplay Task captures the SMS through the Twilio integration and sends it to a custom Code Block.
- The Code Block requests weather data from OpenWeather, builds a readable message, and returns it.
- If the text includes the word forecast after the city name, the Code Block returns a 5-day forecast instead of current weather.
- The query uses the city name as q, an OpenWeather API key as APPID, and either imperial or metric units.
- Another Stamplay Task runs after the Code Block finishes and sends the response SMS using the body and to values from the Code Block output.
- To test the service, the page says to text the Twilio number from a verified number in Twilio.
