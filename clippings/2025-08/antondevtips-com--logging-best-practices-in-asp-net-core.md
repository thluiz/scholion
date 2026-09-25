---
url: "https://antondevtips.com/blog/logging-best-practices-in-asp-net-core?utm_source=email&utm_medium=email&utm_campaign=website"
captured_at: "2025-08-11T15:12:34+01:00"
title: "Logging Best Practices in ASP.NET Core"
domain: "antondevtips-com"
---

---
Logging is an essential aspect of any application, especially in a production environment. Logging provides crucial insights into the behavior of your application, helping to diagnose issues, track the flow of execution, and monitor performance.

In this blog post, I will share with you my experience on what are the best practices for implementing logging in ASP.NET Core applications.

## Best Practise 1: Use Serilog Library for Logging

ASP.NET Core has a built-in logging provider - `Microsoft.Extensions.Logging`. While it is a good option, it lacks some important features.

So I recommend using Serilog as a logging library that is very performant and supports structured logging. It adds on top of `Microsoft.Extensions.Logging` package, and you don't need to add a Serilog package to all your projects.

Serilog has a big ecosystem of sinks, and its flexibility in configuration makes it an excellent choice for logging. Sink is a source where you can output and store your logs, it can be a console, file, database, or a monitoring system.

To get started with Serilog in an ASP.NET Core application, install the following Nuget packages:

```
<p><code id="code-lang-bash"><span>dotnet </span><span ne="0.6355707853923825">add</span><span> package Serilog.AspNetCore
</span><span>dotnet </span><span ne="0.22326804322606586">add</span><span> package Serilog.Sinks.Console
</span><span>dotnet </span><span ne="0.16360481944605576">add</span><span> package Serilog.Sinks.File</span></code></p>
```

Then add the following configuration to your `appsettings.json` file to configure logging to Console and File:

```
<p><code id="code-lang-json"><span ne="0.7044989599156318">{</span><span>
</span><span>  </span><span ne="0.1384702139562889">"Serilog"</span><span ne="0.10138354793690862">:</span><span> </span><span ne="0.001384317819442149">{</span><span>
</span><span>    </span><span ne="0.03376151445031672">"Using"</span><span ne="0.5018585350976091">:</span><span> </span><span ne="0.6812422398453317">[</span><span>
</span><span>      </span><span ne="0.8028712405587873">"Serilog.Sinks.Console"</span><span ne="0.8780138860357694">,</span><span>
</span><span>      </span><span ne="0.6406251828367411">"Serilog.Sinks.File"</span><span>
</span><span>    </span><span ne="0.5427096804183">]</span><span ne="0.9024477662394845">,</span><span>
</span><span>    </span><span ne="0.8487282256496324">"MinimumLevel"</span><span ne="0.6823036125980444">:</span><span> </span><span ne="0.08540778989239095">{</span><span>
</span><span>      </span><span ne="0.3852766260499749">"Default"</span><span ne="0.9156734732180696">:</span><span> </span><span ne="0.42323182735754805">"Debug"</span><span ne="0.6325859218682562">,</span><span>
</span><span>      </span><span ne="0.8064471731315609">"Override"</span><span ne="0.16882401059803032">:</span><span> </span><span ne="0.6428054648619244">{</span><span>
</span><span>        </span><span ne="0.23260319940328122">"Microsoft"</span><span ne="0.6011352231346094">:</span><span> </span><span ne="0.45584617129152494">"Information"</span><span>
</span><span>      </span><span ne="0.38744823928582306">}</span><span>
</span><span>    </span><span ne="0.26128989703043837">}</span><span ne="0.5004716673044132">,</span><span>
</span><span>    </span><span ne="0.03695999643354664">"WriteTo"</span><span ne="0.1846923319946353">:</span><span> </span><span ne="0.004444690359637793">[</span><span>
</span><span>      </span><span ne="0.06910569246435805">{</span><span> </span><span ne="0.8004590775742764">"Name"</span><span ne="0.9550480418866556">:</span><span> </span><span ne="0.7644565082874956">"Console"</span><span> </span><span ne="0.3789808087008881">}</span><span ne="0.16788939866636954">,</span><span>
</span><span>      </span><span ne="0.5578965866812109">{</span><span> </span><span ne="0.03069148940877786">"Name"</span><span ne="0.8149114889521074">:</span><span> </span><span ne="0.7877175951777532">"File"</span><span ne="0.4589444181577893">,</span><span> </span><span ne="0.9465867966773291">"Args"</span><span ne="0.263095629276046">:</span><span> </span><span ne="0.06979679057508437">{</span><span> </span><span ne="0.07103349706332751">"path"</span><span ne="0.4593897013252849">:</span><span> </span><span ne="0.6466579149687005">"service.log"</span><span ne="0.46593082877437564">,</span><span> </span><span ne="0.0014253208696844988">"rollingInterval"</span><span ne="0.8201128250132438">:</span><span> </span><span ne="0.7187244176488489">"Day"</span><span> </span><span ne="0.5004129291086302">}</span><span> </span><span ne="0.06856333036756479">}</span><span>
</span><span>    </span><span ne="0.6902067815672023">]</span><span ne="0.33993362925237713">,</span><span>
</span><span>    </span><span ne="0.1117999916675585">"Enrich"</span><span ne="0.08442989123834466">:</span><span> </span><span ne="0.9663755972006829">[</span><span> </span><span ne="0.9162497204669944">"FromLogContext"</span><span ne="0.3389044956486925">,</span><span> </span><span ne="0.11752072237664035">"WithMachineName"</span><span ne="0.25791548361481487">,</span><span> </span><span ne="0.45208470354456365">"WithThreadId"</span><span> </span><span ne="0.6569229051981234">]</span><span ne="0.45750565790107156">,</span><span>
</span><span>    </span><span ne="0.2786871106356337">"Properties"</span><span ne="0.8862083994910106">:</span><span> </span><span ne="0.4124629146614016">{</span><span>
</span><span>      </span><span ne="0.3545745425518655">"Application"</span><span ne="0.3809398838694157">:</span><span> </span><span ne="0.3204144729653565">"ApplicationName"</span><span>
</span><span>    </span><span ne="0.06065905981705677">}</span><span>
</span><span>  </span><span ne="0.7121369616922514">}</span><span>
</span><span></span><span ne="0.7432277237779861">}</span></code></p>
```

