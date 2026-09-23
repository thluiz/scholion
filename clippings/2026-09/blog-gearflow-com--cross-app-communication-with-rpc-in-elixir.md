---
url: "https://blog.gearflow.com/cross-app-communication?utm_medium=email&utm_source=elixir-radar"
captured_at: "2026-09-23T19:05:10+01:00"
title: "Cross-App Communication with RPC in Elixir"
domain: "blog.gearflow.com"
---

Technology
Cross-App Communication with RPC in Elixir

Learn how we use Erlang's built-in RPC and EPMD to connect two Phoenix apps without HTTP overhead—and when this lightweight approach makes sense.

Christian Koch
Jan 21, 2026
Inter-app comms- HTTP not required
RPC with Distributed Erlang

We run two Phoenix applications that need to share data. One handles procurement workflows, the other manages users and core platform features. The obvious solutions: HTTP APIs, message queues, shared databases each come with tradeoffs and overhead we didn't want.

We used distributed Erlang instead.

Definitions and terms:

RPC – Remote Procedure Call. A protocol that lets one program execute a function on another machine as if it were local.
OTP – Open Telecom/Telephony Platform. Erlang's battle-tested framework for building concurrent, fault-tolerant applications. Includes supervisors, gen_servers, and the libraries that make Elixir reliable.
BEAM – Bogdan/Björn's Erlang Abstract Machine. The virtual machine that runs Erlang and Elixir code, designed for massive concurrency and distributed computing.
EPMD – Erlang Port Mapper Daemon. A small service that tracks which Erlang nodes are running on a host and what ports they're listening on.
VPC – Virtual Private Cloud. An isolated network within a cloud provider where your services can communicate privately.
DNS – Domain Name System. Translates hostnames (like my-app.internal) to IP addresses.
The Erlang Advantage

Elixir runs on the BEAM, which was designed for distributed systems decades before "microservices" became a buzzword. Most elixir apps are apps that implement OTP. Nodes that share a secret can call functions on each other directly:

:rpc.call(node, Module, :function, [args], timeout)

No HTTP. No JSON. No binary serialization. No auth middleware. The remote node executes the function and returns the result.

Both apps already expose GraphQL (GQL) via Absinthe. We have the option to reuse the GQL schemae or we can reach directly for remote module.

:rpc.call(remote_node, Absinthe, :run, [
    "{ session { user { id name } } }",
    MyApp.Schema,
    [context: %{current_user_id: user_id}]
  ], 30_000)

Same schema, same resolvers, same authorization—just a different transport.

We wrapped this in an RPC client module:

def query(query_string, variables \\ %{}, opts \\ []) do
  case get_remote_node() do
    nil -> {:error, :no_node_available}
    node -> execute_rpc(node, query_string, variables, opts)
  end
end
The Coupling Question

Treating two distinct apps as interchangeable BEAM nodes is a code smell. It creates implicit coupling—schema changes in one app can break the other at runtime with no compile-time warning. There's no API contract, no versioning, no deprecation path. If the remote module changes its function signature, you find out in production.

We went in with eyes open.

The alternative is building an internal API: define endpoints, add authentication between services, handle serialization, manage HTTP connection pools, implement retries and circuit breakers, version the schema, maintain documentation. That's real work that solves real problems—but those problems emerge at a certain scale and team size.

For two apps maintained by the same team, the implicit coupling already exists in practice. We share a deployment pipeline, coordinate releases, and communicate changes over Slack. HTTP doesn't remove the coupling; it just adds ceremony around it. The compile-time safety of an API contract matters more when separate teams own each service and can't coordinate releases easily.

The honest trade-off: we're betting that the cost of an accidental breaking change (which we'd catch quickly) is lower than the ongoing cost of maintaining internal API infrastructure (which we'd pay every day). If that bet stops paying off—more apps, more teams, more churn—we'll add explicit boundaries. The migration path is clear: swap :rpc.call for HTTP and keep the same GraphQL queries.

Until then, we avoid:

Maintaining two API schemas (GraphQL for clients, something else for internal)
Auth token management between services
HTTP connection pools and retry logic
Serialization overhead on every request
Node Discovery

Knowing which nodes exist is the harder problem. We used libcluster, which polls DNS and connects to discovered nodes automatically:

config :libcluster,
    topologies: [
      remote_app: [
        strategy: Cluster.Strategy.DNSPoll,
        config: [...]
      ]
    ]

This didn't work. Fly.io appends image hashes to node names:

Expected: my-app@fdaa:0:846:...
  Actual:   my-app-01ABC123@fdaa:0:846:...
                  ^^^^^^^^^ image hash

DNSPoll constructs node names from a static basename, missing the hash entirely.

Custom Discovery via EPMD

We built a custom libcluster strategy that queries EPMD (Erlang Port Mapper Daemon) directly. Every Erlang node registers with EPMD on its host. Our approach:

DNS lookup → get IP addresses
EPMD query on each IP → get actual node names with hashes
Filter by prefix → find the nodes we want
Connect
defp discover_nodes_via_epmd(ips, basename) do
  Enum.flat_map(ips, fn ip -> query_epmd(ip, basename) end)
end

defp query_epmd(ip, basename) do
  case :erl_epmd.names(ip) do
    {:ok, names} ->
      names
      |> Enum.filter(fn {name, _port} ->
        name |> List.to_string() |> String.starts_with?(basename)
      end)
      |> Enum.map(fn {name, _port} -> :"#{name}@#{format_ip(ip)}" end)

    {:error, _} -> []
  end
end

The strategy handles both IPv4 and IPv6, gracefully recovers from unreachable nodes, and tracks connections as nodes scale up and down.

When This Makes Sense

This approach works when:

Both apps run on the BEAM
You control both codebases
The network is trusted (same Fly.io org, same VPC)
You want to iterate without infrastructure overhead

It doesn't work when:

Apps are in different languages
You need explicit API contracts for separate teams
The network boundary is untrusted
Implicit coupling becomes expensive at your scale
Production Setup
# Same cookie on both apps
fly secrets set RELEASE_COOKIE="<shared-secret>" -a app-one
fly secrets set RELEASE_COOKIE="<shared-secret>" -a app-two

# Tell one app where to find the other
fly secrets set REMOTE_APP_NAME="app-two" -a app-one

The apps discover each other automatically. Querying across the cluster is a single function call:

RemoteApp.RpcClient.query(
  "{ session { user { id name email } } }",
  %{},
  context: %{current_user_id: user_id}
)

OTP has been solving distributed systems problems since 1986. In fact both Erlang and OTP were literally designed for it computing. Sometimes the old tools are the not only the right ones but they are the best ones for the job.

Technology
elixir
otp
rpc
