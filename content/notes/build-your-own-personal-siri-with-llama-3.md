---
title: "Build your own personal SIRI with LLAMA-3 like a PRO! 🧙‍♂️ 🪄"
date: '2026-09-25T00:59:55+01:00'
category: webclip
summary: 'Tutorial para montar um assistente de voz tipo Siri em Python com LLAMA-3, Groq, Google Generative AI e opções de TTS, além de suporte a webcam, screenshot e clipboard.'
tags: ["python", "assistente-de-voz", "llama-3", "groq"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Build your own personal SIRI with LLAMA-3 like a PRO! 🧙‍♂️ 🪄"
    url: "https://dev.to/shricodev/build-your-personal-siri-with-llama-3-like-a-pro-5h1o?context=digest"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--build-your-own-personal-siri-with-llama-3.md"
    kind: repo
---

The tutorial shows how to build a multi-modal voice assistant in Python with LLAMA-3. It sets up speech recognition, chat responses through Groq, image analysis with Google Generative AI, and three text-to-speech options: OpenAI, gTTS, and pyttsx3.

It also adds support for daily chat logs, screenshot capture, webcam capture, clipboard extraction, and a shell script to automate setup and execution. The project uses a `.env` file for API keys and stores responses and images in local folders.

## Fichamento

- O artigo ensina a montar um assistente de voz em Python com LLAMA-3.
- A configuração inicial cria pastas para código, logs, histórico de chat e arquivos de resposta.
- O projeto usa SpeechRecognition, OpenCV, Groq, Google Generative AI, Whisper, PyAudio e outras bibliotecas.
- O arquivo `utils.py` reúne funções para obter o log do dia, encerrar o programa, capturar screenshot, remover a última screenshot e ler o clipboard.
- O arquivo `setup.py` carrega as credenciais do `.env` e exige as chaves da Groq e da Google Generative AI.
- O suporte a webcam procura uma câmera disponível e salva a imagem em uma pasta do usuário.
- A classe `Siri` inicializa os clientes de Groq, OpenAI e Google Generative AI, além do modelo Whisper para transcrição.
- O assistente mantém um histórico de conversa e escuta a palavra de ativação "siri".
- A transcrição de áudio usa Faster Whisper para converter o arquivo gravado em texto.
- A extração do comando remove a palavra de ativação e captura o pedido do usuário.
- A resposta do chat é gerada pela Groq com o modelo `llama-3.1-8b-instant`.
- O texto pode ser convertido em fala por pyttsx3, OpenAI TTS ou gTTS.
- O método de análise de imagem usa Gemini para extrair contexto de screenshot ou webcam antes da resposta.
- O método de seleção de ação escolhe entre extrair clipboard, tirar screenshot, apagar screenshot, capturar webcam ou seguir como genérico.
- O processamento principal salva o áudio, transcreve, identifica a ação e, quando necessário, gera a resposta em voz.
- O `main.py` importa os módulos do `src`, carrega as credenciais e inicia o método `listen()`.
- O script de shell automatiza criação de ambiente virtual, instalação de dependências e execução do programa.
