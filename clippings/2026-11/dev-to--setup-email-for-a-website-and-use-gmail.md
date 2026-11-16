---
url: "https://dev.to/ogrotten/setup-email-for-a-website-and-perform-send-receive-thru-your-main-gmail-3dme"
captured_at: "2026-11-16T01:10:42+00:00"
title: "Setup email for a website, and perform send/receive thru your main Gmail."
domain: "dev-to"
---

[![Cover image for Setup email for a website, and perform send/receive thru your main Gmail.](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fu532lhu70cb2j9csaujb.jpg)](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fu532lhu70cb2j9csaujb.jpg)

[![ogrotten](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F67612%2Fa80bb8fd-0b5b-4dc2-8ae5-e860d0428346.png)](https://dev.to/ogrotten)

[ogrotten](https://dev.to/ogrotten)

Posted on Jun 3, 2020 Edited on Jun 3, 2020

Having a portfolio site is cool and all, but I always felt it kinda janky to have a portfolio website and an email address that do not line up. After spending the better part of 2 days trying to find setup instructions, I finally tripped across the docs, and decided not to be [**DenverCoder9**](https://xkcd.com/979/).

Using Namecheap domain name registrar, and GMail as my email client, I have setup both services so that email intended for `you@yourdomain.com` can be sent and received, discreetly, in GMail. This can likely be setup with any services, but these instructions focus on Namecheap and Gmail.

This has no extra cost. The "Secure" or "Private" email service that Namecheap and other registrars offer is a _separate service and cost_ that is not required for this setup.

The end result will be that incoming email goes to your custom domain, and is then forwarded to your Gmail. Outgoing mail will do the reverse.

The Gmail setup requests permission for this by sending an email to the custom domain email with a confirmation link, so you need to have some kind of simple forwarding already setup. Once the process is completed, it will allow you to send email from within Gmail using the custom domain email as the "From" address.

These instructions assume you're using Namecheap. If you used a different registrar, the interface will be different but the configuration will be largely the same.

## [](#setup-namecheap)Setup Namecheap

Namecheap needs to be setup to forward your domain email to your gmail account.

1.  Login to Namecheap.
2.  On the left click `Domain List`.
3.  On the list, to the far right, click `Manage` next to the domain you want to setup email.
4.  Scroll down to the section `Redirect Email`.
5.  Click `Add Forwarder`. You **_could_** click `Add Catch-All` and then any email sent to any address @ your domain would be forwarded whether it was configured or not.
6.  `Alias` column: Enter _only the name_ of the custom domain email that you want redirected. So if your custom domain is example.com, and you are setting up for the email address [chrisrock@example.com](mailto:chrisrock@example.com), then in the `Alias` column you would put `chrisrock`.
7.  `Forward to` column: Enter the Gmail address where you want to receive the emails.
8.  Click the ✔ to the far right to save the config.

### [](#namecheap-part-ii)_Namecheap Part II_

1.  At the top click `Advanced DNS`.
2.  Scroll down to `Mail Settings`.
3.  On that line, it should already say `Email Forwarding`.
    
    _If it does not:_
    
    1.  Click the entry that is there to expose a dropdown
    2.  Choose `Email Forwarding`
    3.  Click the ✔ to save.

### [](#youre-done-with-namecheap)_You're done with Namecheap._

You could feasibly stop here as this is the simplest setup. Anything sent to your custom domain email will now be forwarded to your Gmail account. You would need to use your Gmail address as the "From" to send replies.

Continue below to setup a custom "From" address.

## [](#setup-gmail)Setup Gmail

Use this link to the original Gmail documentation on support.google.com.

> [Send an email from your alias in Gmail](https://support.google.com/domains/answer/9437157?hl=en)

## [](#when-gmail-setup-is-complete)When Gmail setup is complete...

1.  Refresh the Gmail tab.
2.  Click `Compose` to start a new email.
3.  In the New Message window, the `From` line should now be a dropdown. If you look, you should see your custom domain email.
4.  Send a test email: _From_ your regular Gmail address, _To_ your custom domain email. Put in some simple text and click send.
5.  Within a split second you should receive an email in the Gmail inbox.
6.  Open it, click Reply, click the _From_ dropdown, and choose your custom domain email. Put in some simple text and click send.
7.  Within a split second you should receive another email in the Gmail inbox, this time _From_ the custom domain email.

### [](#one-more-thing-in-gmail)_One more thing in Gmail:_

1.  ⚙Icon > `Settings` > `Accounts and Import` > section `Send mail as`
2.  Set your preference for `When replying to a message`.

* * *

This is the setup that worked for me. If there is a problem here or something missing, comment here and I'll look to fix it.
