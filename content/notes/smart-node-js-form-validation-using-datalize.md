---
title: "Smart Node.js Form Validation"
date: '2026-11-16T06:18:50+00:00'
category: webclip
summary: 'The article shows how datalize adds validation for Node.js APIs, including request bodies, queries, params, arrays, nested objects, custom rules, and automatic error handling.'
tags: ["node-js", "form-validation", "api", "datalize"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Node.js Form Validation Using Datalize | Toptal®"
    url: "https://toptal.com/nodejs/smart-node-js-form-validation"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/toptal-com--smart-node-js-form-validation-using-datalize.md"
    kind: repo
---

The article presents datalize as a small, extendable Node.js library for validating API input and formatting the accepted data. It works with request bodies, query strings, and params, and supports async filters, nested objects, arrays, and custom rules.

It also shows how datalize can simplify create and update flows with shared validation middleware, automatic validation errors, and custom field filters. The library includes helpers for dates, files, and other repeated validation tasks.

## Reading notes

- Datalize is described as a tiny but powerful library for Node.js form validation.
- It validates request body, query, and params data.
- It supports async filters and complex JSON structures such as arrays and nested objects.
- Rules and filters run in the order they are defined.
- The .form object contains only the validated fields.
- The .form.isValid property indicates whether validation succeeded.
- A global autoValidate setting can make datalize throw validation errors automatically.
- Query validation uses .query(), and validated query data is stored in .data.
- Parameter validation is also available through .params().
- The .custom() method lets you define validation logic when no built-in rule fits.
- The .container() method is used for nested objects.
- The .array() filter applies rules to each array value.
- The .patch() and .optional() filters support create and update workflows.
- Custom global filters can be added by extending Field.prototype.
- The article mentions date, dateTime, file, mime, and size filters.
