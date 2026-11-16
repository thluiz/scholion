---
title: "Sending an SMS with Phoenix"
date: '2020-04-19T12:03:25+00:00'
category: webclip
summary: 'The walkthrough shows how to create a Phoenix app, add a Nexmo SMS form, wire routes and controller actions, install HTTPoison, and configure API credentials and a virtual number.'
tags: ["phoenix", "elixir", "sms", "nexmo"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Sending an SMS with Phoenix"
    url: "https://dev.to/vonagedev/sending-an-sms-with-phoenix-20od"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--sending-an-sms-with-phoenix.md"
    kind: repo
---

The walkthrough starts with a new Phoenix app and shows how to install dependencies, create the database, and run the server. It then adds a Nexmo account, API credentials, and a virtual number so the app can send SMS messages.

It also defines the routes, controller actions, templates, and environment variables needed for the app to submit a text message and show a success page.

## Reading notes

- Phoenix is presented as the main web framework in the Elixir ecosystem, with an intuitive setup and low barrier to entry.
- The app is created with `mix phx.new sms_app`, then the database is created with `mix ecto.create` and the server is started with `mix phx.server`.
- A Nexmo account is created for free, and the user fetches API credentials from the dashboard.
- For sending SMS in the US, the tutorial says a Nexmo virtual number must be purchased and used as the originating phone number.
- The router gets three routes: `GET /sms`, `POST /send`, and `GET /update`.
- `index/2` renders the form and supplies a CSRF token.
- `send/2` uses HTTPoison to post to the Nexmo SMS API with the API key, API secret, sender number, message text, and recipient number.
- If the message succeeds, the controller redirects to `update/2`; otherwise it shows an error.
- The tutorial adds `httpoison` as a dependency in `mix.exs` and installs it with `mix deps.get`.
- The view module and two templates are created for the SMS form and the success page.
- The form posts the recipient number and message, and includes the CSRF token as a hidden field.
- The app reads `NEXMO_API_KEY`, `NEXMO_API_SECRET`, and `NEXMO_NUMBER` from a `.env` file, which should be kept out of GitHub.
