---
title: "How to Enable and Secure Remote Desktop on Windows"
date: '2015-06-30T15:54:14-03:00'
category: webclip
summary: 'The guide explains how to turn on Remote Desktop in Windows, limit which users can log in, strengthen authentication and encryption, change the RDP port, and monitor logins.'
tags: ["remote-desktop", "windows", "security", "network-level-authentication"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to Enable and Secure Remote Desktop on Windows"
    url: "http://www.howtogeek.com/175087/how-to-enable-and-secure-remote-desktop-on-windows/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-06/howtogeek-com--how-to-enable-and-secure-remote-desktop-on-windows.md"
    kind: repo
---

The page shows how to enable Microsoft Remote Desktop on supported Windows editions and then tighten access so it is usable without leaving the computer exposed. It recommends strong passwords, limiting allowed users, enabling Network Level Authentication, and setting stronger security policies for RDP sessions.

It also suggests changing the default RDP port, updating Windows Firewall to allow that custom port, and checking Event Viewer to see who logs in and from where.

## Reading notes

- Enable Remote Desktop through System Properties and choose which users can connect.
- Prefer “Allow connections only from computers running Remote Desktop with Network Level Authentication” for better protection against man-in-the-middle attacks.
- Make sure power settings keep the computer from sleeping or hibernating when Remote Desktop is enabled.
- Grant access only to the accounts that need it, and use strong passwords with more than eight characters, ideally 12 or more, with mixed character types.
- In Local Security Policy, the page recommends removing the Administrators and Remote Desktop Users groups from “Allow log on through Remote Desktop Services,” then adding only specific users.
- In Group Policy, set the client connection encryption level to High, enable secure RPC communication, require SSL/TLS for RDP connections, and enable Network Level Authentication.
- Change the default RDP port from 3389 to a custom five-digit port as an extra precaution.
- After changing the port, create a Windows Firewall inbound rule for that port.
- To connect, use the computer name or IP address followed by the port number.
- To access the machine from outside the local network, forward the port on the router.
- Use Event Viewer under TerminalServices-LocalSessionManger > Operational to review logon events.
