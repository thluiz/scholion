---
url: "http://www.howtogeek.com/175087/how-to-enable-and-secure-remote-desktop-on-windows/"
captured_at: "2015-06-30T15:54:14-03:00"
title: "How to Enable and Secure Remote Desktop on Windows"
domain: "howtogeek-com"
---

# [How to Enable and Secure Remote Desktop on Windows](http://www.howtogeek.com/175087/how-to-enable-and-secure-remote-desktop-on-windows/ "How to Enable and Secure Remote Desktop on Windows")

![650x275x1-rdpconnection.jpg.pagespeed.ic.NQnIg1Wqey.webp](howtogeek-com--how-to-enable-and-secure-remote-desktop-on-windows/3509c88355aa7b200761d2b464631622.webp)

While there are many alternatives, Microsoft’s Remote Desktop is a perfectly viable option for accessing other computers, but it has to be properly secured.  After recommended security measures are in place, Remote Desktop is a powerful tool for geeks to use and lets you avoid installing third party apps for this type of functionality.

This guide and the screenshots that accompany it are made for Windows 8.1.  However, you should be able to follow this guide as long as you’re using one of these editions of Windows:

- Windows 8.1 Pro
- Windows 8.1 Enterprise
- Windows 8 Enterprise
- Windows 8 Pro
- Windows 7 Professional
- Windows 7 Enterprise
- Windows 7 Ultimate
- Windows Vista Business
- Windows Vista Ultimate
- Windows Vista Enterprise
- Windows XP Professional

### Enabling Remote Desktop

First, we need to enable Remote Desktop and select which users have remote access to the computer.  Hit Windows key + R to bring up a Run prompt, and type “sysdm.cpl.”

![413x213x2-runpromptsysdmcpl.jpg.pagespeed.ic.i2zlVNqR0i.webp](howtogeek-com--how-to-enable-and-secure-remote-desktop-on-windows/8b6ce554da91d221d6057f704bfe2edc.webp)

Another way to get to the same menu is to type “This PC” in your Start menu, right click “This PC” and go to Properties:

![315x324x3-thispc.jpg.pagespeed.ic.Qw5x6YgHD8.webp](howtogeek-com--how-to-enable-and-secure-remote-desktop-on-windows/430e71e988070fc0d22240e5ea999afc.webp)

Either way will bring up this menu, where you need to click on the Remote tab:

![4-systemproperties.jpg](howtogeek-com--how-to-enable-and-secure-remote-desktop-on-windows/e420c74d4cad7a08ae9d02d629d29bf8.jpg)

Select “Allow remote connections to this computer” and the option below it, “Allow connections only from computers running Remote Desktop with Network Level Authentication.”

