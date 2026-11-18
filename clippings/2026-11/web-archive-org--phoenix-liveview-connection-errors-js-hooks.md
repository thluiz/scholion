---
url: "https://web.archive.org/web/20200808211521id_/https://curiosum.dev/blog/elixir-phoenix-liveview-messenger-part-4"
captured_at: "2026-11-18T11:30:34+00:00"
title: "Phoenix LiveView Tutorial: Handling Connection Errors And Push Notifications With JS Hooks – Curiosum"
domain: "web-archive-org"
---

> ### Psst! Don't forget to [subscribe to our newsletter](#c-newsletter) as there's still more to come.

## A brutal wake-up call...

We were keen to point out that Phoenix LiveView can be treated as an alternative to reactive UI frameworks such as React or Vue.

While this is true, let's think about what can go wrong with full reliance on Phoenix LiveView's proposed approach.

> ### Server-side statefulness, which is Phoenix LiveView's major selling point, can also be seen as its major weakness, creating several challenges to resolve.

**HTTP is stateless by nature.** You pass and mutate cookies back and forth between the browser and the server to create an illusion of state, storing a set of data - a session.

What happens in HTTP when the server's down? **HTTP is stateless, so there's not much to worry about. You have your cookies on the browser side of things.**

What happens in HTTP when the connection's down? Ditto. Well, [technically there is not even such a thing as a connection in HTTP](https://www.tutorialspoint.com/http/http_overview.htm).

What happens in HTTP when an unhandled server exception occurs in data processing? **HTTP is stateless, so there's not much to worry about. The server will bail out by throwing a 500, but remains stable and responds to requests, and you still have your state in the cookie.**

### With LiveView, forget what you're used to in HTTP.

Each instance of a user seeing a LiveView is backed by a stateful Elixir process supervised inside an Erlang VM instance. So whatever you'd like to call a _session_ is part of the process's internal state.

What happens when the server is down? Suppose that the whole Erlang VM has crashed. **By default, any state that may have been present is obviously lost.**

