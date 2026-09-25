---
title: "Using CockroachDB CDC With Azure Event Hubs"
date: '2026-09-25T08:29:33+01:00'
category: webclip
summary: 'The page shows how to send CockroachDB changefeeds to Azure Event Hubs by setting up Event Hubs, enabling enterprise changefeeds, configuring Kafka protocol details, and verifying messages in Azure.'
tags: ["cockroachdb","azure-event-hubs","changefeeds","cdc"]
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

## Reading notes

- The text proposes a provisional way to integrate CockroachDB with Azure Event Hubs while the official integration is still in its initial phase.
- To use CDC, the text says that an enterprise license, a dedicated cluster, or billing enabled in CockroachDB Serverless is required.
- The general steps are to deploy Azure Event Hubs, deploy a CockroachDB cluster with enterprise changefeeds, and verify the result.
- When creating Event Hubs, the text instructs you to open an account, create a resource group, a namespace, an Event Hub, and a SAS policy.
- The article treats Event Hubs as equivalent to creating topics in Kafka for configuration purposes.
- In CockroachDB, the text says to enable `kv.rangefeed.enabled` to activate CDC.
- The connection to Event Hubs uses the Kafka endpoint on `9093`, `sasl_user` set as `$ConnectionString`, and `sasl_password` as the entire URL-encoded connection string.
- The changefeed example uses `CREATE CHANGEFEED FOR TABLE history INTO` a `kafka://...` address with TLS, SASL, and JSON format.
- Then, the text generates load with the Cockroach TPC-C workload to produce test data.
- Verification is done in the Azure portal, observing message counters and using the process data with real-time insights option to view the messages.
