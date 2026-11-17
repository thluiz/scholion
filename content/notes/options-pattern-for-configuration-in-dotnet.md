---
title: "What is the cleanest way to get configuration values in .NET?"
date: '2023-11-27T20:30:38+00:00'
category: webclip
summary: 'Thread recommends using the Options pattern for .NET configuration instead of raw IConfiguration, highlighting binding to classes, validation, and easier, less error‑prone usage.'
tags: ["dotnet", "configuration", "options-pattern"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Thread by @mjovanovictech: What is the cleanest way to get configuration values in .NET? I use the Options pattern, a…"
    url: "https://x.com/mjovanovictech/status/1728687891788820602"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2023-11/x-com--options-pattern-for-configuration-in-dotnet.md"
    kind: repo
---

Milan Jovanović explains that application configuration in .NET often comes from environment variables or JSON files and that directly accessing individual values via `IConfiguration` is cumbersome and error‑prone. He recommends using the Options pattern instead, where settings are represented by strongly typed classes that can be bound to configuration and consumed through `IOptions`, with support for validation.

## Reading notes

- Application configuration typically resides in environment variables or JSON configuration files.
- Accessing configuration values directly with the `IConfiguration` interface is described as error‑prone and awkward to use.
- The Options pattern is proposed as a cleaner alternative for handling configuration data in .NET applications.
- Using the Options pattern starts with defining a class that models the configuration settings.
- The properties of the settings class are bound to the corresponding application settings from JSON configuration.
- The configured settings are then consumed in application code via the `IOptions` abstraction.
- Data annotations can be applied on the settings class to perform simple validation of configuration values.
- More complex configuration validation rules can be implemented with tools such as FluentValidation.
- Jovanović promotes his .NET weekly newsletter as a resource with short, practical advice on .NET and software architecture.
- He mentions that configuration using this approach can be updated on the fly.
- The thread ends by asking readers whether they are already using the Options pattern.
