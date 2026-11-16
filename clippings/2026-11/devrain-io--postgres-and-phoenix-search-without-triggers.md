---
url: "https://devrain.io/ecto/phoenix/elixir/postgresql/2020/05/14/postgres-and-phoenix-search-without-triggers.html"
captured_at: "2026-11-16T03:00:01+00:00"
title: "Postgres & Phoenix Search Without Triggers"
domain: "devrain-io"
---

![Searching in a Maze](https://devrain.io/assets/images/searching-maze.jpg)

While integrating search in our Phoenix application, we ended up at a [lovely blog post](http://nathanmlong.com/2018/01/fast-fulltext-search-with-ecto-and-postgresql/) that explained how we could implement it for all our entities, without having to think about it for every update insert or delete.

Our first implementation of search looked pretty much as described there, we had materialized views per type that we wanted to conduct searches on. These materialized views are created by triggers in the database on every insert, update and delete of that entity. Next to the materialized views, we also created indexes to increase the search speed.

## Slow pages

Searches were fast but some pages turned out to be **slow**. This was because the materialized views were recreated by every trigger (create, update, delete) of one entity and building the materialized view could take up to 3 seconds. This happened despite that option `concurrently` has been set for refreshing the materialized views. Which is documented by PostgreSQL: “only one REFRESH at a time may run against any one [materialized view](https://www.postgresql.org/docs/12/interactive/sql-refreshmaterializedview.html)”

Since the triggers, and thus the refreshes, are happening in [the same transaction as the statement](https://www.postgresql.org/docs/9.6/plpgsql-structure.html), all create/update/delete actions on one table had to wait for each other. This could become very slow and batch operations also needed to ensure that the triggers were off before firing.

To improve performance we needed a way of asynchronously refreshing our views. This is a difficult task for PostgreSQL but for Elixir this fits like a glove. We removed the database triggers and replaced them with a GenServer. In the `MyApp.Repo` we have monkey patched all insert, update and delete functions. These functions are defined with a macro in the module and this can be bypassed by using the option `read_only: true` on `Ecto.Repo`

```
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
defmodule MyApp.Repo do
  use Ecto.Repo,
    otp_app: :my_app,
    adapter: Ecto.Adapters.Postgres,
    read_only: true

  ...

  # a monkey patch of `Repo.insert/2`
  def insert(struct, opts \\ []) do
    __MODULE__
    |> Ecto.Repo.Schema.insert(get_dynamic_repo(), struct, opts)
    |> perform_callback()
  end

  ...

end
```

With extending the insert and similar functions of Repo (update/2, delete/2 etc.) all actions will first be resolved and with the result it will call the async `perform_callback/1`.

```
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
defp perform_callback(result) do
  case result do
    # insert, update & delete
    {:ok, %module{}} ->
      Search.Interface.refresh_for(module)

    # insert_all & update_all
    {count, [%module{} | _]} when count > 0 ->
      Search.Interface.refresh_for(module)

    # insert!, update! and delete!
    %module{} ->
      Search.Interface.refresh_for(module)

    # do nothing
    _ ->
      nil
  end

  result
end
```

The function `perform_callback/1` will check on the type of the module that was changed in the database and will call the Search.Interface that looks like this:

```
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
defmodule MyApp.Search.Interface do
  ...

  def refresh_for(module) do
    module
    |> module_to_table()
    |> search_views_for_table()
    |> Enum.each(&refresh_later/1)
  end

  defp module_to_table(module) do
    with %{__meta__: meta} <- struct(module), %{source: table} <- meta, do: table
  end

  defp search_views_for_table("courses"), do: ~w(course_search)
  ...

  defp refresh_later(view_name), do: GenServer.cast(RefresherServer, {:refresh, view_name})
end
```

This is an interface for the GenServer, that is created for clarity with functions that can be called from the outside of the GenServer. It checks on the module that comes in and selects the materialized view that should be refreshed. The list returned by `search_views_for_table/1` can be extended so that other views can be refreshed. The function can be copied and altered so views of other modules will be updated as well. In the end, we cast to the GenServer in `refresh_later/1` with the view we want to refresh. The cast of the interface lets the view be added async to the RefresherServer shown here.

```
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
defmodule MyApp.Search.RefresherServer do
  @minimum_time_in_queue : 5_000
  @max_concurrency 5
  @valid_search_views ~w(course_search ...)
  defstruct queue: [], running: [], timer_ref: nil
  ...

  # Internal API
  defp cancel_running_timer_if_any(nil), do: nil
  defp cancel_running_timer_if_any(ref), do: Process.cancel_timer(ref)

  defp fill_progress_queue(%{queue: [view | remainder], running: progress_queue} = state)
       when length(progress_queue) < @max_concurrency do
    %Task{ref: task_ref} = Task.Supervisor.async_nolink(MyApp.TaskSupervisor, __MODULE__, :refresh_materialized_view, [view])

    fill_progress_queue(%{state | queue: remainder, running: [task_ref | progress_queue]})
  end


  defp fill_progress_queue(state), do: state

  def refresh_materialized_view(view_name) when view_name in @valid_search_views,
    do: Repo.query("REFRESH MATERIALIZED VIEW CONCURRENTLY #{view_name};", [], timeout: :infinity)
end
```

Aside from a `handle_cast/2` and the default GenServer setup, this is what our RefresherServer looks like. To hook this up, our handle\_cast takes the refresh message coming from the `refresh_later/1` in the Search.Interface. It will take the view that needs to be updated and checks if that view is in the queue and if not, it will add it.

```
0
1
2
3
4
def handle_cast({:refresh, view}, %{queue: queue} = state) do
  new_queue = if view in queue, do: queue, else: [view | queue]

  {:noreply, %{state | queue: new_queue}, {:continue, :set_timer}}
end
```

The `handle_cast/2` reply will make the GenServer continue by canceling the current timer and then setting the timer again. This ensures that we don’t refresh the materialized views for every update and allows us to give the database some time (`@minimum_time_in_queue 5_000`) to complete the refresh that is actually happening on the database.

```
0
1
2
3
4
5
6
def handle_continue(:set_timer, %{queue: [_ | _], timer_ref: ref} = state) do
  cancel_running_timer_if_any(ref)

  new_timer = Process.send_after(self(), :stage_refresh, @minimum_time_in_queue)

  {:noreply, %{state | timer_ref: new_timer}}
end
```

Finally a `handle_info/2` triggered by the timer will call `fill_progress_queue/1` and that triggers the refresh of our materialized view and returns the current state of the GenServer. For each query a task would spin to refresh the materialized view, once that task returns an `:ok` it will be removed from the queue.

```
0
1
2
3
4
5
6
7
8
9
10
def handle_info(:stage_refresh, state) do
  new_state = fill_progress_queue(state)

  {:noreply, %{new_state | timer_ref: nil}, {:continue, :set_timer}}
end

def handle_info({ref, {:ok, _}}, %{running: views} = state) do
  Process.demonitor(ref, [:flush])

  {:noreply, %{state | running: List.delete(views, ref)}}
end
```

With this implementation our database was freed of slow pages caused by refreshing the views too often.

It’s good to note that this solution will use database connections. Repo calls are done to update the refreshes of the materialized views, if the queue size (`@max_concurrency`) is larger than or equal to your amount of database connections it could still block other calls from within your application.

### Tests

To use this GenServer for searches in your tests, you should either skip the callbacks during the tests or lower the timeout duration. Without one of these two options, tests will become slow.

When testing the search, be aware that the search views are generated asynchronously and thus need to be waited on before they can be found.

## Searching with Typos

In the blog mentioned before, a trigram index was added but it wasn’t used. This meant that search queries with typos wouldn’t match while this is a great strength of the trigram searches. This can be solved by using the [similarity](https://www.postgresql.org/docs/12/pgtrgm.html#//apple_ref/cpp/Function/%2525) function of PostgreSQL. The `%` is an operator for the similarity function that uses the created index. It takes the similarity\_threshold which is 0.3 by default. A better explanation of using similarity search searching can be found in [Super Fuzzy Searching on PostgreSQL](http://www.www-old.bartlettpublishing.com/site/bartpub/blog/3/entry/350).

With that update our search queries now look like this:

```
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
  defmacro matching_courses_ids_and_ranks(search_string) do
    quote do
      fragment(
        """
        SELECT course_search.id AS id,
        ts_rank(
          course_search.document, plainto_tsquery(unaccent(?))
        ) AS rank
        FROM course_search
        WHERE course_search.document @@ plainto_tsquery(unaccent(?))
        OR course_search.title % ?
        """,
        ^unquote(search_string),
        ^unquote(search_string),
        ^unquote(search_string),
      )
    end
  end
```

## Did you mean …?

To search with suggestions, we’re saving the searches that are done. Whenever someone has done a search query while having a typo in it, we can check if the correct searches have been done before. In the following database query the keyword is used to look through the searches which has been searched for the most and also matches our threshold. The query is also making sure it is not the current search keyword of the user.

The resulting answer can be used to make a line below the input bar with: `Did you mean: <anser>`

```
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
Searches
|> join(
  :left_lateral,
  [s],
  exact in fragment(
    """
    SELECT keyword, count(*) as total
    FROM searches AS s
    WHERE keyword = ?
    GROUP BY keyword
    """,
    ^keyword
  )
)
|> where(
  [s],
  fragment("? % ? and similarity(?, ?) > 0.5", s.keyword, ^keyword, s.keyword, ^keyword)
)
|> group_by([s, exact], [s.keyword, exact.total])
|> order_by([s], fragment("? <-> ?", s.keyword, ^keyword))
|> select([s, exact], %{keyword: s.keyword})
|> having(
  [s, exact],
  count(s.keyword) >= @suggestion_threshold and coalesce(exact.total, 0) < count(s.keyword)
)
|> limit(1)
|> Repo.one()
```

The same table can also be used for the typeahead. The following query is used to get suggestions based on the keyword that the user is typing. It takes the keyword and checks if it can be completed into anything that has been searched for before. It will check if the suggestions have been searched more than the threshold and returns a limited number of suggetions while the user is typing.

```
0
1
2
3
4
5
6
7
Searches
|> where([s], ilike(s.keyword, ^"#{keyword}%"))
|> group_by([s], s.keyword)
|> order_by([s], desc: count(s.keyword))
|> having([s], count(s.keyword) >= @typeahead_suggestion_threshold)
|> limit(@typeahead_suggestions)
|> select([s], %{keyword: s.keyword, id: s.keyword})
|> Repo.all()
```
