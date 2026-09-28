---
title: "Errors and Exception Handling in GoLang"
date: '2022-03-29T11:02:30-03:00'
category: webclip
summary: 'The page explains how Go handles errors with a second return value, how to create them with errors.New and fmt.Errorf, and how panic, recover, and custom error types fit into that model.'
tags: ["golang", "errors", "panic", "recover"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Errors and Exception Handling in GoLang - GoLang Docs"
    url: "https://golangdocs.com/errors-exception-handling-in-golang"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-03/golangdocs-com--errors-and-exception-handling-in-golang.md"
    kind: repo
---

Go handles errors through a simple pattern: functions can return an error as a second value, and that value should be checked before continuing. The page also shows that errors are used to represent unexpected cases, help keep code stable, and make programs easier to maintain.

## Reading notes

- Go functions return errors as a second value, and the error should be checked immediately before the next step.
- The errors package provides New() for creating a basic error.
- fmt.Errorf() creates a formatted error message.
- An error is checked by comparing it with nil, since the zero value of an error is nil.
- panic stops function execution when something unexpected happens.
- recover can catch a panic inside a deferred function and allow execution to continue.
- A custom error can be created by implementing the error interface with an Error() string method.
- Go can return a value and an error together, then the error is checked after the call.
- The blank identifier _ can be used to ignore the returned error.
