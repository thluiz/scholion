---
title: "Logging Best Practices in ASP.NET Core"
date: '2025-08-11T15:12:34+01:00'
category: webclip
summary: 'The post recommends Serilog for ASP.NET Core, using the right log levels, filters, structured logging, sensitive-data protection, error logging, log rotation, async sinks, and a centralized UI like Seq.'
tags: ["asp-net-core", "serilog", "structured-logging", "seq"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Logging Best Practices in ASP.NET Core"
    url: "https://antondevtips.com/blog/logging-best-practices-in-asp-net-core?utm_source=email&utm_medium=email&utm_campaign=website"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-08/antondevtips-com--logging-best-practices-in-asp-net-core.md"
    kind: repo
---

The post lays out practical logging guidance for ASP.NET Core applications. It favors Serilog over the built-in provider, uses log levels and filters to control volume, and treats structured logging as the default so fields stay searchable. It also stresses keeping sensitive data out of logs, capturing errors with context, and managing size and performance with rotation, retention, and async sinks. A centralized UI such as Seq is presented as a way to search, visualize, and alert on logs.

## Reading notes

- Serilog is recommended because it is performant, supports structured logging, and works on top of Microsoft.Extensions.Logging.
- Logging levels should match message importance, with Information or Warning as the default and Debug or Trace enabled only when needed.
- Filters can lower log volume by setting different minimum levels for namespaces such as Microsoft, OpenTelemetry, Quartz, and ASP.NET Core MVC.
- Structured logging keeps values like OrderId, ShipmentNumber, and State as searchable fields instead of plain text.
- String interpolation should be avoided in log calls because it turns structured data into unsearchable text.
- Sensitive information such as passwords, credit card numbers, API keys, authentication tokens, and connection strings should not be logged.
- Serilog can mask properties through destructuring policies, redact values manually, or exclude log events with filters.
- Errors should be logged with exception details and contextual data such as UserId and RequestPath, while stack traces should not be exposed to users.
- Log growth should be controlled with daily rotation, retention limits, file size limits, and asynchronous sinks for file logging.
- Console logging should be turned off in production.
- A centralized logging UI such as Seq can aggregate logs, support searches on structured fields, and enable alerts.
- The post also lists alternatives such as ELK Stack, Datadog, New Relic, Loggly, GrayLog, Azure Monitor Logs, and Amazon CloudWatch Logs.
