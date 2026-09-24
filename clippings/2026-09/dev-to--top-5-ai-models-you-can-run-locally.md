---
url: "https://dev.to/best_codes/5-best-ai-models-you-can-run-locally-on-your-device-475h?context=digest"
captured_at: "2026-09-24T23:48:49+01:00"
title: "Top 5 AI Models YOU Can Run Locally on YOUR Device! 🤯"
domain: "dev-to"
---

What's up, folks? Did you know you can run an AI model on **YOUR** machine?! Let me explain.

Most AI models are run on private servers far away (unless you happen to live near your server). This is because it takes a LOT of power to run an AI model — well, you can run _some_ AI models on your personal device, but there is no guarantee that everybody has a device strong enough. Plus, for companies like OpenAI, running the AI on a big server makes it a lot faster for their users as well.

Most companies that offer AI services use an AI API rather than run the AI models themselves. After all, GPT-4 and Claude-3.5-Sonnet are some of the highest quality AI models, but both OpenAI and Anthropic (Claude) have not made these models open source, so they cannot be run locally.

So, why not just use a chat website like ChatGPT.com to get access to powerful models?  
Hmm. I should be clear. This article does **not** tell you how to run models as powerful as GPT-4 on your device. Most devices can't. This article is about how to run alternative open source models on your device, easily and efficiently.

Back to our question of 'why not just use ChatGPT?'. Here are a few reasons:

*   **Security**. Most AI APIs don't really provide any form of encryption. You need to provide an API key to use the API, but providing an API key does not magically encrypt your data.

