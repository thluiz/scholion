---
title: "Best practices for private config data and connection strings in configuration in ASP.NET and Azure"
date: '2016-01-07T16:36:14-03:00'
category: webclip
summary: 'The post recommends keeping passwords and connection strings out of source control, externalizing them into ignored files or environment variables, and using Azure app settings, user secrets, or Key Vault when appropriate.'
tags: ["asp-net", "azure", "connection-strings", "secrets"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Best practices for private config data and connection strings in configuration in ASP.NET and Azure - Scott Hanselman"
    url: "http://www.hanselman.com/blog/BestPracticesForPrivateConfigDataAndConnectionStringsInConfigurationInASPNETAndAzure.aspx"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-01/hanselman-com--best-practices-for-private-config-data-and-connection.md"
    kind: repo
---

The post argues that the safest way to avoid leaking passwords and connection strings is to keep them out of source files and out of common config files that get checked into source control. It suggests externalizing sensitive values, ignoring the external file, and using Azure application settings or user-level secrets when the platform supports them.

## Reading notes

- Keep passwords and connection strings out of source control.
- Treat only truly sensitive material, such as private keys, as a stronger security case and use data protection systems or Azure Key Vault for that.
- In ASP.NET 4.6, move sensitive appSettings values into an external file through the `file` attribute so they are merged at runtime.
- For connection strings, use `configSource` to point to a separate file.
- In Azure Web Apps, store connection strings and app settings in the Application Settings section instead of in `web.config` or hard-coded values.
- Azure app settings are also exposed as environment variables, so code can read them without changing the application.
- ASP.NET 5 introduces User Secrets stored outside the project folder, which reduces the chance of checking them in.
- The configuration builder can combine appsettings files, environment-specific settings, user secrets, and environment variables in code.
- The post closes by recommending that private values stay out of code, out of shared config files, and out of the project folder during development.
