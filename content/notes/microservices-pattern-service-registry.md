---
title: "Microservices Pattern: Service registry"
date: '2026-11-25T16:12:59+00:00'
category: webclip
summary: 'Describes the Service Registry pattern for tracking dynamic service instances and enabling client/server-side discovery, with examples and trade-offs.'
tags: ["microservices", "service-discovery", "service-registry", "infrastructure"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Microservices Pattern: Pattern: Service registry"
    url: "https://microservices.io/patterns/service-registry"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/microservices-io--microservices-pattern-service-registry.md"
    kind: repo
---

A service registry is presented as a key pattern for enabling both client-side and server-side service discovery when service instances change frequently. The registry stores services, their instances, and locations, and can validate instance health so that clients and routers can find endpoints reliably in dynamic environments.

## Reading notes

- Clients use client-side or server-side discovery to determine where to send requests for a given service.
- The core problem is how clients or routers learn which service instances exist and where they are located.
- Each service instance exposes a remote API, such as HTTP/REST or Thrift, bound to a specific host and port.
- The set of service instances and their IP/port locations changes over time, especially with VMs and containers that receive dynamic IPs.
- Autoscaling mechanisms like EC2 Auto Scaling Groups adjust the number of running instances based on load, further changing the instance pool.
- The solution is a service registry that maintains a database of services, instances, and their network locations.
- Service instances register with the registry when they start and deregister when they shut down.
- Clients and/or routers query the registry to obtain the list of currently available instances for a service.
- A registry can call each instance’s health check API to confirm that the instance can handle requests.
- The Microservices Example application uses client-side service discovery with Spring Boot and Spring Cloud as a microservice chassis.
- In that example, Netflix Eureka is used as the service registry provided by the Spring Cloud stack.
- The Eureka Server can be implemented as a small Spring Boot application annotated with `@SpringBootApplication` and `@EnableEurekaServer`.
- The Eureka Server example is packaged as a JAR and run via Java, and can be deployed as a Docker container exposing port 8761.
- Other technologies that can act as service registries include Apache Zookeeper, Consul, and Etcd.
- Some platforms such as Kubernetes, Marathon, and AWS ELB have an implicit service registry built into the infrastructure.
- A key benefit of a service registry is that clients and routers can discover where service instances are running.
- A drawback is that, when not provided by the platform, the registry becomes an extra infrastructure component to install, configure, and operate.
- Because the registry is a critical system component, its failure risks clients using stale cached data, so it must be highly available.
- Registration strategy must be chosen: either instances register themselves or a separate component handles registration.
- With the self-registration pattern, each service instance is responsible for registering and deregistering in the service registry.
- With the 3rd-party registration pattern, an external process or component registers service instances on their behalf.
- Clients that query the registry must know how to reach the registry instances themselves.
- Registry instances should run on fixed, well-known IP addresses so that clients can be configured with those addresses.
- Netflix Eureka in AWS is typically deployed using Elastic IP addresses reserved for the registry nodes.
- The pool of available Elastic IP addresses for Eureka can be configured using a properties file or DNS entries.
- When a Eureka instance starts, it uses configuration to select one of the available Elastic IP addresses.
- Eureka clients are configured with the same pool of Elastic IP addresses so they can connect to the registry.
- Client-side and server-side discovery mechanisms rely on a service registry to resolve service locations.
- Self-registration and 3rd-party registration are presented as the two main options for populating the registry with instances.
- The service registry may use a health check API on each instance to ensure that only healthy instances are advertised.
