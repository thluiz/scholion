---
title: "Why we Built a Mini-Language for a Golang Hackathon"
date: '2026-09-25T01:02:43+01:00'
category: webclip
summary: 'The team created Fractal, a data-processing tool with a declarative mini-language for validation and transformation, to make pipelines more flexible and easier to configure.'
tags: ["golang","hackathon","data-pipelines","mini-language"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why we Built a Mini-Language for a Golang Hackathon"
    url: "https://dev.to/skysingh04/why-we-built-a-mini-language-for-a-golang-hackathon-42a3"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--why-we-built-a-mini-language-for-a-golang-hackathon.md"
    kind: repo
---

The page explains that the team wanted to build more than another tool in a Golang hackathon, so they created Fractal, a data-processing tool with a mini-language for validation and transformation rules. It also says the system was meant to work with a YAML configuration and support multiple input and output formats.

## Reading notes

- The Fractal project emerged as a data-processing tool to migrate data from legacy systems, such as SQL databases and CSV files, to platforms like MongoDB or AWS S3.
- The team wanted to go beyond a common ETL and create something more flexible and easy to use, with a declarative syntax for validation and transformation rules.
- The mini-language was designed to reduce reliance on rigid scripts and configurations that require more programming knowledge.
- The text highlights three goals for the language: simplicity, flexibility, and scalability.
- The YAML configuration was presented as part of the proposal to make the pipeline easier to configure.
- The validation rules mentioned include field type, numeric range, email regex, and membership in a set of values.
- The transformation rules mentioned include renaming fields, mapping values, adding new fields, and applying conditions such as a discount for age above 50.
- The system was also described as extensible, configurable, and robust, with support for formats such as JSON, CSV, SQL databases, and message queues.
- The hackathon work was divided into four modules: mini-language implementation, data integrations, pipeline engine, and command-line interface.
- Among the challenges were the design of the syntax, the creation of the lexer and parser in Golang, real-time error feedback, and the hackathon time limit.
- In the final evaluation, the team had a problem with a bug in the parser during the live demonstration, which caused them to lose first place.
- Even so, the group received the Best Pitch award.
- The text concludes that hackathons serve to test limits and explore new possibilities, and associates Fractal with an attempt to make data-processing tools more accessible, modular, and easier for developers.
