---
title: "Apache Thrift"
date: '2015-06-02T10:44:00-03:00'
category: webclip
summary: 'Apache Thrift is a framework for scalable cross-language services development. It combines a code generation engine with a software stack to build services and RPC clients and servers across many languages.'
tags: ["rpc", "code-generation", "cross-language", "services"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Apache Thrift - Home"
    url: "https://thrift.apache.org/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-06/thrift-apache-org--apache-thrift-home.md"
    kind: repo
---

Apache Thrift is presented as a software framework for scalable cross-language services development. It combines a software stack with a code generation engine so services can work efficiently across languages such as C++, Java, Python, PHP, Ruby, Erlang, Perl, Haskell, C#, Cocoa, JavaScript, Node.js, Smalltalk, OCaml, and Delphi.

## Reading notes

- Get started by downloading Thrift, building and installing the compiler, and creating a .thrift file.
- A thrift file is an interface definition made up of thrift types and services.
- The services defined in the file are implemented by the server and called by clients.
- The Thrift compiler generates source code from the thrift file for the client libraries and the server.
- The page points to a whitepaper for more information.
- The example shows that a definition file can describe data types and service interfaces.
- The compiler output is used to build RPC clients and servers that communicate across programming languages.
- The example emphasizes that Thrift reduces boilerplate for serialization, transport, and remote method calls.
- The snippet includes a service with methods such as ping, add, calculate, and a oneway void zip method.
