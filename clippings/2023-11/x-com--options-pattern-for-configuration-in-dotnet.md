---
url: "https://x.com/mjovanovictech/status/1728687891788820602"
captured_at: "2023-11-27T20:30:38+00:00"
title: "Thread by @mjovanovictech: What is the cleanest way to get configuration values in .NET? I use the Options pattern, a…"
domain: "x-com"
---

Thread by Milan Jovanović (@mjovanovictech), 1 tweets.

## 1/1

What is the cleanest way to get configuration values in .NET? 
 
I use the Options pattern, and here's why you should know about it. 
 
App configuration lives in environment variables or JSON files. 
 
You can get individual values using the `IConfiguration` interface. 
 
But this is error-prone and cumbersome, so I don't recommend it. 
 
Instead, I use the Options pattern: 
 
- Create a class to represent the settings 
- Bind the class properties to application settings (JSON) 
- Consume the Options pattern in my code using IOptions 
 
You can also add data annotations to your settings class for simple validation. Or even implement complex validation rules with something like FluentValidation. 
 
If you enjoyed this, you will love The .NET weekly newsletter. More than 33,000+ engineers already read it. 
 
Subscribe here: 
https://
milanjovanovic.tech 
 
Are you using the Options pattern?

![image](https://pbs.twimg.com/media/F_2IaVYXUAAlDKp?format=png&name=orig)

Links: https://t.co/xip45XpWuB

([tweet](https://x.com/mjovanovictech/status/1728687891788820602), 2023-11-26 08:11 UTC)

## Author's replies in the conversation

Tweets by the same author in the conversation, posted after the thread (mostly replies to comments).

---

Want to become a better software engineer?

Each week, I send one piece of practical advice about .NET and software architecture.

It's a 5-minute read (or less) and comes every Saturday morning.

Join 33,000+ engineers here:

Card: https://t.co/5wMaFqDYBG

([tweet](https://x.com/mjovanovictech/status/1728724096660480399), 2023-11-26 10:35 UTC)

---

It can be updated on the fly

([tweet](https://x.com/mjovanovictech/status/1728764951911604364), 2023-11-26 13:17 UTC)
