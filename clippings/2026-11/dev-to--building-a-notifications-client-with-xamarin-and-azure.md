---
url: "https://dev.to/azure/building-a-notifications-client-with-xamarin-and-azure-p6e"
captured_at: "2026-11-16T01:28:06+00:00"
title: "Building a notifications client with Xamarin and Azure"
domain: "dev-to"
---

## [](#intro)Intro

> **[Find the GitHub repository for this series here](https://github.com/lbugnion/sample-azure-xamarin-notifications)**.

I often find myself needing to send a notification to my mobile device, for example when a job finishes on Azure, when one of my computers at home is done doing something, or when I just want to send an alert when something changes in a system I am observing.

Normally I would go ahead and create a companion app for the system I am building, and then send notifications to this app, but sometimes it's really overkill to build a full-blown app for this. This is why I decided to build a generic notifications client that I can install on my phone.

What's really cool is that a lot of the development (with dotnet and Xamarin) can be done locally on my Surface Pro, which makes testing and debugging very much easier, before the services and applications are deployed to Azure and to my devices.

## [](#why-push-notifications-aka-why-not-signalr)Why Push Notifications? (aka why not SignalR?)

Why did I choose to use push notifications and not another messaging service like SignalR for example?

SignalR is an amazing feature that you can easily add to a Xamarin application [as shown in this sample](https://github.com/lbugnion/sample-xamarin-signalr). It is very well suited for high traffic, real-time communication. In our scenario, it doesn't quite fit, because we want the notifications to reach the device also when the application is not running, which is exactly what push notifications are made for. Also, even when the application is running, adding SignalR would be overkill because we don't really need real time, high traffic here. What we get from our watched systems is a notification from time to time, and even if this notification is delayed by a few seconds, it's not mission critical.

Finally the push notification system also includes retries, in case one device is offline for a period of time. This is very useful for our scenario too.

## [](#steps)Steps

I am planning to build this system in the following order:

### [](#step-0-specification)Step 0: Specification

In this step we will specify what we want the system to achieve, create a few sketches of the application and get ready :)

### [](#step-1-sending-a-notification-from-the-firebase-cloud-messaging)Step 1: Sending a notification from the Firebase Cloud Messaging

The first step will include:

*   Creating a new project in Google Firebase and setting up [Firebase Cloud Messaging (FCM)](http://gslb.ch/d426b).
*   Building a client app just here to receive the Push Notification and test that it works.
*   Test the notification with [with Postman](https://www.postman.com/).

### [](#step-2-sending-a-notification-from-azure-notification-hubbuildingnotificationsclient2md)Step 2: Sending a notification from Azure Notification Hub\](./building-notifications-client-2.md)

So far I hadn't worked directly with [Azure Notification Hub](http://gslb.ch/d425b) (I was using App Center, [but this is being retired](http://gslb.ch/d423b)), so I need to figure out how the Notification Hub works. Thankfully there is good documentation available. Here is what we'll do in this step:

*   Create a new Azure Notification Hub and connect it to FCM.
*   Test the setup by sending a push notification [with Postman](https://www.postman.com/).

### [](#step-3-build-the-endpoint-and-connect-to-notification-hub)Step 3: Build the endpoint and connect to Notification Hub.

Once we have the FCM project and the Notification Hub set up, we can build an [Azure Function](http://gslb.ch/d10b) to serve as the main endpoint for the notification system. The Azure Function will communicate with the Azure Notification Hub by means of an SDK for .NET. This includes:

*   Build the Azure Functions application locally.
*   Build a test request in Postman to try things out.
*   Create the Azure Functions application on Azure.
*   Publish the function to the Azure Functions application.

> Not started yet

### [](#step-sending-a-notification-from-the-windows-push-notification-services)Step: Sending a notification from the Windows Push Notification Services

> Not started yet.

### [](#step-show-the-new-notification-in-a-page-on-the-device)Step: Show the new notification in a page on the device.

> Not started yet.

### [](#step-save-the-notifications-in-cosmos-db)Step: Save the notifications in Cosmos DB.

> Not started yet.

### [](#step-get-the-notifications-from-cosmos-db-into-the-app)Step: Get the notifications from Cosmos DB into the app.

> Not started yet.

### [](#step-save-all-the-secrets-to-azure-keyvault)Step: Save all the secrets to Azure KeyVault.

> Not started yet

### [](#step-organize-the-notifications-in-the-app-in-pages)Step: Organize the notifications in the app in pages.

> Not started yet.

### [](#step-save-the-notifications-locally-synchronize)Step: Save the notifications locally (synchronize).

> Not started yet.

### [](#step-customize-the-application-with-icons-design-etc)Step: Customize the application with icons, design etc...

> Not started yet.

## [](#building-an-arm-deployment-template)Building an ARM deployment template

In order to allow people to use this on their own, I am also planning to prepare an ARM deployment template for the Azure components.

*   Azure Function connected to the Azure Functions application GitHub repo.
*   CosmosDB.
*   Notification Hub.
*   KeyVault for the connection strings and other secrets.

In addition I will write detailed description on how to create the Firebase Cloud Messaging project, and how to configure all the Azure pieces.

> **[Find the GitHub repository for this series here](https://github.com/lbugnion/sample-azure-xamarin-notifications)**.

**[Next article: Notifications Client Step 0: Specification](https://dev.to/azure/notifications-client-step-0-specification-527p)**

Happy coding!

Laurent
