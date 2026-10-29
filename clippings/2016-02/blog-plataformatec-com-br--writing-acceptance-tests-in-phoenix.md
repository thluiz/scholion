---
url: "http://blog.plataformatec.com.br/2016/01/writing-acceptance-tests-in-phoenix/"
captured_at: "2016-02-07T22:54:30-03:00"
title: "Writing Acceptance tests in Phoenix"
domain: "blog-plataformatec-com-br"
---

# Writing Acceptance tests in Phoenix

Acceptance testing seems to be in its first steps in the Elixir ecosystem, but there are already some cool libs that can help us out to do it. I’m going to show you how we did it with [Hound](https://github.com/HashNuke/hound).

In this blog post, we’ll write a few acceptance tests for an expenses report listing page, where we’ll interact with the report and some form elements.

To make possible to interact with the elements on the page, we’ll need a web browser driver. Hound accepts `chrome_driver`, `firefox`, `phantomjs` and `selenium`. My choice is `phantomjs` because I want to use a headless browser (I don’t want the driver to open a browser during the execution of the test suite).

## Setup

First we’ll need to add Hound into our dependencies, so add the following line in your `mix.exs`:

```
{:hound, "~> 0.8"}
```

Make sure it’ll start during the test suite runtime. To do this we’ll need to add `Application.ensure_all_started(:hound)` before `ExUnit.start` in our test helper:

```
Application.ensure_all_started(:hound)
ExUnit.start
```

We’ll be using `phantomjs` as our web driver. [Make sure it’s properly installed and that you can start it](http://phantomjs.org/download.html) with `phantomjs --wd`. To configure it, add this to the `config.exs` file:

```
config :hound, driver: "phantomjs"
```

Take a look at [this doc from Hound resources](https://github.com/HashNuke/hound/blob/master/notes/configuring-hound.md) to check if you’d like different configs.

We’ll also need to set the server config in our `config/test.exs`to `true`.

```
config :my_app, MyApp.Endpoint,
  http: [port: ]
  server:
```

That should do it! Before writing our first test, let’s define an `IntegrationCase` module, similar to the `ModelCase` and `ConnCase` provided by Phoenix, which will include all functionality we need to write our integration tests. Create the `test/support/integration_case.ex` file and add the following content:

```
defmodule MyApp.IntegrationCase 
   ExUnit.CaseTemplate

  using 
    quote 
       Hound.Helpers

      import Ecto.Model
      import Ecto.Query, only: [from: ]
      import MyApp.Router.Helpers

      alias MyApp.Repo

      # The default endpoint for testing
      @endpoint MyApp.Endpoint

      hound_session
    
  

  setup tags 
    unless tags[:async] 
      Ecto.Adapters.SQL.restart_test_transaction(MyApp.Repo, [])
```

There are a few lines that are worth commenting:

- `use Hound.Helpers` will include the helpers necessary for us to interact with our interface ([take a look at the docs and explore them a little, they’ll be very helpful](http://hexdocs.pm/hound/readme.html));
- `hound_session` will make sure that Hound will start and closes its session during the test execution;
- `import MyApp.Router.Helpers` will include helpers so we can manipulate routes and URLs.

## Exercise

Let’s test!

We’re testing a simple list of expenses from a city (that example was extracted from an app we have been working on, but its scope was reduced so we can follow the steps more easily).

Take a look at its template code:

```
<>
  < form_for @, city_expense_path(@, :index, @city.id), [ , method: ],   > %>
    <>
      <label ="q_status">Status</label>
      <
        select , :status, [{"", ""}, {"Cancelled", "cancelled"}], prompt: "" %>
    </>

    <>
      <label ="q_supplier">Supplier</label>
      < text_input , :supplier %>
    </>

    < submit "Submit" %>
  <  %>
</>

<table>
  <thead>
    <>ID</>
    <>Status</>
    <>Supplier</>
    <>Value</>
    <>Date</>
  </thead>
  <tbody>
    <  expense < @expenses  %>
      <>
        <>< expense.id %></>
        <>< expense.status %></>
        <>< expense.supplier.name %></>
        <>< expense.value %></>
        <>< expense.date %></>
      </>
    <  %>
  </tbody>
</table>
```

We’ll need a new test file, let’s put it at `test/integration/expenses_list_test.exs`. To use Hound’s facilities, we’ll need to use the `IntegrationCase` module that we have previously created.

```
defmodule MyApp.ExpenseListTest 
   MyApp.IntegrationCase
```

We’ll be using three private functions to help us making assertions and interacting with elements in our test file. The first one, `expense_on_the_list`, will check if a given expense, that is represented by the Ecto model called `MyApp.Expense`, is in there. The second function is just a helper for getting the expenses list and the third will help us interact with a select input within a form.

```
defmodule MyApp.ExpenseListTest 
   MyApp.IntegrationCase

  

   expense_on_the_list(expense, list) 
    list
    |> visible_text
    |> String.contains?(expense.id)
  

   expense_list_items 
    find_element(, "tbody")
    |> find_all_within_element(, )
  

   select_status(form, status) 
    form
    |> find_within_element(, "q_status")
    |> input_into_field(status)
```

To interact with an element, you’ll always need to find the element on the page and for this, you need to know Hound’s [page helpers](http://hexdocs.pm/hound/Hound.Helpers.Page.html). I’ve noticed that we ended up using `find_element` and `find_all_within_element` most of the time to find the elements on the page or in a context (i.e inside a previously found element).

Since this test is about the City resource, we’ve created just this city and navigated to it directly on the setup, since this would be a requirement for all the tests in this file, and shared it with all the tests through the setup context.

```
setup 
  city = insert_city!(%{name: "Winterfell"})

  navigate_to("/cities/#{city.id}/expenses")

  {, city: city}
```

[Navigation](http://hexdocs.pm/hound/Hound.Helpers.Navigation.html#content) is another important Hound module. It will help us go through our app easily and get info about the page, like the `current_path()` function that returns the path we’re navigating on that moment.

Now that we’re on the page, we’ll be interacting with the form, by finding elements that are within it and filling or selecting values on them.

```
test "filter by supplier", %{city: city} 
  supplier = insert_supplier!(%{name: "Ned Stark"})
  supplier_b = insert_supplier!(%{name: "Bell Tower Management"})
  expense = insert_expense!(%{supplier: supplier, city: city, status: "paid"})
  insert_expense!(%{supplier: supplier_b, city: city, status: "paid"})

  search_form = find_element(, "form")
  search_form
  |> find_within_element(, "q_supplier")
  |> fill_field("Ned")

  submit_element(search_form)

  items = expense_list_items
  assert length(items) == 
  assert expense_on_the_list(expense, items)
```

The module responsible for these tasks is [Element](http://hexdocs.pm/hound/Hound.Helpers.Element.html). It has very useful functions, like `fill_field` we used above. All of its functions require an element.

In the previous example, the interactions with the form ended with `submit_element`, but if we need any other action on it after this, we would need to re-assign it (otherwise, we’ll get a `** (RuntimeError) Element does not exist in cache` error), like in the following example:

```
test "filter by statuses", %{city: city} 
  supplier = insert_supplier!(%{name: "Jon Snow"})

  cancelled_expense = insert_expense!(%{supplier: supplier, city: city, status: "cancelled"})
  paid_expense = insert_expense!(%{supplier: supplier, city: city, status: "paid"})

  search_form = find_element(, "form")
  select_status(search_form, "Cancelled")

  submit_element(search_form)

  items = expense_list_items
  assert length(items) == 
  assert expense_on_the_list(cancelled_expense, items)

  search_form = find_element(, "form")
  select_status(search_form, "Paid")
  submit_element(search_form)

  items = expense_list_items
  assert length(items) == 
  assert expense_on_the_list(paid_expense, items)
```

## Verify

### Runtime

One of the things I’ve paid a lot of attention during this experience was the test suite runtime. As expected, it can get slow with acceptance tests. The original app is still really tiny and before adding the acceptance tests, the runtime was:

```
Finished in 0.6 seconds (0.5s on load, 0.1s on tests)
23 tests, 0 failures, 2 skipped
```

After including two tests (but with more interactions than the ones presented), it was noticeable the test suite became slower. It tripled the runtime.

```
Finished in 1.8 seconds (0.5s on load, 1.2s on tests)
25 tests, 0 failures, 2 skipped
```

This effect is actually expected. We know that acceptance tests are expensive and that they should be a small portion of your [test pyramid](http://martinfowler.com/bliki/TestPyramid.html)

There are a few things that can make acceptance tests faster:

- Upcoming Ecto v2.0 will allow us to [run tests that use database persistence asyncronously](https://github.com/elixir-lang/ecto/pull/1198);
- In my experience Phantom.js considerably faster than the other options, I recommend you to go with it.

You will definitely need to write some acceptance tests, but give preference to controller tests in most scenarios and use acceptance tests for important flows of your app (take a look at the [user journey concept](https://www.techwell.com/2012/10/performing-effective-automated-acceptance-testing), that can give you some good insights).

## Web driver server execution

Currently, Hound doesn’t execute the browser automatically during tests. You’ll need to start it; otherwise, your tests will fail. There may be some workarounds to achieve it, if you’re on OS X, you can run [Phantomjs as a service](http://blog.animascodelabs.com/2015/12/31/running-phantomjs-ghostdriver-as-an-osx-service/).

## Teardown

I really enjoyed playing with Hound, and I found very simple to work with it. Also, I see it as a potential project if you’re considering contributing to an Open Source Project.

I hope this post was useful and gave you some ideas of how to write acceptance tests with Elixir and Phoenix. If you have any questions or suggestions, I’m all ears (or eyes).

*Which tool have you recently found to be useful when writing tests in Elixir?*

[![02729411279d02d2d8aead9c2f810d98.png](blog-plataformatec-com-br--writing-acceptance-tests-in-phoenix/02729411279d02d2d8aead9c2f810d98.png)](http://plataformatec.com.br/elixir-radar?utm_source=our-blog&utm_medium=referral&utm_campaign=elixir-radar&utm_content=elixir-radar-cta-blog-post-bottom)
