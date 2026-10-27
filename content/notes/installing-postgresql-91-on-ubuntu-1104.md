---
title: "Installing PostgreSQL 9.1 on Ubuntu 11.04"
date: '2012-06-13T20:43:18-03:00'
category: webclip
summary: 'The page lists the commands to add the PostgreSQL PPA on Ubuntu 11.04, install PostgreSQL 9.1 and libpq-dev, set the postgres user password, and install pgAdmin3.'
tags: ["postgresql", "ubuntu", "installation"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "linux tutorial: Installing PostgreSQL 9.1 on Ubuntu 11.04"
    url: "http://netadminlinux.blogspot.com.br/2011/11/installing-postgresql-91-on-ubuntu-1104.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-06/netadminlinux-blogspot-com-br--installing-postgresql-91-on-ubuntu-1104.md"
    kind: repo
---

The page gives a command sequence for installing PostgreSQL 9.1 on Ubuntu 11.04. It starts by installing python-software-properties, then adds the pitti/postgresql PPA and updates apt before installing postgresql-9.1 and libpq-dev.

## Reading notes

- Install python-software-properties first.
- Add the pitti/postgresql repository and run apt-get update.
- Install postgresql-9.1 and libpq-dev.
- Switch to the postgres user, open psql on the postgres database, and set the postgres password.
- Install pgadmin3 as a GUI client for PostgreSQL.
