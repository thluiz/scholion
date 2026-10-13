---
title: "Part 9 - Introduction to Web Services"
date: '2013-08-05T13:54:00-03:00'
category: webclip
summary: 'The page surveys Xamarin options for consuming REST, SOAP, and WCF services, then shows request, parsing, async, proxy, and security patterns with code samples.'
tags: ["xamarin", "web-services", "rest", "soap"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Part 9 - Introduction to Web Services | xamarin"
    url: "http://docs.xamarin.com/guides/cross-platform/application_fundamentals/introduction_to_web_services"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-08/docs-xamarin-com--introduction-to-web-services-xamarin.md"
    kind: repo
---

The page outlines how Xamarin mobile apps can integrate with web services when cloud-dependent apps need remote data. It groups the topic into REST, SOAP, and WCF support, then shows request, parsing, async, proxy, and security patterns.

## Reading notes

- Xamarin supports built-in and third-party APIs for RESTful, SOAP, and WCF services.
- REST is presented as a common choice because it is simple, platform agnostic, and cacheable over HTTP.
- The article compares HttpWebRequest, WebClient, RestSharp, Hammock, NSURLConnection, and ServiceStack for REST requests.
- Synchronous service calls block the main UI thread, so async calls and main-thread callbacks are recommended.
- REST responses can be deserialized with System.Xml, System.Json, Json.NET, or ServiceStack.Text.
- XML examples use LINQ to XML to populate C# objects from response data.
- JSON examples show key-value access with JsonObject, ServiceStack.Text, and JSON.NET.
- SOAP 1.1 and ASMX services are supported over HTTP.
- SOAP use starts with generating a proxy from WSDL in Xamarin Studio or by adding an existing proxy to a project.
- Async SOAP calls can use Begin and End methods or Completed event handlers, and event handlers should be unsubscribed when done.
- Xamarin.iOS supports WCF client-side use for common Silverlight-style bindings such as BasicHttpBinding.
- WCF proxy generation uses SLSvcUtil on Windows, and the generated files are then added to the Mac project.
- WCF configuration can set endpoint address, binding options, timeouts, SSL certificate validation, and HTTP basic credentials.
- The sample service section shows sharing server-side models with a client and deserializing a REST response into a User object.
