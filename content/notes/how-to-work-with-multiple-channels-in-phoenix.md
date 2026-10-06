---
title: "How to work with multiple Channels in Phoenix?"
date: '2015-05-25T08:56:39-03:00'
category: webclip
summary: 'The thread asks whether user info can be shared across Phoenix topics through the socket struct. Chris McCord says the client must join each topic, while socket params and channel params can carry shared data.'
tags: ["phoenix", "channels", "pubsub", "socket-params"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "[elixir-talk:8579] How to work with multiple Channels in Phoenix? - th.luiz@gmail.com - Gmail"
    url: "https://mail.google.com/mail/u/0/?pli=1#label/Listas%2F05+-+Principais/14d7eb385171ca3a"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/mail-google-com--how-to-work-with-multiple-channels-in-phoenix.md"
    kind: repo
---

The discussion is about a Phoenix app where a user needs to receive and send messages on three topics: chat, news, and stock exchange. Ivan asks whether the user info can be shared between topics through the socket struct or whether the user must join all three topics separately.

Chris McCord answers that the client needs to join the three topics. He says broadcasts can go to any topic, but the client only receives events from topics it has joined. He also explains that socket params and channel params can be used together so shared data like a user token is available in each join, and he notes that later Phoenix versions add helper functions for generating and verifying channel tokens and data.

## Reading notes

- The user wants one connection to handle chat, news, and stock exchange topics.
- The question is whether user data can be shared through the socket struct across those topics.
- Chris says the client must join every topic it wants to receive events from.
- Broadcasts can target any topic with `broadcast topic, event, payload`.
- Socket params and channel params are merged in each `join/3`.
- The example uses a user token in socket params and extra channel data in channel params.
- Chris says future Phoenix versions will add helper functions to generate and verify channel tokens and data.
- The thread also points Ivan to the Phoenix mailing list for the question.