The final step is to register Serilog to work on top of Microsoft Logging:

```
<p><code id="code-lang-csharp"><span ne="0.4838189735305538">var</span><span> builder </span><span ne="0.27440518742110953">=</span><span> WebApplication</span><span ne="0.1553657470161155">.</span><span ne="0.7497552024992438">CreateBuilder</span><span ne="0.16079449928087497">(</span><span>args</span><span ne="0.8776457227117767">)</span><span ne="0.7110189793193471">;</span><span>
</span><span>builder</span><span ne="0.6875359894079734">.</span><span>Host</span><span ne="0.17409529284950254">.</span><span ne="0.738207686584259">UseSerilog</span><span ne="0.9124961444373354">(</span><span ne="0.8410310830320792">(</span><span>context</span><span ne="0.3687199804425725">,</span><span> loggerConfig</span><span ne="0.23996349623443114">)</span><span> </span><span ne="0.691305941101703">=&gt;</span><span>
</span><span>    loggerConfig</span><span ne="0.8586399223526322">.</span><span>ReadFrom</span><span ne="0.6531760998024366">.</span><span ne="0.7808291417033413">Configuration</span><span ne="0.7936664483656328">(</span><span>context</span><span ne="0.9397971167009651">.</span><span>Configuration</span><span ne="0.6362611769457979">)</span><span>
</span><span></span><span ne="0.9468652755338265">)</span><span ne="0.7018869980987985">;</span></code></p>
```

You can use `ILogger` from the `Serilog` namespace, or you can continue using `ILogger` from the `Microsoft.Extensions.Logging` namespace and Serilog will handle logging in both cases.

