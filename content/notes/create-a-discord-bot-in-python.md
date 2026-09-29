---
title: "Create a Discord Bot in Python"
date: '2022-05-05T20:40:10-03:00'
category: webclip
summary: 'The tutorial shows how to set up a Discord application, install Python dependencies, and build a bot that replies to simple messages and handles Minecraft commands for help, server status, load, and online players.'
tags: ["discord", "python", "minecraft-bot"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Create a Discord Bot in Python"
    url: "https://devdojo.com/ruanbekker/create-a-discord-bot-in-python"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-05/devdojo-com--create-a-discord-bot-in-python.md"
    kind: repo
---

The page walks through creating a Discord bot in Python, first as a simple bot that replies to `hello` and `goodbye`, then as a Minecraft bot with `!mc` subcommands for help, server usage, server status, and who is online. It also covers creating the Discord application, adding the bot through OAuth2, and storing the token in a `.env` file.

## Reading notes

- The tutorial uses a Python virtual environment and installs `discord` and `python-dotenv`.
- It says to create a Discord application, add a bot, and authorize it to a server through an OAuth2 URL.
- The basic bot loads `DISCORD_TOKEN` from `.env`, listens for messages, and replies with the sender name when the content is `hello` or `goodbye`.
- The Minecraft bot uses `commands.Bot(command_prefix="!")` and a `mc` command with an argument.
- `!mc help` sends a usage message.
- `!mc serverusage` gets the system load with `multiprocessing.cpu_count()` and `os.getloadavg()`.
- `!mc serverstatus` requests `https://api.mcsrvstat.us/2/{minecraft_server_url}` and reports whether the server is online.
- `!mc whoisonline` requests player data from the same API and formats the number of online players and their names.
- The page says the bot source code is in a GitHub repository.
