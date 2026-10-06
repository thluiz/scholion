---
url: "http://blog.drewolson.org/elixir-streams/"
captured_at: "2015-06-09T08:57:09-03:00"
title: "Elixir Streams"
domain: "blog-drewolson-org"
---

# Elixir Streams

08 June 2015

I previously [wrote](http://blog.drewolson.org/the-value-of-explicitness/) about explicitness in Elixir. One of my favorite ways the language embraces explicitness is in its distinction between eager and lazy operations on collections. Any time you use the `Enum` module, you're performing an eager operation. Your collection will be transformed/mapped/enumerated immediately. When you use the `Stream` module, you're performing lazy operations.

The `Stream` module provides many of the same operations as `Enum`, but when used with `Stream` they're describing future computations rather than actions to be taken immediately. Conveniently, all streams also implement the `Enumerable` protocol, meaning they can use any of the functions within `Enum`.

You can realize a stream (eagerly forcing the computation to take place) by using any of the functions inside of `Enum`. Let's see some examples. The examples will be a mix of `iex` sessions and Elixir files to help demonstrate the concepts.

#### A Few Examples

Here's an extremely simple example of using the `Stream.map` function.

```
iex()> [, , ] |> Stream.map(&(& + ))  
#Stream<[enum: [1, 2, 3], funs: [#Function<45.29647706/1 in Stream.map/2>]]>
```

I've used an `iex` session because it helps to understand the return value. As you can see, a `Stream` struct is returned. The details are not important now, but you can see that it is storing functions to be applied in the future rather than actually performing any computation on the data immediately.

We can force the computation using the `Enum.to_list` function.

```
iex()> [, , ]  
|> Stream.map(&(& + ))
|> Enum.to_list
[, , ]
```

Let's look at another example that should give us more of an idea of the advantages streams provide over traditional collections. This time, we'll operate on a `Range`. In Elixir, ranges are implemented as streams, meaning we can build very large ranges without immediately realizing them.

```
iex()> ..1000000  
|> Stream.map(&("This is number #{&1}"))
|> Enum.take()
["This is number 1", "This is number 2"]
```

The important thing to understand from this example is that we're using `Stream.map` to represent a transform on a range with 1,000,000 items but we're only ever performing the computation on 2 of them. The `Enum.take` function only asks for 2 items and this means the stream will only perform computation on the first 2 items in the range.

This can be an extremely useful way to represent computation on very large (or even infinitely large) sets of data in a tractable way.

Streams are composable, meaning we can perform an arbitrary number of computation stages efficiently on large collections.

```
iex()> ..1000000  
|> Stream.filter(&Integer.is_even/)
|> Stream.map(&("This is number #{&1}"))
|> Enum.take()
["This is number 2", "This is number 4"]
```

#### Standard Library Streams

Elixir's standard library provides several streams out of the box. We've already seen `Range`. Let's quickly discuss some other commonly used streams.

The `File.stream!` function provides the lines (by default) or bytes of a file in the form a stream. This is a pleasant way to consume file data.

```
"./my_file.txt"
|> File.stream!
|> Stream.map(&String.strip/)
|> Stream.with_index
|> Stream.map( {line, i} -> ": #{line}" )
|> Enum.take()
|> inspect

# => ["0: first line"]
```

This program lazily strips the newline from the end of each line of the file, adds the index at the beginning of each line, takes the first line and prints it. Because we've only asked for the first line, the file could be extremely large and our program would still be efficient.

Another commonly used function that returns a stream is `IO.stream`. As you might expect, this provides a stream interface to things such as standard in. Let's make our previous program operate on standard in rather than a file.

```
stream(:stdio, :line)  
|> Stream.map(&String.strip/)
|> Stream.with_index
|> Stream.map( {line, i} -> ": #{line}" )
|> Enum.take()
|> inspect

# $ elixir foo.ex < my_file.txt
# ["0: first line"]
```

As a final example, the `GenEvent.stream` function creates a stream of events from a `GenEvent` manager. The details of `GenEvent` are beyond the scope of this post, so that's all we'll say on the subject of this function. If you're interested you can read more [in the docs](http://elixir-lang.org/docs/stable/elixir/GenEvent.html#stream/2).

#### Stream Construction

We've just seen a few of the streams provided by Elixir's standard library. Elixir also provides several functions in the `Stream` module that allow you construct your own streams. Let's take a look at a few of them. We'll start with simple constructors and get progressively more complex.

`Stream.repeatedly` is a simple stream constructor that builds an infinite stream by calling the provided function each time an item is requested from the stream. Let's make an infinite stream of all `1`s.

```
iex()> Stream.repeatedly(fn ->  end) |> Enum.take()  
[, , , , ]
```

Next, there's `Stream.iterate`. This takes an initial value and a "generator" function. This function will be called with the previous item in the stream (starting with the initial value) and is expected to return the next item. We can make a stream of all the positive integers.

```
iex()> Stream.iterate(, &(& + )) |> Enum.take()  
[, , , , ]
```

Now, let's talk about `Stream.unfold`. This function is more complex but also allows creating more flexible streams. Unfold takes two arguments: an initial value for the "accumulator" and a generator function. The generator function will be called with the accumulator and is expected to return a tuple of `{next_element, new_accumulator}`. The `next_element` value represents the next item in the stream and the `new_accumulator` will be passed to the generator function on the subsequent call. Let's use `Stream.unfold` to make an infinite stream of the fibonacci sequence.

```
fibs = Stream.unfold({, },  {a, b} ->  
  {a, {b, a + b}}
)

fibs  
|> Enum.take()
|> inspect

# => [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

Note that our accumulator represents two numbers in the sequence because we need both of these numbers to generate the next number.

The last constructor function we'll look at is `Stream.resource`. This function is well suited to building streams around external resources. It is called by providing a "start function", a "next function" and an "after function". It's best understood with an example, so let's use it to wrap Github's API.

#### Building an API with Streams

Many of the resources provided by Github's API return paginated results. We want to make the pagination simple but efficient for the consumers of our library. It should be invisible but also only performed if actually need the results on a given page. First, let's create a Github gateway module that will be responsible for communicating with the Github API. We'll use `HTTPoison` for the HTTP communication.

```
defmodule Github.Gateway   
   HTTPoison.Base

  @endpoint "https://github.com/api/v3"

   endpoint 
    @endpoint
  

   process_url(url) 
    @endpoint <> url
  

   process_request_headers(headers) 
    headers ++ [
      {"Authorization", "Basic #{:base64.encode(credentials)}"}
    ]
  

   credentials 
    "#{config[:access_token]}:x-oauth-basic"
  

   config 
    Application.get_env(:house_keeper, __MODULE__)
```

Our gateway module assumes that we've configured our application with a personal access token.

Responses from Github contain two attributes relevant to our API: the `Link` header and the request body. The `Link` header tells us about the next page of results (if any exists). The request body is a JSON serialized collection of results. Let's create a module that generates a `Stream` around the API response for a given a url. We'll use `Poison` for JSON parsing.

```
defmodule Github.ResultStream   
  alias Github.Gateway

  (url) 
    Stream.resource(
       -> fetch_page(url) ,
      &process_page/,
       -> 
    )
  

   fetch_page(url) 
    response = Gateway.get!(url)
    items = Poison.decode!(response.body)
    links = parse_links(response.headers["Link"])

    {items, links["next"]}
  

   parse_links() 
    %{}
  

   parse_links(links_string) 
    links = String.split(links_string, )

    Enum.map(links,  link ->
      [name] = Regex.run(~r{rel="([a-z]+)"}, link)
      [url] = Regex.run(~r{<([^>]+)>}, link)
      short_url = String.replace(url, Gateway.endpoint, )

      {name, short_url}
    ) |> Enum.into(%{})
  

   process_page({, }) 
    {:halt, }
  

   process_page({, next_page_url}) 
    next_page_url
    |> fetch_page
    |> process_page
  

   process_page({items, next_page_url}) 
    {items, {, next_page_url}}
```

There's a lot of code here, so let's focus on it piece by piece.

```
  (url) 
    Stream.resource(
       -> fetch_page(url) ,
      &process_page/,
       -> 
    )
```

The `new` function returns a `Stream` built using the `Stream.resource` function. We provided it a "start function" that fetches the first page, a "next fuction" that processes each page and fetches a new page if necessary, and an empty "after function". Our "after function" is empty because there's nothing to clean up.

Let's look at the `fetch_page` next.

```
   fetch_page(url) 
    response = Gateway.get!(url)
    items = Poison.decode!(response.body)
    links = parse_links(response.headers["Link"])

    {items, links["next"]}
```

`fetch_page` is our "start function". We use the `HTTPoison`-based gateway previously shown to fetch the url provided. We parse the JSON of the body with `Poison` and then parse the `Link` header into a map of `link name => url`. The details of the link parsing aren't very important.

Finally, let's look at our "next\_function" `process_page`.

```
   process_page({, }) 
    {:halt, }
  

   process_page({, next_page_url}) 
    next_page_url
    |> fetch_page
    |> process_page
  

   process_page({items, next_page_url}) 
    {items, {, next_page_url}}
```

The `process_page` function has three clauses. The clause to be executed is determined by the tuple passed to the function. This is known as pattern matching. Each clause is expected to return a tuple where the first element contains a list of items to add to the stream and the second item is the value of the accumulator for the next call to `process_page`. We'll look at each clause individually.

```
   process_page({, }) 
    {:halt, }
```

In the first clause, we handle the case where there are no items and no next link. This means we've reached the last page and added all the items to the stream. We should stop paginating, so we return the special value `:halt` that tells `Stream.resource` our stream has ended.

```
   process_page({, next_page_url}) 
    next_page_url
    |> fetch_page
    |> process_page
```

The second clause is invoked in the case when we've consumed the items on a page and there is a non-nil next page link to follow. In this case, we fetch the next page and process it.

```
   process_page({items, next_page_url}) 
    {items, {, next_page_url}}
```

The third and final clause is the "normal" case because it is invoked when we have items to add to the stream. We return the items as the first element of the tuple, adding them to the stream. We then return the tuple `{nil, next_page_url}` as our accumulator, saying "I need more items and here's the next url to fetch".

Ok, we've looked at all the code required to paginate Github API responses! This example is a little more advanced than the others we've seen, but it is a remarkably small amount of code to provide invisible, lazy pagination of arbitrary responses from the Github API.

Finally, we'll use our `Github.ResultStream` module to expose a nice API to our users for fetching the repositories for an organization.

```
defmodule Github   
  alias Github.ResultStream

   repos(organization) 
    ResultStream.new("/orgs/#{organization}/repos")
```

We can use our new API to fetch the name of all the repositories for the `elixir-lang` organization.

```
"elixir-lang"
|> Github.repos
|> Stream.map( repo -> repo["full_name"] )
|> Enum.take()

# => ["elixir-lang/elixir"]
```

Remind yourself when reading this code that it is lazy, meaning we only consume the first page of results to get the first repository's name.

This enumerable-like API allows our users to do familiar things with the results. For example, we could build a stream of the names of all the repositories for both the `elixir-lang` and `tryghost` organizations using `Stream.flat_map`.

```
["elixir-lang", "tryghost"]
|> Stream.flat_map(&Github.repos/)
|> Stream.map( repo -> repo["full_name"] )
|> Enum.take()

# => ["elixir-lang/elixir"]
```

Again, this is lazy and efficient in that it only paginates of the results as we need them. That's pretty amazing.

#### Wrap Up

I hope this gives you a sense of the power and flexibility provided by Elixir's `Stream` facilities. Use them in your libraries!
