---
title: "Hosting Gotchas — Ocelot API Gateway v25.0 \".NET 10\" documentation"
date: '2026-09-25T18:31:49+01:00'
category: webclip
summary: 'The page lists hosting issues for Ocelot under IIS and Kestrel, warning about startup errors, slow responses, large-file proxying, and Kestrel request-body limits.'
tags: ["iis", "kestrel", "hosting", "large-files"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Hosting Gotchas — Ocelot API Gateway v25.0 \".NET 10\" documentation"
    url: "https://ocelot.readthedocs.io/en/latest/introduction/gotchas.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/ocelot-readthedocs-io--hosting-gotchas-ocelot-api-gateway.md"
    kind: repo
---

The page says many Ocelot errors and incidents come from web server hosting scenarios. It separates the advice by IIS and Kestrel, and points to common deployment problems for each environment.

## Reading notes

- IIS deployment is not recommended, but if Ocelot is hosted there, ASP.NET Core 2.2+ should use `UseIIS()` for in-process hosting, not `UseIISIntegration()`, to avoid startup errors.
- IIS in-process hosting is discouraged because it can lead to very slow responses.
- Slow responses can also happen if DNS servers for downstream hosts are not online and working correctly.
- For IIS problems, the page advises checking open and closed issues and searching the repository for IIS-related code and discussions.
- Kestrel self-hosting is recommended, including Kestrel and Docker scenarios.
- Large files should not be pumped through the gateway when possible, because it consumes memory and CPU, increases delay, can cause downstream streaming errors, and affects other routes.
- The page says large-file issues are commonly reported around `application/octet-stream` content type and chunked encoding.
- If large files still go through Ocelot, the page points to version 23.0 and higher.
- Another Kestrel issue is `MaxRequestBodySize` not being configured correctly when large files exceed the limit.
- The page gives a quick fix that sets `serverOptions.Limits.MaxRequestBodySize` to a total size larger than the expected file size.
