---
title: "Install and Configure Vim in Windows"
date: '2025-10-21T19:06:15+01:00'
category: webclip
summary: 'A guide to setting up Vim on Windows for Python work, covering PowerShell, Python, Git, ripgrep, Lua, Node, plugins, LSP, snippets, debugging, fuzzy finding, and gVim tweaks.'
tags: ["vim", "windows", "python-development", "editor-setup"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Install and Configure Vim in Windows"
    url: "https://shayallenhill.com/vim-in-windows"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-10/shayallenhill-com--install-and-configure-vim-in-windows.md"
    kind: repo
---

The guide walks through a Windows 11 setup for Vim aimed at Python development. It starts with Vim, PowerShell 7, a vimrc that preserves Vim defaults, and environment-variable setup, then adds Python, Git, ripgrep, Lua, Node, and other tools Vim can call from the shell.

It then builds out Vim with minpac, built-in and external plugins, LSP and completion, AI tools, snippets, Vimspector debugging, fuzzy finding, and common Tim Pope plugins. It finishes with Windows-specific gVim configuration, font and rendering tweaks, filetype settings, and a pre-commit workflow.

## Reading notes

- Vim on Windows works best when paired with external command-line tools and some upfront configuration.
- The guide prefers PowerShell 7, and notes that Vim should be told explicitly which shell to use.
- A custom vimrc should source $VIMRUNTIME/defaults.vim so Vim keeps its normal default behavior.
- Python support is made explicit by setting pythonthreehome and pythonthreedll for a chosen stable Python version.
- The Python Launcher is presented as a cleaner way to manage multiple Python versions.
- Git is configured from PowerShell with user identity, core.editor, merge and diff tools, default branch, and GitHub username.
- Ripgrep is set as Vim’s grepprg so :grep uses rg.
- Lua is optional, but the guide sets luadll so Vim can find lua54.dll.
- Node and Yarn are optional installs for plugins such as copilot.vim and vim-prettier.
- gVim fullscreen support can be added with a separate DLL and mapped to Ctrl+F11 and Ctrl+F12.
- minpac is used as the plugin manager, with PackUpdate, PackClean, and PackStatus commands.
- vim-lsp, vim-lsp-settings, asyncomplete.vim, and asyncomplete-lsp.vim provide LSP and completion support.
- Copilot and vim-ai are added as AI plugins, with vim-ai opening an AI chat buffer.
- UltiSnips is installed for snippets, with custom triggers and a Python docstring snippet example.
- Vimspector is configured with a .vimspector.json file for Python run and test setups.
- fuzzbox.vim is used for fuzzy finding, with Ctrl+P mapped to FuzzyGitFiles.
- vim-dispatch, vim-fugitive, and vim-obsession are treated as common plugins worth having.
- The guide uses after/ftplugin files for Python-specific settings and for the aichat buffer.
- A compiler file and vim-dispatch let Python buffers run pre-commit asynchronously through :Make.
