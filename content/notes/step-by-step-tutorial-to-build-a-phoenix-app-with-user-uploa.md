---
title: "Step-by-Step Tutorial to Build a Phoenix App that Supports User Upload · Poeticoding"
date: '2026-11-16T04:15:55+00:00'
category: webclip
summary: 'The article builds a Phoenix app from scratch with local file uploads, Postgres and Ecto, a Documents context, a controller for upload, list, and download actions, and a higher multipart limit.'
tags: ["phoenix", "file-uploads", "ecto", "postgres"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Step-by-Step Tutorial to Build a Phoenix App that Supports User Upload · Poeticoding"
    url: "https://poeticoding.com/step-by-step-tutorial-to-build-a-phoenix-app-that-supports-user-uploads"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/poeticoding-com--step-by-step-tutorial-to-build-a-phoenix-app-with-user-uploa.md"
    kind: repo
---

The guide shows how to build a Phoenix 1.4 app that accepts user uploads using only Phoenix tools. It sets up Postgres with Docker, configures Ecto, stores upload metadata in the database, saves files locally, and later lets users download them.

## Reading notes

- Starts a new Phoenix app, installs dependencies, and builds assets with Node.js tools.
- Uses Docker to run a Postgres container with a persistent volume.
- Keeps the uploads directory outside the app folder and reads its path from configuration.
- Generates an Ecto schema and migration for uploads with filename, size, content_type, and hash fields.
- Changes the migration to use bigint for size, limits hash to 64 characters, and adds an index on hash.
- Adds schema validations for required fields, positive size, and 64-character hash length.
- Defines a SHA-256 helper that hashes a file stream.
- Defines a local_path function that builds the destination filename from the upload id and original filename.
- Notes that reading uploads_directory at compile time makes configuration changes harder, so it replaces the module attribute with a function.
- Maps GET /uploads/new, POST /uploads, GET /uploads, and GET /uploads/:id to the UploadController.
- Renders a multipart form with file input and submit button in the new template.
- Shows that Plug receives the uploaded file as a %Plug.Upload{} with filename, content_type, and path.
- Introduces a Documents context to keep upload logic out of the controller.
- The create_upload_from_plug_upload/1 function calculates the hash, gets file size, inserts the upload record, and copies the file to local storage.
- Wraps the database insert and file copy in a transaction so failures roll back.
- Implements create/2 to call the context, set a flash message, and redirect on success or error.
- Adds list_uploads/0 and index/2 to display stored uploads in a table.
- Adds a download link for each upload and uses send_download in show/2 to serve the file.
- Raises the multipart parser limit in Endpoint so larger files can be uploaded.
