---
title: "Build Your Own Custom SlackBot with Node.js"
date: '2016-05-11T06:31:50-03:00'
category: webclip
summary: 'The tutorial shows how to turn a Slack channel into a command-driven terminal with a Node.js bot, using slack-terminalize to map commands, handle aliases, and post responses back to the channel.'
tags: ["node", "slack", "slackbots"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Build Your Own Custom SlackBot with Node.js"
    url: "http://www.sitepoint.com/custom-slackbot-with-node/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-05/sitepoint-com--build-your-own-custom-slackbot-with-node-js.md"
    kind: repo
---

The article explains how to build a simple Slack bot with Node.js that treats regular channel messages as commands. It uses slack-terminalize to handle message processing, dispatch commands from configuration files, and support custom behavior through separate command modules.

## Reading notes

- Slack is presented as a good fit for custom integrations because its APIs let developers extend team workflows.
- The tutorial’s goal is to turn a Slack channel into a custom command-line terminal.
- The approach uses slack-terminalize, which wraps message parsing and dispatching.
- It does not use Slash Commands; it interprets normal messages as commands.
- The reader is assumed to know JavaScript, Node.js, and Slack concepts such as teams, channels, bots, and integrations.
- A new bot user is created in Slack, and its API token is copied for use in the app.
- The sample app is cloned and dependencies are installed with npm.
- Configuration files live in config/, and command implementations live in commands/.
- commands.json defines each command with a primary name, aliases, description, help text, exclude flag, and optional endpoint.
- The command filename in commands/ matches the primary command name in commands.json.
- The help command reads command details from commands.json and responds synchronously.
- The gem command shows an asynchronous example by calling a REST endpoint and posting the result back to the same channel.
- New commands are added by defining them in commands.json and creating a matching implementation file.
- Command names with spaces are not supported.
- The command function receives the command name, args, user id, channel id, and the command’s config object.
- slack-terminalize can be configured with options such as autoReconnect and directory paths for config and commands.
- The article closes by encouraging readers to define more commands, fork the project, and use Slack API capabilities for productivity.
