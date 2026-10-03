---
url: "https://dev.to/ecnepsnai/pragmatically-generating-a-self-signed-certificate-and-private-key-usingopenssl"
captured_at: "2017-07-04T12:13:28-03:00"
title: "Pragmatically Generating a Self-Signed Certificate and Private Key using OpenSSL"
domain: "dev-to"
---

# Pragmatically Generating a Self-Signed Certificate and Private Key using OpenSSL

### 

Recently I found myself needing to generate a HTTPS Server Certificate and Private Key for an iOS app using OpenSSL, what surprised me was the total lack of documentation for OpenSSL.

While there is plenty of function documentation, what OpenSSL really lacks is examples of how it all fits together. It’s like having all of the pieces of a puzzle, but no picture of that the finished product will look like. Many online examples are insecure or make use of deprecated functions, a serious concern considering the consequences.

This tutorial will cover the basics for how to generate a RSA or ECDSA Private Key and a X509 Server Certificate for your application in C. For this tutorial, we will be using OpenSSL 1.0.1t.

# Generating the Private Key

A private key is required for any PKI encryption setup, and you generally have two choices for algorithms: RSA and ECDSA.

## ECDSA V.S. RSA

RSA has been the defacto standard for private keys for quite a long time, and if used correctly is still secure. The security of an RSA key relies on how large the “big number” is when the key is created. The recommended size of this number keeps going up and up as we’re getting better and better at breaking smaller numbers.  
ECDSA keys, however, are created differently than RSA keys, and are much harder to break. In fact, no tangible progress has been made on solving the problem that ECDSA keys use — The Elliptic Curve Discrete Logarithm Problem (ECDLP) — since 1985. Because of this, ECDSA keys provide much greater security without the need for larger numbers. For example: a 256-bit ECDSA key is equivalent to a 3,248-bit RSA key.  
Not only are ECDSA keys more secure than most RSA keys, they’re also much less CPU intensive. CloudFlare dissected the performance of the two in their [write up on the algorithm](https://blog.cloudflare.com/ecdsa-the-digital-signature-algorithm-of-a-better-internet/).

```
sign/s
256bitecdsa(nistp256)9516.8
rsa2048bits1001.8

(openssl1.0.2betaonx86_64withenable-ec_nistp_64_gcc_128)
```

To put it simply: ECDSA keys are 9x less CPU intensive while providing greater security than RSA keys.

## Generating an RSA Private Key

```
#include <openssl/x509.h>
#include <openssl/rsa.h>

ERR_load_CRYPTO_strings();
OPENSSL_add_all_algorithms_noconf();

EVP_PKEY * pkey      = EVP_PKEY_new();
BIGNUM   * bigNumber = BN_new();
int        exponent  = RSA_F4;

if (BN_set_word(bigNumber, exponent) < 0) {
    // Error creating the big number
    // Use ERR_peek_last_error_line to find out why
    goto cleanup;
}

RSA * rsa = RSA_new();
if (RSA_generate_key_ex(rsa,
                        2048, // This is the length of your private key
                        bigNumber,
                        NULL) < 0) {
    // Error generating RSA key
    // Use ERR_peek_last_error_line to find out why
    goto cleanup;
}

EVP_PKEY_assign_RSA(pkey, rsa);

cleanup:
    RSA_free(rsa);
    BN_free(bigNumber);
```

## Generating a ECDSA Private Key

```
#include <openssl/x509.h>
#include <openssl/ecdsa.h>

ERR_load_CRYPTO_strings();
OPENSSL_add_all_algorithms_noconf();

EVP_PKEY * pkey = EVP_PKEY_new();

EC_KEY * ecc = EC_KEY_new_by_curve_name(NID_secp256k1);
if (!ecc) {
    // Error selecting curve
    // Use ERR_peek_last_error_line to find out why
}

EC_KEY_set_asn1_flag(ecc, OPENSSL_EC_NAMED_CURVE);
if (EC_KEY_generate_key(ecc) < 0) {
    // Error generating key
    // Use ERR_peek_last_error_line to find out why
}

if (EVP_PKEY_assign_EC_KEY(pkey, ecc) < 0) {
    // Error assigning key to pkey class
    // Use ERR_peek_last_error_line to find out why
}
```

# Generating the Server Certificate

The server certificate is the client-facing piece of information that details the connection to the server. It tells the client what type of cipher to use, and validates the identity of the server. We’re generating a self-signed certificate in this case, so your computer won’t trust the certificate until you install it locally.

```
#include <openssl/x509.h>

ERR_load_CRYPTO_strings();
OPENSSL_add_all_algorithms_noconf();

X509 * x509;
x509 = X509_new();

// It's dangerous to use a static serial number!
// However for the purpose of this tutorial we will ignore this danger.
ASN1_INTEGER_set(X509_get_serialNumber(x509), 1234);

// Set the certificate validity dates.
// These value is appended to the systems current time stamp meaning that 0 = now.
X509_gmtime_adj(X509_get_notBefore(x509), 0);
X509_gmtime_adj(X509_get_notAfter(x509), 7776000); // 60 * 60 * 24 * NUMBER_OF_DAYS_TO_BE_VALID

X509_set_pubkey(x509, pkey); // Use the pkey that you generated before

X509_NAME * name;
name = X509_get_subject_name(x509);

// Now to add the subject name fields to the certificate
// I use a macro here to make it cleaner.
#define addName(field, value) X509_NAME_add_entry_by_txt(name, field,  MBSTRING_ASC, (unsigned char *)value, -1, -1, 0);

// The domain name or IP address that the certificate is issued for.
addName("CN", "ecn.io");

// The organizational unit for the cert. Usually this is a department.
addName("OU", "Certificate Authority");

// The organization of the cert.
addName("O",  "Explicit Congestion Notification");

// The city of the organization.
addName("L",  "Vancouver");

// The state/province of the organization.
addName("S",  "British Columbia");

// The country (ISO 3166) of the organization
addName("C",  "CA");

X509_set_issuer_name(x509, name);

// Specify the encryption algorithm of the signature.
// SHA256 should suit your needs.
if (X509_sign(x509, pkey, EVP_sha256()) < 0) {
    // Error signing the certificate with the key
    // Use ERR_peek_last_error_line to find out why
}
```

# Saving your private key and certificate

OpenSSL encourages that you use their built-in methods for writing to the disk as they can automatically encrypt the private key contents using a password and cipher of your choice.

It’s *absolutely vital* — and I cannot stress this enough — that you keep your private key safe.

At a minimum, you should be changing the file permissions to not be world-readable. Jeff Atwood has a good write-up on [Keeping Private Keys Private](https://blog.codinghorror.com/keeping-private-keys-private/).

```
#include <openssl/x509.h>
#include <openssl/pem.h>

ERR_load_CRYPTO_strings();
OPENSSL_add_all_algorithms_noconf();

const char * encryptionPassword = "MySuperDuperSecurePassword";

FILE * f = fopen("./private_key.pem", "wb");

// Here you write the private key (pkey) to disk. OpenSSL will encrypt the
// file using the password and cipher you provide.
if (PEM_write_PrivateKey(f,
                         pkey,
                         EVP_des_ede3_cbc(),
                         (unsigned char *)encryptionPassword,
                         (int)strlen(encryptionPassword),
                         NULL,
                         NULL) < 0) {
    // Error encrypting or writing to disk.
    // Use ERR_peek_last_error_line to find out why
    fclose(f);
}
fclose(f);

f = fopen("./server_cert.pem", "wb");

// Here you write the certificate to the disk. No encryption is needed here
// since this is public facing information
if (PEM_write_X509(f, x509) < 0) {
    // Error writing to disk.
    // Use ERR_peek_last_error_line to find out why
    fclose(f);
}
fclose(f);
```

# Verifying our Server Certificate

OpenSSL has a nifty little function that lets you quickly print out the summary of a X509 certificate to a file (or stdout):

```
X509*cert=...
X509_print_fp(stdout,cert);
```

Inspecting the certificate created with a RSA private key:

```
Certificate:
    Data:
        Version: 1 (0x0)
        Serial Number: 1234 (0x4d2)
    Signature Algorithm: sha256WithRSAEncryption
        Issuer: CN=ecn.io, OU=Certificate Authority, O=Explicit Congestion Notification, L=Vancouver, C=CA
        Validity
            Not Before: Sep  2 04:29:52 2016 GMT
            Not After : Dec  1 04:29:52 2016 GMT
        Subject: CN=ecn.io, OU=Certificate Authority, O=Explicit Congestion Notification, L=Vancouver, C=CA
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (2048 bit)
                Modulus: ...omitted...
```

And with the ECDSA key:

```
Certificate:
    Data:
        Version: 1 (0x0)
        Serial Number: 1234 (0x4d2)
    Signature Algorithm: ecdsa-with-SHA256
        Issuer: CN=ecn.io, OU=Certificate Authority, O=Explicit Congestion Notification, L=Vancouver, C=CA
        Validity
            Not Before: Sep  2 04:29:52 2016 GMT
            Not After : Dec  1 04:29:52 2016 GMT
        Subject: CN=ecn.io, OU=Certificate Authority, O=Explicit Congestion Notification, L=Vancouver, C=CA
        Subject Public Key Info:
            Public Key Algorithm: id-ecPublicKey
                Public-Key: (256 bit)
                pub: ...omitted...
```

If you’re looking for easily verify your new X509 certificate on-the-go using your iOS mobile device, check out one of my projects: [Certificate Inspector](https://certificate-inspector.com/). The worlds first Free & Libre X509 Certificate Inspector on iOS ([GitHub](https://github.com/certificate-helper/certificate-inspector)).
