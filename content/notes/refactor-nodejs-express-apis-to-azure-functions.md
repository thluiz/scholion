---
title: "Tutorial: Refactor Your Node.js and Express APIs to Serverless APIs with Azure Functions"
date: '2020-04-20T21:22:21+00:00'
category: webclip
summary: 'The tutorial walks through shifting a Node.js and Express API to Azure Functions, with the aim of reducing server maintenance, scaling work, and deployment costs while keeping the app running locally during refactoring.'
tags: ["nodejs", "express", "azure-functions", "serverless"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Tutorial: Refactor Your Node.js and Express APIs to Serverless APIs with Azure Functions"
    url: "https://dev.to/azure/refactor-your-node-js-and-express-apis-to-serverless-apis-with-azure-functions-355j"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--refactor-nodejs-express-apis-to-azure-functions.md"
    kind: repo
---

The tutorial explains how to move a Node.js and Express API to a serverless model with Azure Functions. It frames the change around fewer servers to maintain, lower costs, and automatic scaling as demand changes, while also noting that the sample app starts as a TypeScript Express project.

## Reading notes

- The app powers a vacation planning website where customers can add, edit, view, and remove plans from a wish list.
- The API runs on Node.js and Express and is described as critical to the application.
- Serverless architecture is presented as a way to avoid maintaining a server, reduce costs, and scale the application up and down as needed.
- The tutorial starts by running the sample Node.js and Express app.
- The next step is creating an Azure Functions application.
- The code is then refactored so the Express routes and data calls use Azure Functions.
- The final step is to explore and launch the application.
- The sample project uses Angular on the client side, though the text says Vue.js or React.js could also have been used.
- The module also covers running and debugging the app locally alongside the Angular application.
