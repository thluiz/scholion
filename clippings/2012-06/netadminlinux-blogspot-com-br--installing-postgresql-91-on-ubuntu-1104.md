---
url: "http://netadminlinux.blogspot.com.br/2011/11/installing-postgresql-91-on-ubuntu-1104.html"
captured_at: "2012-06-13T20:43:18-03:00"
title: "linux tutorial: Installing PostgreSQL 9.1 on Ubuntu 11.04"
domain: "netadminlinux-blogspot-com-br"
---

# Installing PostgreSQL 9.1 on Ubuntu 11.04

**first install python-software-properties:**  
sudo apt-get install python-software-properties  
  
**now add repository and update apt.**  
sudo add-apt-repository ppa:pitti/postgresql  
sudo apt-get update  
  
**now instal postgresql**  
sudo apt-get install postgresql-9.1 libpq-dev  
  
**Now change the postgres user password (still running as root):**  
su postgres  
psql -d postgres -U postgres  
alter user postgres with password 'a';  
\q  
  
**To install GUI client pgsql**   
sudo apt-get install pgadmin3
