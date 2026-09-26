---
url: "https://gist.github.com/richardtape/269b3c1500fc46049a5d"
captured_at: "2026-09-27T00:27:39+01:00"
title: "Install Oh My ZSH on Ubuntu 14.04"
domain: "gist-github-com"
---

[![@richardtape](https://avatars.githubusercontent.com/u/116946?s=64&v=4)](https://gist.github.com/richardtape)

*   [Star (20)](https://gist.github.com/login?return_to=https%3A%2F%2Fgist.github.com%2Frichardtape%2F269b3c1500fc46049a5d) You must be signed in to star a gist
*   [Fork (12)](https://gist.github.com/login?return_to=https%3A%2F%2Fgist.github.com%2Frichardtape%2F269b3c1500fc46049a5d) You must be signed in to fork a gist

Install Oh My ZSH on Ubuntu 14.04

\# Where is the location of your current shall. Useful if we need to revert

echo $0

\# Install ZSH

sudo apt-get install zsh

\# Instal GIT

sudo apt-get install git-core

\# Install OhMyZSH

curl -L http://install.ohmyz.sh | sh

or

wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh

\# Where is ZSH installed i.e. /bin/zsh

which zsh

\# Change Shell

chsh

<sudo password>

/bin/zsh # Or whatever the path was from above
