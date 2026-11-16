---
title: "If you’re not using SSH certificates you’re doing SSH wrong | Episode 2: Certificates improve usability, operability, & security"
date: '2026-11-16T01:56:23+00:00'
category: webclip
summary: 'The post argues that SSH certificates remove TOFU warnings, support SSO, reduce key-management work, ease host-name reuse, and make SSH access expire automatically with auditable renewals.'
tags: ["ssh-certificates", "certificate-authentication", "security", "operability"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "If you’re not using SSH certificates you’re doing SSH wrong | Episode 2: Certificates improve usability, operability, & security"
    url: "https://dev.to/smallstep/if-you-re-not-using-ssh-certificates-you-re-doing-ssh-wrong-episode-2-certificates-improve-usability-operability-security-45hg"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--ssh-certificates-usability-operability-security.md"
    kind: repo
---

The post says SSH certificates improve usability by removing first-connection TOFU warnings and by allowing custom authentication at certificate issuance, which can extend SSO to SSH. It also says they improve operability by reducing key-approval work, supporting automation with ephemeral certificates, and letting host names be reused without host key verification failures.

## Reading notes

- Public key SSH asks users to trust a host on first use, which produces a warning many people ignore.
- Certificate authentication lets clients authenticate the host even on first connection, so the TOFU warning disappears.
- A certificate can be issued only after custom authentication, which can be used to extend SSO to SSH.
- Removing key approval and distribution saves operations work and avoids maintaining systems for adding, removing, synchronizing, and auditing static public keys.
- Scripts and cron jobs can obtain ephemeral SSH certificates when needed instead of carrying long-lived static private keys.
- Public key authentication ties a host name to one public key in `known_hosts`, so replacing a host with the same name can trigger host key verification failures.
- Certificates communicate the current name-to-public-key binding at connection time, so changing a host key is fine if the host gets a new certificate.
- This lets teams reuse host names and run multiple hosts with the same name without host key verification failures.
- Public key authentication can leave compromised or stale keys trusted for a long time and may fail open when keys are not removed.
- Certificates expire automatically, so compromised credentials stop working without intervention even if an incident is not noticed.
- Periodic renewals through a CA create a complete audit record.
- Certificate authentication makes host rekeying easier and reduces the pressure to keep old keys in place.
- Public key authentication encourages key reuse and makes users reluctant to rekey, while a CA plus a simple client can make key generation and SSH workflows easier to manage.