It’s not a necessity to require Network Level Authentication, but doing so makes your computer more secure by protecting you from [Man in the Middle attacks](http://www.howtogeek.com/glossary/man-in-the-middle-attack/).  Systems even as old as Windows XP can connect to hosts with Network Level Authentication, so there’s no reason not to use it.

You may get a warning about your power options when you enable Remote Desktop:

![5-poweroptions.jpg](howtogeek-com--how-to-enable-and-secure-remote-desktop-on-windows/05579ab9775dcf52cd3500e8c17f075e.jpg)

If so, make sure you click the link to Power Options and configure your computer so it doesn’t fall asleep or hibernate.  See our article on [managing power settings](http://www.howtogeek.com/howto/9090/learning-windows-7-manage-power-settings/) if you need help.

Next, click “Select Users.”

![6-selectusers.jpg](howtogeek-com--how-to-enable-and-secure-remote-desktop-on-windows/8e506253a4d2440bbb66436c24b7d7fe.jpg)

Any accounts in the Administrators group will already have access.  If you need to grant Remote Desktop access to any other users, just click “Add” and type in the usernames.

![7-addusers.jpg](howtogeek-com--how-to-enable-and-secure-remote-desktop-on-windows/9d70bfd19786a9635b7a9f84d0045ad1.jpg)

Click “Check Names” to verify the username is typed correctly and then click OK.  Click OK on the System Properties window as well.

### Securing Remote Desktop

Your computer is currently connectable via Remote Desktop (only on your local network if you’re behind a router), but there are some more settings we need to configure in order to achieve maximum security.

First, let’s address the obvious one.  All of the users that you gave Remote Desktop access need to have strong passwords.  There are a lot of bots constantly scanning the internet for vulnerable PCs running Remote Desktop, so don’t underestimate the importance of a strong password.  Use more than eight characters (12+ is recommended) with numbers, lowercase and uppercase letters, and special characters.

Go to the Start menu or open a Run prompt (Windows Key + R) and type “secpol.msc” to open the Local Security Policy menu.

![8-secpol.jpg](howtogeek-com--how-to-enable-and-secure-remote-desktop-on-windows/fa73f48be15d7a211303b6bfb72877dd.jpg)

Once there, expand “Local Policies” and click on “User Rights Assignment.”

![9-localsecuritypolicy.jpg](howtogeek-com--how-to-enable-and-secure-remote-desktop-on-windows/22f994543997fe9ab1628c4fffa40801.jpg)

Double-click on the “Allow log on through Remote Desktop Services” policy listed on the right.

![10-allowlogon.jpg](howtogeek-com--how-to-enable-and-secure-remote-desktop-on-windows/5834166b93919d8c4e05e6390e816400.jpg)

It’s our recommendation to remove both of the groups already listed in this window, Administrators and Remote Desktop Users.  After that, click “Add User or Group” and manually add the users you’d like to grant Remote Desktop access to.  This isn’t an essential step, but it gives you more power over which accounts get to use Remote Desktop.  If, in the future, you make a new Administrator account for some reason and forget to put a strong password on it, you’re opening your computer up to hackers around the world if you never bothered removing the “Administrators” group from this screen.

Close the Local Security Policy window and open the Local Group Policy Editor by typing “gpedit.msc” into either a Run prompt or the Start menu.

![11-gpeditmsc.jpg](howtogeek-com--how-to-enable-and-secure-remote-desktop-on-windows/58271a92a726661c862adebf01a34b56.jpg)

When the Local Group Policy Editor opens, expand Computer Policy > Administrative Templates > Windows Components > Remote Desktop Services > Remote Desktop Session Host, and then click on Security.

![12-grouppolicy.jpg](howtogeek-com--how-to-enable-and-secure-remote-desktop-on-windows/c839819af57692ce8bad1da267bd85ee.jpg)

Double-click on any settings in this menu to change their values.  The ones we recommend changing are:

Set client connection encryption level – Set this to High Level so your Remote Desktop sessions are secured with 128-bit encryption.

![13-encryption.jpg](howtogeek-com--how-to-enable-and-secure-remote-desktop-on-windows/f57753398d5e092b0e4ae20c027636d1.jpg)

Require secure RPC communication – Set this to Enabled.

Require use of specific security layer for remote (RDP) connections – Set this to SSL (TLS 1.0).

Require user authentication for remote connections by using Network Level Authentication – Set this to Enabled.

Once those changes have been made, you can close the Local Group Policy Editor.  The last security recommendation we have is to change the default port that Remote Desktop listens on.  This is an optional step and is considered a security through obscurity practice, but the fact is that changing the default port number greatly decreases the amount of malicious connection attempts that your computer will receive.  Your password and security settings need to make Remote Desktop invulnerable no matter what port it is listening on, but we might as well decrease the amount of connection attempts if we can.

### Security through Obscurity: Changing the Default RDP Port

By default, Remote Desktop listens on port 3389.  Pick a five digit number less than 65535 that you’d like to use for your custom Remote Desktop port number.  With that number in mind, open up the Registry Editor by typing “regedit” into a Run prompt or the Start menu.

![14-regedit.jpg](howtogeek-com--how-to-enable-and-secure-remote-desktop-on-windows/1386b9a7fc0328a034150a76ccf9955b.jpg)

When the Registry Editor opens up, expand HKEY\_LOCAL\_MACHINE > SYSTEM > CurrentControlSet > Control > Terminal Server > WinStations > RDP-Tcp > then double-click on “PortNumber” in the window on the right.

![15-pornnumber.jpg](howtogeek-com--how-to-enable-and-secure-remote-desktop-on-windows/d23c23d1ae3abbe474529933d8ad64e9.jpg)

With the PortNumber registry key open, select “Decimal” on the right side of the window and then type your five digit number under “Value data” on the left.

![16-pornumber.jpg](howtogeek-com--how-to-enable-and-secure-remote-desktop-on-windows/3f570c5ede05cbc982e466c23d132196.jpg)

Click OK and then close the Registry Editor.

Since we’ve changed the default port that Remote Desktop uses, we’ll need to configure Windows Firewall to accept incoming connections on that port.  Go to the Start screen, search for “Windows Firewall” and click on it.

![17-firewallsearch.jpg](howtogeek-com--how-to-enable-and-secure-remote-desktop-on-windows/1b1cebc2e8d79a54a53a7a3f038fb4f9.jpg)

When Windows Firewall opens, click “Advanced Settings” on the left side of the window.  Then right-click on “Inbound Rules” and choose “New Rule.”

![18-newrule.jpg](howtogeek-com--how-to-enable-and-secure-remote-desktop-on-windows/f0e286e614c4526a2479b957905b8bf4.jpg)

The “New Inbound Rule Wizard” will pop up, select Port and click next.  On the next screen, make sure TCP is selected and then enter the port number you chose earlier, and then click next.  Click next two more times because the default values on the next couple pages will be fine.  On the last page, select a name for this new rule, such as “Custom RDP port,” and then click finish.

### Last Steps

Your computer should now be accessible on your local network, just specify either the IP address of the machine or the name of it, followed by a colon and the port number in both cases, like so:

![19-connecting.jpg](howtogeek-com--how-to-enable-and-secure-remote-desktop-on-windows/a470acfac88a6ac2b170f5edaf60a370.jpg)

To access your computer from outside your network, you’ll more than likely need to [forward the port on your router](http://www.howtogeek.com/66214/).  After that, your PC should be remotely accessible from any device that has a Remote Desktop client.

If you’re wondering how you can keep track of who is logging into your PC (and from where), you can open up Event Viewer to see.

![20-vieweventlogs.jpg](howtogeek-com--how-to-enable-and-secure-remote-desktop-on-windows/0ff697bd872a1e73eab74d15209f2ad0.jpg)

Once you have Event Viewer opened, expand Applications and Services Logs > Microsoft > Windows > TerminalServices-LocalSessionManger and then click Operational.

![21-eventviewer.jpg](howtogeek-com--how-to-enable-and-secure-remote-desktop-on-windows/c5a5c37ac8724745f38ba05eb59ce7b7.jpg)

Click on any of the events in the right pane to see login information.
