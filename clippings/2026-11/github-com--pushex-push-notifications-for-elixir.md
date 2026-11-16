---
url: "https://github.com/danhper/pushex"
captured_at: "2026-11-16T03:21:22+00:00"
title: "GitHub - danhper/pushex: Push notifications for Elixir"
domain: "github-com"
---

[![Build Status](https://camo.githubusercontent.com/9db5c68f1e07df40267200b6673f41c2d517378758836cf89fc6dd539e5512b3/68747470733a2f2f7472617669732d63692e6f72672f64616e687065722f7075736865782e7376673f6272616e63683d6d6173746572)](https://travis-ci.org/danhper/pushex) [![Coverage Status](https://camo.githubusercontent.com/eaa19ae4aa29ab8d2f6faccf40822ef14076c0b0049f0da16a835e9a7bb92b4a/68747470733a2f2f636f766572616c6c732e696f2f7265706f732f6769746875622f64616e687065722f7075736865782f62616467652e7376673f6272616e63683d6d6173746572)](https://coveralls.io/github/danhper/pushex?branch=master)

Pushex is a library to easily send push notifications with Elixir.

## About

[](#about)

### Goals

[](#goals)

The main goals are the following:

*   Easy to use async API
*   Common API for iOS and Android
*   Multiple applications handling
*   Proper error and response handling
*   Testable using a sanbox mode

### Status

[](#status)

Both GCM and APNS are working. APNS delegates to [apns4ex](https://github.com/chvanikoff/apns4ex) for now, I will probably use the HTTP2 API in a later version.

The API is still subject to change, with a minor version bump for each change.

## Installation

[](#installation)

Add the following to your dependencies mix.ex.

\[{:pushex, "~> 0.2"}\]

Then, add `:pushex` to your applications.

## Usage

[](#usage)

The most basic usage, with no configuration looks like this:

app \= %Pushex.GCM.App{name: "a\_unique\_name\_you\_like", auth\_key: "a GCM API auth key"}
Pushex.push(%{title: "my\_title", body: "my\_body"}, to: "registration\_id", with\_app: app)

To avoid having to create or retreive your app each time, you can configure as many apps as you want in your `config.exs`:

config :pushex,
  gcm: \[
    default\_app: "first\_app",
    apps: \[
      \[name: "first\_app", auth\_key: "a key"\],
      \[name: "other\_app", auth\_key: "another key"\]
    \]
  \],
  apns: \[
    default\_app: "first\_app",
    apps: \[
      \[name: "first\_app", env: :dev, certfile: "/path/to/certfile", pool\_size: 5\]
    \]
  \]

You can then do the following:

\# this will use the default app, "first\_app" with the above configuration
Pushex.push(%{title: "my\_title", body: "my\_body"}, to: "registration\_id", using: :gcm)

\# this will use the other\_app
Pushex.push(%{title: "my\_title", body: "my\_body"}, to: "registration\_id", using: :gcm, with\_app: "other\_app")

Note that the function is async and only returns a reference, see the response and error handling documentation for more information.

### Sending to multiple platforms

[](#sending-to-multiple-platforms)

If you want to use the same message for both platforms, you can define messages as follow:

message \= %{
  common: "this will be in both payloads",
  other: "this will also be in both payloads",
  apns: %{
    alert: "My alert",
    badge: 1
  },
  gcm: %{
    title: "GCM title",
    body: "My body"
  }
}

Pushex.push(message, to: \["apns\_token1", "apns\_token2"\], using: :apns)
Pushex.push(message, to: \["gcm\_registration\_id1", "gcm\_registration\_id2"\], using: :gcm)

Only `:gcm` and `:apns` are currently available.

### Passing more options

[](#passing-more-options)

If you need to pass options, `priority` for example, you can just pass it in the keyword list and it will be sent.

See

[https://developers.google.com/cloud-messaging/http-server-ref#downstream-http-messages-json](https://developers.google.com/cloud-messaging/http-server-ref#downstream-http-messages-json)

for more information.

The parameters from `Table 1` should be passed in the keyword list, while the parameters from `Table 2` should be passed in the first argument.

For more information about `APNS` options, see [apns4ex](https://github.com/chvanikoff/apns4ex) docs.

NOTE: if you pass an array to the `to` parameter, if will automatically be converted to `registration_ids` when sending the request, to keep a consistent API.

### Loading app from somewhere else

[](#loading-app-from-somewhere-else)

If you are saving your auth\_keys in your database, you can override the default way to retreive the apps:

\# config.exs
config :pushex,
  app\_manager\_impl: MyAppManager

\# my\_app\_manager.ex
defmodule MyAppManager do
  @behaviour Pushex.AppManager

  def find\_app(platform, name) do
    if app \= Repo.get\_by(App, platform: platform, name: name) do
      make\_app(platform, app)
    end
  end

  \# transform to a \`Pushex.\_.App\`
  defp make\_app(:gcm, app) do
    struct(Pushex.GCM.App, Map.from\_struct(app))
  end
  defp make\_app(:apns, app) do
    struct(Pushex.APNS.App, Map.from\_struct(app))
  end
end

### Handling responses

[](#handling-responses)

To handle responses, you can define a module using `Pushex.EventHandler` which uses `:gen_event` to process events.

\# config.exs
config :pushex,
  event\_handlers: \[MyEventHandler\]

\# my\_event\_handler.ex
defmodule MyEventHandler do
  use Pushex.EventHandler

  def handle\_event({:request, request, {pid, ref}}, state) do
    \# do whatever you want with the request
    \# for example, logging or saving in a DB
    {:ok, state}
  end

  def handle\_event({:response, response, request, {pid, ref}}, state) do
    \# do whatever you want with the response and request
    {:ok, state}
  end
end

The `ref` passed here is the one returned when calling `push`.

## Testing

[](#testing)

Pushex offers a sandbox mode to make testing easier.

To enable it, you should add the following to your configuration:

```
config :pushex,
  sandbox: true
```

Once you are using the sandbox, the messages will not be sent to GCM or APNS anymore, but stored in `Pushex.Sandbox`. Furthermore, all the messages will be returned to the process that sent them. Here is a sample test.

test "send notification to users" do
  ref \= Pushex.push(%{body: "my message"}, to: "my-user", using: :gcm)
  pid \= self()
  assert\_receive {{:ok, response}, request, ^ref}
  assert \[{{:ok, ^response}, ^request, {^pid, ^ref}}\] \= Pushex.Sandbox.list\_notifications
end

Note that `list_notifications` depends on the running process, so if you call it from another process, you need to explicitly pass the pid with the `:pid` option.

Also note that `Pushex.push` is asynchronous, so if you remove the `assert_receive`, you will have a race condition. To avoid this, you can use `Pushex.Sandbox.wait_notifications/1` instead of `Pushex.Sandbox.list_notifications`. It will wait (by default for `100ms`) until at least `:count` notifications arrive

test "send notification to users and wait" do
  Enum.each (1..10), fn \_ \->
    Pushex.push(%{body: "foo"}, to: "whoever", using: :gcm)
  end
  notifications \= Pushex.Sandbox.wait\_notifications(count: 10, timeout: 50)
  assert length(notifications) \== 10
end

However, the requests are asynchronous, so there is no guaranty that the notifications in the sandbox will in the same order they have been sent.
