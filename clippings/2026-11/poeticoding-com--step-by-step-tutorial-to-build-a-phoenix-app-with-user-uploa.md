---
url: "https://poeticoding.com/step-by-step-tutorial-to-build-a-phoenix-app-that-supports-user-uploads"
captured_at: "2026-11-16T04:15:55+00:00"
title: "Step-by-Step Tutorial to Build a Phoenix App that Supports User Upload · Poeticoding"
domain: "poeticoding-com"
---

*   Part 1: this article
*   Part 2: [Creating Thumbnails of uploaded Images and PDF in Phoenix](https://poeticoding.com/creating-thumbnails-of-uploaded-images-and-pdf-in-phoenix/)
*   Part 3: [Add a Progress Bar in the Phoenix File Upload app](https://poeticoding.com/add-a-progress-bar-in-the-phoenix-file-upload-app/)

There are many ways to let users upload their files to our Phoenix app, including reliable libraries that manage the uploads for us, saving the files securely on cloud storage.

However, in this guide we will focus on the foundation - we will only use the tools shipped with Phoenix, rather than third-party libraries.

We will create a fully-functional Phoenix app from scratch, running and configuring our Postgres database and Ecto schemas, handling uploads with Plug and storing the files locally.

Once we’ve done this, we’ll able to download the files.

Now, let’s get to coding! 👩‍💻👨‍💻

Let’s start by creating a new Phoenix 1.4 application called _poetic_

```
$ mix phx.new poetic && cd poetic
```

Once created, make sure the dependencies are correctly downloaded

```
$ mix deps.get
Resolving Hex dependencies...
```

We need [Node.js](https://nodejs.org/) in our system so we can build the assets inside the `assets` directory. I find [nvm](https://github.com/creationix/nvm) is pretty useful and easy to use if you need to handle different node versions on the same machine.

If you just want to compile these assets, you can download the installer of the latest version from the [Node.js website](https://nodejs.org/). Once you’ve installed the latest version of Node.js, you can build the assets using the `npm install` and `webpack.js` commands

```
$ cd assets && npm install && \
node node_modules/webpack/bin/webpack.js --mode development
```

## Postgres 🐘 using Docker 🐳

The Phoenix app we’ve just created comes with [Ecto](https://hexdocs.pm/ecto/Ecto.html), which helps us to deal with relational databases like [PostgreSQL](https://www.postgresql.org/). A database is necessary to store details about the uploaded files.

I think that, in this case, using Docker is the easiest and fastest way to get a PostgreSQL database up and running on our local system.

If you’re not sure how to use Docker, you can take a look at [How to run a Docker Container](https://poeticoding.com/how-to-run-a-docker-container/) resource, to gain an initial understanding of how to run docker containers.

First, we create a docker volume, to keep the database data persistent

```
$ docker volume create poetic-postgres`
```

With a volume we can safely destroy and recreate a container without incurring any data loss.

We then launch a container running the [official Postgres docker image](https://hub.docker.com/_/postgres), version _11-alpine_.

```
$ docker container run --name postgres -p 5432:5432 \
  -e POSTGRES_PASSWORD=postgres \
  -v poetic-postgres:/var/lib/postgresql/data \
  --rm postgres:11-alpine

LOG:  listening on IPv4 address "0.0.0.0", port 5432
LOG:  database system is ready to accept connections
```

We’ve started a Postgres server with these options:

*   `-p 5432:5432`  
    It means `--publish port_local_machine:port_container`. The port in the local machine is opened and the connection is forwarded to the container port.
*   `-e POSTGRES_PASSWORD=postgres`  
    We pass the environment variable `POSTGRES_PASSWORD` to set the password `postgres` to the default `postgres` user.
*   `-v poetic-postgres:/var/lib/postgresql/data`  
    We mount the docker volume we’ve created before to the _/var/lib/postgresql/data_ directory, which is the directory Postgres uses to store its data.
*   `--name postgres`  
    The name we give to the container which we can use later to refer to it.
*   `--rm`  
    Once stopped, the container is removed automatically while the volume is preserved.

To remove the container, given it was launched with the `--rm` option, we simply need to stop it and it will be removed automatically. We can press `CTRL+C` in the terminal where we started _postgres_. Alternatively, using another terminal we can stop the container with the command:

```
$ docker container stop postgres
```

When the container is removed the volume is not deleted.

We can use the same `docker container run ...` command we used before to start a new _postgres_ container, using the same volume and this will restore the old data.

## Configuration

### Ecto configuration

Now that our Postgres server is up and running, we need to configure the Phoenix app to connect to the database.

Let’s take a look at `config/dev.exs`, where we find our [Ecto Repo](https://hexdocs.pm/ecto/Ecto.Repo.html) configuration

```
# config/dev.exs
...
config :poetic, Poetic.Repo,
	username: "postgres",
	password: "postgres",
	database: "poetic_dev",
	hostname: "localhost",
	pool_size: 10
```

By default, this configuration matches the username, password and hostname of our server, so we don’t need to touch it.

However, at the moment there is no _poetic\_dev_ database in our Postgres. To create it, let’s run this ecto task on the terminal

```
$ mix ecto.create
The database for Poetic.Repo has been created
```

This creates the _poetic\_dev_ database.

If you haven’t seen the `Poetic.Repo` module yet, it’s the module we use to run queries to the database and which inherits the [Ecto.Repo](https://hexdocs.pm/ecto/Ecto.Repo.html) functions (`insert`, `get`, …)

```
# lib/poetic/repo.ex
defmodule Poetic.Repo do
  use Ecto.Repo,
    otp_app: :poetic,
    adapter: Ecto.Adapters.Postgres
end
```

### Uploads directory

Let’s now add a configuration to set the absolute path of the _uploads directory_, outlining where we’re going to locally store the uploads, in this case for the dev environment.

```
# config/dev.exs
config :poetic,
   uploads_directory: "/Users/alvise/uploads_dev"
```

I prefer to keep the _uploads directory_ out of the Phoenix app folder, so in my case, I’ve created an _uploads\_dev_ folder in my home directory.

If we then want to use this app in production - and we want to take advantage of cloud storage instead of refactoring it to use S3 (which is obviously a great option!) - we could use a service like [AWS EFS](https://aws.amazon.com/efs/) where we mount a network filesystem in a directory of our cloud server.

We then just need to set the production configuration to use the mounted network file-system

```
# config/prod.exs
config :poetic,
  uploads_directory: System.get_env("POETIC_UPLOADS_DIRECTORY") || "/uploads"
```

In production, like in this case, it’s usually better to use environment variables to pass our settings to a configuration file.

## Upload module

We could use the `phx.gen.html` generator which creates schema, migration, context, controller, view, test and html files for us.

However, I find the generated scaffold a bit too much for what we need. Instead, I like to use this generator to learn more about the phoenix patterns, observing how the components are supposed to be used together.

The only generator we are going to use here is to create the Ecto schema and migration. We’ll manually create the remaining necessary files.

### Ecto schema and migration

Once the user has uploaded a file, we want to save different information about it into our database. Let’s generate _schema_ and _migration_ files for the upload using the `phx.gen.schema` task

```
$ mix phx.gen.schema Documents.Upload uploads \
filename:string size:integer \
content_type:string hash:string 

* creating lib/poetic/documents/upload.ex
* creating priv/repo/migrations/20190412141226_create_uploads.exs
```

The first parameter `Documents.Upload` is the schema name, which creates a `Poetic.Documents.Upload` module, where `Documents` is our context (we will see more about this later).

`uploads` is the table that will be created in the database.

The remaining parameters define the fields in the schema and columns in the migration file.

Let’s take a look first at the migration file

```
# priv/repo/migrations/20190412141226_create_uploads.exs

defmodule Poetic.Repo.Migrations.CreateUploads do
  use Ecto.Migration

  def change do
    create table(:uploads) do
      add :filename, :string
      add :size, :integer
      add :content_type, :string
      add :hash, :string

      timestamps()
    end
  end
end
```

This file reflects the changes we want to do in our database, creating the `uploads` table with `filename`, `size`, `content_type` and `hash` columns. By default Ecto also creates the `id` column, which is the primary key.

With `timestamps()` Ecto adds two _timestamp_ columns, `inserted_at` and `updated_at`, which are managed automatically for us each time we insert or update a record in the table.

Let’s make a few small changes to our migration

```
create table(:uploads) do
	...
	add :size, :bigint
	add :hash, :string, size: 64
	...
end

create index(:uploads, [:hash])
```

The first thing we’ve changed is the `size` column’s type. The [`integer`](https://www.postgresql.org/docs/10/datatype-numeric.html) Postgres type is an integer between _\-2147483648_ and _+2147483647_. To save a value bigger than 2GB, we need a `bigint` - which is plenty of space to store the kind of file we need to handle in our app (up to 8192 Petabytes!).

To hash the file, the algorithm we are going to use is SHA-256, where the hexadecimal digest is a 64-character string. We’ve set the size of the string using the `size: 64` option and created an index on this column with `create index(:uploads, [:hash])`, so if we need to search for files using the hash, the search will be much faster.

Now let’s take a look at the Upload Ecto schema file, which is used to map the database record into an Elixir struct.

```
# lib/poetic/documents/upload.ex
defmodule Poetic.Documents.Upload do
  use Ecto.Schema
  import Ecto.Changeset

  schema "uploads" do
    field :content_type, :string
    field :filename, :string
    field :hash, :string
    field :size, :integer

    timestamps()
  end
  
end
```

The fields in the schema are fields of the `%Poetic.Documents.Upload{}` struct. They map the database type (like _bigint_, _varchar_, etc.) to an Elixir type (_integer_, _string_, etc.).

```
iex> alias Poetic.Documents.Upload
iex> %Upload{}
%Poetic.Documents.Upload{
  __meta__: #Ecto.Schema.Metadata<:built, "uploads">,
  content_type: nil,
  filename: nil,
  hash: nil,
  id: nil,
  inserted_at: nil,
  size: nil,
  updated_at: nil
}
```

In this module we also find the `changeset/2` function, where we set our validation rules and the required fields.

```
# lib/poetic/documents/upload.ex
defmodule Poetic.Documents.Upload do
  ...
  def changeset(upload, attrs) do
    upload
    |> cast(attrs, [:filename, :size, :content_type, :hash])
    |> validate_required([:filename, :size, :content_type, :hash])

    # added validations
    |> validate_number(:size, greater_than: 0) #doesn't allow empty files
    |> validate_length(:hash, is: 64)
  end
end
```

We’ve added two other validations:

*   `validate_number(:size, greater_than: 0)`  
    Checks that the given size is greater than 0 (no empty files).
*   `validate_length(:hash, is: 64)`  
    Checks that the hash is a 64 characters string.

It’s now time to create the `uploads` table by running the migration task

```
$ mix ecto.migrate
[info] == Running 20190412141226 Poetic.Repo.Migrations.CreateUploads.change/0 forward
[info] create table uploads
[info] == Migrated 20190412141226 in 0.0s
```

To see if everything was created correctly, we can use the `psql` client in the running _postgres_ Docker container

```
$ docker container exec -it postgres psql -U postgres
psql (10.7)
Type "help" for help.

postgres=# \l
                                  List of databases
    Name     |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges
-------------+----------+----------+------------+------------+-----------------------
 poetic_dev  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |
...
postgres=# \c poetic_dev
You are now connected to database "poetic_dev" as user "postgres".

postgres=# \d
 Schema |       Name        |   Type   |  Owner
--------+-------------------+----------+----------
 public | schema_migrations | table    | postgres
 public | uploads           | table    | postgres
 public | uploads_id_seq    | sequence | postgres

postgres=# \d+ uploads
    Column    |              Type              
--------------+--------------------------------
 id           | bigint                         
 filename     | character varying(255) 
 size         | integer                        
 content_type | character varying(255)         
 hash         | character varying(64)         
 inserted_at  | timestamp(0) without time zone 
 updated_at   | timestamp(0) without time zone 
 Indexes:
    "uploads_pkey" PRIMARY KEY, btree (id)
    "uploads_hash_index" btree (hash)
```

Then, we run _iex_ and use _Ecto_ and _Upload_ to create a record

```
poetic$ iex -S mix

iex> alias Poetic.Repo
iex> alias Poetic.Documents.Upload
iex> %Upload{} \
...> |> Upload.changeset(%{
	filename: "image.jpg", 
	content_type: "image/jpeg",
	hash: String.duplicate("a",64), #fake hash
	size: 1_000
}) |> Repo.insert()

[debug] QUERY OK db=2.4ms decode=0.8ms queue=0.8ms
INSERT INTO "uploads" ...

{:ok, %Poetic.Documents.Upload{id: 1, ...}
```

`Upload.changeset/2` returns an `Ecto.Changeset` which is passed to the `Repo.insert/2` function to create the upload record in the database.

### SHA-256 function

Using what we’ve seen in [Hashing a File in Elixir](https://poeticoding.com/hashing-a-file-in-elixir/), we add the `sha256(chunks_enum)` function in the `Poetic.Documents.Upload` module. This calculates and returns the SHA-256 hexadecimal digest of the given stream.

```
# lib/poetic/documents/upload.ex
defmodule Poetic.Documents.Upload do
  ...
  def sha256(chunks_enum) do
    chunks_enum
    |> Enum.reduce(
        :crypto.hash_init(:sha256),
        &(:crypto.hash_update(&2, &1))
    ) 
    |> :crypto.hash_final()
    |> Base.encode16()
    |> String.downcase()
  end
end
```

To calculate the hash of a file we can use the following method

```
iex> File.stream!("assets/static/images/phoenix.png", [], 2048) \
...> |> Poetic.Documents.Upload.sha256()
"07aa9b01595fe10..."
```

### local\_path

Now, we need a simple function that tells us where to store the file, once received.

```
# lib/poetic/documents/upload.ex
defmodule Poetic.Documents.Upload do
  @upload_directory Application.get_env(:poetic, :uploads_directory)

  def local_path(id, filename) do
    [@upload_directory, "#{id}-#{filename}"]
    |> Path.join()
  end
end
```

This function returns an _absolute path_, placing the file in the uploads directory we defined previously in `config/dev.exs`.

There are several ways to make the path unique; in this case we just add the `id` (primary key of the upload’s database record) to the beginning of the filename.

In general, if we have many uploads, it’s not a good idea to save them all in one directory. A better practice would be to use an upload feature, such as the creation date, to produce a directory hierarchy, for example `"2019/04/15/#{id}-#{filename}"`.

**UPDATE** based on the conversation in the comments section below (I’ve also updated the git repo): if we use the `@upload_directory` module attribute, the function `Application.get_env(:poetic, :uploads_directory)` is evaluated at compile time and whatever is returned from this function can’t be changed in the future. This makes difficult to use the same compiled app with different production settings - if we want to change the upload directory we have to recompile the whole app, which is quite annoying.

To fix it, we just need to define and use a function instead

```
def upload_directory do
  Application.get_env(:poetic, :uploads_directory)
end

def local_path(id, filename) do
  [upload_directory(), "#{id}-#{filename}"]
  |> Path.join()
end
```

Now the `Application.get_env/2` is evaluated at runtime and it returns the value set in the configuration file, passed via the environment variable `POETIC_UPLOADS_DIRECTORY`.

## UploadController

In the `PoeticWeb.UploadController` controller we are going to implement the functions to answer the following HTTP requests:

*   `GET /uploads/new` Render a page with a form to upload our file
*   `POST /uploads` Receive the upload and stores it locally
*   `GET /uploads` List the uploaded files
*   `GET /uploads/:id` Download a file

We start by changing our `PoeticWeb.Router` router, using `resources` to match the HTTP requests to the controller actions

```
# lib/poetic_web/router.ex
defmodule PoeticWeb.Router do
	...
	
  scope "/", PoeticWeb do
    pipe_through :browser
    
    resources "/uploads", UploadController, only: [:index, :new, :create, :show]
  end
end
```

Using the `phx.routes` mix task we can list all the routes

```
$ mix phx.routes
...
upload_path  GET   /uploads         PoeticWeb.UploadController :index
upload_path  GET   /uploads/new     PoeticWeb.UploadController :new
upload_path  GET   /uploads/:id     PoeticWeb.UploadController :show
upload_path  POST  /uploads         PoeticWeb.UploadController :create
```

And now the _uploads_ routes should be listed.

### :new action

To start writing the `UploadController` we must create a new file `lib/poetic_web/controllers/upload_controller.ex` in which we define the `PoeticWeb.UploadController` module

```
# lib/poetic_web/controllers/upload_controller.ex

defmodule PoeticWeb.UploadController do
  use PoeticWeb, :controller

  def new(conn, _params) do
    render(conn, "new.html")
  end
end
```

The `new/2` function renders the `new.html` template, where we are going to write our upload form.

This template file has to be called [new.html.eex](https://github.com/poeticoding/phoenix_uploads_articles/blob/d67c4b2495a75410f7cc497a6df2dd54be37cc03/lib/poetic_web/templates/upload/new.html.eex) and placed in `lib/poetic_web/templates/upload` (where _upload_ is the lowercase name of the controller).

```
<%= form_for @conn, Routes.upload_path(@conn, :create), 
                    [multipart: true], fn f-> %>

    <%= file_input f, :upload, class: "form-control" %>
    <%= submit "Upload", class: "btn btn-primary" %>

<% end %>
```

This _EEx_ template creates a **multipart** form where the user can choose the file to send. When the user submits the form, it will make a `POST /uploads` request (action returned by `Routes.upload_path(@conn, :create)`).

To render the template, we need a view for this controller. Phoenix assumes a strong naming convention from controllers, to views, to the templates they render. The `UploadController` requires a `UploadView` to render templates in the `lib/poetic_web/templates/upload` directory.

```
defmodule PoeticWeb.UploadView do
  use PoeticWeb, :view
end
```

Before testing our code, let’s first add the `create/2` function to the controller and inspect what the form sends to the action

```
defmodule PoeticWeb.UploadController do
  ...
	
  def create(conn, %{"upload" => %Plug.Upload{}=upload}) do
    IO.inspect(upload, label: "UPLOAD")
    text conn, "ok"
  end

end
```

We expect an `upload` key in the params, with a `%Plug.Upload{}` struct which holds our uploaded file.

[Plug](https://github.com/elixir-plug/plug) manages the upload for us, saving the data in a temporary file that we find in the `path` field of the struct; when the request terminates, the temporary file is automatically deleted.

It’s time to run the Phoenix server to test the upload.

To see the form, we need to go to _http://localhost:4000/uploads/new_

```
$ mix phx.server
[info] Running PoeticWeb.Endpoint with cowboy 2.6.3 at 0.0.0.0:4000 (http)
[info] Access PoeticWeb.Endpoint at http://localhost:4000
```

![New upload multipart form](https://poeticoding.com/step-by-step-tutorial-to-build-a-phoenix-app-that-supports-user-uploads/phoenix_multipart_upload_form.jpg)

New upload multipart form

I’m going to upload the _phoenix.png_ image found in the project’s assets. Once submitted, we should see this inspection log on the terminal

```
%Plug.Upload{
  content_type: "image/png",
  filename: "phoenix.png",
  path: "/var/folders/lt/t88p62t91mg1mxdlmv_rlkl80000gn/T//plug-1555/multipart-1555258629-39672758309128-2"
}
```

There are three important fields that Plug gives us: `filename`, `content_type` and `path` - which is the path of the temporary file.

## Documents context

Once the `UploadController.create/2` function is invoked, it has to create an upload record in the database and store the file in the uploads directory.

Instead of putting all the logic into the `create` function, it’s much better to write this logic into a [context](https://hexdocs.pm/phoenix/contexts.html). A context is a great way to decouple the controllers from the logic of the application (like using `Repo` to create, or load, records).

### Create upload from `%Plug.Upload{}`

Let’s create the file `lib/poetic/documents.ex` with our context `Poetic.Documents`, which we use as the public interface to manage the uploads.

```
# lib/poetic/documents.ex
defmodule Poetic.Documents do
  import Ecto.Query, warn: false

  alias Poetic.Repo
  alias Poetic.Documents.Upload

  def create_upload_from_plug_upload(%Plug.Upload{
    filename: filename,
    path: tmp_path,
    content_type: content_type
  }) do
		
    # upload creation logic

  end

end
```

The actual hash calculation, database record creation and file’s copy take place as part of the `create_upload_from_plug_upload/1` function.

```
#create_upload_from_plug_upload function

hash = 
  File.stream!(tmp_path, [], 2048) 
  |> Upload.sha256()

with {:ok, %File.Stat{size: size}} <- File.stat(tmp_path),  
  {:ok, upload} <- 
    %Upload{} |> Upload.changeset(%{
      filename: filename, content_type: content_type,
      hash: hash, size: size }) 
    |> Repo.insert(),
				
  :ok <- File.cp(
      tmp_path,
      Upload.local_path(upload.id, filename)
   )

do
  
  {:ok, upload}

else

  {:error, reason}=error -> error

end
```

Using pattern matching, we can easily extract the _filename_, _content\_type_ and _path_ from the _Plug.Upload_ struct passed to the function.

We first calculate the SHA-256 hash of the file, and then we use the `with` construct to check that all of the three passed clauses match.

*   In the first clause we use [`File.stat`](https://hexdocs.pm/elixir/File.html#stat/2) and pattern matching to bind the `size` variable to the size of the file.
*   If the previous clause matches, we now have everything we need to insert our upload into the database.
*   Once the upload is successfully created in the database, we copy the file into our uploads directory using the `Upload.local_path(upload.id, filename)` function.

If everything goes well, the function returns `{:ok, upload}`, where `upload` is a `Poetic.Documents.Upload` struct.

If one of the clauses doesn’t match, there is an error and the function returns the `{:error, reason}` tuple.

To test this function on _iex_, we pass a `%Plug.Upload{}` struct that points to a valid file (remember to set an absolute path).

```
iex> alias Poetic.Documents
iex> upload = %Plug.Upload{
	filename: "phoenix.png", 
	content_type: "image/png",
	path: "/absolute_path_to/phoenix.png", 
}
iex> Documents.create_upload_from_plug_upload(upload)
{:error, :enoent}
```

Uh oh - something’s gone wrong 🤔

`enoent` means _No such files or directory_, and in this case we’ve received this error because we didn’t create the _uploads directory_ (which in my case would be _/Users/alvise/uploads\_dev_).

We can also see that it’s difficult to understand to which clause the error refers. [There is an effective way of managing this problem using tuple-wrapping](https://medium.com/@tylerpachal/using-tuple-wrapping-to-improve-with-expressions-in-elixir-f491b06265fa).

But there’s another problem, so let’s see what we have inside the uploads table

```
poetic_dev=# select * from uploads;
id |  filename   | size  | ...
 5 | phoenix.png | 13900 | ...

(1 rows)
```

Although we had an error, the uploads record is still in the database.

This happens because the function that returns an error `File.cp/2` fails _after_ we’ve inserted the upload into the database.

### Repo.transaction

Hopefully, we can use [transactions](https://hexdocs.pm/ecto/Ecto.Repo.html#c:transaction/2_) to pack everything into an _atomic_ operation. Doing it this way means that, if anything fails, the changes are rolled-back (i.e., if we match an error, we ask to rollback).

```
Repo.transaction fn ->
  with ...
  do
    upload
  else
    {:error, reason} -> Repo.rollback(reason)
  end
end
```

If everything goes well, the `Repo.transaction` returns `{:ok, upload}` while, in the case of an error, it returns `{:error, reason}`.

Let’s fix the error by creating the _uploads directory_, then try again.

```
iex> %Plug.Upload{
	filename: "phoenix.png", 
	content_type: "image/png",
	path: "/absolute_path_to/phoenix.png", 
} |> Documents.create_upload_from_plug_upload()

{:ok,
  %Poetic.Documents.Upload{
		...
		content_type: "image/png",
    filename: "phoenix.png",
    hash: "07aa9b01...",
    id: 7,
    size: 13900,
    inserted_at: ~N[2019-04-15 12:25:24],
    updated_at: ~N[2019-04-15 12:25:24]
  }
}
```

Fantastic - it worked 🎉! The upload is created in the database and the file is copied into the _uploads\_dev_ directory.

```
$ ls /Users/alvise/uploads_dev/
7-phoenix.png
```

## UploadController -`:create` action

We can use the Documents context we just created to implement the `create/2` function in the Upload controller

```
# PoeticWeb.UploadController

alias Poetic.Documents

def create(conn, %{"upload" => %Plug.Upload{}=upload}) do

  case Documents.create_upload_from_plug_upload(upload) do

    {:ok, upload}->
      put_flash(conn, :info, "file uploaded correctly")
      redirect(conn, to: Routes.upload_path(conn, :index))

    {:error, reason}->
      put_flash(conn, :error, "error upload file: #{inspect(reason)}")
      render(conn, "new.html")
  end

end
```

We pass the upload to `Documents.create_upload_from_plug_upload/1` which handles everything for us.

*   when it returns successfully, we set a flash info message and redirect to the _index_ page where we list all the uploads.
*   when it returns an error, we set a flash error message and redirect to the _new_ page.

## UploadController - `:index` action

To list the uploads, firstly we add a simple function in the `Documents` context, called `list_uploads`. This returns all the uploads in the database.

```
defmodule Poetic.Documents do
  ...
  def list_uploads do
    Repo.all(Upload)
  end
end
```

In the `UploadController`, we then create the `index/2` function where we get the uploads list and render the _index.html_ template.

```
defmodule PoeticWeb.UploadController do
  ...
  def index(conn, _params) do
    uploads = Documents.list_uploads()
    render(conn, "index.html", uploads: uploads)
  end
end
```

We pass the _uploads_ list to the rendering function and - in the template `lib/poetic_web/templates/upload/index.html.eex` - we loop over the list to render a table of uploads.

```
<table class="table">
  <thead>
    <th>ID</th>
    <th>Filename</th>
    <th>Type</th>
    <th>Time</th>
  </thead>
  <tbody>
		
    <%= for upload <- @uploads do %>
      <tr>
        <td><%= upload.id %></td>
        <td><%= upload.filename %></td>
        <td><%= upload.content_type %></td>
        <td><%= upload.inserted_at %></td>
      </tr>
    <% end %>
		
  </tbody>
</table>
```

## Let’s try it

```
$ mix phx.server
Running PoeticWeb.Endpoint with cowboy
Access PoeticWeb.Endpoint at http://localhost:4000
...
```

![:index action to list uploads](https://poeticoding.com/step-by-step-tutorial-to-build-a-phoenix-app-that-supports-user-uploads/index_action_to_list_uploads.png)

:index action to list uploads

## Download

To request a download we use the `show/2` function, which we invoked using the `GET /uploads/:id` HTTP request.

We start amending the `index.html.eex` template, by adding a download link to the row of each upload.

```
<%= for upload <- @uploads do %>
  ...
  <td>
    <%= link "download", to: Routes.upload_path(@conn, :show, upload.id) %>
  </td>
<% end %>
```

Then, in the `Documents` context, we add the `get_upload!(id)` function which, when given an `id` returns an Upload struct.

```
# lib/poetic/documents.ex
defmodule Poetic.Documents do
  ...
  def get_upload!(id) do
    Upload
    |> Repo.get!(id)
  end
end
```

Finally, let’s implement the `show/2` function.

Here, we use the given `id` to obtain the upload from the database, along with the `local_path` where the file is saved, and send the file using `send_download`.

```
# PoeticWeb.UploadController

def show(conn, %{"id" => id}) do
  upload = Documents.get_upload!(id)
  local_path = Upload.local_path(upload.id, upload.filename)
  send_download conn, {:file, local_path}, filename: upload.filename
end
```

We pass then connection to `send_download` and a tuple with the file’s path we want to send and the filename of the file.

Going with our browser to _http://localhost:4000/uploads_ we now see the _download_ link we can use to download a file

![list of uploads with download link](https://poeticoding.com/step-by-step-tutorial-to-build-a-phoenix-app-that-supports-user-uploads/index_download_link.jpg)

List of uploads with download link

## Upload size limit

If we try to upload a large file such as a 200MB tiff image, we receive the following error

![The request is too large](https://poeticoding.com/step-by-step-tutorial-to-build-a-phoenix-app-that-supports-user-uploads/the_request_is_too_large.jpg)

The request is too large

By default the [Plug multipart parser](https://hexdocs.pm/plug/Plug.Parsers.MULTIPART.html) reads a maximum of _8\_000\_000 bytes_. To increase this limit we need to amend the `lib/poetic_web/endpoint.ex` file

```
# lib/poetic_web/endpoint.ex
plug Plug.Parsers,
     parsers: [:urlencoded, :multipart, :json],
```

changing `:multipart` with `{:multipart, length: num_of_bytes}`

```
plug Plug.Parsers,
     parsers: [:urlencoded, {:multipart, length: 500_000_000}, :json],
```

In this case, we’ve set a limit of 500MB. After restarting the server, we see that following this change, we can now upload a huge 200MB tiff image.

![Large image uploaded correctly](https://poeticoding.com/step-by-step-tutorial-to-build-a-phoenix-app-that-supports-user-uploads/large_file_upload.jpg)

Large image uploaded correctly

## Wrap up

In this tutorial we saw in depth how to build a Phoenix app from scratch, letting users upload their files using a multipart form. We learnt how to easily run PostgreSQL with Docker on our machine, to receive uploads using Plug, and how to use Ecto to store uploads’ details into the database.\\

There are many libraries out there that help you to deal with uploads and cloud storage. A great one is [Arc](https://github.com/stavro/arc), which integrates well with Ecto and AWS S3.

You can find all the code related to this article in the GitHub repo: [poeticoding/phoenix\_uploads\_articles](https://github.com/poeticoding/phoenix_uploads_articles).

In the next part - [Creating Thumbnails of uploaded Images and PDF in Phoenix](https://poeticoding.com/creating-thumbnails-of-uploaded-images-and-pdf-in-phoenix/) - we see how to integrate ImageMagick and the Mogrify wrapper to create thumbnails for image and PDF files.
