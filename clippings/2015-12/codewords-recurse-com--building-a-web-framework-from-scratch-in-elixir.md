---
url: "https://codewords.recurse.com/issues/five/building-a-web-framework-from-scratch-in-elixir"
captured_at: "2015-12-21T15:29:45-03:00"
title: "Building a web framework from scratch in Elixir"
domain: "codewords-recurse-com"
---

# Building a web framework from scratch in Elixir

[Robert Lord](https://codewords.recurse.com/about#Robert Lord)

[Elixir](http://elixir-lang.org/) is a fantastic new functional programming language that targets the Erlang VM, designed to build fault-tolerant distributed systems. There are numerous exciting use-cases, but one that always gets a lot of attention is building web applications. Elixir already has a Rails-like framework called Phoenix, but today, we’ll use a much more simple library, called Plug, to write a Sinatra-like web framework from scratch.

## Why you should care

Phoenix is a great framework, and actually uses Plug under the hood. It works well with other Plug-compatible libraries, but tends to put these features behind macros, obfuscating the direct calls to Plug functions. I think that understanding the way the underlying Plug library works is an excellent way to learn both Elixir and Phoenix, both because it helps you understand what Phoenix’s macros are doing under the surface, and also because writing performant code is incredibly simple and easy with just Plug, Elixir, and Erlang’s pattern-matching. We *could* just browse through Phoenix’s macro definitions, but those are difficult to understand, since there’s a lot of extra code to make the DSLs work properly. Instead, we’ll write straightforward code ourselves, using Plug directly to build our own framework from scratch! Who knows, maybe you’ll even find you prefer the simple router that we build.

## Following along

If you are already familiar with the basics of Elixir’s syntax, that’s great, though not required. I’ll do my best to explain the trickier parts in more depth in case you aren’t, but if you get stuck, try taking a look at the [Elixir Crash Course](http://elixir-lang.org/crash-course.html).
You don’t need to know anything about Phoenix, although I’m assuming you’ve programmed a web app before in some language or framework, and won’t explain simple concepts like headers and query strings.

To follow along with this guide, you’ll need [Elixir installed](http://elixir-lang.org/install.html), and you’ll also need to create a new project with `mix new helloplug`. Then, add Cowboy, Plug, Ecto, and Sqlite.Ecto to your project’s `mix.exs` file by adding the following lines:

```
  :cowboy ~> 1.0.0"
   :plug ~> 1.0"
   :sqlite_ecto ~> 1.0.0"
   :ecto ~> 1.0"

 application 
  applications: :logger :sqlite_ecto :ecto :cowboy :plug
```

Don’t forget to run `mix deps.get` when you’re done! Once the Plug is set up properly, you can write any code in the `lib/helloplug.ex` file, although if you’re comfortable with it, Elixir’s standard directory structure[1](https://codewords.recurse.com/issues/five/building-a-web-framework-from-scratch-in-elixir#fn:1) is cleaner.

## What is a Plug?

A Plug is a module that responds to web requests. To create one, we just need two functions, `init/1`[2](https://codewords.recurse.com/issues/five/building-a-web-framework-from-scratch-in-elixir#fn:2) and `call/2`.

```
defmodule Helloplug 
   default_opts 
     starting up Helloplug..."
    default_opts
  

    _opts 
     saying hello!"
    send_resp  Hello, world!"
```

`init/1` is called once when the server is started, and `call/2` is called every time a new request comes in. There are *two* arguments to `call/2`.

- `conn`: This is a `Plug.Conn`, the connection with the client. It contains information about the request. We also use it to send responses.
- `opts`: This is whatever the output of our `init/1` function was. It doesn’t change from request to request.

Any options passed to the module are given to `init/1`. We’ll take a look at that later, but for now, just know that whatever `init/1` returns gets passed to every subsequent `call/2`.

Finally, let’s take a look at `send_resp`. This is a function that accepts three arguments: the connection, the HTTP status code to send, and the body of the reply to send. You’ll note that this is the last line of `call/2`, and this is intentional. In Elixir, the last line of a function is implicitly returned. `send_resp`, as well as the rest of the `Plug.Conn` functions, returns a mutated copy of `conn`, and it’s important that `call/2` returns this mutated `conn` so that the outside function calling it knows what has changed.

We can connect `Helloplug` to cowboy, the web server, by running `iex -S mix` in the project directory, and typing `{:ok, _} = Plug.Adapters.Cowboy.http Helloplug, []` into the resulting Elixir REPL.[3](https://codewords.recurse.com/issues/five/building-a-web-framework-from-scratch-in-elixir#fn:3) If you browse to `http://localhost:4000` a few times, you should see “Hello, world!” in your browser, and this in the terminal:

```
starting up Helloplug...
saying hello!
saying hello!
saying hello!
```

The `call` function is run every time we visit the web page. We can also use the `conn` object to set headers.

```
  _opts 
   saying hello!"
   |> put_resp_headerServer" Plug" |> send_resp Hello, world!"
```

In case you haven’t seen the `|>` operator before, `A() |> B() |> C()` is equivalent to `C(B(A))`. We could rewrite the line above if we wanted a less idomatic and more verbose version:

```
conn2  put_resp_header Server" Plug"
send_respconn2  Hello, world!"
```

If there are arguments passed to any of the functions, the output of the previous function is inserted *before* the specified arguments. So `conn |> Plug.Conn.put_resp_header("Server", "Plug")` is equivalent to `Plug.Conn.put_resp_header(conn, "Server", "Plug")`. Also, remember that the last statement of a function in Elixir is implicitly returned.

`put_resp_header` and `send_resp` are two examples of functions that manipulate connections. If you’ve done some web programming before, you’ll likely recognize what they do—they add a header to the response `Server: Plug` and then send the response “Hello, world!” with status code `200 OK`. Neither of these functions can modify `conn` directly, since all variables and values in Elixir are immutable. That’s why we can’t have this:

```
# This is broken!
put_resp_header Server" Plug"
send_resp  Hello, world!"
```

`put_resp_header` doesn’t touch the `conn` passed to it, but it *does* return a duplicated, modified version of the `conn`. We *need* the mutated `conn` returned from `put_resp_header` to go into `send_resp`, which is why we chain the output from one function into the first argument of the next with `|>` in the first example. With the broken code, `send_resp` is receiving the original `conn` with no `Server` header, which means that no `Server` header would be sent to the client.

There are a number of other `Plug.Conn` functions for manipulating connection details. Check out the [Plug.Conn documentation](http://hexdocs.pm/plug/Plug.Conn.html) for a full list.

The connection object is not just for sending responses. It contains the details of the request, too! We can use Elixir’s powerful pattern matching to match based on `conn`’s `path_info` (the path requested, split on `/` into an array) to call different functions for different pages. We can also match on `method` so that a `POST` request calls a different function than a `GET` request.

```
  _opts 
  routemethod path_info 

 route hello"  
  # this route is for /hello
   |> send_resp Hello, world!"

 route users" user_id  
  # this route is for /users/<user_id>
   |> send_resp You requested user user_id

 route_method _path  
  # this route is called if no other routes match
   |> send_resp Couldn't find that page, sorry!"
```

The second route shows off my favorite part of using this syntax—we can extract a `user_id` variable from the URL entirely using Elixir’s pattern matching.

## Writing a macro

We may want to have separate routers for different parts of our application, all using this `route` syntax. Rather than retyping the same identical `call` in every router, we can move it into a macro, and then just call the macro in each router. Macros are evaluated at compile time, so the Erlang VM will receive the same code, and we get to [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) up our code. We can also reuse this macro in future projects.

```
defmodule Router 
  defmacro __using___opts 
    quote 
       options 
        options
      
        _opts 
        routemethod path_info 
      
    
  

defmodule Helloplug 
   Router
   route users" user_id  
     |> send_resp You requested user user_id
  
   route_method _path  
     |> send_resp Couldn't find that page, sorry!"
```

Remember that `call` needs to return the modified connection object. When Plug runs `call/2`, this is how it knows what has changed about the connection. However, it also makes it *composable*. We can call plugs within other plugs. For instance, let’s say we want to route all calls to user endpoints to a different Plug:

```
defmodule UserRouter 
   Router
   route users" user_id  
    # this route is for /users/<user_id>
     |> send_resp You requested user user_id
  
   routePOST" users"  
    # do some sort of database insertion here maybe
  
   route_method _path  
     |> send_resp Couldn't find that user page, sorry!"
  

defmodule WebsiteRouter 
   Router

  @user_router_options UserRouter
   route users"    
    UserRouter @user_router_options
  
   route_method _path  
     |> send_resp Couldn't find that page, sorry!"
```

If you haven’t seen the syntax for module attributes used in `@user_router_options UserRouter.init([])` before, when `WebsiteRouter` is compiled, it stores the output from `UserRouter.init([])` and inserts it anywhere you see `@user_router_options` appear. It’s a compile-time constant for the module. We run it once to get the options hash. We don’t use the options hash in UserRouter, but we need to do this in case we’re using a plug that does.

Also, remember when I mentioned `init/1` could sometimes be passed options from outside? This is where we could do that! For instance, (to use a somewhat contrived example) maybe we want to treat two different models, `User` and `Admin` almost identically. We could create one plug, and initialize it twice, passing a different model into the options each time. Our plug’s `init/1` would return the options given to it, and our `call/2` function would then be able to see via its second parameter whether it should serve `User` objects or `Admin` objects.

A Plug doesn’t need to be a router—we could use this technique to include Plugs that do authentication, DOS protection, logging, and more. For instance, if there was a third-party `ApiLogPlug` module, we could add it as a dependency, and update our user route to use it:

```
@user_router_options UserRouter
@api_logger_options ApiLogPlug
 route users"  _path 
   |> ApiLogPlug@api_logger_options |> UserRouter@user_router_options
```

## Basic templates

At some point, we’re probably going to want to serve more than just plain text with our framework. We *could* continue to write HTML strings manually, but that’s not practical for larger webapps. Fortunately, Elixir comes built-in with a [handy templating language](http://elixir-lang.org/docs/v1.0/eex/). We can use it pretty easily:

```
 route users" user_id  
  page_contents  eval_filetemplates/show_user.eex" user_id: user_id
   |> put_resp_content_typetext/html" |> send_resp page_contents
```

The first argument to `eval_file` is the filename of the template, and the second is a map of variables that we’ll be able to use inside the template. We’ll also need to create a template, which we can do in our project directory under `templates/show_user.eex`. Elixir’s templating language is similar to many other templating languages, especially Ruby’s `erb`.

```
<!DOCTYPE html>
<html>
  <body>
    <h1>User Information Page</h1>
    <p>Looks like you've requested information for the user with id %= user_id %>.</p>
    <p>Also, 1 + 1 = %= 1 + 1 %></p>
    %= if user_id == "0" do %>
      %# we should tell everybody that user 0 is really cool %>
      User zero is really cool!
    % end %>
  </body>
</html>
```

As you can see above, you can put any sort of Elixir statement in a `<% %>` block and it will run. Adding a equal sign like `<%= %>` will make it print the statement’s result to the page, and `<%# %>` creates a comment that will not be sent to the client. Note how we have a `=` before the if statement—everything that prints something to the page needs an `=`. The `if` statement returns the contents of the block inside of it, and we need the `=` to make it print instead of discarding it.

If we visit `/users/1092`, we should now see a rendered HTML page stating that we requested information on user 1092.

## Precompiling templates

Our template code is a little inefficient, though, since every time the route is called, Elixir has to load the template file, parse the template file into an Elixir function, and then run the function. If we can just parse and compile the template once, and then run the function every time the route is called, we’ll save a lot of time, especially for larger, frequently-called templates.

```
require  # you have to require EEx before using its macros outside of functions
function_from_file :defp :template_show_user templates/show_user.eex" :user_id
 route users" user_id  
  page_contents  template_show_useruser_id
   |> put_resp_content_typetext/html" |> send_resp page_contents
```

## Ecto models

Phoenix, the Rails-like framework we talked about earlier, has a database model library called Ecto.
Fortunately, Ecto is a standalone project, so we can use it too! Let’s update our `/users/<user_id>` route to actually retrieve user data from a Sqlite database. In your config.exs file, add:

```
config :helloplug Helloplug
  adapter: Sqlite
  database: hello_plug.sqlite3"
```

We’re also going to need to create a new module for our database’s “Repo”, a module that holds functions that query our database.

```
defmodule Helloplug 
   
    otp_app: :helloplug
    adapter: Sqlite
```

We’ll also need a `User` model.

```
defmodule  
   Model

  schema users" 
    # id field is implicit
    field :first_name :string
    field :last_name :string
```

The Ecto schema has [way too many options](http://hexdocs.pm/ecto/Ecto.Schema.html) to even start covering here. If you start using Ecto more, you should read the docs.

We’re also going to need this `User` model to actually exist as a table in the database—let’s do that now. Run `mix ecto.gen.migration create_users` to generate an empty migration, and then we’ll update the migration’s `change` function.

```
 change 
  create table:users 
     :first_name :string
     :last_name :string

    timestamps
```

You can run migrations with `mix ecto.migrate`.

We’ll need to modify our UserRouter to actually use this User model:

```
 route users" user_id  
   Helloplug user_id 
     ->
       |> send_resp User with that ID not found, sorry"
     ->
      page_contents  eval_filetemplates/show_user.eex" user: 
       |> put_resp_content_typetext/html" |> send_resp page_contents
```

And finally, let’s update our template to list the first and last name of the user.

```
<%= first_name  <%= last_name  </
Looks   requested information      <%=  >.</
<%=  first_name  Fluffums"  
        Fluffums  awesome
```

Our database is empty, so let’s fix that! If we jump into an Elixir shell with `iex -S mix`, we can use Ecto to insert a record.

```
iex> Helloplug.Repo.start_link
iex> user = %User{id: 1, first_name: "Fluffums", last_name: "the Cat"}
iex> Helloplug.Repo.insert!(user)
```

The `User` struct is something we get for free when we create an Ecto model! We can just pass the struct to `Repo`, and it’ll automatically figure out which table to insert it into in the database.

Now, if we run the web server and visit `localhost:4000/users/1`, we should see “Fluffums the Cat” appear on our screen! Success!

## Testing everything

One of the coolest features of this functional setup is that it’s incredibly simple to test! We don’t need any fancy magic; all we need to do is pass a fake `Conn` to our router’s `call` function, and inspect the result we get back. Elixir ships with a unit testing framework called [ExUnit](http://elixir-lang.org/docs/stable/ex_unit/ExUnit.html) that we can use. We won’t go in-depth into to the nuances of testing in Elixir, but here is an example Plug test:

```
defmodule HelloTest 
   ExUnit async: 
   

  @website_router_opts WebsiteRouter
   returns a user" 
       /users/1"
      WebsiteRouter @website_router_opts

    assert state  :sent
    assert status  
    assert Stringmatch?resp_body ~r/Fluffums/
```

`use Plug.Test` simply imports functions from `Plug.Test`, including the `conn` function used above that creates fake connections to pass to the router.

## Our framework’s performance

The Erlang VM’s pattern matching code has been heavily optimized. Rather than do a linear search through all our `route` definitions, the VM actually [does a binary search](http://stackoverflow.com/a/28850816) through all the possibilities, which makes our route lookups run in `O(log n)` time instead of `O(n)`. You’d likely only see improvements if you had a truly gargantuan number of routes in a single router, but still, it’s cool to know that we get this faster routing lookup for free, with no extra work on our end.

By using just a very thin layer over Plug and Cowboy, we get all of the performance benefits put into those projects with very little overhead. Cowboy can run multiple requests through our Plug simultaneously, and since all values in Elixir and Erlang are immutable, our framework is thread-safe by default. These libraries are also just generally fast—Matthew Rothenberg has [a benchmark table](https://github.com/mroth/phoenix-showdown#comparative-benchmark-numbers) comparing various frameworks. In his benchmark, our web framework would rank roughly near the “Plug” listing (it uses Plug’s Router, which works similarly to ours) at 54948 requests per second, which puts it at a higher throughput than even a Go based solution, Gin, which does around 51483 requests per second! These benchmarks are very simplistic, and don’t take into database fetching or a lot of other common web framework tasks, so it’s best to not give much weight to them. Still, it’s exciting to see that our simple framework is competitive with much bigger ones.

Not too shabby, considering we’ve barely written any code, and haven’t been considering performance until now.

## Next steps

One of the cool side-effects of writing our own framework from scratch is that we ~~have~~ *get* to organize our own directory structure! Right now, everything is put together
in the global namespace, which isn’t so great. We could improve this by putting things in sub-modules and sub-directories.[4](https://codewords.recurse.com/issues/five/building-a-web-framework-from-scratch-in-elixir#fn:4) For instance, models could go in a `lib/helloplug/models` folder, and we could call them `Helloplug.Models.User` instead of just `User`.

We could also add some more macros. For instance, the syntax for chaining Plugs together and precompiling templates is clunky. We also have no way of running a Plug before every single route in a router; this could perhaps be an argument passed to `__using__` with a list of Plugs that `call` routes through before calling `route/3`.

We could also use a library like [active](https://github.com/synrc/active) to automatically reload modules when they change.

## Further reading

- The [documentation for Ecto](http://hexdocs.pm/ecto/Ecto.html) is a great reference. In particular, I’d look at the [query reference](http://hexdocs.pm/ecto/Ecto.Query.html), the [schema reference](http://hexdocs.pm/ecto/Ecto.Schema.html), and the [migration reference](http://hexdocs.pm/ecto/Ecto.Migration.html).
- The [Plug documentation](http://hexdocs.pm/plug/extra-readme.html) is great. A lot of the concepts in this article were based off [Plug’s router](http://hexdocs.pm/plug/Plug.Router.html), which similarly uses the Erlang VM’s pattern matching for faster routing. However, I didn’t use it in this article, since I think understanding how the underlying system works is both exciting and educational. It’s also worth taking a look at the [docs for Plug.Test](http://hexdocs.pm/plug/Plug.Test.html), the testing module we saw briefly.
- The [documentation for Eex](http://elixir-lang.org/docs/v1.0/eex/) is great for learning more about templates.
- The [Phoenix framework](http://www.phoenixframework.org/) is quite cool. Their website has some relevant articles on [Ecto](http://www.phoenixframework.org/docs/ecto-models), [templates](http://www.phoenixframework.org/docs/templates), and [deployment](http://www.phoenixframework.org/docs/advanced-deployment). Although some parts are Phoenix-specific, there’s plenty of concepts applicable to any Plug-based framework.

1. At the time of writing, I couldn’t actually find any free, online resource explaining how Elixir projects are laid out, although it is explained in Dave Thomas’ *Programming Elixir*. It mirrors the structure of Ruby’s `lib` folders. The module `One:Two:Three` belongs in `lib/one/two/three.ex`. Multiple words get separated by underscores, so `ModuleName` becomes `module_name.ex`. [↩](https://codewords.recurse.com/issues/five/building-a-web-framework-from-scratch-in-elixir#fnref:1)
2. If you’re not familiar with the meaning of `init/1`—Erlang/Elixir considers the functions with different numbers of arguments to be completely different, so we call `init` with one argument `init/1`, with two arguments `init/2`, etc. [↩](https://codewords.recurse.com/issues/five/building-a-web-framework-from-scratch-in-elixir#fnref:2)
3. We’ll be making a lot of changes to our modules very quickly, so if you’d rather not do this repeatedly, you can reload an existing module in the REPL by simply typing `r` followed by the module name, like `r Helloplug`. You don’t need to swap out the running cowboy server—the Erlang VM hotswaps your new code in for you. [↩](https://codewords.recurse.com/issues/five/building-a-web-framework-from-scratch-in-elixir#fnref:3)
4. Fun fact: The underlying Erlang VM has no concept of nested modules. The dot gets translated to be literally part of the name before it’s passed to the VM. This is why you can’t access functions in the `Helloplug` module automatically from `Helloplug.Models.User`. [↩](https://codewords.recurse.com/issues/five/building-a-web-framework-from-scratch-in-elixir#fnref:4)
