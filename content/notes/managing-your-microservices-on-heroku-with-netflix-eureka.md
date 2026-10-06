---
title: "Managing your Microservices on Heroku with Netflix's Eureka"
date: '2015-03-09T09:43:14-03:00'
category: webclip
summary: 'The article shows how to deploy Netflix Eureka on Heroku, register a microservice client, and add replica server instances for redundancy using Spring Cloud and Heroku config.'
tags: ["microservices", "eureka", "heroku", "spring-cloud"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Heroku | Managing your Microservices on Heroku with Netflix's Eureka"
    url: "https://blog.heroku.com/archives/2015/3/3/managing_your_microservices_on_heroku_with_netflix_s_eureka"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-03/blog-heroku-com--managing-your-microservices-on-heroku-with-netflix-eureka.md"
    kind: repo
---

The post explains that Netflix’s open source tools, especially Eureka, are aimed at microservices systems where many services need a way to find each other. Eureka acts as a service registry, keeping track of service metadata, health, availability, and registrations so clients can discover one another.

It then walks through deploying a Eureka server and a Eureka client on Heroku, setting config variables, and checking the dashboard and logs to confirm registration. It also shows how to add a peer profile so two Eureka server instances can replicate across regions, and notes that Spring Cloud also offers Hystrix, Ribbon, and Feign.

## Reading notes

- Netflix open sourced components such as Eureka for service discovery, Hystrix for service failure, and Ribbon for client-side load balancing.
- Spring Framework makes it easier to deploy Netflix OSS on Heroku while following Twelve Factor principles.
- Microservices split a large project into smaller, more manageable pieces.
- A Eureka server is a service registry where each microservice registers itself so consumers can find it.
- Eureka keeps service health, availability, and other metadata.
- The server demo is deployed on Heroku with Git deployment, a config variable for the user password, and a browser login.
- A Eureka client registers itself with the server, sends heartbeat messages, and is removed if heartbeats stop within the configured timetable.
- The client demo uses `EUREKA_URL` and `DOMAIN_NAME` config variables before deployment.
- The logs show the client registering successfully, and the dashboard then lists the service instance.
- Non-Spring clients can also use Netflix’s Eureka Client directly, with Scala examples mentioned in Atlas and IEP.
- Eureka keeps the registry in memory and clients also cache registrations in memory.
- Replication is configured with a new Spring profile called `peer` and a `Procfile` change.
- Two Heroku apps are created in different regions and pointed at each other with `EUREKA_PEER_URL`.
- Spring Cloud also provides Hystrix Clients, Hystrix Dashboard, Ribbon, and Feign for a broader microservices stack.
