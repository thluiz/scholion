---
url: "https://systemdesign.one/what-is-service-discovery/?ref=dailydev"
captured_at: "2026-09-25T21:18:19+01:00"
title: "What Is Service Discovery?"
domain: "systemdesign-one"
---

* * *

_The target audience for this article falls into the following roles:_

*   _Tech workers_
*   _Students_
*   _Engineering managers_

_The prerequisite to reading this article is fundamental knowledge of system design components. This article does not cover an in-depth guide on individual system design components._

_Disclaimer: The system design questions are subjective. This article is written based on my research on the topic and might differ from real-world implementations. Feel free to share your feedback and ask questions in the comments._

* * *

* * *

**Download my system design playbook for free on newsletter signup:**

* * *

* * *

* * *

A monolith application executes a function call to facilitate communication between services. The services in a microservice architecture are typically deployed on separate machines to attain improved fault tolerance. Therefore, the communication between services must be routed over the network in a microservice architecture [1](#fn:1).

The service location (combination of the IP address and port number) and binding (transport mechanism such as TCP for calling the endpoint) should be identified to interact with an instance of the service provider [2](#fn:2). The identification of the service location and management of resources in a microservice is challenging due to the dynamic nature of resources. On top of that, monitoring the health of system components such as the database, and message queue is crucial for increased reliability [3](#fn:3).

* * *

* * *

* * *

The system requirements can be summarized as follows [2](#fn:2), [4](#fn:4), [5](#fn:5).

*   service information can be written, read, deleted, or updated
*   services can be searched
*   provide RESTful API
*   support checks at the service level

* * *

*   high availability
*   low memory and CPU footprint
*   reliability
*   low latency

* * *

* * *

* * *

The following terminology might be helpful for you:

*   service provider: a service exposing an Application Programming Interface (**API**) such as Representational State Transfer (**REST**)
*   service consumer: a service that reads and writes data
*   service registry: a database that stores locations of all available service instances
*   service location: a combination of Internet Protocol (**IP**) address and port number

* * *

* * *

* * *

The location of a service instance is required to interact with the service provider. The count of service instances and service location change dynamically in a microservice architecture. Service discovery is the process of retrieving the list of instances of a service provider for interaction between service consumers and the server provider [6](#fn:6).

The service registry is the database component of service discovery that stores the service locations (IP addresses and port numbers) to provide runtime service endpoint resolution [7](#fn:7). The service instances must register with the service registry on startup and deregister on shutdown.

* * *

* * *

* * *

The service discovery can expose a RESTful or Remote Procedure Call (**RPC**) based API [8](#fn:8).

The service instance (**client**) can execute a Hypertext Transfer Protocol (**HTTP**) PUT request to register the service instance to the service registry.

```
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
```

```
/services/:service-id
method: PUT
authorization: Bearer <JWT>
content-length: 100
content-type: application/JSON
content-encoding: gzip

{
    name: "Service A",
    ip_address: "10.0.x.x",
    port_number: "8042",
    protocol: "TCP"
}
```

The server responds with status code 200 OK on success.

```
1
```

```
status code: 200 OK
```

The server responds with status code 400 bad request to indicate a failed request due to an invalid request payload by the client.

```
1
```

```
status code: 400 bad request
```

* * *

* * *

The client can execute an HTTP DELETE request to deregister a service instance.

```
1
2
3
```

```
/services/:service-id/:instance-id
method: DELETE
authorization: Bearer <JWT>
```

The server responds with status code 204 No Content on success.

```
1
```

```
status code: 204 No Content
```

* * *

* * *

The client can execute an HTTP GET request to fetch the list of service instances.

```
1
2
3
4
```

```
/services/:service-id
method: GET
authorization: Bearer <JWT>
accept: application/json, text/html
```

A successful response from the server can include status code 200 OK.

```
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
```

```
status code: 200 OK
cache-control: private, no-cache, must-revalidate, max-age=300
content-encoding: gzip
content-type: application/json

{
  service_name: "Service A",
  instance_count: 5,
  updated_at: "2031-10-10T12:11:42Z",
  instances: [
    {
      ip_address: "10.0.1.x",
      port_number: "8042"
    },
    {...}
  ]
}
```

* * *

* * *

* * *

The service registry data model should be kept flexible to accommodate future service deployments. The attributes of a service instance can be extended via key-value pairs in the metadata table [9](#fn:9). The major entities of the service discovery data schema are shown in Figure 1.

[![Figure 1: Service Discovery Database Schema](https://systemdesign.one/what-is-service-discovery/service-discovery-database-schema.webp)](https://systemdesign.one/what-is-service-discovery/service-discovery-database-schema.webp "Figure 1: Service Discovery Database Schema")

Figure 1: Service Discovery Database Schema

The operational metadata of a service instance could also include information about the active UDP sockets, TCP sockets, process names, path to the process executables, and the command line arguments [10](#fn:10), [11](#fn:11).

* * *

* * *

* * *

**Download my system design playbook for free on newsletter signup:**

* * *

* * *

* * *

[![Figure 2: Service Discovery; Write Workflow](https://systemdesign.one/what-is-service-discovery/service-discovery-write-workflow.webp)](https://systemdesign.one/what-is-service-discovery/service-discovery-write-workflow.webp "Figure 2: Service Discovery; Write Workflow")

Figure 2: Service Discovery; Write Workflow

The service provider provides its IP address and port number to register on the service registry. The periodic heartbeat signal is used to indicate the liveness status of a service instance. The polite service instances usually deregister themselves on shutdown. The absence of a heartbeat signal for an extended period caused by an abrupt shutdown of the service marks the instance as dead automatically [9](#fn:9).

* * *

* * *

[![Figure 3: Service Discovery; Read Workflow](https://systemdesign.one/what-is-service-discovery/service-discovery-read-workflow.webp)](https://systemdesign.one/what-is-service-discovery/service-discovery-read-workflow.webp "Figure 3: Service Discovery; Read Workflow")

Figure 3: Service Discovery; Read Workflow

The publish-subscribe (**pub-sub**) pattern can be used to implement a reliable service discovery. The service consumers should subscribe to the interested service providers on the service registry. Any changes to the service providers are pushed to the subscribed service consumers by the service registry [9](#fn:9), [2](#fn:2).

* * *

* * *

The different techniques to implement service discovery in a microservice architecture are the following [5](#fn:5), [2](#fn:2), [4](#fn:4):

*   hard code the service location in the service consumers
*   external configuration file
*   DNS-based service discovery
*   service discovery using a load balancer
*   service registry

A trivial approach to implementing service discovery is through manual management of the service provider locations within the application code of service consumers. However, the technique of manual management is error-prone and will not scale as the number of services increases [3](#fn:3).

In addition, hard coding the service location limits the service consumer to perform only certain types of load balancing and also makes it non-trivial to relocate the service instances due to tight coupling between the service consumer and service provider locations [5](#fn:5), [2](#fn:2). In summary, do not hard code the service provider locations to enable service discovery in a microservice architecture.

* * *

An external configuration file that is local to the service consumer can be used to store the location of the service providers. The external configuration file on the service consumers allows changes to the service provider without performing any code changes to the service consumers. The external configuration file can be modified with a configuration management tool such as Puppet or Chef [4](#fn:4).

[![Figure 4: Service Discovery; External Configuration File](https://systemdesign.one/what-is-service-discovery/service-discovery-configuration-file.webp)](https://systemdesign.one/what-is-service-discovery/service-discovery-configuration-file.webp "Figure 4: Service Discovery; External Configuration File")

Figure 4: Service Discovery; External Configuration File

The primary benefit of utilizing an external configuration file is the trivial implementation of service discovery [4](#fn:4). The downsides of this approach are as follows [2](#fn:2):

*   scalability problems when the count of service consumers or service providers increases
*   non-trivial implementation of heartbeats to support health checks

In summary, do not use an external configuration file to implement service discovery in a microservice architecture.

* * *

The Domain Name System (**DNS**) is a distributed database that supports service discovery via the resolution of service names to IP addresses [5](#fn:5). The primary difference between service discovery and DNS is that service discovery handles a dynamic number of service instances while DNS handles only a static number of service instances [1](#fn:1).

[![Figure 5: Service Discovery; DNS](https://systemdesign.one/what-is-service-discovery/service-discovery-dns.webp)](https://systemdesign.one/what-is-service-discovery/service-discovery-dns.webp "Figure 5: Service Discovery; DNS")

Figure 5: Service Discovery; DNS

DNS is a proven technology that works on a large [scale](https://newsletter.systemdesign.one/p/scalable-software-architecture) and provides the following benefits [12](#fn:12), [5](#fn:5):

*   reliability through replication
*   built-in cache support
*   trivial configuration

As everything comes with a price, DNS holds the following drawbacks [4](#fn:4):

*   offers only a crude interface to execute any updates
*   stale data due to multi-level [cache](https://newsletter.systemdesign.one/p/caching-patterns)
*   limited horizontal scalability of the system due to the delay in updating the state of a service

In summary, do not use DNS to build service discovery in a microservice architecture.

* * *

A load balancer can be introduced in front of each service provider to facilitate service discovery. The tradeoffs with this approach are the following [1](#fn:1):

*   slightly degraded latency due to an additional network hop
*   the load balancer becomes a single point of failure
*   increased system complexity due to numerous load balancers
*   increased effort for management of the load balancers

In summary, do not implement service discovery with load balancers in a scalable microservice architecture.

* * *

The service registry is a database that contains the locations of the instances by a service provider. The service registry is also known as a **discovery server**. The key idea behind the service registry is to use a distributed key-value store to store the service configuration and service locations. The simplest service registry can be implemented using a key-value store such as Redis [6](#fn:6).

The instances of a service provider must register to the service registry on startup. The service consumers query the service registry to identify the instances of a service provider [1](#fn:1). The service registry persists also information about invocation policies for each service provider [2](#fn:2). In conclusion, it is recommended to build service discovery with a service registry in a scalable microservice architecture.

* * *

* * *

The different patterns for service discovery are the following [6](#fn:6):

*   client-side service discovery
*   server-side service discovery

The service consumer determines the location of a service provider instance by directly querying the service registry. The service consumer performs load balancing through either a round-robin or a [consistent hashing](https://systemdesign.one/consistent-hashing-explained/) algorithm [6](#fn:6). The following is the workflow for client-side service discovery:

1.  the service provider registers to the service registry on the startup
2.  the service consumer performs a lookup operation on the service registry for the location of a service provider
3.  the service registry returns the location of a healthy instance
4.  the service consumer invokes the service instance

[![Figure 6: Client-Side Service Discovery](https://systemdesign.one/what-is-service-discovery/client-side-service-discovery.webp)](https://systemdesign.one/what-is-service-discovery/client-side-service-discovery.webp "Figure 6: Client-Side Service Discovery")

Figure 6: Client-Side Service Discovery

The benefits of client-side service discovery are as follows [8](#fn:8):

*   improved fault tolerance due to resilience against load balancer failures by caching service information on the client
*   slightly improved latency due to a decrease in the count of network hops

On the other hand, the limitations of client-side service discovery are the following [6](#fn:6):

*   increased client-side complexity
*   increased coupling between service discovery logic and service consumers causes difficulty to reimplement service discovery logic with different types of clients and frameworks

The [sidecar pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/sidecar) can be used to mitigate the coupling between the service consumers and service discovery logic.

* * *

The service discovery pattern typically used on a production system is server-side service discovery. The instances of a service provider are put behind the load balancer and the client requests are routed via the load balancer. The service configuration and service locations are stored in the service registry [6](#fn:6). The following is the workflow for server-side service discovery:

1.  the service provider registers with the service registry on the startup
2.  the service consumer executes a service request to the load balancer
3.  the load balancer performs a lookup operation for the service location on the service registry
4.  the service registry returns the list of healthy instances to the load balancer
5.  the load balancer forwards the request to an instance of the service provider based on the load-balancing algorithm

[![Figure 7: Server-Side Service Discovery](https://systemdesign.one/what-is-service-discovery/server-side-service-discovery.webp)](https://systemdesign.one/what-is-service-discovery/server-side-service-discovery.webp "Figure 7: Server-Side Service Discovery")

Figure 7: Server-Side Service Discovery

The advantages of server-side service discovery are the following [13](#fn:13):

*   trivial implementation
*   loose coupling between the service consumers and service providers
*   latency limits can be defined for smart request routing to healthy service instances

On the contrary, the limitations of server-side service discovery are increased system complexity and slightly degraded latency due to an additional network hop [6](#fn:6), [3](#fn:3).

* * *

* * *

* * *

**Download my system design playbook for free on newsletter signup:**

* * *

* * *

* * *

The registry database is the core of service discovery because the registry database stores information about all the available services in the system. The registry service encapsulates access to the registry database through a set of APIs. The registry service delivers the following benefits [2](#fn:2), [9](#fn:9):

*   abstracts the database schema and database interactions from the service consumers
*   minimizes the count of database connections to improve performance and throughput
*   support publish-subscribe model to inform service consumers about any service changes in near real-time

[![Figure 8: Service Discovery Architecture](https://systemdesign.one/what-is-service-discovery/service-discovery-architecture.webp)](https://systemdesign.one/what-is-service-discovery/service-discovery-architecture.webp "Figure 8: Service Discovery Architecture")

Figure 8: Service Discovery Architecture

Health checks can be configured against the service provider to improve reliability. The service registry must be replicated to avoid a single point of failure and to provide high availability. The popular implementations of the service registry are the following [6](#fn:6), [4](#fn:4), [13](#fn:13):

Tool

CAP Theorem

Consensus

Description

[Apache Zookeeper](https://zookeeper.apache.org/)

CP

Zab

Filesystem-like API

[CoreOS Etcd](https://etcd.io/)

CP

Raft

Key-value store with HTTP API

[Hashicorup Consul](https://www.consul.io/)

CP

Raft

[Gossip protocol](https://systemdesign.one/gossip-protocol/), RESTful API, key-value store

[Netflix Eureka](https://github.com/Netflix/eureka)

AP

\-

RESTful API, cached client that polls

* * *

* * *

Zookeeper supports Zab consensus protocol and provides a filesystem-like API.

[![Figure 9: Service Discovery; Apache Zookeeper](https://systemdesign.one/what-is-service-discovery/service-discovery-apache-zookeeper.webp)](https://systemdesign.one/what-is-service-discovery/service-discovery-apache-zookeeper.webp "Figure 9: Service Discovery; Apache Zookeeper")

Figure 9: Service Discovery; Apache Zookeeper

The following operations are executed when the service provider registers with the Zookeeper [14](#fn:14):

1.  Zab protocol is leveraged to attain a consensus on the current location and status of the service instance
2.  A parent node is created in Zookeeper to represent the service type
3.  Child nodes are created in Zookeeper to depict the service instances

Zookeeper nodes are ephemeral and support only rudimentary health checks [14](#fn:14).

* * *

* * *

The consul cluster consists of consul agents (**clients**) and consul servers. The consul agents are usually deployed alongside the service instances. The consul agent interacts with the consul server on behalf of the service instance. The consul agent is usually the API endpoint of the consul service. The service information is stored only by the consul server [4](#fn:4).

[![Figure 10: Service Discovery; Hashicorp Consul](https://systemdesign.one/what-is-service-discovery/service-discovery-consul.webp)](https://systemdesign.one/what-is-service-discovery/service-discovery-consul.webp "Figure 10: Service Discovery; Hashicorp Consul")

Figure 10: Service Discovery; Hashicorp Consul

The service consumer can query the consul agent over HTTP. The consul agent executes a periodic health check on the service provider to check whether the service instance is still healthy. The instance can also proactively push the health data to the consul agent or mark itself as unhealthy when there is no response received from the consul agent due to a network partition [4](#fn:4).

Consul supports Raft consensus protocol. The [gossip protocol](https://systemdesign.one/gossip-protocol/) is used by Consul to check the service membership status at a high scale [14](#fn:14). The consul agent can interact with any consul server over HTTP. Consul is also often used as a key-value store for service configurations. Consul supports a DNS interface beside an HTTP API interface to support service discovery with legacy services [15](#fn:15).

* * *

* * *

[Netflix](https://newsletter.systemdesign.one/p/how-does-netflix-work) Eureka consists of the Eureka server (service registry) and the Eureka client. The Eureka client simplifies the server interaction by handling load balancing and failover support. Eureka server offers a RESTful API and is typically deployed on Amazon Web Services (**AWS**) hyperscaler [16](#fn:16), [17](#fn:17).

[![Figure 11: Service Discovery; Netflix Eureka](https://systemdesign.one/what-is-service-discovery/service-discovery-netflix-eureka.webp)](https://systemdesign.one/what-is-service-discovery/service-discovery-netflix-eureka.webp "Figure 11: Service Discovery; Netflix Eureka")

Figure 11: Service Discovery; Netflix Eureka

Netflix Eureka is an optimal choice to implement client-side service discovery and client-side load balancing. The Eureka client caches the service registry to achieve high availability [8](#fn:8). The architecture of Eureka favors availability over [consistency](https://systemdesign.one/consistency-patterns/). Therefore, the staleness of the service registry should be expected by the client. The client must be ready to perform an automated failover due to the potential staleness of the registry to achieve improved reliability [9](#fn:9).

The service registry is replicated across multiple data centers for high availability and low latency. The registered service instances will send periodic heartbeat signals every thirty seconds. The service instance is automatically deregistered from the service registry if heartbeat signals are not received for a few minutes [8](#fn:8), [17](#fn:17).

* * *

* * *

The CoreOS’s Etcd is similar to Apache Zookeeper and forms a cluster through the Raft consensus protocol. Etcd is a key-value store and supports RPC API [14](#fn:14).

Alternatively, Conflict-free Replicated Data Type (**CRDT**) can be used to build an eventually consistent service discovery. The CRDT set data type can be used to persist the membership list. The [gossip protocol](https://systemdesign.one/gossip-protocol/) can be used to propagate the state of the application across the cluster [14](#fn:14).

* * *

* * *

The different techniques for service registration in service discovery are the following:

*   self-registration
*   third-party registration

A service instance must register and deregister on its own from the service registry. The self-registration service discovery approach keeps the system complexity low at the expense of increased coupling between the service instance and the service registry. Besides, the service registration logic must be reimplemented in different programming languages and frameworks in a [microservices](https://newsletter.systemdesign.one/p/prime-video-microservices) architecture.

* * *

A third-party library or service can be used to reduce the coupling between the service instances and the service registry. The third-party registration approach eliminates the need to reimplement registration logic in different programming languages and frameworks.

* * *

* * *

* * *

Service Discovery is a crucial aspect to implement the [microservices](https://newsletter.systemdesign.one/p/netflix-microservices) architecture. The service discovery enables loose coupling between the service provider and service consumers [5](#fn:5). Service discovery is implemented in internet-scale systems such as [Pastebin](https://systemdesign.one/system-design-pastebin/) and [URL shortener](https://systemdesign.one/url-shortening-system-design/).

* * *

* * *

* * *

**Download my system design playbook for free on newsletter signup:**

* * *

* * *

* * *

[CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/): This license allows reusers to copy and distribute the content in this article in any medium or format in unadapted form only, for noncommercial purposes, and only so long as attribution is given to the creator. The original article must be backlinked.

* * *

* * *

* * *

* * *

1.  Armon Dadgar, [Introduction to HashiCorp Consul with Armon Dadgar](https://www.youtube.com/watch?v=mxeMdl0KvBI) (2018), HashiCorp [↩︎](#fnref:1)
    
2.  Boris Lublinsky, [Implementing a Service Registry for .NET Web Services](https://www.infoq.com/articles/net-service-registry/) (2008), infoq.com [↩︎](#fnref:2)
    
3.  Kent Weare, [Amazon Introduces AWS Cloud Map: Service Discovery for Cloud Resources](https://www.infoq.com/news/2018/12/AWS-Cloud-MAP/) (2018), infoq.com [↩︎](#fnref:3)
    
4.  York Xyander, Bodo Junglas, [Resilience, Service Discovery and Zero Downtime Deployment in Microservice Architectures](https://www.infoq.com/presentations/microservices-zero-downtime/) (2015), infoq.com [↩︎](#fnref:4)
    
5.  Jan Algermissen, [Using DNS for REST Web Service Discovery](https://www.infoq.com/articles/rest-discovery-dns/) (2010), infoq.com [↩︎](#fnref:5)
    
6.  Ian Cooper, [Service Discovery and Clustering for .NET developers](https://www.infoq.com/presentations/brighter/) (2016), infoq.com [↩︎](#fnref:6)
    
7.  Ben Wilcock, [DIY SOA: How to build your own Simple Service Repository](https://www.infoq.com/articles/SimpleServiceRepository/) (2011), infoq.com [↩︎](#fnref:7)
    
8.  Karthikeyan Ranganathan, [Netflix Shares Cloud Load Balancing And Failover Tool: Eureka!](https://netflixtechblog.com/netflix-shares-cloud-load-balancing-and-failover-tool-eureka-c10647ef95e5) (2012), Netflix TechBlog [↩︎](#fnref:8)
    
9.  [Eureka 2.0 Architecture Overview](https://github.com/Netflix/eureka/wiki/Eureka-2.0-Architecture-Overview) (2015), GitHub.com [↩︎](#fnref:9)
    
10.  Matt Campbell, [Gremlin Adds Automated Service Discovery for Targeting Chaos Experiments](https://www.infoq.com/news/2021/05/gremlin-automated-service/) (2021), infoq.com [↩︎](#fnref:10)
     
11.  Steef-Jan Wiggers, [Google Introduces Service Directory to Manage All Your Services in One Place at Scale](https://www.infoq.com/news/2020/04/google-service-directory-beta/) (2020), infoq.com [↩︎](#fnref:11)
     
12.  Daniel Bryant, [Mesosphere Release Mesos-DNS Service Discovery for Apache Mesos](https://www.infoq.com/news/2015/01/mesos-dns-service-discovery/) (2015), infoq.com [↩︎](#fnref:12)
     
13.  Mike Amundsen, [Description, Discovery, and Profiles: A Primer](https://www.infoq.com/articles/description-discovery-profiles-primer/) (2015), infoq.com [↩︎](#fnref:13)
     
14.  Mushtaq Ahmed, Unmesh Joshi, [Service Discovery Using CRDTs](https://www.infoq.com/presentations/service-discovery-crdt/) (2018), infoq.com [↩︎](#fnref:14)
     
15.  Carlos Sanchez, [Service Discovery with Consul](https://www.infoq.com/news/2015/01/service-discovery-consul/) (2015), infoq.com [↩︎](#fnref:15)
     
16.  Abel Avram, [Netflix Open Sources Their AWS Service Registry, Eureka](https://www.infoq.com/news/2012/09/Eureka/) (2012), infoq.com [↩︎](#fnref:16)
     
17.  Abhijit Sarkar, [Spring Cloud Netflix Eureka - The Hidden Manual](https://blogs.asarkar.com/technical/netflix-eureka/) (2017), blogs.asarkar.com [↩︎](#fnref:17)
