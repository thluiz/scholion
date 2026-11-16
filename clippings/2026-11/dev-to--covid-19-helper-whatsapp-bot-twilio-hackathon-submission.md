---
url: "https://dev.to/alessandrojcm/covid-19-helper-whatsapp-bot-a-twilio-hackathon-submission-5fje"
captured_at: "2026-11-16T01:19:04+00:00"
title: "COVID-19 Helper Whatsapp Bot - A Twilio Hackathon Submission"
domain: "dev-to"
---

## [](#what-i-built)What I built

### [](#category-interesting-integrations)Category: Interesting Integrations

I set up to build a Whatsapp Bot using Twilio Autopilot which would help the user with several tasks in his daily quarantined life; several ones stayed just as ideas (hows that for feature-creep huh?) and my bot got the following function:

*   Statistical data of the COVID19 pandemic by country:
    *   "How are they doing in Spain?"
    *   "I'd like information on the USA"
*   Historical data of the COVID19 pandemic by country:
    *   "How was Ireland doing on march 15th"
*   A self-screening process (with a little help from AI):
    *   Here, the bot will ask the users if they are feeling the most common symptoms of COVID-19
    *   Then, along with other variables (do they live in a country with confirmed cases? have they had contact with someone that looks ill?), would advise the users if they should seek medical attention
    *   Of course, this self checker is merely informative, by no means replaces the diagnosis of a health professional

## [](#but-first-show-me-dah-gifs)But first, **show me dah** GIFS!

