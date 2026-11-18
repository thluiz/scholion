---
title: "Phoenix LiveView Tutorial: Handling Connection Errors And Push Notifications With JS Hooks"
date: '2020-07-05T14:10:34+00:00'
category: webclip
summary: 'Explains how Phoenix LiveView’s server-side state fails on disconnects and shows how to use JS hooks to restore form state and implement browser notifications for new conversations and messages.'
tags: ["phoenix-liveview", "elixir", "javascript-hooks", "push-notifications"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Phoenix LiveView Tutorial: Handling Connection Errors And Push Notifications With JS Hooks – Curiosum"
    url: "https://web.archive.org/web/20200808211521id_/https://curiosum.dev/blog/elixir-phoenix-liveview-messenger-part-4"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--phoenix-liveview-connection-errors-js-hooks.md"
    kind: repo
---

The article examines how Phoenix LiveView’s server-side state differs from traditional stateless HTTP, and how that affects resilience to server crashes, connection drops and unhandled exceptions. Because each LiveView is backed by a stateful process, failures or disconnects cause state loss, unlike cookie-backed HTTP sessions. The text shows how LiveView marks disconnected or errored components, then introduces JavaScript hooks to react to lifecycle events, restore form state on reconnect, and build notification features using browser APIs.

Using a messenger app as an example, the article walks through wiring JS hooks to LiveView components, serializing form data on reconnect and reapplying it as an Ecto changeset. It then extends LiveView with Phoenix PubSub to broadcast new conversations and messages, and uses `updated` hooks plus data attributes in rendered HTML to trigger browser notifications for new conversations and incoming messages. The piece ends by outlining when LiveView is a poor fit for offline or fully reactive offline UIs and suggests alternatives or more advanced push mechanisms.

## Reading notes

- Phoenix LiveView is contrasted with reactive UI frameworks like React or Vue, but its server-side statefulness introduces different failure characteristics.
- Traditional HTTP is stateless, with session data stored in cookies, so server restarts or connection issues do not inherently destroy client-side session state.
- In HTTP, when the server is down or an unhandled exception occurs, the client still holds cookies and the server can recover by returning error responses while keeping sessions intact.
- With LiveView, each user view is backed by a stateful Elixir process running in the Erlang VM, so the effective session lives in process state.
- If the Erlang VM crashes, any LiveView process state present is lost because it is not persisted by default.
- LiveViews run on Phoenix Channels; when a channel goes down the associated LiveView process is terminated, so its state disappears.
- An unhandled exception in a LiveView process causes the process to crash, which also discards its internal state.
- LiveView provides a CSS bundle that adds `.phx-disconnected` and `.phx-error` classes to DOM elements containing failing LiveViews, allowing developers to visually mark malfunctioning components.
- Importing `live_view.css` gives basic UX hints such as red background, spinner and pointer changes for disconnected LiveViews, signaling that embedded elements like forms cannot be used.
- Disabling `Phoenix.LiveReloader` is suggested to prevent live code reloading from interfering with manual reconnection tests.
- Inspecting the DOM for a running LiveView reveals a container `div` with the `.phx-connected` class, which flips to disconnected/error classes when the server stops.
- When the server is stopped while a changeset-backed form in `DashboardLive` holds data, a reconnect resets the form to its initial state with only the current user selected, confirming state loss.
- Testing via local IP and toggling network connectivity shows that client-side network drops also lead to LiveView process termination and form reset on reconnect.
- The text argues that automatic teardown of LiveView processes for lost connections is positive because it avoids dangling processes, but forces explicit design for recovering non-persistent state.
- In a conversation view, typing a message and then stopping the server appears to retain the typed message after reconnect, which seems inconsistent with `DashboardLive` behavior.
- Changing the message `text_input` to use a dynamic `value: :rand.uniform()` reveals that the previously typed text is lost after reconnect, replaced by a new random number.
- This demonstrates that LiveView optimizes templates by splitting them into static and dynamic parts and skips DOM replacements when markup is rendered identically, so browser-maintained input values can appear preserved.
- The conversation message input without an explicit value attribute renders identically each time, so LiveView avoids replacing it and the browser keeps its value across reconnects.
- For the `DashboardLive` create-conversation form, the changeset state is not easily reconstructed, making this part of LiveView state a candidate for extra resilience mechanisms.
- Server-side persistence strategies for form state could include storing per-user form data in PostgreSQL, Mnesia or ETS and reloading it on LiveView mount.
- Cookies are considered less suitable because Phoenix’s secure session cookie is tied to HTTP request–response cycles and not easily manipulated from LiveView’s WebSocket workflow.
- The text notes that client-side approaches such as `localStorage` may be acceptable depending on data sensitivity, but still require JS code to pass stored state back to LiveView.
- For the create-conversation form, the chosen goal is to make it survive reconnection events without needing persistence across full page reloads.
- Phoenix LiveView exposes JavaScript hooks to handle lifecycle events: `mounted`, `updated`, `destroyed`, `disconnected`, and `reconnected`.
- A `CreateConversationFormHooks` JS object is defined with functions for lifecycle events, and exported from `/assets/js/create_conversation_form_hooks.js`.
- In `/assets/js/app.js`, this hooks module is imported, added to a `Hooks` map, and passed into the `LiveSocket` constructor, then `liveSocket.connect()` is called.
- The template for the create-conversation form is updated with a `phx-hook="CreateConversationFormHooks"` attribute so LiveView knows to attach these hooks to that element.
- When the page loads and the form updates, `mounted` and `updated` hook callbacks are logged; further LiveView updates such as adding conversation members trigger additional `updated` calls.
- The `destroyed` hook is mentioned as firing when a LiveView or nested view disappears, but is described as unreliable for page exits.
- Stopping and restarting the Phoenix server leads to `disconnected` and `reconnected` hook events being logged for the form.
- The author proposes serializing form state on `reconnected` and sending it over the WebSocket using `pushEvent` for server-side restoration.
- Inside hook callbacks, `this` refers to the client-side representation of the hooked LiveView element and provides a `pushEvent` method to communicate with the Elixir process.
- The `reconnected` hook is updated to build a `FormData` from `this.el`, convert it to a URL-encoded query string with `URLSearchParams`, and push a `restore_state` event containing `form_data`.
- On the Elixir side, a new `handle_event("restore_state", ...)` clause decodes the URL-encoded data using `Plug.Conn.Query.decode`.
- The decoded data is applied to the existing `conversation_changeset` taken from socket assigns, using `Conversation.changeset(decoded_form_data["conversation"])`.
- Assigning the restored changeset back to the socket triggers a re-render so the form shows the pre-disconnect state.
- The article suggests extracting this restore logic into a reusable module if used across multiple LiveViews.
- With this pattern in place, disconnecting and reconnecting no longer resets the create-conversation form; it is restored from the serialized state.
- Building on the previous episode, the article revisits Phoenix PubSub to notify a user’s `DashboardLive` when they participate in a new conversation.
- The `Chat.create_conversation` function is modified so that after inserting a new `Conversation`, it iterates over `conversation.conversation_members` and broadcasts a `"new_conversation"` event on a `"user_conversations_#{user_id}"` topic for each member.
- `DashboardLive` subscribes to the `"user_conversations_#{current_user.id}"` topic in `mount/2` using `CuriousMessengerWeb.Endpoint.subscribe`.
- The `handle_event("create_conversation", ...)` callback is simplified to compute a title (building it from contacts if blank), call `Chat.create_conversation`, and either ignore success or log errors.
- A new `handle_info/2` clause handles `%{event: "new_conversation", payload: new_conversation}`, updating the `current_user` assign with an extended `conversations` list including the new conversation.
- This approach lets all participants in a conversation see live updates to their conversation lists when a new conversation is created.
- The text then asks how to intercept these updates for push notification behavior.
- It states that Phoenix LiveView does not provide a direct API for arbitrary server-to-browser messages; server output is limited to DOM diffs.
- As an alternative to adding Phoenix Channels, the article suggests using JS `updated` hooks to interpret new DOM content for notification purposes.
- In `handle_info` for `new_conversation`, the conversation payload is annotated with a `:notify` flag using `Map.put(:notify, true)` before updating the user’s conversations list.
- Existing conversations are mapped through `Map.delete(&1, :notify)` to clear earlier notification markers, and the annotated new conversation is appended.
- The dashboard template conversation list is wrapped in an `<article>` element with `phx-hook="ConversationListHooks"` so a new hook can respond to updates.
- Each conversation link uses `data: if Map.get(conversation, :notify), do: [notify: true], else: []` so that only the most recent conversation carries a `data-notify` attribute.
- In `app.js`, `ConversationListHooks` is imported, added to the `Hooks` object, and `Notification.requestPermission()` is called to enable browser notifications.
- The `ConversationListHooks` JS module defines an `updated` callback that queries `this.el` for a `[data-notify]` link when the DOM updates.
- If such a link exists, the hook creates a new `Notification` with the link’s text and attaches an `onclick` handler that opens the conversation URL in a new window.
- This setup causes all users involved in a new conversation to receive a browser notification, including the creator, which is acknowledged as an imperfection.
- The same pattern is proposed as a basis for message-level notifications.
- A `ConversationHooks` JS module is introduced and added to `Hooks` in `app.js`, targeting conversation-level updates.
- `ConversationHooks.updated` initializes a `notifiedMessages` array on `this` when absent, then selects all elements under `this.el` with `[data-incoming]`.
- For each such element not already tracked, the hook stores it in `notifiedMessages`, creates a `Notification` with its text, and sets `onclick` to refocus the window.
- The conversation template is modified so that each message is wrapped in a `div` that conditionally includes `data-incoming="true"` if `Map.get(message, :incoming)` is present.
- In `ConversationLive`, `handle_info` for `"new_message"` is updated to annotate the `new_message` with `:incoming` when the message author differs from `socket.assigns[:user].id`.
- Annotated messages are appended to the `messages` assign, ensuring only incoming messages carry the `data-incoming` marker and trigger notifications.
- This logic prevents the user who sent a message from receiving a notification for their own outgoing message.
- The article notes that message and conversation notifications work while the conversation tab is open, but not when it is closed.
- For notifications that work without an open tab, readers are pointed to the Push API, Service Workers, and the `web_push_encryption` Elixir library.
- The text cautions that LiveView’s server-side event handling makes it unsuitable for applications that must function offline, since interaction logic lives on the server.
- For offline-oriented apps, LiveView might be limited to displaying live data, while client-side logic handles interactive controls.
- A possible approach is described using the `disconnected` hook to attach custom offline logic to form controls and queue user actions while the connection is down.
- In such a setup, user activity during disconnection could be recorded and then sent back via `pushEvent` when `reconnected` occurs.
- The article points out that this still does not provide a fully reactive offline UI, since LiveView cannot react to events while disconnected.
- It recommends considering other solutions for critical components that must stay fully reactive offline.
- A link to the app repository, current as of this episode, is provided for readers who want to inspect the code.
- The closing section notes that the episode covered typical production issues in LiveView apps and showed how JS hooks can mitigate them by reacting to LiveView lifecycle events.
