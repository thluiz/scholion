---
title: "How to build a LinkedIn-like Messaging App with React and TalkJS - Part 1"
date: '2019-12-24T23:27:35+00:00'
category: webclip
summary: 'The tutorial shows how to set up a React app for a LinkedIn-like messaging experience, with a login form, a My Network page, and local storage for the current user before adding TalkJS chat in part 2.'
tags: ["react", "talkjs", "messaging-app"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to build a LinkedIn-like Messaging App with React and TalkJS - Part 1"
    url: "https://dev.to/talkjs/how-to-build-a-linkedin-like-messaging-app-with-react-and-talkjs-part-1-n9c"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--how-to-build-a-linkedin-like-messaging-app-with-react-and-ta.md"
    kind: repo
---

The page introduces a two-part tutorial for building a LinkedIn-like messaging app with React and TalkJS. In this first part, it sets up the app, creates the login flow, and builds the My Network page with dummy users and a current-user panel saved in local storage.

## Reading notes

- Chat is presented as a common feature in modern web applications, but building it from scratch is described as difficult.
- TalkJS is introduced as a way to add chat to a website or mobile app through its API and SDK.
- The tutorial’s example app is a LinkedIn-like messaging app, and the repository and live demo are linked.
- The tutorial is split into two parts, with part 1 covering the app without chat and part 2 adding chat with TalkJS.
- TalkJS is described as offering real-time messaging, file sharing, location sharing, emoji, email and SMS fallback, a chat pop-up, conversation history, responsive UI, and multilingual interfaces.
- The prerequisites listed are basic JavaScript knowledge, React knowledge, and Node and npm installed.
- The app being built has three major parts: a login page, a MyNetwork page, and a Messaging page.
- The login form collects name, email, and description, generates a random user ID, stores the data in local storage, and redirects to the My Network page.
- The app uses Create React App and react-router to set up the basic project structure and routes.
- The My Network page uses dummy user data to render a list of connections, each with a Message button.
- The current user is read from local storage and displayed in the interface alongside the user list.
- The page ends after the app has a login page and a My Network page, and says TalkJS chat will be added in the next part.
