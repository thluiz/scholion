---
url: "http://www.markliu.me/2011/sep/29/django-celery-on-webfaction-using-rabbitmq/"
captured_at: "2015-03-30T09:11:26-03:00"
title: "Mark's Blog | Entries | Django-Celery on Webfaction using RabbitMQ"
domain: "markliu-me"
---

# [Django-Celery on Webfaction using RabbitMQ](http://www.markliu.me/2011/sep/29/django-celery-on-webfaction-using-rabbitmq/)

This tutorial is meant to get you up and running from scratch with django-celery on Webfaction. Each of the steps is a bit of a hassle since you typically need to find different install steps for each individual part, so I just lumped up the whole experience in this guide.

## Install Erlang

Erlang is needed for installing RabbitMQ which is the preferred message broker for Celery. Webfaction doesn't come with this installed, so you'll need to do it manually:

- Go to the webfaction control panel and create a new app -> Custom App, Listening on Port
- Download the [latest version of Erlang](http://www.erlang.org/doc/installation_guide/INSTALL.html#How-to-Build-and-Install-ErlangOTP). You can just use the command: wget <http://www.erlang.org/download/otp_src_R14B03.tar.gz>
- Unzip it: gunzip -c otp\_src\_R14B03.tar.gz | tar xf -
- cd into the directory
- Configure the build: ./configure --prefix=/home/your\_webfaction\_username/
- Make it: make
- Install it: make install
- Run it on the port given to you when you created the new Erlang app: epmd -port 12345 -daemon

## Install RabbitMQ

- Go to the webfaction control panel and create a new app -> Custom App, Listening on Port
- Download the [latest version of the RabbitMQ server generic package](http://www.rabbitmq.com/server.html). You can just use the command: wget <http://www.rabbitmq.com/releases/rabbitmq-server/v2.6.1/rabbitmq-server-generic-unix-2.6.1.tar.gz>
- Unzip it: gunzip -c rabbitmq-server-generic-unix-2.6.1.tar.gz | tar xf -
- Simlink rabbitmq to the erlang lib directory: cd ~/lib/erlang/lib/; ln -s ../src/rabbitmq\_server-2.6.1 rabbitmq\_server-2.6.1

Next, you need to change the file ~/lib/rabbitmq/rabbitmq-server. I found some [information about this on the webfaction community forums](http://community.webfaction.com/questions/2366/can-i-use-rabbit-mq-on-the-shared-servers). Open your text editor and change three lines to:

> CONFIG\_FILE=~/src/rabbitmq\_server-2.6.1/sbin/
>
> LOG\_BASE=~/logs/user/rabbitmq
>
> MNESIA\_BASE=~/src/rabbitmq\_server-2.6.1/sbin/

Added these lines to the rabbitmq-env file and use the ports you reserved for epmd and rabbitmq in your earlier steps:

> export ERL\_EPMD\_PORT=12708
>
> export RABBITMQ\_NODE\_PORT=35478
>
> export ERL\_INETRC=$HOME/.erl\_inetrc

Added the file $HOME/hosts which looks like:

> 127.0.0.1 localhost.localdomain localhost
>
> ::1      localhost6.localdomain6 localhost6
>
> 127.0.0.1 web160 [web160.webfaction.com](http://web160.webfaction.com/)

Added the file $HOME/.erl\_inetrc which looks like:

> {hosts\_file, "/home/<your\_user\_name>/hosts"}.
>
> {lookup, [file,native]}.

Run Rabbitmq and check that it is working:

> ./rabbitmq-server -detached
>
> ./rabbitmqctl status

Finally, add a new user and vhost, and[configure it](http://www.rabbitmq.com/man/rabbitmqctl.1.man.html#User management) so only your app will have access to it.

> ./rabbitmqctl add\_user <username> <password>
>
> ./rabbitmqctl set\_user\_tags <username> administrator
>
> ./rabbitmqctl add\_vhost <vhostpath>
>
> ./rabbitmqctl set\_permissions -p <vhostpath> <username> ".\*" ".\*" ".\*"
>
> ./rabbitmqctl clear\_permissions -p <vhostpath> guest

## Install Celery and Django-Celery

> pip install django-celery

In your settings file, you will then need to add the lines:

> BROKER\_HOST = "localhost"
>
> BROKER\_PORT = 36784
>
> BROKER\_USER = "username"
>
> BROKER\_PASSWORD = "password"
>
> BROKER\_VHOST = "vhostpath"
>
> CELERYD\_CONCURRENCY = 1
>
> CELERYD\_NODES="w1"
>
> CELERY\_RESULT\_BACKEND="amqp"

The reason we set the concurrency so low is because Celery takes up a good amount of memory, and you are likely limited with your memory consumption on webfaction. The minimum amount of memory Celery can take will be however much it needs to run the main process (consuming messages, sending tasks to workers, etc), and a worker tasks that actually does stuff. Each of these will take up about 20-30MB of memory depending on the size of your Django app.

Add 'djcelery' to your installed apps.

Follow any other steps listed in their [installation guide](http://ask.github.com/django-celery/introduction.html#installation) that are relevant to your app.  If you are using mod\_wsgi, add the following to your .wsgi module:

> import os
>
> os.environ["CELERY\_LOADER"] = "django"

## Install a tool to create a Daemon

Celery [does not daemonize itself](http://docs.celeryq.org/en/latest/cookbook/daemonizing.html), and thus you need to do this yourself. Creating a daemon is [not exactly the same as simply running it in the background](http://stackoverflow.com/questions/958249/whats-the-difference-between-nohup-and-a-daemon), so you should install a tool that can help you do this. Celery recommends a couple options. One of the easiest ways is to use a simple tool called [django-supervisor](https://github.com/rfk/django-supervisor). To install this, just type:

> pip install django-supervisor

Add the file supervisord.conf in the same directory as manage.py, and add the content:

> [program:celeryd]
>
> command={{ PYTHON }} {{ PROJECT\_DIR }}/manage.py celeryd -l info
>
> [program:autoreload]
>
> exclude=true
>
> [program:runserver]
>
> exclude=true
>
> [program:celerybeat]
>
> exclude=true

Every time you restart your webserver, you can restart celery by issuing the following commands:

> python manage.py supervisor --daemonize
>
> python manage.py supervisor stop all
>
> python manage.py supervisor start all

However, there is a downside with using django-supervisor in that it will run in the background and take up another 20-30MB of memory. A more memory efficient way would be to install a tool called [daemonize](http://software.clapper.org/daemonize/). This page has very easy installation instructions. Once you install it, just add an alias to it in your .bashrc or .profile and then run:

> daemonize /<full\_path\_to\_django\_directory>/manage.py celeryd

Everything should then be up and running. Good luck!
