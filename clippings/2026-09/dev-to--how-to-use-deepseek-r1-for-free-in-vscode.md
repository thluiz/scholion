---
url: "https://dev.to/dwtoledo/how-to-use-deepseek-r1-for-free-in-visual-studio-code-with-cline-or-roo-code-3an9?"
captured_at: "2026-09-24T23:58:07+01:00"
title: "How to Use DeepSeek R1 for Free in Visual Studio Code with Cline or Roo Code"
domain: "dev-to"
---

[![Cover image for How to Use DeepSeek R1 for Free in Visual Studio Code with Cline or Roo Code](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fzfp76z5zrpac0hk5fw15.png)](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fzfp76z5zrpac0hk5fw15.png)

[![Douglas Toledo](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F485518%2F71e95753-06a9-4195-a19a-50ec3a6b6cad.jpeg)](https://dev.to/dwtoledo)

If you're looking for an AI that excels in reasoning and is also free because it's _open source_, the newly launched **DeepSeek R1** is a great choice. It competes with and outperforms models like GPT-4, o1-mini, Claude 3.5, among others. I tested it and have nothing but praise!

If you want to run it directly in your **Visual Studio Code** as a _code agent_ similar to GitHub Copilot, without spending a dime, come along as I show you how to do this using tools like **LM Studio**, **Ollama**, and **Jan**.

* * *

### [](#why-is-deepseek-r1-so-talked-about-these-days)**Why is DeepSeek R1 so talked about these days?**

*   **It's free and _open source_**: Unlike many models that charge a fortune, you can use it without paying anything. It's even available for chat at [https://chat.deepseek.com](https://chat.deepseek.com/).
    
*   **Performance**: It competes with and outperforms other models in tasks involving logic, mathematics, and even code generation (which is my favorite part).
    
*   **Multiple versions**: To run it locally (LLM), there are models ranging from 1.5B to 70B parameters, so you can choose what works best on your PC depending on your hardware.
    
*   **Easy to integrate**: You can connect it to VSCode using extensions like **Cline** or **Roo Code**.
    
*   **No costs**: If you run it locally, you don't pay for tokens or APIs. A graphics card is recommended, as running it solely on the CPU is slower.
    

* * *

### [](#important-tips-before-you-start)**Important Tips Before You Start**

*   **Save resources**: If your PC isn't very powerful, stick with the smaller models (1.5B or 7B parameters) or quantized versions.
    
*   **RAM Calculator**: Use [LLM Calc](https://llm-calc.rayfernando.ai/?quant=fp16) to find out the minimum RAM you'll need.
    
*   **Privacy**: Running it locally means your data stays on your PC and doesn't go to external servers.
    
*   **No costs**: Running it locally is free, but if you want to use the DeepSeek API, you'll need to pay for tokens. The good news is that their price is much lower than competitors.
    

* * *

### [](#which-model-to-choose-it-depends-on-your-pc)**Which Model to Choose? It Depends on Your PC!**

DeepSeek R1 has several versions, and the choice depends on your hardware:

*   **1.5B Parameters**:
    
    *   **RAM required**: ~4 GB.
    *   **GPU**: Integrated (like NVIDIA GTX 1050) or a modern CPU.
    *   **What for?**: Simple tasks and modest PCs.
*   **7B Parameters**:
    
    *   **RAM required**: ~8-10 GB.
    *   **GPU**: Dedicated (like NVIDIA GTX 1660 or better).
    *   **What for?**: Intermediate tasks and PCs with better hardware.
*   **70B Parameters**:
    
    *   **RAM required**: ~40 GB.
    *   **GPU**: High-end (like NVIDIA RTX 3090 or higher).
    *   **What for?**: Complex tasks and super powerful PCs.

* * *

### [](#how-to-run-deepseek-r1-locally)**How to Run DeepSeek R1 Locally**

* * *

#### [](#1-using-lm-studio)**1\. Using LM Studio**

*   **Download and install LM Studio**: Just go to the [LM Studio](https://lmstudio.ai/) website and download the version for your system.
    
*   **Download the DeepSeek R1 model**: In LM Studio, go to the **Discover** tab, search for "DeepSeek R1," and select the version most compatible with your system. If you're using a MacBook with Apple processors, keep the **MLX** option selected next to the search bar (these versions are optimized for Apple hardware). For Windows or Linux, choose the **GGUF** option.
    
*   **Load the model**: After downloading, go to **Local Models**, select DeepSeek R1, and click **Load**.
    
*   **Start the local server**: In the **Developer** tab, enable **Start Server**. It will start running the model at `http://localhost:1234`.
    
*   Proceed to step 4 **Integrating with VSCode**!
    

* * *

#### [](#2-using-ollama)**2\. Using Ollama**

*   **Install Ollama**: Download it from the [Ollama](https://ollama.ai/) website and install it.
*   **Download the model**: In the terminal, run\*:

```
   ollama pull deepseek-r1  
```

Enter fullscreen mode Exit fullscreen mode

_\*This is the main model; if you want smaller models, go to [https://ollama.com/library/deepseek-r1](https://ollama.com/library/deepseek-r1) and see which command to run in the terminal._

*   **Start the server**: In the terminal, execute:

```
   ollama serve  
```

Enter fullscreen mode Exit fullscreen mode

The command will start running the model at `http://localhost:11434`.

*   Proceed to step 4 **Integrating with VSCode**!

* * *

#### [](#3-using-jan)**3\. Using Jan**

*   **Download and install Jan**: Choose the version for your system on the [Jan](https://jan.ai/) website.
    
*   **Download the model**: I couldn't find DeepSeek R1 directly in Jan. So, I went to the [Hugging Face](https://huggingface.co/models?sort=trending&search=unsloth+gguf+deepseek+r1) website and manually searched for "unsloth gguf deepseek r1." I found the desired version, clicked the "Use this model" button, and selected Jan as the option. The model automatically opened in Jan, and I then downloaded it.
    
*   **Load the model**: After downloading, select the model and click **Load**.
    
*   **Start the server**: Jan automatically starts the server, usually at `http://localhost:1337`.
    
*   Proceed to step 4 **Integrating with VSCode**!
    

* * *

#### [](#4-integrating-with-vscode)**4\. Integrating with VSCode**

*   **Install the extension**: In VSCode, open the Extensions tab and install Cline or Roo Code.

* * *

*   **Configure the extension for Jan or LM Studio**: The configuration for both **Cline** and **Roo Code** is practically identical. Follow the steps below:
    
    *   Click on the extension and access **"Settings"**.
    *   In **API Provider**, select **"LM Studio"**.
    *   In the **Base URL** field, enter the URL configured in Jan or LM Studio.
    *   The **Model ID** field will be automatically filled if you only have one model available. Otherwise, manually select the **DeepSeek** model you downloaded.
    *   Finish by clicking **"Done"**.

* * *

*   **Configure the extension for Ollama**:
    
    *   Click on the extension and access **"Settings"**.
    *   In **API Provider**, select **"Ollama"**.
    *   In the **Base URL** field, enter the URL configured in Ollama.
    *   The **Model ID** field will be automatically filled if you only have one model available. Otherwise, manually select the **DeepSeek** model you downloaded.
    *   Finish by clicking **"Done"**.
*   Integration complete, now just enjoy the functionalities of Cline or Roo Code.
    

* * *

### [](#conclusion)**Conclusion**

DeepSeek R1 is a lifesaver for those who want a powerful AI without spending anything. With **LM Studio**, **Ollama**, or **Jan**, you can run it locally and integrate it directly into **Visual Studio Code**. Choose the model that fits your PC and start using it today!
