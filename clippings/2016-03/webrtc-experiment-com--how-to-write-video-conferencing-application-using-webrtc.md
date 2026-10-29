---
url: "https://www.webrtc-experiment.com/docs/how-to-WebRTC-video-conferencing.html"
captured_at: "2016-03-12T10:34:06-03:00"
title: "How to write video-conferencing application using WebRTC? ® Muaz Khan"
domain: "webrtc-experiment-com"
---

# How to write video-conferencing application using WebRTC? ® Muaz Khan

|  |
| --- |
| If you're newcomer, newbie or beginner; you're suggested to try [RTCMultiConnection.js](http://bit.ly/RTCMultiConnection-Documentation) or [DataChannel.js](http://bit.ly/DataChannel-Documentation) libraries. |

## How to video conferencing?

1. Open multiple peer connections to support multi-users connectivity

It is called peer-to-peer model; where all peers are interconnected.

## You should

1. create two reusable functions: one for creating offer and other for creating answer. These will be called/invoked many times on each new room participation request.
2. create a function like "openSignalingChannel" that should open new socket on each invocation.
3. uniquely identify the current user

It is preferred to use socket.io because it supports multiplexing.

## Those functions

On invocation; those functions should:

1. create a new peer connection
2. create offer or answer session-descriptions accordingly

## Then, on page load

On page load: call "openSignalingChannel" method. This time your "openSignalingChannel" must open "default-channel" that must be active all the time. That default channel will be used to:

1. show list of all active rooms
2. allow new users to send "participation requests"

## For room creator

If someone creates new room; you should continuously transmit his room details over the "default-channel".

You can use transmission-interval i.e. 3 or 5 seconds. It should be your own preference.

## For room participant

Send "participation request" over same "default-channel".

You should also send participant's unique id in the "participation request" message.

Call "openSignalingChannel" method to create new socket where you should use his unique id as channel name/label.

That newly created socket will be used to get offer-sdp from room owner. It will also be used to get ICE gathered by room owner.

## As soon as room owner will receive participation-request

You should create new socket using "openSignalingChannel" method where you should use participant's unique id for channel name/label. Otherwise, use random number that must be passed along with "participation request" message.

That new socket will be used to exchange SDP/ICE between room owner and that participant.

## On the room owner's side

You should quickly create a new peer connection.

You should also quickly create "offer" because room-owner is expected to play the role of "offerer" for each new participant.

As soon as offer is created; you should pass that "offer sdp" over same socket that is being used to exchange SDP/ICE between room owner and participant.

## On the participant's side

Set remote descriptions using offer sdp sent by room owner.

Create answer. Participant will always play role of "answerer" on joining new room.

As soon as answer is created; you should pass that "answer sdp" over same socket that is being used to exchange SDP/ICE between room owner and participant.

## Again, on the room owner's side

Set remote descriptions using answer sdp sent by participant.

And handshake is completed! Are you sure? Wait....there is something else!

## ICE candidates gathered on room owner's side

You should use same socket to exchange/post/transfer these ICE candidates on participant's side.

## ICE candidates gathered on participant's side

You should use same socket to exchange/post/transfer these ICE candidates on room owner's side.

## Finally...

And finally handshake is completed. You're done! Good job Sir!

## For upcoming participants

For each new participant; repeat above process and that's it!

## For video-conferencing

After successful handshake between room owner and the participant; transmit participant's details over all other connected sockets i.e. toward all other room participants.

As soon as other participants will receive transmitted details; make "auto" participation request toward that "last participant".

And then follow above process again.

Explaining above theory using (a little bit real however) pseudo codes.

## Reusable functions...

```
function openSignalingChannelchannel

    socket  ioconnect'http://your-site:8888/'  channel

function createOffer

    peer   RTCPeerConnection(...);
   peercreateOfferonSuccess

function createAnsweroffer_sdp

    peer   RTCPeerConnection(...);
   peersetRemoteDescriptionoffer_sdp
   peercreateAnsweronSuccess
```

## Opening default signaling channel

```
 channel  openSignalingChannel'default-channel'
channelonmessage  functionmessage

   messageparticipationRequest 
   messagesharingRoomDetails
```

## Assuming a new participant

```
channel
   isNewParticipant 
   participant_id participant_id

// this private socket will be used to exchange sdp/ice
 privateChannel  openSignalingChannelparticipant_id
privateChannelonmessage  functionmessage

   messagetype  'offer'
   
       createAnswermessagesdp

       // on creating answer-sdp; transmit it over "privateChannel"
       privateChannelanswer_sdp
```

## On participation request

```
messageisNewParticipant

    privateChannel  openSignalingChannelmessageparticipant_id

   createOffer

   // on creating offer-sdp; transmit it over "privateChannel"
   privateChanneloffer_sdp
   privateChannelonmessage  functionmessage
   
      messagetype  'answer' peersetRemoteDescriptionmessagesdp
```

## Exchanging ICE

```
privateChannelonmessage  functionmessage

   messageice peeraddIceCandidate RTCIceCandidatemessageice

peeronicecandidate  functionevent

   privateChanneleventcandidate
```

## For video-conferencing

After successful handshake:

```
 i   i  otherParticipantslength i

     participant  otherParticipantsi

    // send/emit/push/etc.
    participant
        isNewParticipant 
        participant_id '0123456789'
```

Use "participant\_id" you can make additional participation requests to him.
