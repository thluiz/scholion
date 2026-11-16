---
title: "Correios CEP 0.6.0 released! Remove zipcode field and update HTTPoison."
date: '2020-07-05T14:10:33+00:00'
category: webclip
summary: 'Correios CEP lets you find Brazilian addresses by postal code through the Correios API. Version 0.6.0 removes `Address.zipcode`, switches to `postal_code`, updates HTTPoison, and drops OTP 20 support.'
tags: ["elixir", "correios-cep", "httpoison", "otp"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Correios CEP 0.6.0 released! Remove zipcode field and update HTTPoison."
    url: "https://elixirstatus.com/p/PKb3-correios-cep-060-released-remove-zipcode-field-and-update-httpoison"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/elixirstatus-com--correios-cep-060-released-remove-zipcode-field-and-update-ht.md"
    kind: repo
---

Correios CEP looks up Brazilian addresses by postal code through the Correios API and does not use HTML parsers. The 0.6.0 release removes `Correios.CEP.Address.zipcode`, replaces it with `Correios.CEP.Address.postal_code`, updates HTTPoison to 1.17.0, and drops support for OTP 20.

## Reading notes

- It retrieves Brazilian addresses from the Correios API.
- It does not use HTML parsers.
- `Correios.CEP.Address.zipcode` was removed in 0.6.0.
- `Correios.CEP.Address.postal_code` is the replacement field.
- HTTPoison was updated to 1.17.0.
- Support for OTP 20 was removed.
