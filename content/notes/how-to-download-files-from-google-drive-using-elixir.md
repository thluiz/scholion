---
title: "How to download files from Google Drive using Elixir"
date: '2020-08-26T19:31:15+00:00'
category: webclip
summary: 'The post shows how to set up a Google service account, share a Drive folder with it, configure Goth in Elixir, and use the Drive API to list CSV files and download the first one found.'
tags: ["elixir", "google-drive", "goth", "google-api-drive"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to download files from Google Drive using Elixir"
    url: "https://pedroassuncao.com/posts/how-to-download-files-from-google-drive-using-elixir"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/pedroassuncao-com--how-to-download-files-from-google-drive-using-elixir.md"
    kind: repo
---

The post explains a small workflow for reading a CSV file from Google Drive in Elixir. It starts by setting up a service account, saving the JSON credentials in the project, and sharing the target Drive folder with the service account email.

## Reading notes

- create a service account in Google Developer Console and save the JSON credentials file in the Elixir project
- give the service account access to the domain accounts if needed, though the post says this step may not be necessary
- share the Drive folder that contains the files with the service account email
- add `google_api_drive` and `goth` to `mix.exs`
- configure `goth` in `config.exs` to read the JSON credentials file
- request a token for the Google Drive scope with `Goth.Token.for_scope("https://www.googleapis.com/auth/drive")`
- create a Drive connection with the token
- list files with `drive_files_list/2` using `includeItemsFromAllDrives`, `supportsAllDrives`, and `corpora: "allDrives"`
- filter the returned files for `text/csv`, take the first one, and keep its `id` and `name`
- fetch the file body with `drive_files_get/4` using `mimeType: "text/csv"`, `alt: "media"`, and `decode: false`
- the final result is the downloaded body of the CSV file
