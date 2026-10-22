---
title: "Node.js Best Practices — Error Handling and Logging"
date: '2020-09-21T15:10:01-03:00'
category: webclip
summary: 'The article recommends documenting API errors with GraphQL, exiting on unknown errors, logging with mature tools, testing error flows, monitoring app health, and catching unhandled promise rejections.'
tags: ["node-js", "error-handling", "logging", "monitoring"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Node.js Best Practices — Error Handling and Logging | by John Au-Yeung | Level Up Coding"
    url: "https://levelup.gitconnected.com/node-js-best-practices-error-handling-and-logging-341fc4ce6a72"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-09/levelup-gitconnected-com--node-js-best-practices-error-handling-and-logging.md"
    kind: repo
---

The article groups several practices for keeping a Node.js app maintainable when things fail. It points to GraphQL for documenting API errors, suggests stopping the process when an unknown error occurs, and recommends using a mature logger and monitoring tool to make failures easier to see.

## Reading notes

- GraphQL can document API errors through schema and comments, while also giving strong typing and autocomplete for queries.
- When an unknown error occurs, the process should exit and be restarted with a tool such as Forever or PM2.
- A logger such as Winston, Bunyan, Log4js, or Pino helps surface activity and errors; the example uses express-winston with Express.
- Automated tests are preferred over manual testing because they can cover both success and error cases quickly.
- APM or status monitoring tools can track CPU, memory usage, response time, requests per second, and other health metrics.
- Unhandled promise rejections and error events should be caught with catch handlers or process.on('unhandledRejection').
