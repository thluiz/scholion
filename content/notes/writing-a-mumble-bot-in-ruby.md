---
title: "Writing a Mumble Bot in Ruby"
date: '2015-08-03T16:40:40-03:00'
category: webclip
summary: 'Explains how to use the mumble-ruby gem to connect to Mumble, join channels, send and receive messages, mute or deafen audio, and keep a bot running.'
tags: ["ruby", "mumble", "chat-bot", "voice-communication"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Writing a Mumble Bot in Ruby"
    url: "http://devdungeon.com/content/writing-mumble-bot-ruby"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-08/devdungeon-com--writing-a-mumble-bot-in-ruby.md"
    kind: repo
---

The page shows how to build a Mumble client in Ruby with the mumble-ruby gem. It covers installing prerequisites, connecting to a server, joining a channel, listing users and channels, sending chat messages, and receiving incoming text messages.

It also includes examples for muting, deafening, playing WAV files, recording audio, and streaming raw PCM data. At the end, it presents a full command-line chat client that connects to the DevDungeon Mumble server and stays online in a loop.

## Reading notes

- Mumble is described as an open-source voice communication tool with low latency for gaming.
- The ruby gem mumble-ruby provides a library to connect and interact with Mumble as a client.
- The examples demonstrate chat-room and private-message communication.
- The page notes that the project requires Ruby 2.1.0 or greater and the OPUS codec.
- Installation examples include libopus packages on Debian-based systems and gem installation.
- The client connection example sets a host, username, password, connects, waits, and disconnects.
- Global configuration can be set before creating clients so new clients inherit the defaults.
- Channel joining can use either the room name or the channel ID.
- The examples show how to list all channels and all users.
- Message-sending examples cover text and image messages to users and channels.
- The text-message callback must be set before client.connect so it can handle chat and private messages.
- The client can be muted or deafened, including turning those states off again.
- WAV playback depends on matching the file sample rate to the client configuration.
- Audio recording and raw PCM streaming are shown as experimental features.
- A loop is needed to keep the bot alive, and the page mentions using CTRL-C to stop it or daemonizing it with the Ruby Deamons gem.
- The final script connects to devdungeon.com, lists channels and users, joins a channel, prints incoming messages, and sends typed messages from the console.
