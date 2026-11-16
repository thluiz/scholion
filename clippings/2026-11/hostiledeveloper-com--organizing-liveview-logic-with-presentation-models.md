---
url: "https://hostiledeveloper.com/2020/06/19/organizing-liveview-logic-with-presentation-models.html"
captured_at: "2026-11-16T03:01:56+00:00"
title: "Organizing LiveView Logic with Presentation Models"
domain: "hostiledeveloper-com"
---

I’ve been really enjoying Phoenix LiveView! Working on smart interfaces is super easy and just works. It’s really incredible.

I’ve been going through the [PragmaticStudio LiveView course](https://pragmaticstudio.com/phoenix-liveview) and have been LOVING IT. If you just hearing about it, SIGN UP NOW (well maybe after reading this post…). You’ll thank me. It’s really well done and is the best way to get your head around the awesomeness of LiveView.

They build a series of UI patterns in LiveView to show you how simple it is to add seemingly complex interactions into a Phoenix app. In one module, the implement search. Having been a teacher in a previous life I know that sometimes you have to keep things simple at the cost of implementing better patterns. One such example is [this LiveView](https://github.com/pragmaticstudio/live_view_studio/blob/0420ed745e71f931d17d70e32f5be1b72cfa1495/lib/live_view_studio_web/live/search_live.ex).

There’s nothing _wrong_ with their code. It works! But I think it suffers from tutorial-itis, where it’s enough to prove a point, but not what you would actually ship.

## Thinking in Layers

LiveViews suffer from the same neck snapping, eye darting issues as GenServers. With a GenServer you define a client API, then a server API. Check the client API for the arguments passed in. Did we pattern match on the client side? Look for `handle_*` to see what it does, and how it handles errors. Also, testing complex logic in GenServers is less than great. But that’s fine! We have a way to deal with this by decoupling our [Boundary Layer](https://pragprog.com/titles/jgotp/) from our core business logic, breaking them into nice, pure functions we can easily test.

LiveViews are a bit different though. The data we want to isolate isn’t really part of our _core_ business logic. In fact, in most cases, it exists to deliver a single experience in your app.

Let’s take a look at the code example. It stores a few pieces of state that get manipulated over the course of the page’s life.

defmodule LiveViewStudioWeb.SearchLive do

use LiveViewStudioWeb, :live\_view

alias LiveViewStudio.Stores

def mount(\_params, \_session, socket) do

socket \=

assign(socket,

zip: "",

stores: \[\],

loading: false

)

{:ok, socket}

end

\# the rest

end

In the example, the `LiveViewStudio.Stores` module runs our search and is very much part of our _core_ business logic. This might be some code that gets optimized and used in several places in our app in a number of contexts. The results from our search will be stored in `stores`. Our LiveView can potentially act on the data it got back from the data store, further decorating it in preparation to render it. Along with `zip` and `loading`, this specific interpretation of `stores` would never be used outside of this view. Why does this matter?

## Separation of concerns and testing

The more complex our transformations get, the more state we have to hold at different points of this page’s life in response to user actions or other process’ messages, the more we’d benefit from separating out a functional core.

Now I know that LiveView has [great ways](https://hexdocs.pm/phoenix_live_view/Phoenix.LiveViewTest.html) of mimicking clicks, and changes from your front-end, as well as a way to send messages to that process to simulate internal messages, but we still want to keep our Boundary Layer small, and extract our logic into small testable modules.

A quick note before we move on… I know this is going to be a LOT of code for solving a relatively small problem. I think this pattern will come in handy when you’re dealing with apps that take advantage of `live_action` and have a single LiveView render several subcomponents. For now… Go with me.

## Extracting the Module

[Presentation Model](https://martinfowler.com/eaaDev/PresentationModel.html)

> Represent the state and behavior of the presentation independently of the GUI controls used in the interface - Martin Fowler

We’re going to extract the state for this component, and encapsulate the logic a bit. We showed the state, but what’s this thing do? Users are presented a search box, where, the request takes 2 seconds to complete. Between submission and bringing up results, a `loading` icon appears.

The flow looks something like: 1. Send query to LiveView 2. LiveView sets a loading state, sends self message to actually RUN the query, and returns the new `loading` state. 3. Query finishes asynchronously, updates state with results, clears the loading state and returns that to the view.

Let’s start out with some tests:

defmodule LiveViewStudioWeb.SearchLive.PresentationModelTest do

use ExUnit.Case

alias LiveViewStudioWeb.SearchLive.PresentationModel

describe "new/1" do

test "success: returns empty state" do

assert {:ok, %PresentationModel{zip: "", stores: \[\], loading: false, search\_function: \_fun}} \=

PresentationModel.new(search\_function: fn \_zip \-> \[\] end)

end

test "failure: requires search function to take 1 argument" do

assert {:error, "Query function must take one argument"} \=

PresentationModel.new(search\_function: fn \-> :womp end)

end

end

describe "prepare\_query/2" do

setup :add\_zip

setup :model\_with\_no\_op\_function

test "success: updates loading state", %{pm: pm, zip: zip} do

%PresentationModel{loading: true} \= PresentationModel.prepare\_query(pm, zip)

end

test "success: updates zip query", %{pm: pm, zip: zip} do

assert %PresentationModel{zip: ^zip} \= PresentationModel.prepare\_query(pm, zip)

end

end

describe "execute\_query/1" do

setup :add\_zip

setup :add\_results

setup :model\_that\_expects\_zip\_and\_returns\_results

setup %{pm: pm, zip: zip} do

pm \=

pm

|> PresentationModel.prepare\_query(zip)

|> PresentationModel.execute\_query()

%{pm: pm}

end

test "success: returns search results", %{pm: pm, results: results} do

assert %PresentationModel{stores: ^results} \= pm

end

test "success: clears loading state", %{pm: pm} do

assert %PresentationModel{loading: false} \= pm

end

test "failure: populates info message when results are empty" do

{:ok, pm} \= PresentationModel.new(search\_function: fn \_ \-> \[\] end)

assert %{info: "No stores matching \\"bogus\\""} \=

pm

|> PresentationModel.prepare\_query("bogus")

|> PresentationModel.execute\_query()

end

end

defp model\_with\_no\_op\_function(context) do

{:ok, pm} \= PresentationModel.new(search\_function: fn \_ \-> \[\] end)

context

|> Map.put(:pm, pm)

end

defp model\_that\_expects\_zip\_and\_returns\_results(context) do

zip \= context.zip

results \= context.results

{:ok, pm} \= PresentationModel.new(search\_function: fn ^zip \-> results end)

context

|> Map.put(:pm, pm)

end

defp add\_zip(context) do

context

|> Map.put(:zip, "90210")

end

defp add\_results(context) do

context

|> Map.put(:results, \["result 1", "result 2"\])

end

end

Our module expects to receive a function that takes one argument. Note we’ve broken up the flow between preparing the query (storing it) and actually executing it. OK, on to the code.

defmodule LiveViewStudioWeb.SearchLive.PresentationModel do

defstruct zip: "", stores: \[\], loading: false, search\_function: nil, info: nil

def new(search\_function: search\_function) when is\_function(search\_function, 1) do

{:ok, %\_\_MODULE\_\_{search\_function: search\_function}}

end

def new(\_), do: {:error, "Query function must take one argument"}

def prepare\_query(%\_\_MODULE\_\_{} \= struct, zip) do

struct

|> store\_zip(zip)

|> set\_loading\_state

end

def execute\_query(%\_\_MODULE\_\_{} \= struct) do

struct

|> run\_query

|> clear\_loading\_state

end

defp run\_query(%\_\_MODULE\_\_{search\_function: search\_function, zip: zip} \= struct) do

stores \= search\_function.(zip)

info \=

case stores do

\[\] \-> "No stores matching \\"#{zip}\\""

\_ \-> nil

end

struct

|> Map.put(:stores, stores)

|> Map.put(:info, info)

end

defp store\_zip(%\_\_MODULE\_\_{} \= struct, zip) do

struct

|> Map.put(:zip, zip)

end

defp set\_loading\_state(%\_\_MODULE\_\_{} \= struct) do

struct

|> Map.put(:loading, true)

end

defp clear\_loading\_state(%\_\_MODULE\_\_{} \= struct) do

struct

|> Map.put(:loading, false)

end

end

OK, so this is a lot of code, compared to what the final result I linked to earlier but let’s think about what we’ve won. There are clearly 3 things this module can do. Each of those things has a clear pipeline describing what it means to execute it. And best of all, it’s all pure! We don’t have to simulate clicks, or mess with input fields. We can test plain old values. Adding a new feature to this and verifying it works with automated tests is trivial. Imagine how you would add the ability to ensure a zip code is only numbers? Or that they’re 5 characters long?

## Updating the LiveView

We’re going to take a look at what the `SearchLive` LiveView would look like using this Presentation Model.

defmodule LiveViewStudioWeb.SearchLive do

use LiveViewStudioWeb, :live\_view

alias LiveViewStudio.Stores

alias LiveViewStudioWeb.SearchLive.PresentationModel

def mount(\_params, \_session, socket) do

socket \=

socket

|> initialize\_presentation\_model

{:ok, socket}

end

def render(assigns) do

~L"""

<h1>Find a Store</h1>

<div id="search">

<form phx-submit="zip-search">

<input type="text" name="zip" value="<%= @presentation\_model.zip %>"

placeholder="Zip Code"

autofocus autocomplete="off"

<%= if @presentation\_model.loading, do: "readonly" %> />

<button type="submit">

<img src="images/search.svg">

</button>

</form>

<%= if @presentation\_model.loading do %>

<div class="loader">

Loading...

</div>

<% end %>

<div class="stores">

<ul>

<%= for store <- @presentation\_model.stores do %>

<li>

<div class="first-line">

<div class="name">

<%= store.name %>

</div>

<div class="status">

<%= if store.open do %>

<span class="open">Open</span>

<% else %>

<span class="closed">Closed</span>

<% end %>

</div>

</div>

<div class="second-line">

<div class="street">

<img src="images/location.svg">

<%= store.street %>

</div>

<div class="phone\_number">

<img src="images/phone.svg">

<%= store.phone\_number %>

</div>

</div>

</li>

<% end %>

</ul>

</div>

</div>

"""

end

def handle\_event("zip-search", %{"zip" \=> zip}, socket) do

send(self(), :run\_zip\_search)

socket \=

socket

|> prepare\_query(zip)

{:noreply, socket}

end

def handle\_info(:run\_zip\_search, socket) do

socket \=

socket

|> execute\_query

|> maybe\_put\_flash

{:noreply, socket}

end

defp initialize\_presentation\_model(socket) do

{:ok, presentation\_model} \= PresentationModel.new(search\_function: &Stores.search\_by\_zip/1)

socket

|> assign(presentation\_model: presentation\_model)

end

defp prepare\_query(socket, zip) do

socket

|> update(:presentation\_model, &PresentationModel.prepare\_query(&1, zip))

end

defp execute\_query(socket) do

socket

|> update(:presentation\_model, &PresentationModel.execute\_query(&1))

end

defp maybe\_put\_flash(socket) do

%{info: info} \= socket.assigns.presentation\_model

if info do

socket |> put\_flash(:info, info)

else

socket

end

end

end

SO NICE! Our live view is solely responsible for making sure the right parts of our Presentation Model module get called and use it to render state. Notice how we’re using `@presentation_model.x`. If you’re wondering, there’s no hit to performance using this! LiveView does a diff on the server before sending the change over the wire. If there’s no change, it doesn’t send anything. And what’s best is that to test the LiveView, you only have to test a couple of cases for success and failure, as opposed to every detail and edge case of the view logic. This is kind of great.

## Wrap up

LiveView is awesome, and with the right patterns we can ensure our fancy UIs have equally fancy tests. You can build really complex logic that you will KNOW works. Thanks for reading. Happy Clacking.
