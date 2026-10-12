---
url: "https://www.digitalocean.com/community/articles/how-to-use-mina-to-deploy-a-ruby-on-rails-application"
captured_at: "2014-03-17T09:35:17-03:00"
title: "How To Use Mina to Deploy a Ruby on Rails Application | DigitalOcean"
domain: "digitalocean-com"
---

# How To Use Mina to Deploy a Ruby on Rails Application

### What the Red Means

The lines that users need to enter or customize will be in red in this tutorial!

---

### Introduction

---

Mina is a deployment tool that will let you build and run scripts to manage deployments on servers via SSH. Unlike Capistrano or Vlad, mina only creates one SSH session per deploy. Mina is built on Rake, which means there are no YAML files-- everything is written in Ruby, so configuration files are simply Rake files.  
You can use mina with any type of project deployable via SSH.

## Step One: Install Mina

---

With Ruby installed, you can install mina like any other gem, through RubyGems on the command line:

```
gem install mina
```

Or you can add mina at the bottom of Gemfile in your current rails application.

```
nano Gemfile
```

```
gem 'mina'
```

Note: If you don't have ruby installed on your system, you can check this tutorial: [How to Install Ruby On Rails on Ubuntu 12.04 LTS with rbenv](https://www.digitalocean.com/community/articles/how-to-install-ruby-on-rails-on-ubuntu-12-04-lts-with-rbenv--2)

## Step Two: Create and Edit deploy.rb

---

The file deploy.rb is a Rakefile invoked by Rake. In this file, we have to configure the server and define tasks that we later invoke using mina.
Before we go and create the deploy.rb file, let's understand some commands used in our file.  
  
Queue is a really useful command that lets us queue bash commands to be ran on the remote server.
Invoke command is a helper command used to invoke other tasks from a task.  
  
For example, let's suppose we have something like this in deploy.rb:

```
    set  :domain,  'myserver.com'
    set  :user,  'myuser'
    task :down do
      invoke :restart
      invoke :logs
    end

    task :restart do
      queue 'sudo service nginx restart'
    end

    task :logs do
      queue 'tail -f /var/log/nginx/error.log'
    end
```

If you are going to run mina restart in your terminal, mina will search a task with name restart and run the queued commands on the remote server specified on set :domain, via SSH. So in this case, mina restart is going to restart the nginx server on myserver.com  
  
Same thing happens for mina logs-- it invokes queue command (tail -f /var/log/nginx/error.log) remotely on the server using ssh myuser@myserver.com  
  
And for mina down, it invokes the subtasks(restart and logs) which queues up their commands.   
  
Let's generate the deploy.rb file. For this, run mina init in the rails application folder:

```
mina init
```

Let's open the file and configure the server:

```
nano config/deploy.rb
```

As you can see, the sample file is well commented so it will be very easy to understand what's happening there.  
  
At the beginning of the file, mina will require bundler, rails and git. If you are using rbenv or rvm, you have to uncomment line 4 or line 5.

```
    require 'mina/bundler' 
    require 'mina/rails' 
    require 'mina/git' 
    require 'mina/rbenv'
    # require 'mina/rvm'
```

On the lines 13-16 are the settings of domain, path to the deployed folder, repository and branch.

```
    # set :rails_env, 'production'
    set :domain, 'myserver.com' 
    set :deploy_to, '/home/myuser/myserver.com' 
    set :repository, 'https://github.com/my-git-user/my-repo.git'
    set :branch, 'master'
```

:rails\_env specify the environment used for deploy.
:domain is the hostname or ip address to SSH to
:deploy\_to is the path to deploy into, you can setup for any folder from your server, but be sure you have permissions.

```
chown -R user-name /var/www/mydir
```

:repository is the Git repository to clone from. You can use HTTP clone URL or a SSH clone URL, but for SSH clone URL you'll need to have your private key on the server (I don't recommend that), or to use some of mina magic. All you have to do is set :ssh\_options, '-A' and configure username and port.

```
    set :user, 'myuser'
    # set :port, '22'
    set :ssh_options, '-A'
```

