---
title: "Using CockroachDB CDC With Azure Event Hubs"
date: '2026-09-25T08:29:33+01:00'
category: webclip
summary: 'The page shows how to send CockroachDB changefeeds to Azure Event Hubs by setting up Event Hubs, enabling enterprise changefeeds, configuring Kafka protocol details, and verifying messages in Azure.'
tags: ["cockroachdb", "azure-event-hubs", "changefeeds", "cdc"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Using CockroachDB CDC With Azure Event Hubs"
    url: "https://dzone.com/articles/using-cockroachdb-cdc-with-azure-event-hubs"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dzone-com--using-cockroachdb-cdc-with-azure-event-hubs.md"
    kind: repo
---

The page walks through a workaround for using CockroachDB enterprise changefeeds with Azure Event Hubs while official integration is still in progress. It covers creating Event Hubs resources, enabling changefeeds in CockroachDB, URL-encoding the SAS connection string, and pointing a changefeed at the Event Hubs Kafka endpoint.

## Fichamento

- O texto propõe um caminho provisório para integrar CockroachDB com Azure Event Hubs enquanto a integração oficial ainda está em fase inicial.
- Para usar CDC, o texto diz que é preciso uma licença enterprise, um cluster dedicado ou billing habilitado no CockroachDB Serverless.
- Os passos gerais são implantar Azure Event Hubs, implantar um cluster CockroachDB com enterprise changefeeds e verificar o resultado.
- Na criação do Event Hubs, o texto orienta abrir uma conta, criar resource group, namespace, Event Hub e uma SAS policy.
- O artigo trata Event Hubs como equivalente à criação de tópicos em Kafka para fins de configuração.
- No CockroachDB, o texto manda habilitar `kv.rangefeed.enabled` para ativar CDC.
- A conexão com Event Hubs usa o endpoint Kafka em `9093`, `sasl_user` definido como `$ConnectionString` e `sasl_password` como a connection string inteira URL-encoded.
- O exemplo de changefeed usa `CREATE CHANGEFEED FOR TABLE history INTO` um endereço `kafka://...` com TLS, SASL e formato JSON.
- Depois, o texto gera carga com o workload TPC-C do Cockroach para produzir dados de teste.
- A verificação é feita no portal da Azure, observando os contadores de mensagens e usando a opção de processar dados com insights em tempo real para visualizar as mensagens.
