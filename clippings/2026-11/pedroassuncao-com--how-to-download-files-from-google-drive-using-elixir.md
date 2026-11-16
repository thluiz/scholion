---
url: "https://pedroassuncao.com/posts/how-to-download-files-from-google-drive-using-elixir"
captured_at: "2026-11-16T04:35:04+00:00"
title: "How to download files from Google Drive using Elixir"
domain: "pedroassuncao-com"
---

![attachments/covers/how-to-download-files-from-google-drive-using-elixir.png](https://publish-01.obsidian.md/access/b8103112685b26b19f61b853d7c6dff1/attachments/covers/how-to-download-files-from-google-drive-using-elixir.png)

_24 Jul 2020_

The documentation around downloading a file from a [Google Drive](https://drive.google.com/) account is a bit spread out, so i figured i could make a mini tutorial on how to do this.

The scenario is having a CSV file in a folder on my Google Drive and being able to read it from [Elixir](https://elixir-lang.org/). Here's the setup:

*   Setup a service account using the [Google Developer Console Dashboard](https://console.developers.google.com/apis/credentials) (there are plenty tutorials on the web how to setup service accounts), and save the .json credentials file in your Elixir project somewhere.

![1\*CDjPWQ\_FJfk4KRTGCm8ZOA.png](https://cdn-images-1.medium.com/max/864/1*CDjPWQ_FJfk4KRTGCm8ZOA.png)

*   Make sure the service account has access to all accounts in your domain (unsure this step is necessary, TBH).

![1\*ZXs8OThvHzTClITkqhreuw.png](https://cdn-images-1.medium.com/max/458/1*ZXs8OThvHzTClITkqhreuw.png)

*   The service account will have an email associated with it (something along the lines of [service\_account\_name@yourproject.iam.gserviceaccount.com](mailto:service_account_name@yourproject.iam.gserviceaccount.com)). Share the folder you want to read the files from with that email in your Google Drive interface.

![1\*D6YJO9UvhuUfzvghNwgPCA.png](https://cdn-images-1.medium.com/max/496/1*D6YJO9UvhuUfzvghNwgPCA.png)

*   Now we are ready to move to Elixir.
*   Install the following two dependencies in mix.exs:

```
{:google_api_drive, "~> 0.15.0"},<br>{:goth, "~> 1.2.0"},
```

*   Configure goth to use your .json credentials file in config.exs (you can also do it programmatically, just look at [goth's docs](https://github.com/peburrows/goth)):

```
config :goth,<br>  json: “google_service_account.json” |> File.read!
```

*   Finally, the following snippet will take the first CSV file it finds and read its contents:

````
{:ok, %{token: token}} = Goth.Token.for_scope("https://www.googleapis.com/auth/drive")
``` ```
conn = GoogleApi.Drive.V3.Connection.new(token)
``` ```
{:ok, %{files: files} = file_list} = GoogleApi.Drive.V3.Api.Files.drive_files_list(<br>  conn,<br>  includeItemsFromAllDrives: true,<br>  supportsAllDrives: true,<br>  corpora: "allDrives"<br>)
``` ```
[first | _rest] = files <br>  |> Enum.filter(&(&1.mimeType == "text/csv"))<br>  |> Enum.map(&(Map.take(&1, [:id, :name])))
``` ```
{:ok, %{body: body}} = GoogleApi.Drive.V3.Api.Files.drive_files_get(<br>  conn,<br>  first.id,<br>  [<br>    mimeType: "text/csv",<br>    alt: "media"<br>  ],<br>  [<br>    decode: false<br>  ]<br>)
``` ```
body
````

Happy Elixir'ing
