---
title: "How to Create a Resumable Video Uploader in Node.js"
date: '2013-08-26T09:49:53-03:00'
category: webclip
summary: 'The tutorial builds a Node.js and Socket.io uploader that resumes interrupted video uploads, tracks progress in blocks, stores temporary data, and generates a thumbnail when the upload finishes.'
tags: ["node-js", "socket-io", "resumable-upload", "video-upload"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to Create a Resumable Video Uploader in Node.js | Nettuts+"
    url: "http://net.tutsplus.com/tutorials/javascript-ajax/how-to-create-a-resumable-video-uploade-in-node-js/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-08/net-tutsplus-com--how-to-create-a-resumable-video-uploader-in-node-js.md"
    kind: repo
---

The page explains how to build a resumable video uploader in Node.js with Socket.io. The browser sends file blocks with FileReader, the server keeps track of what has already been received, and the completed file is moved out of a temp folder before a thumbnail is generated with ffmpeg.

## Reading notes

- The uploader is designed to resume after an interrupted upload, so the server tracks how much of a file has already arrived and continues from that point.
- Socket.io handles communication between the Node.js server and the HTML page through emitted events.
- The HTML form uses a file input, a name field, and an upload button inside a simple layout.
- The page checks whether the browser supports the HTML5 File API and FileReader before enabling the upload flow.
- The FileChosen function stores the selected file in a global variable and fills the name field with the file name.
- The Node.js server serves index.html and listens for Socket.io connections on port 8080.
- The client connects to the Socket.io server, creates a FileReader, updates the page with a progress bar, and starts the upload by sending the file name and size.
- The Start event creates an entry for each file, checks whether a temporary file already exists, and sets the upload position from that file size when needed.
- The Upload event appends incoming data to a buffer, writes to disk when the upload completes or when the buffer grows too large, and then requests more data.
- The client responds to MoreData by slicing the next block from the selected file and reading it as a binary string.
- The progress bar shows upload percentage and megabytes uploaded.
- After the upload finishes, the file is copied from Temp/ to Video/ with streams and util.pump, then the temporary file is deleted.
- ffmpeg is called through exec to generate a JPG thumbnail from the finished video.
- The Done event replaces the progress bar with the thumbnail and adds a button to upload another file.
