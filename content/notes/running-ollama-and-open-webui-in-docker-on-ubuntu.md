---
title: "Local LLMs: Running Ollama and Open WebUI in Docker on Ubuntu"
date: '2025-10-22T11:19:56+01:00'
category: webclip
summary: 'The post explains how to run Ollama as a local service on Ubuntu and Open WebUI in Docker, including Ollama host binding, model pulling, and container setup.'
tags: ["ollama", "open-webui", "docker", "ubuntu"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Local LLMs: Running Ollama and Open WebUI in Docker on Ubuntu - DEV Community"
    url: "https://dev.to/pauldotyu/running-ollama-locally-with-open-webui-ol1?"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-10/dev-to--running-ollama-and-open-webui-in-docker-on-ubuntu.md"
    kind: repo
---

The post describes a setup where Ollama runs as a local service on Ubuntu and Open WebUI runs in a Docker container. It explains why the author prefers this split, with Ollama using the machine directly and Open WebUI staying available in the background.

## Reading notes

- Docker is required, and the author mentions Docker Desktop or Docker Engine as installation options.
- Ollama is installed on Ubuntu through the Linux installation instructions and runs as a local service.
- By default, Ollama listens on 127.0.0.1, so the post changes the service configuration to listen on 0.0.0.0:11434.
- The Ollama service override sets OLLAMA_HOST=0.0.0.0:11434 and OLLAMA_CONTEXT_LENGTH=32768.
- The post notes that exposing Ollama on 0.0.0.0 makes it reachable from the local network and suggests firewall restrictions for security.
- A model is pulled with ollama pull gpt-oss:20b, and other models such as llama3, mistral, or gemma are mentioned as options.
- Open WebUI is started with docker run, mapping port 9090 to 8080, naming the container open-webui, and mounting $HOME/.open-webui for persistent data.
- The container uses --add-host=host.docker.internal:host-gateway so it can reach services on the host.
- After startup, the post says to wait for the container status to show Up and (healthy), then open http://localhost:9090.
- In Open WebUI, the user selects the pulled Ollama model from the model dropdown and starts chatting.
- When a new Open WebUI version is available, the post says to stop the container and rerun the docker command with the new image tag.
- An alternative setup uses --network=host and OLLAMA_BASE_URL=http://127.0.0.1:11434/ instead of changing Ollama’s host binding.
- The author prefers the bridge-network approach because it keeps the container limited to services that are explicitly reachable on the host network.
- Cleanup commands include docker rm open-webui --force, sudo systemctl stop ollama, and sudo systemctl disable ollama.
