---
title: "Using ReactJS with Rails Action Cable"
date: '2015-07-26T10:20:51-03:00'
category: webclip
summary: 'The post shows how to wire React into a Rails chat app built with Action Cable, using jbuilder, a React comment list, channel subscriptions, and a broadcast job to refresh comments in real time.'
tags: ["reactjs", "rails", "action-cable", "websocket"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Using ReactJS with Rails Action Cable | BigBinary Blog"
    url: "http://blog.bigbinary.com/2015/07/19/using-reactjs-with-rails-actioncable.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-07/blog-bigbinary-com--using-reactjs-with-rails-action-cable.md"
    kind: repo
---

The post walks through adding ReactJS to an Action Cable chat application. It sets up the required gems and JavaScript files, uses jbuilder to send message and comment data to a React component, and replaces the old comment rendering with a React-based `CommentList`.

It also shows how the component subscribes to `CommentsChannel` through Action Cable, listens for updates, and refreshes its state when a new comment arrives. On the Rails side, a job broadcasts rendered message data after a comment is created so subscribed clients update in real time.

## Reading notes

- Action Cable is presented as Rails’ websocket-based real-time layer for applications like chats and status updates.
- ReactJS is used on the client side to manage view complexity and state updates.
- The setup adds `react-rails` and `sprockets-es6`, then requires React, `react_ujs`, and the components file in `application.js`.
- The article replaces the old CoffeeScript channel setup with an ES6 channel index file.
- A `CommentList` React component reads JSON passed in as props and renders each comment with the author name and content.
- A jbuilder partial builds JSON for a message and its comments, including nested user data.
- The message show view renders the React component with the JSON from the jbuilder partial.
- The component creates an Action Cable subscription to `CommentsChannel`, calls `follow` after connecting, and updates its state when data is received.
- On the Rails side, `CommentsChannel` streams from a message-specific comments channel.
- When a new comment is created, `MessageRelayJob` renders the message partial and broadcasts it to subscribed clients.