After this, you have to put your host and enable forwardagent in your ~/.ssh/config.

```
nano ~/.ssh/config
```

And put this line there. Replace myserver.com with your host or ip address.

```
    Host myserver.com
    ForwardAgent yes
```

The first command will set the username to SSH to. If you are using a custom port for ssh, uncomment the second line. The third line will add -A flag to the ssh command to enable forwarding of the authentication agent connection. Basically, the last command tells ssh to use the same private key, used for logging into the server to clone the repository.  
  
In the environment task, you have to uncomment which environment you want to load. If you installed ruby using rbenv, uncomment line 32. For rvm, uncomment line 35.

```
    task :environment do
      
      invoke :'rbenv:load'
      # invoke :'rvm:use[ruby-1.9.3-p125@default]'
      
    end
```

**Note:** If you are using rvm, put your ruby version in the square brackets. You can find which ruby version you have installed using `ruby -v`  
  
In the task :setup, mina will create some folders and files using the path from deploy\_to, and change permission to that folders and files.
For the beginning, using the default folder structure is very convinient.  
  
At the end of the file, we have task :deploy. When we use mina deploy, all invokes written there are going to execute. By default, mina will clone the repository, deploy the shared\_paths, run a bundle install to get all needed gems to the server, migrate the database and precompile assets.

```
    task :deploy => :environment do 
      deploy do 
        invoke :'git:clone' 
        invoke :'deploy:link_shared_paths' 
        invoke :'bundle:install' 
        
        #invoke :'rails:db_migrate' 
        #invoke :'rails:assets_precompile' 
        
        to :launch do 
          queue "touch #{deploy_to}/tmp/restart.txt" 
        end 
      end 
    end
```

If you are using MySQL, you have to uncomment `#invoke :'rails:db_migrate'` . For more information about MySQL, please consult this [tutorial](https://www.digitalocean.com/community/articles/a-basic-mysql-tutorial) or look up for something more specific [here](https://www.digitalocean.com/community/community_tags/mysql).

## Step Three: Setup and Deploy

---

To create the folder structure configured in deploy.rb file run:

```
mina setup --verbose
```

Verbose command will let you see what's happening in this phase, and if something goes wrong here, you will see exactly which command fails.  
It shouldn't take more than 3 seconds for this step.  
  
To deploy the application run

```
mina deploy --trace
```

Trace command will show backtraces when errors occur.

## Optional Step Four: Example

---

Create a rails application:

```
rails new mynewapp
```

Change directory and add mina to the Gemfile:

```
cd mynewapp && nano Gemfile
```

Before creating deploy.rb, add your rails application to Github using:

```
    git init
    git remote add origin git@github.com:username/mynewapp.git
    git add .
    git commit -a -m 'start a new rails application'
    git push origin master
```

Create deploy.rb with desired content:

```
nano config/deploy.rb
```

This is how my deploy.rb looks for this project:

```
    require 'mina/bundler'
    require 'mina/rails'
    require 'mina/git'
    require 'mina/rbenv'

    set :rails_env, 'production'

    set :domain,     'ip_adress'
    set :deploy_to,  "/home/username/app/#{rails_env}"
    set :app_path,   "#{deploy_to}/#{current_path}"
    set :repository, 'https://github.com/username/mynewapp.git'
    set :branch,     'master'

    task :environment do
      invoke :'rbenv:load'
    end

    task deploy: :environment do

      deploy do
        invoke :'git:clone'
        invoke :'bundle:install'
      end
    end
```

**Note:** I'm using https instead of ssh. Also, this is a very simple deploy.rb file-- feel free to add tasks.   
  
Run `mina setup` to create all folders, then run `mina deploy` to deploy the rails application.   
  
You can see the result by logging into your VPS and checking this folder: `/home/username/app/production/current`. To test the rails application, run `bundle exec rails server` in this folder then open a browser and go to `ip_adress:3000`  
  
\*WEBrick is a simple HTTP Server written in Ruby. I don't recommend using WEBrick for production.

Submitted by: [Radu-Bogdan Croitoru](https://github.com/radubogdan)
