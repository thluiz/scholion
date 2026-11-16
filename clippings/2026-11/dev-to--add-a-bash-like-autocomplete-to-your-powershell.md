---
url: "https://dev.to/ofhouse/add-a-bash-like-autocomplete-to-your-powershell-4257"
captured_at: "2026-11-16T19:22:09+00:00"
title: "Add a Bash-like autocomplete to your PowerShell"
domain: "dev-to"
---

[![Cover image for Add a Bash-like autocomplete to your PowerShell](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fthepracticaldev.s3.amazonaws.com%2Fi%2Fca4b14ss88ebs85gpaf3.jpg)](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fthepracticaldev.s3.amazonaws.com%2Fi%2Fca4b14ss88ebs85gpaf3.jpg)

[![Felix Haus](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F244702%2F25d44934-65d9-461b-b8e6-43763133a37b.jpg)](https://dev.to/ofhouse)

[Felix Haus](https://dev.to/ofhouse)

Posted on Dec 27, 2019 Edited on Jun 15, 2022

I mostly use Ubuntu or MacOS for development, but recently I switched sides because I needed the power from my Windows gaming machine to start playing around with Blender and Unreal Engine.

What I missed much when using the PowerShell console was the autocomplete ability which Bash offers:

*   When you begin to type a command and hit Tab Bash shows you all available commands which begin with the phrase you typed and you can then select the one you want with the arrow keys.
    
    PowerShell by default only completes the command immediately without showing you all available commands.
    
*   If you already started typing the beginning of a command you can use ↑ / ↓ to cycle through your history to autocomplete the command with the parameters you have used before.
    
    Cycling through the history with the arrow keys is also supported by PowerShell but it completely ignores what you have already typed and replaces everything with the last used command from the history.
    

## [](#enable-better-autocompletion-in-your-powershell)Enable better autocompletion in your PowerShell

![Autocomplete in PowerShell](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fbppf8a6dfjc0i5rwkuju.gif)

Thankfully PowerShell already has this functionality built-in provided by a module called `PSReadline`.  
You simply have to enable it in your PowerShell profile (The PowerShell equivalent to your `.bashrc`) 👏:

1.  Open or create a new [PowerShell Profile](https://docs.microsoft.com/en-us/powershell/scripting/components/ise/how-to-use-profiles-in-windows-powershell-ise?view=powershell-6#selecting-a-profile-to-use-in-the-windows-powershell-ise) by typing the following commands directly in your PowerShell:  
    
    ```
    # Create profile when not exist
    if (!(Test-Path -Path $PROFILE.CurrentUserAllHosts)) {
      New-Item -ItemType File -Path $PROFILE.CurrentUserAllHosts -Force
    }
    
    # Open the profile with an editor (e.g. good old Notepad)
    ii $PROFILE.CurrentUserAllHosts
    ```
    
2.  In the editor add the following lines to the profile:  
    
    ```
    # Shows navigable menu of all options when hitting Tab
    Set-PSReadlineKeyHandler -Key Tab -Function MenuComplete
    
    # Autocompletion for arrow keys
    Set-PSReadlineKeyHandler -Key UpArrow -Function HistorySearchBackward
    Set-PSReadlineKeyHandler -Key DownArrow -Function HistorySearchForward
    ```
    
3.  Save the file and reopen your PowerShell, now you can use the advanced autocomplete features.
    

_Credit for this goes to StackOverflow users [svick](https://stackoverflow.com/a/37715242/831465) and [JerryGoyal](https://stackoverflow.com/a/59334852/831465) which have posted this in their answers._

## [](#bonus-add-the-raw-open-endraw-command-from-macos-to-your-powershell)Bonus: Add the `open` command from MacOS to your PowerShell

On MacOS there is the powerful `open` command to open folders in Finder (the file explorer from MacOS) or files with their default application from the terminal.  
PowerShell also has this command built-in which is called `ii` (Which stands for [Invoke-Item](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/invoke-item)).  
Because I find the term `ii` hard to remember I added an `open` alias for it which makes it more convenient when switching between the platforms.

Adding a new alias to the PowerShell profile is really simple with the [`New-Alias`](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/new-alias) command, so simply edit your profile and add the following line:  

```
# New-Alias <alias> <aliased-command>
New-Alias open ii
```

Enter fullscreen mode Exit fullscreen mode

Save it and reopen your PowerShell and test it by typing `open .` to open an Windows explorer window in your working directory.

## [](#last-tip-use-the-new-windows-terminal)Last tip: Use the new Windows Terminal

To make your PowerShell experience even better you should also install the new Windows Terminal preview from the Microsoft store:  
[https://www.microsoft.com/store/productId/9N0DX20HK701](https://www.microsoft.com/store/productId/9N0DX20HK701)

It offers tabs and a better customization than the default console in Windows.

* * *

_I am still pretty new to PowerShell so if you have other tips to increase the productivity like this I would love when you leave a comment here._ 💖

[![Sentry image](https://media2.dev.to/dynamic/image/width=775%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimages.ctfassets.net%2Fem6l9zw4tzag%2F1GYxa0VJ4TOkpKyV4TaIur%2F34e4f6e2f1068894f9d0738008646289%2Fmcp-config.png%3Fw%3D1500%26h%3D1003%26q%3D50%26fm%3Dwebp)](https://blog.sentry.io/smarter-debugging-sentry-mcp-cursor/?utm_source=devto&utm_medium=paid-community&utm_campaign=smarter-debugging-mcp-cursor-blog&bb=240306)

## [](#smarter-debugging-with-sentry-mcp-and-cursor)[Smarter debugging with Sentry MCP and Cursor](https://blog.sentry.io/smarter-debugging-sentry-mcp-cursor/?utm_source=devto&utm_medium=paid-community&utm_campaign=smarter-debugging-mcp-cursor-blog&bb=240306)

No more copying and pasting error messages, logs, or trying to describe your distributed tracing setup or stack traces in chat. MCP can investigate real issues, understand their impact, and suggest fixes based on the actual production context.

[Read more →](https://blog.sentry.io/smarter-debugging-sentry-mcp-cursor/?utm_source=devto&utm_medium=paid-community&utm_campaign=smarter-debugging-mcp-cursor-blog&bb=240306)
