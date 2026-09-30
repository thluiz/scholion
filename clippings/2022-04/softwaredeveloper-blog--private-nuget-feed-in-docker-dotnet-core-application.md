---
url: "https://www.softwaredeveloper.blog/private-nuget-feed-in-docker"
captured_at: "2022-04-05T18:36:54-03:00"
title: "Private Nuget feed in Docker .Net Core application"
domain: "softwaredeveloper-blog"
---

Using public _Nuget_ from [Nuget.org](https://www.nuget.org/) is always easy, you just need internet connection. But when you need private _Nuget feed_ it sometimes doesn’t want to work, especially in isolated _Docker container_.

## Why private _nuget_ feed won’t work in Docker without additional effort

When you restore _nuget_ packages in your Windows, then access to feed is granted because of your credentials stored by _OS_. When you try to access private _nuget_ packages in _Docker_ then your credentials are not accessible (and you wouldn’t want to use them in _CI/CD pipeline_) so you need to resolve it some other way.

## How to access private _nuget_ packages in _Docker_

In theory, it should be easy, it should just end up with passing proper credentials to _Docker_ somehow. In my case it was more difficult and I think similar problems are common, so I will share all steps I had to do.

### Use _nuget_ config file in _Dockerfile_ to pass credentials to _Docker_

First you have to pass _nuget_ config file in _Dockerfile_. To do so, you can use `--configfile Nuget.config` option in _dotnet publish/restore_ commands. This file should be stored at solution level, not to need copy-paste it for every image from solution. Remember to set proper path (or/and copy it to convenient directory in image), otherwise you will see error claiming that this file doesn’t exist:

```
/usr/share/dotnet/sdk/2.1.803/NuGet.targets(525,5): error : File '/app/Nuget.config' does not exist.
```

You can read more about _Nuget.config_ file with examples and explanations in [official documentation](https://docs.microsoft.com/en-us/nuget/reference/nuget-config-file).

### Establishing ssl connection to private Docker feed

Next I faced error while trying to establish encrypted connection to my Azure DevOps server _nuget feed_.

It was something like this:

```
System.Net.Http.HttpRequestException: The SSL connection could not be established, see inner exception. 
---> System.Security.Authentication.AuthenticationException: Authentication failed, see inner exception. 
---> System.ComponentModel.Win32Exception: The client and server cannot communicate, because they do not possess a common algorithm
   --- End of inner exception stack trace ---
   at System.Net.Security.SslState.StartSendAuthResetSignal(ProtocolToken message, AsyncProtocolRequest asyncRequest, ExceptionDispatchInfo exception)
   at System.Net.Security.SslState.CheckCompletionBeforeNextReceive(ProtocolToken message, AsyncProtocolRequest asyncRequest)
   at System.Net.Security.SslState.StartSendBlob(Byte[] incoming, Int32 count, AsyncProtocolRequest asyncRequest)
   at System.Net.Security.SslState.ProcessReceivedBlob(Byte[] buffer, Int32 count, AsyncProtocolRequest asyncRequest)
   at System.Net.Security.SslState.StartReadFrame(Byte[] buffer, Int32 readBytes, AsyncProtocolRequest asyncRequest)
   at System.Net.Security.SslState.PartialFrameCallback(AsyncProtocolRequest asyncRequest)
```

I solved this one by adding `DOTNET_SYSTEM_NET_HTTP_USESOCKETSHTTPHANDLER=0` before using dotnet publish, like this:

```
RUN DOTNET_SYSTEM_NET_HTTP_USESOCKETSHTTPHANDLER=0 dotnet publish project -c Release --configfile Nuget.config
```

### Still not able to authenticate - Response status code does not indicate success: 401 (Unauthorized)

After doing above steps I still faced issue while trying to use this _nuget feed_. I knew that credentials I used were corrected, the account which I used was created especially for _nuget_ purposes and I knew that it had all proper permissions set and still was not able to connect. Error said:

```
/usr/share/dotnet/sdk/2.1.803/NuGet.targets(123,5): error : Unable to load the service index for source http://myazuredevopsserver:8080/tfs/DefaultCollection/_packaging/PackageFeed/nuget/v3/index.json. [/app/App.csproj]

/usr/share/dotnet/sdk/2.1.803/NuGet.targets(123,5): error : Response status code does not indicate success: 401 (Unauthorized). [/app/App.csproj]

The command '/bin/sh -c DOTNET_SYSTEM_NET_HTTP_USESOCKETSHTTPHANDLER=0 dotnet restore App --configfile Nuget.config' returned a non-zero code: 1
```

Azure DevOps server admin didn’t know why and couldn’t read it from server logs so suggested trying another approach, which by the way may be good for security - using [authentication with PAT (personal access token)](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&tabs=preview-page). He generated such a token, and we passed this token to _Nuget.config_ file and feed finally started to work. Now it looks like this:

```
<?xml version="1.0" encoding="utf-8"?>
<configuration>
<config>
    <add key="http_proxy" value="http://myazuredevopsserver:8080@company.corp" />
</config>
  <packageSources>
    	<clear />
    <add key="nuget.org" value="https://api.nuget.org/v3/index.json" />
    <add key="Internal" value="http://myazuredevopsserver:8080/tfs/DefaultCollection/_packaging/CompanyPackageFeed/nuget/v3/index.json" />
  </packageSources>
	<activePackageSource>
		<add key="All" value="(Aggregate source)" />
	</activePackageSource>
  <packageSourceCredentials>
          <Internal>
            <add key="Username" value="xxx" />
            <add key="ClearTextPassword" value="xxx" />
            <add key="ValidAuthenticationTypes" value="basic" />
          </Internal>
  </packageSourceCredentials>
</configuration>
```

Where _xxx_ is the token (exactly the same value passed both to _Username_ and _ClearTextPassword_ field). Note that (as far as I know) this token can be generated max for 1 year, so better set some reminder in your calendar, or red builds in build server will remind it for you after a year :)

### Local _Nuget feed_ as a last resort

For a while till I didn’t get this working I created [local Nuget feed](https://docs.microsoft.com/en-us/nuget/hosting-packages/local-feeds), to have some workaround until I figured out proper solution. With local feed you can store _Nugets_ in local directory and commit it to repo. But of course you need to maintain it by yourself, manually or with some automation which will commit new _Nuget_ versions for you, so I don’t recommend it until it’s really the only way to get job done.  
There are articles on the internet how to set it up, I will just show you screenshot of how it looked in my case (it’s actually screenshot from commit which removed it from my project): ![Screenshot showing Nuget.config file with local Nuget feed](https://www.softwaredeveloper.blog/assets/images/local-nuget-feed.jpg "Nuget.config file with local Nuget feed")

## Summary

I must admit that this problem ate much of my time, moreover I had to ask Azure DevOps server admin for help with reading server logs, and trying to figure out how to solve it. I didn’t have time to write this post earlier, but questions about private feed were common in my inbox, so I know that many of you face similar issues.

If your case is yet different, feel free to ask question in comment. And of course feedback is welcome, if this article has helped you or is missing something, it is very valuable for me to know it :)

### Stay up to date!

Get all the latest & greatest posts  
delivered straight to your inbox
