---
title: "Transactional HTML Email Templates"
date: '2015-05-10T09:14:11-03:00'
category: webclip
summary: 'The page presents open-sourced transactional email templates for action, alert, and billing messages, and explains inline CSS, media queries, client testing, and a Grunt workflow for designing and testing them.'
tags: ["email-templates", "inline-css", "responsive-design", "email-client-testing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Transactional HTML Email Templates"
    url: "http://blog.mailgun.com/transactional-html-email-templates/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/blog-mailgun-com--transactional-html-email-templates.md"
    kind: repo
---

The page introduces a free, open-sourced set of transactional HTML email templates. It says HTML email styling is difficult because of tables, inline CSS, unsupported CSS, and differences across desktop, web, and mobile clients, so the templates are meant to reduce that work.

## Reading notes

- The collection includes templates for action emails such as account activation and password resets, email alerts such as limits or problems, and billing emails such as monthly receipts and invoices.
- Each template is responsive and has been tested in popular email clients.
- The page recommends inlining CSS before sending HTML email and notes that media queries should not be inlined.
- The repository includes original templates with a separate stylesheet and versions with CSS already inlined.
- The templates use media queries for mobile-friendly design, and the page notes that only a handful of email clients support them, including iOS Mail, Android 4.x, and Windows Phone 7.5 native email apps.
- The templates were tested across major desktop, web, and mobile clients using Litmus.
- The page also points to a Grunt task used to compile and test HTML emails, including email layouts, SCSS compilation, CSS inlining, and preview emails.
