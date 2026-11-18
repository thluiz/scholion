---
title: "Create a Video Party App With Rails Part 1: Building the Backend"
date: '2020-05-14T11:41:27+00:00'
category: webclip
summary: 'The article outlines the Rails backend for a video watch party app, including routes, a Session model, controller actions, shared site configuration, and ERB views wired to Vonage Video API credentials.'
tags: ["rails", "vonage-video-api", "backend", "ruby"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Create a Video Party App With Rails Part 1: Building the Backend"
    url: "https://dev.to/vonagedev/create-a-video-party-app-with-rails-part-1-building-the-backend-2p4k"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--create-a-video-party-app-with-rails-part-1-building-the-back.md"
    kind: repo
---

The post describes the backend for a Rails video watch party app built with the Vonage Video API. It sets up a landing page, a party video chat view, and a watch-party screenshare view, with password gating and moderator-only watch mode control.

## Reading notes

- The app uses Ruby on Rails 6+ and the Vonage Video API, with PostgreSQL and environment variables managed through dotenv-rails.
- A `Session` model stores the current video session ID and marks sessions as expired or active.
- The model can create a new Vonage session, load the last active session, and generate participant tokens.
- Moderator access is handled by generating a token with moderator role when the user name matches the configured moderator name.
- Routes map the landing page, party view, screenshare view, name submission, and chat submission to `VideoController` actions.
- The controller loads API credentials, the session ID, the moderator name, and the participant token before each action.
- The `name` action checks the submitted password against `PARTY_PASSWORD` and redirects to the party page only when it matches.
- A `site_info.yml` file centralizes language, layout text, navbar text, and chat labels used across the views.
- `ApplicationController` reads the YAML config and exposes it through instance variables for the views.
- The shared layout sets the HTML language and direction, loads the OpenTok JavaScript library, and passes Ruby variables into JavaScript.
- The header partial shows the app title, participant count placeholder, and the Watch Mode button.
- The chat partial includes a history container and a form that posts messages to `/chat/send`.
- The landing page asks for name and party password and displays flash errors for incorrect passwords.
- The party view passes token, name, and moderator name to JavaScript, then renders placeholders for publisher, subscribers, chat, and the chat toggle button.
- The screenshare view uses similar JavaScript setup and renders placeholders for screenshare video, audio, chat, and the chat toggle button.
- The article ends by noting that the backend is ready and the frontend will be built in Part 2.
