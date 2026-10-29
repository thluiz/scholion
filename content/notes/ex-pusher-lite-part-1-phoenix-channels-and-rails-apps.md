---
title: "Ex Pusher Lite - Part 1: Phoenix Channels and Rails apps"
date: '2016-01-08T08:39:45-03:00'
category: webclip
summary: 'The post shows a Rails chat built with Pusher, then starts replacing Pusher with a Phoenix server that receives POSTs from Rails and broadcasts them over WebSockets.'
tags: ["elixir", "phoenix", "rails", "pusher"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Ex Pusher Lite - Part 1: Phoenix Channels and Rails apps | AkitaOnRails.com"
    url: "http://www.akitaonrails.com/2015/12/09/ex-pusher-lite-part-1-phoenix-channels-and-rails-apps"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-01/akitaonrails-com--ex-pusher-lite-part-1-phoenix-channels-and-rails-apps.md"
    kind: repo
---

The post first sketches a simple Rails chat that posts form data to a controller, hands it to a background job, and sends the message to Pusher. The browser subscribes to a channel, receives the broadcast, and appends the new message to the page.

It then starts a Phoenix-based replacement that accepts HTTP POSTs from Rails, authenticates them with a Basic Auth header, and broadcasts messages to connected WebSocket clients. The second part changes the Rails app to use Phoenix.js, a Socket connection, Guardian token tags, and a POST to Phoenix instead of the Pusher gem.

## Reading notes

- Rails 5 introduces Action Cable, and Rails 4.2 can use Faye for WebSocket support.
- Pusher is presented as a low-friction messaging service for real-time features.
- The demo Rails app uses a form, an EventsController#create action, and a background job to trigger messages.
- The browser loads Pusher JavaScript, subscribes to a channel, and appends incoming messages to the page.
- The Phoenix side starts with a socket handler at /socket and a RoomChannel that can broadcast incoming payloads.
- The Phoenix server uses a POST /events endpoint and a Basic Auth authorization header.
- The Rails app replaces Pusher with Phoenix.js copied into the asset pipeline.
- Babel and Almond are added so Rails can load Phoenix’s ES6 client code.
- The Rails layout adds guardian_token_tags and body data-route attributes for the page loader.
- The Rails model posts to Phoenix with Net::HTTP.post_form, sending topic, event, and payload.
- The post ends by outlining future work on Guardian/JWT, private channels, channel listing APIs, and an admin dashboard.
