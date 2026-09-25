---
title: "Twitter System Design Example for Tech Interviews"
date: '2026-09-25T01:04:31+01:00'
category: webclip
summary: 'Guia de system design para entrevistas que estrutura a criação de um Twitter/X.com em requisitos, estimativas de capacidade, APIs, banco de dados, arquitetura e trade-offs.'
tags: ["system-design", "twitter", "interview-prep"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Twitter System Design Example for Tech Interviews"
    url: "https://dev.to/somadevtoo/twitter-system-design-example-for-tech-interviews-1ihb?context=digest"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--twitter-system-design-example-for-tech-interviews.md"
    kind: repo
---

The post frames Twitter or X.com as a common system design interview problem and says the main challenge is explaining a structured design within 40 minutes. It walks through requirements, capacity estimation, QPS, API design, database design, storage, high-level architecture, detailed components, trade-offs, failure scenarios, and bottlenecks.

## Fichamento

- O texto apresenta Twitter ou X.com como um caso típico de entrevista de system design e insiste na necessidade de uma resposta estruturada para caber no tempo da conversa.
- Propõe um template para organizar a resposta e diz que seguir essa estrutura ajuda a articular melhor o raciocínio na entrevista.
- Nos requisitos funcionais, lista publicar tweets, seguir usuários e favoritar tweets.
- Nos requisitos não funcionais, destaca escalabilidade, alta disponibilidade e estabilidade.
- Na estimativa de capacidade, assume 500 milhões de usuários.
- A partir dessa base, estima 500 milhões de tweets por dia, 10 páginas de feed por usuário por dia, 100 seguidores em média por usuário e 5 favoritos por dia.
- Converte essas hipóteses em carga aproximada de 15k QPS para escrita, 75k QPS para leitura e 30k QPS para favoritos.
- Estima 140 GB de novos dados por dia para tweets e 10 TB por dia para mídia, chegando a 50 TB por ano para tweets e 4 PB por ano para mídia.
- Na API de tweeting, propõe um método para postar tweet com userId, texto, localização e data.
- Na API de follow, propõe métodos para seguir e deixar de seguir usuários.
- Na API de favorites, propõe métodos para favoritar e desfavoritar tweets.
- Para o feed, propõe uma API de obtenção de timelines com paginação.
- No banco de dados, define tabelas para informações de usuários, tweets e relações de seguidores.
- A tabela de usuários guarda userId, userName, status e outros dados de perfil.
- A tabela de tweets guarda tweetId, userId, conteúdo, postTime, modifyTime e status.
- A tabela de followers guarda userId, followerId e followedTime.
- Na camada de storage, sugere MySQL para dados estruturados e Amazon S3 para imagens e vídeos.
- Na arquitetura em alto nível, descreve clientes, load balancers, rate limiter, CDN, serviços de tweet, usuário, follow e feed, além de Redis, MySQL e S3 na camada de dados.
- No fluxo de requisição, a chamada passa pelo load balancer, segue para um servidor, passa pelo rate limiter, grava em MySQL e Redis e usa CDN para mídia nas leituras.
- No design detalhado, recomenda múltiplos load balancers em cluster e algoritmos como round-robin, least connections ou IP hash.
- Para CDN, sugere caching pull e push e ajuste de TTL para melhorar taxa de acerto.
- Para Redis, sugere cluster, replicação master-slave e Sentinel para failover.
- Para MySQL, sugere arquitetura master-slave e particionamento horizontal.
- Nos trade-offs, escolhe MySQL em vez de NoSQL por causa de consultas complexas e suporte a transações.
- Também escolhe Redis em vez de Memcached por causa de tipos de dados, recursos avançados e escalabilidade horizontal.
- Entre os cenários de falha, propõe modelo híbrido de pull e push para usuários que seguem muita gente.
- Para hotspots de leitura, recomenda cache em Redis com cache-aside e uso de cache local.
- Como melhoria futura, sugere estratégia multi-região active-active para disaster recovery e alta disponibilidade.
