---
url: "https://medium.com/@wttj_tech/elixir-how-to-distribute-mnesia-between-multiple-nodes-cb7c851b1ed1"
captured_at: "2021-06-17T16:54:08-03:00"
title: "Elixir: How to distribute Mnesia between multiple nodes | by WTTJ Tech | Jun, 2021 | Medium"
domain: "medium-com"
---

# Elixir: How to distribute Mnesia between multiple nodes

![1*5T0KVgzKK4t0cnZgtRUNKA.png](medium-com--elixir-distribute-mnesia-between-multiple-nodes/91c447287ed1391879ef142e7499ac6d.png)

At Welcome to the Jungle, we love Elixir. It’s the main stack we use to build back-end services and it really helps us keep our code clean and leverage great performance. One of its strengths is that it is built on the BEAM, the Erlang virtual machine, and it also offers us access to great built-in features, Mnesia being one of them. Mnesia is a distributed database that’s embedded in Erlang and is super-easy to access — you don’t have to rely on a third-party service because it’s already available with your Elixir app.

In a [previous article](https://www.welcometothejungle.com/en/articles/redis-mnesia-distributed-database), we showed how Mnesia could be used to store data for performance-sensitive systems and that it was simple to set up and access directly from an Elixir application. This time we want to share how we scaled our Mnesia usage in our different services, how we coupled the performances of Mnesia, and the persistence that was required to deploy our services with multiple nodes running.

# **A bit of context**

We developed a service for building and sending emails based on saved job searches. To initiate this service’s main task, we created a couple of GenServers to process some data in the background. This worked well but we needed at some point to persist their states, and we looked at two options:

- Using classic Redis.
- Using Mnesia as our state store.

You already know which one we went for: The second option. One reason was that we did not have Redis set up for this instance and that Mnesia was available right out of the box.

One problem arose quickly, though: How would we manage to avoid data loss when deploying the app on instances?

As we carry out [blue/green deployments](https://martinfowler.com/bliki/BlueGreenDeployment.html), we knew that we would occasionally have two applications running at the same time before they were swapped. This means that those two applications needed to be synced to prevent GenServers performing the same tasks (sending the same emails twice, for example) and to permit the new instance to be updated with both the data that has already been processed and the data that needs to be processed, so that it can continue doing the job after the old instance is terminated.

That’s when Mnesiac and Libcluster joined the game.

- [Mnesiac](https://github.com/beardedeagle/mnesiac) is a library for building and managing Mnesia clusters.
- [Libcluster](https://github.com/bitwalker/libcluster) supports Mnesiac and helps supervise the clusters.

With these two libraries, we were able to define proper stores (Mnesia tables) to use in our app and sync those stores between multiple nodes. Now we know that, when we deploy our apps, our stores are syncing and can seamlessly continue processing.

Now that we’ve talked a little about why we looked into those libraries, we’d like to show you the steps that we followed to set up our clusters. In the next section, you’ll find out how to:

- Use Mnesiac to define stores that will represent your tables and define the types used in those tables and the behaviors to perform when conflicts occur while synchronizing.
- Use Libcluster to build your Mnesia cluster, communicate with outside nodes (such as EC2 instances), and supervise how your cluster is doing.

# **Building clean clusters with Mnesiac**

## **Defining our stores**

The first step is to define your Mnesia tables (or stores) using Mnesiac.

Mnesiac provides great tools for defining your tables beforehand. You are able to create stores to define the content and types of tables and execute some code when conflict occurs between two nodes.

In our case, we wanted one store to use for notifications that are being processed. So you need to define your store using code such as `notification_store.ex`.

```
defmodule MyApp.Stores.NotificationStore do  
 use Mnesiac.Store  
  import Record, only: [defrecord: 3] require Logger  defrecord(  
    :notification,  
    :notifications,  
    reference: nil,  
    message: nil  
  ) @type notification ::  
          record(  
            :notification,  
            reference: String.t(),  
            message: String.t()  
          )  @impl true  
  def store_options do  
  [  
      record_name: :notification,  
      attributes: notification() |> notification() |> Keyword.keys(),  
      index: [],  
      disc_copies: [node()]  
    ]  
 end  
end
```

Defining your store will help centralize your code related to initializing Mnesia tables in one place and also give them a more explicit look with clear types and behaviors. For example, Mnesiac will allow you to resolve the conflicts between 2 nodes when they are synchronizing. You can maybe add a logger to keep track of what happens:

```
@impl true  
def resolve_conflict(node) do  
  Logger.warn("RESOLVE CONFLICT #{inspect(node())} vs #{inspect(node)}")  
  
copy_store()  
end
```

## **Configuring Mnesiac in our project**

Next, we just have to add our store in our app config (`config/config.exs`)

```
config :mnesiac,  
  dir: '.mnesia/#{node()}',  
  stores: [MyApp.Stores.NotificationStore],  
  schema_type: :disc_copies
```

After setting up your store, you can directly use it as you would any other Mnesia table inside your application.

```
:mnesia.transaction(fn ->  
	:mnesia.read({:notification, some_reference})  
end)
```

At this point we did set up our store, but we needed to register it inside a cluster. To do that we needed a second library: Libcluster

# **Clustering Mnesiac stores with Libcluster and Libcluster\_EC2**

## **Using your cluster on Libcluster**

Once we had our Mnesiac Stores, we needed to build our cluster.

Here, using Libcluster, we defined our cluster as a process of our app and were able to benefit from the supervisor. We were also able to define the strategy we wanted to use for our nodes to connect (having the cluster run in Kubernetes or simply multiple EC2 instances). You will also see that we were able to leverage that by having a larger cluster with multiple EC2 instances.

First, we built a simple config to be used in our cluster module later. Our hosts represent nodes for our cluster. Right now we use simple, local nodes, but later in the article we will fetch nodes using EC2 tags.

```
config :libcluster,  
  topologies: [  
    my_app: [  
      strategy: Cluster.Strategy.Epmd,  
      config: [hosts: [:foo@localhost, :bar@localhost]]  
    ]  
  ]
```

The configuration above is the most simple one — it simply uses the [Erlang port mapper daemon](https://erlang.org/doc/man/epmd.html) as strategy. There are a lot more parameters and strategies that you can add to this config to control how your cluster will behave.

The base of our cluster will look like the below example. It will simply define what to do when the cluster is starting and define its children and how to supervise them. We will also be able to add more “helpers” to register external nodes to the cluster (EC2 instances, for example).

```
defmodule MyApp.Cluster do  
  use GenServer  
  
def start_link(_opts) do  
    GenServer.start_link(__MODULE__, Node.list(), name: __MODULE__)  
  end  
  
@impl true  
  def init(state) do  
		## Here we are setting up our stores  
    Mnesiac.init_mnesia(Node.list())  
    {:ok, state}  
  end  
  
def children_spec() do  
		# get our previously defined config  
    case Application.get_env(:libcluster, :topologies) do  
      nil ->  
        nil  
  
topologies ->  
        hosts = get_in(topologies, [:my_app, :config, :hosts]) || []  
  
[  
          {Cluster.Supervisor, [topologies, [name: MyApp.ClusterSupervisor]]},  
  
## Here we are adding our Mnesiac supervisor  
					{Mnesiac.Supervisor, [hosts, [name: MyApp.MnesiacSupervisor]]}  
        ]  
    end  
  end  
end
```

At this point, you can add your cluster to your `application.ex` children processes.

```
defmodule MyApp.Application do  
#...  
  def start(_type, _args) do  
		children = [  
			#...  
			MyApp.Cluster  
		]  
  
# add cluster children (Mnesiac)  
		children = case MyApp.Cluster.children_spec() do  
			nil ->  
				children  
  
children_spec ->  
          children ++ children_spec  
		end  
  end  
  
#...  
end
```

Then you should be good to go. Our cluster starts with our other processes. So when starting your app, you should see the below 2 lines:

![1*jFUWnTQXeWozhLKXtyvm8g.png](medium-com--elixir-distribute-mnesia-between-multiple-nodes/dd1c57065c21ccebe4edfec27ec95ff0.png)

![]()

You will now be able to use your `state` table directly :

```
> mnesia.transaction(fn -> :mnesia.write({:notification, "test", "test!"}) end)  
{:atomic, :ok}  
  
> :mnesia.transaction(fn -> :mnesia.read({:notification, "test"}) end)  
{:atomic, [{:notification, "test", "test!"}]}
```

To test that the nodes are properly connected we are able to start 2 terminals with 2 IEx sessions with names that match the hosts we defined for our cluster earlier.

```
> iex --sname foo@localhost -S mix  
__________________________________  
  
> iex --sname bar@localhost -S mix
```

Then, when we’re listing nodes for our cluster, we should see something like this:

```
iex(bar@localhost)1> Mnesiac.running_nodes()  
[:foo@localhost, :bar@localhost]
```

Then you can write something in one node and read it in the other.

Now that you are able to communicate between nodes, we can look at how to do the same thing in a more complex environment: EC2 instances.

## **Using your cluster on AWS**

With Libcluster, you can build your cluster on Kubernetes, like we did, or by using [Libcluster\_EC2](https://github.com/kyleaa/libcluster_ec2) on multiple AWS EC2 instances.

For that config we would slightly change what we used before:

```
config :libcluster,  
  topologies: [  
    my_app: [  
      strategy: ClusterEC2.Strategy.Tags,  
      config: [  
        ec2_tagname: System.get_env("EC2_TAGNAME", "DefaultTagName"),  
        ec2_tagvalue: System.get_env("EC2_TAGVALUE", "DefaultTagValue"),  
        app_prefix: "my_app",  
				# you can pass a function that will be used to map a list of ip  
        ip_to_nodename: &MyApp.Cluster.ip_to_nodename/2  
      ]  
    ]  
  ]
```

Adding `ip_to_nodename/2`to our `MyApp.Cluster`helps to map our list of ip given by ClusterEC2 to the Erlang node name.

```
def ip_to_nodename(list, app_prefix) when is_list(list) do  
  list  
  |> Enum.map(fn ip ->  
    :"#{app_prefix}@ip-#{ip |> String.replace(".", "-")}"  
  end)  
end
```

# What happened next

Currently, this system is running in production, seamlessly processing about 150,000 notifications, and sending roughly 30,000 mails per day. We can safely deploy our application without losing any data and we are quite happy with the solution. Everything stays inside the BEAM and our service remains as independent as possible.

If your goal is to keep a service self-contained and retain control over your dependencies, this is something that will both perform well and be scalable between multiple nodes and, therefore, instances. We haven’t tested this system inside a dockerized environment and Kubernetes cluster yet, but so far, thanks to Libcluster, things seem promising!

*Curious about what we’re dealing with in WTTJ’s engineering team? Check out our* [*Welcome Bits*](https://github.com/WTTJ/welcome-bits) *GitHub repository! Every two weeks, we share a selection of curated content as well as learnings and explorations from our journey as engineers.*

*Written by* [*Samuel Collon*](https://www.linkedin.com/in/%F0%9F%8C%B4-samuel-collon-3b0114114/?locale=fr_FR)*, Back-end developer @ WTTJ*

[*Join our team!*](https://www.welcometothejungle.co/companies/wttj/jobs)

*Illustration by* [*Blok*](https://fr.creasenso.com/portfolio/blok)
