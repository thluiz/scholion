---
title: "Slack on Rails"
date: '2015-04-27T12:00:38-03:00'
category: webclip
summary: 'The post shows how Slack can act as an interface to internal services and explains two ways to build a simple command-and-response integration in a Rails app: Outgoing WebHooks and Slash Commands.'
tags: ["slack", "ruby-on-rails", "webhooks", "slash-commands"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Slack on Rails | Viget"
    url: "http://viget.com/extend/slack-on-rails"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-04/viget-com--slack-on-rails-viget.md"
    kind: repo
---

Slack can be used as an interface to internal services, and the post argues that this is easier than it was with Campfire and Hubot. It focuses on simple command-and-response integrations and says that Slash Commands and Outgoing WebHooks are the right fit for that use case.

## Reading notes

- Slack improves on Campfire by making chatroom integrations much more powerful.
- Outgoing WebHooks let an app receive Slack messages and reply publicly in the channel.
- Slack can be configured to receive messages that start with a trigger word or all messages from one channel.
- Slash Commands let an app receive command messages and reply privately to the user.
- A Rails app can be updated with Slack integration endpoints by storing Slack tokens, adding a route, and handling requests in a controller.
- The controller checks for a `:command` parameter to distinguish Slash Commands from normal Slack messages.
- A separate responder object turns the incoming message into the reply text.
