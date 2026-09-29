---
url: "https://www.welcometothejungle.com/fr/articles/tips-test-driven-development"
captured_at: "2020-07-11T21:38:32-03:00"
title: "4 tips for mastering test-driven development"
domain: "welcometothejungle-com"
---

# 4 Tips for Mastering Test-Driven Development

[![collection_coder_stories.jpg](welcometothejungle-com--4-tips-for-mastering-test-driven-development/7aa3530644715cdec9c623df37737c9a.jpg)](https://www.welcometothejungle.com/fr/collections/behind-the-code/coder-stories "Coder stories")

Need some guidance for the best way to carry out test-driven development (TDD)? Read on. Here, we share some useful tips, such as how to isolate your code to simplify unit testing. We’ll also look at an important aspect that doesn’t often get tested—database-migration rollback—as well as how code coverage could prevent you from omitting testing some important parts of your code. Finally, there’s a helpful overview of property-based testing—a new way of writing tests that’s a great complement to unit testing.

*Note that we will not be covering other types of tests, such as end-to-end or functional, or other xDD techniques (such as behavior DD, domain DD, or Postman DD).*

## The basics of TDD

Let’s begin with a little reminder: What is a unit test? Well, these enable you to test small chunks of code (a module, a class, a function), check some inputs versus expected output (examples), and quickly discover regressions, as well as serve as documentation.

The most natural procedure to follow when developing a feature is to code it and then add unit tests. TDD is an unnatural way of writing unit tests. It consists of **short development cycles**, for which tests are written to meet a given requirement prior to writing the actual code. Then we iterate over the other requirements.

The steps are as follows:

1. Write a unit test to meet a requirement.
2. Check that your test fails.
3. Write the code.
4. Check that your test succeeds.

…and then you iterate until you have met all the requirements.

### The advantages

There are several advantages to processing in this way. Firstly, **you don’t end up writing more code than you actually need**. When writing code first, you often tend to start with a complex architecture that doesn’t fit the actual needs.

In addition, **you won’t forget any requirement** as you iterate over them, and you can be confident that **code refactoring will not break anything**. You’ll also find that, as the different parts of your code are loosely coupled, they offer clean interfaces by design, and finally, that your productivity is increased.

Your reaction to that last statement might be one of skepticism, but after several years of implementing TDD, we’re convinced that we would have spent more time debugging an issue in production than writing one more unit test during the initial development phase.

### The trade-offs

There are also several trade-offs with TDD that you should be aware of. For a start, **the number of lines of code you get can quickly grow**, leading to you end up with more lines for TDD than your actual code. Therefore, choose your examples carefully and refactor your tests (yeah, sorry, tests need to be refactored, too).

Also, tests might end up being **hard to maintain**, so make them as small as possible and add comments around the more important parts, pay attention to race conditions and tests that randomly fail, and clean resources that were created during tests to avoid any interference between the tests.

Finally, introducing tests means **a longer continuous integration and delivery process**. If they end up taking too long to execute, consider taking some time to fix this (through refactoring or deleting less-relevant tests, for example).

That’s it for the basics. As mentioned, we’re not going to explore all TDD steps in-depth, as there are already plenty of articles out there on how to do it efficiently. Instead, we’re going to share with you 4 tips you should know about when you adopt TDD. Although all examples are given in Elixir, you can easily adapt the concepts to any programming language.

## 1. Deal with the outside world

Often, you find yourself wanting to unit test a piece of code that makes calls to external modules/functions and you don’t want later ones to interfere with your tests.

Let’s take the example of a job controller, where a message is automatically posted on a Slack channel upon successful creation:

```
# job_controller.ex

defmodule WttjWeb.JobController do
  use WttjWeb, :controller
  alias Wttj.{Repo, Job}

  def create(conn, params) do
    changeset = Job.changeset(%Job{}, params)
    case Repo.insert(changeset) do
      {:ok, job} ->
        Slack.send("#jobs", "new job posted: #{job.title}")
        conn
        |> put_status(:created)
        |> render("job.json", job: job)
      {:error, _changeset} ->
        send_resp(conn, :unprocessable_entity, "")
    end
  end
```

```
# slack.ex

defmodule Slack do
  use Tesla

  plug Tesla.Middleware.BaseUrl, Application.get_env(:wttj, :slack)[:base_url]
  plug Tesla.Middleware.JSON

  def send(channel, message) do
    post!("/", %{"channel" => channel, "username" => "WTTJ bot", "text" => message})
  end

end
```

Here is a unit test for the job controller:

```
defmodule WttjWeb.JobControllerTest do
  use WttjWeb.ConnCase

  setup %{conn: conn} do
    {:ok, conn: put_req_header(conn, "accept", "application/json")}
  end

  test "POST /", %{conn: conn} do
    attrs = %{"title" => "Backend Engineer",
              "description" => "Full-time, based in Paris",
              "status" => "published"}
    conn = post(conn, Routes.job_path(conn, :create), attrs)
    assert json_response(conn, 201)
  end
end
```

When you’re writing unit tests for the job controller, you don’t actually want to post a message on Slack every time the test is run. Our Slack module must be tested independently.

We’ve put a bang in the Slack module to make it crash on purpose when running the job controller test.

```
$ mix test test/wttj_web/controllers/job_controller_test.exs

  1) test POST / (WttjWeb.JobControllerTest)
     test/wttj_web/controllers/job_controller_test.exs:13
     ** (Tesla.Error) :econnrefused (POST /)
     code: conn = post(conn, Routes.job_path(conn, :create), attrs)
     stacktrace:
       (tesla) lib/tesla.ex:300: Tesla.execute!/3
       (wttj) lib/wttj_web/controllers/job_controller.ex:23: WttjWeb.JobController.create/2
       (wttj) lib/wttj_web/controllers/job_controller.ex:1: WttjWeb.JobController.action/2
       (wttj) lib/wttj_web/controllers/job_controller.ex:1: WttjWeb.JobController.phoenix_controller_pipeline/2
       (wttj) lib/wttj_web/endpoint.ex:1: WttjWeb.Endpoint.instrument/4
       (phoenix) lib/phoenix/router.ex:275: Phoenix.Router.__call__/1
       (wttj) lib/wttj_web/endpoint.ex:1: WttjWeb.Endpoint.plug_builder_call/2
       (wttj) lib/wttj_web/endpoint.ex:1: WttjWeb.Endpoint.call/2
       (phoenix) lib/phoenix/test/conn_test.ex:235: Phoenix.ConnTest.dispatch/5
       test/wttj_web/controllers/job_controller_test.exs:17: (test)

Finished in 0.1 seconds
1 test, 1 failure

Randomized with seed 522928
```

**You can therefore see that an error that occurs outside the module being tested makes the test fail. This is why it’s very important to isolate your module.**

To perform this isolation, you must introduce a test double, which [Martin Fowler](https://martinfowler.com/bliki/TestDouble.html) defines as a *“generic term for any case where you replace a production object for testing purposes”*. The main types as dummy, fake, stubs, spies, and mocks.

For our example we will be focusing on using a stub, also called a *“mock as a noun”* by [José Valim](http://blog.plataformatec.com.br/2015/10/mocks-and-explicit-contracts/).

A stub is an alternate implementation of a given functionality; its code differs from the one used in production and provides a canned response.

In our case we will use a different implementation of the Slack module, depending on the environment.

The easiest way to do this is to set the module to be used according to the Mix environment (dev, test, prod, and so on).

```
# prod.exs

config :wttj, :slack,
  module: Slack,
  base_url: "https://hooks.slack.com/services/foobar"
```

```
# test.exs

config :wttj, :slack,
  module: SlackStub,
  base_url: "http://localhost"
```

By doing this, the Slack module will be used in production and SlackStub in tests.  
The stub module does nothing, it merely returns`:ok`.

On introducing a new module named SlackService, which acts as a router to the relevant module, the new code looks like this:

```
# slack.ex

defmodule Slack do
  use Tesla

  plug Tesla.Middleware.BaseUrl, Application.get_env(:wttj, :slack)[:base_url]
  plug Tesla.Middleware.JSON

  def send(channel, message) do
    post!("/", %{"channel" => channel, "username" => "WTTJ bot", "text" => message})
  end

end

defmodule SlackStub do
  def send(_channel, _message) do
    :ok
  end
end

defmodule SlackService do

  @slack_module Application.get_env(:wttj, :slack)[:module]

  def send(channel, message) do
    @slack_module.send(channel, message)
  end
end
```

In the job controller, we now make a call to SlackService instead of Slack.

```
# job_controller.ex

defmodule WttjWeb.JobController do
  use WttjWeb, :controller
  alias Wttj.{Repo, Job}

  def create(conn, params) do
    changeset = Job.changeset(%Job{}, params)
    case Repo.insert(changeset) do
      {:ok, job} ->
        SlackService.send("#jobs", "new job posted: #{job.title}")
        conn
        |> put_status(:created)
        |> render("job.json", job: job)
      {:error, _changeset} ->
        send_resp(conn, :unprocessable_entity, "")
    end
  end
```

By doing this, the job controller module is completely isolated and can be tested with confidence.

```
$ mix test test/wttj_web/controllers/job_controller_test.exs
.
Finished in 0.06 seconds
1 test, 0 failures
Randomized with seed 492140
```

But what about testing the Slack module itself?

We could adopt the same strategy and create a stub for the Tesla module, which wouldn’t actually perform HTTP calls but merely return fake HTTP responses. However, your test would be too constricted by the HTTP client library you chose, in this case Tesla. **But a well-written test should not change if you decide you want to switch to another HTTP client library than the one originally chosen.**

By using a bypass library, we are able to start a dummy web server on a free port, which will, in our case, act as the Slack server. Next, remove the bang in the Slack module so that errors are handled nicely:

```
# slack.ex

defmodule Slack do
  use Tesla

  plug Tesla.Middleware.BaseUrl, Application.get_env(:wttj, :slack)[:base_url]
  plug Tesla.Middleware.JSON

  def send(channel, message) do
    case post("/", %{"channel" => channel, "username" => "WTTJ bot", "text" => message}) do
      {:ok, %Tesla.Env{status: status}} when status in 200..299 ->
        :ok
      _ ->
        :error
    end
  end

end
```

As you can see, the remote url is stored in a configuration. During tests, we will dynamically set the relevant value according to the port the bypass is listening to, which means we will then be able to simulate Slack-server behaviors, such as nominal case, connectivity error, and bad requests. Very convenient!

The test looks like this. Notice there’s no reference to Tesla at all!

```
# slack_test.exs

defmodule SlackTest do
  use ExUnit.Case, async: true

  setup do
    bypass = Bypass.open
    config = Application.get_env(:wttj, :slack)
    |> Keyword.merge([base_url: "http://localhost:#{bypass.port}"])
    Application.put_env(:wttj, :slack, config)
    {:ok, bypass: bypass}
  end

  test "nominal case", %{bypass: bypass} do
    Bypass.expect bypass, "POST", "/", fn conn ->
      Plug.Conn.resp(conn, 200, "")
    end
    assert Slack.send("my_channel", "hello world") == :ok
  end

  test "server downtime", %{bypass: bypass} do
    Bypass.expect bypass, "POST", "/", fn conn ->
      Plug.Conn.resp(conn, 200, "")
    end
    Bypass.down(bypass)
    assert Slack.send("my_channel", "hello world") == :error
    Bypass.up(bypass)
    assert Slack.send("my_channel", "hello world") == :ok
  end

  test "bad request", %{bypass: bypass} do
    Bypass.expect_once bypass, "POST", "/", fn conn ->
      Plug.Conn.resp(conn, 400, "")
    end
    assert Slack.send("a_non_existing_channel", "hello world") == :error
  end
end
```

There are other types of test doubles (mock, fake) that are not covered here, but it’s worth having a look at them if you don’t already know them. The main thing to keep in mind is that you have to keep your modules as small as possible and organize your code to facilitate module isolation and, thus, unit testing. Sometimes, writing tests and thinking about module isolation can even help you refactor and architecture your code properly.

## 2. Test database-migration rollback

Here, we’re going to tackle a topic rarely covered by unit tests in all the projects we’ve seen so far: The unit testing of database-migration files, especially the rollback process.

Many frameworks offer the possibility of creating database-migration files to keep track of the database-schema history, migrate to the last step, or rollback to a previous step in the history.

Unit tests always match the last schema, and migration files are implicitly tested the first time you run your migration file in a development environment, yet there is often no test for the rollback process.

When creating an Ecto migration file, the default callback to implement is `change/0`, which should contain automatically reversible migrations.

```
# 20190318203551_create_jobs.exs

defmodule Wttj.Repo.Migrations.CreateJobs do
  use Ecto.Migration

  def change do
    create table(:jobs) do
      add :title, :string
      add :description, :string
      add :slug, :string
      add :status, :string

      timestamps()
    end

  end
end
```

We can check that the above migration can be reversed without any error, but bear in mind that **not all migrations are automatically reversible**!

```
$ mix ecto.migrate -n 1
[info] == Running 20190318203551 Wttj.Repo.Migrations.CreateJobs.change/0 forward
[info] create table jobs
[info] == Migrated 20190318203551 in 0.0s

$ mix ecto.rollback
[info] == Running 20190318203551 Wttj.Repo.Migrations.CreateJobs.change/0 backward
[info] drop table jobs
[info] == Migrated 20190318203551 in 0.0s
```

A good example of this is deleting a column. Let’s add a migration file to delete the slug column in the jobs table:

```
# wttj/priv/repo/migrations/20190318203905_remove_job_slug.exs

defmodule Wttj.Repo.Migrations.RemoveJobSlug do
  use Ecto.Migration

  def change do
    alter table(:jobs) do
      remove :slug
    end
  end
end
```

In this case, the rollback will fail:

```
$ mix ecto.migrate -n 1
[info] == Running 20190318203905 Wttj.Repo.Migrations.RemoveJobSlug.change/0 forward
[info] alter table jobs
[info] == Migrated 20190318203905 in 0.0s

$ mix ecto.rollback
[info] == Running 20190318203905 Wttj.Repo.Migrations.RemoveJobSlug.change/0 backward
** (Ecto.MigrationError) cannot reverse migration command: alter table jobs. You will need to explicitly define up/0 and down/0 in your migration
    (ecto_sql) lib/ecto/migration/runner.ex:206: Ecto.Migration.Runner.execute_in_direction/4
    (ecto_sql) lib/ecto/migration/runner.ex:110: anonymous fn/2 in Ecto.Migration.Runner.flush/0
    (elixir) lib/enum.ex:1925: Enum."-reduce/3-lists^foldl/2-0-"/3
    (ecto_sql) lib/ecto/migration/runner.ex:108: Ecto.Migration.Runner.flush/0
    (stdlib) timer.erl:166: :timer.tc/1
    (ecto_sql) lib/ecto/migration/runner.ex:26: Ecto.Migration.Runner.run/7
    (ecto_sql) lib/ecto/migrator.ex:211: Ecto.Migrator.attempt/7
    (ecto_sql) lib/ecto/migrator.ex:149: anonymous fn/4 in Ecto.Migrator.do_down/4
    (ecto_sql) lib/ecto/migrator.ex:193: anonymous fn/3 in Ecto.Migrator.run_maybe_in_transaction/5
    (ecto_sql) lib/ecto/adapters/sql.ex:820: anonymous fn/3 in Ecto.Adapters.SQL.checkout_or_transaction/4
    (db_connection) lib/db_connection.ex:1355: DBConnection.run_transaction/4
    (ecto_sql) lib/ecto/migrator.ex:192: Ecto.Migrator.run_maybe_in_transaction/5
    (elixir) lib/task/supervised.ex:89: Task.Supervised.do_apply/2
    (elixir) lib/task/supervised.ex:38: Task.Supervised.reply/5
    (stdlib) proc_lib.erl:247: :proc_lib.init_p_do_apply/3
```

Occasionally, you might have to rollback a deployment in production after having found a regression, and thus have to rollback all Ecto migrations included in your release. In the above case, you would have to manually perform the necessary SQL commands to rollback your database to the previous step. Too bad!

To explicitly define a rollback behavior, you will need to implement both `up/0` and `down/0` callbacks instead of the `change/0` one:

```
# wttj/priv/repo/migrations/20190318203905_remove_job_slug.exs

defmodule Foo.Repo.Migrations.DeleteBlogPostsViews do
  use Ecto.Migration

  def up do
    alter table(:jobs) do
      remove :slug
    end
  end

  def down do
    alter table(:jobs) do
      add :slug, :string
    end
  end

end
```

Now the rollback will work.

```
$ mix ecto.reset
The database for Wttj.Repo has been dropped
The database for Wttj.Repo has been created
[info] == Running 20190318203551 Wttj.Repo.Migrations.CreateJobs.change/0 forward
[info] create table jobs
[info] == Migrated 20190318203551 in 0.0s
[info] == Running 20190318203905 Wttj.Repo.Migrations.RemoveJobSlug.up/0 forward
[info] alter table jobs
[info] == Migrated 20190318203905 in 0.0s

$ mix ecto.rollback
[info] == Running 20190318203905 Wttj.Repo.Migrations.RemoveJobSlug.down/0 forward
[info] alter table jobs
[info] == Migrated 20190318203905 in 0.0s
```

To anticipate such problems, we recommend adding a simple unit test to check that it’s possible to rollback all your migrations files.

```
# ecto_rollback_test.exs

defmodule EctoRollbackTest do
  use ExUnit.Case, async: true

  setup_all do
    on_exit fn -> Mix.Shell.IO.cmd("MIX_ENV=test mix ecto.migrate") end
    :ok
  end

  test "test migrations are rollbackable (exit status = 0)" do
    assert 0 == Mix.Shell.IO.cmd("MIX_ENV=test mix ecto.rollback --all")
  end

end
```

One might ask why use `ecto.rollback` when you can merely take a snapshot of your database before each upgrade and use it in case you need to rollback? **Although this method appears to be more straightforward and safe, you must bear in mind that the database write operations which occurred between the upgrade and the rollback will be lost.** It’s a matter of choice—we personally prefer not losing any data and so use ecto.rollback instead.

## 3. Use code coverage to test all the relevant parts of your code base

Code coverage is a way to measure the number of lines of code that have been executed while running all your unit tests. It is mainly used to highlight parts of the code that should be but are not tested.  
Including a test-coverage tool in your project is a must-do, no matter what programming language you’re using.

**You must keep in mind that having 100% code coverage doesn’t mean your code is bug-free!**

By looking at the code-coverage reports, you are able to pay attention to the sensitive parts of the code that get missed by unit tests. Testing every single line is a waste of time and you may find yourself with a huge amount of unit tests that can be hard to maintain. If you’re using Elixir, we recommend the [excoveralls library](https://hex.pm/packages/excoveralls), which generates friendly HTML reports stored locally or on the coveralls website.

To generate the report, simply run `mix coveralls.html`:

```
$ mix coveralls.html
........

Finished in 1.4 seconds
8 tests, 0 failures

Randomized with seed 10360
----------------
COV    FILE                                        LINES RELEVANT   MISSED
  0.0% lib/wttj.ex                                     9        0        0
 75.0% lib/wttj/application.ex                        31        4        1
100.0% lib/wttj/job.ex                                21        2        0
  0.0% lib/wttj/repo.ex                                5        0        0
100.0% lib/wttj/slack.ex                              31        2        0
  0.0% lib/wttj_web.ex                                69        1        1
  0.0% lib/wttj_web/channels/user_socket.ex           33        0        0
 21.1% lib/wttj_web/controllers/job_controller.ex     52       19       15
100.0% lib/wttj_web/controllers/page_controller.ex     7        1        0
  0.0% lib/wttj_web/endpoint.ex                       46        0        0
  0.0% lib/wttj_web/gettext.ex                        24        0        0
100.0% lib/wttj_web/router.ex                         27        3        0
  0.0% lib/wttj_web/views/error_helpers.ex            44        5        5
100.0% lib/wttj_web/views/error_view.ex               16        1        0
 50.0% lib/wttj_web/views/job_view.ex                 11        2        1
  0.0% lib/wttj_web/views/layout_view.ex               3        0        0
  0.0% lib/wttj_web/views/page_view.ex                 3        0        0
  0.0% test/support/channel_case.ex                   37        4        4
100.0% test/support/conn_case.ex                      38        4        0
  0.0% test/support/data_case.ex                      53        7        7
[TOTAL]  38.2%
----------------
Generating report...
```

15 lines missed in job\_controller.ex—shame on us!

Next, in your browser, open the file `cover/excoveralls.html`. This will show you, file by file, which lines are covered by unit tests (green) and which ones are not (red).

## 4. Write code that writes tests with property-based testing

The way we write unit tests is not perfect, and doesn’t necessarily cover all possible inputs your code could receive in real life.

We can test nominal cases, some edge cases we have thought of, but we always end up with a set of unit tests that has a finite set of inputs with their expected output. Unfortunately, some inputs you’ve not tested could lead to a bug and, if you’re unlucky, you’ll only see it when your code is in production.

The purpose of property-based testing is to **automatically generate a wide range of possible inputs for your piece of code and thus detect bugs as soon as possible**. To do this, you have to define the *properties* of the input your function expects. Input generators can then be set up according to these properties.

The notion of property-based testing was born in 1999, with the release of the Haskell library [QuickCheck](https://www.cs.tufts.edu/~nr/cs257/archive/john-hughes/quick.pdf). Since then, the library has been ported in many languages, including Elixir.

We’re going to use the [stream\_data library](https://github.com/whatyouhide/stream_data) presented by [Andrea Leopardi](https://www.youtube.com/watch?v=p84DMv8TQuo) at ElixirConf EU 2018. It’s not included in Elixir yet, but there’s a high chance it will be in the near future.

So here’s a light-hearted example of property-based testing: Let’s say you’re asked to write the function Wttj.Math.sum/2 that returns the sum of 2 integers. Following good practices of TDD, you start writing the tests (nominal case, negative numbers, commutativity):

```
# math_test.exs

defmodule MathTest do
  use ExUnit.Case, async: true

  test "sum" do
    assert Wttj.Math.sum(0, 1) == 1
    assert Wttj.Math.sum(-3, 4) == 1
    assert Wttj.Math.sum(2, 5) == 7
    assert Wttj.Math.sum(5, 2) == 7
  end
end
```

Then you write the function itself:

```
# math.ex

defmodule Wttj.Math do

  def sum(x, y) do
    x + y
  end
end
```

Your test passes, everything is OK.

```
$ mix test test/wttj/math_test.exs
.
Finished in 0.01 seconds
1 test, 0 failures
```

Then life goes on, the code evolves and then, one day, someone introduces a bug:

```
# math.ex

defmodule Wttj.Math do

  def sum(x, y) do
    if y == 42, do: raise "oops!"
    x + y
  end
end
```

Unfortunately, the test you wrote still passes!

Property-based testing to the rescue! In the same test module, we’re going to add a property-based test, starting with the keyword *property* (an Elixir macro). Instead of writing examples, we’re going to write some code that generates random examples, so there’s no hard-coded integer value:

```
# math_pb_test.exs

defmodule MathPBTest do
  use ExUnit.Case, async: true
  use ExUnitProperties

  test "sum" do
    assert Wttj.Math.sum(0, 1) == 1
    assert Wttj.Math.sum(-3, 4) == 1
    assert Wttj.Math.sum(2, 5) == 7
    assert Wttj.Math.sum(5, 2) == 7
  end

  property "sum" do
    check all x <- integer(),
              y <- integer() do
      assert x + y == Wttj.Math.sum(x,y)
    end
  end
end
```

You can see that the property and unit test have an equivalent number of lines of code.

Here, we’ve defined the properties of our function as x and y integers. You should read the code like this: In the property-based test *sum*, check that for all combinations of randomly generated integers x and y, assert that the function output equals to x+y.

When you run the test file, you will be able to see in the output that one test and one property have been run. This time, the bug is found by the property, which shows that the assertion failed while choosing x=0 and y=42 as input. Nice!

```
$ mix test test/wttj/math_pb_test.exs

  1) property sum (MathPBTest)
     test/wttj/math_pb_test.exs:5
     ** (ExUnitProperties.Error) failed with generated values (after 86 successful runs):

         * Clause:    x <- integer()
           Generated: 0

         * Clause:    y <- integer()
           Generated: 42

     got exception:

         ** (RuntimeError) oops!
     code: check all x <- integer(),
     stacktrace:
       (wttj) lib/wttj/math.ex:4: Wttj.Math.sum/2
       test/wttj/math_pb_test.exs:8: anonymous fn/3 in MathPBTest."property sum"/1
       (stream_data) lib/stream_data.ex:2114: StreamData.shrink_failure/6
       (stream_data) lib/stream_data.ex:2078: StreamData.check_all/7
       test/wttj/math_pb_test.exs:6: (test)

Finished in 0.04 seconds
1 property, 1 test, 1 failure
```

You can also see that, prior to that, the function has been successfully run with 86 random inputs. By default, stream\_data generates 100 inputs. Therefore, your test may not detect the bug every time it is run.  
This value is configurable—for example, you can set a higher example using your CI/CD tool. You want your tests to run fast on your laptop but let your CI/CD tool take its time testing a wider range of inputs.

```
config :stream_data,
  max_runs: if System.get_env("CI"), do: 1_000, else: 100
```

This way, a bug that’s not necessarily detected on your laptop has a higher chance of being detected by your CI/CD tool—better late than never!

The stream\_data library is made up of 2 main modules: StreamData and ExUnitProperties. StreamData holds the building blocks (integer(), list(), binary(), tuple()) to help you create your own input generators, whereas ExUnitProperties holds the implementation of all useful macros: *property*, *gen*, *check*, and so on. We would encourage you to have a look at the documentation and some useful talks that can be found on YouTube, such as this one from the [Indianapolis Elixir Users Group](https://www.youtube.com/watch?v=VhW9D0mbW1o).

Property-based tests must not be seen as an alternate way of testing. Unit tests are still good, especially in the first development stages, and are easier to write. But once everything has settled down, it’s worth making the effort to write property-based tests to battle-proof your code base.

In this article, we wanted to share our experience of unit testing and TDD, as well as some useful tips (module isolation, database-migration rollbacks) and good practices (code coverage).

Although all the examples were in Elixir, you will face the same issues whatever your favorite programming language is, and you’ll find similar libraries to help you on your way.

Due to its tests-first nature, TDD is still underused. Yet, from our own experience, **it helps you to focus just on what your code needs to do**. It also helps when refactoring and makes your code tend to fall into the most relevant design pattern. That’s why we think any developer should embrace this methodology.

Property-based testing is even less widespread. We’re relatively new to it and are looking forward to adding more of this to our future projects. We hope we’ve at least raised your curiosity…

*This article is part of Behind the Code, the media for developers, by developers. Discover more articles and videos by visiting [Behind the Code](https://www.welcometothejungle.com/collections/behind-the-code)!*

*Want to contribute? [Get published!](https://docs.google.com/forms/d/e/1FAIpQLSeelH8Eh0HohNrrDWnmKJGBRsFijXfMsMw1fPxOSGdMVypCyg/viewform?usp=sf_link)*

*Follow us on [Twitter](https://twitter.com/behind_thecode) to stay tuned!*

*Illustration by [Blok](https://fr.creasenso.com/portfolio/blok)*
