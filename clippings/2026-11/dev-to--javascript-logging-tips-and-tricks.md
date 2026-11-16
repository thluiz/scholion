---
url: "https://dev.to/headwayio/javascript-logging-tips-and-tricks-2h2c"
captured_at: "2026-11-16T01:38:58+00:00"
title: "Javascript Logging Tips and Tricks"
domain: "dev-to"
---

[![Headway profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Forganization%2Fprofile_image%2F2115%2Fe67da453-8c2f-44aa-93a4-7a9e7b0482b8.jpg)](https://dev.to/headwayio) [![Chris Held](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F13867%2F2686dc77-89bd-416f-8475-89b4dce0d892.jpg)](https://dev.to/chrisheld927)

`console.log` and `debugger` are probably the most common examples of debugging front end applications. Though `log` is the most common `console` function, there are a few others that you can leverage in your application for more descriptive and useful logging. In this post I'm going to cover a few extra functions you may not know about in the `console` object.

### [](#styled-logging)Styled Logging

In addition to `console.log`, there are a few functions to make your logging more semantic. `console.info`, `console.warn`, and `console.error` can apply some extra styles to your log statements and make your code a little bit more descriptive:

[![console info, warn, and error example](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F9o9oqy4eoqyr6hh1evqg.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F9o9oqy4eoqyr6hh1evqg.png)

### [](#assertions)Assertions

If you need to conditionally log an error, `console.assert` takes an expression and will log an error if the assertion is false.

[![console assert example](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fnhfuo3xmrwykmu7mi2bd.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fnhfuo3xmrwykmu7mi2bd.png)

### [](#tables)Tables

If you're logging table data, instead of using `console.log(data)`, consider using `console.table(data)`. `console.table` optionally accepts a second argument that lets you specify what columns you'd like displayed.

[![console table example](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fsxz8plvoyw350jkywhha.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fsxz8plvoyw350jkywhha.png)

### [](#custom-styles)Custom Styles

Info, warn, and error are a nice way to add some canned styles to your logging statements, but if you're looking for a little more control, `console.log` accepts a second argument that allows you to style your log statements using CSS:

[![Custom styled console log](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F9b7fcgfw9nrvro7m13sv.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F9b7fcgfw9nrvro7m13sv.png)

If you'd like to learn more, the [full MDN reference](https://developer.mozilla.org/en-US/docs/Web/API/console) is a great resource.
