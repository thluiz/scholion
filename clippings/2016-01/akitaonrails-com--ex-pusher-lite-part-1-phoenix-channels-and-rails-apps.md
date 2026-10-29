---
url: "http://www.akitaonrails.com/2015/12/09/ex-pusher-lite-part-1-phoenix-channels-and-rails-apps"
captured_at: "2016-01-08T08:39:45-03:00"
title: "Ex Pusher Lite - Part 1: Phoenix Channels and Rails apps | AkitaOnRails.com"
domain: "akitaonrails-com"
---

# Ex Pusher Lite - Part 1: Phoenix Channels and Rails apps

2015 December 09, 18:39 h - tags: [elixir](http://www.akitaonrails.com/elixir) [expusherlite](http://www.akitaonrails.com/expusherlite) [english](http://www.akitaonrails.com/english) [pusher](http://www.akitaonrails.com/pusher) [phoenix](http://www.akitaonrails.com/phoenix)

Finally, after a lengthy exercising period (and plenty of blogging!) I will start implementing the Elixir app I wanted from the very beginning.

As a Rails developer there are a few things we can't do in Rails. One of them is to deal with real-time messaging.

Rails 5 will bring [Action Cable](https://github.com/rails/actioncable), and it might be good enough for most cases. It uses [Faye](https://github.com/faye/faye), which in turn is based on Eventmachine. You can implement a good enough solution for Websockets using Faye in your Rails 4.2 app right now.

Another option is to avoid the trouble altogether and use a messaging service. One option I always recommend for zero friction is to use [Pusher.com](https://pusher.com/).

![big_Screenshot_from_2015-12-09_18_41_22.png](akitaonrails-com--ex-pusher-lite-part-1-phoenix-channels-and-rails-apps/aeeaa8537de633ec578ecd6b9a8a14ca.png)

### The Basics

You will want to clone from my [example repository](https://github.com/akitaonrails/pusher_lite_demo/tree/v0.1), like this:

|  |  |
| --- | --- |
| ``` 1234 ``` | ``` git clone https://github.com/akitaonrails/pusher_lite_democd pusher_lite_demogit checkout tags/v0.1 -b v0.1bundle ``` |

This is a very very simple implementation of a real-time, websocket-based, chat using Pusher. The idea goes like this:

We start by having a front-end Form to send messages

|  |  |
| --- | --- |
| ``` 123456789 ``` | ``` <!-- app/views/home/index.html.erb --><%= form_for @event, url: events_path, remote: true, html: {class: "pure-form pure-form-stacked"} do |f| %>  <fieldset>    <legend>Send your message remotely</legend>    <%= f.text_field :name, placeholder: "Name" %>    <%= f.text_field :message, placeholder: "Message" %>    <%= f.submit "Send message", class: "pure-button pure-button-primary" %>  </fieldset><% end %> ``` |

It's using Rails built-in jQuery support for Ajax posting the form to the "EventsController#create" method:

|  |  |
| --- | --- |
| ``` 12345678910 ``` | ``` # app/controllers/events_controller.rbclass EventsController < ApplicationController   create    SendEventsJob.perform_later(event_params)     event_params    params.require(:pusher_event).permit(:name, :message) ``` |

Just to annotate the process, the "routes.rb" looks like this:

|  |  |
| --- | --- |
| ``` 123456 ``` | ``` # config/routes.rbRails.application.routes.draw   resources :events, : [:create]  root home#index ``` |

The HTML layout looks like this:

|  |  |
| --- | --- |
| ``` 12345678910111213141516171819202122232425262728293031 ``` | ``` <!-- app/views/layout/application.html.erb --><!DOCTYPE html><html><head>  <title>Pusher  <title>  <meta name="viewport" content="width=device-width, initial-scale=1">  <meta name="pusher_key" content="<%= Rails.application.secrets.pusher_key %>">  <meta name="pusher_channel" content="<%= Rails.application.secrets.pusher_channel %>">  <%= stylesheet_link_tag    'application', media: 'all', 'data-turbolinks-track' => true %>  <%= javascript_include_tag 'application', 'data-turbolinks-track' => true %>  <script src="/js.pusher.com//pusher.min.js></script>  <%= csrf_meta_tags %></head><body><div class=pure-menu pure-menu-horizontal>    <span class=pure-menu-heading>Pusher Client Demo</span>...</div><div class=pure-g-r>  <div class=pure-u-- message-form>    <%= yield %>  </div>    <div class=pure-u-- message-receiver>  </div></div></body></html> ``` |

This layout imports the default "application.js" which configures Pusher, establishes the Websocket connection and subscribes to messages on a specific topic with specific events:

|  |  |
| --- | --- |
| ``` 123456789101112131415161718 ``` | ``` // app/assets/javascript/application.js//= require jquery//= require jquery_ujs//= require turbolinks//= require_tree .(document).on(page:change, function(){   pusherKey = (meta[name=pusher_key]).attr(content);   pusher =  Pusher(pusherKey, { encrypted:  });   pusherChannel = (meta[name=pusher_channel]).attr(content);   channel = pusher.subscribe(pusherChannel);    channel.bind(new_message, function(data) {     new_line = <p><strong> + data.name + <strong>:  + data.message + </p>;    (.message-receiver).append(new_line);  });}); ``` |

It gets the configuration metadata from the layout meta tags which grabs the values from "config/secrets.yml":

|  |  |
| --- | --- |
| ``` 12345678910111213141516171819 ``` | ``` development:  secret_key_base: ded7c4a2a298c1b620e462b50c9ca6ccb60130e27968357e76cab73de9858f14556a26df885c8aa5004d0a7ca79c0438e618557275bdb28ba67a0ffb0c268056  pusher_url: <%= ENV['PUSHER_URL'] %>  pusher_key: <%= ENV['PUSHER_KEY'] %>  pusher_channel: test_chat_channel:  secret_key_base: f51ff494801ff0f9e1711036ef6f2f6f1e13544b02326adc5629c6833ae90f1a476747fae94b792eba8a444305df8e7a5ad53f05ea4234692ac96cc44f372029  pusher_url: <%= ENV['PUSHER_URL'] %>  pusher_key: <%= ENV['PUSHER_KEY'] %>  pusher_channel: test_chat_channel# Do not keep production secrets in the repository,# instead read values from the environment.production:  secret_key_base: <%= ENV["SECRET_KEY_BASE"] %>  pusher_url: <%= ENV['PUSHER_URL'] %>  pusher_key: <%= ENV['PUSHER_KEY'] %>  pusher_channel: <%= ENV['PUSHER_CHANNEL'] %> ``` |

And as I'm using dotenv-rails, the ".env" looks like this:

|  |  |
| --- | --- |
| ``` 123 ``` | ``` PUSHER_URL: "https://14e86e5fee3335fa88b0:2b94ff0f07ce9769567f@api.pusherapp.com/apps/159621"PUSHER_KEY: "14e86e5fee3335fa88b0"PUSHER_CHANNEL: "test_chat_channel" ``` |

Pusher is configured in the server-side through this initializer:

|  |  |
| --- | --- |
| ``` 12345 ``` | ``` # config/initializers/pusher.rbrequire pusherPusher.url = Rails.application.secrets.pusher_urlPusher.logger = Rails.logger ``` |

Finally, the "EventsController#create" actually do an async call to a [SuckerPunch](https://github.com/brandonhilkert/sucker_punch) job:

|  |  |
| --- | --- |
| ``` 12345678 ``` | ``` class SendEventsJob < ActiveJob::  queue_as :default   perform(event_params)    @event = PusherEvent.new(event_params)    @event.save ``` |

By the way, as a segway, [SuckerPunch](https://github.com/brandonhilkert/sucker_punch) is a terrific solution for in-process asynchronous tasks. It's a better option to start with it without having to implement a separated system with Sidekiq workers.

Once you have larger job queues or jobs that are taking too long, then go to Sidekiq. If you use ActiveJob, the transition is as simple as changing the following configuration line in the "config/application.rb" file:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` config.active_job.queue_adapter = :sucker_punch ``` |

This job just calls the "save" method in the fake-model "PusherEvent":

|  |  |
| --- | --- |
| ``` 12345678910111213 ``` | ``` class PusherEvent  include ActiveModel::Model  attr_accessor :name, :message  validates :name, :message, presence:        Pusher.trigger(Rails.application.secrets.pusher_channel, new_message, {      : name,      message: message    }) ``` |

As it's a very simple, the Gemfile is equally simple:

|  |  |
| --- | --- |
| ``` 1234 ``` | ``` gem pushergem dotenv-railsgem purecss-railsgem sucker_punch ``` |

So what it does is very simple:

1. The application loads Pusher and the necessary configuration.
2. When the user goes to "http://localhost:3000" he is presented with the message Form.
3. When the user posts the message, it ends in "EventsController#create", which calls SuckerPunch's "SendEventsJob", instantiates a new "PusherEvent" model with the received form params and finally triggers the message to the Pusher server.
4. The same form page also loads the Pusher javascript client and connects to the "test\_chat\_channel" topic and listens to the "new\_message" event, which is the same thing the "Pusher.trigger" call sends together with the form message params.
5. The Pusher server broadcasts the received trigger message to all subscribed Websocket clients.
6. The Pusher javascript client in the user's browser receives the new message and just formats the message and appends to the "message-receiver" div HTML block in the same page.

Pusher has support for authenticated users, private channels and more, but this is 80% of the usage for most cases. You can implement this as a chat system, a notification system, or anything like that.

Your Rails app sets up the front-end HTML/Javascript to connect to Pusher, listening to certain topics and events and the same Rails app triggers Pusher in the server-side, posting new messages. Pusher receives messages and broadcasts to the clients that subscribes to its topics. That's it.

## Ex Pusher Lite - Part 1: Initial Phoenix-based Pusher replacement

My original idea was to make a drop-in replacement for the Pusher server, using the same Pusher client, but for now it was not easy to do so.

Instead, this Part 1 will focus on implementing an initial server ExPusherLite server that also receives events triggered by the same Rails server-side controller process and broadcasting to the same Rails front-end component through WebSockets.

I followed [Daniel Neighman](https://labs.opendoor.com/phoenix-on-rails-for-client-push-notifications) tutorial. I had to do a few adjustments to have it working (and as this is still Part 1, it's not a complete solution yet!)

You can close the initial version from [my other Github repository](https://github.com/akitaonrails/ex_pusher_lite) like this:

|  |  |
| --- | --- |
| ``` 123 ``` | ``` git clone https://github.com/akitaonrails/ex_pusher_litecd ex_pusher_litemix deps.get ``` |

The tutorial implemented initial setup for [Guardian](https://github.com/hassox/guardian) and [Joken](https://github.com/bryanjos/joken) for JSON Web Tokens. I am still getting used to how [channels](http://www.phoenixframework.org/docs/channels) are implemented in Phoenix.

It already comes pre-configured with a single socket handler that multiplexes connections. You start through the EndPoint OTP application:

|  |  |
| --- | --- |
| ``` 123456 ``` | ``` # lib/ex_pusher_lite/endpoint.exdefmodule ExPusherLite.Endpoint   use Phoenix.Endpoint, otp_app: :ex_pusher_lite  socket /socket, ExPusherLite.UserSocket  ... ``` |

This application is started by the main supervisor in "lib/ex\_pusher\_lite.ex". It points the endpoint "/socket" to the socket handler "UserSocket":

|  |  |
| --- | --- |
| ``` 1234567891011 ``` | ``` # web/channels/user_socket.exdefmodule ExPusherLite.UserSocket   use Phoenix.Socket  ## Channels  channel , ExPusherLite.RoomChannel  ## Transports  transport :websocket, Phoenix.Transports.WebSocket  # transport :longpoll, Phoenix.Transports.LongPoll  ... ``` |

The "channel" function comes commented out, so I started by uncommenting it. You can pattern match the topic name like "public:\*" to different Channel handlers. For this simple initial test I am sending everything to the "RoomChannel", which I had to create:

|  |  |
| --- | --- |
| ``` 1234567891011121314151617181920212223242526272829303132333435363738394041424344454647 ``` | ``` defmodule ExPusherLite.RoomChannel   use Phoenix.Channel  use Guardian.Channel  # no auth is needed for public topics   (public: <> _topic_id, _auth_msg, socket)     {, socket}     (topic,  claims: claims, resource: _resource , socket)      permitted_topic?(claims[:listen], topic)       { ,  message: "Joined" , socket }          { :error, :authentication_required }         (_room, _payload, _socket)     { :error, :authentication_required }     handle_in(, payload, socket =  topic: "public:" <> _ )     broadcast socket, , payload    { :noreply, socket }     handle_in(, payload, socket)     claims = Guardian.Channel.claims(socket)     permitted_topic?(claims[:publish], socket.topic)       broadcast socket, , payload      { :noreply, socket }          { :reply, :error, socket }         permitted_topic?(, _), : false   permitted_topic?([], _), : false   permitted_topic?(permitted_topics, topic)     matches = fn permitted_topic ->      pattern = String.replace(permitted_topic, , )      Regex.match?(~r/#{pattern}\z/, topic)        .any?(permitted_topics, matches) ``` |

This is all straight from Daniel's original tutorial, the important bit for this example is the first "join" function, the others deal with permissions and authentication that came through a JWT claim. I will deal with this in Part 2.

To make this work, I had to add the dependencies in "mix.exs":

|  |  |
| --- | --- |
| ``` 12345678910111213141516 ``` | ``` # mix.exsdefmodule ExPusherLite.Mixfile   use .Project  ...  defp deps     [{:phoenix, ~> 1.0.3},     {:phoenix_ecto, ~> 1.1},     {:postgrex, >= 0.0.0},     {:phoenix_html, ~> 2.1},     {:phoenix_live_reload, ~> 1.0, : },     {:cowboy, ~> 1.0},     {:joken, ~> 1.0.0},     {:guardian, ~> 0.7.0}]    ... ``` |

And add the configuration at "config.exs":

|  |  |
| --- | --- |
| ``` 12345678910 ``` | ``` # config/config.exs...config :joken, config_module: Guardian.config :guardian, Guardian,  issuer: ExPusherLite,  : { , :days },  verify_issuer: false,  serializer: ExPusherLite.GuardianSerializer,  atoms: [:listen, :publish, :crews, :email, :name, ] ``` |

Now I have to add a normal HTTP POST endpoint, first adding it to the router:

|  |  |
| --- | --- |
| ``` 123456789101112131415161718 ``` | ``` # web/router.exdefmodule ExPusherLite.Router   use ExPusherLite., :router  pipeline :browser     plug :accepts, []    plug :fetch_session    plug :fetch_flash    #plug :protect_from_forgery    plug :put_secure_browser_headers    ...  scope , ExPusherLite     pipe_through :browser # Use the default browser stack    get , PageController, :index    post /events, EventsController, :create ``` |

Notice that I totally disabled CSRF token verification in the pipeline because I am not sending back Phoenix CSRF token from the Rails controller. Now, the "EventsController" is also almost all from Daniel's tutorial:

|  |  |
| --- | --- |
| ``` 123456789101112131415161718192021222324 ``` | ``` # web/controllers/events_controller.exdefmodule ExPusherLite.EventsController   use ExPusherLite., :controller  plug :authenticate   create(conn, params)     topic = params[topic]    event = params[event]    message = (params[payload] || ) |> Poison.decode!    ExPusherLite.Endpoint.broadcast! topic, event, message    json conn,     defp authenticate(conn, _)     secret = Application.get_env(:ex_pusher_lite, :authentication)[:secret]    Basic  <> auth_token = hd(get_req_header(conn, authorization))     .Crypto.secure_compare(auth_token, .encode64(secret))       conn          conn |> send_resp(, ) |> halt ``` |

I had to change the authenticate function a bit because either I didn't understood Daniel's implementation or it expected something different. But in this version I am just expecting a simple Basic HTTP Authentication "authorization" header which is a string with the format "Basic [base64 username:password]". Look how I am pattern matching the string, removing the Base64 and ["secure comparing"](http://codahale.com/a-lesson-in-timing-attacks/) it (a constant-time binary compare to avoid timing attacks, this comes built-in with Phoenix).

This is a simple authentication technique for the Rails controller to POST the message trigger just the same as in the Pusher version.

And this is it, this is all it takes for this initial Phoenix-based Pusher replacement.

## Ex Pusher Lite - Part 2: Changing the Rails application

Now that we have a bare bone Phoenix app that we can start through "mix phoenix.server" and make it available at "localhost:4000" we can start changing the Rails application.

As I said in the beginning, my original wish was to use the same Pusher javascript client but change the endpoint, turns out it's more difficult than I thought, so I will start by removing the following line from the application layout:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` <script =//js.pusher.com/3.0/pusher.min.js</script> ``` |

We can get rid of the Pusher gem in the Gemfile and the "pusher.rb" initializer as well.

Now, a replacement for the "pusher.min.js" is Phoenix own "phoenix.js" that comes bundled in "deps/phoenix/web/static/js/phoenix.js". The problem is that it is an ES6 javascript source that Phoenix passes through Brunch to be transpiled back to ES5 in every Phoenix application.

But I am copying this file directly to the Rails repository at "app/assets/javascripts/phoenix.es6". I could change it to ES5 but I decided to go the more difficult path and just add Babel support to Rails Asset Pipeline using [Nando's very helpful tutorial](http://nandovieira.com/using-es6-with-asset-pipeline-on-ruby-on-rails) on the subject.

The gist goes like this, first we add the dependencies in the Gemfile:

|  |  |
| --- | --- |
| ``` 12345678910 ``` | ``` # Use SCSS for stylesheets#gem 'sass-rails', '~> 5.0'gem sass-rails, github: rails/sass-rails, branch: mastergem sprockets-rails, github: rails/sprockets-rails, branch: mastergem sprockets, github: rails/sprockets, branch: mastergem babel-transpiler...source https://rails-assets.org   gem rails-assets-almond ``` |

Babel needs some configuration:

|  |  |
| --- | --- |
| ``` 12345678 ``` | ``` # config/initializers/babel.rbRails.application.config.assets.configure  |env|  babel = Sprockets::BabelProcessor.new(    modules    => ,    moduleIds  =>   )  env.register_transformer application/ecmascript-6, application/javascript, babel ``` |

And for some reason I had to manually redeclare application.js and application.css in the assets initializer:

|  |  |
| --- | --- |
| ``` 123 ``` | ``` # config/initializers/assets.rb...Rails.application.config.assets.precompile +=  application.css application.js ``` |

We need Almond in order to be able to import the Socket module from the Phoenix javascript package. Now, we change the "application.js":

|  |  |
| --- | --- |
| ``` 12345678 ``` | ``` //= require almond//= require jquery//= require jquery_ujs//= require turbolinks//= require phoenix//= require_tree .require([application/boot]); ``` |

It require an "app/assets/javascripts/application/boot.es6" file, this is straight from Nando's tutorial:

|  |  |
| --- | --- |
| ``` 12345678910111213141516171819202122232425262728293031323334353637383940 ``` | ``` import  from jquery;function runner() {  // All scripts must live in app/assets/javascripts/application/pages/**/*.es6.   path = ().data(route);  // Load script for this page.  // We should use System.import, but it's not worth the trouble, so  // let's use almond's require instead.   {    require([path], onload, , );  } catch (error) {    handleError(error);  }}function onload(Page) {  // Instantiate the page, passing <body> as the root element.   page =  Page((document.body));  // Set up page and run scripts for it.   (page.setup) {    page.setup();  }  page.run();}// Handles exception.function handleError(error) {   (error.message.match(undefined missing)) {    console.warn(missing module:, error.message.split().pop());  }  {    throw error;  }}(window)  .ready(runner)  .on(page:load, runner); ``` |

And it relies on attributes in the body tag, so we change our layout template:

|  |  |
| --- | --- |
| ``` 123 ``` | ``` <!-- app/views/layouts/application.html.erb -->...<body data-route=application/pages/<%= controller.controller_name %/<%= controller.action_name %>" ``` |

I didn't mention before but I also have a "HomeController" just to be the root path for the main HTML page, it has a single "index" method and "index.html.erb" template with the message form. So I will have the need for an "application/pages/home/index.es6" inside the "app/assets/javascripts" path:

|  |  |
| --- | --- |
| ``` 123456789101112131415161718192021222324252627282930313233343536373839 ``` | ``` import {Socket} from phoenixexport default class Index {  constructor(root) {    .root = root;  }  setup() {    // add event listeners    console.log(-> Setting up Pusher Lite socket)    let guardianToken = (meta[name=guardian-token]).attr(content)    let csrfToken     = (meta[name=guardian-csrf]).attr(content)    let pusherKey     = (meta[name=pusher_key]).attr(content)    let pusherChannel = (meta[name=pusher_channel]).attr(content)    let socket =  Socket(ws://localhost:4000/socket, {      params: { guardian_token: guardianToken, csrf_token: csrfToken }    })    socket.connect()    // Now that you are connected, you can join channels with a topic:    let channel = socket.channel(pusherChannel, {})    channel.join()      .receive(, resp => { console.log(Joined successfully, resp) })      .receive(error, resp => { console.log(Unable to join, resp) })    channel.on(, data => {      let new_line = <p><strong>${data.name}<strong>: ${data.message}</p>      (.message-receiver).append(new_line)    })  }  run() {    // trigger initial action (e.g. perform http requests)    console.log(-> perform initial actions)  }} ``` |

This bit is similar to the Pusher javascript handling, but we are getting a bit more information from the meta tags, the "guardian-token" and "guardian-csrf" tokens. Because I was following Daniel's tutorial I also changed the name of the event from "new\_message" to just "msg" and the topics now need to have a "public:" prefix in order for the Phoenix's RoomChannel handler to match the public topic name correctly.

First things first. In order for this new javascript to have the correct tokens I had to add the following helper in the views layout:

|  |  |
| --- | --- |
| ``` 12345 ``` | ``` ...  <%= csrf_meta_tags %>  <%= guardian_token_tags %></head>... ``` |

And this "guardian\_token\_tags" is again straight from Daniel's tutorial:

|  |  |
| --- | --- |
| ``` 1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859 ``` | ``` module GuardianHelper  ISSUER = pl-web-Rails.env  DIGEST = OpenSSL::Digest.new(sha256)   guardian_token_tags    token = Base64.urlsafe_encode64(SecureRandom.random_bytes())    [      <meta content=jwt(token) name=guardian-csrf />,      <meta content=token name=guardian-token />,    ].shuffle.join.html_safe    private   (token)    .encode(jwt_claims(token), Rails.application.secrets.pusher_key, HS256)     jwt_claims(token)    {      : :csrf,      : jwt_sub,      : ISSUER,      : .now.utc.to_i,      : (.now + .days).utc.to_i,      s_csrf: guardian_signed_token(token),      listen: jwt_listens,      publish: jwt_publish,    }     jwt_sub    return {} unless current_human.present?    {      : current_human.id,      : current_human.full_name,      email: current_human.email,      crews: current_human.crews.map(&:identifier),    }     jwt_listens    listens = [deploys:web, public:*]    listens.push(private:*)  current_human.try(:in_crew?, :admins)    listens     jwt_publish    publish = [public:*]    publish.push(private:*)  current_human.try(:in_crew?, :admins)    publish     guardian_signed_token(token)    key = Rails.application.secrets.pusher_key    signed_token = OpenSSL::.digest(DIGEST, key, token)    Base64.urlsafe_encode64(signed_token).gsub(={1,}$, ) ``` |

I had to tweak it a bit, specially to get the proper keys from the "secrets.yml" file which now looks like this:

|  |  |
| --- | --- |
| ``` 12345678910111213141516171819202122 ``` | ``` development:  secret_key_base: ded7c4a2a298c1b620e462b50c9ca6ccb60130e27968357e76cab73de9858f14556a26df885c8aa5004d0a7ca79c0438e618557275bdb28ba67a0ffb0c268056  pusher_url: http://<%= ENV['PUSHER_KEY'] %>:<%= ENV['PUSHER_SECRET'] %>@<%= ENV['PUSHER_URL'] %>  pusher_key: <%= ENV['PUSHER_KEY'] %>  pusher_secret: <%= ENV['PUSHER_SECRET'] %>  pusher_channel: public:test_chat_channel:  secret_key_base: f51ff494801ff0f9e1711036ef6f2f6f1e13544b02326adc5629c6833ae90f1a476747fae94b792eba8a444305df8e7a5ad53f05ea4234692ac96cc44f372029  pusher_url: http://<%= ENV['PUSHER_KEY'] %>:<%= ENV['PUSHER_SECRET'] %>@<%= ENV['PUSHER_URL'] %>  pusher_key: <%= ENV['PUSHER_KEY'] %>  pusher_secret: <%= ENV['PUSHER_SECRET'] %>  pusher_channel: public:test_chat_channel# Do not keep production secrets in the repository,# instead read values from the environment.production:  secret_key_base: <%= ENV["SECRET_KEY_BASE"] %>  pusher_url: http://<%= ENV['PUSHER_KEY'] %>:<%= ENV['PUSHER_SECRET'] %>@<%= ENV['PUSHER_URL'] %>  pusher_key: <%= ENV['PUSHER_KEY'] %>  pusher_secret: <%= ENV['PUSHER_SECRET'] %>  pusher_channel: <%= ENV['PUSHER_CHANNEL'] %> ``` |

My local ".env" file looks like this:

|  |  |
| --- | --- |
| ``` 1234 ``` | ``` PUSHER_URL: "localhost:4000"PUSHER_KEY: "14e86e5fee3335fa88b0"PUSHER_SECRET: "2b94ff0f07ce9769567f"PUSHER_CHANNEL: "public:test_chat_channel" ``` |

This bit needs more working, I know. I just copied Pusher's key and Pusher's password as KEY and SECRET. This is the bit I mentioned I tweaked in the RoomChannel's authenticate function in the Phoenix side.

Now that I have this in place, I have to change the "PusherEvent" model to trigger the message from the form to the Phoenix's EventsController, like this:

|  |  |
| --- | --- |
| ``` 123456789101112131415161718 ``` | ``` # app/models/event.rbrequire net/httprequire class PusherEvent  include ActiveModel::Model  attr_accessor :name, :message  validates :name, :message, presence:        uri = .parse(Rails.application.secrets.pusher_url/events)    ::.post_form(uri, {      topic => Rails.application.secrets.pusher_channel,      event => ,      payload => { => name, message => message}.to_json    }) ``` |

As I am doing this through SuckerPunch, I am using plain old "Net::HTTP.post()" to post the message to the Phoenix "/events" endpoint. Phoenix will properly authenticate because the "pusher\_url" is sending the "PUSHER\_KEY:PUSHER\_SECRET" as HTTP Basic Auth. It will end up in the "authorization" header and Phoenix will properly authenticate the server side, then it will broadcast to the WebSocket connections subscribed to the topic.

The new javascript will subscribe to the "public:test\_chat\_channel" topic and listen to the "msg" event. Once it receives the payload, it just formats the message and, again, appends to the same place in the "message-receiver" div tag.

### Conclusion: Further Work

So, with this we have exactly the same behavior than the Pusher version, but now it's under my control.

The idea is for the Phoenix app to have apps, a real authentication for different apps. Then every Rails app I do can just connect to this same Phoenix service.

The next steps include properly implementing the Guardian/JWT pieces, then I can jump to private channels support and add HTTP APIs to list channels in apps and users online in channels.

I will then create a second companion Rails app as an administration dashboard to consume those APIs and be able to create or revoke apps and basic maintenance and reporting. This should be a good enough replacement for a Pusher-like messaging solution that is really fast.
