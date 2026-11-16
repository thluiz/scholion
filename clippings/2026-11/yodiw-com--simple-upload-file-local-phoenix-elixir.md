---
url: "https://yodiw.com/simple-upload-file-local-phoenix-elixir"
captured_at: "2026-11-16T03:16:51+00:00"
title: "Simple upload file local Phoenix Elixir"
domain: "yodiw-com"
---

There is a lack of information on how to do simple upload form in Phoenix Framework and store file into local storage. Although people recommend using Plug or external libraries, sometimes is useful to understand how essential thing work like upload image or PDF can be done using few Elixir scripts.

In this tutorial, I’m using an example of Hello project from Phoenix’s installation guideline. If you don’t have the project yet, please set-up by yourself since this tutorial does not cover it.

![](https://www.yodiw.com/wp-content/uploads/2020/04/%E6%8D%95%E8%8E%B7.png)

In the beginning, let write a path to access the upload page in the router, “lib/hello\_web/router.ex”. Let use “upload” as the access path

```
  scope "/", HelloWeb do
    pipe_through :browser

    get "/", PageController, :index
    resources "/upload", UploadController, only: [:index, :create]
  end
```

If you don’t understand how resources work in Phoenix, please read the docs. In this case, we enable “index” as the main page and “create” to handle the upload action.

```
defmodule HelloWeb.UploadController do
  use HelloWeb, :controller

  @spec index(Plug.Conn.t(), any) :: Plug.Conn.t()
  def index(conn, _params) do
    render(conn, "index.html")
  end

  def create(conn, %{"upload" => upload}) do
    path_upload = upload["docfile"]

    IO.inspect path_upload.filename, label: "Photo upload information"
    File.cp(path_upload.path, Path.absname("uploads/#{path_upload.filename}"))

    json(conn, "Uploaded #{path_upload.path} to a temporary directory")
  end

end
```

Upload params with are containing Plug.Upload where it’s handle uploaded files are stored in a temporary directory and removed that directory after the process that requested the file dies.

Third, we need to create a view “hello\_web/views/upload\_view.ex”

```
defmodule HelloWeb.UploadView do
  use HelloWeb, :view
end
```

Fourth, create the templates in “/hello\_web/templates/upload/index.html.eex”

```
<%= form_for @conn, "/upload", [as: :upload, multipart: true], fn f -> %>

  <div class="form-group">
    <label>Document</label>
    <%= file_input f, :docfile, class: "form-control" %>
  </div>

  <div class="form-group">
    <%= submit "Submit", class: "btn btn-primary" %>
  </div>
<% end %>
```

Finish! Now you can access the upload page and test to upload some file and see how it’s stored in “upload” folder in the project. Yes, you need to create a new folder call “uploads” in root in this case.

You also can visit the example of project via github in here: [https://github.com/yodiaditya/phoenix-upload-file-example](https://github.com/yodiaditya/phoenix-upload-file-example)
