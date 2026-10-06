---
title: "Exponentiation by squaring"
date: '2015-05-01T12:17:34-03:00'
category: webclip
summary: 'A method for fast computation of large integer powers that also applies to semigroups, modular arithmetic, matrices, and cryptographic settings. It reduces work with squaring-based variants and related recodings.'
tags: ["mathematics", "computer-programming", "modular-arithmetic", "cryptography"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Exponentiation by squaring - Wikipedia, the free encyclopedia"
    url: "http://en.wikipedia.org/wiki/Exponentiation_by_squaring"
    kind: wiki
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/en-wikipedia-org--exponentiation-by-squaring.md"
    kind: repo
---

Exponentiation by squaring is a general method for computing large positive integer powers efficiently. The page says it also applies to elements of a semigroup, including polynomials, square matrices, and elliptic-curve settings used in cryptography. Variants are called square-and-multiply, binary exponentiation, or double-and-add.

## Reading notes

- The basic method uses the identity for positive integers that breaks x^n into smaller powers by repeated squaring.
- A recursive algorithm handles n < 0, n = 0, n = 1, even n, and odd n separately.
- The algorithm can be rewritten as tail-recursive to reduce stack depth.
- The complexity is O(log n) squarings and O(log n) multiplications.
- For n greater than about 4, it is more efficient than repeated multiplication.
- If multiplying d-digit numbers costs O(d^k), then the cost of x^n follows the stated asymptotic bound in the page.
- The 2k-ary method expands the exponent in base 2^k and uses precomputed values.
- The sliding window method is presented as an efficient variant of the 2k-ary method.
- Montgomery's ladder uses a fixed sequence of operations for each bit of the exponent.
- The page notes that Montgomery's ladder helps against side-channel attacks, though the shown implementation is still exposed to cache timing attacks.
- For fixed bases, precomputations are important.
- Yao's method and the Euclidean method are described as fixed-base approaches.
- The same idea is used for modular exponentiation, especially in cryptography and integer rings modulo q.
- The page gives a modular arithmetic example that reduces the number of multiplications dramatically compared with a naive approach.
- Example implementations show a non-recursive Ruby version and runtime traces for computing 3^10.
- The method can also compute products of several powers more efficiently when the underlying structure is commutative.
- Signed-digit recoding allows negative coefficients when inverses are fast or precomputed.
- The non-adjacent form is described as a signed-binary representation with minimal Hamming weight.
- Exponentiation by squaring is presented as a suboptimal addition-chain method, and optimal chains are only practical for small exponents.
- Finding an optimal addition chain is stated to be a hard problem.
