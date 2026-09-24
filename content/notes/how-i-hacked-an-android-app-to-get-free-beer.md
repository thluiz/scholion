---
title: "How I Hacked an Android App to Get Free Beer"
date: '2026-09-24T23:05:09+01:00'
category: webclip
summary: 'The post shows how the app’s point authorization can be abused by intercepting HTTPS traffic and replacing the PIN flow with beacon data broadcast openly over BLE.'
tags: ["android-security", "https-interception", "ble-beacons", "mobile-apps"]
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

## Fichamento

- O app dá pontos por compras em estabelecimentos e autoriza a operação com PIN ou com um beacon físico do local.
- O autor identifica que os beacons da Estimote transmitem UUID, Major e Minor por BLE e que o app usa esses valores como chave de autorização.
- A verificação por beacon depende da proximidade medida pelo sinal e os dados do beacon são enviados ao servidor para validar a pontuação.
- O tráfego HTTPS do app é interceptado com Fiddler em rede local e depois com VPN e SSLsplit em conexão móvel.
- O app não usa certificate pinning, o que permite aceitar certificados forjados e ler o conteúdo das requisições.
- A requisição de pontos envia authentication_token, promoted_products_ids, pin, place_id, latitude e longitude em JSON.
- O servidor bloqueia tentativas repetidas de PIN por 30 minutos após poucas falhas.
- Quando a autorização usa beacon, a requisição inclui main_beacon com major, minor e uuid, junto com os demais dados da compra.
- O autor confirma que os valores capturados no app da Estimote são os mesmos enviados na requisição de autorização.
- O texto propõe usar hash do estado da conta, obfuscação, Secure UUID, certificate pinning, beacon de curto alcance e validação no dispositivo do vendedor para aumentar a segurança.
