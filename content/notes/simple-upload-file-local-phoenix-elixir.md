---
title: "Simple upload file local Phoenix Elixir"
date: '2026-11-16T03:16:51+00:00'
category: webclip
summary: 'The page shows a minimal Phoenix upload form that receives a Plug.Upload, copies the temporary file into a local uploads folder, and wires the route, controller, view, and template.'
tags: ["phoenix", "elixir", "file-upload", "plug-upload"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Simple upload file local Phoenix Elixir"
    url: "https://yodiw.com/simple-upload-file-local-phoenix-elixir"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/yodiw-com--simple-upload-file-local-phoenix-elixir.md"
    kind: repo
---

The page explains a simple Phoenix file upload flow using only a few Elixir snippets. It adds an upload route, defines an UploadController with index and create actions, and stores the uploaded file in a local uploads folder with File.cp.

## Reading notes

- The tutorial uses the Hello project from the Phoenix installation guide and assumes the project already exists.
- The router adds "/upload" as a resources route with index and create actions.
- The UploadController renders the upload form on index.
- The create action reads the uploaded file from params under "docfile".
- The file upload data is a Plug.Upload stored in a temporary directory.
- The create action copies the temporary file to Path.absname("uploads/#{path_upload.filename}").
- The page creates an UploadView with an empty module definition.
- The template uses form_for with multipart: true and a file_input field named :docfile.
- The page says you need to create an uploads folder in the project root.
- It also links to a GitHub example project.
