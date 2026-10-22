---
title: "How to develop locally using serverless offline"
date: '2022-03-20T18:18:53-03:00'
category: webclip
summary: 'The article explains how the serverless-offline plugin emulates AWS Lambda and API Gateway locally, speeds up testing, and fits into an existing serverless workflow with Fauna.'
tags: ["serverless-offline", "aws-lambda", "fauna", "local-development"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to develop locally using serverless offline"
    url: "https://fauna.com/blog/develop-using-serverless-offline"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-03/fauna-com--how-to-develop-locally-using-serverless-offline.md"
    kind: repo
---

The article explains that serverless-offline lets Node.js developers emulate AWS Lambda and API Gateway on a local machine, so they can test changes without deploying every time. It says this improves logs, debugging, and team workflow, while keeping development local or in a shared environment.

## Reading notes

- The plugin starts a local HTTP server that handles request lifecycles and invokes handlers.
- The setup adds the serverless-offline package to a Node.js project and registers it in serverless.yml.
- Running `serverless offline` starts a local server that emulates AWS Lambda and API Gateway.
- An `.env` flag such as `IS_OFFLINE` can switch a Lambda client between a local endpoint and an AWS endpoint.
- The article shows invoking a Lambda locally with the AWS CLI against `http://localhost:3002`.
- The plugin provides a CLI with many options for ports, CORS, HTTPS, Docker, WebSocket settings, and other local configuration.
- The same options can also be set in `serverless.yml`, and CLI values override the file values.
- The guide then walks through creating a Fauna database, generating a security key, and creating an AWS Lambda function that queries a Fauna collection.
- The example uses the `faunadb` package, a client configured with the database secret, and a query against `indexes/all_customers`.
- The article closes by describing Fauna as a secure, scalable cloud API with native GraphQL and support for serverless, multiregional use.
