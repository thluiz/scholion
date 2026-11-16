---
url: "https://dev.to/azure/refactor-your-node-js-and-express-apis-to-serverless-apis-with-azure-functions-355j"
captured_at: "2026-11-16T01:21:57+00:00"
title: "Tutorial: Refactor Your Node.js and Express APIs to Serverless APIs with Azure Functions"
domain: "dev-to"
---

Wondering how you could take advantage of Serverless architecture? Now you can [refactor a Node.js Express app to Azure Functions in this hands-on tutorial](https://docs.microsoft.com/en-us/learn/modules/shift-nodejs-express-apis-serverless/?wt.mc_id=devto-blog-jopapa)

## [](#overview)Overview

Your company is launching a vacation planning website that helps customers add, edit, view, and remove plans from their wish list. Your API, which powers these features, runs on Node.js and Express is critical to the success of the application.

Your API server is critical to the success of the application. The APIs are hosted on a server running Node.js and Express. When you launch your application, it must scale up and down as needed while minimizing costs. There's a lot for you to think about!

What if you could reduce some of these burdens without rewriting your entire API? By shifting the API to a serverless model using Azure Functions, you enjoy the following benefits:

*   No server to maintain
*   Cost reductions
*   Application scaling up and down as needed

Plus, you could write less code!

## [](#learning-objectives)Learning objectives

In this tutorial, you move from an Express API to a serverless architecture through the following steps:

1.  You'll begin by exploring and running the Node.js and Express APIs in the sample project
2.  Next, you'll create an Azure Functions application
3.  Then, you'll refactor the Express routes and data calls to use the Azure Functions application
4.  Finally, you'll explore and launch your application, as shown below

[![Vacation Wish List app](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fu4m5klznlmz42nibr15r.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fu4m5klznlmz42nibr15r.png)

## [](#planning-the-shift-to-serverless)Planning the Shift to Serverless

You're ready to shift your Express.js APIs to the serverless model. But first, consider why you might make these changes and what effort is required to update your app. Here are three things to consider:

*   Configure and maintain the physical server for your Express app
*   Managing scaling for your app (up and down), as demand fluctuates
*   Manage the costs associated with deploying your server

Serverless architecture eases the server maintenance, scaling, and cost for you.

Why would you make this shift? Overall there's less to think about when building a serverless app.

## [](#about-your-project)About your project

The app begins as a Node.js Express application in TypeScript that you'll shift to an Azure Functions app.

> If your Express app is using JavaScript instead of TypeScript, create an Azure Functions app using JavaScript.

What's in the [sample project on GitHub](https://github.com/MicrosoftDocs/mslearn-module-shifting-nodejs-express-apis-to-serverless) that you'll learn about in this module? That's a great question!

The client application is developed with Angular, however you could easily have used Vue.js or React.js. In this module, you learn to:

*   Create the Azure Functions app
*   Run and debug the app alongside the Angular application locally on your computer
*   Refactor the application's code to leverage a serverless design

When you're done, your application and its API will feature all the benefits of serverless technology!

Next, you'll get the sample application, install its dependencies, and build it locally.

[Try everything you see in this article in this hands-on tutorial](https://docs.microsoft.com/en-us/learn/modules/shift-nodejs-express-apis-serverless/?wt.mc_id=devto-blog-jopapa)
