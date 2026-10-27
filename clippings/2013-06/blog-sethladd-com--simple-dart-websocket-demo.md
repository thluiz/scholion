---
url: "http://blog.sethladd.com/2012/07/simple-dart-websocket-demo.html"
captured_at: "2013-06-25T10:01:17-03:00"
title: "Seth Ladd's Blog: Simple Dart + WebSocket demo"
domain: "blog-sethladd-com"
---

# **S**imple Dart + WebSocket demo

[EDIT: Updated on 2013-03-05]  
  
I just posted a [simple demo of Dart with WebSockets](https://github.com/sethladd/Dart-Web-Sockets) **.** Not only does it show how to connect to a [WebSocket](http://en.wikipedia.org/wiki/WebSocket)  server and send messages, it also shows off a few neat features of the [Dart language](http://www.dartlang.org/) **.**  
  
(The code follows below, or check out the full [open source project](https://github.com/sethladd/Dart-Web-Sockets) **.**)  
  
**Look mom, no classes**!****  
  
Dart is a class-based object oriented language, but that doesn't mean you are required to wrap everything in a class**.** No sir, this is Dart, not Java**.** In Dart, you can use top level functions and top level variables**.**  
  
**Libraries for modularity**  
  
Dart organizes code into libraries for modularity**.** For example, this code uses the dart:html library for the WebSocket code**.** Concerned about bloat here**?** Don't be! Thanks to tree-shaking, the code that you don't use is eliminated during a (optional) compile step**.** The Dart to JavaScript compiler uses tree shaking to help generate minimal JavaScript code (still more work to do here)**.** An upcoming Dart to Dart script will also generate a minimal Dart file for your app**.** So include all the libraries that you want, and stop worrying about how many bytes a dependencies adds**.**  
  
**Inline function definitions**  
  
Dart's syntax for inline function definitions is very handy for callbacks**.** For example, the code for the reconnection logic reads:  
  
new Timer(new Duration(seconds:retrySeconds),  
   () => initWebSocket(url, retrySeconds));  
  
**Optional parameters with default values**

Make function parameters optional by wrapping them in square brackets**.** In the code below, I made retrySeconds optional, with a default value of 2**.**  
  
**Main is where it starts**

I know where every Dart program starts**.** This might sound minor, but understanding the structure of your program is key for building larger apps**.** Look for the main() function to learn where the script begins**.**

**The code**

You can also check out the full [open source code for the Dart + WebSockets demo](https://github.com/sethladd/Dart-Web-Sockets) **.** Here's a snippet.

```
/*
 * See LICENSE file.
 */

import 'dart:html';
import 'dart:async';

WebSocket ws;

outputMsg(String msg) {
  var output = query('#output');
  output.text = "${output.text}\n${msg}";
}

void initWebSocket(String url, [int retrySeconds = 2]) {
  var encounteredError = false;
  
  outputMsg("Connecting to Web socket");
  ws = new WebSocket(url);
  
  ws.onOpen.listen((e) {
    outputMsg('Connected');
    ws.send('Hello from Dart!');
  });
  
  ws.onClose.listen((e) {
    outputMsg('web socket closed, retrying in $retrySeconds seconds');
    if (!encounteredError) {
      new Timer(new Duration(seconds:retrySeconds),
          () => initWebSocket(url, retrySeconds*2));
    }
    encounteredError = true;
  });
  
  ws.onError.listen((e) {
    outputMsg("Error connecting to ws");
    if (!encounteredError) {
      new Timer(new Duration(seconds:retrySeconds),
          () => initWebSocket(url, retrySeconds*2));
    }
    encounteredError = true;
  });
  
  ws.onMessage.listen((MessageEvent e) {
    outputMsg('received message ${e.data}');
  });
}

void main() {
  //initWebSocket('ws://echo.websocket.org');
  initWebSocket('ws://127.0.0.1:8889/ws');
}
```
