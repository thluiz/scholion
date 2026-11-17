---
title: "Continuous products, product integrals and physics"
date: '2023-12-11T16:49:30+00:00'
category: webclip
summary: 'Thread introduces the product integral as a multiplicative analogue of the Riemann integral, explains its basic properties, and shows how it appears in solving differential equations and quantum time evolution.'
tags: ["product-integral", "riemann-integral", "differential-equations", "quantum-mechanics"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Thread by @martinmbauer: If you want to define a continuous addition you get the Riemann integral This is what happ…"
    url: "https://x.com/martinmbauer/status/1733589338909188450"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2023-12/x-com--martin-bauer-thread-product-integral-physics.md"
    kind: repo
---

Martin Bauer’s thread presents the product integral as the multiplicative counterpart of the Riemann integral. He outlines how it can be rewritten using exponentials and logarithms, shows that its basic properties justify the name "product integral", and explains its role in solving certain differential equations and in quantum mechanics time evolution.

## Reading notes

- The Riemann integral arises when one defines a continuous version of addition, while the thread asks what happens when one defines a continuous version of multiplication.
- The Riemann integral is obtained by approximating the area under a function with discrete blocks and taking the limit of their sum as the blocks become infinitesimally thin.
- Replacing the sum in this construction by a product leads to the definition of the "product integral".
- For sufficiently nice functions \(f(x)\), properties of the exponential and logarithm allow rewriting the product integral as the exponential of an ordinary integral.
- Because of this relation, product-integral calculus can be treated within ordinary calculus as long as one can take the exponential of the resulting integral.
- The name "product integral" is motivated by its behavior: for \(f(x)=1\) the value is 1, and for a constant \(f(x)=c\) it yields \(c^{b-a}\), which matches expectations for a continuous product over an interval.
- There are rules for product integrals that mirror the familiar rules for the Riemann integral once addition is replaced by multiplication, and Bauer suggests it is interesting to verify these parallels.
- Volterra introduced the product integral to handle a class of differential equations; it plays for equations of the form \(y'(x)=a(x)y(x)\) the role that the ordinary integral plays for \(y'(x)=a(x)\).
- Differential equations of the type \(y'(x)=a(x)y(x)\) occur frequently in physics, with the time-dependent Schrödinger equation given as an example.
- The time-dependent Schrödinger equation can be solved using the time-evolution operator, which Bauer identifies as a product integral.
- With the product integral definition, time evolution appears as a product of small phase factors that move \(\psi(t)\) infinitesimally along a curve determined by the Hamiltonian \(H\).
- When the Hamiltonian is constant in time, this product-integral description reproduces the standard time evolution for the time-independent Schrödinger equation.
- Product integrals also play an important role in contexts such as the Dyson series and the path integral.
- Bauer suggests that product integrals should perhaps be introduced together with the Riemann integral, since many steps in quantum mechanics and quantum field theory become more intuitive once this connection is seen.
- In later replies, he notes that this structure is widely used in solutions of differential equations of the form \(y' = a y\), though it is often not explicitly recognized as a product integral.
- He also remarks that this may explain why in physics the function involved is typically an exponential.
