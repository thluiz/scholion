---
url: "https://github.com/web-push-libs/web-push"
captured_at: "2026-11-16T03:53:01+00:00"
title: "GitHub - web-push-libs/web-push: Web Push library for Node.js"
domain: "github-com"
---

[![Build Status](https://github.com/web-push-libs/web-push/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/web-push-libs/web-push/actions/workflows/ci.yml)

## Why

[](#why)

Web push requires that push messages triggered from a backend be done via the [Web Push Protocol](https://tools.ietf.org/html/draft-ietf-webpush-protocol) and if you want to send data with your push message, you must also encrypt that data according to the [Message Encryption for Web Push spec](https://tools.ietf.org/html/draft-ietf-webpush-encryption).

This module makes it easy to send messages and will also handle legacy support for browsers relying on GCM for message sending / delivery.

## Install

[](#install)

Installation is simple, just install via npm.

```
npm install web-push --save
```

## Usage

[](#usage)

The common use case for this library is an application server using a GCM API key and VAPID keys.

const webpush \= require('web-push');

// VAPID keys should be generated only once.
const vapidKeys \= webpush.generateVAPIDKeys();

webpush.setGCMAPIKey('<Your GCM API Key Here>');
webpush.setVapidDetails(
  'mailto:example@yourdomain.org',
  vapidKeys.publicKey,
  vapidKeys.privateKey
);

// This is the same output of calling JSON.stringify on a PushSubscription
const pushSubscription \= {
  endpoint: '.....',
  keys: {
    auth: '.....',
    p256dh: '.....'
  }
};

webpush.sendNotification(pushSubscription, 'Your Push Payload Text');

## Using VAPID Key for applicationServerKey

[](#using-vapid-key-for-applicationserverkey)

When subscribing to push messages, you'll need to pass your VAPID key, which you can do like so:

registration.pushManager.subscribe({
  userVisibleOnly: true,
  applicationServerKey: '<Your Public Key from generateVAPIDKeys()>'
});

## Command Line

[](#command-line)

You can install `web-push` globally and use it for sending notifications and / or generating VAPID keys.

Install like so:

```
npm install web-push -g
```

Then you can run the following commands:

```
Usage:

  web-push send-notification --endpoint=<url> [--key=<browser key>] [--auth=<auth secret>] [--payload=<message>] [--encoding=<aesgcm | aes128gcm>] [--ttl=<seconds>] [--vapid-subject=<vapid subject>] [--vapid-pubkey=<public key url base64>] [--vapid-pvtkey=<private key url base64>] [--proxy=<http proxy uri>] [--gcm-api-key=<api key>]

  web-push generate-vapid-keys [--json]
```

Example of send notification:

  \> web-push generate-vapid-keys --json
  \> {"publicKey":"BGtkbcjrO12YMoDuq2sCQeHlu47uPx3SHTgFKZFYiBW8Qr0D9vgyZSZPdw6\_4ZFEI9Snk1VEAj2qTYI1I1YxBXE","privateKey":"I0\_d0vnesxbBSUmlDdOKibGo6vEXRO-Vu88QlSlm5j0"}

The subscription value:

  { 
    "endpoint": "https://fcm.googleapis.com/fcm/send/d61c5u920dw:APA91bEmnw8utjDYCqSRplFMVCzQMg9e5XxpYajvh37mv2QIlISdasBFLbFca9ZZ4Uqcya0ck-SP84YJUEnWsVr3mwYfaDB7vGtsDQuEpfDdcIqOX\_wrCRkBW2NDWRZ9qUz9hSgtI3sY", 
    "expirationTime": null, 
    "keys": { 
      "p256dh": "BL7ELU24fJTAlH5Kyl8N6BDCac8u8li\_U5PIwG963MOvdYs9s7LSzj8x\_7v7RFdLZ9Eap50PiiyF5K0TDAis7t0", 
      "auth": "juarI8x\_\_VnHvsOgfeAPHg" 
    } 
  }

The command example:

  web-push send-notification  \\
  --endpoint=https://fcm.googleapis.com/fcm/send/d61c5u920dw:APA91bEmnw8utjDYCqSRplFMVCzQMg9e5XxpYajvh37mv2QIlISdasBFLbFca9ZZ4Uqcya0ck-SP84YJUEnWsVr3mwYfaDB7vGtsDQuEpfDdcIqOX\_wrCRkBW2NDWRZ9qUz9hSgtI3sY \\
  --key=BL7ELU24fJTAlH5Kyl8N6BDCac8u8li\_U5PIwG963MOvdYs9s7LSzj8x\_7v7RFdLZ9Eap50PiiyF5K0TDAis7t0 \\
  --auth=juarI8x\_\_VnHvsOgfeAPHg \\
  --vapid-subject=mailto:example@qq.com \\
  --vapid-pubkey=BGtkbcjrO12YMoDuq2sCQeHlu47uPx3SHTgFKZFYiBW8Qr0D9vgyZSZPdw6\_4ZFEI9Snk1VEAj2qTYI1I1YxBXE \\
  --vapid-pvtkey=I0\_d0vnesxbBSUmlDdOKibGo6vEXRO-Vu88QlSlm5j0 \\
  --payload=Hello

## API Reference

[](#api-reference)

## sendNotification(pushSubscription, payload, options)

[](#sendnotificationpushsubscription-payload-options)

const pushSubscription \= {
  endpoint: '< Push Subscription URL >',
  keys: {
    p256dh: '< User Public Encryption Key >',
    auth: '< User Auth Secret >'
  }
};

const payload \= '< Push Payload String >';

const options \= {
  gcmAPIKey: '< GCM API Key >',
  vapidDetails: {
    subject: '< \\'mailto\\' Address or URL >',
    publicKey: '< URL Safe Base64 Encoded Public Key >',
    privateKey: '< URL Safe Base64 Encoded Private Key >'
  },
  timeout: <Number\>
  TTL: <Number\>,
  headers: {
    '< header name >': '< header value >'
  },
  contentEncoding: '< Encoding type, e.g.: aesgcm or aes128gcm \>',
  urgency:'< Default is "normal" \>',
  topic:'< Use a maximum of 32 characters from the URL or filename-safe Base64 characters sets. \>',

  proxy: '< proxy server options \>',
  agent: '< https.Agent instance \>'
}

webpush.sendNotification(
  pushSubscription,
  payload,
  options
);

> **Note:** `sendNotification()` you don't need to define a payload, and this method will work without a GCM API Key and / or VAPID keys if the push service supports it.

### Input

[](#input)

**Push Subscription**

The first argument must be an object containing the details for a push subscription.

The expected format is the same output as JSON.stringify'ing a PushSubscription in the browser.

**Payload**

The payload is optional, but if set, will be the data sent with a push message.

This must be either a _string_ or a node [_Buffer_](https://nodejs.org/api/buffer.html).

> **Note:** In order to encrypt the _payload_, the _pushSubscription_ **must** have a _keys_ object with _p256dh_ and _auth_ values.

**Options**

Options is an optional argument that if defined should be an object containing any of the following values defined, although none of them are required.

*   **gcmAPIKey** can be a GCM API key to be used for this request and this request only. This overrides any API key set via `setGCMAPIKey()`.
*   **vapidDetails** should be an object with _subject_, _publicKey_ and _privateKey_ values defined. These values should follow the [VAPID Spec](https://tools.ietf.org/html/draft-thomson-webpush-vapid).
*   **timeout** is a value in milliseconds that specifies the request's socket timeout. On timeout, the request will be destroyed and the promise will be rejected with a meaningful error. It's a common misconception that a socket timeout is the timeout to receive the full response. So if you have a socket timeout of 1 second, and a response comprised of 3 TCP packets, where each response packet takes 0.9 seconds to arrive, for a total response time of 2.7 seconds, then there will be no timeout. Once a socket 'timeout' triggers the request will be aborted by the library (by default undefined).
*   **TTL** is a value in seconds that describes how long a push message is retained by the push service (by default, four weeks).
*   **headers** is an object with all the extra headers you want to add to the request.
*   **contentEncoding** is the type of push encoding to use (e.g. 'aes128gcm', by default, or 'aesgcm').
*   **urgency** is to indicate to the push service whether to send the notification immediately or prioritize the recipient’s device power considerations for delivery. Provide one of the following values: very-low, low, normal, or high. To attempt to deliver the notification immediately, specify high.
*   **topic** optionally provide an identifier that the push service uses to coalesce notifications. Use a maximum of 32 characters from the URL or filename-safe Base64 characters sets.
*   **proxy** is the [HttpsProxyAgent's constructor argument](https://github.com/TooTallNate/node-https-proxy-agent#new-httpsproxyagentobject-options) that may either be a string URI of the proxy server (eg. http://< hostname >:< port >) or an "options" object with more specific properties.
*   **agent** is the [HTTPS Agent instance](https://nodejs.org/dist/latest/docs/api/https.html#https_class_https_agent) which will be used in the `https.request` method. If the `proxy` options defined, `agent` will be ignored!

> **Note:** As of this writing, if a push notification request contains a VAPID `subject` referencing an `https://localhost` URI (set either using the `options` argument or via the global `setVapidDetails()` method), Safari's push notification endpoint rejects the request with a `BadJwtToken` error.

### Returns

[](#returns)

A promise that resolves if the notification was sent successfully with details of the request, otherwise it rejects.

In both cases, resolving or rejecting, you'll be able to access the following values on the returned object or error.

*   _statusCode_, the status code of the response from the push service;
*   _headers_, the headers of the response from the push service;
*   _body_, the body of the response from the push service.

* * *

## generateVAPIDKeys()

[](#generatevapidkeys)

const vapidKeys \= webpush.generateVAPIDKeys();

// Prints 2 URL Safe Base64 Encoded Strings
console.log(vapidKeys.publicKey, vapidKeys.privateKey);

### Input

[](#input-1)

None.

### Returns

[](#returns-1)

Returns an object with **publicKey** and **privateKey** values which are URL Safe Base64 encoded strings.

> **Note:** You should create these keys once, store them and use them for all future messages you send.

* * *

## setGCMAPIKey(apiKey)

[](#setgcmapikeyapikey)

webpush.setGCMAPIKey('Your GCM API Key');

### Input

[](#input-2)

This method expects the GCM API key that is linked to the `gcm_sender_id` in your web app manifest.

You can use a GCM API Key from the Google Developer Console or the _Cloud Messaging_ tab under a Firebase Project.

### Returns

[](#returns-2)

None.

* * *

## setVapidDetails(subject, publicKey, privateKey)

[](#setvapiddetailssubject-publickey-privatekey)

webpush.setVapidDetails(
  'mailto:user@example.org',
  process.env.VAPID\_PUBLIC\_KEY,
  process.env.VAPID\_PRIVATE\_KEY
);

Globally sets the application's VAPID subject, public key, and private key, to be used in subsequent calls to `sendNotification()` and `generateRequestDetails()` that don't specifically override them in their `options` argument.

### Input

[](#input-3)

The `setVapidDetails` method expects the following input:

*   _subject_: the VAPID server contact information, as either an `https:` or `mailto:` URI ([as per the VAPID spec](https://datatracker.ietf.org/doc/html/draft-thomson-webpush-vapid#section-2.1)). Use a real, externally valid contact URI rather than a local placeholder such as `mailto:user@localhost`; Apple Push may reject localhost-based subjects with `403 BadJwtToken`.
*   _publicKey_: the VAPID public key.
*   _privateKey_: the VAPID private key.

### Returns

[](#returns-3)

None.

* * *

## encrypt(userPublicKey, userAuth, payload, contentEncoding)

[](#encryptuserpublickey-userauth-payload-contentencoding)

const pushSubscription \= {
  endpoint: 'https://....',
  keys: {
    p256dh: '.....',
    auth: '.....'
  }
};
webPush.encrypt(
  pushSubscription.keys.p256dh,
  pushSubscription.keys.auth,
  'My Payload',
  'aes128gcm'
)
.then(encryptionDetails \=> {

});

Encrypts the payload according to the [Message Encryption for Web Push](https://webpush-wg.github.io/webpush-encryption/) standard.

> (_sendNotification_ will automatically encrypt the payload for you, so if you use _sendNotification_ you don't need to worry about it).

### Input

[](#input-4)

The `encrypt()` method expects the following input:

*   _userPublicKey_: the public key of the receiver (from the browser).
*   _userAuth_: the auth secret of the receiver (from the browser).
*   _payload_: the message to attach to the notification.
*   _contentEncoding_: the type of content encoding to use (e.g. aesgcm or aes128gcm).

### Returns

[](#returns-4)

This method returns an object with the following fields:

*   _localPublicKey_: The public key matched the private key used during encryption.
*   _salt_: A string representing the salt used to encrypt the payload.
*   _cipherText_: The encrypted payload as a Buffer.

* * *

## getVapidHeaders(audience, subject, publicKey, privateKey, contentEncoding, expiration)

[](#getvapidheadersaudience-subject-publickey-privatekey-contentencoding-expiration)

const parsedUrl \= url.parse(subscription.endpoint);
const audience \= parsedUrl.protocol + '//' +
  parsedUrl.hostname;

const vapidHeaders \= vapidHelper.getVapidHeaders(
  audience,
  'mailto: example@web-push-node.org',
  vapidDetails.publicKey,
  vapidDetails.privateKey,
  'aes128gcm'
);

The _getVapidHeaders()_ method will take in the values needed to create an Authorization and Crypto-Key header.

### Input

[](#input-5)

The `getVapidHeaders()` method expects the following input:

*   _audience_: the origin of the **push service**.
*   _subject_: the mailto or URL for your application.
*   _publicKey_: the VAPID public key.
*   _privateKey_: the VAPID private key.
*   _contentEncoding_: the type of content encoding to use (e.g. aesgcm or aes128gcm).

### Returns

[](#returns-5)

This method returns an object with the following fields:

*   _localPublicKey_: The public key matched the private key used during encryption.
*   _salt_: A string representing the salt used to encrypt the payload.
*   _cipherText_: The encrypted payload as a Buffer.

* * *

## generateRequestDetails(pushSubscription, payload, options)

[](#generaterequestdetailspushsubscription-payload-options)

const pushSubscription \= {
  endpoint: '< Push Subscription URL >';
  keys: {
    p256dh: '< User Public Encryption Key >',
    auth: '< User Auth Secret >'
  }
};

const payload \= '< Push Payload String >';

const options \= {
  gcmAPIKey: '< GCM API Key >',
  vapidDetails: {
    subject: '< \\'mailto\\' Address or URL >',
    publicKey: '< URL Safe Base64 Encoded Public Key >',
    privateKey: '< URL Safe Base64 Encoded Private Key >',
  }
  TTL: <Number\>,
  headers: {
    '< header name >': '< header value >'
  },
  contentEncoding: '< Encoding type, e.g.: aesgcm or aes128gcm >',
  urgency:'< Default is normal "Defult" >',
  topic:'< Use a maximum of 32 characters from the URL or filename-safe Base64 characters sets. >',
  proxy: '< proxy server options >'
}

try {
  const details \= webpush.generateRequestDetails(
    pushSubscription,
    payload,
    options
  );
} catch (err) {
  console.error(err);
}

> **Note:** When calling `generateRequestDetails()` the payload argument does not _need_ to be defined, passing in null will return no body and exclude any unnecessary headers. Headers related to the GCM API Key and / or VAPID keys will be included if supplied and required.

### Input

[](#input-6)

**Push Subscription**

The first argument must be an object containing the details for a push subscription.

The expected format is the same output as JSON.stringify'ing a PushSubscription in the browser.

**Payload**

The payload is optional, but if set, will be encrypted and a [_Buffer_](https://nodejs.org/api/buffer.html) will be returned via the `payload` parameter.

This argument must be either a _string_ or a node [_Buffer_](https://nodejs.org/api/buffer.html).

> **Note:** In order to encrypt the _payload_, the _pushSubscription_ **must** have a _keys_ object with _p256dh_ and _auth_ values.

**Options**

Options is an optional argument that if defined should be an object containing any of the following values defined, although none of them are required.

*   **gcmAPIKey** can be a GCM API key to be used for this request and this request only. This overrides any API key set via `setGCMAPIKey()`.
*   **vapidDetails** should be an object with _subject_, _publicKey_ and _privateKey_ values defined. These values should follow the [VAPID Spec](https://tools.ietf.org/html/draft-thomson-webpush-vapid).
*   **TTL** is a value in seconds that describes how long a push message is retained by the push service (by default, four weeks).
*   **headers** is an object with all the extra headers you want to add to the request.
*   **contentEncoding** is the type of push encoding to use (e.g. 'aesgcm', by default, or 'aes128gcm').
*   **urgency** is to indicate to the push service whether to send the notification immediately or prioritize the recipient’s device power considerations for delivery. Provide one of the following values: very-low, low, normal, or high. To attempt to deliver the notification immediately, specify high.
*   **topic** optionally provide an identifier that the push service uses to coalesce notifications. Use a maximum of 32 characters from the URL or filename-safe Base64 characters sets.
*   **proxy** is the [HttpsProxyAgent's constructor argument](https://github.com/TooTallNate/node-https-proxy-agent#new-httpsproxyagentobject-options) that may either be a string URI of the proxy server (eg. http://< hostname >:< port >) or an "options" object with more specific properties.

### Returns

[](#returns-6)

An object containing all the details needed to make a network request, the object will contain:

*   _endpoint_, the URL to send the request to;
*   _method_, this will be 'POST';
*   _headers_, the headers to add to the request;
*   _body_, the body of the request (As a Node Buffer).

* * *

## Browser Support

[](#browser-support)

**Browser**

**Push without Payload**

**Push with Payload**

**VAPID**

**Notes**

Chrome

✓ v42+

✓ v50+

✓ v52+

In v51 and less, the \`gcm\_sender\_id\` is needed to get a push subscription.

Edge

✓ v17+ (April 2018)

✓ v17+ (April 2018)

✓ v17+ (April 2018)

Firefox

✓ v44+

✓ v44+

✓ v46+

Opera

✓ v39+ **\***

✓ v39+ **\***

✗

**\*** Opera supports push on Android but not on desktop.

The \`gcm\_sender\_id\` is needed to get a push subscription.

Safari

✓ v16+

✓ v16+

✓ v16+

Safari 16 in macOS 13 or later

Samsung Internet Browser

✓ v4.0.10-53+

✓ v5.0.30-40+

✗

The \`gcm\_sender\_id\` is needed to get a push subscription.

## Help

[](#help)

**MDN**

There's an example on [MDN](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Tutorials/js13kGames/Re-engageable_Notifications_Push).

Also, the [Service Worker Cookbook](https://github.com/mdn/serviceworker-cookbook) is full of Web Push examples using this library.

## Running tests

[](#running-tests)

> Prerequisites:
> 
> *   Java JDK or JRE ([http://www.oracle.com/technetwork/java/javase/downloads/index.html](http://www.oracle.com/technetwork/java/javase/downloads/index.html))

To run tests:

```
npm test
```

[![](https://camo.githubusercontent.com/a7d393aae19f4d0c83164ddc4d432db00db9059ba5b506a2df8b9667313761d0/68747470733a2f2f6e6f6465692e636f2f6e706d2f7765622d707573682e7376673f646f776e6c6f6164733d74727565)](https://www.npmjs.com/package/web-push)
