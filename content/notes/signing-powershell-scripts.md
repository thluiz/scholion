---
title: "Signing PowerShell Scripts"
date: '2013-11-10T13:41:31-03:00'
category: webclip
summary: 'Explains PowerShell execution policies, how to create a self-signed code-signing certificate, sign a .ps1 file, and move the needed certificates so the script runs on another computer.'
tags: ["powershell", "code-signing", "certificates", "execution-policies"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Signing PowerShell Scripts - Scott Hanselman"
    url: "http://www.hanselman.com/blog/SigningPowerShellScripts.aspx"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-11/hanselman-com--signing-powershell-scripts.md"
    kind: repo
---

PowerShell execution policies control which files can be loaded for execution and configuration. The page describes the four policies, shows that Restricted is the default, and explains that AllSigned is useful in production because it requires digital signatures on scripts and configuration files.

It then walks through creating a self-signed certificate with makecert, verifying it in the certificate store, signing a script with Set-AuthenticodeSignature, and running it under AllSigned. It also shows that a signed script can fail on another machine unless the root certificate is exported and imported there, and that Trusted Publishers may also need to be imported to avoid the first-run prompt.

## Reading notes

- PowerShell execution policies define the restrictions under which files are loaded for execution and configuration.
- The four policies listed are Restricted, AllSigned, RemoteSigned, and Unrestricted.
- Restricted is the default policy and works as an interactive shell only.
- AllSigned is presented as the best choice for production because it requires signatures on all scripts and configuration files.
- A digital signature requires a code signing certificate.
- The page distinguishes between certificates from a certificate authority and self-signed certificates.
- Self-signing is described as useful for internal scripts because it is free and quick.
- The drawback of self-signing is that the certificate must be installed on every computer that will run the scripts.
- makecert.exe is used to create the self-signed certificate.
- The article shows how to verify the generated certificate with Get-ChildItem cert:\CurrentUser\My -codesign.
- Signing a script adds a signature block to the end of the file.
- Under AllSigned, an unsigned script is blocked from running.
- After signing, PowerShell prompts the first time to confirm trust in the publisher.
- If the certificate is missing, the script fails.
- A signed script can be validated on another computer only after the relevant certificate is exported and imported there.
- Importing the Trusted Publishers certificate can prevent the first-time prompt.