[![greeting](https://res.cloudinary.com/practicaldev/image/fetch/s--TWvD9NE9--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/fc9qjztqbop63bj5fkej.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s--TWvD9NE9--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/fc9qjztqbop63bj5fkej.gif)  
[![latest data query](https://res.cloudinary.com/practicaldev/image/fetch/s--__0H80vL--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/oq6bc5be0vuzx1hy081x.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s--__0H80vL--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/oq6bc5be0vuzx1hy081x.gif)  
[![historical query](https://res.cloudinary.com/practicaldev/image/fetch/s--mPoIqVdY--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/m11w23xz5asr8yitz4hs.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s--mPoIqVdY--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/m11w23xz5asr8yitz4hs.gif)  
[![screening query](https://res.cloudinary.com/practicaldev/image/fetch/s--uVybfgKh--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/v68nidwtka2jjoi8pet4.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s--uVybfgKh--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/v68nidwtka2jjoi8pet4.gif)

## [](#link-to-code)Link to Code

You can join the sandbox by sending a Whatsapp message to: `+1 (415) 523-8886`, first text `join using-similar` and then say hi!

## COVID19 Helper Bot

[![buddy pipeline](https://camo.githubusercontent.com/08de0b90b7b1c723f583edfb263e34f504c2c5e485f1b8674e73106a4c4e6951/68747470733a2f2f6170702e62756464792e776f726b732f616c657373616e64726f6a637570706172692f7477696c696f2d6465762d6861636b6174686f6e2f706970656c696e65732f706970656c696e652f3234393539392f62616467652e7376673f746f6b656e3d61396531663463373666363038616333316162333463336235323838626634333761643338656530323963386236306232303430366566626530343834333335 "buddy pipeline")](https://app.buddy.works/alessandrojcuppari/twilio-dev-hackathon/pipelines/pipeline/249599) [![DeepSource](https://camo.githubusercontent.com/434e93b877c79c590cdefc44446594600a959d9f425b2e9ead69648052c7523b/68747470733a2f2f7374617469632e64656570736f757263652e696f2f64656570736f757263652d62616467652d6461726b2d6d696e692e737667)](https://deepsource.io/gh/alessandrojcm/twilio-dev-hackathon/?ref=repository-badge) [![buddy pipeline](https://camo.githubusercontent.com/08de0b90b7b1c723f583edfb263e34f504c2c5e485f1b8674e73106a4c4e6951/68747470733a2f2f6170702e62756464792e776f726b732f616c657373616e64726f6a637570706172692f7477696c696f2d6465762d6861636b6174686f6e2f706970656c696e65732f706970656c696e652f3234393539392f62616467652e7376673f746f6b656e3d61396531663463373666363038616333316162333463336235323838626634333761643338656530323963386236306232303430366566626530343834333335 "buddy pipeline")](https://app.buddy.works/alessandrojcuppari/twilio-dev-hackathon/pipelines/pipeline/249599)

A Whatsapp Bot to help get information about COVID19, aiming to participate on the [Twilio & Dev 2020 Hackathon](https://dev.to/devteam/announcing-the-twilio-hackathon-on-dev-2lh8).

Using Twilio Autopilot and Python 3.8

## Stack

*   Python3.8.2
*   Poetry
*   Fastapi
    *   Pydantic
*   Fauna DB
*   Hosted on Heroku
*   Pytest
*   Loguru
*   Requests
*   Sentry
*   Click

Kickstarted with: [https://github.com/Dectinc/cookiecutter-fastapi](https://github.com/Dectinc/cookiecutter-fastapi)

## Project structure

Files related to application are in the `app` or `tests` directories Application parts are:

```

├── app
│   ├── api - Api routes
│   │   └── routes
│   │       └── autopilot - Twilio Autopilot Dynamic actions
│   ├── core - Critical configuration (sessions, logging, etc)
│   ├── custom_routers - FastAPI custom routes
│   ├── error_handlers - Custom error handlers
│   ├── middlewares - FastAPI/Starlette middleware configuration
│   ├── models - Pydatic models
│   ├── scripts - Helper scripts (mainly cli stuff)
│   ├── services - Utilites for interaction with external apis and logic too heavy for the routes
│   └── utils
```

…

## [](#the-project)The project

### [](#the-one-million-dollar-ideas)The one million dollar ideas

So first of all, when I saw the hackathon announcement I knew I had to participate. Right away I also knew that I wanted to make a Whastapp Bot and I wanted to do it with Python. But alas, what should the bot do? I'd started brainstorming ideas like crazy, here are some of then:

*   Query a specific statistic (ie: how many recoveries in Spain)
*   Query by more specific location (ie: how many cases in San Francisco)
*   Take the user's location and show open grocery stores near then
*   Send the user the latest news for their country daily
*   And there are a couple more left out

So, pretty feature creep huh? Some of those features were left out because of lack of time and others for technical reasons (for example, the Whatsapp API does not let you take the user's location; at least not yet). But I knew that I had to implement the self-screening process.

### [](#the-stack-oh-the-stack)The stack, oh the stack

well, I knew more or less what I wanted to do, now with the stack. I wanted to it in Python and I wanted to do it with [Fastapi](https://fastapi.tiangolo.com/), since Twilio has a helper library for Python that was a no brainer.

Now, the fun part was my database of choice: [FaunaDB](https://faunadb.com/). Why did I choose it? Well, first of all, it has a generous free tier, and second, they advertise heavily for being a solution for the JAM stack; so I was curious to see how it fitted with a more traditional use case (spoiler: it can, but with some gotchas).

So I set sail with my shiny stack, and boy it was a ride. First, because it was my first time with an ASGI framework; and thus I had to wrap my head around Python coroutines and async routes. Things that you would normally do in WSGI frameworks are different here (middlewares, for example); but, overall, I had a blast working with Fastapi: I learn a lot in the process and was nice to work with a framework designed for the modern Python.

But Fauna, well that was another beast. I come mainly from a traditional relational database background, so jumping to NoSQL was a challenge of its own; there were a lot of gotchas in the process: where are my primary keys? If this value is unique why does my query return an array? Where are my migrations? How can this record be repeated if all its fields are the same? And all kinds of surprises.

### [](#last-but-not-least-the-bot)Last but not least, the bot

At this point, I was sure developing the bot would be the bigger challenge. At first, it seemed like so: I couldn't get the Autopilot requests to hit my API; it turned out it was a case of me skipping a little of pretty important documentation (specifically how to parse `application/x-www-form-urlencoded` requests with FastAPI). But, once I had that sorted out, the bot itself turned out to be a breeze to develop.

## [](#additional-resourcesinfo)Additional Resources/Info

The APIS I used are:

*   [Novelcovid API](https://corona.lmao.ninja/), an API that aggregates data from several sources. I choose the one from the John Hopkins Universite
*   [Endless Medical API](https://www.endlessmedical.com/), AI-powered trained with real records and diagnosis that suggests outcomes based on a patient's symptoms. Thanks to Lukasz Kiljanek for kindly answering my inquiries!

## [](#conclusion)Conclusion

Overall, this was a great project and not only got me to learn several things in the process; at first, I was a little disappointed that I couldn't squeeze more features in, but seeing all the new concepts I managed to grasp in only a month made it a worthy ride.

It also got my first post on DEV published! So that alone was worth it (I may be following up with more in-depth articles about the code 😉). So that's all, happy coding and keep safe!
