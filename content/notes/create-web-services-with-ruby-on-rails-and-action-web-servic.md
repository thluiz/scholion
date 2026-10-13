---
title: "Create Web services with Ruby on Rails and Action Web Service"
date: '2012-06-27T13:51:21-03:00'
category: webclip
summary: 'The article shows how Action Web Service adds SOAP and XML-RPC support to Rails, explains API classes, dispatching modes, and client access, and walks through working examples.'
tags: ["ruby-on-rails", "web-services", "soap", "xml-rpc"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Create Web services with Ruby on Rails and Action Web Service"
    url: "http://www.ibm.com/developerworks/opensource/library/os-ws-rubyrails/index.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-06/ibm-com--create-web-services-with-ruby-on-rails-and-action-web-servic.md"
    kind: repo
---

The article explains how Action Web Service lets Ruby on Rails publish interoperable Web service APIs without dealing with protocol details. It presents SOAP and XML-RPC as the main protocols, then walks through examples that define API classes, controller classes, and service implementations.

It also covers direct, delegated, and layered dispatching, showing how each changes the way requests reach the method implementation. In the client section, it shows how a Rails application can call a remote Web service with `web_client_api` or with `ActionWebService::Client::Soap` and `ActionWebService::Client::XmlRpc`.

## Reading notes

- Action Web Service provides server-side Web services support in Rails for SOAP and XML-RPC.
- Rails applications can publish interoperable Web service APIs through an API class based on `ActionWebService::API::Base`.
- The example service uses an API class to declare `hello_message` with two string inputs and one string return value.
- The controller class holds the implementation of the Web service methods.
- `web_service_api` links a controller to an API class.
- `web_service_dispatching_mode :direct` sends calls straight to controller methods.
- Direct dispatching is the default and limits a controller to one API.
- `web_service_dispatching_mode :delegated` lets one controller attach more than one service class.
- `web_service_dispatching_mode :layered` prefixes method calls with the service name.
- `web_service_scaffold :invoke` generates a Web service interface for testing methods.
- The article shows a generated Hello service and a client Rails application that calls it.
- `web_client_api` creates a protected client method for invoking a remote Web service endpoint.
- The client example can also use `ActionWebService::Client::Soap` or `ActionWebService::Client::XmlRpc` directly.
- The client application submits a name through an RHTML form and displays the Web service output in another template.
