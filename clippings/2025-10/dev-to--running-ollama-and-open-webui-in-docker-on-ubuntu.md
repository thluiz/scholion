---
url: "https://dev.to/pauldotyu/running-ollama-locally-with-open-webui-ol1?"
captured_at: "2025-10-22T11:19:56+01:00"
title: "Local LLMs: Running Ollama and Open WebUI in Docker on Ubuntu - DEV Community"
domain: "dev-to"
---

---
[Ollama](https://docs.ollama.com/) is a popular tool for running large language models (LLMs) locally on your machine. It provides a simple interface to interact with various models without needing an internet connection. [Open WebUI](https://docs.openwebui.com/) is a web-based user interface that allows you to interact with LLMs through a browser.

I am working on an Ubuntu 24.04.3 LTS Desktop machine with decent hardware to run models locally, so my preference is to run Ollama as a local service rather than confining it to a container. This way, Ollama can take full advantage of my machine's capabilities, especially the GPU.

Open WebUI is also an application that I'd like constantly running in the background so I can access it anytime without remembering to start it up. Naturally, running the web application in a container makes sense for this use case.

Getting these two components to work together came with a few challenges. In this post, I'll walk you through the steps I took to set up Ollama as a local service with Open WebUI running in a Docker container.

## [](https://dev.to/pauldotyu/running-ollama-locally-with-open-webui-ol1?#prerequisites)Prerequisites

To get started, you'll need to have Docker installed on your machine. If you haven't done so already, you can download and install Docker Desktop by following the [Get Docker guide](https://docs.docker.com/get-started/get-docker/). However, I prefer to run Docker Engine directly so I followed this [Install Docker Engine guide](https://docs.docker.com/engine/install/).

## [](https://dev.to/pauldotyu/running-ollama-locally-with-open-webui-ol1?#step-1-install-ollama)Step 1: Install Ollama

Depending on your operating system, you can follow the instructions on the [Ollama Quickstart page](https://docs.ollama.com/quickstart) to install Ollama. For Ubuntu, I followed the [Linux installation instructions](https://docs.ollama.com/linux). This can take a while as it downloads the necessary files and GPU accelerators if applicable.

> I tried this using both AMD and NVIDIA GPUs and they both worked fine. The GPUs were detected automatically by Ollama, which is nice!

## [](https://dev.to/pauldotyu/running-ollama-locally-with-open-webui-ol1?#step-2-configure-ollama)Step 2: Configure Ollama

Once Ollama is installed, it runs as a local service on your machine. You can verify that it's running by executing the following command in your terminal:  

You should see output indicating that the Ollama service is active and running.

But before we can use it in a way that it can be called from a container, we need to make a small configuration change. By default, Ollama listens on `127.0.0.1` which means it can only accept connections from the local machine.

To verify this, you can run:  

You should see output similar to this:  

```
tcp   LISTEN 0      4096        127.0.0.1:11434      0.0.0.0:*
```

To allow connections from other containers, we need to change this to listen on `0.0.0.0`.

To do this, we need to modify the Ollama service configuration file. Run the following command to open the configuration file in a text editor:  

```
<span>sudo </span>systemctl edit ollama.service
```

You will see a file that looks something like this:  

```
### Editing /etc/systemd/system/ollama.service.d/override.conf
### Anything between here and the comment below will become the contents of the drop-in file

&lt;HERE_IS_WHERE_YOU_SHOULD_ADD_YOUR_CHANGES&gt;

### Edits below this comment will be discarded
```

There will be a big blank space where you can add your changes. Add the following lines to the file:  

```
[Service]
Environment="OLLAMA_HOST=0.0.0.0:11434"
Environment="OLLAMA_CONTEXT_LENGTH=32768"
```

> Note the `OLLAMA_CONTEXT_LENGTH` setting. I plan to use models that support long context lengths, so I set this to 32k. You should adjust this value based on the models you plan to use or omit it if you want to stick with the default. You can always change this in other ways. You can find a lot more helpful tips on configuring this in the [Ollama FAQ](https://github.com/ollama/ollama/blob/main/docs/faq.md).

Save and exit the editor. Then, reload the systemd configuration and restart the Ollama service to apply the changes:  

```
<span>sudo </span>systemctl daemon-reload
<span>sudo </span>systemctl restart ollama
```

You can verify that Ollama is now listening on all interfaces by running:  

You should now see the following output:  

```
tcp   LISTEN 0      4096                *:11434            *:*
```

Now Ollama is configured to accept connections on all interfaces!

> **Note**: By configuring Ollama to listen on `0.0.0.0`, it becomes accessible to your entire local network. This is intentional and beneficial for several reasons:
> 
> -   Allows multiple containerized applications to connect to Ollama (not just Open WebUI)
> -   Enables testing AI applications from other devices on your network
> -   Supports development workflows where you might have multiple services that need LLM access
> -   Makes it easy to experiment with different AI tools and interfaces without reconfiguring Ollama each time
> 
> If you're concerned about security, ensure you're on a trusted network or configure your firewall to restrict access to port 11434. For production environments, consider setting up authentication or using a reverse proxy.
> 
> To put it back to the way it was, just delete the file `/etc/systemd/system/ollama.service.d/override.conf` and restart the Ollama service.

Finally, run the following command to pull a model to use with Open WebUI:  

This will download the `gpt-oss:20b` model to your local machine. I chose this model because it's a capable open-source model that runs well on consumer hardware while providing good performance for general-purpose tasks. Feel free to use any other model available in the [Ollama model registry](https://ollama.com/models) such as `llama3`, `mistral`, or `gemma` based on your hardware capabilities and use case.

## [](https://dev.to/pauldotyu/running-ollama-locally-with-open-webui-ol1?#step-3-run-open-webui-in-a-docker-container)Step 3: Run Open WebUI in a Docker Container

Now that Ollama is set up and running the way we want, we can proceed to run Open WebUI in a Docker container.

Run the following command to start the Open WebUI container:  

```
docker run <span>-d</span> <span>\</span>
<span>-p</span> 9090:8080 <span>\</span>
<span>--name</span> open-webui <span>\</span>
<span>--restart</span> unless-stopped <span>\</span>
<span>--add-host</span><span>=</span>host.docker.internal:host-gateway <span>\</span>
<span>-v</span> <span>$HOME</span>/.open-webui:/app/backend/data <span>\</span>
ghcr.io/open-webui/open-webui:v0.6.33
```

This command does the following:

-   `-d`: Runs the container in detached mode (in the background).
-   `-p 9090:8080`: Maps port 8080 in the container to port 9090 on your host machine.
-   `--name open-webui`: Names the container "open-webui".
-   `--restart unless-stopped`: Ensures the container restarts automatically unless explicitly stopped.
-   `--add-host=host.docker.internal:host-gateway`: Adds a host entry to allow the container to access services running on the host.
-   `-v $HOME/.open-webui:/app/backend/data`: Mounts a volume to persist data so that your settings and chat history are saved even if the container is removed.
-   `ghcr.io/open-webui/open-webui:v0.6.33`: Specifies the image to use for the container. You can check for the latest version on the [Open WebUI releases page](https://github.com/open-webui/open-webui/releases).

After initially running the container, run the following command to check the status of the container:  

```
docker ps <span>-a</span> | <span>grep </span>open-webui
```

Wait until the **STATUS** column shows `Up` and `(healthy)` before proceeding.

Once you've confirmed the container is running, you can access the Open WebUI interface by navigating to `http://localhost:9090` in your web browser.

Proceed to set up Open WebUI by following the on-screen instructions.

## [](https://dev.to/pauldotyu/running-ollama-locally-with-open-webui-ol1?#step-4-use-open-webui-with-ollama)Step 4: Use Open WebUI with Ollama

At this point you should be on an empty Open WebUI interface. To connect it to your local Ollama service, click the **Select a model** drop down at the top left of the page. If all went well, you should see a list of models available from your local Ollama installation.

Select the model you pulled earlier (e.g., `gpt-oss:20b`) and start interacting with it through the web interface!

When you get the notification from Open WebUI that a new version is available, all you need to do is stop the container, and re-run the `docker run` command from Step 3 with the new version number.

## [](https://dev.to/pauldotyu/running-ollama-locally-with-open-webui-ol1?#alternative-options)Alternative options

Another option to run the Open WebUI container and avoid making changes to the Ollama service is to run the container with the following command:  

```
docker run <span>-d</span> <span>\</span>
<span>--network</span><span>=</span>host <span>\</span>
<span>-e</span> <span>OLLAMA_BASE_URL</span><span>=</span>http://127.0.0.1:11434/ <span>\</span>
<span>-v</span> <span>$HOME</span>/.open-webui:/app/backend/data <span>\</span>
<span>--name</span> open-webui <span>\</span>
<span>--restart</span> unless-stopped <span>\</span>
ghcr.io/open-webui/open-webui:v0.6.33
```

This command uses the `--network=host` option to allow the container to share the host's network stack, making it easier to connect to services running on the host machine. The `-e OLLAMA_BASE_URL=http://127.0.0.1:11434/` environment variable is set to point to the Ollama service running on the host.

While this approach is simpler, I chose the primary method (exposing Ollama on `0.0.0.0`) for better container isolation. With `--network=host`, the Open WebUI container can access all network services on my host machine, including services that might be running on localhost that weren't intended to be exposed. By using bridge networking with `--add-host=host.docker.internal:host-gateway`, the container can only access services that are explicitly listening on the network, giving me more control over what the container can reach. This follows the principle of least privilege - the container only has access to what it needs (Ollama) rather than unrestricted access to my entire host network.

## [](https://dev.to/pauldotyu/running-ollama-locally-with-open-webui-ol1?#conclusion)Conclusion

In this post, we walked through the steps to set up Ollama and Open WebUI using Docker containers on a Linux machine. By configuring Ollama to listen on all interfaces and running Open WebUI in a container, we created a flexible and accessible environment for interacting with large language models locally.

This Ollama setup also allows you to build and test your own AI applications against Ollama models running locally.

## [](https://dev.to/pauldotyu/running-ollama-locally-with-open-webui-ol1?#cleanup)Cleanup

When you want to stop and remove the Open WebUI container, you can run:  

```
docker <span>rm </span>open-webui <span>--force</span>
```

Note that this removes the container but preserves your data in `$HOME/.open-webui`. Your chat history, settings, and configurations will remain intact if you decide to run the container again later.

If you want to completely remove all Open WebUI data as well, run:  

To stop the Ollama service, you can run:  

```
<span>sudo </span>systemctl stop ollama
```

Or to disable it from starting automatically on boot:  

```
<span>sudo </span>systemctl disable ollama
```

Feel free to explore different models and configurations to suit your needs. Happy chatting!

## [](https://dev.to/pauldotyu/running-ollama-locally-with-open-webui-ol1?#references)References

-   [Ollama Documentation](https://docs.ollama.com/)
-   [Ollama FAQ](https://github.com/ollama/ollama/blob/main/docs/faq.md)
-   [Open WebUI Documentation](https://docs.openwebui.com/)
