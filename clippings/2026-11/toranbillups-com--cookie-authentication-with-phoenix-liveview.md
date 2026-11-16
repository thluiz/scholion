---
url: "https://toranbillups.com/blog/archive/2020/06/26/cookie-authentication-with-phoenix-liveview"
captured_at: "2026-11-16T03:32:02+00:00"
title: "Cookie Authentication with Phoenix LiveView"
domain: "toranbillups-com"
---

Published June 26, 2020 by [Toran Billups](https://toranbillups.com/)

When I started learning [Elixir](https://elixir-lang.org/) a few years ago I built a [multiplayer game](https://github.com/toranb/elixir-match) for the iPad using [Phoenix](https://www.phoenixframework.org/). The game had a fairly minimal authentication requirement so I looked around at some of the popular open source libraries available but ultimatly I decided to write something myself to get experience with the language and ecosystem.

Earlier this year I started getting more serious about [Phoenix LiveView](https://www.phoenixframework.org/blog/build-a-real-time-twitter-clone-in-15-minutes-with-live-view-and-phoenix-1-5) and quickly discovered login forms present a unique challenge because [Plug.Conn.put\_session](https://github.com/toranb/elixir-match/blob/3cfe1f75cef401ef5c6b7dd72ebb6e99e90629ea/app/lib/match_web/controllers/session_controller.ex#L29-L31) isn't available from any \`handle\_event\` callback. This was an important detail because [my first](https://toranbillups.com/blog/archive/2018/11/18/implementing-basic-authentication/) [plug pipeline](https://github.com/toranb/elixir-match/blob/3cfe1f75cef401ef5c6b7dd72ebb6e99e90629ea/app/lib/match_web/router.ex#L24) used [Plug.Conn.put\_session](https://github.com/toranb/elixir-match/blob/3cfe1f75cef401ef5c6b7dd72ebb6e99e90629ea/app/lib/match_web/controllers/session_controller.ex#L30) to signal that the user had been authenticated.

Like any challenging technical problem I decided to get creative and come up with something that would unlock this for my needs and potentially the needs of others who might be searching for answers like I was recently.

TL;DR If you prefer to skip the story all the relevant code is available on [github](https://github.com/toranb/cookie-authentication-phoenix-liveview-example/commit/863e3c3b7cf4f2a0230c4f036d8a10183adcdc5b)

### Cookies

Before I begin writing about the LiveView solution I need to share some about how Phoenix identifies the user for a given web request. By default the [Endpoint](https://github.com/toranb/cookie-authentication-phoenix-liveview-example/blob/master/lib/shop_web/endpoint.ex) in your Phoenix application includes [Plug.Session](https://hexdocs.pm/plug/Plug.Session.html) configured to use the [cookie session store](https://hexdocs.pm/plug/Plug.Session.COOKIE.html).

    `defmodule ShopWeb.Endpoint do`
    `  use Phoenix.Endpoint, otp_app: :shop`
    
    `  # The session will be stored in the cookie and signed,`
    `  # this means its contents can be read but not tampered with.`
    `  # Set :encryption_salt if you would also like to encrypt it.`
    `  @session_options [`
    `    store: :cookie,`
    `    key: "_shop_key",`
    `    signing_salt: "bWk6pxHd"`
    `  ]`
    
    `  plug Plug.Session, @session_options`
    `end`
  

To see this in action spin up the server with iex and make a request to localhost.

    `iex -S mix phx.server`
    
    `curl http://localhost:4000 --verbose`
  

Using the \`verbose\` flag with curl I saw the response from Phoenix includes a [Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie) header.

> The Set-Cookie HTTP response header is used to send cookies from the server to the user agent, so the user agent can send them back to the server later. -MDN Web Docs

For [better or worse](https://baekdal.com/thoughts/the-original-cookie-specification-from-1997-was-gdpr-compliant/) this cookie is all that's needed to identify the user's session. Now that I understood where this cookie originated from, my attention quickly shifted to decoding the value so I could make sense of it.

    `set-cookie: _shop_key=SFMyNTY.g3QAAAABbQAAAAtfY3NyZl90b2tlbm0AAAAYZFRuNUtQMkJ5YWtKT1JnWUtCeXhmNmdP.l0T3G-i8I5dMwz7lEZnQAeK_WeqEZTxcDeyNY2poz_M; path=/; HttpOnly` 
  

I found a great in depth blog post on [decoding Phoenix session cookies](https://bitcrowd.dev/decoding-phoenix-session-cookies) and the TL;DR looks something like this.

    `set_cookie = "SFMyNTY.g3QAAAABbQAAAAtfY3NyZl90b2tlbm0AAAAYZFRuNUtQMkJ5YWtKT1JnWUtCeXhmNmdP.l0T3G-i8I5dMwz7lEZnQAeK_WeqEZTxcDeyNY2poz_M"`
    `[_, payload, _] = String.split(set_cookie, ".", parts: 3)`
    `{:ok, encoded_term } = Base.url_decode64(payload, padding: false)`
    `:erlang.binary_to_term(encoded_term)`
  

For the initial request I found the value only contained a [CSRF](https://developer.mozilla.org/en-US/docs/Glossary/CSRF) token.

    `%{"_csrf_token" => "GadhekDDOc28OZVc3tOfzQ=="}`
  

After I got my head around all the moving parts I quickly started searching for ways to alter this cookie so that I could identify the session for each incoming request.

### Server Rendered Authentication

Adding data to the cookie is simple with \`Plug.Conn.put\_session\` because the session store is configured for this by default with Phoenix.

    `conn |> put_session(:user_id, id)`
  

With a traditional server rendered app I would verify username/password in the POST controller action for [login](https://github.com/toranb/elixir-match/blob/master/app/lib/match_web/controllers/session_controller.ex#L23-L32). When the username/password was correct I'd insert something to identify the user.

    `case Login.authenticate_user(username, password) do`
    `  nil ->`
    `    conn`
    `    |> put_flash(:error, "incorrect username or password")`
    `    |> render("fail.html")`
    `  id ->`
    `    conn`
    `    |> put_session(:user_id, id)`
    `    |> redirect(to: some_path)`
    `end`
  

> Note: relying on the user id like this should be considered nieve and exists solely for the purpose of illustrating the life cycle of the request for authentication at it's most basic level.

With this user id in the cookie I was then able to write a [plug](https://github.com/toranb/elixir-match/blob/master/app/lib/match_web/authenticator.ex) that would look to see if any user id was present and if so, I would add it to \`conn\` for consistent use throughout the request life cycle.

    `case get_session(conn, :user_id) do`
    `  nil ->`
    `    conn`
    `  id ->`
    `    assign(conn, :current_user_id, id)`
    `end`
  

Next I constructed a [plug](https://github.com/toranb/elixir-match/blob/master/app/lib/match_web/router.ex#L6-L16) that would redirect the user if \`current\_user\_id\` was not found. This redirect plug only runs for restricted parts of the site, unlike the plug above which runs for every request.

    `def redirect_unauthorized(conn, _opts) do`
    `  current_user_id = Map.get(conn.assigns, :current_user_id)`
    `  if current_user_id != nil do`
    `    conn`
    `  else`
    `    conn`
    `    |> redirect(to: login_path(conn, :index))`
    `    |> halt()`
    `end`
  

### The Workaround

The trouble with LiveView in this situation is that event handlers only have access to the web socket and cannot use \`Plug.Conn.put\_session\`. To work around this limitation I use [ETS](https://elixir-lang.org/getting-started/mix-otp/ets.html) to accomplish the same end result.

Like the traditional server rendered example I verify username/password in the [event handler](https://github.com/toranb/cookie-authentication-phoenix-liveview-example/blob/0f7d2b58b6be7208039d8e40d2aa2eed041b7dfa/lib/shop_web/live/login_live.ex#L124-L129). When the username/password is correct I insert the user id into ETS and redirect the user.

    `case Login.authenticate_user(changeset) do`
    `  %Shop.User{id: user_id} ->`
    `    :ets.insert(:shop_auth_table, {:user_id, "#{user_id}"})`
    
    `    redirect = socket |> redirect(to: some_path)`
    `    {:noreply, redirect}`
    
    `  changeset ->`
    `    {:noreply, assign(socket, changeset: changeset)}`
    `end`
  

> Note: as with the server rendered example, relying on the user id like this should be considered nieve and exists solely for the purpose of exploring a workaround.

With the user id in ETS I was then able to write a [plug](https://github.com/toranb/cookie-authentication-phoenix-liveview-example/blob/0f7d2b58b6be7208039d8e40d2aa2eed041b7dfa/lib/shop_web/plugs/session.ex#L18-L26) that would look to see if any user id was present and if so, I would add it to \`conn\` for consistent use throughout the request life cycle just as I did in the server rendered plug.

    `case :ets.lookup(:shop_auth_table, :user_id) do`
    `  [{_, user_id}] ->`
    `    assign(conn, :user_id, user_id)`
    
    `  _ ->`
    `    conn`
    `end`
  

Finally, I constructed another [plug](https://github.com/toranb/cookie-authentication-phoenix-liveview-example/blob/0f7d2b58b6be7208039d8e40d2aa2eed041b7dfa/lib/shop_web/plugs/session.ex#L5-L16) that would redirect the user if \`user\_id\` was not found. This redirect plug only runs for restricted parts of the site, unlike the plug above which runs for every request.

    `def redirect_unauthorized(conn, _opts) do`
    `  user_id = Map.get(conn.assigns, :user_id)`
    
    `  if user_id == nil do`
    `    conn`
    `    |> put_session(:return_to, conn.request_path)`
    `    |> redirect(to: ShopWeb.Router.Helpers.login_path(conn, :index))`
    `    |> halt()`
    `  else`
    `    conn`
    `  end`
    `end`
  

> Note: This solution isn't sound engineering for a few reasons but the most glaring can be seen after a single user id is inserted into ETS. After which any incoming request from any user will appear to be authenticated. While not production ready, this prototype did however validate a potential workaround that could be used to emulate \`Plug.Conn.put\_session\`.

### LiveView Authentication

With this working prototype I now had a renewed sense of urgency to firm it up and share about what I'd learned. To first step was to replace user id with a more privacy friendly value I refer to as \`session\_uuid\` which should be self explanatory.

On the [initial](https://github.com/toranb/cookie-authentication-phoenix-liveview-example/blob/master/lib/shop_web/plugs/session.ex#L19-L27) request a new \`session\_uuid\` is generated and stored in the cookie with \`Plug.Conn.put\_session\`. This unique session id will be used in the LiveView process to associate the user with a specific ETS entry at login. For any request after the first we simply defer to \`ets.lookup\` with the users \`session\_uuid\` but more on that later.

    `case get_session(conn, :session_uuid) do`
    `  nil ->`
    `    conn`
    `    |> put_session(:session_uuid, Ecto.UUID.generate())`
    
    `  session_uuid ->`
    `    conn`
    `    |> validate_session_token(session_uuid)`
    `end`
  

In the LiveView for login I extract the \`session\_uuid\` right away in [mount](https://github.com/toranb/cookie-authentication-phoenix-liveview-example/blob/master/lib/shop_web/live/login_live.ex#L70-L76) and set it with \`assign\` for use in the event handlers as needed.

    `def mount(_params, %{"session_uuid" => key}, socket) do`
    `  changeset = ...`
    
    `  {:ok, assign(socket, key: key, changeset: changeset)}`
    `end`
  

In the [event handler](https://github.com/toranb/cookie-authentication-phoenix-liveview-example/blob/master/lib/shop_web/live/login_live.ex#L121-L144) I pattern match out the \`session\_uuid\`, [sign it](https://github.com/phoenixframework/phoenix/blob/e0e930cf7373f2b445c009f80a432d7de7de948c/lib/phoenix/token.ex#L110) to generate a token and finally I put that token into ETS. After all, this was the secret sauce of that original workaround but this time the user is more securely linked with help from the unique \`session\_uuid\` value found in their cookie.

    `def handle_info({:disable_form, changeset}, %{assigns: %{:key => key}} = socket) do`
    `  case Login.authenticate_user(changeset) do`
    `    %Shop.User{id: user_id} ->`
    `      salt = ShopWeb.Endpoint.config(:live_view)[:signing_salt]`
    `      token = Phoenix.Token.sign(ShopWeb.Endpoint, salt, user_id)`
    `      :ets.insert(:shop_auth_table, {:"#{key}", token})`
    
    `      redirect = socket |> redirect(to: some_path)`
    `      {:noreply, redirect}`
    
    `    changeset ->`
    `      {:noreply, assign(socket, changeset: changeset)}`
    `  end`
    `end`
  

Looking back at the [plug code](https://github.com/toranb/cookie-authentication-phoenix-liveview-example/blob/master/lib/shop_web/plugs/session.ex#L30-L44) from earlier, when a user's \`session\_uuid\` does yield a token I then verify it. When this token checks out I take the \`user\_id\` and add it to \`conn\` for consistent use throughout the request life cycle just as I did in the server rendered plug.

> Note: Below I use [Phoenix.Token.verify](https://github.com/phoenixframework/phoenix/blob/e0e930cf7373f2b445c009f80a432d7de7de948c/lib/phoenix/token.ex#L188) to extract the token and pull user id from it. In truth I started with this because I assumed it was somehow "more secure" but later that evolved into a practical mechanism to expire the session.

    `def validate_session_token(conn, session_uuid) do`
    `  case :ets.lookup(:shop_auth_table, :"#{session_uuid}") do`
    `    [{_, token}] ->`
    `      case Phoenix.Token.verify(ShopWeb.Endpoint, signing_salt(), token, max_age: 806_400) do`
    `        {:ok, user_id} ->`
    `          conn`
    `          |> assign(:user_id, user_id)`
    
    `        _ ->`
    `          conn`
    
    `      end`
    `  ->`
    `    conn`
    `  end`
    `end`
  

Finally, I use the same \`redirect\_unauthorized\` [plug](https://github.com/toranb/cookie-authentication-phoenix-liveview-example/blob/master/lib/shop_web/plugs/session.ex#L5-L16) to redirect the user if \`user\_id\` isn't available in \`conn.assigns\`.

    `def redirect_unauthorized(conn, _opts) do`
    `  user_id = Map.get(conn.assigns, :user_id)`
    
    `  if user_id == nil do`
    `    conn`
    `    |> put_session(:return_to, conn.request_path)`
    `    |> redirect(to: ShopWeb.Router.Helpers.login_path(conn, :index))`
    `    |> halt()`
    `  else`
    `    conn`
    `  end`
    `end`
  

### What about mount?

After I got login working, I flipped over to the restricted LiveView assuming I could get \`user\_id\` without any trouble. Unfortunately I found you don't have access to \`conn.assigns\` from [mount](https://github.com/toranb/cookie-authentication-phoenix-liveview-example/blob/master/lib/shop_web/live/shop_live.ex#L14-L24) as I would have expected. To work around this constraint I used the \`session\_uuid\` to get the token like I did in the [plug](https://github.com/toranb/cookie-authentication-phoenix-liveview-example/blob/master/lib/shop_web/plugs/session.ex#L31-L36).

    `def mount(_params, session, socket) do`
    `  socket = assign_new(socket, :current_user, fn ->`
    `    user_id = get_user_id(session)`
    
    `    Shop.User`
    `    |> Shop.Repo.get(user_id)`
    `  end)`
    
    `  {:ok, socket}`
    `end`
  

The [get\_user\_id](https://github.com/toranb/cookie-authentication-phoenix-liveview-example/blob/master/lib/shop_web/live/shop_live.ex#L26-L40) function does exactly what the plug did to extract the token, then from it the \`user\_id\` like you might expect.

    `def get_user_id(%{"session_uuid" => session_uuid}) do`
    `  case :ets.lookup(:shop_auth_table, :"#{session_uuid}") do`
    `    [{_, token}] ->`
    `      case Phoenix.Token.verify(ShopWeb.Endpoint, signing_salt(), token, max_age: 806_400) do`
    `        {:ok, user_id} ->`
    `          user_id`
    
    `        _ ->`
    `          nil`
    `      end`
    
    `    _ ->`
    `      nil`
    `  end`
    `end`
  

### Bonus!

If you don't like the idea of running \`:ets.lookup\` along with \`Phoenix.Token.verify\` each time the mount function executes and you are cool with exposing \`user\_id\` as part of the cookie you could instead alter the [plug](https://github.com/toranb/cookie-authentication-phoenix-liveview-example/commit/90ff976085f1dc7197ca15f436169fcda5ade7bf) that previously only set \`conn.assigns\` to also include a call to \`put\_session\` with the \`user\_id\`.

    `def validate_session_token(conn, session_uuid) do`
    `  case :ets.lookup(:shop_auth_table, :"#{session_uuid}") do`
    `    [{_, token}] ->`
    `      case Phoenix.Token.verify(ShopWeb.Endpoint, signing_salt(), token, max_age: 806_400) do`
    `        {:ok, user_id} ->`
    `          conn`
    `          |> assign(:user_id, user_id)`
    `          |> put_session("user_id", user_id)`
    
    `        _ ->`
    `          conn`
    
    `      end`
    `  ->`
    `    conn`
    `  end`
    `end`
  

Now in the restricted LiveView I can get \`user\_id\` in the [mount](https://github.com/toranb/cookie-authentication-phoenix-liveview-example/commit/90ff976085f1dc7197ca15f436169fcda5ade7bf) function with ease.

    `def mount(_params, %{"user_id" => user_id}, socket) do`
    `  socket = assign_new(socket, :current_user, fn ->`
    `    Shop.User`
    `    |> Shop.Repo.get(user_id)`
    `  end)`
    
    `  {:ok, socket}`
    `end`
  

You can find the source code from my adventure on [github](https://github.com/toranb/cookie-authentication-phoenix-liveview-example/commits/master).

* * *
