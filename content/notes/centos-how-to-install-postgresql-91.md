---
title: "CentOS: how to install postgresql 9.1"
date: '2012-05-23T22:13:44-03:00'
category: webclip
summary: 'The page lists the commands to add the pgdg CentOS 9.1 repository, exclude the default PostgreSQL packages in yum, install postgresql91-server, initialize the database, start the service, and enable it at boot.'
tags: ["centos", "postgresql", "yum", "replication"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "CentOS: how to install postgresql 9.1 | ag-up.com"
    url: "http://ag-up.com/?p=524"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-05/ag-up-com--centos-how-to-install-postgresql-91.md"
    kind: repo
---

The page gives a short installation sequence for PostgreSQL 9.1 on CentOS. It downloads and installs the pgdg repository RPM, adds a yum exclude rule for PostgreSQL in the CentOS Base repo, then installs the server package, initializes the database, starts the service, and enables it at boot. It also points to the PostgreSQL wiki for streaming replication.

## Reading notes

- Download the pgdg CentOS 9.1 repository RPM with wget and install it with rpm.
- Add `exclude=postgresql*` to the end of the `[base]` and `[updates]` sections in `/etc/yum.repos.d/CentOS-Base.repo`.
- Install `postgresql91-server` with yum.
- Initialize the database with `service postgresql-9.1 initdb`.
- Start PostgreSQL with `service postgresql-9.1 start`.
- Enable PostgreSQL at boot with `chkconfig postgresql-9.1 on`.
- For replication, consult the official PostgreSQL wiki page on streaming replication.
