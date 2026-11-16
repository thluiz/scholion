---
url: "https://poeticoding.com/creating-thumbnails-of-uploaded-images-and-pdf-in-phoenix"
captured_at: "2026-11-16T04:16:09+00:00"
title: "Creating Thumbnails of uploaded Images and PDF in Phoenix · Poeticoding"
domain: "poeticoding-com"
---

*   Part 1: [Step-by-Step Tutorial to Build a Phoenix App that Supports User Upload](https://poeticoding.com/step-by-step-tutorial-to-build-a-phoenix-app-that-supports-user-uploads/)
*   Part 2: this article
*   Part 3: [Add a Progress Bar in the Phoenix File Upload app](https://poeticoding.com/add-a-progress-bar-in-the-phoenix-file-upload-app/)

In [Step-by-Step Tutorial to Build a Phoenix App that Supports User Upload](https://poeticoding.com/step-by-step-tutorial-to-build-a-phoenix-app-that-supports-user-uploads/) we’ve built from scratch a Phoenix application where users can upload and download their files. We saw how to deal with uploads, saving them locally, using Ecto and Postgres database to save file’s details like size, filename, hash etc.

We are now going to add a new layer, where we create thumbnails for image and PDF files.

Let’s see quickly how to get [the previous part’s code](https://github.com/poeticoding/phoenix_uploads_articles/tree/df18b03800df06c15b12791f21f559ebdc92f0d2) up and running, so we can start building from it. If you already have everything setup, you can skip this part and go directly to [ImageMagick](#imagemagick).

```
$ git clone git@github.com:poeticoding/phoenix_uploads_articles.git

$ cd phoenix_uploads_articles 
$ git checkout tags/part-1
```

To be on the same page, once cloned the repository, let’s checkout to the commit with tag `part-1`, which is the situation at the end of [previous article](https://poeticoding.com/step-by-step-tutorial-to-build-a-phoenix-app-that-supports-user-uploads/).

We then need to get the app dependencies and build the javascript and css assets.

```
$ mix deps.get && mix deps.compile
$ cd assets && npm install && \
  node node_modules/webpack/bin/webpack.js \
  --mode development
```

We need a Postgres server up and running, where we save the uploaded files details. In [Postgres using Docker](https://poeticoding.com/step-by-step-tutorial-to-build-a-phoenix-app-that-supports-user-uploads/#postgres-docker) you can see in detail how to run a Postgres server with Docker on your local machine.

Once the the Postgres server is ready, we can create the database and `uploads` table using the Ecto mix tasks.

```
$ mix ecto.create
Generated poetic app
The database for Poetic.Repo has been created

$ mix ecto.migrate
[info] == Running 20190412141226 Poetic.Repo.Migrations.CreateUploads.change/0 forward
[info] create table uploads
[info] create index uploads_hash_index
[info] == Migrated 20190412141226 in 0.0s
```

One last thing - at the bottom of `config/dev.exs` you find the `uploads_directory` option set to my local directory `/Users/alvise/uploads_dev`. It’s important you create a folder where to store the uploads (better outside the project’s directory) and set the absolute path in the configuration file. You could also set it using an environment variable (which is the best way in production).

We are now ready to run the Phoenix server and upload a file.

```
$ mix phx.server
[info] Running PoeticWeb.Endpoint with cowboy 2.6.3 at 0.0.0.0:4000 (http)
[info] Access PoeticWeb.Endpoint at http://localhost:4000
...
```

![uploading a file](https://poeticoding.com/creating-thumbnails-of-uploaded-images-and-pdf-in-phoenix/upload_to_phoenix.gif)

Uploading files

## ImageMagick

To create images’ and PDF’s thumbnails, we need to install [ImageMagick](https://imagemagick.org/). If you never used ImageMagick before, it’s one of the most famous and used tools to process images on a web backend. We will use it to read any image format and convert it to a resized jpeg that we can display in the uploads page.

On my mac I’ve installed it using [H](https://brew.sh/)[o](https://brew.sh/)[mebrew](https://brew.sh/), this is definitely the easiest way to install it on macOS.

```
$ brew install imagemagick
$ magick --version
Version: ImageMagick 7.0.8-44 Q16 x86_64 ...
...
```

If you are on linux, it depends which distribution you are using. You can install it using the binaries available on the ImageMagick website, [Unix Binary Release](https://imagemagick.org/script/download.php#unix). If you are using Debian or Ubuntu you can use `apt-get`

```
# Ubuntu 18.04
$ apt-get install imagemagick
$ mogrify -version
Version: ImageMagick 6.9.7-4 Q16 x86_64 20170114
...
```

Ubuntu 18.04, for example, has a slightly older ImageMagick version, which is not an issue for what we need to do.

ImageMagick 6.9 doesn’t have the `magick` command like in the Mac installation. To check the version you can run the `mogrify` command, which is one of the ImageMagick tools and the one we’ll use to create thumbnails.

## Create thumbnails with Mogrify in Elixir

[Mogrify](https://hex.pm/packages/mogrify) is a wrapper around the ImageMagick `mogrify` command, which brings a great Elixir-like experience on processing images. We add it in our `mix.exs` under `deps`

```
$ mix deps.get
Resolving Hex dependencies...
Dependency resolution completed:
...
  mogrify 0.7.2
...
```

The only Mogrify’s dependency is ImageMagick, which we’ve already installed.

You can download the `phoenix_uploads.png` image and save it into the `assets/static/images/` folder, so you can use it do some resizing experiments in the Elixir’s interactive shell `iex`.

```
$ iex -S mix
iex> Mogrify.open("assets/static/images/phoenix_uploads.png") \
...> |> Mogrify.resize_to_limit("300x300") \
...> |> Mogrify.save(path: "phoenix_uploads_thumb.jpg")
%Mogrify.Image{
  animated: false,
  buffer: nil,
  dirty: %{},
  ext: ".jpg",
  format: nil,
  frame_count: 1,
  height: nil,
  operations: [],
  path: "phoenix_uploads_thumb.jpg",
  width: nil
}
```

*   with `resize_to_limit("300x300")` the image is resized maintaining proportions, limiting the width and hight to a maximum of 300 pixels.
*   with `Mogrify.save(path: "phoenix_uploads_thumb.jpg")` we start the processing. The library at this point runs the ImageMagick `mogrify` command. With the `:path` option we specify the path where we want to store the file, and using a different extension (like _.jpg_ in this case) the image is converted to the new image format.

We find our resized image in the root directory of the project. We can use `Mogrify` to check `width` and `hight` of this new image.

```
iex> ls
...
phoenix_uploads_thumb.jpg

iex> Mogrify.open("phoenix_uploads_thumb.jpg") \
...> Mogrify.verbose()
%Mogrify.Image{
  ...
  ext: ".jpg",
  format: "jpeg",
  height: 199,
  width: 300
  path: ...
}
```

## `thumbnail?` field in Upload Ecto Schema

The user should be able to upload any file format, but we can create thumbnails just for images and PDF. We need then to have a new field in Upload schema reflecting a boolean column in our database, where we store if the upload has a thumbnail or not.

We are going to _alter_ the current _uploads_ database table, adding a new `has_thumb` boolean column. To do so, we generate a new Ecto migration

```
$ mix ecto.gen.migration add_uploads_has_thumb
* creating priv/repo/migrations/20190514143331_add_uploads_has_thumb.exs
```

The task creates a migration template file with an empty `change` function we need to fill.

```
# priv/repo/migrations/20190514143331_add_uploads_has_thumb.exs
defmodule Poetic.Repo.Migrations.AddUploadsHasThumb do
  use Ecto.Migration

  def change do
    alter table(:uploads) do
      add :has_thumb, :boolean, default: false
    end
  end
end
```

In this way we alter the _uploads_ table adding the `has_thumb` column. All the existing records will have this value set to `false`.

To apply this migration we run the migration task

```
$  mix ecto.migrate
[info] == Running 20190514143331 Poetic.Repo.Migrations.AddUploadsHasThumb.change/0 forward
[info] alter table uploads
[info] == Migrated 20190514143331 in 0.0s
```

Let’s add the new `thumbnail?` field in the _uploads_ schema defined in the `Poetic.Documents.Upload` [module](https://github.com/poeticoding/phoenix_uploads_articles/blob/part-2/lib/poetic/documents/upload.ex), mapping this field to the `has_thumb` column, using the `:source` option

```
# lib/poetic/documents/upload.ex
defmodule Poetic.Documents.Upload do
  schema "uploads" do
    ...
    field :thumbnail?, :boolean, source: :has_thumb
    ...
  end
end
```

## Upload module and changeset

After adding the `thumbnail?` field to the schema, it’s now time to write the functions where we create the thumbnail and update the upload database record.

Let’s start from the `Upload.changeset/2` function. As it is, if we try to change the `thumbnail?` value, nothing happens

```
iex> alias Poetic.Documents.Upload
iex> Upload.changeset(%Upload{},%{thumbnail?: true})
#Ecto.Changeset<
  action: nil,
  changes: %{},
  ...
>
```

We need to add the `:thumbnail?` atom to the valid fields passed to `cast`

```
# lib/poetic/documents/upload.ex
def changeset(upload, attrs) do
  upload
  |> cast(attrs, [:filename, :size, :content_type, 
          :hash, :thumbnail?])
  ...
end

# on iex
iex> Upload.changeset(%Upload{}, %{thumbnail?: true})
#Ecto.Changeset<
  action: nil,
  changes: %{thumbnail?: true},
  ...
>
```

## Thumbnails path

Now, where do we store our thumbnails?

We could store them in `priv/static/images` directory of the project, in this way we would use the `Plug.Static` plug that serves static assets. Just copying the the image into the `priv/static/images` directory, the thumbnail could be downloaded at the URL `http://localhost:4000/images/thumbnail_filename.jpg`. In this way is really easy to serve new images. `Plug.Static` also uses etags for HTTP caching.

But we go in a different direction, saving thumbnails into the same directory where we store the uploaded files. In this way we put everything together and we can have a better control on serving these thumbnails based on user’s permission.

Let’s now define a `thumbnail_path/1` function that returns a valid and unique absolute path for our thumbnail

```
# lib/poetic/documents/upload.ex
def thumbnail_path(id) do
  [@upload_directory, "thumb-#{id}.jpg"]
  |> Path.join()
end
```

As we did for the `local_path/2`, we use the `id` to uniquely identify the thumbnail. In general it’s a good idea to have a dedicated directory for each single upload - in this way we can have the freedom to group multiple files that refer to the same upload, without overcrowding the uploads directory. Since this adds a bit of complexity (for example creating a directory for each upload), we save the thumbnails directly in the `@upload_directory`.

## Image’s thumbnail

To generate thumbnails we use a `Mogrify` code similar to what we’ve tried before on iex

```
# lib/poetic/documents/upload.ex
 def mogrify_thumbnail(src_path, dst_path) do
   try do
     Mogrify.open(src_path)
     |> Mogrify.resize_to_limit("300x300")
     |> Mogrify.save(path: dst_path)
   rescue
     File.Error -> {:error, :invalid_src_path}
     error -> {:error, error}
   else
     _image -> {:ok, dst_path}
   end
 end
```

In general I prefer to avoid the `try/rescue` construct to handle errors, it’s usually better to pattern match `{:error, _}` `{:ok, _}` tuples.

The `Mogrify.open/1` function raises a `File.Error` when the source image file doesn’t exist, so we need to use `try/rescue` to properly handle the error and return a tuple.

At the moment, with the current Mogrify (version 0.7.2) , `Mogrify.save/2` doesn’t return or raise an error if it fails, which is not something that can be left to fate. We will see later, when creating thumbnails for PDF files, how to run ImageMagick commands in Elixir handling open and save errors.

Using pattern matching we can define a `create_thumbnail/1` function for each `content_type` we want. We start with _image_ content type to support different image formats (`image/png, image/jpg` etc.)

```
# lib/poetic/documents/upload.ex

def create_thumbnail(%__MODULE__{
  content_type: "image/" <> _img_type
}=upload) do

  original_path = local_path(upload.id, upload.filename)
  thumb_path = thumbnail_path(upload.id)
  {:ok, _} = mogrify_thumbnail(original_path, thumb_path)

  changeset(upload, %{thumbnail?: true})
end

def create_thumbnail(%__MODULE__{}=upload), 
	do: changeset(upload, %{})
```

The function arguments is an `%Upload{}` struct, with `content_type` starting with `image/`. We use the `id` and `filename` fields to get the original file path and `thumbnail_path/1` function to get the destination path.

For simplicity, we expect that `mogrify_thumbnail/2` returns a `{:ok, _}` tuple - when it returns `{:error, _}` a `MatchError` is raised. If unhandled, it can lead to a _HTTP 500 Internal Server Error_ error message that is shown to the user. There are many ways of handling these type of errors: we could silently fail and set a generic thumbnail, or return an Ecto Changeset with an error on the `thumbnail?` field etc. At the end it depends on how we want our app to behave in these situations.

At the function’s last line, we convert the upload struct to an Ecto changeset, setting the `thumbnail?` value to `true`. This function doesn’t apply any change to the upload’s record - to persist this change we will pass the changeset to `Repo.update/1` function.

The second `create_thumbnail/1` it’s a catchall clause. It handles the cases where the file is not an image. It just returns a changeset with no changes.

## Documents context

Now that we have everything we need to create our thumbnail, we just need to decide in which part of the code we want to generate it.

The easiest way is adding a new step inside the `Documents.create_upload_from_plug_upload/1` function. We append a new step to the `with` in the transaction.

```
# lib/poetic/documents.ex
defmodule Poetic.Documents do

  def create_upload_from_plug_upload(%Plug.Upload{...}) do
    ...
    
	with ...,
	 {:ok, upload} <- 
		 ... |> Repo.insert(),
	 ...
     {:ok, upload} <- 
	     Upload.create_thumbnail(upload) |> Repo.update() 
    do
      ...
    else
      ...
    end

    ...
  end
end
```

If we now run our app and upload an image, we still don’t see any thumbnail shown in the uploads page - but looking inside the uploads folder, we see that the thumbnail has been successfully created during the upload process.

![Thumbnail creation working correctly](https://poeticoding.com/creating-thumbnails-of-uploaded-images-and-pdf-in-phoenix/create_thumbnail_working.gif)

Thumbnail creation working correctly

## Serve and show the thumbnails

We’ve just seen that the `Documents` context successfully creates thumbnails for image files, but these aren’t shown in the uploads page. Since thumbnail images are in the uploads directory, to serve them we need first to add a route in the [router](https://github.com/poeticoding/phoenix_uploads_articles/blob/part-2/lib/poetic_web/router.ex#L22) and an action in the `PoeticWeb.UploadController`.

```
# lib/poetic_web/router.ex
...
scope "/", PoeticWeb do
  resources "/uploads", UploadController, only: [:index, :new, :create, :show] do
    get "/thumbnail", UploadController, :thumbnail, as: "thumbnail"
  end
end
```

```
$ mix phx.routes
...
upload_thumbnail_path  GET  /uploads/:upload_id/thumbnail \
      PoeticWeb.UploadController :thumbnail
...
```

Inside the uploads resources, we define a `get` route, which points to the `UploadController.thumbnail` action.

With `mix phx.routes` we see that the new route is listed and the `upload_thumbnail_path` helper is created. Notice that the key used to the pass the id in the parameters is now `upload_id`.

In the `UploadController` we write the `thumbnail/2` function

```
# lib/poetic_web/controllers/upload_controller.ex
def thumbnail(conn, %{"upload_id" => id}) do
  thumb_path = Upload.thumbnail_path(id)

  conn
  |> put_resp_content_type("image/jpeg")
  |> send_file(200, thumb_path)
end
```

We pattern match the `upload_id` and get the thumbnail path. We then set the content type to _image/jpeg_ and send the file to the client. We can see immediately if it works, uploading a file and making a GET request with the browser

![GET /uploads/1/thumbnail](https://poeticoding.com/creating-thumbnails-of-uploaded-images-and-pdf-in-phoenix/http_get_thumbnail.jpg)

GET /uploads/1/thumbnail

Let’s now change the `lib/poetic_web/templates/upload/index.html.eex` file to show the thumbnail in the list

```
<%= for upload <- @uploads do %>

<tr>
  <td>
    <%= if upload.thumbnail? do 
      img_tag Routes.upload_thumbnail_path(@conn, :thumbnail, upload.id)
    else
      img_tag "/images/generic_thumbnail.jpg"
    end %>
  </td>
	    
  <td>...</td>
    
</tr>

<% end %>
```

*   If the upload has a thumbnail, we show the thumbnail using `img_tag` and the `upload_thumbnail_path` helper (which returns the path to get the thumbnail for the given upload id).
*   in the case it hasn’t a thumbnail, we show a generic thumbnail placed in `assets/static/images`.

![](https://poeticoding.com/creating-thumbnails-of-uploaded-images-and-pdf-in-phoenix/uploads_with_thumbnails-1.jpg)

## PDF’s thumbnail

Until now, we’ve just focused on thumbnail of images. In the case of PDF files, we can create a thumbnail of the first page.

The best tool to create an image from a page of a PDF is the ImageMagick’s `convert` command, which isn’t covered by the Mogrify wrapper.

So we need to build our Elixir function that runs the `convert` command, based on `System.cmd/3`.

First, let’s see how we create a PDF’s thumbnail

```
# on linux/mac/unix
$ convert -density 300 -resize 300x300 \
  'programming-phoenix.pdf[0]' \
  'pdf_thumb.jpg'
```

The `[0]` after the pdf path is used to choose which page we want to convert, starting from 0.

If `convert` returns an error like `convert: no images defined` it could be related to a an issue of `ghostscript` 9.26, which is used to process PDFs. To temporarily fix this issue, waiting for the next version, I’ve downgraded ghostscript to version 9.25.

```
# on mac
$ brew uninstall ghostscript
$ brew install https://raw.githubusercontent.com/Homebrew/homebrew-core/b0b6b9495113b0ac5325e07d5427dc89170f690f/Formula/ghostscript.rb
```

On Windows, from ImageMagick 7, the command is a little different. We need to prepend the `magick`

```
> magick.exe convert ...
```

![Thumbnail of a PDF](https://poeticoding.com/creating-thumbnails-of-uploaded-images-and-pdf-in-phoenix/pdf_thumbnail_preview.jpg)

Thumbnail of a PDF

```
# lib/poetic/documents/upload.ex
def pdf_thumbnail(pdf_path, thumb_path) do
  args = ["-density", "300", "-resize", 
          "300x300","#{pdf_path}[0]", 
          thumb_path]

  case System.cmd("convert", args, stderr_to_stdout: true) do
    {_, 0} -> {:ok, thumb_path}  
    {reason, _} -> {:error, reason}
  end
end
```

The arguments are passed to `System.cmd/3` as a list and we enable the `stderr_to_stdout` option to catch anything printed by the command.

*   in the case `convert` exits with `0`, it means the thumbnail was created correctly.
*   for any other exit code, we return `{:error, reason}` where `reason` is the command’s output string

If we try to make it fail, providing an invalid PDF path, we get an `{:error, reason}` tuple as expected.

```
iex> Poetic.Documents.Upload.pdf_thumbnail(
  "invalid.pdf", "thumb.jpg"
)

{:error,
 "convert: unable to open image 'invalid.pdf': No such file or  directory @ error/blob.c/OpenBlob/3497.\nconvert: no images defined `thumb.jpg' @ error/convert.c/ConvertImageCommand/3300.\n"}
```

Since we are catching all the output on `stdout` and `stderr`, the error string could be a bit too verbose. We can process the string, for example getting just the first line until the `@` symbol.

Same for an invalid output path

```
iex> Poetic.Documents.Upload.pdf_thumbnail(
  "programming-phoenix.pdf", 
  "/tmp/invalid/thumb.jpg")

{:error,
 "convert: unable to open image '/tmp/invalid/thumb.jpg': No such file or directory @ error/blob.c/OpenBlob/3497.\n"}
```

We can now use this function to extend the support to the `application/pdf` content type.

```
# lib/poetic/documents/upload.ex
def create_thumbnail(%__MODULE__{
  content_type: "application/pdf"
}=upload) do
	original_path = local_path(upload.id, upload.filename)
	thumb_path = thumbnail_path(upload.id)
	{:ok, _} = pdf_thumbnail(original_path, thumb_path)
	changeset(upload, %{thumbnail?: true})
end
```

We see that once added this new `create_thumbnail` clause into Upload module, the PDF’s thumbnails are created and shown successfully

![Uploaded PDFs with thumbnails](https://poeticoding.com/creating-thumbnails-of-uploaded-images-and-pdf-in-phoenix/uploaded_pdf_with_thumbnails.jpg)

Uploaded PDFs with thumbnails

### Full code of this part

You can find the full code of this article on the [poeticoding/phoenix\_uploads\_articles](https://github.com/poeticoding/phoenix_uploads_articles/tree/part-2) GitHub repo.
