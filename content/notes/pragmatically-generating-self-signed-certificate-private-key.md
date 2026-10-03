---
title: "Pragmatically Generating a Self-Signed Certificate and Private Key using OpenSSL"
date: '2017-07-04T12:13:28-03:00'
category: webclip
summary: 'The tutorial explains how to generate RSA or ECDSA private keys and a self-signed X509 server certificate with OpenSSL, then save and verify the files, while stressing key protection.'
tags: ["openssl", "x509", "rsa", "ecdsa"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Pragmatically Generating a Self-Signed Certificate and Private Key using OpenSSL"
    url: "https://dev.to/ecnepsnai/pragmatically-generating-a-self-signed-certificate-and-private-key-usingopenssl"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2017-07/dev-to--pragmatically-generating-self-signed-certificate-private-key.md"
    kind: repo
---

The tutorial shows how to generate a private key and a self-signed server certificate with OpenSSL for a C application. It compares RSA and ECDSA, then walks through key creation, certificate fields, file output, and a quick verification step.

## Reading notes

- The article says OpenSSL has function documentation, but lacks examples that show how the pieces fit together, and warns that many online examples are insecure or use deprecated functions.
- It covers the basics of generating an RSA or ECDSA private key and an X509 server certificate in C, using OpenSSL 1.0.1t.
- It presents RSA as the long-standing standard and says its security depends on key size.
- It presents ECDSA as harder to break, based on the Elliptic Curve Discrete Logarithm Problem, and says a 256-bit ECDSA key is equivalent to a 3,248-bit RSA key.
- It says ECDSA is less CPU intensive than RSA and cites CloudFlare performance numbers.
- For RSA key generation, it creates a BIGNUM exponent, generates a 2048-bit RSA key, and assigns it to an EVP_PKEY.
- For ECDSA key generation, it selects curve NID_secp256k1, sets the named-curve ASN.1 flag, generates the EC key, and assigns it to an EVP_PKEY.
- For the server certificate, it creates an X509 object, sets a serial number, sets validity dates, attaches the public key, fills in subject fields such as CN, OU, O, L, S, and C, copies the subject to the issuer, and signs with SHA256.
- It recommends using OpenSSL’s built-in write methods to save the private key and certificate, encrypting the private key with a password and cipher.
- It stresses that the private key must be kept safe and that file permissions should prevent world-readable access.
- It shows X509_print_fp as a quick way to inspect a certificate and includes example output for both RSA and ECDSA certificates.
- It ends by mentioning a project called Certificate Inspector for checking X509 certificates on iOS.
