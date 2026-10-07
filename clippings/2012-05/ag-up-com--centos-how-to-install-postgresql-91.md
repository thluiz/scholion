---
url: "http://ag-up.com/?p=524"
captured_at: "2012-05-23T22:13:44-03:00"
title: "CentOS: how to install postgresql 9.1 | ag-up.com"
domain: "ag-up-com"
---

# CentOS: how to install postgresql 9.1

**$ wget http://yum.pgrpms.org/reporpms/9.1/pgdg-centos91-9.1-4.noarch.rpm**

**# rpm -i pgdg-centos91-9.1-4.noarch.rpm**

add **"exclude=postgresql\*** " (without quotes) to /etc/yum.repos.d/CentOS-Base.repo in the end of sections [base] and [updates].

**# yum install postgresql91-server**

**# service postgresql-9.1 initdb**

**# service postgresql-9.1 start**

**# chkconfig postgresql-9.1 on**

Replication:

how to make replication you can learn from official wiki:

<https://wiki.postgresql.org/wiki/Streaming_Replication>
