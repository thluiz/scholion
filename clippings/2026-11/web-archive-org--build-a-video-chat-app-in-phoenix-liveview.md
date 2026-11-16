---
url: "https://web.archive.org/web/20200823145045id_/https://littlelines.com/blog/2020/07/06/building-a-video-chat-app-in-phoenix-liveview"
captured_at: "2026-11-16T08:17:52+00:00"
title: "Build a Video Chat App in Phoenix LiveView | Littlelines"
domain: "web-archive-org"
---

During this global pandemic, online video calls have become essential to the way we work. Millions of workers are now accustomed to hopping on calls with their colleagues to hash things out that they would previously have done in person. Zoom has shown itself to be a reliable partner for video conferencing. However, as a company, Zoom has given [plenty of](https://theintercept.com/2020/03/31/zoom-meeting-encryption/) [reasons to](https://techcrunch.com/2019/07/10/apple-silent-update-zoom-app/) [avoid](https://www.theverge.com/2020/6/3/21279355/zoom-end-encryption-calls-fbi-police-free-users) [its software.](https://www.npr.org/2020/06/12/876351501/zoom-acknowledges-it-suspended-activists-accounts-at-china-s-request)

The world’s new reliance on video conferencing got me thinking: _How hard could it be to build a video conferencing web application?_ Like most things worth doing, the answer was _difficult, but fun_.

When I first started researching for this project, I discovered that there isn’t much information out there about building a WebRTC-based application from start to finish. Mozilla’s WebRTC documentation is invaluable, but it lacked answers to some of the questions I had. And tutorials that exist generally only cover connecting two users in a fairly basic way. I wanted to do something more ambitious.

## What we’re going to build:

In this article, we’re going to build a real-time video chat application with the following requirements:

*   The app will allow users to create video chat rooms with a unique slug, allowing any user to join.
*   The app will keep track of which users are connected to the given room.
*   The app will allow users to establish a group video call with eachother through WebRTC peer connections.

Well, that sounds easy enough. Creating pages with central information on the fly in a web app is the bread and butter of any self-respecting web framework—and with Phoenix it’s a piece of cake. Tracking users seems a little tricky, but if you’ve heard of what LiveView and PubSub can do, you can probably guess that we’re still on the right track. WebRTC was designed for video calls, but group video calls? That might get complex. Plus, how would that even work if each of the connections is only peer-to-peer? We’ll get to that.

*   [We’ve wrapped up the finished product and deployed it at littlechat.app](https://littlechat.app/). Try creating a room and hopping on it with a friend or two. That’s what we’re going to create.
*   [You can also find the source code for this project here if you’re more of the self-guided type.](https://github.com/littlelines/littlechat)

## Prerequisites

I’m going to assume that you are comfortable working with Elixir and Phoenix. I’ll assume that you might have toyed around with LiveView a few times before this article, but it doesn’t take much to get up to speed. Finally, I’ll assume you have no WebRTC experience beyond having heard about it a few times.

We will be using the latest versions of Elixir, Erlang, Phoenix, and Phoenix LiveView in this article, which are the following at the time of writing:

*   Elixir 1.10.3
*   Erlang 23.0.2
*   Phoenix 1.5.3
*   Phoenix LiveView 0.13.3

## The Tech

### WebRTC

Web Real Time Communication, or WebRTC for short, is a technology that allows real-time, peer-to-peer communication between users. It provides an API for handling user video, audio, and other data via peer-to-peer connections.

WebRTC has been around since 2011, but implementation by the various browsers has been uneven over the years. Nowadays, each browser has a more consistent WebRTC implementation, making browser support much better, but implementing it can still be a dance.

What makes WebRTC so flexible—and, at times, confounding—is that it has no standardized server-side implementation. WebRTC does not care how users in a video chat learn about each other and send their connection information, it only handles how to connect those users once their information has been sent. This originally confused me, as I was not sure where the server-side _signaling_ (the WebRTC term for the process of telling two users about each other for a peer connection) ended and the `RTCPeerConnection` began. We’ll dig into this later.

### Phoenix

Elixir’s Phoenix framework allows us to build reliable and performant web applications built on Erlang’s rock-solid foundation. On any project, my first instinct these days is to reach for Phoenix. But the motivation goes deeper.

Elixir is built on Erlang’s VM, which was specifically developed for the challenges of the telecoms industry, where fault-tolerance and high-availability are essential. That sounds perfect for this project.

### LiveView

[LiveView](https://hexdocs.pm/phoenix_live_view/Phoenix.LiveView.html) is one of my favorite components of Phoenix. It makes real-time user interaction between the client’s UI and the server seamless, without needing to write (much) JavaScript. LiveView makes real-time user interactions much easier to build and maintain, all while working within familiar concepts: Phoenix, Elixir, and OTP.

## Getting Started

Have you got all your tools ready? Let’s go!

First, we’re going to create a new Phoenix project with LiveView already configured. If you’re trying to add video chat to an existing app without LiveView already configured, [LiveView is pretty easy to set up from scratch too.](https://hexdocs.pm/phoenix_live_view/installation.html#content) We’re going to call our project Littlechat, a portmenteau of Littlelines and chat.

```
$ mix phx.new littlechat --live
```

Now let’s `cd littlechat` into our brand new app and install its dependencies.

```
$ cd littlechat
$ mix deps.get
$ npm install --prefix assets
```

Standard stuff. Let’s go a little deeper.

## Creating the Rooms

Users can’t connect to each other if they don’t have a place to meet, so let’s build them a room!

Let’s create a _context_ called `Organizer` with a schema `Room`.

```
$ mix phx.gen.context Organizer Room rooms title:string slug:string
```

That generated a few files for us, `lib/littlechat/organizer.ex`, `lib/littlechat/organizer/room.ex`, and a migration file ending in `XXXXX_create_rooms.exs` Let’s start with our Room schema.

Our rooms will only have two data to start, `slug` and `title`, both strings. `slug` will be the unique identifier for the room, so we’ll need to add a unique index to the database to prevent collisions. Let’s set up the database:

```
# priv/repo/migrations/XXXXX_create_rooms.exs

defmodule Littlechat.Repo.Migrations.CreateRooms do
  use Ecto.Migration

  def change do
    create table("rooms") do
      add :slug, :string
      add :title, :string

      timestamps()
    end

    create unique_index(:rooms, :slug)
  end
end
```

For the schema, we’re going to create a basic changeset function with the added `unique_constraint` on slug. But we’re also going to add a private function, `format_slug/1` for the purpose of cleaning our slug input.

```
# lib/littlechat/room.ex

defmodule Littlechat.Room do
  @moduledoc """
  Schema for creating video chat rooms.
  """

  use Ecto.Schema
  import Ecto.Changeset

  schema "rooms" do
    field :title, :string
    field :slug, :string

    timestamps()
  end

  @fields [:title, :slug]

  def changeset(room, attrs) do
    room
    |> cast(attrs, @fields)
    |> validate_required([:title, :slug])
    |> format_slug()
    |> unique_constraint(:slug)
  end

  defp format_slug(%Ecto.Changeset{changes: %{slug: _}} = changeset) do
    changeset
    |> update_change(:slug, fn slug ->
      slug
      |> String.downcase()
      |> String.replace(" ", "-")
    end)
  end
  defp format_slug(changeset), do: changeset
end
```

Great! Now we can create rooms in the database. What about getting one from the DB? Easy.

```
# lib/littlechat/organizer.ex

defmodule Littlechat.Organizer do
  alias Littlechat.Repo
  alias Littlechat.Room

  import Ecto.Query

  def get_room(slug) when is_binary(slug) do
    from(room in Room, where: room.slug == ^slug)
    |> Repo.one()
  end
end
```

Now let’s build LiveViews for creating and viewing rooms.

We’re going to create two LiveViews, `LittlechatWeb.Room.NewLive` and `LittlechatWeb.Room.ShowLive`, the former for creating and the latter for showing the rooms. Let’s start with `NewLive`:

```
# lib/littlechat_web/live/room/new_live.ex

defmodule LittlechatWeb.Room.NewLive do
  use LittlechatWeb, :live_view

  alias Littlechat.Repo
  alias Littlechat.Room

  @impl true
  def render(assigns) do
    ~L"""
    <h1>Create a New Room</h1>
    <div>
      <%= form_for @changeset, "#", [phx_change: "validate", phx_submit: "save"], fn f -> %>
        <%= text_input f, :title, placeholder: "Title" %>
        <%= error_tag f, :title %>
        <%= text_input f, :slug, placeholder: "room-slug" %>
        <%= error_tag f, :slug %>
        <%= submit "Save" %>
      <% end %>
    </div>
    """
  end

  @impl true
  def mount(_params, _session, socket) do
    {:ok,
      socket
      |> put_changeset()
    }
  end

  @impl true
  def handle_event("validate", %{"room" => room_params}, socket) do
    {:noreply,
      socket
      |> put_changeset(room_params)
    }
  end

  def handle_event("save", _, %{assigns: %{changeset: changeset}} = socket) do
    case Repo.insert(changeset) do
      {:ok, room} ->
        {:noreply,
          socket
          |> push_redirect(to: Routes.room_show_path(socket, :show, room.slug))
        }
      {:error, changeset} ->
        {:noreply,
          socket
          |> assign(:changeset, changeset)
          |> put_flash(:error, "Could not save the room.")
        }
    end
  end

  defp put_changeset(socket, params \\ %{}) do
    socket
    |> assign(:changeset, Room.changeset(%Room{}, params))
  end
end
```

Let’s break this down by function.

*   `render/1` implements a LiveView callback with the given `assigns` (variables containing session data) and expects a `~L` sigil (Live EEx). I prefer my LEEx templates inline, but you’re welcome to create a file `lib/littlechat_web/live/room/new_live.html.leex` and get rid of this function if you prefer to keep your templates separate.
*   Inside of this template, we create a basic form for creating a new Room. Note the reference to the `@changeset` assign.
*   We then tell the form (via LiveView) to send the event `"validate"` to the server every time user input is added.
*   Finally, we tell the form to send the event `"submit"`, along with the associated form data, to the server when the user makes a submit action (presses enter or clicks “Submit”).
*   `mount/3` is a key callback that makes the LiveView function. It contains three arguments, `params`, `session`, and `socket`. The job of `mount/3` is to take these data and initialize the LiveView, returning a contract of `{:ok, socket}`. To this final contract, we call our new private function, `put_changeset/2`, to create a new Room schema changeset using the given parameters and assign it to the provided socket.
*   The `handle_event/2` callbacks simply handle our form events, `validate` and `submit`. This code is similar to code you’ve used in your Phoenix controllers.

Now that we’ve created our LiveView, let’s add it to our routes. While we’re at it, let’s add a route for our next LiveView, `ShowLive`.

```
# lib/livechat_web/router.ex

defmodule LittlechatWeb.Router do
# ...
  scope "/room" do
    live "/new", Room.NewLive, :new
    live "/:slug", Room.ShowLive, :show
  end
# ...
end
```

Next, we’ll create a basic LiveView for viewing one of our created rooms.

```
# lib/livechat_web/live/room/show_live.ex

defmodule LittlechatWeb.Room.ShowLive do
  @moduledoc """
  A LiveView for creating and joining chat rooms.
  """

  use LittlechatWeb, :live_view

  alias Littlechat.Organizer

  @impl true
  def render(assigns) do
    ~L"""
    <h1><%= @room.title %></h1>
    """
  end

  @impl true
  def mount(%{"slug" => slug}, _session, socket) do
    case Organizer.get_room(slug) do
      nil ->
        {:ok,
          socket
          |> put_flash(:error, "That room does not exist.")
          |> push_redirect(to: Routes.room_new_path(socket, :new))
        }
      room ->
        {:ok,
          socket
          |> assign(:room, room)
        }
    end
  end
end
```

Now you can start your server with `iex -S mix phx.server`, and head to [http://localhost:4000/room/new](http://localhost:4000/room/new). Try creating a new room and head to it. You’ll see this.

![Creating a Room in Littlechat](https://cdn.littlelines.com/assets/blog/multi-person-video-chat/Littlechat_Creating-a-Room-de2168773da170ece4ec880aae7d57f96cd77a1cf7e4fdc9b8ed5e7c5bf4e24b.gif)

## Tracking User Presence

Cool, we can create a room. But having a room isn’t much use to us if users can’t see each other. We need to add functionality to keep track of the users in each room. Luckily, Phoenix already has a built-in library for this called [Phoenix Presence](https://hexdocs.pm/phoenix/Phoenix.Presence.html). Phoenix Presence provides an easy API to track which users are connected to a given PubSub topic. This is exactly what we need.

We also can’t keep track of users if we don’t know who they are, so we’re going to set up a system for tracking ephemeral users. In our design, our users will not persist beyond the current session. This is designed to keep things simple, but we could easily modify our application to have persistent users in the database if we wanted. Let’s create a struct for our user, called `ConnectedUser`, identifiable by a UUID.

```
# lib/littlechat/connected_user.ex

defmodule Littlechat.ConnectedUser do
  defstruct uuid: ""
end
```

While we’re at it, let’s add `{:uuid, "~> 1.1"}` to our `mix.exs` file and run `mix deps.get`, to make sure we have access to the UUID module.

Next, we need to add logic to our `Room.ShowLive` to create the current user upon joining the room. Add this function somewhere near the bottom of our LiveView. We’ll use it in a moment.

```
# lib/littlechat_web/live/room/show_live.ex

defmodule LittlechatWeb.Room.ShowLive do
+ alias Littlechat.ConnectedUser

  # ...

+ defp create_connected_user do
+   %ConnectedUser{uuid: UUID.uuid4()}
+ end

  # ...
end
```

Now, let’s add a `@user` assign to the socket on `mount` to represent us.

```
# lib/littlechat_web/live/room/show_live.ex

@impl true
def mount(%{"slug" => slug}, _session, socket) do
+ user = create_connected_user()

  case Organizer.get_room(slug) do
    nil ->
      {:ok,
        socket
        |> put_flash(:error, "That room does not exist.")
        |> push_redirect(to: Routes.room_new_path(socket, :new))
      }
    room ->
      {:ok,
        socket
        |> assign(:room, room)
+       |> assign(:user, user)
      }
  end
end
```

Nice. We can identify ourselves. Now, let’s work on keeping track of others. Let’s set up our [presence](https://hexdocs.pm/phoenix/Phoenix.Presence.html) module.

```
# lib/littlechat_web/presence.ex

defmodule LittlechatWeb.Presence do
  use Phoenix.Presence,
    otp_app: :littlechat,
    pubsub_server: Littlechat.PubSub
end
```

Now, we need to add it to our supervision tree after our PubSub setup and before our Endpoint is started.

```
# lib/littlechat/application.ex

defmodule Littlechat.Application do
  # See https://hexdocs.pm/elixir/Application.html
  # for more information on OTP Applications
  @moduledoc false
  use Application
  def start(_type, _args) do
    children = [
      # Start the Ecto repository
      Littlechat.Repo,
      # Start the Telemetry supervisor
      LittlechatWeb.Telemetry,
      # Start the PubSub system
      {Phoenix.PubSub, name: Littlechat.PubSub},
+     # Start our Presence module.
+     LittlechatWeb.Presence,
      # Start the Endpoint (http/https)
      LittlechatWeb.Endpoint
      # Start a worker by calling: Littlechat.Worker.start_link(arg)
      # {Littlechat.Worker, arg}
    ]
    # See https://hexdocs.pm/elixir/Supervisor.html
    # for other strategies and supported options
    opts = [strategy: :one_for_one, name: Littlechat.Supervisor]
    Supervisor.start_link(children, opts)
  end
  # Tell Phoenix to update the endpoint configuration
  # whenever the application is updated.
  def config_change(changed, _new, removed) do
    LittlechatWeb.Endpoint.config_change(changed, removed)
    :ok
  end
end
```

Phoenix Presence works by tracking all users currently active and subscribed to a given PubSub topic. You can probably guess our topic already: `room:ROOM_SLUG`. Let’s add code to subscribe to the given topic and begin tracking our user.

```
# lib/littlechat_web/live/room/show_live.ex

defmodule LittlechatWeb.Room.ShowLive do
  @moduledoc """
  A LiveView for creating and joining chat rooms.
  """

  use LittlechatWeb, :live_view

  alias Littlechat.Organizer
  alias Littlechat.ConnectedUser

+ alias LittlechatWeb.Presence

  @impl true
  def render(assigns) do
    ~L"""
    <h1><%= @room.title %></h1>
    """
  end

  @impl true
  def mount(%{"slug" => slug}, _session, socket) do
    user = create_connected_user()
+   Phoenix.PubSub.subscribe(Littlechat.PubSub, "room:" <> slug)
+   {:ok, _} = Presence.track(self(), "room:" <> slug, user.uuid, %{})

    case Organizer.get_room(slug) do
      nil ->
        {:ok,
          socket
          |> put_flash(:error, "That room does not exist.")
          |> push_redirect(to: Routes.room_new_path(socket, :new))
        }
      room ->
        {:ok,
          socket
          |> assign(:room, room)
          |> assign(:user, user)
+         |> assign(:slug, slug)
        }
    end
  end

  defp create_connected_user do
    %ConnectedUser{uuid: UUID.uuid4()}
  end
end
```

Looking at your browser, you’ll see that nothing has changed. But on the backend, Phoenix is now tracking the presence of our user. Because the user is subscribed to the given room slug as a topic (`room:test` in our case), we can now list all users in a given room. Let’s do that.

Phoenix Presence broadcasts a message to connected processes with the event `presence_diff`, with a payload diff of the present users. We could parse this diff, but we don’t need to do that, so instead we’re going to use it as a signal to refresh the list of currently present users. We’ll put the currently connected users into an assign, `@connected_users`, and then display a list of their UUIDs. Let’s see that in action:

```
defmodule LittlechatWeb.Room.ShowLive do
  @moduledoc """
  A LiveView for creating and joining chat rooms.
  """

  use LittlechatWeb, :live_view

  alias Littlechat.Organizer
  alias Littlechat.ConnectedUser

  alias LittlechatWeb.Presence
+ alias Phoenix.Socket.Broadcast

  @impl true
  def render(assigns) do
    ~L"""
    <h1><%= @room.title %></h1>
+   <h3>Connected Users:</h3>
+   <ul>
+   <%= for uuid <- @connected_users do %>
+     <li><%= uuid %></li>
+   <% end %>
+   </ul>
    """
  end

  @impl true
  def mount(%{"slug" => slug}, _session, socket) do
    user = create_connected_user()
    Phoenix.PubSub.subscribe(Littlechat.PubSub, "room:" <> slug)
    {:ok, _} = Presence.track(self(), "room:" <> slug, user.uuid, %{})

    case Organizer.get_room(slug) do
      nil ->
        {:ok,
          socket
          |> put_flash(:error, "That room does not exist.")
          |> push_redirect(to: Routes.room_new_path(socket, :new))
        }
      room ->
        {:ok,
          socket
          |> assign(:room, room)
          |> assign(:user, user)
          |> assign(:slug, slug)
+         |> assign(:connected_users, [])
        }
    end
  end

+ @impl true
+ def handle_info(%Broadcast{event: "presence_diff"}, socket) do
+   {:noreply,
+     socket
+     |> assign(:connected_users, list_present(socket))}
+ end

+  defp list_present(socket) do
+    Presence.list("room:" <> socket.assigns.slug)
+    |> Enum.map(fn {k, _} -> k end) # Phoenix Presence provides nice metadata, but we don't need it.
+  end

  defp create_connected_user do
    %ConnectedUser{uuid: UUID.uuid4()}
  end
end
```

We can see our users in realtime now! Go on, try opening a few tabs at [http://localhost:4000/room/test](http://localhost:4000/room/test) and watch the users grow and shrink. For some real fun, open a session on your phone too.

![User Presence](https://cdn.littlelines.com/assets/blog/multi-person-video-chat/User-Presence-69b6360e6636d2833ec8c71ced08b4676f435aa4a117beb75a4c33f124008178.gif)

## Firing Up Our Camera

We’ve had our fun with LiveView and Phoenix for user sessions, but now it’s time to to get our hands dirty with some WebRTC and JavaScript. The first step in any video application is getting your own webcam and streaming the video to the browser. It seems simple enough, so let’s see how it works.

In LiveView, JavaScript should be handled through “hooks”. These can be attached to any element within the LiveView, and they contain various callbacks to fire JS on a given event. [You can read more about JS interoperability with LiveView here.](https://hexdocs.pm/phoenix_live_view/Phoenix.LiveView.html#module-js-interop-and-client-controlled-dom) We’re going to attach our first hook to a new button at the bottom of the page, “Join Call.”

```
# lib/littlechat_web/live/room/show_live.ex

defmodule LittlechatWeb.Room.ShowLive do
  # ...

  @impl true
  def render(assigns) do
    ~L"""
    <h1><%= @room.title %></h1>
    <h3>Connected Users:</h3>
    <ul>
    <%= for {uuid, _} <- @connected_users do %>
      <li><%= uuid %></li>
    <% end %>
    </ul>

+   <video id="local-video" playsinline autoplay muted width="600"></video>
+
+   <button class="button" phx-hook="JoinCall">Join Call</button>
    """
  end

  # ...
end
```

Now we need to configure this hook in JavaScript, along with code to get our webcam and microphone.

```
// assets/js/app.js

import {LiveSocket} from "phoenix_live_view"

let csrfToken = document.querySelector("meta[name='csrf-token']").getAttribute("content")
const localStream

async function initStream() {
  try {
    // Gets our local media from the browser and stores it as a const, stream.
    const stream = await navigator.mediaDevices.getUserMedia({audio: true, video: true, width: "1280"})
    // Stores our stream in the global constant, localStream.
    localStream = stream
    // Sets our local video element to stream from the user's webcam (stream).
    document.getElementById("local-video").srcObject = stream
  } catch (e) {
    console.log(e)
  }
}

let Hooks = {}
Hooks.JoinCall {
  mounted() {
    initStream()
  }
}

let liveSocket = new LiveSocket("/live", Socket, {hooks: Hooks, params: {_csrf_token: csrfToken}})

window.addEventListener("phx:page-loading-start", info => NProgress.start())

window.liveSocket = liveSocket
```

So what did we just do? The main function of note here is `initStream()`, which is an async function that requests the user’s local user media (a webcam, generally) and then stores the stream in a constant, `localStream`. The global scope of `localStream` is important, as we will be using it multiple times in different functions when establishing peer connections with users.

We also added the `Hooks` object, which contains hooks that we pass to the LiveSocket through `{hooks: Hooks, ...}`. We created a new hook, `JoinCall` (notice that its name corresponds with our `phx-hook` attribute in the LiveView). Inside of this, we create a callback function for LiveView’s `mounted` event and call our `initStream()` function. This is just the beginning of our fun with LiveView hooks in this application.

Now, we can open up the browser at [http://localhost:4000/room/test](http://localhost:4000/room/test) and click “Join Call.” The browser will request access to your webcam and microphone. With any luck, you’ll see your face smiling back at you.

If you’re like me, you will probably find this very jarring. Not because you and I don’t have nice faces, but because I am not used to seeing my face mirrored back at me and you probably aren’t either. Luckily, this can be easily fixed with a little CSS.

```
// assets/css/app.scss

// Rotate the video to give a "mirror" appearance. Feels more natural.
#local-video {
  transform: rotateY(180deg);
}
```

Now that we have our own stream looking nice and pretty, it’s time to start connecting to other users.

## WebRTC

Before we can begin implementing peer-to-peer video calling in WebRTC, we first have to understand how it works. WebRTC provides the technology for connecting two peers and enabling them to send data to each other. What WebRTC does _not_ implement is how they find each other and initially communicate. This very important task, called _signaling_, is up to the programmer.

This signaling-agnosticism is what many web developers find confusing at first. However, what I found confusing was knowing where exactly signaling ends and WebRTC’s peer connections take over. We’ll dive deep into that. But as a general rule of thumb, WebRTC does nothing for you unless you tell it exactly what you want, all the time.

### The WebRTC flow with two users.

WebRTC follows a very specific set of rules. So it’s important that we understand the general flow first. Below, I’m going to use WebRTC terminology such as _[peer connection](https://webrtcglossary.com/peerconnection/)_, _[SDP](https://developer.mozilla.org/en-US/docs/Glossary/SDP)_, _offer_, _answer_, [_ICE (interactive connectivity establishment)_](https://developer.mozilla.org/en-US/docs/Glossary/ICE), and _[STUN server](https://webrtcglossary.com/stun/)._ Don’t get bogged down in the details of these words – what’s important here is understanding the broad flow so that we can deepen our understanding as we implement it. Without further introduction, here is how to create a video call with someone else via WebRTC, _in 18 easy steps!_

1.  User A wants to call User B.
2.  User A gets their local webcam and mic stream.
3.  User A generates an empty peer connection to connect to User B (`RTCPeerConnection`) and adds its local stream to this peer connection.
4.  Upon User A adding their stream’s tracks to their `RTCPeerConnection` for User B, this `RTCPeerConnection` triggers its `onnegotiationneeded` callback.
5.  The `onnegotiationneeded` callback creates a new SDP **offer** for the peer connection, sets its `localDescription` to this offer, and then sends this information to the signaling server to be sent to User B.
6.  The signaling server accepts this SDP offer and forwards the string to the appropriate user, User B.
7.  Meanwhile, the STUN server (which was provided when creating the RTCPeerConnection) sends several ICE candidates back to the peer connection, triggering its `onicecandidate` callback.
8.  The `onicecandidate` callback sends the given ICE candidate string to the signaling server, to also be forwarded to User B. The signaling server accepts this and forwards it to User B.
9.  User B receives the SDP **offer** from User A via the signaling server.
10.  User B gets their local webcam and mic stream.
11.  Upon receiving User A’s **offer**, User B creates a new `RTCPeerConnection` for User A and adds User B’s local video and mic track to it.
12.  User B sets its peer connection with User A’s `remoteDescription` to the received SDP offer from User A.
13.  User B then creates an **answer**, sets its `localDescription` to its own answer, and then sends the SDP **answer** back to User A via the signaling server.
14.  Meanwhile, User B receives ICE candidates from its configured **STUN server**, which it sends to User A via the signaling server. Likewise, User B receives ICE candidates through the **signaling server** sent by User A, which it adds to its peer connection with User A’s list of ICE candidates. This mutual exchange of ICE candidates is called _ice candidate negotiation_.
15.  User A **receives** this SDP **answer** and sets its peer connection with User B’s `remoteDescription` to the given **answer**.
16.  Meanwhile, User A receives various ICE candidates from User B via the signaling server, which it adds to its peer connection with User A’s list of ICE candidates.
17.  Once User A accepts User B’s answer and the two find a mutually agreeable ICE candidate to start sending a stream over, both User A and User B’s mutual peer connections’ `ontrack` callbacks are triggered. User A adds User B’s remote stream to User A’s browser via a video element and User B does the same with User A’s remote stream on its browser.
18.  At this point, media is flowing and a video call has begun!

Are you thoroughly confused? I certainly was when I first started learning WebRTC. If you couldn’t follow, try reading the steps again. Again, don’t worry if you don’t understand this or that detail, focus on how the data flows–who sends what: _e.g._ User A via the signaling server to User B, STUN server handled by User A’s browser and sent to User B via the signaling server, etc. If you’re looking to get deeper into how the WebRTC flow works, I recommend [this article](https://www.pkc.io/blog/untangling-the-webrtc-flow/).

### What about 3+ users?

Now we’re talking! If I asked you to take a guess at how we would implement multi-user functionality, you would probably guess that we simply need to have an extra peer connection for each user to connect to eachother, and you would be right! This is what’s called a _[mesh](https://webrtcglossary.com/mesh/)_ architecture in WebRTC lingo. I won’t be getting into other architectures in this article, but know that [there are pros and cons of whatever architecture you decide.](https://webrtchacks.com/webrtc-beyond-one-one/) I’ll be demonstrating mesh because it is the simplest to implement and the most decentralized of the architectures, but you could certainly modify this code to handle a mixer or SFU routing architecture.

In a mesh architecture, each user has `n - 1` peer connections to each other user. So, if a User C were to enter the chat room, users A and B would need to send their offers, with User C responding, and the rest of the steps taking place as layed out above.

## Who are our peers?

To build out a mesh architecture, our clients need to know about each other so that we can create peer connections with every other connected user. We have the `@connected_users` assign, which stores this information, but we need a way of sending that information to our JavaScript because `RTCPeerConnection`s may only be created in the browser. In LiveView, this can sometimes seem a bit awkward. This is because LiveView is designed mainly for live UI interaction, rather than handling data behind the scenes. In these cases, Phoenix also provides us with [Channels](https://hexdocs.pm/phoenix/channels.html), but given how relatively simple the data is that our signaling server needs to send, LiveView’s hooks will do the trick.

We will rely on the following pattern a few times in the next few minutes:

1.  On the server, an assign is changed.
2.  Our LiveView reflects this change by adding a hidden HTML element to the browser, with a LiveView hook attribute and any associated data within the element’s dataset.
3.  The newly-mounted element’s hook is triggered in the JavaScript, passing along its associated data to our JS.

Let’s use storing our users on the JS-side as an example.

We already have the `@connected_users` assign, so all we need to do is add a hook to our loop of that assign. Let’s do that. But at the same time, let’s rely on our `@connected_users` assign to create `video` elements for our other connected users.

```
# lib/littlechat_web/live/room/show_live.ex

defmodule LittlechatWeb.Room.ShowLive do
  # ...

  @impl true
  def render(assigns) do
    ~L"""
    <h1><%= @room.title %></h1>
    <h3>Connected Users:</h3>
    <ul>
    <%= for {uuid, _} <- @connected_users do %>
      <li><%= uuid %></li>
    <% end %>
    </ul>

+   <div class="streams">
      <video id="local-video" playsinline autoplay muted width="600"></video>

+     <%= for uuid <- @connected_users do %>
+       <video id="video-remote-<%= uuid %>" data-user-uuid="<%= uuid %>" playsinline autoplay phx-hook="InitUser"></video>
+     <% end %>
+   </div>


    <button class="button" phx-hook="JoinCall">Join Call</button>
    """
  end

  # ...
end
```

Now, let’s set up our hook in `app.js`. First, we’re going to create a variable at the top of our file for keeping track of our users. Our `users` object will be key to how we build peer connections in a mesh architecture, as it allows us to create a peer connection to each of the connected users.

```
// assets/js/app.js

var users = {}
```

Now we’re going to create two functions for manipulating this object, `addUserConnection()` and `removeUserConnection()`.

```
// assets/js/app.js

function addUserConnection(userUuid) {
  if (users[userUuid] === undefined) {
    users[userUuid] = {
      peerConnection: null
    }
  }

  return users
}

function removeUserConnection(userUuid) {
  delete users[userUuid]

  return users
}
```

`addUserConnection()` accepts a user’s UUID and then creates an object (`{peerConnection: null}`) for them in our `users` object, as long as they aren’t already in the `users` object.

`removeUserConnection()` simply deletes our user.

Now, let’s create a hook that uses both of these functions to keep track of users when they enter or leave our chat room. Add the following hook near our `JoinCall` hook in `app.js`.

```
// assets/js/app.js

Hooks.InitUser = {
  mounted () {
    addUserConnection(this.el.dataset.userUuid)
  },

  destroyed () {
    removeUserConnection(this.el.dataset.userUuid)
  }
}
```

Nice! On mount of this element (_i.e._ a user has entered), this hook will add the new user to our `users` variable. When the element is destroyed _i.e._ a user has left), we remove this user from our `users` variable.

Note how LiveView gives you access to the underlying element of the hook, making it easy for us to grab the UUID we placed in `data-user-uuid`. We’ll see later that LiveView also allows us to send data back to the server via `this`.

## Creating the Peer Connection

Up until this point, we’ve been in familiar territory—Phoenix, LiveView, a little JS. But now it’s time to dig into the meat of WebRTC, the peer connection. Remember that in a mesh architecture, each of our users will have a peer connection with each other. Now that we have a place to keep track of these peer connections, let’s make a function to create them, `createPeerConnection()`. This function may seem confusing, so we’re going to take it slow. Open up `app.js` and add the following.

```
// lv       - Our LiveView hook's `this` object.
// fromUser - The user to create the peer connection with.
// offer    - Stores an SDP offer if it was passed to the function.
function createPeerConnection(lv, fromUser, offer) {
  // Creates a variable for our peer connection to reference within
  // this function's scope.
  let newPeerConnection = new RTCPeerConnection({
    iceServers: [
      // We're going to get into STUN servers later, but for now, you
      // may use ours for this portion of development.
      { urls: "stun:littlechat.app:3478" }
    ]
  })

  // Add this new peer connection to our `users` object.
  users[fromUser].peerConnection = newPeerConnection;

  // Add each local track to the RTCPeerConnection.
  localStream.getTracks().forEach(track => newPeerConnection.addTrack(track, localStream))

  // If creating an answer, rather than an initial offer.
  if (offer !== undefined) {
    newPeerConnection.setRemoteDescription({type: "offer", sdp: offer})
    newPeerConnection.createAnswer()
      .then((answer) => {
        newPeerConnection.setLocalDescription(answer)
        console.log("Sending this ANSWER to the requester:", answer)
        lv.pushEvent("new_answer", {toUser: fromUser, description: answer})
      })
      .catch((err) => console.log(err))
  }

  newPeerConnection.onicecandidate = async ({candidate}) => {
    // fromUser is the new value for toUser because we're sending this data back
    // to the sender
    lv.pushEvent("new_ice_candidate", {toUser: fromUser, candidate})
  }

  // Don't add the `onnegotiationneeded` callback when creating an answer due to
  // a bug in Chrome's implementation of WebRTC.
  if (offer === undefined) {
    newPeerConnection.onnegotiationneeded = async () => {
      try {
        newPeerConnection.createOffer()
          .then((offer) => {
            newPeerConnection.setLocalDescription(offer)
            console.log("Sending this OFFER to the requester:", offer)
            lv.pushEvent("new_sdp_offer", {toUser: fromUser, description: offer})
          })
          .catch((err) => console.log(err))
      }
      catch (error) {
        console.log(error)
      }
    }
  }

  // When the data is ready to flow, add it to the correct video.
  newPeerConnection.ontrack = async (event) => {
    console.log("Track received:", event)
    document.getElementById(`video-remote-${fromUser}`).srcObject = event.streams[0]
  }

  return newPeerConnection;
}
```

That was a lot of code, so let’s break it down step by step.

Remember those 18 easy steps for video calling? We’ve essentially created the client-side of these steps. You’ll note that we called `lv.pushEvent` a few times. This sends our LiveView a specific message to be passed on to the given `toUser`. We will be implementing the functions for handling these messages later on.

Right at the start of the function, we create a peer connection. Note that we added in what’s called a STUN server. If you’ve done any research on WebRTC, you’ve probably encountered this term. A STUN server essentially just figures out where your computer is and ways to connect to it. It then sends these “addresses” back as ICE candidates. This is necessary because most people’s computers aren’t connected to public-facing IP addresses, but rather to more complex internal networks. We will be adding a STUN server to the application later, but for now, feel free to use ours for development.

Next, we add this newly-created peer connection to our `users` object from earlier.

After this, we add our `localStream` (our webcam and microphone) to the peer connection. This tells the peer connection we just created that we want to send this stream over the connection.

We then have code for handling the creation of an answer if `offer` exists, and then sending it back to `fromUser` via the server using our `lv` object.

Specifically, if an offer was passed in, our function will set the remote description to the `offer` and then call `createAnswer` on the peer connection. It sets the peer connection’s `localDescription` to the new answer and the sends the answer to the server to be forwarded back to `fromUser`.

We then add our `onicecandidate` callback as an async function that simply passes any new ICE candidates returned by our STUN server (there’s usually around 5-8) on to our `fromUser` via the signaling server.

We then add a callback for `onnegotiationneeded` to our peer connection. If `offer` is undefined, this callback will create an offer, set its `localDescription` to that offer, and then pass the offer to `fromUser` via the signaling server (our LiveView).

Finally, we add a callback for `ontrack`, which simply adds the remote peer’s video track to the proper video when the two peers have established a connection.

## Building the Signaling Server

Now that we’ve built out our main functions for managing our data and peer connections, we need to add the remaining signal server and JS glue to get the whole thing working. The most logical way to do this is by coding in the way that our application would work through its flow. As we do this, feel free to reference the flow reference above.

Our next task will be adding an ability for a user to request offers from all of the other users. This will kickstart the offer-answer WebRTC flow, but allow it to be flexible with all users. Let’s get started by adding a `phx-click` attribute to our Join Call button like this:

```
<button class="button" phx-hook="JoinCall" phx-click="join_call">Join Call</button>
```

Easy. To implement the server-side of this button, we’ll want to add functionality that gets every other connected user and then sends them a message asking for a call offer. To do this, we’ll first need a mechanism for sending a message to a specific user. The most straightforward way to implement this is by subscribing each user to their own PubSub topic and then pattern matching on messages received. Let’s do this.

First, let’s subscribe our users on mount to their own topic. While we’re at it, let’s add an empty list for our `@offer_requests` assign, to keep track of offer requests.

```
# lib/littlechat_web/live/room/show_live.ex

defmodule LittlechatWeb.Room.ShowLive do
  # ...

  @impl true
  def mount(%{"slug" => slug}, _session, socket) do
    user = create_connected_user()

    Phoenix.PubSub.subscribe(Littlechat.PubSub, "room:" <> slug)

+   Phoenix.PubSub.subscribe(Littlechat.PubSub, "room:" <> slug <> ":" <> user.uuid)

    {:ok, _} = Presence.track(self(), "room:" <> slug, user.uuid, %{})

    case Organizer.get_room(slug) do
      nil ->
        {:ok,
          socket
          |> put_flash(:error, "That room does not exist.")
          |> push_redirect(to: Routes.room_new_path(socket, :new))
        }
      room ->
        {:ok,
          socket
          |> assign(:room, room)
          |> assign(:user, user)
          |> assign(:slug, slug)
          |> assign(:connected_users, [])
+         |> assign(:offer_requests, [])
        }
    end
  end

  # ...
end
```

Great, now let’s create a function for sending a direct message to another user. Add the following private function to `show_live.ex`:

```
defp send_direct_message(slug, to_user, event, payload) do
  LittlechatWeb.Endpoint.broadcast_from(
    self(),
    "room:" <> slug <> ":" <> to_user,
    event,
    payload
  )
end
```

Now that we have a method for sending messages, let’s add code to send a message to each connected user requesting an offer when the `join_call` button is clicked. Add the following to your `ShowLive` LiveView.

```
# lib/littlechat_web/live/room/show_live.ex

defmodule LittlechatWeb.Room.ShowLive do
  # ...

  @impl true
  def handle_event("join_call", _params, socket) do
    for user <- socket.assigns.connected_users do
      send_direct_message(
        socket.assigns.slug,
        user,
        "request_offers",
        %{
          from_user: socket.assigns.user
        }
      )
    end

    {:noreply, socket}
  end

  # ...
end
```

Now we can send offer requests to every other connected user, but we need to allow them to process these requests. First, we’ll handle the new message:

```
# lib/littlechat_web/live/room/show_live.ex

defmodule LittlechatWeb.Room.ShowLive do
  # ...

  @impl true
  @doc """
  When an offer request has been received, add it to the `@offer_requests` list.
  """
  def handle_info(%Broadcast{event: "request_offers", payload: request}, socket) do
    {:noreply,
      socket
      |> assign(:offer_requests, socket.assigns.offer_requests ++ [request])
    }
  end

  # ...
end
```

Next, we’ll add a hidden HTML tag for each item in the `@offer_requests` assign. We do this so that we can send a WebRTC offer back to the requesting user when an offer request is received. We have to use this hook mechanism so that we can access WebRTC functions in the browser.

```
# lib/littlechat_web/live/room/show_live.ex

defmodule LittlechatWeb.Room.ShowLive do
  # ...

  @impl true
  def render(assigns) do
    ~L"""
    <h1><%= @room.title %></h1>
    <h3>Connected Users:</h3>
    <ul>
    <%= for {uuid, _} <- @connected_users do %>
      <li><%= uuid %></li>
    <% end %>
    </ul>

    <div class="streams">
      <video id="local-video" playsinline autoplay muted width="600"></video>

      <%= for uuid <- @connected_users do %>
        <video id="video-remote-<%= uuid %>" data-user-uuid="<%= uuid %>" playsinline autoplay phx-hook="InitUser"></video>
      <% end %>
    </div>

    <button class="button" phx-hook="JoinCall" phx-click="join_call">Join Call</button>

+   <div id="offer-requests">
+     <%= for request <- @offer_requests do %>
+     <span phx-hook="HandleOfferRequest" data-from-user-uuid="<%= request.from_user.uuid %>"></span>
+     <% end %>
+   </div>
    """
  end

  # ...
end
```

Great, let’s hook in our JS to create a peer connection. Now that we’ve implemented our `createPeerConnection()` function, everything on the JS end should be pretty smooth.

```
// assets/js/app.js


Hooks.HandleOfferRequest = {
  mounted () {
    console.log("new offer request from", this.el.dataset.fromUserUuid)
    let fromUser = this.el.dataset.fromUserUuid
    createPeerConnection(this, fromUser)
  }
```

If you try out this code, you’ll notice that we’re missing implementation for some of those `lv.pushEvent` calls in our `createPeerConnection()` function. Let’s fix that. Let’s open up our LiveView and implement the remaining functions.

```
# lib/littlechat_web/live/room/show_live.ex

defmodule LittlechatWeb.Room.ShowLive do
  # ...

  @impl true
  def handle_event("new_ice_candidate", payload, socket) do
    payload = Map.merge(payload, %{"from_user" => socket.assigns.user.uuid})

    send_direct_message(socket.assigns.slug, payload["toUser"], "new_ice_candidate", payload)
    {:noreply, socket}
  end

  @impl true
  def handle_event("new_sdp_offer", payload, socket) do
    payload = Map.merge(payload, %{"from_user" => socket.assigns.user.uuid})

    send_direct_message(socket.assigns.slug, payload["toUser"], "new_sdp_offer", payload)
    {:noreply, socket}
  end

  @impl true
  def handle_event("new_answer", payload, socket) do
    payload = Map.merge(payload, %{"from_user" => socket.assigns.user.uuid})

    send_direct_message(socket.assigns.slug, payload["toUser"], "new_answer", payload)
    {:noreply, socket}
  end

  @impl true
  def handle_info(%Broadcast{event: "new_ice_candidate", payload: payload}, socket) do
    {:noreply,
      socket
      |> assign(:ice_candidate_offers, socket.assigns.ice_candidate_offers ++ [payload])
    }
  end

  @impl true
  def handle_info(%Broadcast{event: "new_sdp_offer", payload: payload}, socket) do
    {:noreply,
      socket
      |> assign(:sdp_offers, socket.assigns.ice_candidate_offers ++ [payload])
    }
  end

  @impl true
  def handle_info(%Broadcast{event: "new_answer", payload: payload}, socket) do
    {:noreply,
      socket
      |> assign(:answers, socket.assigns.answers ++ [payload])
    }
  end

  # ...
end
```

Notice that each respective `handle_event/3` and `handle_info/2` implements the same function with different assigns and events for pattern matching. Also note that each `handle_event/3` has a corresponding `handle_info/2`. Think of the `handle_event/3` as the dispatcher that sends the message and the `handle_info/2` as the receiver who handles the message.

Now that we have these callbacks are built out, our final step is adding their associated hooks. We’re going to be repeating from our offer request pattern and create hooks based on our assigns. Let’s do that.

```
# lib/littlechat_web/live/room/show_live.ex

defmodule LittlechatWeb.Room.ShowLive do
  # ...

  @impl true
  def render(assigns) do
    ~L"""
    <h1><%= @room.title %></h1>
    <h3>Connected Users:</h3>
    <ul>
    <%= for {uuid, _} <- @connected_users do %>
      <li><%= uuid %></li>
    <% end %>
    </ul>

    <div class="streams">
      <video id="local-video" playsinline autoplay muted width="600"></video>

      <%= for uuid <- @connected_users do %>
        <video id="video-remote-<%= uuid %>" data-user-uuid="<%= uuid %>" playsinline autoplay phx-hook="InitUser"></video>
      <% end %>
    </div>

    <button class="button" phx-hook="JoinCall" phx-click="join_call">Join Call</button>

    <div id="offer-requests">
      <%= for request <- @offer_requests do %>
      <span phx-hook="HandleOfferRequest" data-from-user-uuid="<%= request.from_user.uuid %>"></span>
      <% end %>
    </div>

+   <div id="sdp-offers">
+     <%= for sdp_offer <- @sdp_offers do %>
+     <span phx-hook="HandleSdpOffer" data-from-user-uuid="<%= sdp_offer["from_user"] %>" data-sdp="<%= sdp_offer["description"]["sdp"] %>"></span>
+     <% end %>
+   </div>
+
+   <div id="sdp-answers">
+     <%= for answer <- @answers do %>
+     <span phx-hook="HandleAnswer" data-from-user-uuid="<%= answer["from_user"] %>" data-sdp="<%= answer["description"]["sdp"] %>"></span>
+     <% end %>
+   </div>
+
+   <div id="ice-candidates">
+     <%= for ice_candidate_offer <- @ice_candidate_offers do %>
+     <span phx-hook="HandleIceCandidateOffer" data-from-user-uuid="<%= ice_candidate_offer["from_user"] %>" data-ice-candidate="<%= Jason.encode!(ice_candidate_offer["candidate"]) %>"></span>
+     <% end %>
+   </div>
    """
  end

  @impl true
  def mount(%{"slug" => slug}, _session, socket) do
    user = create_connected_user()

    Phoenix.PubSub.subscribe(Littlechat.PubSub, "room:" <> slug)

    Phoenix.PubSub.subscribe(Littlechat.PubSub, "room:" <> slug <> ":" <> user.uuid)

    {:ok, _} = Presence.track(self(), "room:" <> slug, user.uuid, %{})

    case Organizer.get_room(slug) do
      nil ->
        {:ok,
          socket
          |> put_flash(:error, "That room does not exist.")
          |> push_redirect(to: Routes.room_new_path(socket, :new))
        }
      room ->
        {:ok,
          socket
          |> assign(:room, room)
          |> assign(:user, user)
          |> assign(:slug, slug)
          |> assign(:connected_users, [])
          |> assign(:offer_requests, [])
+         |> assign(:ice_candidate_offers, [])
+         |> assign(:sdp_offers, [])
+         |> assign(:answers, [])
        }
    end
  end

  # ...
end
```

This is still pretty straightforward. The only item of note here is our ICE candidate hook. You’ll notice that we encoded our ICE candidate data into our hook’s dataset. This is necessary because adding an ICE candidate requires more data values than SDP offers and answers need, so we need to pass the whole payload directly back to our JS. We could theoretically do this with our offers and answers as well, but it’s best practice to avoid unnecessary JSON encoding and decoding.

We’re so close to a working video call application! The only thing that’s missing is our LiveView hooks! Let’s build those.

```
// assets/js/app.js

Hooks.HandleIceCandidateOffer = {
  mounted () {
    let data = this.el.dataset
    let fromUser = data.fromUserUuid
    let iceCandidate = JSON.parse(data.iceCandidate)
    let peerConnection = users[fromUser].peerConnection

    console.log("new ice candidate from", fromUser, iceCandidate)

    peerConnection.addIceCandidate(iceCandidate)
  }
}

Hooks.HandleSdpOffer = {
  mounted () {
    let data = this.el.dataset
    let fromUser = data.fromUserUuid
    let sdp = data.sdp

    if (sdp != "") {
      console.log("new sdp OFFER from", data.fromUserUuid, data.sdp)

      createPeerConnection(this, fromUser, sdp)
    }
  }
}

Hooks.HandleAnswer = {
  mounted () {
    let data = this.el.dataset
    let fromUser = data.fromUserUuid
    let sdp = data.sdp
    let peerConnection = users[fromUser].peerConnection

    if (sdp != "") {
      console.log("new sdp ANSWER from", fromUser, sdp)
      peerConnection.setRemoteDescription({type: "answer", sdp: sdp})
    }
  }
}
```

`HandleIceCandidateOffer`, which is called whenever a new ICE candidate has been received, adds the ICE candidate for the peer connection for the user who sent the ICE candidate.

`HandleSdpOffer`, which is called whenever a new offer has been received, creates a new SDP answer for the given user using the `createPeerConnection()` function with its third parameter (the offer).

Finally, `HandleAnswer`, which is called whenever a new answer has been received, sets the given answer as a remote description for the peer connection for the given user.

Important here is that we are always working with a peer connection for user on the other side of the connection. So if User A has received an answer from User C, it will use the `users` object to work with the existing peer connection for User C. This implementation is what allows us to work with multiple users.

Are you still with me? Because we just finished our implementation of a video chat application! Either [deploy the application](https://github.com/littlelines/littlechat#deployment) or [ngrok](https://ngrok.com/) a tunnel, create a room, and then send the link to a friend (or three)! Once you’re both in the room, you just need to press “Join Call” and the connection will start!

## Bonus: The STUN Server

We’ve touched on the concept of the STUN server, the element of WebRTC that helps us tell where on the internet our peers are. But, we’ve been working off of the [production Littlechat](https://littlechat.app/) STUN server. That’s okay for development, but it’s so easy to configure a STUN server in our Phoenix app that we might as well add one.

Thankfully, there are already a few STUN server implementations out there in Elixir and Erlang. (Lucky for us, or this would be a much longer tutorial!) We’re going to use one written in Erlang called, conveniently, [stun](https://github.com/processone/stun).

Looking at their docs, it seems easy enough to start the server in Erlang:

```
application:start(stun).
stun_listener:add_listener(3478, udp, []).
```

How would we translate this to Elixir?

```
:stun_listener.add_listener(3478, :udp, [])
```

Add `{:stun, "~> 1.0"}` to your `mix.exs` and run `mix deps.get`. If you have issues compiling, like I did, [you’ll need to add your OpenSSL headers.](https://github.com/processone/ejabberd/issues/1107#issuecomment-217828211)

Now let’s create a [GenServer](https://hexdocs.pm/elixir/GenServer.html) to start our STUN server with our Phoenix application on startup.

Create a new file: `lib/littlechat_web/stun.ex`.

```
# lib/littlechat_web/stun.ex

defmodule LittlechatWeb.Stun do
  use GenServer

  def start_link(_) do
    GenServer.start_link(__MODULE__, [])
  end

  @impl true
  @doc """
  Starts the Erlang STUN server at port 3478.
  """
  def init(_) do
    :stun_listener.add_listener(3478, :udp, [])

    {:ok, []}
  end
end
```

Now let’s add this GenServer to our application’s supervision tree, beneath our endpoint.

```
# lib/littlechat/application.ex

defmodule Littlechat.Application do
  # See https://hexdocs.pm/elixir/Application.html
  # for more information on OTP Applications
  @moduledoc false

  use Application

  def start(_type, _args) do
    children = [
      # Start the Ecto repository
      Littlechat.Repo,
      # Start the Telemetry supervisor
      LittlechatWeb.Telemetry,
      # Start the PubSub system
      {Phoenix.PubSub, name: Littlechat.PubSub},
      # Start the Endpoint (http/https)
      LittlechatWeb.Presence,
      LittlechatWeb.Endpoint,
+     LittlechatWeb.Stun
      # Start a worker by calling: Littlechat.Worker.start_link(arg)
      # {Littlechat.Worker, arg}
    ]

    # See https://hexdocs.pm/elixir/Supervisor.html
    # for other strategies and supported options
    opts = [strategy: :one_for_one, name: Littlechat.Supervisor]
    Supervisor.start_link(children, opts)
  end

  # Tell Phoenix to update the endpoint configuration
  # whenever the application is updated.
  def config_change(changed, _new, removed) do
    LittlechatWeb.Endpoint.config_change(changed, removed)
    :ok
  end
end
```

Now, our STUN server will also start when our Phoenix app starts up. Once you have the app deployed, replace the STUN server in `app.js` with your new STUN server. Make sure that whatever port you pick for your STUN server isn’t blocked.

```
function createPeerConnection(lv, fromUser, offer) {
  let newPeerConnection = new RTCPeerConnection({
    iceServers: [
-     { urls: "stun:littlechat.app:3478" }
+     { urls: "stun:myserver.com:3478" }
    ]
  })

  // ...
}
```

If everything went well, your video calling should be working great, with ICE candidates flowing.

## Where to now?

As you can see, there’s a lot that goes into building a working video chat application, especially for more than two users. And of course, as you scale to more users, things even more complex. But now that we have a base of knowledge and an application to build upon, it’s much easier to experiment, learn, and customize our application to our liking. And I must say, hopping on a video call in an application you built yourself is a pretty great feeling.

Here at Littlelines, we specialize in breaking down complex product requirements—connecting the dots between business requirements and a finished product your customers will love. [If we sound like a good fit for your business, let’s start a conversation.](https://littlelines.com/contact)
