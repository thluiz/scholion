---
title: "Replacing Throwing Exceptions with Notification in Validations"
date: '2015-07-08T15:25:32-03:00'
category: webclip
summary: 'The article argues that validation failures should usually be collected in a Notification instead of thrown as exceptions, so code can report all errors and keep validation inside normal flow.'
tags: ["refactoring", "validation", "notification-pattern"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Replacing Throwing Exceptions with Notification in Validations"
    url: "http://martinfowler.com/articles/replaceThrowWithNotification.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-07/martinfowler-com--replacing-throwing-exceptions-with-notification-in-validatio.md"
    kind: repo
---

The article recommends replacing exceptions in raw-input validation with the Notification pattern. Its goal is to collect all validation errors, keep failure handling in the main flow, and preserve existing behavior while refactoring.

## Reading notes

- Exceptions fit unexpected failures, but validation errors in incoming data are expected and should usually be handled another way.
- Throwing on the first failure hides later problems, while a notification can gather multiple errors for one response.
- A notification can start as a simple list of strings, but a small class makes the intent clearer.
- The refactoring begins by splitting the original check method into an outer method that keeps throwing and an inner validation method that returns a notification.
- The article stresses preserving observable behavior and checking whether callers depend on the first error message or on a combined message.
- When replacing checks, it is important to move in small steps that keep the code working.
- Null checks need special care, because adding an error and then continuing can cause a null pointer exception.
- Extracting separate validation methods helps keep the code simpler when different fields need different handling.
- Guard clauses are preferred over nested if-then-else blocks in validation code.
- When an exception includes a cause, the notification must be extended to store that cause as well.
- The notification’s error record changes from a string to a small error object so messages and causes can be collected together.
- After the refactoring, callers can move from the old check method to the new validate method, and tests can be updated to expect collected errors.
