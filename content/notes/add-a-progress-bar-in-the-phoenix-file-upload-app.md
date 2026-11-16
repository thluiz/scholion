---
title: "Add a Progress Bar in the Phoenix File Upload app"
date: '2026-11-16T04:15:41+00:00'
category: webclip
summary: 'The article shows how to monitor Phoenix file uploads with jQuery Ajax, XHR progress events, a percentage label, and an HTML5 progress bar, then auto-start the upload and redirect on success.'
tags: ["phoenix", "file-upload", "javascript", "progress-bar"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Add a Progress Bar in the Phoenix File Upload app · Poeticoding"
    url: "https://poeticoding.com/add-a-progress-bar-in-the-phoenix-file-upload-app"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/poeticoding-com--add-a-progress-bar-in-the-phoenix-file-upload-app.md"
    kind: repo
---

The article explains how to add a visible upload progress indicator to a Phoenix file upload app. It starts by simulating slow network conditions in Chrome, then uses jQuery Ajax and XHR progress events to read upload progress and update both a percentage label and an HTML5 progress element.

## Reading notes

- The app already supports multipart uploads and thumbnail generation for images and PDFs, but slow real-world uploads need a better interface.
- Chrome throttling can expose how the page behaves during large uploads and makes the lack of feedback easier to see.
- The upload form gets an id so jQuery can intercept submit events and build a FormData object from the form.
- The upload is sent with jQuery.ajax to POST /uploads, with processData set to false and contentType set to false.
- The xhr callback creates an XMLHttpRequest and attaches a progress listener to xhr.upload.
- A progress handler receives ProgressEvent data, reads loaded and total, and computes a percentage string.
- The form template is updated with a label that displays the upload percentage.
- The handler is created by a function that closes over form elements so it can update the label and later the progress bar.
- On success, the browser is redirected to /uploads instead of staying on a page stuck at 100%.
- The page then replaces the plain label with an HTML5 progress element and styles it with CSS.
- The progress bar is hidden until the upload starts, then shown from JavaScript.
- The same progress event updates the bar by setting max to total and value to loaded.
- The upload form is moved into the upload list page by rendering the form template from the index template.
- The file input is wrapped around a custom button so selecting a file can trigger upload automatically.
- The article ends by mentioning other libraries for richer upload and progress UI, including progressbar.js, jQuery File Upload, and DropzoneJS.
