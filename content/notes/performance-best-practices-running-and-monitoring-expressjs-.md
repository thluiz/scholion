---
title: "Performance Best Practices: Running and Monitoring Express.js in Production"
date: '2020-07-05T14:11:25+00:00'
category: webclip
summary: 'The article argues that production Express.js apps should prioritize uptime, predictable resource use, scaling, and faster debugging through structure, async code, logging, metrics, and DevOps tooling.'
tags: ["expressjs", "performance", "monitoring", "devops"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Performance Best Practices: Running and Monitoring Express.js in Production"
    url: "https://dev.to/sematext/performance-best-practices-running-and-monitoring-express-js-in-production-3e82"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--performance-best-practices-running-and-monitoring-expressjs-.md"
    kind: repo
---

The article says a performant Express.js application should aim for minimal downtime, predictable resource usage, effective scaling, and higher developer productivity. It recommends a basic project structure, async code, structured logging, metrics, and production tooling like dotenv, systemd, PM2, Nginx, Redis, and monitoring.

## Reading notes

- An intuitive file structure helps keep files small, makes reviews and refactoring easier, and reduces merge conflicts.
- The suggested layout separates config, controllers, providers, services, models, routes, database setup, and tests.
- Setting `NODE_ENV=production` is presented as a quick performance improvement.
- Gzip compression should be enabled, either in Express or at the Nginx layer.
- Synchronous functions should be avoided because they block the thread; Promises and async functions are preferred.
- If a CPU-heavy task cannot be avoided, it should run in child processes or forks instead of blocking the main thread.
- Logs should be structured and collected centrally instead of using `console.log()`.
- The Sematext Express agent is shown as a way to send logs and request data to a central logging system.
- Errors should be handled with try-catch, a catch-all error middleware, and process-level listeners for uncaught exceptions and unhandled rejections.
- Memory leaks should be watched through process and heap metrics, especially when memory grows steadily without matching request growth.
- Pure functions are recommended because they do not mutate outer state and make code easier to reason about.
- Function arguments are easier to manage when passed as objects, since names do not depend on parameter order.
- Tests should be written first or early, using Mocha and Chai in the example.
- `dotenv` is used to load environment variables from a `.env` file.
- Systemd can run the Node.js app as a service and restart it on failure.
- PM2 can also restart the app and run it in cluster mode.
- The Node.js cluster module can fork workers across CPU cores and restart failed workers.
- Nginx is recommended as a reverse proxy rather than exposing Node.js directly on ports 80 or 443.
- Nginx can also handle load balancing, caching, and gzip compression.
- Redis can cache API responses and reduce repeated database work.
- Infrastructure-wide monitoring is needed because Nginx or Redis can fail even when the Express app itself is still running.
- Alerts are important so failures are detected before users report them.
