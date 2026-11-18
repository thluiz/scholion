---
title: "DIY FAQ Bot"
date: '2019-07-04T10:05:03+00:00'
category: webclip
summary: 'The post shows how to build a simple FAQ chatbot with Azure Bot Service, QnA Maker, and Twilio to handle common messages, test it, publish it, and connect it to SMS.'
tags: ["azure-bot-service", "qna-maker", "twilio", "chatbot"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "DIY FAQ Bot"
    url: "https://dev.to/twilio/diy-faq-bot-o61"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--diy-faq-bot.md"
    kind: repo
---

The post walks through a basic chatbot setup using Azure Bot Service, QnA Maker, and Twilio. It frames the bot as a way to handle noisy inbound messages by answering common questions from a FAQ-style knowledge base.

## Reading notes

- The post describes a simple chatbot built with minimal programming.
- It says the bot was meant to help manage DMs and common inbound messages.
- The author groups messages into categories such as Azure questions, career advice, speaking inquiries, close-friend conversations, creepy greetings, and miscellaneous opportunities.
- It says QnA Maker can create a bot from a simple FAQ list.
- It instructs the reader to create a knowledge base in the QnA Portal.
- It says the knowledge base is a collection of searchable questions and answers hosted in Azure.
- It notes that service details include name, subscription, location, pricing tier, resource group, and optional App Insights.
- It says the knowledge base is populated by uploading a Word document of FAQs.
- It says the bot personality can be set with a chit-chat option such as friendly.
- It says the bot can be tested before publishing.
- It says publishing turns the knowledge base into an endpoint.
- It says an Azure Web App Bot is created with SDK v3, C#, and the Question and Answer template.
- It says the bot is connected to the published QnA service through application settings.
- It says Twilio is used as the channel for SMS messaging.
- It says the Twilio setup needs a phone number, Account SID, and Auth Token.
- It says a TwiML app is created with the messaging request URL https://sms.botframework.com/api/sms.
- It says the Twilio credentials are added in Azure Channels.
- It says the result is a basic QnA bot that can answer common questions over text.
