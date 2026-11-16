---
url: "https://elixirstatus.com/p/PKb3-correios-cep-060-released-remove-zipcode-field-and-update-httpoison"
captured_at: "2026-11-16T03:41:51+00:00"
title: "Correios CEP 0.6.0 released! Remove zipcode field and update HTTPoison."
domain: "elixirstatus-com"
---

`Correios CEP` allows to find Brazilian addresses by postal code, directly from Correios API. No HTML parsers.

## DEPRECATION NOTE

`Correios.CEP.Address.zipcode` was removed in the version `0.6.0`. Use `Correios.CEP.Address.postal_code` instead.

### Changelog for version `0.6.0`:

#### Changed

*   Update HTTPoison to 1.17.0 (hackeny 1.16.0)

#### Deprecated

*   The field `zipcode` in `Correios.CEP.Address`. Use the field `postal_code` instead.

#### Removed

*   Support for OTP 20.

Check it out at:

*   [Hex](https://hex.pm/packages/correios_cep)
*   [Documentation](https://hexdocs.pm/correios_cep)
*   [GitHub](https://github.com/prodis/correios-cep-elixir)
