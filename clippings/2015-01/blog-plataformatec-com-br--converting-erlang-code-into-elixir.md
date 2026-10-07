---
url: "http://blog.plataformatec.com.br/2014/11/converting-erlang-code-into-elixir/"
captured_at: "2015-01-16T20:51:17-03:00"
title: "Converting Erlang code into Elixir « Plataformatec Blog"
domain: "blog-plataformatec-com-br"
---

# Converting Erlang code into Elixir « Plataformatec Blog

When you are new to any language, you probably want to run some existing code just to see how it works. [Achieving success](https://www.youtube.com/watch?v=Djv4C9H9yz4) while trying new things is important, because it helps fueling your interest.

The number of code examples in Elixir is increasing, but sometimes you will have to read some Erlang code. Recently, I wanted to play a little bit with Cowboy HTTP Server, which is written in Erlang. The Cowboy repo has a lot of [small examples](https://github.com/ninenines/cowboy/tree/b57f94661f5fd186f55eb0fead49849e0b1399d1/examples) presenting the features which is provided by it. When I tried to convert one of them to Elixir, it wasn’t as simple as I expected, since I’m not so familiarized with the language yet.

When converting, you may get into some misleading code that will not work as you expected at first. So, I’m going to present a transcoding of [Cowboy WebSocket server example](https://github.com/ninenines/cowboy/tree/b57f94661f5fd186f55eb0fead49849e0b1399d1/examples/websocket) from Erlang to Elixir, so that you can learn some of the details that exists in the process of porting Erlang code into Elixir code.

This will not be a tutorial explaining how that Cowboy example works, it’s just about how to convert it to Elixir. Also, I’m not going to show how it could be done in idiomatic Elixir, the goal here is to translate Erlang code into Elixir the simplest way possible.

So let’s start!

## Creating the project

Create a project called `ws_cowboy` with the following command:

```
mix new ws_cowboy
 ws_cowboy
```

After that we are going to change/create 4 files:

- `mix.exs`: declares the dependencies in the project and the application module to run
- `lib/ws_cowboy.ex`: the application module that setups the cowboy routes and http server
- `lib/ws_handler.ex`: handles a WebSocket request connection
- `lib/ws_supervisor.ex`: supervisor for Cowboy server

Also, copy the whole [`priv`](https://github.com/ninenines/cowboy/tree/b57f94661f5fd186f55eb0fead49849e0b1399d1/examples/websocket/priv) directory from the [Cowboy example](https://github.com/ninenines/cowboy/tree/b57f94661f5fd186f55eb0fead49849e0b1399d1/examples/websocket) to the project’s root dir.

## The project definition

In the `mix.exs` file we are going to add the Cowboy dependency and also configure the module application, in this case `WsCowboy`.

```
defmodule WsCowboy.Mixfile 
   Mix.Project

   project 
    [ :ws_cowboy,
     version: "0.0.1",
     elixir: "~> 1.0",
     deps: deps]
  

  # Configuration for the OTP application
  
  # Type `mix help compile.app` for more information
   application 
    [applications: [:logger, :cowboy],
      {WsCowboy, []}]
  

  # Dependencies can be Hex packages:
  
  #   {:mydep, "~> 0.3.0"}
  
  # Or git/path repositories:
  
  #   {:mydep, git: "https://github.com/elixir-lang/mydep.git", tag: "0.1.0"}
  
  # Type `mix help deps` for more examples and options
  defp deps 
    [{:cowboy, "~> 1.0.0"}]
```

## Configuring the HTTP application

Here is the transcode of `websocket_app.erl` file to the `ws_cowboy.ex` file:

```
defmodule WsCowboy 
  @behaviour :application

   start(_type, _args) 
    dispatch = :cowboy_router.compile([
      {, [
        {, :cowboy_static, {:priv_file, :ws_cowboy, "index.html"}},
        {"/websocket", WsHandler, []},
        {"/static/[...]", :cowboy_static, {:priv_dir, :ws_cowboy, "static"}}
      ]}
    ])
    {,  = :cowboy.start_http(:http, , [{:port, }],
                                  [{, [{:dispatch, dispatch}]}])
    WsSupervisor.start_link
  

   (_state)
```

If you never read any Erlang code and you came from a language like Ruby, you might get confused on basic things. So, let’s go through some of the details of porting `websocket_app.erl` to the `ws_cowboy.ex`.

Erlang files represents a module, in Elixir it is the same thing, but in this case we use the `defmodule` macro. Erlang modules can be accessed using `:<module_name>`, so in this case we are defining that this module has the application behaviour.

Different from other languages like Ruby, lowercase names aren’t variables in Erlang, but atoms, while in Elixir atoms look the same as Ruby symbols. So, we scanned every lowercase names and replaced them with `:<name>`.

Upper case names in Erlang aren’t constant but variables, so we changed them to lowercase. It is good to do this in inverse order to avoid mixing variables and atoms.

During the process of converting this file, there was a line making the application not work and I spent some time trying to figure out what was wrong. In Ruby, `'foo'` and `"foo"` are both strings, but in Elixir and Erlang they are different things. The single quote in Erlang is an atom (symbol), so the `'_'` line must be converted to `:_` in Elixir. If you miss this little detail, unfortunately it will compile and run, but Cowboy will always return a 400 status code.

Except that, everything is pretty straightforward, the only detail is the `:cowboy_static` definition that you have to replace with your dir app name, in this case `:ws_cowboy`.

To transcode function calls, you just have to replace the `:` with `.`, like in Ruby.

## Handling the WebSocket connection

You can read more about how Cowboy handles WebSocket [here](http://ninenines.eu/docs/en/cowboy/HEAD/guide/ws_handlers/). Here’s the transcode of the file `ws_handler.erl` to `ws_handler.ex`:

```
defmodule WsHandler 
  @behaviour :cowboy_websocket_handler

   ({, :http}, _req, _opts) 
    {:upgrade, :protocol, :cowboy_websocket}
  

   websocket_init(_transport_name, req, _opts) 
    :erlang.start_timer(, (), "Hello!")
    {, req, :undefined_state}
  

   websocket_handle({:text, msg}, req, state) 
    {:reply, {:text, "That's what she said! #{msg}"}, req, state}
  

   websocket_handle(_data, req, state) 
    {, req, state}
  

   websocket_info({:timeout, _ref, msg}, req, state) 
    :erlang.start_timer(, (), "How' you doin'?")
    {:reply, {:text, msg}, req, state}
  

   websocket_info(_info, req, state) 
    {, req, state}
  

   websocket_terminate(_reason, _req, _state)
```

Following the steps done in the previous file, there is no secret on this one. The only detail is that the Erlang version used binary notation for strings, but in Elixir you can use just `"string"` normally. Also, you can use string interpolation `"That's what she said! #{msg}"`.

## Writing the supervisor

Now there’s just one translation missing, from `websocket_sup.erl` to `ws_supervisor.ex`. Here we just used `__MODULE__` instead of the Erlang `?MODULE`:

```
defmodule WsSupervisor 
  @behaviour :supervisor

   start_link 
    :supervisor.start_link({:local, __MODULE__}, __MODULE__, [])
  

  
    procs = []
    {, {{:one_for_one, , }, procs}}
```

## Running your server

Running your server is pretty easy, just run the `mix run --no-halt` command and check http://127.0.0.1:8080 in your browser.

## Conclusion

The goal of this post was to show an example of how to port Erlang code into Elixir code. The result we got is the simplest translation possible, it was not my idea to write idiomatic Elixir here. For example, in Elixir you would not use Erlang’s supervisor module, but rather the Elixir’s supervisor.

I hope you could get the picture of how it is to translate Erlang code into Elixir, how it’s not so hard and some of the details that you must pay attention while doing it.

If you are interesting in learning more about Elixir, check out the [getting started page](http://elixir-lang.org/getting_started/1.html).

*Do you had any issues when starting to play with Elixir that you cracked your head to figuring out why it didn’t work? Share your experience and doubts with us!*

[Like what you've read? Click here to subscribe to our blog!](http://cta-service-cms2.hubspot.com/cs/c/?&cta_guid=802dcfad-048a-49b9-9ff1-36be9fe0d702&placement_guid=2aeae558-5b72-4df3-bf32-e1119f34d85e&portal_id=378213&redirect_url=vxV%2B4KcMvLA9AN6xRET%2B8J/o3sX9Cg%2BizerniHmlh8YlQy/VZGxwVzc7l1cV%2B/rRMcOyvHf3cvJrCQvHms4%2BDWZkCmAraU4duXCFVnEevV7rOQSAdcgPtCLluROvkbFKDupPKNXES2oGYjdoh3YK8VVx6x4hfcPQMASFHWPUDfqIz1thuxE6j921ElYs5EqMseFcT2dKOAzdBrzkJ7pDbizlErL1X3hG86bPz3T1AM0%3D&iv=TgtuFJ5KIuo%3D&hsutk=e40c660b0bf9ef194ea8847443f73ad4&utm_referrer=http%3A%2F%2Fblog.plataformatec.com.br%2F2014%2F11%2Fconverting-erlang-code-into-elixir%2F&canon=http%3A%2F%2Fblog.plataformatec.com.br%2F2014%2F11%2Fconverting-erlang-code-into-elixir%2F&__hstc=215850376.e40c660b0bf9ef194ea8847443f73ad4.1420580498394.1420580498394.1421450530499.2&__hssc=215850376.2.1421450530499&__hsfp=3873217458 "Like what you've read? Click here to subscribe to our blog!")
