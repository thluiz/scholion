---
title: "How to Design Messages for gRPC Services in .NET Core"
date: '2020-02-22T12:11:43+00:00'
category: webclip
summary: 'The article explains how .proto files define gRPC service methods and message structures in .NET Core, how proto3 maps to generated C# classes, and how to evolve message schemas safely.'
tags: ["grpc", "dotnet-core", "protocol-buffers"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to Design Messages for gRPC Services in .NET Core -- Visual Studio Magazine"
    url: "https://visualstudiomagazine.com/articles/2020/01/06/defining-grpc-messages.aspx"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/visualstudiomagazine-com--how-to-design-messages-for-grpc-services-in-dotnet-core.md"
    kind: repo
---

The article explains that a gRPC service is defined in a .proto file, which specifies the service methods and the data structure of their parameters and return values. In proto3, messages are built from scalar types, collections, and maps, and Visual Studio generates C# classes from them. It also notes how .NET Core maps ProtoBuf types to .NET types, including ByteString for bytes fields and RepeatedField<T> for repeated fields.

It also covers how message definitions can evolve after deployment. New fields can be added without breaking older clients, but existing field numbers should not change or be reused. Because generated properties are not nullable and default values can hide removed fields, the article warns that bool fields are especially risky to remove. It ends by noting some efficiency limits on field positions and reserved field numbers.

## Reading notes

- A .proto file defines the gRPC service interface in a language-neutral format.
- The interface has two parts: the methods the service exposes and the data structure of the parameters and return values.
- Proto3 should be declared explicitly with `syntax = "proto3";` on the first non-empty line.
- ProtoBuf message fields use scalar types such as boolean, string, byte array, and numeric types, but there are no date or fixed decimal types.
- In .NET Core, message definitions become classes, and field names are converted into properties with uppercase initial letters and underscores removed.
- ProtoBuf `int32` maps to .NET `int`, `int64` maps to `long`, and `fixed32` maps to `uint`.
- `bytes` fields use the .NET `ByteString` type, which can be created with `ByteString.CopyFrom` and copied back with `CopyTo`.
- Repeated fields use `Google.Protobuf.RepeatedField<T>` and can be initialized with collection syntax or populated with `Add` methods.
- `map` fields become dictionary-like `MapField` collections with key and value types.
- Adding fields with new position numbers can be compatible with older clients because clients ignore fields not listed in their own .proto files.
- Existing field numbers should not be changed or reused.
- Generated properties default to zero values, empty strings, false, empty ByteString, or empty repeated and map collections when unset.
- Removing a field can be hard for clients to detect because a missing field and a default value can look the same.
- Positions 1 through 15 use less overhead than positions 16 through 2047, so keeping messages under 16 positions is presented as an efficiency tip.
- Field position numbers cannot be negative, zero, in the 19,000 to 19,999 reserved range, or above 536,870,911.
