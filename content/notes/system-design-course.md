---
title: "GitHub - karanpratapsingh/system-design: Learn how to design systems at scale and prepare for system design interviews"
date: '2026-09-25T08:56:35+01:00'
category: webclip
summary: 'Course outline on system design covering networking, storage, databases, distributed systems, APIs, messaging, security, and interview patterns, plus worked designs for URL shortener, WhatsApp, Twitter, Netflix, and Uber.'
tags: ["system-design", "distributed-systems", "databases", "system-design-interviews"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "GitHub - karanpratapsingh/system-design: Learn how to design systems at scale and prepare for system design interviews"
    url: "https://github.com/karanpratapsingh/system-design?utm_source=weeklyfoo&utm_medium=email&utm_campaign=weeklyfoo"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/github-com--system-design-course.md"
    kind: repo
---

The page presents a course on system design and organizes it from fundamentals to interview-oriented case studies. It covers networking basics, storage, caching, load balancing, databases, distributed systems, APIs, messaging, security, and scaling concepts, then applies them to URL shortener, WhatsApp, Twitter, Netflix, and Uber designs.

## Fichamento

- O curso começa definindo system design como o processo de definir arquitetura, interfaces e dados para um sistema que atenda requisitos específicos.
- A estrutura do conteúdo inclui capítulos sobre rede, armazenamento, bancos de dados, arquitetura distribuída, comunicação entre serviços, segurança e entrevistas de system design.
- O material explica IP, modelo OSI, TCP e UDP, DNS, balanceamento de carga, clustering, cache, CDN e proxy.
- Também trata de disponibilidade, escalabilidade, armazenamento e conceitos como RAID, volumes, file storage, block storage, object storage, NAS e HDFS.
- Na parte de bancos de dados, distingue SQL e NoSQL, discute replicação, índices, normalização, desnormalização, ACID, BASE, CAP, PACELC, transações, transações distribuídas, sharding, consistent hashing e federation.
- A seção de arquitetura aborda N-tier, message brokers, message queues, publish-subscribe, ESB, monólitos e microservices, event-driven architecture, event sourcing, CQRS, API gateway, REST, GraphQL, gRPC e meios de comunicação em tempo real como long polling, WebSockets e SSE.
- O texto também cobre geohashing, quadtrees, circuit breaker, rate limiting, service discovery, SLA, SLO, SLI, disaster recovery, VMs, containers, OAuth 2.0, OIDC, SSO, SAML, SSL, TLS e mTLS.
- A parte de entrevistas recomenda clarificar requisitos funcionais, não funcionais e estendidos, estimar escala, desenhar modelo de dados, definir APIs, montar componentes de alto nível e identificar gargalos.
- O exemplo de URL shortener define requisitos de geração de alias curto, redirecionamento, expiração, prevenção de abuso e analytics, além de discutir Base62, MD5, counter, Key Generation Service e cache.
- O exemplo de WhatsApp descreve chat um-a-um, grupos, compartilhamento de arquivos, receipts, last seen, push notifications, WebSockets, presença, media service, object storage, CDN e API gateway.
- O exemplo de Twitter inclui postagens, follow, newsfeed, busca, retweets, favoritos, ranking, fan-out, Elasticsearch, Kafka, Spark, cache, media storage e CDN.
- O exemplo de Netflix trata de streaming, upload, busca, comentários, processamento de vídeo, transcoding, qualidade, HLS, CDN, geo-blocking, recomendações e analytics.
- O exemplo de Uber aborda busca por cabs próximos, booking, live location, geohashing, quadtrees, surge pricing, pagamentos, notificações, sharding e cache.