You can find the full list of supported Sinks [in the Serilog GitHub page](https://github.com/serilog/serilog/wiki/Provided-Sinks).

## Best Practise 2: Use The Appropriate Logging Level

When logging, you need to use various types of log levels depending on each message's importance:

-   **Trace:** logs that contain the most detailed messages. These messages may contain sensitive application data. They are disabled by default and should be used sparingly.
-   **Debug:** logs that are used for interactive investigation during development. These should primarily be enabled during development and testing.
-   **Information:** logs that track the general flow of the application. These logs should have long-term value.
-   **Warning:** logs that highlight an unexpected event in the application flow but do not cause the application to stop.
-   **Error:** logs that highlight when the current flow of execution is stopped due to a failure. These should indicate a failure in the current activity or request.
-   **Critical:** logs that describe an unrecoverable application or system crash, or a catastrophic failure that requires immediate attention.

By default, in most of the applications, the default logging level should be set to `Info` or `Warning`. Make sure to log the most important information for your application. Enable `Debug` and `Trace` in production when you need extra information or need to investigate any issues.

## Best Practise 3: Use Logging Filters

Logs can be huge, that can take from gigabytes to terabytes of space. That's why you need to log only the important information.

I recommend using logging filters in Serilog to control what is logged. With log filters, you can specify a minimum logging level for each logging namespace, for example:

```
<p><code id="code-lang-json"><span ne="0.26562942185553984">{</span><span>
</span><span>  </span><span ne="0.015971730853286736">"Serilog"</span><span ne="0.10492373103734198">:</span><span> </span><span ne="0.7815326206964174">{</span><span>
</span><span>    </span><span ne="0.9375911285682814">"MinimumLevel"</span><span ne="0.47059203112573345">:</span><span> </span><span ne="0.604095946394421">{</span><span>
</span><span>      </span><span ne="0.38795596239387464">"Default"</span><span ne="0.38725380889293237">:</span><span> </span><span ne="0.3435329606359312">"Debug"</span><span ne="0.005858341136064205">,</span><span>
</span><span>      </span><span ne="0.6055341378689397">"Override"</span><span ne="0.603253997393729">:</span><span> </span><span ne="0.9215624854881491">{</span><span>
</span><span>        </span><span ne="0.8300581285112743">"Microsoft"</span><span ne="0.9816372548165844">:</span><span> </span><span ne="0.5987139597844051">"Information"</span><span ne="0.17479750801357397">,</span><span>
</span><span>        </span><span ne="0.9962319729294886">"OpenTelemetry"</span><span ne="0.25822420611166574">:</span><span> </span><span ne="0.9938568191115398">"Debug"</span><span ne="0.8837101633811565">,</span><span>
</span><span>        </span><span ne="0.1400391243393334">"Quartz"</span><span ne="0.7519629520629246">:</span><span> </span><span ne="0.13027283642577736">"Information"</span><span ne="0.35109598533808795">,</span><span>
</span><span>        </span><span ne="0.9047020708077127">"Microsoft.AspNetCore.Mvc"</span><span ne="0.8591427793547165">:</span><span> </span><span ne="0.8898216335238536">"Warning"</span><span ne="0.3743059504948244">,</span><span>
</span><span>        </span><span ne="0.899882766604889">"Microsoft.AspNetCore.Routing"</span><span ne="0.653661453020374">:</span><span> </span><span ne="0.1759887971041857">"Warning"</span><span ne="0.7156749595989462">,</span><span>
</span><span>        </span><span ne="0.5403043698895174">"Microsoft.AspNetCore.HttpLogging.HttpLoggingMiddleware"</span><span ne="0.38306185619561617">:</span><span> </span><span ne="0.04517351268666925">"Information"</span><span>
</span><span>      </span><span ne="0.34672256566092285">}</span><span>
</span><span>    </span><span ne="0.6386789439506476">}</span><span ne="0.9969196340332791">,</span><span>
</span><span>    </span><span ne="0.2893629156795149">"WriteTo"</span><span ne="0.28741816895409866">:</span><span> </span><span ne="0.24979512545708493">[</span><span>
</span>      ...
<span>    </span><span ne="0.8991836490826367">]</span><span>
</span><span>  </span><span ne="0.5270280089049985">}</span><span>
</span><span></span><span ne="0.1739347336649938">}</span></code></p>
```

Here I am setting minimum log levels for standard asp.net core loggers, for Open Telemetry and Quartz. All logs that have log level lower than the specified - won't be logged. For example, I will log only `Warnings`, `Errors` and `Critical` messages for `Microsoft.AspNetCore.Mvc` while `Information`, `Debug` and `Trace` logs will be skipped.

## Best Practise 4: Use Structured Logging

Serilog allows you to log structured data (key-value pairs) instead of plain text, making it easier to query and analyze logs.

```
<p><code id="code-lang-csharp"><span>logger</span><span ne="0.5951940902398116">.</span><span ne="0.27010823453284705">LogInformation</span><span ne="0.47477284069918246">(</span><span ne="0.012451436061202692">"Shipment for order '{OrderId}' is already created"</span><span ne="0.04861497024537087">,</span><span> request</span><span ne="0.017986350405946316">.</span><span>OrderId</span><span ne="0.6464901777956277">)</span><span ne="0.42413446938532584">;</span><span>
</span>
<span>logger</span><span ne="0.5469703995956283">.</span><span ne="0.27216580986923566">LogInformation</span><span ne="0.11875927399730213">(</span><span ne="0.3812252259485047">"Created shipment: {@Shipment}"</span><span ne="0.6004264409794212">,</span><span> shipment</span><span ne="0.5858125771139697">)</span><span ne="0.7835840903475012">;</span></code></p>
```

The log message "Shipment for order '{OrderId}' is already created" includes the `OrderId` as a structured property. Instead of embedding the `OrderId` directly in the log message as plain text, it is passed as a named parameter. This allows logging systems to capture `OrderId` as a separate, searchable field.

The log message "Created shipment: {@Shipment}" uses the @ notation to serialize the shipment object into a structured format. This means that all the properties of the shipment object are logged as separate fields, preserving the structure and making it easier to analyze.

Please never use string interpolation when logging, or you will end up with plain-text logs that are not searchable by important parameters:

```
<p><code id="code-lang-csharp"><span>logger</span><span ne="0.7479346124513248">.</span><span ne="0.1541263673785389">LogInformation</span><span ne="0.24796326665401902">(</span><span ne="0.40355372040007453">$"Shipment for order '</span><span ne="0.46353685420803104">{</span><span id="code-lang-csharp">request</span><span id="code-lang-csharp">.</span><span id="code-lang-csharp">OrderId</span><span ne="0.42288460096973846">}</span><span ne="0.09652595084901261">' is already created"</span><span ne="0.9364912460252777">)</span><span ne="0.6538983753897168">;</span></code></p>
```

Another example of structured logging could be:

```
<p><code id="code-lang-csharp"><span>logger</span><span ne="0.27855415508454506">.</span><span ne="0.3027813546707263">LogInformation</span><span ne="0.9101198926528576">(</span><span ne="0.8648391528523706">"Shipment for order '{OrderId}' is already created"</span><span ne="0.5551716246066051">,</span><span> request</span><span ne="0.025444194851998447">.</span><span>OrderId</span><span ne="0.9055296700911843">)</span><span ne="0.18385515280915188">;</span><span>
</span><span>logger</span><span ne="0.8994530655964003">.</span><span ne="0.30193821028519785">LogInformation</span><span ne="0.5382093492005269">(</span><span ne="0.45476390539339495">"Updated state of shipment {ShipmentNumber} to {NewState}"</span><span ne="0.6679076875758532">,</span><span> request</span><span ne="0.14737153357757438">.</span><span>ShipmentNumber</span><span ne="0.06521411237238128">,</span><span> request</span><span ne="0.6583657998149344">.</span><span>Status</span><span ne="0.5795207230263657">)</span><span ne="0.6014395529168609">;</span></code></p>
```

By implementing logging in such a structured way, you will be able to search logs in log view tool to get, for example, all the events related to a given ShipmentNumber, State or OrderId.

## Best Practise 5: Avoid Logging Sensitive Information

Ensure that sensitive information such as passwords, credit card numbers, or personally identifiable information is not logged. Logging sensitive data can lead to security vulnerabilities.

You should also avoid logging such security information as API Keys, authentication tokens, connection strings, etc.

Serilog out of the box provides several features and practices to help avoid logging sensitive information:

**1\. Use Destructuring Policies:**

Serilog allows you to control how objects are logged using destructuring policies. These policies enable you to sanitize or mask sensitive information before it is logged. For example, if you have a complex object that contains sensitive data, you can define a destructuring policy to exclude or mask specific properties:

```
<p><code id="code-lang-csharp"><span>Log</span><span ne="0.21246453483830674">.</span><span>Logger </span><span ne="0.47509420899025956">=</span><span> </span><span ne="0.9280770546968931">new</span><span> </span><span ne="0.596866494404418">LoggerConfiguration</span><span ne="0.7884026084826232">(</span><span ne="0.9986718893494123">)</span><span>
</span><span>    </span><span ne="0.4285864065386379">.</span><span>Destructure</span><span ne="0.8570801361765006">.</span><span ne="0.2207247055520113">ByMaskingProperties</span><span ne="0.10537644296690118">(</span><span ne="0.5153240550948753">"Password"</span><span ne="0.4989224365734264">,</span><span> </span><span ne="0.4334305184063515">"CreditCardNumber"</span><span ne="0.3960365057610502">)</span><span>
</span><span>    </span><span ne="0.10233604950457242">.</span><span>WriteTo</span><span ne="0.12679152150897055">.</span><span ne="0.48811924045954">Console</span><span ne="0.4817307298461847">(</span><span ne="0.8814313088124291">)</span><span>
</span><span>    </span><span ne="0.05506093284926983">.</span><span ne="0.34022118170484394">CreateLogger</span><span ne="0.17817184428325572">(</span><span ne="0.46351877841136824">)</span><span ne="0.42233779615339107">;</span><span>
</span>
<span></span><span ne="0.44420792499183137">var</span><span> user </span><span ne="0.51607002279192">=</span><span> </span><span ne="0.38322837263977516">new</span><span>
</span><span></span><span ne="0.5497556431432333">{</span><span>
</span><span>    Username </span><span ne="0.6990413040192519">=</span><span> </span><span ne="0.0312695594949427">"anton"</span><span ne="0.8691669991882754">,</span><span>
</span><span>    Password </span><span ne="0.6981118298084552">=</span><span> </span><span ne="0.39859844230279484">"password_secret_information"</span><span ne="0.06535521267191047">,</span><span>
</span><span>    CreditCardNumber </span><span ne="0.03506481386472304">=</span><span> </span><span ne="0.10274154233586541">"1000-1000-1000-1000"</span><span>
</span><span></span><span ne="0.05782005235875243">}</span><span ne="0.473418283872284">;</span><span>
</span>
<span>Log</span><span ne="0.5337519642770823">.</span><span ne="0.6659505061583691">Information</span><span ne="0.8386179391488154">(</span><span ne="0.04998336451710972">"User details: {@User}"</span><span ne="0.7030337964942486">,</span><span> user</span><span ne="0.6372449130138208">)</span><span ne="0.2344005316733322">;</span></code></p>
```

In this example, the `Password` and `CreditCardNumber` properties are masked before being logged.

**2\. Redact Sensitive Information Manually:**

If you are logging individual pieces of information, you can manually redact or sanitize sensitive data before passing it to the logger.

```
<p><code id="code-lang-csharp"><span ne="0.19430441752740413">var</span><span> password </span><span ne="0.8982764017549743">=</span><span> </span><span ne="0.027323224913428645">"password_secret_information"</span><span ne="0.5890859507464954">;</span><span>
</span><span></span><span ne="0.5690840692601656">var</span><span> sanitizedPassword </span><span ne="0.250716974847378">=</span><span> </span><span ne="0.9450293930360097">new</span><span> </span><span ne="0.06764145222249618">string</span><span ne="0.20431849889538922">(</span><span ne="0.07422382855547605">'*'</span><span ne="0.6465714010510404">,</span><span> password</span><span ne="0.444632992193395">.</span><span>Length</span><span ne="0.2859345215359266">)</span><span ne="0.36161761192956243">;</span><span>
</span>
<span>Log</span><span ne="0.9547097542202391">.</span><span ne="0.4655571686351705">Information</span><span ne="0.4716857449185662">(</span><span ne="0.6813892610458202">"User attempted to login with password: {Password}"</span><span ne="0.037414851227347445">,</span><span> sanitizedPassword</span><span ne="0.5478205668799772">)</span><span ne="0.4829577198446342">;</span></code></p>
```

Here, the actual password is replaced with a string of asterisks, ensuring that sensitive data is not logged.

**3\. Configure Filters to Exclude Sensitive Information:**

Serilog allows you to configure filters that can exclude specific log events or properties based on certain conditions. You can set up filters to prevent sensitive information from being logged.

```
<p><code id="code-lang-csharp"><span>Log</span><span ne="0.9016717476314279">.</span><span>Logger </span><span ne="0.14283982688356667">=</span><span> </span><span ne="0.6342102711394453">new</span><span> </span><span ne="0.7481804160674923">LoggerConfiguration</span><span ne="0.040053140727324466">(</span><span ne="0.824657112155973">)</span><span>
</span><span>    </span><span ne="0.34846299905784284">.</span><span>Filter</span><span ne="0.7966511556177592">.</span><span ne="0.9400702468791613">ByExcluding</span><span ne="0.28850637148991176">(</span><span>logEvent </span><span ne="0.3123876874855096">=&gt;</span><span> logEvent</span><span ne="0.8562487778718157">.</span><span>Properties</span><span ne="0.490976445072161">.</span><span ne="0.3908765732313497">ContainsKey</span><span ne="0.4260526651380988">(</span><span ne="0.37144840688623815">"Password"</span><span ne="0.853195642489308">)</span><span ne="0.2496236006804835">)</span><span>
</span><span>    </span><span ne="0.7392119582234428">.</span><span>WriteTo</span><span ne="0.4630978053145969">.</span><span ne="0.5581264640490291">Console</span><span ne="0.8641315803519283">(</span><span ne="0.223076531026827">)</span><span>
</span><span>    </span><span ne="0.027037845356409407">.</span><span ne="0.07132749793114967">CreateLogger</span><span ne="0.2819533906267676">(</span><span ne="0.15320341754268818">)</span><span ne="0.7040630407482242">;</span><span>
</span>
<span>Log</span><span ne="0.43619358385154205">.</span><span ne="0.8629663264834723">Information</span><span ne="0.4900451483643793">(</span><span ne="0.13868734062877586">"User details: {Username}, {Password}"</span><span ne="0.4493651845558092">,</span><span> </span><span ne="0.9325462455286861">"anton"</span><span ne="0.7951981750813754">,</span><span> </span><span ne="0.9606133234057738">"password_secret_information"</span><span ne="0.39282451385948425">)</span><span ne="0.55470086681187">;</span></code></p>
```

In this example, any log event containing a `Password` property will be excluded from the logs.

Regularly review your logs to ensure that no sensitive information is being inadvertently logged. Implement automated checks or manual reviews as part of your security practices to detect any potential issues.

## Best Practise 6: Log Errors

Error logging is essential for diagnosing and troubleshooting issues within an application. When errors occur, detailed logs can provide insights into the cause, context, and impact of the error. This information is crucial for resolving issues quickly and ensuring the reliability and stability of your application.

Depending on your application's security requirements, you may or may not log an exception stacktrace. But please, never expose stacktrace to your end users, for example, as a part of your "500 Internal Server Error" response.

Here is how you can log an exception with stacktrace with Serilog

```
<p><code id="code-lang-csharp"><span ne="0.30136263075071">try</span><span>
</span><span></span><span ne="0.9787382426843323">{</span><span>
</span><span>    </span><span ne="0.8162970112046689">// The code might throw an exception</span><span>
</span><span></span><span ne="0.9059059385311287">}</span><span>
</span><span></span><span ne="0.560539602110339">catch</span><span> </span><span ne="0.6732525356564476">(</span><span ne="0.5743770954175835">Exception</span><span> ex</span><span ne="0.7742396060048141">)</span><span>
</span><span></span><span ne="0.5538217908063024">{</span><span>
</span><span>    Log</span><span ne="0.47914101991599567">.</span><span ne="0.44009943016831754">Error</span><span ne="0.38508517573647205">(</span><span>ex</span><span ne="0.43873517607599133">,</span><span> </span><span ne="0.5052522616963246">"An unexpected error occurred"</span><span ne="0.5106689410735729">)</span><span ne="0.14675889512412987">;</span><span>
</span><span></span><span ne="0.9058319631986333">}</span></code></p>
```

When logging errors, you can include relevant contextual information that can help diagnose the issue. This could include information about the current user, request details, or the state of the application at the time of the error.

For example:

```
<p><code id="code-lang-csharp"><span ne="0.8051357885170832">try</span><span>
</span><span></span><span ne="0.7213025528091841">{</span><span>
</span><span>    </span><span ne="0.01224767279769412">// The code might throw an exception</span><span>
</span><span></span><span ne="0.9539868010866018">}</span><span>
</span><span></span><span ne="0.21035106508229873">catch</span><span> </span><span ne="0.1913832164806697">(</span><span ne="0.27048178321161187">Exception</span><span> ex</span><span ne="0.9674705506372667">)</span><span>
</span><span></span><span ne="0.07531676631661688">{</span><span>
</span><span>    Log</span><span ne="0.9688261882099561">.</span><span ne="0.9696286522654772">ForContext</span><span ne="0.9351835270268652">(</span><span ne="0.39397240644407183">"UserId"</span><span ne="0.5622785802074229">,</span><span> userId</span><span ne="0.5974951947210673">)</span><span>
</span><span>       </span><span ne="0.08071541957499573">.</span><span ne="0.9401867918958411">ForContext</span><span ne="0.35342333751941934">(</span><span ne="0.05465371491109039">"RequestPath"</span><span ne="0.15300517248994094">,</span><span> requestPath</span><span ne="0.7620087555871224">)</span><span>
</span><span>       </span><span ne="0.07937955130566632">.</span><span ne="0.733978506757466">Error</span><span ne="0.4081591066137681">(</span><span>ex</span><span ne="0.5900888346352194">,</span><span> </span><span ne="0.6622628132326409">"An error occurred while processing the request"</span><span ne="0.4389148425285906">)</span><span ne="0.19811640213268933">;</span><span>
</span><span></span><span ne="0.32342923439702476">}</span></code></p>
```

Serilog supports custom **enrichers** that allow you to automatically add specific pieces of information to all log events, including errors. This can ensure that critical contextual information is always included in error logs.

```
<p><code id="code-lang-csharp"><span>Log</span><span ne="0.0775899814309523">.</span><span>Logger </span><span ne="0.3059513061864457">=</span><span> </span><span ne="0.17246850401630098">new</span><span> </span><span ne="0.8542279865844778">LoggerConfiguration</span><span ne="0.912539894386537">(</span><span ne="0.23373386337584323">)</span><span>
</span><span>    </span><span ne="0.21328984425700193">.</span><span>Enrich</span><span ne="0.9574506247093884">.</span><span ne="0.7577823796036681">WithProperty</span><span ne="0.2889832903092384">(</span><span ne="0.6903991985814175">"ApplicationName"</span><span ne="0.20424658463238343">,</span><span> </span><span ne="0.11254895316262181">"ApplicationName"</span><span ne="0.524744270323617">)</span><span>
</span><span>    </span><span ne="0.09337266068040506">.</span><span>Enrich</span><span ne="0.21047516368546693">.</span><span ne="0.7603306738644848">WithProperty</span><span ne="0.9303694722081458">(</span><span ne="0.26946488501360133">"Environment"</span><span ne="0.1404830181197595">,</span><span> </span><span ne="0.8538209492048062">"Production"</span><span ne="0.11645291004558922">)</span><span>
</span><span>    </span><span ne="0.7323645973907151">.</span><span>WriteTo</span><span ne="0.7266340389451776">.</span><span ne="0.9423900353792324">Console</span><span ne="0.14394738042247401">(</span><span ne="0.3772052518575528">)</span><span>
</span><span>    </span><span ne="0.1937463832151094">.</span><span ne="0.8387979622202405">CreateLogger</span><span ne="0.37564446830184284">(</span><span ne="0.9535727080331">)</span><span ne="0.9128701079298193">;</span><span>
</span>
<span></span><span ne="0.9914943524978228">try</span><span>
</span><span></span><span ne="0.9078719568329398">{</span><span>
</span><span>    </span><span ne="0.09058536166239084">// The code might throw an exception</span><span>
</span><span></span><span ne="0.11059032524107448">}</span><span>
</span><span></span><span ne="0.7777429366529103">catch</span><span> </span><span ne="0.19451299063189353">(</span><span ne="0.033835977198486966">Exception</span><span> ex</span><span ne="0.3421849581014238">)</span><span>
</span><span></span><span ne="0.22926537547736114">{</span><span>
</span><span>    Log</span><span ne="0.5235868595222186">.</span><span ne="0.29847906170482896">Error</span><span ne="0.8824328618933042">(</span><span>ex</span><span ne="0.9674715475463493">,</span><span> </span><span ne="0.8114950422254538">"An error occurred"</span><span ne="0.4716222802946842">)</span><span ne="0.9580934617366709">;</span><span>
</span><span></span><span ne="0.28910264744495884">}</span></code></p>
```

## Best Practise 7: Monitor Log Size and Performance

Logging if not managed properly, it can introduce performance bottlenecks and excessive storage consumption.

You can limit the log size by applying the following techniques:

-   using appropriate logging levels
-   using logging filters
-   implementing log rotation and retention for file logging

We have already talked about using appropriate logging levels and logging filters. Let's explore the log rotation and retention for file logging.

Log rotation involves automatically archiving and creating new log files at specified intervals, such as daily or weekly. Log retention policies define how long archived logs should be kept before they are deleted. Both of these practices help manage disk usage by preventing log files from growing indefinitely.

For example:

```
<p><code id="code-lang-csharp"><span>Log</span><span ne="0.5975615843065987">.</span><span>Logger </span><span ne="0.5073956018933397">=</span><span> </span><span ne="0.9632039846929739">new</span><span> </span><span ne="0.9898838447863358">LoggerConfiguration</span><span ne="0.8820141103433237">(</span><span ne="0.15481822125810318">)</span><span>
</span><span>    </span><span ne="0.8370094374688833">.</span><span>WriteTo</span><span ne="0.7442222011182676">.</span><span ne="0.7315798285001798">File</span><span ne="0.6298840984295095">(</span><span>
</span><span>        </span><span ne="0.45661494265042557">"logs/service.log"</span><span ne="0.06291592859998363">,</span><span>
</span><span>        </span><span ne="0.4718298658605754">rollingInterval</span><span ne="0.6413877964430155">:</span><span> RollingInterval</span><span ne="0.7235131737550985">.</span><span>Day</span><span ne="0.040188800194384755">,</span><span> </span><span ne="0.3415248264201024">// Rotate logs daily</span><span>
</span><span>        retainedFileCountLimit</span><span ne="0.8775678563681317">:</span><span> </span><span ne="0.7526583300016016">7</span><span ne="0.8158567431924385">)</span><span>  </span><span ne="0.9013427304121825">// Retain only the last 7 days of logs</span><span>
</span><span>    </span><span ne="0.5965057233426819">.</span><span ne="0.7708927239026317">CreateLogger</span><span ne="0.9877733601396473">(</span><span ne="0.5414267698960028">)</span><span ne="0.19276503059780714">;</span></code></p>
```

This configuration ensures that log files are rotated daily and that only the last 7 days of logs are retained, preventing old logs from consuming excessive disk space.

You can also configure this in the `appsettings.json`:

```
<p><code id="code-lang-json"><span ne="0.2638486011552382">{</span><span>
</span><span>  </span><span ne="0.9014927387351344">"Serilog"</span><span ne="0.5325503282321118">:</span><span> </span><span ne="0.7160061742897973">{</span><span>
</span><span>    </span><span ne="0.98770952834233">"MinimumLevel"</span><span ne="0.9812135093143747">:</span><span> </span><span ne="0.6795413909452195">{</span><span>
</span><span>      </span><span ne="0.8594599075154604">"Default"</span><span ne="0.24732142960587666">:</span><span> </span><span ne="0.24798546553652712">"Information"</span><span>
</span><span>    </span><span ne="0.8442052317106635">}</span><span ne="0.4082366365067983">,</span><span>
</span><span>    </span><span ne="0.6683009988984256">"WriteTo"</span><span ne="0.48285380334438177">:</span><span> </span><span ne="0.9488320660186064">[</span><span>
</span><span>      </span><span ne="0.5171170374471753">{</span><span>
</span><span>        </span><span ne="0.4168534289269368">"Name"</span><span ne="0.12439230975909421">:</span><span> </span><span ne="0.21955493714311936">"File"</span><span ne="0.1284921571560137">,</span><span>
</span><span>        </span><span ne="0.7290967605450835">"Args"</span><span ne="0.3526943369838441">:</span><span> </span><span ne="0.20590514699044582">{</span><span>
</span><span>          </span><span ne="0.96124580327106">"path"</span><span ne="0.06921928738590166">:</span><span> </span><span ne="0.7459701715779087">"logs/service.log"</span><span ne="0.6704404055837957">,</span><span>
</span><span>          </span><span ne="0.16834894799011835">"rollingInterval"</span><span ne="0.025192847686146824">:</span><span> </span><span ne="0.17197799749048504">"Day"</span><span ne="0.5791347079606048">,</span><span>
</span><span>          </span><span ne="0.9281900321203774">"retainedFileCountLimit"</span><span ne="0.610922562112778">:</span><span> </span><span ne="0.935490085984899">7</span><span ne="0.5348829883403128">,</span><span> </span><span ne="0.3902741071164395">// Retain logs for 7 days</span><span>
</span><span>          </span><span ne="0.15941705079154367">"fileSizeLimitBytes"</span><span ne="0.773061155903547">:</span><span> </span><span ne="0.0133738435194658">10485760</span><span> </span><span ne="0.541205093983143">// Limit file size to 10MB</span><span>
</span><span>        </span><span ne="0.22218356352114943">}</span><span>
</span><span>      </span><span ne="0.18969839950504308">}</span><span>
</span><span>    </span><span ne="0.07459319914341223">]</span><span>
</span><span>  </span><span ne="0.4402099043237536">}</span><span>
</span><span></span><span ne="0.24587337549142685">}</span></code></p>
```

Logging can impact application performance, particularly if logs are being written to disk or sent over the network. Monitor the overhead introduced by logging, especially in high-traffic or performance-critical applications. Consider using asynchronous logging to minimize the impact on application performance.

```
<p><code id="code-lang-csharp"><span>Log</span><span ne="0.03227151118797722">.</span><span>Logger </span><span ne="0.0038062637023410506">=</span><span> </span><span ne="0.6720275248019418">new</span><span> </span><span ne="0.0034943428288121137">LoggerConfiguration</span><span ne="0.5316963847276376">(</span><span ne="0.398455607877372">)</span><span>
</span><span>    </span><span ne="0.9884822457410529">.</span><span>WriteTo</span><span ne="0.6225446482773715">.</span><span ne="0.8747125182817942">Async</span><span ne="0.25346066182970184">(</span><span>a </span><span ne="0.8956537338599103">=&gt;</span><span> a</span><span ne="0.1324093334117612">.</span><span ne="0.8962565019914033">File</span><span ne="0.036944437980081624">(</span><span ne="0.7803946602639064">"logs/log.txt"</span><span ne="0.5713072693061325">,</span><span> </span><span ne="0.028041197034277765">rollingInterval</span><span ne="0.38180560254994833">:</span><span> RollingInterval</span><span ne="0.6091769669348422">.</span><span>Day</span><span ne="0.7264396267610855">)</span><span ne="0.02381600630934899">)</span><span>
</span><span>    </span><span ne="0.32237373916807766">.</span><span ne="0.17555605749380054">CreateLogger</span><span ne="0.6116714216942565">(</span><span ne="0.4560491715941315">)</span><span ne="0.10673188580300796">;</span></code></p>
```

Here I use `Serilog.Sinks.Async` - an asynchronous wrapper for Serilog sinks that logs on a background thread. It can be useful for file logging that may be affected by I/O bottlenecks.

It is also very important to **turn off console logging** in your production environment. Console logging can slow down your application significantly.

## Best Practise 8: Centralize and Visualize Logs with a Logging UI

In modern applications, especially those running in distributed environments or microservices architectures, logging can quickly become overwhelming. Logs are often spread across multiple servers, services, or containers, making it difficult to gain insights into the overall system health or to troubleshoot specific issues. A centralized logging UI, like Seq, addresses these challenges by aggregating logs from various sources into a single, searchable interface that provides powerful visualization and analysis tools.

Using a logging UI like Seq not only centralizes your logs but also enhances your ability to monitor, search, and analyze log data in real-time.

Remember I told you about structured logging? You can search for specific log parameters using Seq, or any other similar tools.

Another advantage of using centralized tools for logging management - is being able to configure alerts on errors or other important logs.

To get started with Seq, you need to add the following Nuget package:

```
<p><code id="code-lang-bash"><span>dotnet </span><span ne="0.3838993479055448">add</span><span> package Serilog.Sinks.Seq</span></code></p>
```

And update Serilog logging configuration in `appsettings.json`:

```
<p><code id="code-lang-csharp"><span ne="0.7572733629414311">{</span><span>
</span><span>  </span><span ne="0.08841849631659227">"Serilog"</span><span ne="0.23874692361844096">:</span><span> </span><span ne="0.5932280324043033">{</span><span>
</span><span>    </span><span ne="0.11236632010319836">"Using"</span><span ne="0.4782017248953033">:</span><span> </span><span ne="0.6057012634008555">[</span><span>
</span><span>      </span><span ne="0.1414312613030334">"Serilog.Sinks.Console"</span><span ne="0.1945674198996874">,</span><span>
</span><span>      </span><span ne="0.7741505979453003">"Serilog.Sinks.Seq"</span><span>
</span><span>    </span><span ne="0.6138921044335625">]</span><span ne="0.6988574406407767">,</span><span>
</span><span>    </span><span ne="0.732276160948952">"MinimumLevel"</span><span ne="0.8635147748555061">:</span><span> </span><span ne="0.9832363819337587">{</span><span>
</span><span>      </span><span ne="0.19819617546491097">"Default"</span><span ne="0.6163397708193006">:</span><span> </span><span ne="0.37936210805085335">"Debug"</span><span ne="0.8138959063914524">,</span><span>
</span><span>      </span><span ne="0.2730879124230653">"Override"</span><span ne="0.07889441849192969">:</span><span> </span><span ne="0.06555722124390873">{</span><span>
</span><span>        </span><span ne="0.3940480928739336">"Microsoft"</span><span ne="0.38765387599322076">:</span><span> </span><span ne="0.8741330683868564">"Information"</span><span>
</span><span>      </span><span ne="0.8525114850110344">}</span><span>
</span><span>    </span><span ne="0.39381502467252405">}</span><span ne="0.9492578869357055">,</span><span>
</span><span>    </span><span ne="0.26550452842961236">"WriteTo"</span><span ne="0.5334415581827783">:</span><span> </span><span ne="0.043177418644757104">[</span><span>
</span><span>      </span><span ne="0.9907366624732381">{</span><span> </span><span ne="0.7903506805459484">"Name"</span><span ne="0.3322560357110418">:</span><span> </span><span ne="0.6808608342164625">"Console"</span><span> </span><span ne="0.1325615091510095">}</span><span ne="0.47049284566893024">,</span><span>
</span><span>      </span><span ne="0.20693712560078126">{</span><span>
</span><span>        </span><span ne="0.2514248203348475">"Name"</span><span ne="0.7219989245625227">:</span><span> </span><span ne="0.7226575281728298">"Seq"</span><span ne="0.8483702340230623">,</span><span>
</span><span>        </span><span ne="0.09317303820438294">"Args"</span><span ne="0.31770279290306225">:</span><span> </span><span ne="0.11629171192042365">{</span><span>
</span><span>          </span><span ne="0.3806263335906953">"serverUrl"</span><span ne="0.8713975639593352">:</span><span> </span><span ne="0.4555417682870513">"http://localhost:5341"</span><span>
</span><span>        </span><span ne="0.08923981527670555">}</span><span>
</span><span>      </span><span ne="0.7592146450479225">}</span><span>
</span><span>    </span><span ne="0.9752655239588363">]</span><span ne="0.3794763511207665">,</span><span>
</span><span>    </span><span ne="0.3838818806374116">"Enrich"</span><span ne="0.2875151415728898">:</span><span> </span><span ne="0.6596446635115167">[</span><span> </span><span ne="0.2870619182384947">"FromLogContext"</span><span ne="0.5721089184246807">,</span><span> </span><span ne="0.5719173084994993">"WithMachineName"</span><span ne="0.43109218262509497">,</span><span> </span><span ne="0.17215245991428474">"WithThreadId"</span><span> </span><span ne="0.3138379661802808">]</span><span ne="0.20228994533494649">,</span><span>
</span><span>    </span><span ne="0.006514867152611403">"Properties"</span><span ne="0.6840790270381738">:</span><span> </span><span ne="0.06765944395173196">{</span><span>
</span><span>      </span><span ne="0.7162280828260479">"Application"</span><span ne="0.5588101378009309">:</span><span> </span><span ne="0.5692444109164414">"ShippingService"</span><span>
</span><span>    </span><span ne="0.2597600054648538">}</span><span>
</span><span>  </span><span ne="0.44014161763844106">}</span><span>
</span><span></span><span ne="0.19255428835866584">}</span></code></p>
```

Here, we configure logging to Console (don't use in production) and Seq. We point the Seq's URL to http://localhost:5341 when running locally. When running service inside a docker container - you need to use the docker container's name instead of a localhost: http://seq:5341.

Here is how logging looks like in Seq:

![Screenshot_2](https://antondevtips.com/media/code_screenshots/architecture/seq-logging-traces/img_aspnet_seq_2.png)

If you want to learn How to Implement Structured Logging and Distributed Tracing for Microservices with Seq, make sure to check out my [blog post](https://antondevtips.com/blog/how-to-implement-structured-logging-and-distributed-tracing-for-microservices-with-seq).

Here is a list of Seq alternatives, in case you need something else:

-   ELK Stack: Elasticsearch, Logstash, and Kibana
-   Datadog
-   New Relic
-   Loggly
-   GrayLog
-   Azure Monitor Logs
-   Amazon CloudWatch Logs (AWS)

Hope you find this newsletter useful. See you next time.