[![ChatGPT Web Socket](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fijxms5c62l6nqeonzddt.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fijxms5c62l6nqeonzddt.png)

Many AI chats connect to a data stream, send your message as plain text (unencrypted) to a server, and then stream the AI's response, unencrypted, back to you.

*   **Stability**. Most AI companies have reasonably stable chat interfaces. For example, OpenAI's website, [https://chatgpt.com/](https://chatgpt.com/), has a great uptime — [99.7%](https://status.openai.com/). The most likely reason that you wouldn't be able to access AI would be because of an internet outage or loss of internet access. AI models do **not** require an internet connection, but connecting to a server where one is running does. So if you lose your internet connection, you lose AI access as well… unless you run AI models on _your_ device. In which case _your_ device is the server, in which case internet doesn't matter.
    
*   **Privacy**. Many AI companies lack good privacy. Some collect your chat data to train AI models on (commonly euphemized as 'collecting telemetry'). Others have a human team manually review user chats, to gather insights about their AI models.
    

![Google Gemini Privacy](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fru8ga23krbtyb1tdi2um.png)

See [https://support.google.com/gemini/answer/13594961](https://support.google.com/gemini/answer/13594961)

Running models locally addresses each of these issues quite well.

* * *

## [](#running-an-ai-model-locally)Running an AI model locally

It's pretty easy for a developer to run an AI model locally using the CLI, for example with [Ollama](https://ollama.com/) or a similar service. But since this article has both the developer and non-developer audiences in mind, I'll be using an easier method, with an intuitive UI.

There are a number of options, such as Alpaca (Linux only) or LM Studio (very slow), but I'm choosing [GPT4All](https://www.nomic.ai/gpt4all) by NomicAI, due to its cross-platform support and ease of use.

[Download GPT4All](https://www.nomic.ai/gpt4all)

If you're going for privacy, be sure to opt out of any 'Telemetry' or 'Datalake' settings when you set up the app (you can change them later in settings if you miss it).

Now, you'll need to download some models to run, which is what this post is all about! Go to the models tab, then click 'Add model' in the top right.

[![Model tab](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fo763gxw4yzud92ybumqu.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fo763gxw4yzud92ybumqu.png)

[![Add model](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F28491nyprnaxsmslczm4.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F28491nyprnaxsmslczm4.png)

Now, let's get downloading!

* * *

### [](#warning)⚠️ Warning!

AI model files are often **VERY** large. Many models I'm recommending are in the 2-6 GB range, so if your computer is a bit old, check how much space you have before downloading. If you want to test lots of models, you might remove ones you don't use before trying another.

> Note: Since the model search currently is not working for default models, I reference the position of the model in the model list throughout this article. These positions may have changed since this article's publication date.

## [](#1-nous-hermes-2-mistral-dpo)1\. Nous Hermes 2 Mistral DPO

This is a great overall model. It's fairly fast, fine-tuned, and reasonably knowledgeable.  
The model has about 7 billion parameters.

*   **File size**: **3.83 GB**
*   **RAM required**: **8 GB**
*   **Quantization**: **q4\_0** (suitable for older systems)

You won't have to look too hard to find this model. It's #2 on the list. (You shouldn't need to use the search):

[![Model card](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F1ypswndqjoeiz0s3no1d.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F1ypswndqjoeiz0s3no1d.png)

Click 'Download' (not shown in the image; far right of the model card) and wait for the model to be downloaded and installed for future use.

## [](#2-small-or-old-devices-qwen215binstruct)2\. Small or Old Devices: Qwen2-1.5B-Instruct

This model isn't the sharpest knife in the drawer 😒. But if your device is not super powerful, this model is a great choice. It only has 1.5 billion parameters, although it is good at following instructions or interpreting data. All that sounds pretty nice, but this model is also _very_ prone to hallucination — the word we use for when an AI tells a lie (since it doesn't make the ethical choice to lie). Check out the image below to see what I mean.

[![Hallucination](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F9zkttk4shb18g5jewaln.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F9zkttk4shb18g5jewaln.png)

*   **File size**: **0.89 GB**
*   **RAM required**: **4 GB**
*   **Quantization**: **q4\_0**

This model is farther down on the list. To find it, just scroll down to the very bottom of the model list — don't search anything — and it should be there.

[![Model card](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fvwqfk03o0z5wp8hwy50r.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fvwqfk03o0z5wp8hwy50r.png)

## [](#3-llama-3-8b-instruct)3\. Llama 3 8B Instruct

This model is larger than other models suggested so far. Llama models are open-source and usually pretty 'smart'. They also have a very friendly personality and high quality training data. This particular model has 8 billion parameters.

*   **File size**: **4.34 GB**
*   **RAM required**: **8 GB**
*   **Quantization**: **q4\_0**

This model is the first one on the list!

[![Model card](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fcai438n4czptt3ebfkyb.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fcai438n4czptt3ebfkyb.png)

## [](#4-mini-orca-small)4\. Mini Orca (Small)

This model is great at explaining, fairly small, and fast. It is very prone to hallucination, particularly in regard to math problems. I'd recommend this as an informational model rather than a chat model.

*   **File size**: **1.84 GB**
*   **RAM required**: **4 GB** (great for older systems)
*   **Quantization**: **q4\_0**

Since this is a default model, searching for it won't rank it higher. Scroll down to the bottom of the model list, then go up to the three models, and you should see it.

[![Model card](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fpildhhu3pwllq7nno0je.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fpildhhu3pwllq7nno0je.png)

## [](#5-mistral-instruct)5\. Mistral Instruct

This model is a great model in general, and has licensing to be used commercially. It also doesn't have ethical limitations, so it will help you with anything — even naughty things.

*   **File size**: **3.83 GB**
*   **RAM required**: **8 GB**
*   **Quantization**: **q4\_0**

This model is the third model in the default list.  
[![Model card](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fcqatmbyuehkewjcf48sg.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fcqatmbyuehkewjcf48sg.png)

* * *

Now that we've downloaded a model or two, let's talk to one! This is pretty straightforward.

## [](#chatting-with-a-model)Chatting with a model

*   Click the chats tab in the sidebar:  
    [![Chats tab](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Feqxtxo4z1gf0r43welch.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Feqxtxo4z1gf0r43welch.png)
    
*   Click the 'New Chat' button at the top of the sidebar.
    
*   Load a model. You can do this easily by click the load default model button, or choose a specific one in the top bar.
    

[![Load model](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fibwv7c97eeifw5lnh232.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fibwv7c97eeifw5lnh232.png)

Now, you're all set to chat! After the model loads, send it a message and see how it goes. Try a smaller model to start out (Qwen, for example) for your first test.

* * *

Of course, while running AI models locally is a lot more secure and reliable, there are tradeoffs. For instance, local AI models are limited to the processing power of your device, so they can be pretty slow. They also aren't as 'smart' as many closed-source models, like GPT-4. Running models locally is not 'better' than running them in the cloud. It depends on your use case and preferences.

Well, thanks for reading!

* * *

_Article by [BestCodes](https://bestcodes.dev/). No content in this article was generated by AI, excepting images which depict the text output of AI models._

Check out my next post here!
