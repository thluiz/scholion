---
title: "Criando um chat bot com Hubot, Slack, Docker e Azure"
date: '2016-01-07T16:27:13-03:00'
category: webclip
summary: 'O texto mostra como o Hubot se integra ao Slack, ganha um brain no Azure Storage e passa a rodar em Docker e docker-compose para simplificar o deploy e a manutenção.'
tags: ["hubot", "slack", "docker", "azure"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Criando um chat bot com Hubot, Slack, Docker e Azure"
    url: "http://blog.lambda3.com.br/2015/12/criando-um-chat-bot-com-hubot-slack-docker-e-azure/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-01/blog-lambda3-com-br--criando-um-chat-bot-com-hubot-slack-docker-e-azure.md"
    kind: repo
---

O texto apresenta o Hubot como um chat bot mais poderoso que o Slackbot, integrado por adaptadores a serviços como Slack, HipChat, Campfire e Skype. Também mostra exemplos de funções que ele pode executar com scripts, como comandos ligados a GitHub, YouTube, clima, Wolfram Alpha, lembretes e pomodoros.

## Fichamento

- O Slack é usado na Lambda3 há alguns meses e ajuda na comunicação da equipe.
- O Slack oferece integrações com ferramentas como Visual Studio Team Services e GitHub.
- O Slackbot responde a mensagens simples, como repetir "bom dia" quando alguém escreve "bom dia".
- O Hubot é um chat bot feito pelo GitHub, escrito em CoffeeScript, que roda sobre NodeJS e é livre.
- O Hubot usa adaptadores para se integrar a aplicações de chat, incluindo Slack, HipChat, Campfire e Skype.
- O Hubot depende de scripts para responder a comandos e traz scripts padrão pelo pacote hubot-scripts.
- A lista de comandos mostra funções ligadas a GitHub, buscas, clima, traduções, lembretes, pomodoros e relatórios de presença.
- O autor cria o Hubot com yeoman usando "yo hubot" e define nome, autor e adaptador.
- A integração com Slack exige criar o app do Hubot na página do Slack e obter uma API key.
- Para guardar dados, o Hubot usa um brain com Azure Storage por meio do pacote hubot-azure-scripts.
- A configuração do brain pede o nome da storage account e a chave de acesso.
- Os scripts do Hubot são ativados pelos arquivos hubot-scripts.json e external-scripts.json.
- Para rodar localmente, o autor usa um script que configura variáveis de ambiente públicas e seguras.
- A tentativa de rodar o Hubot como Azure website trouxe problemas com npm e com alguns pacotes de extensão.
- A solução escolhida foi usar Docker, com um Dockerfile baseado em Node e um docker-compose.yml simples.
- O docker-compose repassa variáveis de ambiente seguras e permite subir o serviço como daemon.
- O servidor final é um Ubuntu no Azure, e o Docker simplifica o deploy e a movimentação do serviço.
- O texto conclui que o Slack, o Hubot e o Azure permitem experimentar a solução com pouco custo.
