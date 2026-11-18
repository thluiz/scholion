---
title: "Logging Without a Static Logger"
date: '2019-06-30T10:38:37+00:00'
category: webclip
summary: 'Argues that static/global loggers complicate testing and user-facing logs, and proposes passing a log object as an injectable dependency instead.'
tags: ["logging", "object-oriented-design", "testing"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Logging Without a Static Logger"
    url: "https://www.yegor256.com/2019/03/19/logging-without-static-logger.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/yegor256-com--logging-without-a-static-logger-yegor256.md"
    kind: repo
---

The text critiques the common use of static or global loggers (singletons with methods like info(), error(), debug()) in applications. It argues that while this works for simple apps with little testing, global loggers are problematic: they make it harder to test logging behavior and to separate user-specific log output, especially in multi‑threaded environments.

As an alternative, the author describes a Ruby command line application (Zold) where a log object is passed as a constructor parameter into classes that need logging. The example class receives a log parameter with a default value of Log::NULL, which performs no logging. Different contexts provide different log implementations (console, temp file for web rendering, or a fake/mock logger in tests), enabling flexible routing and inspection of log output without relying on a static logger.

## Reading notes

- Typical applications use a global or singleton logger configured at startup or via a config file, sending output to console, files, or databases.
- The author followed this static logger approach for many years before deciding it was a mistake and changing strategy in a recent Ruby application.
- Static loggers are described as global variables, and global variables are characterized as harmful based on earlier discussions.
- One problem with a single global logger is difficulty in unit testing whether the application logs correctly, because intercepted log streams contain noise from other threads and tests.
- That testing issue is solvable, but the workarounds increase the complexity of tests.
- Another problem appears when only a selected part of the log needs to be shown to an end user, since code must separate relevant and irrelevant log entries.
- This separation is especially hard in multi‑threaded environments, and language features like Java thread groups help somewhat, while Ruby lacks an equivalent and needs workarounds.
- In the Zold Ruby command line application, the author decided to pass a log object as a variable to every class that needs logging.
- Ruby’s optional parameters make it convenient to pass such dependencies into constructors.
- The example class Zold::List is initialized with wallets and an optional log, and during run() it iterates over wallets and sends their balances to the log.
- The same class can use different log destinations: console in some cases, a temporary file in a web application that later gets rendered, or another receiver in tests.
- In unit tests, the log argument can be an object with debug(), info(), and similar methods that captures messages for later inspection.
- The default value for the log parameter is Log::NULL, a constant defined by the author as a logger implementation that does not output anywhere.
- With Log::NULL as default, the class performs its work and effectively logs nothing visible unless another log implementation is passed in.
- In tests, a fake or mock logger is injected into Zold::List to collect everything the class sends so that assertions can be made on the captured data.
- The author questions why static loggers are still prevalent in languages like Java, Ruby, PHP, and C# if this injectable approach is known.
- The recommendation is to use an injectable logging dependency instead of static or global loggers.
- The author notes a naming change from logger to log, implying a conceptual shift in how the logging object is viewed.
