---
title: "Multiplayer games room with F#, SignalR, Akka.Net and SAFE stack"
date: '2020-07-05T14:10:33+00:00'
category: webclip
summary: 'The author describes building a multiplayer games room with SAFE stack, using F# with SignalR for client-server communication and Akka.Net for a stateful game server.'
tags: ["fsharp", "signalr", "akka-net", "safe-stack"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Multiplayer games room with F#, SignalR, Akka.Net and SAFE stack"
    url: "https://chester.codes/games-room-fsharp-signalr-akka-net"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/chester-codes--multiplayer-games-room-fsharp-signalr-akka-net-safe-stack.md"
    kind: repo
---

The post says the project was a chance to try SAFE stack, F# with SignalR for client-server communication, and Akka.Net for a stateful game server. It presents the app as a multiplayer games room and walks through the main pieces of the stack.

## Reading notes

- Akka.Net is described as a .Net port of the Akka actor framework, used to manage concurrency, state, and fault tolerance.
- Actors communicate asynchronously with immutable messages and handle one message at a time.
- F# fits Akka.Net well because of default immutability, record types, and pattern matching over discriminated unions.
- The two libraries mentioned for working with Akka.Net are `Akka.FSharp` and `Akkling`.
- Akkling is said to offer slightly better type safety, though it does not work as well with some testing tools.
- The example actor receives a `Msg` union with `PrintInt` and `PrintString` cases and prints values to the console.
- An actor is created with `spawn`, a name, props, and an `ActorSystem`.
- `spawn` returns an `IActorRef<Msg>`, and the custom operator `<!` sends a `Msg` to the actor.
- The games room uses four actor types: GameHub, Group, Game, and ClientResponder.
- GameHub creates Group actors and handles incoming client messages.
- Group actors can send messages back to clients through ClientResponder or to the active Game actor.
- Messages are wrapped in envelopes with identifiers that route them to the right Group or Game actor.
- GameHub and ClientResponder are useful for testing because client messages can be simulated and responses can be routed to a `TestProbe`.
- SignalR is presented as a way to do client-server communication over websockets.
- F# makes it possible to use the same DTOs on client and server for complex objects.
- On the server side, SignalR setup is described as the same as C# and well documented.
- For F# objects to work well with SignalR, property names should use camelCase and DTOs should be simple records with `CLIMutable`.
- The author preferred non-native F# types where possible, such as `array` instead of `list`.
- They did not try to use discriminated unions for SignalR payloads.
- Sending an `int array` from the client required serializing it to a string because the Fable representation was a simple object rather than a JavaScript array.
- Client-side setup required building Fable bindings, and `ts2fable` provided a starting point.
- Send and response handling was not fully type-safe, but server responses could be cast to shared record types and dispatched into the Elmish update loop.
- The SAFE stack dotnet template is described as a good starting point for setup.
- The author first deployed to Azure App Service, then switched to a DigitalOcean droplet for cost reasons.
- A FAKE script was used to build and store a Docker container using Azure DevOps and Dockerhub.
- The author says they became a `paket` convert, though adding a package took longer than expected.
- The conclusion says the experience was pleasant and that the functional style helps express app intent and limit possible states.
- The author says using the same language on client and server was very cool, and only one null-based frontend error occurred.
- They also say `match` expressions on the client side felt like a game changer.
- The code took longer to write than a similar C#/JavaScript app, partly because of the quirks of combining the technologies.
- The author says better planning would have helped, since a better design was found halfway through frontend implementation and required major refactoring.
- The F# type system helped during that refactor.
- The site is available at `gamesroom.xyz`, and the code was open sourced on GitHub for feedback and constructive critique.
