---
url: "https://web.archive.org/web/20190515021401id_/http://www.fsharpreactivepatterns.com:80/system-management-and-infrastructure.html"
captured_at: "2026-11-16T07:52:58+00:00"
title: "System Management and Infrastructure"
domain: "web-archive-org"
---

For more details and full analysis of each pattern described in this section, please refer to **Chapter 10** of [Reactive Messaging Patterns with the Actor Model](http://www.informit.com/store/reactive-messaging-patterns-with-the-actor-model-applications-9780133846836) by [Vaughn Vernon](https://twitter.com/vaughnvernon).

## [Sections](#Sections)

1.  [Introduction](https://web.archive.org/web/20190515021401id_/http://www.fsharpreactivepatterns.com:80/index.html)
2.  [Messaging with Actors](https://web.archive.org/web/20190515021401id_/http://www.fsharpreactivepatterns.com:80/messaging-with-actors.html)
3.  [Messaging Channels](https://web.archive.org/web/20190515021401id_/http://www.fsharpreactivepatterns.com:80/messaging-channels.html)
4.  [Message Construction](https://web.archive.org/web/20190515021401id_/http://www.fsharpreactivepatterns.com:80/message-construction.html)
5.  [Message Routing](https://web.archive.org/web/20190515021401id_/http://www.fsharpreactivepatterns.com:80/message-routing.html)
6.  [Message Transformation](https://web.archive.org/web/20190515021401id_/http://www.fsharpreactivepatterns.com:80/message-transformation.html)
7.  [Message Endpoints](https://web.archive.org/web/20190515021401id_/http://www.fsharpreactivepatterns.com:80/message-endpoints.html)
8.  **System Management and Infrastructure**
    *   [Control Bus](#Control-Bus)
    *   [Detour](#Detour)
    *   [Wire Tap](#Wire-Tap)
    *   [Message Metadata/History](#Message-Metadata-History)
    *   [Message Journal/Store](#Message-Journal-Store)
    *   [Smart Proxy](#Smart-Proxy)
    *   [Test Message](#Test-Message)
    *   [Channel Purger](#Channel-Purger)

## [Control Bus](#Control-Bus)

The Control Bus pattern allows you to administer and control actors and messages.

1: 

```
// No code example
```

[Sections](#Sections)

## [Detour](#Detour)

This pattern enables re-routing messages to execute additional steps.

 1: 
 2: 
 3: 
 4: 
 5: 
 6: 
 7: 
 8: 
 9: 
10: 
11: 
12: 
13: 
14: 
15: 
16: 
17: 
18: 
19: 
20: 
21: 
22: 
23: 
24: 
25: 
26: 
27: 
28: 
29: 
30: 
31: 
32: 
33: 
34: 
35: 
36: 
37: 
38: 
39: 
40: 
41: 
42: 
43: 
44: 
45: 
46: 
47: 
48: 
49: 
50: 
51: 
52: 
53: 

```
let orderProcessor (mailbox: Actor<_>) =
    let rec loop () = actor {
        let! message = mailbox.Receive ()
        printfn "OrderProcessor: %A" message
        return! loop ()
    }
    loop ()

let messageDebugger next (mailbox: Actor<_>) =
    let rec loop () = actor {
        let! message = mailbox.Receive ()
        printfn "MessageDebugger: %A" message
        next <! message
        return! loop ()
    }
    loop ()

let messageTester next (mailbox: Actor<_>) =
    let rec loop () = actor {
        let! message = mailbox.Receive ()
        printfn "MessageTester: %A" message
        next <! message
        return! loop ()
    }
    loop ()

let messageValidator next (mailbox: Actor<_>) =
    let rec loop () = actor {
        let! message = mailbox.Receive ()
        printfn "MessageValidator: %A" message
        next <! message
        return! loop ()
    }
    loop ()

let messageLogger next (mailbox: Actor<_>) =
    let rec loop () = actor {
        let! message = mailbox.Receive ()
        printfn "MessageLogger: %A" message
        next <! message
        return! loop ()
    }
    loop ()

let orderProcessorRef = spawn system "orderProcessor" orderProcessor
let debuggerRef = spawn system "debugger" <| messageDebugger orderProcessorRef
let testerRef = spawn system "tester" <| messageTester debuggerRef
let validatorRef = spawn system "validator" <| messageValidator testerRef
let loggerRef = spawn system "logger" <| messageLogger validatorRef

let orderProcessorDetour = loggerRef // change to = orderProcessorRef to turn the Detour off

orderProcessorDetour <! ProcessOrder(Order)
```

[Complete Code](https://github.com/jorgef/fsharpreactivepatterns/blob/master/SystemManagementInfrastructure/Detour.fsx)

[Sections](#Sections)

## [Wire Tap](#Wire-Tap)

The Wire Tap pattern allows to inspect messages without altering its content and destination.

 1: 
 2: 
 3: 
 4: 
 5: 
 6: 
 7: 
 8: 
 9: 
10: 
11: 
12: 
13: 
14: 
15: 
16: 
17: 
18: 
19: 
20: 
21: 
22: 
23: 

```
let orderProcessor (mailbox: Actor<_>) =
    let rec loop () = actor {
        let! message = mailbox.Receive ()
        printfn "OrderProcessor: %A" message
        return! loop ()
    }
    loop ()

let messageLogger next (mailbox: Actor<_>) =
    let rec loop () = actor {
        let! message = mailbox.Receive ()
        printfn "MessageLogger: %A" message
        next <! message
        return! loop ()
    }
    loop ()

let orderProcessorRef = spawn system "orderProcessor" orderProcessor
let loggerRef = spawn system "logger" <| messageLogger orderProcessorRef

let orderProcessorWireTap = loggerRef

orderProcessorWireTap <! ProcessOrder(Order)
```

[Complete Code](https://github.com/jorgef/fsharpreactivepatterns/blob/master/SystemManagementInfrastructure/WireTap.fsx)

[Sections](#Sections)

## [Message Metadata/History](#Message-Metadata-History)

This pattern adds metadata and history to messages to provide tracking information.

 1: 
 2: 
 3: 
 4: 
 5: 
 6: 
 7: 
 8: 
 9: 
10: 
11: 
12: 
13: 
14: 
15: 
16: 
17: 
18: 
19: 
20: 
21: 
22: 
23: 
24: 
25: 
26: 
27: 
28: 
29: 
30: 
31: 
32: 
33: 
34: 
35: 
36: 
37: 
38: 
39: 

```
type Entry = { Who: Who; What: What; Where: Where; When: DateTimeOffset; Why: Why } with
    static member Create (who, what, where, ``when``, why) = { Who = who; What = what; Where = where; When = ``when``; Why = why }
    static member Create (who: Who, what: What, where: Where, why: Why) = Entry.Create (who, what, where, DateTimeOffset.UtcNow, why)
    static member Create (who, what, actorType, actorName, why) =  Entry.Create (Who who, What what, Where(actorType, actorName), Why why)
    member this.AsMetadata () = (Metadata.Create () : Metadata).Including this
and Metadata = { Entries: Entry list } with
    static member Create () = { Entries = [] }
    member this.Including entry = { Entries = this.Entries @ [entry] }
type SomeMessage = SomeMessage of payload: string * metadata: Metadata with
    static member Create payload = SomeMessage(payload, Metadata.Create ())
    member this.Including entry =
        let (SomeMessage(payload, metadata)) = this 
        SomeMessage(payload, metadata.Including entry)

let processor next (mailbox: Actor<SomeMessage>) =
    let random = Random()
    let user = sprintf "user%i" (random.Next 100)
    let wasProcessed = sprintf "Processed: %i" (random.Next 5)
    let because = sprintf "Because: %i" (random.Next 10)
    let entry = Entry.Create (Who user, What wasProcessed, Where("processor", mailbox.Self.Path.Name), DateTimeOffset.UtcNow, Why because)
    let report message heading = printfn "%s %s: %A" mailbox.Self.Path.Name (defaultArg heading "received") message
    
    let rec loop () = actor {
        let! message = mailbox.Receive ()
        report message None
        let nextMessage = message.Including entry
        match next with
        | Some next -> next <! nextMessage
        | None -> report nextMessage <| Some "complete"
        return! loop ()
    }
    loop ()

let processor3Ref = spawn system "processor3" <| processor None
let processor2Ref = spawn system "processor2" <| processor (Some processor3Ref)
let processor1Ref = spawn system "processor1" <| processor (Some processor2Ref)

let entry = Entry.Create (Who "driver", What "Started", Where("processor", "driver"), DateTimeOffset.UtcNow, Why "Running processors")
processor1Ref <! SomeMessage("Data...", entry.AsMetadata ())
```

[Complete Code](https://github.com/jorgef/fsharpreactivepatterns/blob/master/SystemManagementInfrastructure/MessageMetadataHistory.fsx)

[Sections](#Sections)

## [Message Journal/Store](#Message-Journal-Store)

This pattern records the delivered messages in a permanent location.

1: 

```
// No code example
```

[Sections](#Sections)

## [Smart Proxy](#Smart-Proxy)

The Smart Proxy pattern allows to track messages that are using the Return Address pattern.

 1: 
 2: 
 3: 
 4: 
 5: 
 6: 
 7: 
 8: 
 9: 
10: 
11: 
12: 
13: 
14: 
15: 
16: 
17: 
18: 
19: 
20: 
21: 
22: 
23: 
24: 
25: 
26: 
27: 
28: 
29: 
30: 
31: 
32: 
33: 
34: 
35: 
36: 
37: 
38: 
39: 
40: 
41: 
42: 
43: 
44: 
45: 
46: 
47: 
48: 
49: 
50: 
51: 
52: 
53: 
54: 
55: 
56: 
57: 
58: 
59: 
60: 
61: 
62: 
63: 
64: 
65: 
66: 
67: 
68: 
69: 
70: 

```
type ServiceRequest =
    | ServiceRequestOne of requestId : string
    | ServiceRequestTwo of requestId : string
    | ServiceRequestThree of requestId : string with
    member this.RequestId with get () = match this with | ServiceRequestOne requestId | ServiceRequestTwo requestId | ServiceRequestThree requestId -> requestId
type ServiceReply = 
    | ServiceReplyOne of replyId : string
    | ServiceReplyTwo of replyId : string
    | ServiceReplyThree of replyId : string with 
    member this.ReplyId with get () = match this with | ServiceReplyOne replyId | ServiceReplyTwo replyId | ServiceReplyThree replyId -> replyId 
type RequestService = RequestService of service: ServiceRequest

let serviceProvider (mailbox: Actor<_>) =
    let rec loop () = actor {
        let! message = mailbox.Receive ()
        match message with
        | ServiceRequestOne requestId -> mailbox.Sender () <! ServiceReplyOne requestId
        | ServiceRequestTwo requestId -> mailbox.Sender () <! ServiceReplyTwo requestId
        | ServiceRequestThree requestId -> mailbox.Sender () <! ServiceReplyThree requestId
        return! loop ()
    }
    loop ()

let serviceRequester serviceProvider (mailbox: Actor<_>) =
    let rec loop () = actor {
        let! message = mailbox.Receive ()
        match box message with
        | :? RequestService as request -> 
            printfn "ServiceRequester: %s: %A" mailbox.Self.Path.Name request
            let (RequestService service) = request
            serviceProvider <! service
        | reply -> printfn "ServiceRequester: %s: %A" mailbox.Self.Path.Name reply
        return! loop ()
    }
    loop ()

let serviceProviderProxy serviceProvider (mailbox: Actor<_>) =
    let analyzeReply reply = printfn "Reply analyzed: %A" reply
    let analyzeRequest request = printfn "Request analyzed: %A" request

    let rec loop requesters = actor {
        let! message = mailbox.Receive ()
        match box message with
        | :? ServiceRequest as request ->
            let requesters = requesters |> Map.add request.RequestId (mailbox.Sender ())
            serviceProvider <! request
            analyzeRequest request
            return! loop requesters
        | :? ServiceReply as reply -> 
            let requester = requesters |> Map.tryFind reply.ReplyId
            match requester with 
            | Some sender ->
                analyzeReply reply
                sender <! reply
                let requesters = requesters |> Map.remove reply.ReplyId
                return! loop requesters
            | None -> return! loop requesters
        | _ -> return! loop requesters
    }
    loop Map.empty

let serviceProviderRef = spawn system "serviceProvider" serviceProvider
let proxyRef = spawn system "proxy" <| serviceProviderProxy serviceProviderRef
let requester1Ref = spawn system "requester1" <| serviceRequester proxyRef
let requester2Ref = spawn system "requester2" <| serviceRequester proxyRef
let requester3Ref = spawn system "requester3" <| serviceRequester proxyRef

requester1Ref <! RequestService(ServiceRequestOne "1")
requester2Ref <! RequestService(ServiceRequestTwo "2")
requester3Ref <! RequestService(ServiceRequestThree "3")
```

[Complete Code](https://github.com/jorgef/fsharpreactivepatterns/blob/master/SystemManagementInfrastructure/SmartProxy.fsx)

[Sections](#Sections)

## [Test Message](#Test-Message)

This pattern allows to check the health of an actor.

 1: 
 2: 
 3: 
 4: 
 5: 
 6: 
 7: 
 8: 
 9: 
10: 
11: 
12: 
13: 
14: 
15: 
16: 
17: 
18: 
19: 
20: 

```
type Message = { IsTest: bool }

let inline (|TestMessage|_|) (message: 'a) = 
    let inline isTest (message: ^a) = (^a: (member get_IsTest: unit -> bool) (message))
    if (isTest message) then Some message else None

let processor (mailbox: Actor<Message>) =
    let rec loop () = actor {
        let! message = mailbox.Receive ()
        match message with
        | TestMessage message -> printfn "Test message: %A" message
        | message -> printfn "Production message: %A" message
        return! loop ()
    }
    loop ()

let processorRef = spawn system "processor" processor

processorRef <! { IsTest = true }
processorRef <! { IsTest = false }
```

[Complete Code](https://github.com/jorgef/fsharpreactivepatterns/blob/master/SystemManagementInfrastructure/TestMessage.fsx)

[Sections](#Sections)

## [Channel Purger](#Channel-Purger)

The Channel Purger pattern removes messages from an actor or Message Store.

 1: 
 2: 
 3: 
 4: 
 5: 
 6: 
 7: 
 8: 
 9: 
10: 
11: 
12: 
13: 
14: 
15: 
16: 
17: 
18: 
19: 
20: 
21: 
22: 
23: 
24: 
25: 
26: 
27: 

```
let orderProcessor (mailbox: Actor<_>) =
    let rec normal () = actor {
        let! message = mailbox.Receive ()
        match message with
        | ProcessOrder -> 
            printfn "Normal: %A" message
            return! normal ()
        | PurgeNow -> 
            printfn "Normal: %A" message
            return! purger ()
        | _ -> return! normal () }
    and purger () = actor {
        let! message = mailbox.Receive ()
        match message with
        | StopPurge -> 
            printfn "Purger: %A" message
            return! normal ()
        | _ -> return! purger ()
    }
    normal ()

let orderProcessorRef = spawn system "orderProcessor" orderProcessor

orderProcessorRef <! ProcessOrder
orderProcessorRef <! PurgeNow
orderProcessorRef <! StopPurge
orderProcessorRef <! ProcessOrder
```

[Complete Code](https://github.com/jorgef/fsharpreactivepatterns/blob/master/SystemManagementInfrastructure/ChannelPurger.fsx)

[Sections](#Sections)

val orderProcessor : mailbox:'a -> 'b

Full name: systemmanagementandinfrastructure.orderProcessor

val mailbox : 'a

val loop : (unit -> 'a)

val printfn : format:Printf.TextWriterFormat<'T> -> 'T

Full name: Microsoft.FSharp.Core.ExtraTopLevelOperators.printfn

val messageDebugger : next:'a -> mailbox:'b -> 'c

Full name: systemmanagementandinfrastructure.messageDebugger

val next : 'a

val messageTester : next:'a -> mailbox:'b -> 'c

Full name: systemmanagementandinfrastructure.messageTester

val messageValidator : next:'a -> mailbox:'b -> 'c

Full name: systemmanagementandinfrastructure.messageValidator

val messageLogger : next:'a -> mailbox:'b -> 'c

Full name: systemmanagementandinfrastructure.messageLogger

val orderProcessorRef : obj

Full name: systemmanagementandinfrastructure.orderProcessorRef

val debuggerRef : obj

Full name: systemmanagementandinfrastructure.debuggerRef

val testerRef : obj

Full name: systemmanagementandinfrastructure.testerRef

val validatorRef : obj

Full name: systemmanagementandinfrastructure.validatorRef

val loggerRef : obj

Full name: systemmanagementandinfrastructure.loggerRef

val orderProcessorDetour : obj

Full name: systemmanagementandinfrastructure.orderProcessorDetour

val orderProcessorWireTap : obj

Full name: systemmanagementandinfrastructure.orderProcessorWireTap

type Entry =  
  {Who: obj;  
   What: obj;  
   Where: obj;  
   When: obj;  
   Why: obj;}  
  member AsMetadata : unit -> Metadata  
  static member Create : who:'a0 \* what:'a1 \* where:'a2 \* why:'a3 -> 'a4  
  static member Create : who:'a0 \* what:'a1 \* where:'a2 \* when:'a3 \* why:'a4 -> Entry  
  static member Create : who:'a0 \* what:'a1 \* actorType:'a2 \* actorName:'a3 \* why:'a4 -> 'a5

Full name: systemmanagementandinfrastructure.Entry

Entry.Who: obj

Entry.What: obj

Entry.Where: obj

Entry.When: obj

Entry.Why: obj

static member Entry.Create : who:'a0 \* what:'a1 \* where:'a2 \* when:'a3 \* why:'a4 -> Entry

Full name: systemmanagementandinfrastructure.Entry.Create

val who : 'a

val what : 'a

val where : 'a

val why : 'a

static member Entry.Create : who:'a0 \* what:'a1 \* where:'a2 \* why:'a3 -> 'a4

Full name: systemmanagementandinfrastructure.Entry.Create

static member Entry.Create : who:'a0 \* what:'a1 \* where:'a2 \* why:'a3 -> 'a4  
static member Entry.Create : who:'a0 \* what:'a1 \* where:'a2 \* when:'a3 \* why:'a4 -> Entry  
static member Entry.Create : who:'a0 \* what:'a1 \* actorType:'a2 \* actorName:'a3 \* why:'a4 -> 'a5

static member Entry.Create : who:'a0 \* what:'a1 \* actorType:'a2 \* actorName:'a3 \* why:'a4 -> 'a5

Full name: systemmanagementandinfrastructure.Entry.Create

val actorType : 'a

val actorName : 'a

val this : Entry

member Entry.AsMetadata : unit -> Metadata

Full name: systemmanagementandinfrastructure.Entry.AsMetadata

type Metadata =  
  {Entries: Entry list;}  
  member Including : entry:Entry -> Metadata  
  static member Create : unit -> Metadata

Full name: systemmanagementandinfrastructure.Metadata

static member Metadata.Create : unit -> Metadata

Metadata.Entries: Entry list

type 'T list = List<'T>

Full name: Microsoft.FSharp.Collections.list<\_>

static member Metadata.Create : unit -> Metadata

Full name: systemmanagementandinfrastructure.Metadata.Create

val this : Metadata

member Metadata.Including : entry:Entry -> Metadata

Full name: systemmanagementandinfrastructure.Metadata.Including

val entry : Entry

Multiple items  
union case SomeMessage.SomeMessage: payload: string \* metadata: Metadata -> SomeMessage

\--------------------  
type SomeMessage =  
  | SomeMessage of payload: string \* metadata: Metadata  
  member Including : entry:Entry -> SomeMessage  
  static member Create : payload:string -> SomeMessage

Full name: systemmanagementandinfrastructure.SomeMessage

Multiple items  
val string : value:'T -> string

Full name: Microsoft.FSharp.Core.Operators.string

\--------------------  
type string = System.String

Full name: Microsoft.FSharp.Core.string

static member SomeMessage.Create : payload:string -> SomeMessage

Full name: systemmanagementandinfrastructure.SomeMessage.Create

val payload : string

val this : SomeMessage

member SomeMessage.Including : entry:Entry -> SomeMessage

Full name: systemmanagementandinfrastructure.SomeMessage.Including

val metadata : Metadata

member Metadata.Including : entry:Entry -> Metadata

val processor : next:'a -> mailbox:'b -> 'c

Full name: systemmanagementandinfrastructure.processor

val random : obj

val user : string

val sprintf : format:Printf.StringFormat<'T> -> 'T

Full name: Microsoft.FSharp.Core.ExtraTopLevelOperators.sprintf

val wasProcessed : string

val because : string

val entry : obj

val report : ('a -> string option -> unit)

val message : 'a

val heading : string option

val defaultArg : arg:'T option -> defaultValue:'T -> 'T

Full name: Microsoft.FSharp.Core.Operators.defaultArg

union case Option.None: Option<'T>

union case Option.Some: Value: 'T -> Option<'T>

val processor3Ref : obj

Full name: systemmanagementandinfrastructure.processor3Ref

val processor2Ref : obj

Full name: systemmanagementandinfrastructure.processor2Ref

val processor1Ref : obj

Full name: systemmanagementandinfrastructure.processor1Ref

val entry : obj

Full name: systemmanagementandinfrastructure.entry

type ServiceRequest =  
  | ServiceRequestOne of requestId: string  
  | ServiceRequestTwo of requestId: string  
  | ServiceRequestThree of requestId: string  
  member RequestId : string

Full name: systemmanagementandinfrastructure.ServiceRequest

union case ServiceRequest.ServiceRequestOne: requestId: string -> ServiceRequest

union case ServiceRequest.ServiceRequestTwo: requestId: string -> ServiceRequest

union case ServiceRequest.ServiceRequestThree: requestId: string -> ServiceRequest

val this : ServiceRequest

member ServiceRequest.RequestId : string

Full name: systemmanagementandinfrastructure.ServiceRequest.RequestId

val requestId : string

type ServiceReply =  
  | ServiceReplyOne of replyId: string  
  | ServiceReplyTwo of replyId: string  
  | ServiceReplyThree of replyId: string  
  member ReplyId : string

Full name: systemmanagementandinfrastructure.ServiceReply

union case ServiceReply.ServiceReplyOne: replyId: string -> ServiceReply

union case ServiceReply.ServiceReplyTwo: replyId: string -> ServiceReply

union case ServiceReply.ServiceReplyThree: replyId: string -> ServiceReply

val this : ServiceReply

member ServiceReply.ReplyId : string

Full name: systemmanagementandinfrastructure.ServiceReply.ReplyId

val replyId : string

Multiple items  
union case RequestService.RequestService: service: ServiceRequest -> RequestService

\--------------------  
type RequestService = | RequestService of service: ServiceRequest

Full name: systemmanagementandinfrastructure.RequestService

val serviceProvider : mailbox:'a -> 'b

Full name: systemmanagementandinfrastructure.serviceProvider

val serviceRequester : serviceProvider:'a -> mailbox:'b -> 'c

Full name: systemmanagementandinfrastructure.serviceRequester

val serviceProvider : 'a

val box : value:'T -> obj

Full name: Microsoft.FSharp.Core.Operators.box

val serviceProviderProxy : serviceProvider:'a -> mailbox:'b -> 'c

Full name: systemmanagementandinfrastructure.serviceProviderProxy

val analyzeReply : ('a -> unit)

val reply : 'a

val analyzeRequest : ('a -> unit)

val request : 'a

val loop : ('a -> 'b)

val requesters : 'a

Multiple items  
module Map

from Microsoft.FSharp.Collections

\--------------------  
type Map<'Key,'Value (requires comparison)> =  
  interface IEnumerable  
  interface IComparable  
  interface IEnumerable<KeyValuePair<'Key,'Value>>  
  interface ICollection<KeyValuePair<'Key,'Value>>  
  interface IDictionary<'Key,'Value>  
  new : elements:seq<'Key \* 'Value> -> Map<'Key,'Value>  
  member Add : key:'Key \* value:'Value -> Map<'Key,'Value>  
  member ContainsKey : key:'Key -> bool  
  override Equals : obj -> bool  
  member Remove : key:'Key -> Map<'Key,'Value>  
  ...

Full name: Microsoft.FSharp.Collections.Map<\_,\_>

\--------------------  
new : elements:seq<'Key \* 'Value> -> Map<'Key,'Value>

val add : key:'Key -> value:'T -> table:Map<'Key,'T> -> Map<'Key,'T> (requires comparison)

Full name: Microsoft.FSharp.Collections.Map.add

val tryFind : key:'Key -> table:Map<'Key,'T> -> 'T option (requires comparison)

Full name: Microsoft.FSharp.Collections.Map.tryFind

val remove : key:'Key -> table:Map<'Key,'T> -> Map<'Key,'T> (requires comparison)

Full name: Microsoft.FSharp.Collections.Map.remove

val empty<'Key,'T (requires comparison)> : Map<'Key,'T> (requires comparison)

Full name: Microsoft.FSharp.Collections.Map.empty

val serviceProviderRef : 'a

Full name: systemmanagementandinfrastructure.serviceProviderRef

val proxyRef : 'a

Full name: systemmanagementandinfrastructure.proxyRef

val requester1Ref : 'a (requires member ( <! ))

Full name: systemmanagementandinfrastructure.requester1Ref

val requester2Ref : 'a (requires member ( <! ))

Full name: systemmanagementandinfrastructure.requester2Ref

val requester3Ref : 'a (requires member ( <! ))

Full name: systemmanagementandinfrastructure.requester3Ref

type Message =  
  {IsTest: bool;}

Full name: systemmanagementandinfrastructure.Message

Message.IsTest: bool

type bool = System.Boolean

Full name: Microsoft.FSharp.Core.bool

val message : 'a (requires member get\_IsTest)

val isTest : ('a -> bool) (requires member get\_IsTest)

type unit = Unit

Full name: Microsoft.FSharp.Core.unit

val processor : mailbox:'a -> 'b

Full name: systemmanagementandinfrastructure.processor

active recognizer TestMessage: 'a -> 'a option

Full name: systemmanagementandinfrastructure.( |TestMessage|\_| )

val processorRef : 'a (requires member ( <! ))

Full name: systemmanagementandinfrastructure.processorRef

val normal : (unit -> 'a)

val purger : (unit -> 'a)

val orderProcessorRef : 'a (requires member ( <! ) and member ( <! ) and member ( <! ) and member ( <! ))

Full name: systemmanagementandinfrastructure.orderProcessorRef
