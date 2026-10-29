---
url: "http://codeloveandboards.com/blog/2016/03/20/supervising-multiple-genserver-processes/?utm_campaign=elixir_radar_45&utm_medium=email&utm_source=RD+Station"
captured_at: "2016-04-17T17:11:26-03:00"
title: "Supervising multiple GenServer processes - Code, Love & Boards"
domain: "codeloveandboards-com"
---

# Supervising multiple GenServer processes

Special thanks to Daniel Grieve ([@cazzrin](https://twitter.com/cazzrin)) for helping me understand supervised processes and for sharing his [Stranger](https://github.com/cazrin/stranger) project which has been an awesome source of inspiration for this refactoring.

In [part 10](http://codeloveandboards.com/blog/2016/02/15/trello-tribute-with-phoenix-and-react-pt-10/ "Tracking connected board members") of the **Trello tribute/clone series** we talked about creating a [GenServer](http://elixir-lang.org/docs/stable/elixir/GenServer.html "Elixir GenServer documentation") processes to keep track of the current connected board members. The state of this process, `PhoenixTrello.BoardChannel.Monitor`, consists of a map which stores a list of user ids indexed by the board is:

```
%{
   => [, , ],
   => [, ]
}
```

This was a good starting point for our goal, but while working on the project I realized that there was an important drawback. If, for any reason, the process dies or it's restarted by the application's supervision tree, it will lose the current state and the application will not be able to display which board members are connected or not.

In our particular case it's not really crucial because it doesn't break any functionality of the application. But imagine for a moment that it's storing important information for multiple different entities... if the process happens to restart due to an error regarding just one entity, the other are also going to be affected. How can we solve this?

## The solution

Instead of having just one process with the state for all boards with connected members, lets create multiple process, one for each board with their connected users, and also a **supervisor** process that will be in charge of starting this process and restarting the one that breaks so the others won't lose their current state.

### The Supervisor

If we take a look the official [Elixir documentation](http://elixir-lang.org/docs/stable/elixir/Supervisor.html "Elixir Supervisor documentation") we can read the following:

> A supervisor is a process which supervises other processes, called child processes.
>
> A supervisor implemented using this module will have a standard set of interface functions and include functionality for tracing and error reporting. It will also fit into a supervision tree.

So lets start by creating the new **module-based** `Supervisor`:

```
# lib/phoenix_trello/board_channel/supervisor.ex

defmodule PhoenixTrello.BoardChannel.Supervisor 
  use Supervisor

   start_link 
    Supervisor.start_link(__MODULE_, , name: __MODULE_)
  

   
    children = [
      worker(PhoenixTrello.BoardChannel.Monitor, [], restart: :transient)
    ]

    supervise(children, strategy: :simple_one_for_one)
```

This module will supervise `PhoenixTrello.BoardChannel.Monitor` processes. The `restart: transient` option determines that the children processes will be restarted just if they terminate **abnormally**, which is perfect for our case. We are also using the `strategy: :simple_one_for_one` which will make the supervisor restart only the child process that breaks.

### The BoardChannel Monitor

Now that we have the new `Supervisor` lets refactor the existing `PhoenixTrello.BoardChannel.Monitor` so:

1. There can exist multiple processes of it.
2. We can use a dynamic name to identify them.
3. Every new process is started by the `Supervisor`.

```
defmodule PhoenixTrello.BoardChannel.Monitor 
  # lib/phoenix_trello/board_channel/monitor.ex

  use GenServer

   create(board_id) 
     GenServer.whereis(ref(board_id)) 
       ->
        Supervisor.start_child(PhoenixTrello.BoardChannel.Supervisor, [board_id])
      _board ->
        {:error, :board_already_exists}
    
  

   start_link(board_id) 
    GenServer.start_link(__MODULE_, [], name: ref(board_id))
  

  

  defp ref(board_id) 
    {:global, {:board, board_id}}
```

To understand this better, lets start from the bottom. The private `ref` function will receive a `board_id` and will return a tuple that will be used to identify the process **globally** so we can access it eventually to modify and retrieve its list of user ids. The `start_link` function now receives the `board_id` and uses the `ref` function to start with a **dynamic** name. In the `create` function is where the `Supervisor` comes into play. It receives the `board_id` and checks if there is a process running with the name resulting of the `ref` function. When no process is found it will use `Supervisor.start_child` function specifying the **supervisor** we want to use, in our case our new `BoardChannel.Supervisor`, and it will pass the `board_id` to it making the **supervisor** call the previously commented `start_link` function. In case there is already a process with the same name it returns an error tuple so we can handle it wherever we want.

The next step is to update the existing functions so they are called in the correct process identified by the `board_id` param:

```
defmodule PhoenixTrello.BoardChannel.Monitor 
  # lib/phoenix_trello/board_channel/monitor.ex

  

   user_joined(board_id, user) 
   try_call board_id, {:user_joined, user}
  

   users_in_board(board_id) 
   try_call board_id, {:users_in_board}
  

   user_left(board_id, user) 
    try_call board_id, {:user_left, user}
  

  #####
  # GenServer implementation

   handle_call({:user_joined, user}, _from, users) 
    users = [user] ++ users
      |> Enum.uniq

    {:reply, users, users}
  

   handle_call({:users_in_board}, _from, users) 
    { :reply, users, users }
  

   handle_call({:user_left, user}, _from, users) 
    users = List.delete(users, user)
    {:reply, users, users}
  

  defp ref(board_id) 
    {:global, {:board, board_id}}
  

  defp try_call(board_id, message) 
     GenServer.whereis(ref(board_id)) 
       ->
        {:error, :invalid_board}
      board ->
        GenServer.call(board, message)
```

The implementation is almost the same but instead of using the `__MODULE__` to tell which process we want to use to handle the calls, we are going to use the private function `try_call` that will first look for the process identified using the `board_id` and make the call on it. Also note that the state is now a list instead of a map.

### Updating the application

We also need to change the application supervision tree by removing the `worker` with the old `Monitor` and adding the new `Supervisor`:

```
# /lib/phoenix_trello.ex

defmodule PhoenixTrello 
  use Application

   start(_type, _args) 
    import Supervisor.Spec, warn: false

    children = [
      
      supervisor(PhoenixTrello.BoardChannel.Supervisor, []),
      
    ]
```

And that's it! Now every list of connected users to a single board will be stored in a independent process and won't be affected by errors firing on other processes of the same type. Don't forget to check out the changes on the demo and in the source repository:

Happy coding!
