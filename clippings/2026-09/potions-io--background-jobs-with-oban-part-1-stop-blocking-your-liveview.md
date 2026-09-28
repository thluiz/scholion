---
url: "https://potions.io/blog/background-jobs-with-oban-part-1"
captured_at: "2026-09-28T14:17:38+01:00"
title: "Background jobs with Oban, part 1: stop blocking your LiveView"
domain: "potions-io"
---

This post covers moving slow work out of a LiveView and into a background job with [Oban](https://hex.pm/packages/oban). In it we'll install Oban by hand, create its jobs table, configure its queues and plugins, write a worker, and enqueue that worker from a LiveView event handler.

You can watch the screencast above, or read the full walkthrough below. Unfurl's source is available on [GitHub](https://github.com/potionsio/003_oban) if you'd like to follow along.

Oban is a job processing library for Elixir that keeps its jobs in your database instead of a separate queue server. If you're already running PostgreSQL, which [Potions installs by default](https://potions.io/docs/creating-server), there's nothing new to deploy.

We're working in an app called Unfurl. You paste in a URL, and it fetches the web page, pulls out the title, description, and preview image, writes them to the database, and then displays them.

Right now all of that happens while the user waits. Let's move it into the background.

* * *

## What happens today

Let's take a quick look at how some of this currently works in the codebase.

We'll open the `Preview` module, which holds the logic to fetch a URL and then extract the preview metadata.

In it we'll find the `fetch` function. It takes a URL and makes a request to it with [Req](https://hexdocs.pm/req). Notice that a failed fetch holds on to its status code. That will come in handy in part two.

lib/unfurl/preview.ex

```
@spec fetch(String.t()) :: {:ok, map()} | {:error, term()}
def fetch(url) when is_binary(url) do
  case request(url) do
    {:ok, %Req.Response{status: 200, body: body}} ->
      {:ok, parse(body, url)}

    {:ok, %Req.Response{status: status}} ->
      {:error, {:http_status, status}}

    {:error, reason} ->
      {:error, {:request_failed, reason}}
  end
end
```

Then let's open our `LinkLive` LiveView.

When a `save` event happens, the LiveView calls a private `unfurl` function, which in turn calls the `Preview.fetch` function we just looked at.

That means the fetch happens inside the event handler, so for every new link that's added, the work is done synchronously.

lib/unfurl\_web/live/link\_live.ex

```
defp unfurl(socket, %Link{} = link) do
  case Preview.fetch(link.url) do
    {:ok, attrs} ->
      # ...
  end
end
```

Let's see what that feels like in the app.

Back in the browser, we can enter the URL of a page to preview. I'll paste one in and hit **Preview**. For a site that's fast and has no problems, it works, and a preview is displayed.

Now let's try a web page that's slow.

This time we have to sit and wait for the site to respond. One slow website freezes the page for our user, and this is exactly the kind of work that belongs in the background.

* * *

## Adding Oban

The first thing we need is the dependency. Oban has an automatic installer that uses [Igniter](https://hex.pm/packages/igniter), but we'll install it manually here.

We'll copy the dependency from Hex, open our Mixfile, and add it to our list of dependencies. Oban also has an optional web dashboard, [Oban Web](https://hex.pm/packages/oban_web), so let's grab that and add it as well. We won't wire it up until part two.

mix.exs

```
{:oban, "~> 2.24"},
{:oban_web, "~> 2.12"},
```

With those added, we'll go to the command line and run `mix deps.get` to install them.

```
$ mix deps.get
```

### The jobs table

Because Oban keeps jobs in a database table, we need a migration.

```
$ mix ecto.gen.migration add_oban_jobs_table
```

The generated migration is empty, so let's go to Oban's [manual installation guide](https://oban.hexdocs.pm/installation.html#manual-installation), copy over their example migration, and paste it into the one we just created. This runs all of Oban's versioned migrations against our database.

priv/repo/migrations/20260921143000\_add\_oban\_jobs\_table.exs

```
defmodule Unfurl.Repo.Migrations.AddObanJobsTable do
  use Ecto.Migration

  def up do
    Oban.Migration.up(version: 14)
  end

  def down do
    Oban.Migration.down(version: 1)
  end
end
```

Once that's added, we can migrate the database.

```
$ mix ecto.migrate
```

### Configuration

Now we need to configure Oban, so let's open our app's `config.exs`.

First we'll specify the `engine`. Our app uses PostgreSQL, so we'll use `Oban.Engines.Basic`. There are also engines for MySQL and for SQLite, which uses `Oban.Engines.Lite`.

Then we'll point Oban at our `repo`.

Next we'll name any queues we want jobs to run in. Queues are useful for keeping our jobs organized as we grow, and each queue in Oban operates independently with its own set of worker processes and concurrency limit. Let's add one queue here, `previews`, and set it to run five jobs simultaneously.

Then let's add a few extra optional configuration options. Oban's ["Ready for production" guide](https://oban.hexdocs.pm/ready_for_production.html) has a section on [pruning jobs](https://oban.hexdocs.pm/ready_for_production.html#pruning-jobs), so we'll add `pruner` with a `max_age` of seven days. This deletes finished jobs after seven days so our table doesn't grow forever.

The same guide has a section on [rescuing jobs](https://oban.hexdocs.pm/ready_for_production.html#rescuing-jobs). It details how `lifeline` rescues jobs that would otherwise get stuck in an `executing` state indefinitely after a deploy or an unexpected node restart. We'll set `rescue_after` to one hour, so any job that's been executing for an hour is rescued.

config/config.exs

```
config :unfurl, Oban,
  engine: Oban.Engines.Basic,
  repo: Unfurl.Repo,
  queues: [previews: 5],
  pruner: [max_age: {7, :days}],
  lifeline: [rescue_after: {1, :hour}]
```

And because Oban instances are isolated supervision trees, let's open our `application.ex` and include it in our application's supervisor.

lib/unfurl/application.ex

```
children = [
  UnfurlWeb.Telemetry,
  Unfurl.Repo,
  {Oban, Application.fetch_env!(:unfurl, Oban)},
  # ...
]
```

Then let's open the `test.exs` config and set Oban to [manual testing mode](https://oban.hexdocs.pm/testing.html). This ensures that jobs are still inserted into the database, but nothing is executed until a test says to.

config/test.exs

```
config :unfurl, Oban, testing: :manual
```

* * *

## Writing the worker

Now that Oban is configured, let's start integrating it.

We'll create a new `workers` directory under `unfurl`, and inside it a new worker module, `preview_worker.ex`. This will hold the code that Oban runs in the background.

We'll `use Oban.Worker`, specifying the `previews` queue, and we'll allow a maximum of five attempts for this job.

An [`Oban.Worker`](https://oban.hexdocs.pm/Oban.Worker.html) module needs to implement the `perform/1` callback, so let's define that. It receives an `Oban.Job` struct that carries a link's ID, and it will then fetch the link and preview it, all in the background. The `"id"` key is always a string because `args` round-trip through the database as JSON.

Inside the function we'll call a new function that we'll implement, `Links.fetch_link`, to return the link.

If a link is returned, we'll need to store the metadata and mark it as fetched, which we'll do with a new private function, `unfurl`. If the link no longer exists, `fetch_link` returns `:error`, and we'll return `{:cancel, :link_deleted}`. That tells Oban to stop and not retry the job anymore.

Now let's implement `unfurl` as a new private function that takes the link. In it we'll call the `Preview.fetch` function we looked at earlier.

If the link is fetched successfully, we'll take the `link` and `attrs` and pass them into a new function, `Links.apply_preview`, to update the link with the fetched metadata and mark its status as "ready". Then we'll return `:ok`.

And if there's an error fetching the URL, we'll pattern match on it and call another new function, `Links.mark_failed`, passing in the link to mark its status as "failed". Then we'll return `:ok` here too.

Before we implement those three functions, one more thing: because `perform/1` is a callback from the `Oban.Worker` behaviour, let's add `@impl` above it. That way a typo in the function name gets caught when we compile.

Then let's add aliases for our `Links` and `Preview` modules, as well as the `Link` module, so we can call them here without their prefixes.

lib/unfurl/workers/preview\_worker.ex

```
defmodule Unfurl.Workers.PreviewWorker do
  use Oban.Worker, queue: :previews, max_attempts: 5

  alias Unfurl.{Links, Preview}
  alias Unfurl.Links.Link

  @impl Oban.Worker
  def perform(%Oban.Job{args: %{"id" => id}}) do
    case Links.fetch_link(id) do
      {:ok, link} -> unfurl(link)
      :error -> {:cancel, :link_deleted}
    end
  end

  defp unfurl(%Link{} = link) do
    case Preview.fetch(link.url) do
      {:ok, attrs} ->
        {:ok, _link} = Links.apply_preview(link, attrs)
        :ok

      {:error, _reason} ->
        {:ok, _link} = Links.mark_failed(link)
        :ok
    end
  end
end
```

Now let's open the `Links` module and add those three functions.

First `fetch_link`. We'll use `Repo.get` to look up the link from its ID, returning an `:ok` tuple with the link, or an `:error` if there's no link.

Then `apply_preview`. It sets a `fetched_at` value of the current time, and updates the link with the fetched `attrs`, a status of "ready", and that timestamp.

And finally `mark_failed`, which updates the link's status to "failed".

lib/unfurl/links.ex

```
def fetch_link(id) do
  case Repo.get(Link, id) do
    %Link{} = link -> {:ok, link}
    nil -> :error
  end
end

def apply_preview(%Link{} = link, attrs) do
  fetched_at = DateTime.utc_now(:second)
  update_link(link, Map.merge(attrs, %{status: "ready", fetched_at: fetched_at}))
end

def mark_failed(%Link{} = link) do
  update_link(link, %{status: "failed"})
end
```

* * *

## Enqueuing the job

To enqueue a job, all we need to do is insert it, so let's add one more function here to do that.

We'll define a new public function, `schedule_preview`, that takes a link struct and some options. We'll take the link's ID to build a map, and once we have that we'll pipe it into `PreviewWorker.new`, which `use Oban.Worker` generates for us, to build a changeset. Then we'll pipe that into `Oban.insert` to write it to the jobs table. And let's add an alias above so we can call the `PreviewWorker` module without its prefix.

lib/unfurl/links.ex

```
alias Unfurl.Workers.PreviewWorker
...

def schedule_preview(%Link{} = link, opts \\ []) do
  %{id: link.id}
  |> PreviewWorker.new(opts)
  |> Oban.insert()
end
```

Now all we need to do is call this for Oban to run the work in the background.

Let's open the `LinkLive` LiveView module. Before, we were calling `unfurl` to fetch our link, so let's remove that function. And above, we were calling `unfurl` from the `handle_event` callback when a link was saved. Let's remove that too, and in its place call `Links.schedule_preview` as soon as the link is saved to the database.

Then let's add a flash message to let users know we're fetching their preview.

lib/unfurl\_web/live/link\_live.ex

```
def handle_event("save", %{"link" => link_params}, socket) do
  case Links.create_link(link_params) do
    {:ok, link} ->
      {:ok, _job} = Links.schedule_preview(link)

      {:noreply,
       socket
       |> put_flash(:info, "Fetching a preview for #{link.url}.")
       |> assign(:form, to_form(Links.change_link(%Link{})))}

    {:error, changeset} ->
      # ...
  end
end
```

With those changes, the LiveView's `save` handler doesn't fetch anything. It just creates the link and queues the work to happen in the background.

* * *

## Trying it out

Let's go to the command line and start our server.

```
$ mix phx.server
```

Then let's go to the browser. When we paste in a URL, we see our flash message right away, but we don't see anything else on the page.

Let's try refreshing. And when we do, the card shows up.

The page never froze, and our user isn't stuck waiting on somebody else's server. That's the whole point of moving this work into Oban.

* * *

## Coming up in part two

The one thing left is that this page doesn't know when a job finished.

So that's what we'll tackle in part two. We'll update the app to use [Phoenix PubSub](https://hexdocs.pm/phoenix_pubsub) so that previews show up the moment they're ready, no refresh required. Then we'll set up Oban Web's dashboard so we can keep an eye on our queues.

Unfurl's source is available on [GitHub](https://github.com/potionsio/003_oban).

That's it for part one. Thanks for watching, and happy deploying.
