---
title: "Building a URL shortening service with NodeJS and MongoDB. Deploy to Azure."
date: '2026-11-16T19:41:13+00:00'
category: webclip
summary: 'The tutorial builds a URL shortener with NodeJS, Express, and MongoDB, then deploys it to Azure. It covers project setup, the frontend, database connection, URL model, routes, and form submission.'
tags: ["nodejs", "mongodb", "express", "azure"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building a URL shortening service with NodeJS and MongoDB. Deploy to Azure."
    url: "https://dev.to/olamideaboyeji/building-a-url-shortening-service-with-nodejs-and-mongobb-deploy-to-azure-oep"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--building-a-url-shortening-service-with-nodejs-mongodb.md"
    kind: repo
---

The page walks through a URL shortening service built with NodeJS, Express, and MongoDB, then deployed to Azure. It starts from project setup, installs the needed packages, and adds a simple public frontend that submits a long URL and a unique name.

## Reading notes

- The tutorial uses NodeJS, Express, MongoDB, and Azure.
- It assumes basic HTML, CSS, Javascript, NodeJS, MongoDB, and GitHub experience.
- It creates a project folder, runs npm init, and installs express, body-parser, mongoose, and nodemon.
- The package.json uses server.js as the main file and defines dev and start scripts.
- The frontend is a basic public folder with index.html, style.css, and main.js.
- The HTML form includes fields for the original URL and a unique name, and the page sets the displayed domain from window.location.host.
- The server.js file loads path, express, and body-parser, serves static files from public, and listens on process.env.PORT or 3000.
- The db.js file connects mongoose to process.env.MONGO_URI or a local MongoDB URL.
- The URL model stores originalUrl, shortUrl, unique_name, and dateCreated.
- The controllers include createShortLink and openShortLink.
- createShortLink checks whether unique_name already exists, saves the URL data, and returns the shortUrl.
- openShortLink finds a record by unique_name and redirects to the originalUrl.
- The server routes map POST /createShortLink to createShortLink and GET /:unique_name to openShortLink.
- The frontend JavaScript submits the form with fetch, shows a loader while waiting, and displays either an error or a link to the new short URL.
- Before Azure deployment, the page says to push the project to GitHub and use a remote MongoDB server such as MongoDB Atlas.
- The page ends by saying the app is live and mentions possible next features like user registration and link expiry.
