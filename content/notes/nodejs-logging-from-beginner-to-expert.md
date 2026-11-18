---
title: "NodeJS logging, from beginner to expert."
date: '2020-04-18T11:13:58+00:00'
category: webclip
summary: 'Step‑by‑step NodeJS logging tutorial moving from console.log to a custom Winston‑based logger with transports, request tracking, safety checks and integration with external providers.'
tags: ["nodejs", "logging", "winston", "expressjs"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "NodeJS logging, from beginner to expert."
    url: "https://web.archive.org/web/20200418035704id_/https://dev.to/gkoniaris/nodejs-logging-from-beginner-to-expert-30a6"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--nodejs-logging-from-beginner-to-expert.md"
    kind: repo
---

Tutorial that walks through building a robust logging strategy in NodeJS. It starts from basic console.log usage in an Express API, then replaces it with a custom Winston‑based logger. The article shows how to add console and file transports, configure minimum log levels, integrate with Sentry, centralize error handling through middleware, correlate logs per request using async hooks, log manual stack traces, and guard against leaking sensitive metadata.

## Reading notes

- Uses an ExpressJS API example that fetches a post, first without logging, then with console.log for missing posts and database exceptions.
- Demonstrates wrapping route logic in try–catch to log both application errors and not‑found cases, showing the basic behavior of console.log and error stack traces.
- Motivates dedicated logging libraries by pointing out limitations of console.log around levels, filtering, formatting, and colorization.
- Chooses Winston as the logging library and installs it via `npm install --save winston`.
- Implements a Logger class that wraps `winston.createLogger`, sets a default level and `service` metadata, and exposes debug, info, warn and error methods plus a generic log function.
- The generic log function accepts a message and optional metadata object, assembling a metadata container before delegating to the underlying Winston logger.
- First test route `/logger` calls `logger.info` with a message and metadata and triggers a Winston warning because no transports are configured yet.
- Explains that Winston requires transports to know where to send logs and adds a Console transport to the logger’s configuration.
- Configures the console transport with a combined format including timestamp, metadata with `fillExcept`, colorize, and a custom `winstonConsoleFormat` formatter.
- The custom formatter concatenates timestamp, level, logger name and hostname with the message and serialized metadata into a single human‑readable line.
- Uses the NodeJS `os` module to inject the machine hostname into each log line.
- Shows a sample formatted console output that includes ISO timestamp, level, `logging-tutorial@ubuntu` identifier, message text, and JSON metadata.
- Discusses that formatted logs now carry richer context such as time, host, service name, severity and arbitrary metadata for easier debugging.
- Introduces configurable minimum log levels so production can avoid noisy debug messages.
- Changes the logger creation to take a `logLevel` option and passes `options.logLevel` into Winston’s `level` setting.
- Exports the logger instance with `APP_NAME` and `LOG_LEVEL` from environment variables, encouraging configuration through `.env`.
- Gives reasons to restrict severity levels in production: keeping the log stream readable, avoiding excessive storage use, and limiting stdout overhead.
- Notes that streaming to `process.stdout` is asynchronous but can still consume significant resources if used without limits.
- Argues for persisting logs to storage so old events can be inspected when debugging issues that happened days earlier.
- Selects file persistence as the most common approach and explains that Winston includes built‑in file transports.
- Adds a File transport that writes to `./logs/[name].log` with formats that include error stacks, metadata and JSON output.
- Mentions that separate log files per service name help in multi‑service setups and hints at using Winston docs for date‑suffixed filenames.
- States that file logging is generally fault‑tolerant, with failures mainly when disk is full or corrupted.
- Introduces external logging providers to make logs searchable, filterable, and assignable to developers.
- Chooses Sentry as the example provider, describing capabilities like aggregating logs, marking them resolved and detecting regressions.
- Uses the `winston-sentry-log` npm module as a Sentry transport implementation.
- Explains that the Sentry DSN is retrieved from the Sentry dashboard and placed in an environment variable used in transport configuration.
- Installs the Sentry transport module with `npm install --save winston-sentry-log`.
- Requires the Sentry module in the logger file and adds a new transport configured with DSN and `level: "warn"`.
- Notes that after adding the Sentry transport, warnings and errors are sent to Sentry alongside existing transports.
- Shows that Sentry can display structured logs in its UI, using an example info log screenshot.
- Observes that Sentry automatically scrubbed the `author` field as potentially sensitive, based on its default data scrubbers.
- Mentions that these scrubbing rules can be disabled or customized by defining which fields are considered sensitive.
- Identifies duplicated error‑handling patterns in routes where try–catch blocks both log errors and return generic 500 JSON responses.
- Suggests centralizing this behavior to reduce repetition and clarify which errors are truly unpreventable, such as database connectivity issues.
- Implements an Express error‑handling middleware that logs any received error and returns a standard 500 JSON response.
- Registers the error middleware after routes using `app.use(require('./middlewares/postErrorHandler'))`.
- Simplifies route handlers so they no longer need try–catch for generic server errors because unhandled exceptions propagate to the middleware.
- Emphasizes that centralized error handling removes many try–catch blocks dedicated purely to logging and generic responses.
- Introduces the idea of tracking the order and context of logs for each request to understand complex flows with multiple steps.
- Uses NodeJS `async_hooks` and `AsyncLocalStorage` to maintain per‑request context in an experimental API.
- Exports a shared AsyncLocalStorage instance from a LocalStorage helper module.
- Modifies the log function to retrieve the current store via `LocalStorage.getStore()` and attach `store.id` as `uniqueId` in metadata when available.
- In an example route, calls `LocalStorage.enterWith({id: uuid()})` to start a new context with a unique identifier per request.
- Logs several info messages within the same request so they share the same `uniqueId` in metadata.
- Shows console output where three logs in a single request carry the same UUID, and a subsequent request uses a different UUID.
- Suggests adding a pre‑middleware to automatically create and inject unique IDs for all incoming Express requests.
- Explains that filtering and sorting logs by UUID and timestamp helps trace the sequence of events leading up to an error.
- Notes that logging an Error object automatically outputs the stack trace, but sometimes a stack trace is needed for non‑error logs.
- Proposes a `logTrace` helper that creates an empty `Error`, grabs its stack, and forwards it to the main log function together with level, message and metadata.
- Adapts the generic log function to attach a `stackTrace` field into metadata when one is provided.
- Returns to the earlier observation that Sentry filtered out sensitive fields and proposes adding similar safety inside the custom logger.
- Accepts a `sensitiveFields` array in the logger options (e.g. `['password', 'creditCard']`) and sets a flag to enable checks.
- Implements a check that scans `metadataObject.metadata` keys and compares them against the sensitive fields list.
- When a sensitive key is detected, skips the original log and instead calls `logTrace` with a warning explaining which key was attempted to be logged.
- Shows example warning text where a `password` key triggers a warning log with attached stack trace metadata.
- Describes this mechanism as a way to prevent accidental leakage of secrets while still preserving context about where the attempt occurred.
- Briefly discusses log rotation and states a preference to handle it outside the logger rather than via Winston transports.
- Mentions using tools like pm2’s log‑rotation extension or standard UNIX `log-rotate` for managing log files.
- Warns that without rotation, log files can consume large amounts of disk space over time.
- Notes that legal requirements can impose limits on log retention when logs contain personally identifiable user data.
- Suggests moving older logs to other kinds of storage if allowed by local laws and advises consulting a lawyer for compliance details.
- Acknowledges that some features in the tutorial may be unnecessary for small projects or may introduce performance costs.
- Gives the example that checking every log for sensitive fields can be expensive at very high request volumes.
- Recommends moving certain logging responsibilities, such as request logging, into other layers like a proxy server when performance is critical.
- Invites readers to share the tutorial and describe their own NodeJS logging setups and practices.
- Provides links to related articles on Express middlewares, continuation local storage, async/await with global error handling, and the official Winston documentation.
