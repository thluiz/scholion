---
url: "https://medium.com/@wttj_tech/elixir-how-to-distribute-mnesia-between-multiple-nodes-cb7c851b1ed1"
captured_at: "2021-06-17T20:36:46-03:00"
title: "Elixir: How to distribute Mnesia between multiple nodes | by WTTJ Tech | Jun, 2021 | Medium"
domain: "medium-com"
---

[WTTJ Tech](https://medium.com/@wttj_tech?source=post_page-----cb7c851b1ed1--------------------------------)

[17 Followers](https://medium.com/@wttj_tech/followers?source=post_page-----cb7c851b1ed1--------------------------------)

[About](https://medium.com/@wttj_tech/about?source=post_page-----cb7c851b1ed1--------------------------------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40wttj_tech%2Felixir-how-to-distribute-mnesia-between-multiple-nodes-cb7c851b1ed1&source=post_page-----cb7c851b1ed1---------------------nav_reg-----------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1043.63 592.71' class='q r js-evernote-checked' data-evernote-id='135'%3e%3cg data-name='Layer 2' data-evernote-id='136' class='js-evernote-checked'%3e%3cg data-name='Layer 1' data-evernote-id='137' class='js-evernote-checked'%3e%3cpath d='M588.67 296.36c0 163.67-131.78 296.35-294.33 296.35S0 460 0 296.36 131.78 0 294.34 0s294.33 132.69 294.33 296.36M911.56 296.36c0 154.06-65.89 279-147.17 279s-147.17-124.94-147.17-279 65.88-279 147.16-279 147.17 124.9 147.17 279M1043.63 296.36c0 138-23.17 249.94-51.76 249.94s-51.75-111.91-51.75-249.94 23.17-249.94 51.75-249.94 51.76 111.9 51.76 249.94' data-evernote-id='138' class='js-evernote-checked'%3e%3c/path%3e%3c/g%3e%3c/g%3e%3c/svg%3e)](https://medium.com/?source=post_page-----cb7c851b1ed1--------------------------------)

# **Elixir: How to distribute Mnesia between multiple nodes**

[![](https://miro.medium.com/fit/c/56/56/1*_wuiZJlqk_JfauVDrGSUCg.png)](https://medium.com/@wttj_tech?source=post_page-----cb7c851b1ed1--------------------------------)

[WTTJ Tech](https://medium.com/@wttj_tech?source=post_page-----cb7c851b1ed1--------------------------------)

[2 days ago·7 min read](https://medium.com/@wttj_tech/elixir-how-to-distribute-mnesia-between-multiple-nodes-cb7c851b1ed1?source=post_page-----cb7c851b1ed1--------------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='25' height='25' viewBox='0 0 25 25' data-evernote-id='239' class='js-evernote-checked'%3e%3cpath d='M19 6a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2v14.66h.01c.01.1.05.2.12.28a.5.5 0 0 0 .7.03l5.67-4.12 5.66 4.13a.5.5 0 0 0 .71-.03.5.5 0 0 0 .12-.29H19V6zm-6.84 9.97L7 19.64V6a1 1 0 0 1 1-1h9a1 1 0 0 1 1 1v13.64l-5.16-3.67a.49.49 0 0 0-.68 0z' fill-rule='evenodd' data-evernote-id='240' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fcb7c851b1ed1&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40wttj_tech%2Felixir-how-to-distribute-mnesia-between-multiple-nodes-cb7c851b1ed1&source=post_actions_header--------------------------bookmark_preview-----------)

![](https://miro.medium.com/max/10200/1*5T0KVgzKK4t0cnZgtRUNKA.png)

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

![](https://miro.medium.com/max/60/1*jFUWnTQXeWozhLKXtyvm8g.png?q=20)

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

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='25' height='25' viewBox='0 0 25 25' aria-label='clap' data-evernote-id='537' class='js-evernote-checked'%3e%3cg fill-rule='evenodd' data-evernote-id='538' class='js-evernote-checked'%3e%3cpath d='M11.74 0l.76 2.97.76-2.97zM14.81 3.78l1.84-2.56-1.42-.47zM8.38 1.22l1.84 2.56L9.8.75zM20.38 21.62a5.11 5.11 0 0 1-3.16 1.61l.49-.45c2.88-2.89 3.45-5.98 1.69-9.21l-1.1-1.94-.96-2.02c-.31-.67-.23-1.18.25-1.55a.84.84 0 0 1 .66-.16c.34.05.66.28.88.6l2.85 5.02c1.18 1.97 1.38 5.12-1.6 8.1M7.1 21.1l-5.02-5.02a1 1 0 0 1 .7-1.7 1 1 0 0 1 .72.3l2.6 2.6a.44.44 0 0 0 .63-.62L4.1 14.04l-1.75-1.75a1 1 0 1 1 1.41-1.41l4.15 4.15a.44.44 0 0 0 .63 0 .44.44 0 0 0 0-.62L4.4 10.26 3.22 9.08a1 1 0 0 1 0-1.4 1.02 1.02 0 0 1 1.41 0l1.18 1.16L9.96 13a.44.44 0 0 0 .62 0 .44.44 0 0 0 0-.63L6.43 8.22a.99.99 0 0 1-.3-.7.99.99 0 0 1 .3-.7 1 1 0 0 1 1.41 0l7 6.98a.44.44 0 0 0 .7-.5l-1.35-2.85c-.31-.68-.23-1.19.25-1.56a.85.85 0 0 1 .66-.16c.34.06.66.28.88.6L18.63 14c1.57 2.88 1.07 5.54-1.55 8.16a5.62 5.62 0 0 1-5.06 1.65 9.35 9.35 0 0 1-4.93-2.72zM11 5.98l2.56 2.56c-.5.6-.56 1.41-.15 2.28l.26.56-4.25-4.25a.98.98 0 0 1-.12-.45 1 1 0 0 1 .29-.7 1.02 1.02 0 0 1 1.41 0zm8.89 2.06c-.38-.56-.9-.92-1.49-1.01a1.74 1.74 0 0 0-1.34.33c-.38.29-.61.65-.71 1.06a2.1 2.1 0 0 0-1.1-.56 1.78 1.78 0 0 0-.99.13l-2.64-2.64a1.88 1.88 0 0 0-2.65 0 1.86 1.86 0 0 0-.48.85 1.89 1.89 0 0 0-2.67-.01 1.87 1.87 0 0 0-.5.9c-.76-.75-2-.75-2.7-.04a1.88 1.88 0 0 0 0 2.66c-.3.12-.61.29-.87.55a1.88 1.88 0 0 0 0 2.66l.62.62a1.88 1.88 0 0 0-.9 3.16l5.01 5.02c1.6 1.6 3.52 2.64 5.4 2.96a7.16 7.16 0 0 0 1.18.1c1.03 0 2-.25 2.9-.7A5.9 5.9 0 0 0 21 22.24c3.34-3.34 3.08-6.93 1.74-9.17l-2.87-5.04z' data-evernote-id='539' class='js-evernote-checked'%3e%3c/path%3e%3c/g%3e%3c/svg%3e)](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2Fcb7c851b1ed1&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40wttj_tech%2Felixir-how-to-distribute-mnesia-between-multiple-nodes-cb7c851b1ed1&user=WTTJ%20Tech&userId=ae39e5010eaa&source=post_actions_footer-----cb7c851b1ed1---------------------clap_footer-----------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='25' height='25' viewBox='0 0 25 25' data-evernote-id='579' class='js-evernote-checked'%3e%3cpath d='M19 6a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2v14.66h.01c.01.1.05.2.12.28a.5.5 0 0 0 .7.03l5.67-4.12 5.66 4.13a.5.5 0 0 0 .71-.03.5.5 0 0 0 .12-.29H19V6zm-6.84 9.97L7 19.64V6a1 1 0 0 1 1-1h9a1 1 0 0 1 1 1v13.64l-5.16-3.67a.49.49 0 0 0-.68 0z' fill-rule='evenodd' data-evernote-id='580' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fcb7c851b1ed1&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40wttj_tech%2Felixir-how-to-distribute-mnesia-between-multiple-nodes-cb7c851b1ed1&source=post_actions_footer--------------------------bookmark_footer-----------)

- [Elixir](https://medium.com/tag/elixir)
- [Mnesia](https://medium.com/tag/mnesia)

## [More from WTTJ Tech](https://medium.com/@wttj_tech?source=follow_footer-------------------------------------)

## More From Medium

## [Flutter Expanded Widget](https://medium.com/flutter-community/flutter-expanded-widget-e203590f00cf?source=post_internal_links---------0----------------------------)

[Suragch](https://suragch.medium.com/?source=post_internal_links---------0----------------------------) in [Flutter Community](https://medium.com/flutter-community?source=post_internal_links---------0----------------------------)

[![](https://miro.medium.com/max/45/1*PR7UJgfT8073tZVijJFd2w.png?q=20)

![]()](https://medium.com/flutter-community/flutter-expanded-widget-e203590f00cf?source=post_internal_links---------0----------------------------)

## [Searching and Filtering: Spring Data JPA Specification way](https://medium.com/fleetx/searching-and-filtering-spring-data-jpa-specification-way-e22bc055229a?source=post_internal_links---------1----------------------------)

[Rahul Yadav](https://medium.com/@rahul.yadav_90307?source=post_internal_links---------1----------------------------) in [fleetx](https://medium.com/fleetx?source=post_internal_links---------1----------------------------)

[![](https://miro.medium.com/max/45/1*hn4v1tCaJy7cWMyb0bpNpQ.png?q=20)

![]()](https://medium.com/fleetx/searching-and-filtering-spring-data-jpa-specification-way-e22bc055229a?source=post_internal_links---------1----------------------------)

## [Spring Boot —JPA and Unit testing with JUnit](https://haris-zujo.medium.com/spring-boot-jpa-and-unit-testing-with-junit-e14a2d8ff319?source=post_internal_links---------2----------------------------)

[Haris Zujo](https://haris-zujo.medium.com/?source=post_internal_links---------2----------------------------)

[![](https://miro.medium.com/max/45/1*8KX5TdvTf6HlEjls69uPjw.png?q=20)

![]()](https://haris-zujo.medium.com/spring-boot-jpa-and-unit-testing-with-junit-e14a2d8ff319?source=post_internal_links---------2----------------------------)

## [Some of the most used Git interactive rebase options](https://medium.com/swlh/some-of-the-most-used-git-interactive-rebase-options-e152b6302640?source=post_internal_links---------3----------------------------)

[Martin Belev](https://martinbelev.medium.com/?source=post_internal_links---------3----------------------------) in [The Startup](https://medium.com/swlh?source=post_internal_links---------3----------------------------)

[![](https://miro.medium.com/max/45/1*sedyQbgxWRuJZeiMX-07Eg.png?q=20)

![]()](https://medium.com/swlh/some-of-the-most-used-git-interactive-rebase-options-e152b6302640?source=post_internal_links---------3----------------------------)

## [AWS Lambda Logging tools and best practices — Python](https://medium.com/codex/aws-lambda-logging-tools-and-best-practices-python-e156a76f52a7?source=post_internal_links---------4----------------------------)

[Dheeraj Inampudi](https://dheerajinampudi.medium.com/?source=post_internal_links---------4----------------------------) in [CodeX](https://medium.com/codex?source=post_internal_links---------4----------------------------)

[![](https://miro.medium.com/max/45/1*26I3t7jmniwZicjyRLGl-w.png?q=20)

![]()](https://medium.com/codex/aws-lambda-logging-tools-and-best-practices-python-e156a76f52a7?source=post_internal_links---------4----------------------------)

## [Introducing Syncfusion Blazor Code Snippets for Visual Studio Code](https://medium.com/syncfusion/introducing-syncfusion-blazor-code-snippets-for-visual-studio-code-e1921764623f?source=post_internal_links---------5----------------------------)

[Rajeshwari Pandinagarajan](https://medium.com/@rajeshwari.pandinagarajan?source=post_internal_links---------5----------------------------) in [Syncfusion](https://medium.com/syncfusion?source=post_internal_links---------5----------------------------)

[![](https://miro.medium.com/max/45/0*vun9Wy-Z-plUqSmo.png?q=20)

![]()](https://medium.com/syncfusion/introducing-syncfusion-blazor-code-snippets-for-visual-studio-code-e1921764623f?source=post_internal_links---------5----------------------------)

## [Learn to Build a Parser in Rust for Fun and Profit](https://medium.com/geekculture/learn-to-build-a-parser-in-rust-for-fun-and-profit-e22ca0e0ce4c?source=post_internal_links---------6----------------------------)

[pancy](https://pancy.medium.com/?source=post_internal_links---------6----------------------------) in [Geek Culture](https://medium.com/geekculture?source=post_internal_links---------6----------------------------)

[![](https://miro.medium.com/max/45/1*fUfd2n5p2Sm5QerP0sFpBw.jpeg?q=20)

![]()](https://medium.com/geekculture/learn-to-build-a-parser-in-rust-for-fun-and-profit-e22ca0e0ce4c?source=post_internal_links---------6----------------------------)

## [Array Two pointers](https://medium.com/analytics-vidhya/array-two-pointers-4b8d62d2b8a?source=post_internal_links---------7----------------------------)

[Shantanu Tripathi](https://shantanu-tripathi.medium.com/?source=post_internal_links---------7----------------------------) in [Analytics Vidhya](https://medium.com/analytics-vidhya?source=post_internal_links---------7----------------------------)

[![](https://miro.medium.com/max/45/1*fKkUPAz6jONa2QBLboM5Mw.png?q=20)

![]()](https://medium.com/analytics-vidhya/array-two-pointers-4b8d62d2b8a?source=post_internal_links---------7----------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 3940 610' class='mh sr js-evernote-checked' data-evernote-id='830'%3e%3cpath d='M594.79 308.2c0 163.76-131.85 296.52-294.5 296.52S5.8 472 5.8 308.2 137.65 11.69 300.29 11.69s294.5 132.75 294.5 296.51M917.86 308.2c0 154.16-65.93 279.12-147.25 279.12s-147.25-125-147.25-279.12S689.29 29.08 770.61 29.08s147.25 125 147.25 279.12M1050 308.2c0 138.12-23.19 250.08-51.79 250.08s-51.79-112-51.79-250.08 23.19-250.08 51.8-250.08S1050 170.09 1050 308.2M1862.77 37.4l.82-.18v-6.35h-167.48l-155.51 365.5-155.51-365.5h-180.48v6.35l.81.18c30.57 6.9 46.09 17.19 46.09 54.3v434.45c0 37.11-15.58 47.4-46.15 54.3l-.81.18V587H1327v-6.35l-.81-.18c-30.57-6.9-46.09-17.19-46.09-54.3V116.9L1479.87 587h11.33l205.59-483.21V536.9c-2.62 29.31-18 38.36-45.68 44.61l-.82.19v6.3h213.3v-6.3l-.82-.19c-27.71-6.25-43.46-15.3-46.08-44.61l-.14-445.2h.14c0-37.11 15.52-47.4 46.08-54.3m97.43 287.8c3.49-78.06 31.52-134.4 78.56-135.37 14.51.24 26.68 5 36.14 14.16 20.1 19.51 29.55 60.28 28.09 121.21zm-2.11 22h250v-1.05c-.71-59.69-18-106.12-51.34-138-28.82-27.55-71.49-42.71-116.31-42.71h-1c-23.26 0-51.79 5.64-72.09 15.86-23.11 10.7-43.49 26.7-60.45 47.7-27.3 33.83-43.84 79.55-47.86 130.93-.13 1.54-.24 3.08-.35 4.62s-.18 2.92-.25 4.39a332.64 332.64 0 0 0-.36 21.69C1860.79 507 1923.65 600 2035.3 600c98 0 155.07-71.64 169.3-167.8l-7.19-2.53c-25 51.68-69.9 83-121 79.18-69.76-5.22-123.2-75.95-118.35-161.63m532.69 157.68c-8.2 19.45-25.31 30.15-48.24 30.15s-43.89-15.74-58.78-44.34c-16-30.7-24.42-74.1-24.42-125.51 0-107 33.28-176.21 84.79-176.21 21.57 0 38.55 10.7 46.65 29.37zm165.84 76.28c-30.57-7.23-46.09-18-46.09-57V5.28L2424.77 60v6.7l1.14-.09c25.62-2.07 43 1.47 53.09 10.79 7.9 7.3 11.75 18.5 11.75 34.26v71.14c-18.31-11.69-40.09-17.38-66.52-17.38-53.6 0-102.59 22.57-137.92 63.56-36.83 42.72-56.3 101.1-56.3 168.81C2230 518.72 2289.53 600 2378.13 600c51.83 0 93.53-28.4 112.62-76.3V588h166.65v-6.66zm159.29-505.33c0-37.76-28.47-66.24-66.24-66.24-37.59 0-67 29.1-67 66.24s29.44 66.24 67 66.24c37.77 0 66.24-28.48 66.24-66.24m43.84 505.33c-30.57-7.23-46.09-18-46.09-57h-.13V166.65l-166.66 47.85v6.5l1 .09c36.06 3.21 45.93 15.63 45.93 57.77V588h166.8v-6.66zm427.05 0c-30.57-7.23-46.09-18-46.09-57V166.65L3082 212.92v6.52l.94.1c29.48 3.1 38 16.23 38 58.56v226c-9.83 19.45-28.27 31-50.61 31.78-36.23 0-56.18-24.47-56.18-68.9V166.66l-166.66 47.85V221l1 .09c36.06 3.2 45.94 15.62 45.94 57.77v191.27a214.48 214.48 0 0 0 3.47 39.82l3 13.05c14.11 50.56 51.08 77 109 77 49.06 0 92.06-30.37 111-77.89v66h166.66v-6.66zM3934.2 588v-6.67l-.81-.19c-33.17-7.65-46.09-22.07-46.09-51.43v-243.2c0-75.83-42.59-121.09-113.93-121.09-52 0-95.85 30.05-112.73 76.86-13.41-49.6-52-76.86-109.06-76.86-50.12 0-89.4 26.45-106.25 71.13v-69.87l-166.66 45.89v6.54l1 .09c35.63 3.16 45.93 15.94 45.93 57V588h155.5v-6.66l-.82-.2c-26.46-6.22-35-17.56-35-46.66V255.72c7-16.35 21.11-35.72 49-35.72 34.64 0 52.2 24 52.2 71.28V588h155.54v-6.66l-.82-.2c-26.46-6.22-35-17.56-35-46.66v-248a160.45 160.45 0 0 0-2.2-27.68c7.42-17.77 22.34-38.8 51.37-38.8 35.13 0 52.2 23.31 52.2 71.28V588z' data-evernote-id='831' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/?source=post_page-----cb7c851b1ed1--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----cb7c851b1ed1--------------------------------)

[Help](https://help.medium.com/hc/en-us?source=post_page-----cb7c851b1ed1--------------------------------)

[Legal](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----cb7c851b1ed1--------------------------------)