What happens when the connection is down? Well, Phoenix Channels (backing all LiveViews) are monitored, and [when a channel is down, the LiveView process is terminated](https://github.com/phoenixframework/phoenix_live_view/blob/13efe28dc6298d0be622f71a1bf69a0a06ecc740/lib/phoenix_live_view/channel.ex#L40). **Therefore, state is lost.**

What happens when an unhandled LiveView process exception occurs? **This means the function that processes a state transition has no way to transform the process to a next state, so the process crashes. State is lost.**

**Let's see how we can overcome some of the challenges we've identified.**

## Reconnecting to the server

As we've noted, regardless of whether it's caused by the server going entirely down, or by losing connection between the browser at the server, it causes the LiveView process to lose its current state.

We'll do a quick test - by the way, we'll also look at how Phoenix LiveView marks "dead" LiveViews in a page. Let's go to `/assets/css/app.css` and append the following line:

```
@import "../../deps/phoenix_live_view/assets/css/live_view.css";
```

This will pluck a small stylesheet bundle from LiveView's webpack assets.

If you peek into its code, you'll notice that it uses `.phx-disconnected` and `.phx-error` selectors to visually mark tags that contain malfunctioning LiveView components. And indeed, this is how LiveView's bundled JS code annotates them when problems occur.

This can be important, because **it allows the developer to identify these DOM elements as belonging to a failing LiveView**, which is important from a UX standpoint - it needs to be clear that e.g. a form inside such a failing view cannot be interacted with.

Before we proceed and start the server to test it out, let's **temporarily disable watching for file changes and live-reloading the app's pages**, because this would interfere with what we want to test here. To do this, jump into `/lib/curious_messenger_web/endpoint.ex` and find and comment out the line that declares `plug Phoenix.LiveReloader`. Its surroundings should look like this:

```
if code_reloading? do
  socket "/phoenix/live_reload/socket", Phoenix.LiveReloader.Socket
  # plug Phoenix.LiveReloader
  plug Phoenix.CodeReloader
end
```

Let's now open up the server by executing `mix.phx.server`, navigate to http://localhost:4000 and sign into a registered user.

If you dig into the DOM inspector at this point, you'll notice that there is a `<div>` element that has the `.phx-connected` class - this is the LiveView's main container.

Since our LiveView's internal state is represented by a changeset corresponding to our "Create Conversation" form, storing IDs of users to be added, let's add them to the to-be-created conversation, but **instead of submitting the creation form, terminate the Phoenix server**. Here is what you should see:

![Phoenix LiveView Messenger App - LiveView Disconnected From Server](https://i.imgur.com/7Loe5lr.png "Phoenix LiveView Messenger App - LiveView Disconnected From Server")

Note that, as we said, the element now becomes annotated with `.phx-disconnected` and `.phx-error`, and the bundled CSS provides a basic way to distinguish a failed component from the rest of the page by marking it with a red background, a spinner and a changed mouse pointer.

Now let's start the Phoenix server again. The browser will reconnect to the server promptly, but **clearly the form will now be in its initial state, with nobody but the current user added to the conversation**.

To test the scenario of a user's connection going down while the server is still up, connect to the app using your local IP address (as opposed to `localhost` which uses a loopback interface) and disconnect from your network - and then reconnect - you'll again notice that the form is now back in the initial state, which means that the process that held the pre-disconnect state has been terminated.

This is actually good, because having to deal with dangling processes of lost LiveView connections would be disastrous. But it obviously also means that we need to make some conscious decisions about how we deal with reconnecting, if the LiveView's state contains some non-persistent data.

We'll look into how to tackle this in a moment. Now let's create a conversation and get into its view, and we'll see if we need to do anything with `ConversationLive` with regard to behavior on reconnecting.

One could imagine that the most annoying thing that could happen is to lose a message you've been typing when connection issues occur. Will it happen? Let's find out: type in a message and close the server instead of submitting.

![Phoenix LiveView Messenger App - Conversation Disconnected From Server](https://i.imgur.com/cwPeqwK.png "Phoenix LiveView Messenger App - Conversation Disconnected From Server")

Reopen the server. **You surely have noticed that the message is still there.** Isn't that inconsistent with what we've seen with the behaviour of `DashboardLive`? Let's do one more experiment to find out what's going on.

Go into `/lib/curious_messenger_web/templates/conversation/show.html.leex` and find the line that declares the message content field:

```
<%= text_input f, :content %>
```

...and modify it to have a programmatically assigned value - it needn't be anything meaningful, let's just use a function from Erlang's `:rand` module:

```
<%= text_input f, :content, value: :rand.uniform() %>
```

Refresh the page. You'll see a number entered into the "Content" field. Now enter whatever text you want in that field, close the server and reopen it. **You'll notice that the text you had entered is lost, and there is a different random number entered in the field now.**

Long story short, **Phoenix LiveView is [very good at splitting templates into static and dynamic parts](https://hexdocs.pm/phoenix_live_view/Phoenix.LiveView.Engine.html#content), as well as identifying those elements in the DOM that needn't be replaced**. While the `<%= text_input f, :content %>` line is dynamic by nature regardless of whether there's a random number used there, it is rendered identically every single time - so it doesn't need to be replaced, because changing the field's value doesn't create any DOM change.

## Controlling reconnection, restoring state

Coming back to the `DashboardLive` module - we elected to store the form's state as an `Ecto.Changeset` because it's pretty idiomatic to anyone familiar with Ecto and very easy to persist once we're done with selecting contacts to chat with. It's easy to reason about changesets when there are forms that correspond to a specific Ecto schema defining a changeset - in this case, we've got a `Conversation` that accepts nested attributes for associated `ConversationMember` records.

The changeset is a part of the component's state which can't be easily retrieved from elsewhere, so let's think of how we can make it at least a bit fail-safe.

If we wanted to make the form state remain intact between page visits, we could think of server-side solutions such as continously storing data related to the current user's form state in the relational database (PostgreSQL), [Mnesia](https://elixirschool.com/pl/lessons/specifics/mnesia/) or [the Erlang Term Storage](https://elixirschool.com/pl/lessons/specifics/ets/) (the latter being non-persistent, though). Stored data would then be retrieved at the moment the LiveView is mounted.

One could be tempted to think about cookies. But we don't want to use classic HTTP, and Phoenix's secure session cookie cannot be manipulated without getting into the HTTP request-response cycle - which we don't want to do.

With client-side (or mixed) approaches, it gets a bit more complicated. Depending on the nature of processed data, it might be acceptable to use browser's mechanisms such as `localStorage` to store the form's state. And, finally, there is the need to actually **write some JS code** to feed the LiveView with an initial, post-reconnect state.

Since in the case of the "Create Conversation" form we don't necessarily need it to be persistent between page reloads, we'll only **make it fail-safe in reconnection scenarios** described earlier.

### JavaScript Hooks

**Phoenix LiveView allows us to write JS functions reacting to a LiveView instance's lifecycle events.** According to [the documentation](https://hexdocs.pm/phoenix_live_view/Phoenix.LiveView.html#module-js-interop-and-client-controlled-dom), we can react to the following events:

*   `mounted` - the element has been added to the DOM and its server LiveView has finished mounting
*   `updated` - the element has been updated in the DOM by the server
*   `destroyed` - the element has been removed from the page, either by a parent update, or the parent being removed entirely
*   `disconnected` - the element's parent LiveView has disconnected from the server
*   `reconnected` - the element's parent LiveView has reconnected to the server

Create a `/assets/js/create_conversation_form_hooks.js` file:

```
const CreateConversationFormHooks = {
  disconnected() {
    console.log("Disconnected", this)
  },

  reconnected() {
    console.log("Reconnected", this)
  },

  mounted() {
    console.log("Mounted", this)
  },

  destroyed() {
    console.log("Destroyed", this)
  },

  disconnected() {
    console.log("Disconnected", this)
  },

  updated() {
    console.log("Updated", this)
  }
}

export default CreateConversationFormHooks
```

In `/assets/js/app.js`, ensure that the hooks are loaded and passed to the constructor of `LiveSocket`. Let's have the file contain exactly the following code (excluding comments):

```
import css from "../css/app.css"
import "phoenix_html"

import { Socket } from "phoenix"
import LiveSocket from "phoenix_live_view"
import CreateConversationFormHooks from "./create_conversation_form_hooks";

let Hooks = { CreateConversationFormHooks };

let liveSocket = new LiveSocket("/live", Socket, { hooks: Hooks })
liveSocket.connect()
```

Fine, but how does LiveView know what view instance to react on? For this purpose, we annotate an element within a template with the `phx-hook` attribute. In this case, we'll do this with the form we use for creating a conversation.

In `/lib/curious_messenger_web/templates/dashboard/show.html.leex`, let's have the form declared like this:

```
<%= form_for @conversation_changeset, "", [phx_submit: :create_conversation, phx_hook: "CreateConversationFormHooks"], fn f -> %>
...
<% end %>
```

If you open up your browser's developer tools and refresh the page at this point, you'll be able to observe what events are initially triggered - clearly these are `mounted` and `updated`. When you do anything that makes the LiveView update its state (e.g. add a conversation member), the `updated` event is fired again. The `destroyed` event would be triggered when e.g. a LiveView (possibly nested) completely disappears from the page - experience tells that it is not a reliable event on e.g. a page exit.

Now, try closing and restarting the Phoenix server, and here's what you'll probably end up with:

![Phoenix LiveView Messenger App - Lifecycle Events Logged With JS Hooks](https://i.imgur.com/fgOsn1S.png "Phoenix LiveView Messenger App - Lifecycle Events Logged With JS Hooks")

Most importantly, `disconnected` and `reconnected` happened. Conceptually, what we'd like to do is serialize the form to a changeset-friendly representation (e.g. URL-encoded form data) and send it over the LiveView's WebSocket connection when the server is up again (`reconnected`).

Inside these hook functions, `this` is a special object encapsulating the client-side LiveView representation and allowing us to **communicate with the server, most importantly to send events that we'll handle in Elixir using `handle_event` callbacks**.

Let's now change the `reconnected` function definition to the following:

```
  reconnected() {
    console.log("Reconnected", this)
    let formData = new FormData(this.el)
    let queryString = new URLSearchParams(formData)
    this.pushEvent("restore_state", { form_data: queryString.toString() })
  }
```

This will serialize the form into a form that we'll then convert into a changeset at the Elixir side. Recall that, at this point, the LiveView has been mounted and its process is up and running, so let's make it respond to the `restore_state` event we send from JS code. In `/lib/curious_messenger_web/live/dashboard_live.ex`, add a new clause for `handle_event/3`:

```
  def handle_event("restore_state", %{"form_data" => form_data}, socket) do
    # Decode form data sent from the pre-disconnect form
    decoded_form_data = Plug.Conn.Query.decode(form_data)

    # Since the new LiveView has already run the mount function, we have the changeset assigned
    %{assigns: %{conversation_changeset: changeset}} = socket

    # Now apply decoded form data to that changeset
    restored_changeset =
      changeset
      |> Conversation.changeset(decoded_form_data["conversation"])

    # Reassign the changeset, which will then trigger a re-render
    {:noreply, assign(socket, :conversation_changeset, restored_changeset)}
  end
```

Psst! If you follow this pattern in multiple LiveViews, do yourself a favor and extract this into a reusable module.

**Now, when you try disconnecting and reconnecting again, your "Create Conversation" form will be restored to the pre-disconnect state.**

## Reacting to new conversations

As an exercise at the end of our [previous episode](https://curiosum.dev/blog/elixir-phoenix-liveview-messenger-part-3), we suggested that you can (and should) use Phoenix PubSub to notify a user's DashboardLive view when they've got a new conversation they participate in.

Again, to recap, it's just about making conversation creation broadcast a notification to all interested members - let's go to `/lib/curious_messenger/chat.ex` and rework the `create_conversation` function:

```
  def create_conversation(attrs \\ %{}) do
    result =
      %Conversation{}
      |> Conversation.changeset(attrs)
      |> Repo.insert()

    case result do
      {:ok, conversation} ->
        conversation.conversation_members
        |> Enum.each(
          &CuriousMessengerWeb.Endpoint.broadcast!(
            "user_conversations_#{&1.user_id}",
            "new_conversation",
            conversation
          )
        )

        result

      _ ->
        result
    end
  end
```

This needs to be reacted to in `DashboardLive`, so we need to make changes in `/lib/curious_messenger_web/live/dashboard_live.ex`.

In the `mount/2` callback, insert the following code at the beginning:

```
  def mount(%{current_user: current_user}, socket) do
    CuriousMessengerWeb.Endpoint.subscribe("user_conversations_#{current_user.id}")
    
    # prior implementation
  end
```

Since the information about a new conversation being created can now come from elsewhere as well as from self, we'll now handle this information in `handle_info` instead of `handle_event` - the latter's clause for `create_conversation` can now be simplified:

```
  def handle_event("create_conversation", %{"conversation" => conversation_form},
                   %{assigns: %{conversation_changeset: changeset, contacts: contacts}} = socket) do
    title = if conversation_form["title"] == "" do
              build_title(changeset, contacts)
            else
              conversation_form["title"]
            end

    conversation_form = Map.put(conversation_form, "title", title)

    case Chat.create_conversation(conversation_form) do
      {:ok, _} ->
        {:noreply, socket}

      {:error, err} ->
        Logger.error(inspect(err))
        {:noreply, socket}
    end
  end
```

...and a new `handle_info` clause for `new_conversation` can be added:

```
  def handle_info(%{event: "new_conversation", payload: new_conversation}, socket) do
    user = socket.assigns[:current_user]
    user = %{user | conversations: user.conversations ++ [new_conversation]}

    {:noreply, assign(socket, :current_user, user)}
  end
```

This way, users creating conversations for each other will get live updates of their conversation lists.

**How to intercept this event so that, for example, a push notification mechanism can be created?**

Phoenix LiveView itself does not expose an API to push messages _from the server to the browser_; everything that's pushed in this direction is DOM diffs.

You could think of leveraging [Phoenix Channels](https://hexdocs.pm/phoenix/channels.html), also built on top of Phoenix PubSub, to handle this kind of notifications; or, to keep your technological stack thin, **you can just rely on JS `updated` hooks interpreting data present in the new DOM**.

Let's enhance the newly added `handle_info` clause and piggyback a `notify` flag on the newly created record. [Remember how we once explained that a struct is just a map?](https://curiosum.dev/blog/elixir-trickery-cheating-on-structs)

```
  def handle_info(%{event: "new_conversation", payload: new_conversation}, socket) do
    user = socket.assigns[:current_user]
    annotated_conversation = new_conversation |> Map.put(:notify, true)
    user = %{user | conversations: (user.conversations |> Enum.map(&(Map.delete(&1, :notify)))) ++ [annotated_conversation]}

    {:noreply, assign(socket, :current_user, user)}
  end
```

Consume this in the `/lib/curious_messenger_web/templates/dashboard/show.html.leex` view the following way - plugging in the new `ConversationListHooks` that we'll create in a moment into the conversation list.

```
<article class="column" phx-hook="ConversationListHooks">
  <h2>Ongoing Conversations</h2>
  <%= for conversation <- @current_user.conversations do %>
    <div>
      <%= link conversation.title,
          to: Routes.conversation_path(@socket, CuriousMessengerWeb.ConversationLive, conversation.id, @current_user.id),
          data: if Map.get(conversation, :notify), do: [notify: true], else: [] %>
    </div>
  <% end %>
</article>
```

This way, only one conversation link will be annotated with the `data-notify` attribute that we'll then look for in JS code so that we can notify the user about it.

Add the following import to `/assets/js/app.js` and modify the `Hooks` declaration. Also ask the user for permission to display notifications:

```
import ConversationListHooks from "./conversation_list_hooks";
let Hooks = { CreateConversationFormHooks, ConversationListHooks };

Notification.requestPermission() // returns a Promise that we're not much interested in for now
```

...and create a new file in `/assets/js/conversation_list_hooks.js`. Notice that, in this case, `this.el` is the element to which the hook was attached in the HTML template:

```
const ConversationListHooks = {
  updated() {
    let newConversationLink = this.el.querySelector('[data-notify]')
    if (!newConversationLink) return

    let notification = new Notification(newConversationLink.innerText)
    notification.onclick = () => window.open(newConversationLink.href)
  }
}

export default ConversationListHooks
```

**This way, everyone involved with the conversation will now receive a push notification when it is created!** It is slightly imperfect, because the notification will also be displayed to the user who created the conversation. Nonetheless, it is a good starting point to expand the push functionality to messages as well.

![Phoenix LiveView Messenger App - JavaScript Push Notifications On Conversation Creation](https://i.imgur.com/nHSsVHw.png "Phoenix LiveView Messenger App - JavaScript Push Notifications On Conversation Creation")

Let's get to messages now. Add an import and change the hooks declaration again in `/assets/js/app.js`:

```
import ConversationHooks from "./conversation_hooks"

let Hooks = { CreateConversationFormHooks, ConversationListHooks, ConversationHooks }
```

Create a new file in `/assets/js/conversation_hooks.js`. We'll rely on incoming messages - that we want to have notifications on - to have a `data-incoming` attribute.

```
const ConversationHooks = {
  updated() {
    if (!this.notifiedMessages)
      this.notifiedMessages = []
    
    this.el.querySelectorAll('[data-incoming]').forEach(element => {
      if (!this.notifiedMessages.includes(element)) {
        this.notifiedMessages.push(element)
        let notification = new Notification(element.innerText)
        notification.onclick = () => window.focus()    
      }
    })
  }
}

export default ConversationHooks
```

Go to `/lib/curious_messenger_web/templates/conversation/show.html.leex`. Find the `for` loop that renders message markup and replace it like this, so that if a message is annotated with an additional `:incoming` key, the `div` tag should be displayed with an additional data attribute:

```
      <%= for message <- @messages do %>
        <%= if Map.get(message, :incoming) do %>
          <div data-incoming="true">
        <% else %>
          <div>
        <% end %>
          <b><%= message.user.nickname %></b>: <%= message.content %>
        </div>
      <% end %>
```

Then, go to `/lib/curious_messenger_web/live/conversation_live.ex` and modify the definition for `handle_info` dealing with new messages:

```
  def handle_info(%{event: "new_message", payload: new_message}, socket) do
    annotated_message =
      if new_message.user.id != socket.assigns[:user].id do
        new_message |> Map.put(:incoming, true)
      else
        new_message
      end

    updated_messages = socket.assigns[:messages] ++ [annotated_message]

    {:noreply, socket |> assign(:messages, updated_messages)}
  end
```

This time, the message's notification will not appear for the user that sent it.

**You can now test this out - notifications will appear in your conversations!** One caveat is that you'll only see them while the conversation tab is running. \*\*If you'd like to use notifications that don't require the tab to be open, read up on [the Push API and Service Workers](https://developers.google.com/web/ilt/pwa/introduction-to-push-notifications) - and, at the Elixir side of things, get familiar with the [`web_push_encryption` library](https://github.com/danhper/elixir-web-push-encryption).

## What else can go wrong with Phoenix LiveView?

It has to be kept in mind that, in LiveView, with the whole logic behind events and UI updates being on the server side of things.

> ### Server-side event handling makes LiveView far from ideal for aplications that require offline access.

If an application is intended for offline use, it might be a better idea to go for solutions that don't use LiveView for driving the logic behind form controls, and perhaps restrict it to displaying some live-updated data - which, with Phoenix PubSub available, is still very convenient.

You could go more ambitious and **use the `disconnected` hook to create a plug custom logic into your form when it has lost connection**. If you've got an UI whose concept is simple and linear - for instance, let's say you've got a button which you count clicks on - you could try to trace any activity that occurs in the relevant controls (or a form) during the time the connection is down - and push it as events to the server using `pushEvent` when the connection is back. It's not perfect, though, because the UI will still not appear to be reactive during the connection outage.

> ### If your application requires full UI reactivity in offline mode, look for other solutions than Phoenix LiveView for the most critical components.

## Wrapping up

**[Here's the repository of our app, current as of the end of this episode](https://github.com/curiosum-dev/curious_messenger/tree/episode3)**.

There is still some polishing left to do in our app - we'll review the elements of our schema that we haven't covered in the next episode.

Without, though, we've managed to explain a few of the issues you can run into in a production LiveView app, and resolve a few of them - learning how to use JS hooks to react to Phoenix LiveView lifecycle events.

> ### Have you liked the new episode? Give us your feedback [via contact form](https://curiosum.dev/contact) or our social media (don't forget to share using links below). If you don't mind, please also do us a favour and [subscribe to our newsletter](#c-newsletter).
