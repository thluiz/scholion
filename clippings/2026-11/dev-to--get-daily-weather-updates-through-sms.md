---
url: "https://dev.to/shimphillip/get-daily-weather-updates-through-sms-ohp"
captured_at: "2026-11-16T02:03:17+00:00"
title: "Get daily weather updates through SMS"
domain: "dev-to"
---

## [](#what-i-built)What I built

It's called _Weather Me_ ⚡. It's a text message service where a user can signup and receive weather summary updates daily based on the user's location. The text comes around 8 AM and contains forecast by 3-hour intervals until midnight.

Why did I build it? Check out the first post in the series!

[![Alt Text](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fal6cnsd7s0mhuqfyy47e.jpg)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fal6cnsd7s0mhuqfyy47e.jpg)

## [](#category-submission)Category Submission

Interesting Integrations

## [](#demo-link)Demo Link❔

Simply visit [https://weather-me-54a7d.web.app/](https://weather-me-54a7d.web.app/)

Signup then fill out the form with your zip code and phone number. It's that simple! 💪

**Disclaimer**  
Sending texts do cost money. I'm currently using free credits provided by Twilio through a promotion code. Since this is an experimental app I might delete your account at times without letting you know.

## [](#link-to-code)Link to Code 📝

Instructions and details on how to set up the project and what I would do to make the project better.

[https://github.com/shimphillip/weather-me](https://github.com/shimphillip/weather-me)

## [](#gotchas-and-limitations)Gotchas and limitations 👻

The 3-hour forecasts don't give information about the current time the API call is made. Therefore, when you receive the text in the morning around 8 AM, it will likely give start from 9 AM or 10 AM.

Notice the demo is only available in U.S. The scheduled to receive texts are in Central Time.

Be patient! These firebase lambdas functions unfortunately take a long time to wake up from hibernation if they haven't been used for a long time. I am talking 5-10 seconds and maybe up to 20 seconds 💩. I haven't implemented spinners or alerts to notify the loading state yet. So I would at least wait 10 seconds when making CRUD operations.

## [](#techstack)Techstack 📚

*   Vanilla JS
*   A snippet of Vuejs
*   Twilio SMS API
*   OpenWeather API
*   Serverless functions from firebase
*   Firestore - Realtime cloud database
*   Bootstrap framework - sketchy theme

## [](#the-journey)The Journey 🚩

I started out on Wednesday, April 8th, 2020 and finished today on Tuesday, April 14th, 2020. So it took about 6 days to complete dedicating about 1-2 hours each day. My initial plan had way more features but as it always is, you make some compromise along the way for a side project like this 😂. But I give myself a lot of credit for actually finishing the project 🔥.

I took this project as a learning opportunity to get my hands dirty on some new tech stacks I've never played around with. Thus I stumbled into lots of roadblocks and took some grueling hours and efforts to get unblocked. Here are a few things I learned on this journey.

## [](#the-lessons)The lessons 📒

*   Twilio is legit. I can tell that it's a very software-engineer oriented company with smart individuals. The API documentation is almost flawless and is pleasant to explore. Their blogs are also top-notch with interesting topics and innovative practices to up your dev knowledge. Plus they provide really cool APIs and services and there are lots of them!
    
*   Vanilla JS is fun yet could be difficult to organize. I am so used to using JS frameworks such as React and Express that utilize commonJS and import/export modules to easily scaffold your project. Throwing script tags in the `index.html` and searching files through your project directory could be confusing at times. Maybe I should've gone with Parcel📫 or something similar to provide me some basic template and skeleton.
    
*   VueJS gave me flashback when I used to use Angular JS 1.x version. I love the idea of data binding and encapsulating the logic from the model to a view directly. But I disliked learning directives again and whatnot that is framework-specific and not language agnostic.
    
*   OpenWeather API is cool! I initially thought about going with DarkSky API but realized that to grab weather info, I need to pass in geolocation with coordinates. Well, I could've asked users to provide that for me😧 or use Google's reverse geo lookup API. But didn't want to do neither so just went with OpenWeather API. The free plan doesn't provide too many options but it served fine for my app.
    
*   Bootstrap 4 is great. The earlier versions of the Bootstrap CSS framework had some limitations. I remember it was very difficult to add custom styles to my app that's already wrapped around with Bootstrap. However, the current version is niftier, it gives developers more fine-grained control with utility classes, better responsiveness, etc...
    
*   Serverless ☁. I have mixed feelings about this. Having no backend server that I need to manage is awesome but that also means I am giving up a lot on the flexibility on what I can do on the server-side. With that said, firebase is nice that it gives you tools to kick off things with convenience. There are functions you can kick off using HTTP requests and there are also background trigger functions that listen for events that come in handy often. The biggest complaint I have is the firebase cloud functions have insanely high latencies. I understand that if the lambdas haven't been used in a while, they go to sleep. AWS Lambda functions at most probably take less than a second to get up and act but it feels like Google cloud functions that more than 3 seconds most of the time and sometimes up to 10 seconds to serve the incoming request💀. But I still liked that firebase provides one place to control auth, DB, functions, hosting, etc...
    

## [](#in-closing)In closing... 👋

There is so much you can do within a given deadline time, working solo and a fulltime job with a family. One needs to make plans, strategize, learn how to make tradeoffs and persevere.

Finally, what a fun experience. Gratitude and respect towards for Twilio and Dev.to to collaborate and come up with such a fun hackathon during this perilous time and the lockdown. 안뇽👍.
