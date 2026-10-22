---
title: "End-to-End Encrypted Chat with the Web Crypto API"
date: '2020-10-10T10:09:09-03:00'
category: webclip
summary: 'The tutorial shows how to build a basic end-to-end encrypted chat in JavaScript with the Web Crypto API, using key pairs, derived keys, AES-GCM, and Stream Chat integration.'
tags: ["web-crypto-api", "end-to-end-encryption", "aes-gcm", "stream-chat"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "End-to-End Encrypted Chat with the Web Crypto API - DEV Community 👩‍💻👨‍💻"
    url: "https://dev.to/cardoso/end-to-end-encrypted-chat-with-the-web-crypto-api-3d02"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-10/dev-to--end-to-end-encrypted-chat-with-web-crypto-api.md"
    kind: repo
---

The page walks through a basic end-to-end encrypted chat built with JavaScript and the browser’s Web Crypto API. It explains what end-to-end encryption is, how the API exposes cryptographic operations, and how a chat app can use public and private key pairs, derive a shared key for two users, and encrypt and decrypt message text.

It also describes how the sample project is wired into Stream Chat by setting a user, fetching the recipient’s public key, deriving the shared key, and customizing message input and message display so outgoing text is encrypted and incoming text is decrypted.

## Reading notes

- The tutorial is described as basic and educational, with simplifications and warnings about rolling your own encryption protocol.
- End-to-end encryption is presented as a system where only the communicating users can read the messages.
- The Web Crypto API is used as the browser-native way to handle key generation, import and export, key derivation, encryption, and decryption.
- The key pair step uses ECDH with the P-256 curve, and both public and private keys are exported in JWK format.
- Exporting the private key is noted as a security risk and is only shown for educational purposes.
- The derived symmetric key is created from one user’s private key and the other user’s public key, and the same key can be derived on both sides.
- AES-GCM is used for the derived key, with the page citing security, performance, and browser support.
- Before encryption, text is encoded to a Uint8Array, encrypted, then converted through ArrayBuffer and Base64 for transmission.
- The AES-GCM initialization vector must be unique for each encryption operation and is sent with the message so decryption can use it.
- Decryption reverses the Base64 and buffer conversions, uses the same AES-GCM parameters, and returns an error if the key or IV is wrong.
- The integration section uses a Stream Chat project, starting from cloning the repo and configuring an API key.
- The app disables auth and permission checks for development, while noting that production should use proper backend-issued tokens.
- The user setup step stores the user and their public key, and checks for a mismatch if the user already exists with a different key pair.
- The sender screen can generate a key pair or accept pasted keys, while the recipient screen fetches the other user and their public key.
- The key deriver screen computes the shared key from the sender’s private key and the recipient’s public key.
- The custom message component decrypts incoming messages, and the custom input component encrypts outgoing messages before sending.
- The final chat screen combines Stream Chat components with the encrypted message display and encrypted message input.
- The page closes by noting that the example is still basic and lacks additions such as randomized padding, digital signatures, and forward secrecy.
