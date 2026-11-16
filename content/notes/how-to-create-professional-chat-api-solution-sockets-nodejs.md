---
title: "How to Create a Professional Chat API Solution with Sockets in NodeJS [Beginner level]"
date: '2026-11-16T03:35:44+00:00'
category: webclip
summary: 'The article walks through building a chat API with NodeJS, Express, MongoDB, JWT middleware, and Socket.io, covering users, rooms, messages, read states, and deletion endpoints.'
tags: ["nodejs", "express", "mongodb", "socket-io"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to Create a Professional Chat API Solution with Sockets in NodeJS [Beginner level]"
    url: "https://freecodecamp.org/news/create-a-professional-node-express"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/freecodecamp-org--how-to-create-professional-chat-api-solution-sockets-nodejs.md"
    kind: repo
---

The article outlines how to build a REST and sockets chat application on NodeJS, ExpressJS, and MongoDB. It starts with project setup, routes, controllers, middleware, and MongoDB connection, then adds user APIs, JWT authentication, and a socket layer for chat room events.

## Reading notes

- The tutorial sets up a Node project with Express, CORS, Morgan, Mongoose, Socket.io, JSON Web Token support, UUID, and nodemon.
- It creates a server entry point that mounts route handlers for index, users, chat rooms, and delete actions.
- MongoDB connection settings are placed in a config file with a database URL and database name.
- The user model stores first name, last name, and type, with types limited to consumer and support.
- The user API includes create, get by id, get all, and delete by id routes.
- User creation uses make-validation to check request body fields before calling a model static method.
- The JWT middleware defines an encode step that signs a token from the user id and type, and a decode step that verifies the bearer token from the authorization header.
- The login route returns the signed authorization token for a given user id.
- A WebSockets class tracks connected users by socket id and user id, removes them on disconnect, and handles identity, subscribe, and unsubscribe events.
- The chat room model stores user ids, room type, and chat initiator, and its static method either returns an existing room or creates a new one.
- The chat message model stores message data, read recipients, and message metadata, and uses aggregation with lookups to return enriched conversation data.
- The conversation route supports pagination, while the mark-read route updates unread messages for the current user.
- The article closes by noting bonus endpoints for deleting chat rooms and messages, and links to the full source code.
