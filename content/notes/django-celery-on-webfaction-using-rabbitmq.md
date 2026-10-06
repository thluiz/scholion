---
title: "Django-Celery on Webfaction using RabbitMQ"
date: '2015-03-30T09:11:26-03:00'
category: webclip
summary: 'Tutorial for setting up django-celery on Webfaction by installing Erlang and RabbitMQ, configuring broker settings, and running Celery with a daemon tool such as django-supervisor or daemonize.'
tags: ["django-celery", "rabbitmq", "webfaction", "celery"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Mark's Blog | Entries | Django-Celery on Webfaction using RabbitMQ"
    url: "http://www.markliu.me/2011/sep/29/django-celery-on-webfaction-using-rabbitmq/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-03/markliu-me--django-celery-on-webfaction-using-rabbitmq.md"
    kind: repo
---

The guide walks through setting up django-celery on Webfaction from scratch. It covers installing Erlang first, then RabbitMQ, then Celery and django-celery, and finally a way to run Celery as a daemon.

## Reading notes

- Erlang is installed manually on Webfaction because it is needed for RabbitMQ.
- RabbitMQ is set up with custom paths, environment variables, host entries, and an .erl_inetrc file.
- The setup creates a user and vhost, then restricts permissions to that vhost.
- django-celery is installed with pip, and the Django settings define broker host, port, user, password, vhost, concurrency, nodes, and AMQP as the result backend.
- The installed apps list must include djcelery.
- If the project uses mod_wsgi, the WSGI module must set CELERY_LOADER to "django".
- Celery does not daemonize itself, so the page recommends django-supervisor or daemonize.
- django-supervisor can start and stop celery through manage.py supervisor commands, but it uses more memory.
- daemonize is presented as the more memory-efficient option for running manage.py celeryd.
