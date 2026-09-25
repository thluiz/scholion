---
title: "How I Hacked an Android App to Get Free Beer"
date: '2026-09-24T23:05:09+01:00'
category: webclip
summary: 'The post shows how the app’s point authorization can be abused by intercepting HTTPS traffic and replacing the PIN flow with beacon data broadcast openly over BLE.'
tags: ["android-security","https-interception","ble-beacons","mobile-apps"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How I Hacked an Android App to Get Free Beer"
    url: "https://breakdev.org/how-i-hacked-an-android-app-to-get-free-beer/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/breakdev-org--how-i-hacked-an-android-app-to-get-free-beer.md"
    kind: repo
---

The page describes an Android app used in pubs, restaurants, and cafes to grant points for purchases. It shows that the app accepts either a PIN or data from a nearby beacon, and that the beacon values can be read over the air and reused in intercepted requests.

It then walks through intercepting the app’s HTTPS traffic with Fiddler and later with an L2TP/IPsec VPN plus SSLsplit. After capturing both PIN-based and beacon-based authorization packets, the author confirms that the beacon’s UUID, Major, and Minor values are sent to the server and can be swapped into a request to earn points.

## Reading notes

- The app gives points for purchases at establishments and authorizes the operation with a PIN or with a physical beacon from the place.
- The author identifies that Estimote beacons transmit UUID, Major, and Minor over BLE and that the app uses these values as an authorization key.
- Beacon verification depends on proximity measured by the signal, and the beacon data are sent to the server to validate the points.
- The app’s HTTPS traffic is intercepted with Fiddler on a local network and later with VPN and SSLsplit on a mobile connection.
- The app does not use certificate pinning, which allows forged certificates to be accepted and the request content to be read.
- The points request sends authentication_token, promoted_products_ids, pin, place_id, latitude and longitude in JSON.
- The server blocks repeated PIN attempts for 30 minutes after a few failures.
- When authorization uses a beacon, the request includes main_beacon with major, minor and uuid, along with the other purchase data.
- The author confirms that the values captured in the Estimote app are the same as those sent in the authorization request.
- The text proposes using a hash of the account state, obfuscation, Secure UUID, certificate pinning, short-range beacon and on-device validation at the seller’s device to increase security.
