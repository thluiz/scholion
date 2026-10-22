---
title: "Build serverless real-time chat application with Web PubSub and Static Web Apps"
date: '2021-08-02T21:19:05-03:00'
category: webclip
summary: 'The post explains how Chatr uses Azure Web PubSub and Azure Static Web Apps to deliver a serverless, real-time chat app with group chats, private chats, authentication, and idle detection.'
tags: ["azure-web-pubsub", "azure-static-web-apps", "real-time-chat", "serverless"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Build serverless real-time chat application with Web PubSub and Static Web Apps - DEV Community"
    url: "https://dev.to/azure/build-serveless-real-time-chat-application-with-web-pubsub-and-static-web-apps-glc"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2021-08/dev-to--build-serverless-real-time-chat-application-with-web-pubsub-.md"
    kind: repo
---

The post shows how Chatr combines Azure Web PubSub and Azure Static Web Apps to build a serverless real-time chat app. It frames real-time chat as a common need and uses the sample to show how chat features can be delivered with managed WebSockets, a frontend SPA, a Node.js backend, and Table Storage.

## Reading notes

- Real-time chat is presented as useful for healthcare, customer support, education, gaming, and social media.
- The article lists core needs such as user and group management, notifications, AI-enabled moderation or bots, and typing indicators.
- Azure Web PubSub is described as a fully managed service that adds real-time capability with native, serverless WebSockets.
- Chatr is a sample app built to show what is possible on Azure Web PubSub and Azure Static Web Apps, not a production-grade chat system.
- Chatr includes sign-in and authentication, group chats, private chats, a global online user list, and idle detection.
- The system is split into a Vue.js frontend, a Node.js backend, Azure Web PubSub, and Azure Table Storage.
- Web PubSub event handlers receive client WebSocket messages as HTTP events, including built-in system events and custom events like joinChat and userEnterIdle.
- The backend uses the Web PubSub Node.js SDK and keeps configuration such as the connection string in Function App settings.
- When a user creates a group chat, the backend reads event data from headers and the request body, updates state, and sends a custom message to all clients.
- The frontend gets a client access URL from the backend, then connects to Web PubSub with standard fetch and WebSocket APIs.
- The json.webpubsub.azure.v1 subprotocol enables client-to-client messaging, group messaging, and custom events.
- Chat messages can be sent directly through Web PubSub with sendToGroup, carrying JSON metadata such as the sender user ID.
- The post points readers to the Chatr GitHub repo, Azure documentation, and Azure Feedback Forum for more details.
