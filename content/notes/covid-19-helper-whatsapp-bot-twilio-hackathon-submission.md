---
title: "COVID-19 Helper Whatsapp Bot - A Twilio Hackathon Submission"
date: '2020-07-05T14:11:25+00:00'
category: webclip
summary: 'The post describes a WhatsApp bot built with Twilio Autopilot and Python that returns COVID-19 statistics and historical data by country, plus a self-screening flow that suggests when to seek medical attention.'
tags: ["whatsapp-bot", "twilio-autopilot", "covid-19", "fastapi"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "COVID-19 Helper Whatsapp Bot - A Twilio Hackathon Submission"
    url: "https://dev.to/alessandrojcm/covid-19-helper-whatsapp-bot-a-twilio-hackathon-submission-5fje"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--covid-19-helper-whatsapp-bot-twilio-hackathon-submission.md"
    kind: repo
---

The project is a WhatsApp bot built for the Twilio and DEV 2020 hackathon. It uses Twilio Autopilot and Python 3.8, with FastAPI, FaunaDB, Heroku, and external APIs to answer COVID-19 questions and run a symptom-based self-screening flow.

## Reading notes

- The bot returns statistical COVID-19 data by country, such as Spain or the USA.
- It also returns historical COVID-19 data by country, such as Ireland on March 15th.
- A self-screening flow asks about common symptoms and other variables, then advises whether the user should seek medical attention.
- The author says the self-checker is only informative and does not replace a health professional’s diagnosis.
- The stack includes Python 3.8.2, Poetry, FastAPI, Pydantic, Fauna DB, Heroku, Pytest, Loguru, Requests, Sentry, and Click.
- The project was started from cookiecutter-fastapi.
- The author wanted more features, such as more specific location queries, grocery store suggestions, and daily news, but some were left out because of time or technical limits.
- The author says FastAPI was a learning experience, especially because it was the first ASGI framework used.
- FaunaDB introduced a number of surprises compared with relational databases, including primary keys, array results, missing migrations, and repeated records.
- A parsing issue with application/x-www-form-urlencoded requests initially blocked Autopilot requests from reaching the API.
- The APIs used were Novelcovid API and Endless Medical API.
- The author concludes that the project taught several new concepts in a month and became the first post published on DEV.
