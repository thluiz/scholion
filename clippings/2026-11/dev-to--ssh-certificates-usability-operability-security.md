---
url: "https://dev.to/smallstep/if-you-re-not-using-ssh-certificates-you-re-doing-ssh-wrong-episode-2-certificates-improve-usability-operability-security-45hg"
captured_at: "2026-11-16T01:56:23+00:00"
title: "If you’re not using SSH certificates you’re doing SSH wrong | Episode 2: Certificates improve usability, operability, & security"
domain: "dev-to"
---

[In our previous post](https://dev.to/smallstep/if-you-re-not-using-ssh-certificates-you-re-doing-ssh-wrong-episode-1-keys-versus-certificates-5a0n), we discussed the benefits of using certificates over keys for SSH. In this episode we wanted to highlight how switching to certificates improves the lives of developers, operators, and security teams.

### [](#certificate-authentication-improves-usability)Certificate authentication improves usability

With public key authentication, when you SSH to a remote host for the first time, you'll be presented with a security warning like this:

```
$ ssh ubuntu@ec2-54-161-77-102.compute-1.amazonaws.com
The authenticity of host 'ec2-54-161-77-102.compute-1.amazonaws.com (54.161.77.102)' can't be established.
ECDSA key fingerprint is SHA256:2ae53QcOB0W6HO+XtPmMXk7To/MvMuhFxTj8ZD7eSsE.
Are you sure you want to continue connecting (yes/no)?
```

Enter fullscreen mode Exit fullscreen mode

You've probably seen this before. If you're like most people, you've been trained to ignore it by just typing "yes". That's a problem because this is a legitimate security threat. It's also a pretty horrendous user experience. I'd wager the vast majority of SSH users don't actually understand this warning.

When you SSH to a host, the host authenticates you. Your SSH client also attempts to authenticate the host. To do so your client needs to know the host's public key. Host public keys are stored in a simple database in `~/.ssh/known_hosts`. If your client can't find the host's public key in this database you get this warning. **It's telling you that the host can't be authenticated!**

[![Browser certificate warning is equivalent to TOFU](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fqgxtd0kft7507g8p4oh1.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fqgxtd0kft7507g8p4oh1.png)

What you're _supposed_ to do is verify the key fingerprint out-of-band by asking an administrator or consulting a database or something. But no one does that. When you type "yes" the connection proceeds without authentication and the public key is permanently added to `~/.ssh/known_hosts`. This is the _trust on first use_ (TOFU) anti-pattern.

Since certificate authentication uses certificates to communicate public key bindings, clients are always able to authenticate, even if it's the first time connecting to a host. **TOFU warnings go away.**

Certificate authentication also offers a convenient place to gate SSH with custom authentication: when the certificate is issued. This can be leveraged to further enhance SSH usability. In particular, it let's you extend single sign-on (SSO) to SSH. SSO for SSH is certificate authentication's biggest party trick. We'll return to this idea and see how it further enhances usability and security later. For now, let's move on to operability.

### [](#certificate-authentication-improves-operability)Certificate authentication improves operability

Eliminating key approval and distribution has immediate operational benefits. You're no longer wasting ops cycles on mundane key management tasks, and you eliminate any ongoing costs associated with monitoring and maintaining homegrown machinery for adding, removing, synchronizing, and auditing static public key files across your fleet.

The ability to issue SSH user certificates via a variety of authentication mechanisms also facilitates operational automation. If a cron job or script needs SSH access it can obtain an ephemeral SSH certificate automatically, when it's needed, instead of being pre-provisioned with a long-lived, static private key.

SSH public key authentication introduces some weird operational constraints around host names that certificate authentication eliminates. As we've seen, when an SSH client connects to a host for the first time it displays a TOFU warning to the user. When the user types "yes" the host's public key is added locally to `~/.ssh/known_hosts`. This binding between the host name and a specific public key is _permanent_. If the host presents a different public key later, the user gets an even scarier _host key verification failure_ error message that looks like this:

```
$ ssh ubuntu@ec2-54-161-77-102.compute-1.amazonaws.com
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the ECDSA key sent by the remote host is
SHA256:2ae53QcOB0W6HO+XtPmMXk7To/MvMuhFxTj8ZD7eSsE.
Please contact your system administrator.
Add correct host key in ~/.ssh/known_hosts to get rid of this message.
Offending ECDSA key in ~/.ssh/known_hosts:11
ECDSA host key for ec2-54-161-77-102.compute-1.amazonaws.com has changed and you have requested strict checking.
Host key verification failed.
```

Enter fullscreen mode Exit fullscreen mode

This makes it operationally challenging to reuse host names. If `prod01.example.com` has a hardware failure, and it's replaced with a new host using the same name, host key verification failures will ensue. This usually results in a bunch engineers contacting secops to tell them they're being hacked.

Ignoring host key verification failures has the exact same attack surface area as not knowing the key at all. Curiously, OpenSSH chooses to soft-fail with an easily bypassed prompt when the key isn't known (TOFU), but hard-fails with a much scarier and harder to bypass error when there's a mismatch.

In any case, certificates fix all of this since a current name-to-public-key binding is communicated when a connection is established. Changing the host's public key is fine, as long as the host also gets a new certificate. You can safely reuse host names and even run multiple hosts with the same name. You'll never see a host key verification failure again. Beyond name reuse, we'll soon see that eliminating host key verification failures is one of the many ways certificate authentication facilitates good security hygiene.

### [](#certificate-authentication-improves-security)Certificate authentication improves security

While the SSH protocol itself is secure, public key authentication encourages a bunch of bad security practices and makes good security hygiene hard to achieve.

With public key authentication, keys are trusted permanently. A compromised private key or illegitimate key binding may go unnoticed or unreported for a long time. Key management oversight (e.g., forgetting to remove an ex-employee's public keys from hosts) results in SSH failing open: unauthorized access without end.

Certificates, on the other hand, expire. In an incident — a mistake, theft, misuse, or key exfiltration of any form — compromised SSH credentials will expire automatically, without intervention, even if the incident goes unnoticed or unreported. **SSH certificates are fail-secure.** Access expires naturally if no action is taken to extend it. And when SSH users and hosts check in periodically with your CA to renew their credentials, a complete audit record is produced as a byproduct.

We've already seen how public key authentication trains users to ignore serious security warnings (TOFU) and triggers spurious security errors. This is more than an operational nuisance. Confusion caused by host key verification failure discourages host rekeying (i.e., replacing a host's key pair). Host private keys aren't very well protected, so periodic rekeying is good practice. Rekeying may be required after a breach or after offboarding a user. But, to avoid disruption from ensuing host key verification failures, it's often not done. Certificate authentication makes rekeying hosts trivial.

Public key authentication also makes rekeying difficult for users. Key approval and distribution is annoying enough that users are reluctant to rekey, even if you've built tools to make it possible. Worse, frustrated users copy private keys and reuse them across devices, often for many years. Key reuse is a serious security sin. Private keys are _never_ supposed to be transferred across a network. But SSH public key authentication exposes users directly to sensitive private keys, then fails to give them usable tools for key management. It's a recipe for misuse and abuse.

An SSH CA, coupled with a simple command-line client for users, can streamline key generation and insulate users from a lot of unnecessary detail. Certificate authentication can't completely eliminate all security risks, but it does facilitate SSH workflows that are more intuitive, easier to use, and harder to misuse.

To learn more about SSH certificates visit [the Smallstep website](https://smallstep.com/sso-ssh?utm_campaign=Dev.to&utm_source=dev.to). You can even try our free hosted offering and experience the value of SSH certificates in under five minutes!
