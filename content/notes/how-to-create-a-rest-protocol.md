---
title: "How to Create a REST Protocol"
date: '2013-02-20T10:11:05-03:00'
category: webclip
summary: 'The article says a REST protocol should be designed by identifying resources and URIs, choosing representations, mapping HTTP methods to CRUD-style actions, and listing expected status codes, using an employee list as the running example.'
tags: ["rest", "http", "web-services"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "XML.com: How to Create a REST Protocol"
    url: "http://www.xml.com/lpt/a/2004/12/01/restful-web.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-02/xml-com--how-to-create-a-rest-protocol.md"
    kind: repo
---

The article presents REST as an architectural style for building web services with web-like properties. It recommends a practical sequence for designing a protocol: define the resources and their URIs, choose the representations, decide which HTTP methods each URI supports, and specify the status codes that may be returned.

## Reading notes

- REST is described as an architectural style, understood as a coordinated set of architectural constraints.
- The article argues that REST can help with scalability, simpler implementation, and reuse.
- Each resource should have its own URI, and the text warns against using a single URI for everything.
- Collections and search interfaces are treated as possible resources in their own right.
- The example employee contact list assigns one URI per employee and one URI for all employees.
- The term for what a URI returns is representation, and the article focuses on XML as the format for the examples.
- For the employee example, the individual employee representation contains name, title, and contact information.
- The employee list representation contains references to employee URIs.
- The article uses the term dereferencing for accessing a resource through its URI.
- It limits the discussion to GET, POST, PUT, and DELETE, and relates them to CRUD.
- GET should be safe and idempotent, and should have no side effects.
- The mapping given is POST for create, GET for retrieve, PUT for update, and DELETE for delete.
- The employee example is paired with methods and representations in a table.
- The article says the expected status codes should also be listed so implementers know what to test for.
- It ends by noting that more topics remain, including compression, etags, caching, extensibility, idioms, and implementations.
