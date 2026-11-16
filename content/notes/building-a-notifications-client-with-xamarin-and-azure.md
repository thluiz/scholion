---
title: "Building a notifications client with Xamarin and Azure"
date: '2020-07-05T14:10:33+00:00'
category: webclip
summary: 'The author plans a generic mobile notifications client, preferring push notifications over SignalR because the app should receive alerts even when closed and without real-time traffic needs.'
tags: ["push-notifications", "xamarin", "azure-notification-hub", "firebase-cloud-messaging"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building a notifications client with Xamarin and Azure"
    url: "https://dev.to/azure/building-a-notifications-client-with-xamarin-and-azure-p6e"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--building-a-notifications-client-with-xamarin-and-azure.md"
    kind: repo
---

The author wants a generic notifications client for his phone so he can receive alerts from systems he watches without building a full companion app each time. He also notes that much of the development with .NET and Xamarin can be done locally before deploying services to Azure and devices.

## Reading notes

- The client is meant to receive notifications for events like completed jobs on Azure, home computers finishing tasks, or changes in observed systems.
- Push notifications are preferred because they can reach the device when the app is not running.
- SignalR is described as a better fit for high-traffic, real-time communication, which this scenario does not need.
- Push notifications also provide retries if a device is offline for a period of time.
- The planned work starts with specification, then Firebase Cloud Messaging, then Azure Notification Hub, and then an Azure Function as the main endpoint.
- Later steps include Windows Push Notification Services, showing notifications in the app, saving them in Cosmos DB, getting them back into the app, storing secrets in Azure Key Vault, organizing notifications into pages, local synchronization, and customization.
- The author also plans an ARM deployment template for Azure Function, Cosmos DB, Notification Hub, and Key Vault.
