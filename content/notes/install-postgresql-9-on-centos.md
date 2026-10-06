---
title: "Install PostgreSQL 9 on CentOS"
date: '2012-06-30T19:39:42-03:00'
category: webclip
summary: 'The post walks through installing PostgreSQL 9.1 on CentOS with the PostgreSQL yum repository, then configuring startup, access, remote connections, Webmin, and optional PostGIS.'
tags: ["centos", "postgresql", "postgis", "webmin"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Install PostgreSQL 9 on CentOS : David Ghedini"
    url: "http://www.davidghedini.com/pg/entry/install_postgresql_9_on_centos"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-06/davidghedini-com--install-postgresql-9-on-centos.md"
    kind: repo
---

The post explains how to install PostgreSQL 9.1 on CentOS with the PostgreSQL repository and yum, then how to start the service, set the postgres password, and adjust configuration files for local and remote access. It also covers changes caused by PostgreSQL 9’s directory layout, including PATH updates and symlinks for older software that still expects the previous locations.

It also shows how to create a user and database, enable the service at boot, install PostGIS, and configure Webmin so it can manage PostgreSQL 9. The post ends with the specific Webmin paths and commands that need to be updated for the new PostgreSQL 9 structure.

## Reading notes

- Install PostgreSQL 9.1 from the PostgreSQL yum repository on CentOS, and use the same approach for Red Hat and Fedora with the appropriate RPM.
- Exclude the stock CentOS PostgreSQL packages in CentOS-Base.repo so yum uses the PostgreSQL repository packages.
- Install the server, libraries, development files, and contrib package with yum.
- Initialize the database with service postgresql-9.1 initdb and start the service with service postgresql-9.1 start.
- Set PGDATA for the postgres user to /var/lib/pgsql/9.1/data and add /usr/pgsql-9.1/bin to PATH.
- Set a password for the postgres superuser with ALTER USER after switching to the postgres account.
- Edit pg_hba.conf to change local authentication methods to md5, then reload the configuration.
- Edit postgresql.conf to set listen_addresses to '*' for remote access, and restart the service when changing the port or listen address.
- Create a database, create a user, assign ownership, connect as that user, create a table, insert a row, and list the table.
- Enable postgresql-9.1 at boot for run levels 2, 3, and 4 with chkconfig.
- Create symlinks from /usr/pgsql-9.1/bin/pg_config and the PostgreSQL 9.1 data and backups directories for older software that expects the old layout.
- Install PostGIS with postgis91 and postgis91-utils, then run postgis.sql and spatial_ref_sys.sql in a new database.
- Update Webmin module settings so it uses the PostgreSQL 9.1 psql path, service commands, PID file, pg_hba.conf path, and backup directory.
