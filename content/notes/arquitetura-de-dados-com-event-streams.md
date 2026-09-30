---
title: "Arquitetura de Dados com Event Streams"
date: '2021-02-13T08:41:35-03:00'
category: webclip
summary: 'O texto explica stream processing, brokers, append-only logs e Apache Kafka, e mostra como CDC e event sourcing ligam um banco OLTP a sistemas derivados em tempo real.'
tags: ["event-streams", "apache-kafka", "change-data-capture", "event-sourcing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Arquitetura de Dados com Event Streams | by Breno Ferreira | Feb, 2021 | Medium"
    url: "https://brenocferreira.medium.com/arquitetura-de-dados-com-event-streams-7361dd69438d"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2021-02/brenocferreira-medium-com--arquitetura-de-dados-com-event-streams.md"
    kind: repo
---

O texto compara batch processing e stream processing e apresenta eventos como mensagens entre processos ou como registros que guardam mudanças de estado. A partir daí, descreve brokers de mensagem, append-only logs e Kafka como base para distribuir mudanças de dados em tempo real e manter histórico consultável.

## Fichamento

- Em batch processing, os dados já foram salvos e o processamento termina; em stream processing, os dados são contínuos e o processamento não se completa.
- Eventos podem ser vistos como mensagens entre processos ou como dados persistidos que registram mudanças de estado de uma aplicação.
- Sistemas de mensageria servem como buffer entre serviços quando a comunicação direta via REST ou RPC sofre falhas, excesso de requisições ou risco de perda de dados.
- A durabilidade depende do tipo de armazenamento do broker: alguns guardam mensagens em memória, enquanto outros persistem em disco, banco ou log.
- Em pub-sub, vários consumers assinam um tópico e processam a mesma mensagem; em message queue, um único consumer processa a mensagem.
- Message brokers são voltados para entrega rápida, e as mensagens costumam ser apagadas depois da confirmação de processamento.
- Um append-only log guarda mensagens no fim da estrutura, permite leitura sequencial e pode ser particionado para escalar, como no Apache Kafka.
- Com partitions e offsets, consumers podem ler o log inteiro ou começar a leitura em um ponto específico.
- Bancos OLTP, caches, bancos OLAP e índices full-text resolvem problemas diferentes, mas precisam manter os dados sincronizados entre si.
- O write-ahead log do banco pode ser usado como base para Change Data Capture, com o Kafka distribuindo mudanças em tempo real para outros sistemas.
- Debezium lê o WAL de bancos como MySQL e escreve as mudanças em tópicos Kafka, que depois alimentam outros consumers e sistemas derivados.
- Event Sourcing aparece como uma forma de armazenar eventos de mudança de estado e reconstruir a visão recente de uma entidade a partir deles.
- O texto relaciona CDC, CQRS e Event Sourcing ao uso do banco OLTP como fonte de comandos e queries, enquanto o Kafka distribui os eventos para representações derivadas.
- Em tópicos append-only, apagar mensagens individuais não é simples, o que entra em conflito com exigências de privacidade como LGPD e GDPR.
- O Kafka usa compactação de log para remover dados antigos e versões marcadas como removidas, mas apagar cópias distribuídas continua difícil.
- Em sistemas distribuídos, falhas de cliente, servidor ou rede levam a retries, o que pode causar perda de dados ou duplicação.
- At most once pode perder dados; at least once pode duplicar mensagens; exactly once é difícil de garantir.
- O Kafka usa append idempotente com sequence number e producer id para detectar duplicações, e também oferece transações com atomic commit entre partições e tópicos.
