---
url: "http://www.redmine.org/projects/redmine/wiki/HowTo_Easily_integrate_a_%28SSH_secured%29_GIT_repository_into_redmine"
captured_at: "2014-01-06T08:05:27-03:00"
title: "HowTo Easily integrate a (SSH secured) GIT repository into redmine - Redmine"
domain: "redmine-org"
---

# **H**owTo: Easily integrate a (SSH secured) GIT repository into redmine[¶](#HowTo-Easily-integrate-a-SSH-secured-GIT-repository-into-redmine)

## Scope[¶](#Scope)

This HowTo will show how to integrate a GIT repository to your redmine project and how to keep the repository up to date**.**

## Prerequisites[¶](#Prerequisites)

- The owner of your redmine-directory needs an SSH-Key and (reading) access to the repository you want to integrate in redmine**.**
- A directory to clone the GIT-repository is needed**.**
- Redmine must find the GIT-binaries, that means GIT must be installed**.** You can check this in redmine in the "administration > repositories" settings**.** If there is green checkmark everything is fine**.** If not you have to install GIT first, e.g. via "apt-get install"

### Example configuration[¶](#Example-configuration)

To better understand this HowTo I will use the following configuration

- My owner of redmine is called "redmine"
- My redmine main directory is "/var/lib/redmine" and I will create a subdirectory "repos" there, where I clone the repositories**.** So the full path of this directory is "/var/lib/redmine/repos/"
- The URL of my repo is "git**.**my-url.com", the name "my\_repo", so full URL is "[git@git**.**my-url.com](mailto:git@git.my-url.com) :my\_repo"

## Step 1: Clone the repositories[¶](#Step-1-Clone-the-repositories)

First we need to clone the repository as a **MIRROR** (not BARE**!**) repository. A mirror repository has no workfiles but only the commit information what is all we need for redmine**.**

We switch to redmine-user and clone the repository into the choosen directory**.**

```
sudo -su redmine
cd /var/lib/redmine/repos/
git clone --mirror git@git.my-url.com:my_repo my_repo
```

Now all repository information are on disk, but redmine don't knows anything about that**.** So in the next step we will change this.

## Step 2: Introduce the repository to redmine[¶](#Step-2-Introduce-the-repository-to-redmine)

Inside redmine we open the "administration > project -> repositories" dialog**.** You can access this dialog also via "project -> settings -> repositories"**.** There we add a new repository

```
Type: GIT
Main-repository: check this if the cloned repository is you main repository, if not leave it unchecked.
Name (redmine intern): I suggest to choose the same name as the repository, e.g. "my_repo" 
Path: Absolute path of the repository, e.g. "/var/lib/redmine/repos/my_repo"
```

Now redmine knows the repository**.** If you open the "repository"-tab inside your project you will see the repository tree, last commits and so on**.**

**Note**: When you open the dialog redmine fetchs all changeset **the local repository and the redmine database** since the last time anyone opend this dialog**.** Especially opening the dialog for the first time of a large repository may take very long**.** Don't cancel the progress, just let redmine work until it has finished**.** **Possible Fallacy**: When opening the dialog redmine **DOESN'T** fetch new commits out of GIT**!** This means that you will never see new commits inside redmine if you don't update the local GIT repository**.** For that we will write a cronjob in step 3.

## Step 3: Adding a cronjob to fetch the GIT-repository[¶](#Step-3-Adding-a-cronjob-to-fetch-the-GIT-repository)

To keep the GIT repository automatically up to date we will add a cronjob**.** With the "--all" parameter we define to fetch all branches**.**

We open the user specified crontab for the user "redmine" and add a cronjob to fetch all branches every five minutes**.**

```
sudo -e -u redmine

*/5 * * * * cd /var/lib/redmine/repos/my_repo && git fetch --all
```

Alternatively we can directly edit the "/etc/crontab"-file**.** If we do this we have to add the username of the repository-owner who should execute the commands**.**

```
nano /etc/crontab
*/5 * * * * redmine cd /var/lib/redmine/repos/my_repo && git fetch --all
```

**NOTE** If you clone multiple repositories you have to add a crontab-line for every repository**.**
