---
url: "https://hashrocket.com/blog/posts/implementing-video-chat-in-a-phoenix-application-with-webrtc"
captured_at: "2016-03-11T17:51:57-03:00"
title: "Implementing Video Chat in a Phoenix Application with WebRTC"
domain: "hashrocket-com"
---

# Implementing Video Chat in a Phoenix Application with WebRTC

In this blog post we’re going to cover how to implement video chat in a Phoenix application with WebRTC. By the end of this post we will have enabled two remote clients to connect with each other and engage in a video conversation.

We will use Phoenix channels to communicate messages between our two clients so they can establish a remote peer connection. WebRTC allows clients to establish a direct peer to peer connection with each other, but before they can establish this connection they need to communicate certain information about themselves, and this is what our Phoenix channels will facilitate. For a more in-depth explanation of how WebRTC works, visit <https://www.html5rocks.com/en/tutorials/webrtc/basics>.

To begin, let’s create a new app (Note that we will be using Phoenix version 1.0.2. For install instructions visit <https://www.phoenixframework.org/docs/installation>).

```
mix phoenix.new video_chat
```

Let’s first create a basic call controller to handle our requests.

```
 controllerscall_controller

defmodule VideoChatCallController 
   VideoChat :controller

   index _params 
    render  index
  end
end
```

Then we’ll need to create a corresponding call view to render our template.

```
 viewscall_view

defmodule VideoChatCallView 
   VideoChat :view
```

For our template we will just include two video elements, one for the local stream and another for the remote stream. We will also need some buttons to invoke our actions.

```
<!--  web/templates/call/index.html.eex -->

<div>
  <video “localVideo" autoplay></video>
  <video “remoteVideo" autoplay></video>

  <button “connect”Connect</button>
  <button "call"Call</button>
  <button "hangup"Hangup</button>
</div>
```

Next we need to update our router to redirect to our call controller. Change the root path from PageController to CallController.

```
 router

  CallController :index
```

Now we can run mix phoenix.server and navigate to localhost:4000 to make sure our template is rendering correctly.

With that in place we are ready to set up our channel. Create a call channel with a join/3 function to allow clients to join the channel, as well as a handle\_in/3 function to handle incoming events.

```
  channelscall_channel

defmodule VideoChatCallChannel 
   PhoenixChannel

   call" _auth_msg socket 
     socket
  

   handle_inmessage" body" =>  socket 
    broadcast! socket message" body: 
    :noreply socket
```

Next we need to define our call channel in our socket handler. Add the following line to web/channels/user\_socket.ex.

```
 channelsuser_socket

channel call" VideoChatCallChannel
```

Now we are just about ready to implement our JavaScript code to enable our clients to establish a connection. First add the following line to our application template to enable our WebRTC methods to work across different browsers (Chrome, Firefox, and Opera all currently support WebRTC).

```
<!-- web/templates/layout/app.html.eex -->

<script "//cdn.temasys.com.sg/adapterjs/0.10.x/adapter.debug.js"></script>
```

For this example we will put our JavaScript code in app.js. Let’s first import our socket and then establish a connection with our call channel.

```
// web/static/js/app.js

import socket  "./socket"

 channel  socketchannel"call" 
channel
  receive  =>  console"Successfully joined call channel" 
  receive"error"  =>  console"Unable to join"
```

Note that our socket is imported from web/static/js/socket.js. If you take a look at that file you will see that is where our socket is created and connected. You can also comment out or delete the code attempting to join a new channel since we have implemented that on our own.

Now we can wire up our buttons.

```
//  web/static/js/app.js

 localStream peerConnection
 localVideo  documentgetElementById"localVideo"
 remoteVideo  documentgetElementById"remoteVideo"
 connectButton  documentgetElementById"connect"
 callButton  documentgetElementById"call"
 hangupButton  documentgetElementById"hangup"

hangupButtondisabled  
callButtondisabled  
connectButtononclick  connect
callButtononclick  
hangupButtononclick  hangup
```

And then begin to define how our clients will establish their connections.

```
// web/static/js/app.js

function connect 
  console"Requesting local stream"
  navigatorgetUserMediaaudio video gotStream error => 
       console"getUserMedia error: " error
```

Here we are using the getUserMedia function to capture our local video stream and then call the callback function gotStream.

```
// web/static/js/app.js

function gotStreamstream 
   console"Received local stream"
   localVideo  createObjectURLstream
   localStream  stream
   setupPeerConnection
```

In gotStream we are setting our local stream and then calling setupPeerConnection.

```
// web/static/js/app.js

function setupPeerConnection 
  connectButtondisabled  
  callButtondisabled  false
  hangupButtondisabled  false
  console"Waiting for call"

   servers  
    "iceServers" 
      "url" "stun:stun.example.org"
    
  

  peerConnection   RTCPeerConnectionservers
  console"Created local peer connection"
  peerConnectiononicecandidate  gotLocalIceCandidate
  peerConnectiononaddstream  gotRemoteStream
  peerConnectionaddStreamlocalStream
  console"Added localStream to localPeerConnection"
```

setUpPeerConnection creates a new RTCPeerConnection and then sets callbacks for when certain events occur on the connection, such as an ICE candidate is detected or a stream is added. Then we add our local video stream to the peer connection.

Next we will add our call function to send a message to other clients connected on our channel with a local peer connection.

```
// web/static/js/app.js

function  
  callButtondisabled  
  console"Starting call"
  peerConnectioncreateOffergotLocalDescription handleError
```

We are passing the createOffer function the following gotLocalDescription callback.

```
// web/static/js/app.js

function gotLocalDescriptiondescription
  peerConnectionsetLocalDescriptiondescription  => 
      channel"message"   stringify
              "sdp" peerConnectionlocalDescription
          })});
       handleError
  console"Offer from localPeerConnection: \n"  description
```

The createOffer function created a description of the local peer connection and then sent that description to any potential clients. Once a client receives such a description it then calls the following gotRemoteDescription function.

```
// web/static/js/app.js

function gotRemoteDescriptiondescription
  console"Answer from remotePeerConnection: \n"  description
  peerConnectionsetRemoteDescription RTCSessionDescriptiondescription
  peerConnectioncreateAnswergotLocalDescription handleError
```

Here it sets the remote description on its local peer connection so it can connect to that remote client. It then replies with an answer containing its own description so that remote client can connect back to it as well.

The descriptions being sent back and forth between our clients also contain the streams that we added to their peer connections. Once a client receives a remote stream it will call the following function.

```
// web/static/js/app.js

function gotRemoteStreamevent 
  remoteVideo  createObjectURLeventstream
  console"Received remote stream"
```

Here we are just setting the remote stream we receive to the video element in our template.

Also, when we create our local description we are also creating a local ICE candidate, which will call the following function.

```
// web/static/js/app.js

function gotLocalIceCandidateevent 
   eventcandidate 
    console"Local ICE candidate: \n"  eventcandidatecandidate
    channel"message"  stringify
        "candidate" eventcandidate
    })});
```

This sends information about the local ICE candidate over the channel to any potential clients. When a client receives a description about an ICE candidate it will call the following function.

```
// web/static/js/app.js

function gotRemoteIceCandidateevent 
  callButtondisabled  
   eventcandidate 
    peerConnectionaddIceCandidate RTCIceCandidateeventcandidate
    console"Remote ICE candidate: \n "  eventcandidatecandidate
```

This function will add information about the remote candidate to its local peer connection.

When our channel receives a message from the server it needs to know how to process that message. If the message it receives is a description of the remote peer connection we need to call the gotRemoteDescription function, but if it is a description of the remote ICE candidate we need to call the gotRemoteIceCandidate function. We will implement our channel’s event handler to account for these two scenarios.

```
// web/static/js/app.js

channel"message" payload => 
   message  parsepayload
   message 
    gotRemoteDescriptionmessage
    
    gotRemoteIceCandidatemessage
```

Let’s also include a hangup function so a user can close the connection and stop the video chat session.

```
// web/static/js/app.js

function hangup 
  console"Ending call"
  peerConnectionclose
  localVideo  
  peerConnection  
  hangupButtondisabled  
  connectButtondisabled  false
  callButtondisabled
```

And finally add our handleError function.

```
// web/static/js/app.js

function handleErrorerror 
  consoleerror    errormessage
```

Now if you navigate back to the browser, open up two tabs, and click the connect button in each tab you should see that each one has created a local peer connection and added its local video stream. If you click the call button from one of the tabs then it will send a description of its local peer connection to the other peer connection, and after they exchange the necessary information they will establish their remote connection. Now you can see their video chat session. You can view the sample repository at <https://github.com/chadbrading/phoenix-webrtc>.
