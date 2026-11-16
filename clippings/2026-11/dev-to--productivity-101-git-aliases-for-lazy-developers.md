---
url: "https://dev.to/mojemoron/productivity-101-git-aliases-for-lazy-developers-4hip"
captured_at: "2026-11-16T01:15:55+00:00"
title: "Productivity 101: Git Aliases for Lazy Developers"
domain: "dev-to"
---

According to Larry Wall, the original author of the Perl programming language, one of the qualities of a great program is laziness...  
"The quality that makes you go to great effort to reduce overall energy expenditure. It makes you write labor-saving programs that other people will find useful, and document what you wrote so you don’t have to answer so many questions about it. Hence, the first great virtue of a programmer."

Some years ago, I stumbled upon an interesting article- **Eliminate Stupid Mental Effort (ESME)**. I can't remember the author's name. The article explains why some developers are unproductive because they spend too much time on repetitive tasks that can easily be avoided.

As a lazy developer, I started using aliases in my git workflow to save myself from typing long commands. So instead of typing "git checkout master", my lazy self simply types "gom", which saves precious human fingertip power by allowing the shorter keystroke form.

**What are aliases?**  
Aliases are used to create shorter commands that map to longer commands.  
They are commonly found in popular utilities like bash.

**How to create aliases**  
Creating an alias is as simple as typing:  

```
alias ALIAS_NAME="ALIAS_COMMAND" # generic form
alias gom = "git checkout master" # git example
```

Enter fullscreen mode Exit fullscreen mode

To get started, make sure you have installed git bash or any bash program on your system.  
Open git bash, and type "cd" to get to your home directory.  
Type the following commands to create a **_.bashrc_** file that automatically runs whenever you open git bash.  

```
touch .bashrc # create a  .bashrc
```

Enter fullscreen mode Exit fullscreen mode

You can either open the **_.bashrc_** file with any code editor to start adding your aliases or use shell output redirection.

**Using Output Redirection**  
For example, let's add an alias for **_"git rebase"_** command  

```
cd ~ # to enter your home directory
echo alias gre=\"git rebase\" >> .bashrc
```

Enter fullscreen mode Exit fullscreen mode

**_To have this change taken into account you should then either source this file (ie: run source .bashrc) or restart your terminal._**

**Common examples of lazy git aliases**  

```
alias gs="git status" # to see changes that have been staged and which haven't
alias gac="git add . && git commit -m" # to stage and commit changes
#git push and pull
alias gp="git push" # + remote & branch names
alias gl="git pull" # + remote & branch names

# Pushing/pulling to origin remote
alias gpo="git push origin" # + branch name
alias glo="git pull origin" # + branch name

# Pushing/pulling to origin remote, master branch
alias gpom="git push origin master"
alias glom="git pull origin master"

alias gcb="git checkout -b" # To create a new branch and checkout into it
alias go="git checkout"
alias gom="git checkout master"
alias gre="git rebase"

alias gd='git diff' 
alias glo="git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"


```

Enter fullscreen mode Exit fullscreen mode

In conclusion, using git aliases in your git workflow will increase your productivity as an Engineer and eliminate stupid mental effort.

Also, note that aliases are not only meant for git workflow, you can also create aliases for any command you use frequently e.g Docker, Laravel, Ruby, Python, WordPress and Django commands, etc.

**What aliases are you using?**

Kindly follow me and turn on your notification.  
Thank you! Happy coding! ✌
