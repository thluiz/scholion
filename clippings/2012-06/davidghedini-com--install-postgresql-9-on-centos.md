---
url: "http://www.davidghedini.com/pg/entry/install_postgresql_9_on_centos"
captured_at: "2012-06-30T19:39:42-03:00"
title: "Install PostgreSQL 9 on CentOS : David Ghedini"
domain: "davidghedini-com"
---

# Install PostgreSQL 9 on CentOS

Tuesday Mar 01, 2011

[Install PostgreSQL 9 on CentOS](http://www.davidghedini.com/pg/entry/install_postgresql_9_on_centos "Install PostgreSQL 9 on CentOS")

This post will cover installing and basic configuration of PostgreSQL 9.x on CentOS.  
  
We will install PostgreSQL 9 using the PostgreSQL repository and yum.  
  
The same procedure can be used to install PostgreSQL 9 on Red Hat and Fedora using the appropriate rpm.  
  
Optionally, we'll also see how to install PostGIS.   
  
As the directory structure of PostgreSQL has changed with the release of PostgreSQL 9, we will also look a look at how we can create symlinks to make life easier when installing software or modules that still expect the old directory structure.  
  
Finally, for Webmin users, we will see how to configuring Webmin to manage PostgreSQL 9.  
  
I am using CentOS 6, but the same procedure works for CentOS 5.
Finally, if you are using Webmin, we will also show how to configure Webmin to manage PostgreSQL 9.  
  
With the release of PostgreSQL 9, the directory structure of PostgreSQL has changed.   
  
We will also creating symlinks (if needed) from the new PostgreSQL 9 file locations to the previous PostgreSQL 8 file locations.  
  
If you are looking trying to install PostgreSQL 9 on cPanel, please see my post [here.](http://www.davidghedini.com/pg/entry/installing_postgresql_9_on_cpanel)   
  
We'll use the simplest method to install, which is the postrgres repo rpms.

**1. Download and Install the PostgreSQL Repository**

Download the latest production release for your distro here: <http://yum.pgrpms.org/repopackages.php>   
  
The repo rpms are 32 and 64 bit specific.  
  
Since I am installing on CentOS 6 x64, I will need:  
  
<http://yum.pgrpms.org/9.1/redhat/rhel-5-x86_64/pgdg-centos91-9.1-4.noarch.rpm>  
  
So, using wget:   
  
*wget http://yum.pgrpms.org/9.1/redhat/rhel-6-x86\_64/pgdg-centos91-9.1-4.noarch.rpm*

1. [root@server1 ~]# wget http://yum.pgrpms.org/9.1/redhat/rhel-6-x86\_64/pgdg-centos91-9.1-4.noarch.rpm
2. --2011-11-01 00:11:50--  http://yum.pgrpms.org/9.1/redhat/rhel-6-x86\_64/pgdg-centos91-9.1-4.noarch.rpm
3. Resolving yum.pgrpms.org... 98.129.198.114
4. Connecting to yum.pgrpms.org|98.129.198.114|:80... connected.
5. HTTP request sent, awaiting response... 200 OK
6. Length: 5124 (5.0K) [application/x-redhat-package-manager]
7. Saving to: pgdg-centos91-9.1-4.noarch.rpm
8. 100%[======================================>] 5,124       --.-K/s   in 0s
9. 2011-11-01 00:11:51 (310 MB/s) - pgdg-centos91-9.1-4.noarch.rpm
10. [root@server1 ~]#

```
[root@server1 ~]# wget http://yum.pgrpms.org/9.1/redhat/rhel-6-x86_64/pgdg-centos91-9.1-4.noarch.rpm
--2011-11-01 00:11:50--  http://yum.pgrpms.org/9.1/redhat/rhel-6-x86_64/pgdg-centos91-9.1-4.noarch.rpm
Resolving yum.pgrpms.org... 98.129.198.114
Connecting to yum.pgrpms.org|98.129.198.114|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 5124 (5.0K) [application/x-redhat-package-manager]
Saving to: pgdg-centos91-9.1-4.noarch.rpm

100%[======================================>] 5,124       --.-K/s   in 0s

2011-11-01 00:11:51 (310 MB/s) - pgdg-centos91-9.1-4.noarch.rpm

[root@server1 ~]#
```

  
  
Now, install the repo....

1. [root@server1 ~]# rpm -i pgdg-centos91-9.1-4.noarch.rpm

```
[root@server1 ~]# rpm -i pgdg-centos91-9.1-4.noarch.rpm
```

  
  
We now need to edit the CentOS-Base.repo to exclude postgreql.  
  
To do, so we simply edit CentOS-Base.repo and add 'exclude=postgresql\*' to the [base] and [updates] sections:

1. [root@server1 ~]# cd /etc/yum.repos.d
2. [root@server1 yum.repos.d]# vi CentOS-Base.repo

```
[root@server1 ~]# cd /etc/yum.repos.d
[root@server1 yum.repos.d]# vi CentOS-Base.repo
```

1. [root@server1 yum.repos.d]# vi CentOS-Base.repo
2. # remarked out baseurl= line instead.
3. [base]
4. name=CentOS-$releasever - Base
5. mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=os
6. #baseurl=http://mirror.centos.org/centos/$releasever/os/$basearch/
7. gpgcheck=1
8. gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-6
9. exclude=postgresql\*
10. #released updates
11. [updates]
12. name=CentOS-$releasever - Updates
13. mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=updates
14. #baseurl=http://mirror.centos.org/centos/$releasever/updates/$basearch/
15. gpgcheck=1
16. gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-6
17. exclude=postgresql\*

```
[root@server1 yum.repos.d]# vi CentOS-Base.repo
# remarked out baseurl= line instead.
#
#

[base]
name=CentOS-$releasever - Base
mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=os
#baseurl=http://mirror.centos.org/centos/$releasever/os/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-6
exclude=postgresql*

#released updates
[updates]
name=CentOS-$releasever - Updates
mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=updates
#baseurl=http://mirror.centos.org/centos/$releasever/updates/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-6
exclude=postgresql*
```

  
  
Now, let's use 'yum list' to check the packages that are now available.

1. [root@server1 yum.repos.d]# yum list postgres\*
2. Loaded plugins: fastestmirror
3. base                                                     | 3.7 kB     00:00
4. base/primary\_db                                          | 4.2 MB     00:09
5. extras                                                   | 3.0 kB     00:00
6. extras/primary\_db                                        | 1.9 kB     00:00
7. pgdg91                                                   | 2.8 kB     00:00
8. pgdg91/primary\_db                                        |  79 kB     00:00
9. updates                                                  | 3.5 kB     00:00
10. updates/primary\_db                                       | 3.3 MB     00:00
11. vz-base                                                  |  951 B     00:00
12. vz-base/primary                                          | 1.3 kB     00:00
13. vz-base                                                                     3/3
14. vz-updates                                               |  951 B     00:00
15. vz-updates/primary                                       |  157 B     00:00
16. Available Packages
17. postgresql91.x86\_64                         9.1.1-1PGDG.rhel6             pgdg91
18. postgresql91-contrib.x86\_64                 9.1.1-1PGDG.rhel6             pgdg91
19. postgresql91-debuginfo.x86\_64               9.1.1-1PGDG.rhel6             pgdg91
20. postgresql91-devel.i686                     9.1.1-1PGDG.rhel6             pgdg91
21. postgresql91-devel.x86\_64                   9.1.1-1PGDG.rhel6             pgdg91
22. postgresql91-docs.x86\_64                    9.1.1-1PGDG.rhel6             pgdg91
23. postgresql91-jdbc.x86\_64                    9.1.901-1PGDG.rhel6           pgdg91
24. postgresql91-jdbc-debuginfo.x86\_64          9.1.901-1PGDG.rhel6           pgdg91
25. postgresql91-libs.i686                      9.1.1-1PGDG.rhel6             pgdg91
26. postgresql91-libs.x86\_64                    9.1.1-1PGDG.rhel6             pgdg91
27. postgresql91-odbc.x86\_64                    09.00.0200-1PGDG.rhel6        pgdg91
28. postgresql91-odbc-debuginfo.x86\_64          09.00.0200-1PGDG.rhel6        pgdg91
29. postgresql91-plperl.x86\_64                  9.1.1-1PGDG.rhel6             pgdg91
30. postgresql91-plpython.x86\_64                9.1.1-1PGDG.rhel6             pgdg91
31. postgresql91-pltcl.x86\_64                   9.1.1-1PGDG.rhel6             pgdg91
32. postgresql91-python.x86\_64                  4.0-2PGDG.rhel6               pgdg91
33. postgresql91-python-debuginfo.x86\_64        4.0-2PGDG.rhel6               pgdg91
34. postgresql91-server.x86\_64                  9.1.1-1PGDG.rhel6             pgdg91
35. postgresql91-tcl.x86\_64                     1.9.0-1.rhel6                 pgdg91
36. postgresql91-tcl-debuginfo.x86\_64           1.9.0-1.rhel6                 pgdg91
37. postgresql91-test.x86\_64                    9.1.1-1PGDG.rhel6             pgdg91
38. postgresql\_autodoc.noarch                   1.40-1.rhel6                  pgdg91
39. [root@server1 yum.repos.d]#

```
[root@server1 yum.repos.d]# yum list postgres*
Loaded plugins: fastestmirror
base                                                     | 3.7 kB     00:00
base/primary_db                                          | 4.2 MB     00:09
extras                                                   | 3.0 kB     00:00
extras/primary_db                                        | 1.9 kB     00:00
pgdg91                                                   | 2.8 kB     00:00
pgdg91/primary_db                                        |  79 kB     00:00
updates                                                  | 3.5 kB     00:00
updates/primary_db                                       | 3.3 MB     00:00
vz-base                                                  |  951 B     00:00
vz-base/primary                                          | 1.3 kB     00:00
vz-base                                                                     3/3
vz-updates                                               |  951 B     00:00
vz-updates/primary                                       |  157 B     00:00
Available Packages
postgresql91.x86_64                         9.1.1-1PGDG.rhel6             pgdg91
postgresql91-contrib.x86_64                 9.1.1-1PGDG.rhel6             pgdg91
postgresql91-debuginfo.x86_64               9.1.1-1PGDG.rhel6             pgdg91
postgresql91-devel.i686                     9.1.1-1PGDG.rhel6             pgdg91
postgresql91-devel.x86_64                   9.1.1-1PGDG.rhel6             pgdg91
postgresql91-docs.x86_64                    9.1.1-1PGDG.rhel6             pgdg91
postgresql91-jdbc.x86_64                    9.1.901-1PGDG.rhel6           pgdg91
postgresql91-jdbc-debuginfo.x86_64          9.1.901-1PGDG.rhel6           pgdg91
postgresql91-libs.i686                      9.1.1-1PGDG.rhel6             pgdg91
postgresql91-libs.x86_64                    9.1.1-1PGDG.rhel6             pgdg91
postgresql91-odbc.x86_64                    09.00.0200-1PGDG.rhel6        pgdg91
postgresql91-odbc-debuginfo.x86_64          09.00.0200-1PGDG.rhel6        pgdg91
postgresql91-plperl.x86_64                  9.1.1-1PGDG.rhel6             pgdg91
postgresql91-plpython.x86_64                9.1.1-1PGDG.rhel6             pgdg91
postgresql91-pltcl.x86_64                   9.1.1-1PGDG.rhel6             pgdg91
postgresql91-python.x86_64                  4.0-2PGDG.rhel6               pgdg91
postgresql91-python-debuginfo.x86_64        4.0-2PGDG.rhel6               pgdg91
postgresql91-server.x86_64                  9.1.1-1PGDG.rhel6             pgdg91
postgresql91-tcl.x86_64                     1.9.0-1.rhel6                 pgdg91
postgresql91-tcl-debuginfo.x86_64           1.9.0-1.rhel6                 pgdg91
postgresql91-test.x86_64                    9.1.1-1PGDG.rhel6             pgdg91
postgresql_autodoc.noarch                   1.40-1.rhel6                  pgdg91
[root@server1 yum.repos.d]#
```

**2. Install PostgreSQL 9.1 Using Yum**

We can now install PostgreSQL 9 using yum:  
  
*yum install postgresql91 postgresql91-devel postgresql91-server postgresql91-libs postgresql91-contrib*

1. [root@server1 yum.repos.d]# yum install postgresql91 postgresql91-devel postgresql91-server postgresql91-libs postgresql91-contrib
2. Loaded plugins: fastestmirror
3. Determining fastest mirrors
4. \* base: mirror.us.leaseweb.net
5. \* extras: mirror.lug.udel.edu
6. \* updates: centos.mirror.choopa.net
7. Setting up Install Process
8. Resolving Dependencies
9. --> Running transaction check
10. ---> Package postgresql91.x86\_64 0:9.1.1-1PGDG.rhel6 set to be updated
11. ---> Package postgresql91-devel.x86\_64 0:9.1.1-1PGDG.rhel6 set to be updated
12. ---> Package postgresql91-libs.x86\_64 0:9.1.1-1PGDG.rhel6 set to be updated
13. ---> Package postgresql91-server.x86\_64 0:9.1.1-1PGDG.rhel6 set to be updated
14. --> Finished Dependency Resolution
15. Dependencies Resolved
16. ================================================================================
17. Package                  Arch        Version                 Repository   Size
18. ================================================================================
19. Installing:
20. postgresql91             x86\_64      9.1.1-1PGDG.rhel6       pgdg91      939 k
21. postgresql91-devel       x86\_64      9.1.1-1PGDG.rhel6       pgdg91      1.4 M
22. postgresql91-libs        x86\_64      9.1.1-1PGDG.rhel6       pgdg91      186 k
23. postgresql91-server      x86\_64      9.1.1-1PGDG.rhel6       pgdg91      3.4 M
24. Transaction Summary
25. ================================================================================
26. Install       4 Package(s)
27. Upgrade       0 Package(s)
28. Total download size: 5.9 M
29. Installed size: 25 M
30. Is this ok [y/N]: y
31. Downloading Packages:
32. (1/4): postgresql91-9.1.1-1PGDG.rhel6.x86\_64.rpm         | 939 kB     00:02
33. (2/4): postgresql91-devel-9.1.1-1PGDG.rhel6.x86\_64.rpm   | 1.4 MB     00:01
34. (3/4): postgresql91-libs-9.1.1-1PGDG.rhel6.x86\_64.rpm    | 186 kB     00:00
35. (4/4): postgresql91-server-9.1.1-1PGDG.rhel6.x86\_64.rpm  | 3.4 MB     00:02
36. --------------------------------------------------------------------------------
37. Total                                           800 kB/s | 5.9 MB     00:07
38. Running rpm\_check\_debug
39. Running Transaction Test
40. Transaction Test Succeeded
41. Running Transaction
42. Installing     : postgresql91-libs-9.1.1-1PGDG.rhel6.x86\_64               1/4
43. Installing     : postgresql91-9.1.1-1PGDG.rhel6.x86\_64                    2/4
44. Installing     : postgresql91-server-9.1.1-1PGDG.rhel6.x86\_64             3/4
45. Installing     : postgresql91-devel-9.1.1-1PGDG.rhel6.x86\_64              4/4
46. Installed:
47. postgresql91.x86\_64 0:9.1.1-1PGDG.rhel6
48. postgresql91-devel.x86\_64 0:9.1.1-1PGDG.rhel6
49. postgresql91-libs.x86\_64 0:9.1.1-1PGDG.rhel6
50. postgresql91-server.x86\_64 0:9.1.1-1PGDG.rhel6
51. Complete!
52. [root@server1 yum.repos.d]#

```
[root@server1 yum.repos.d]# yum install postgresql91 postgresql91-devel postgresql91-server postgresql91-libs postgresql91-contrib
Loaded plugins: fastestmirror
Determining fastest mirrors
 * base: mirror.us.leaseweb.net
 * extras: mirror.lug.udel.edu
 * updates: centos.mirror.choopa.net
Setting up Install Process
Resolving Dependencies
--> Running transaction check
---> Package postgresql91.x86_64 0:9.1.1-1PGDG.rhel6 set to be updated
---> Package postgresql91-devel.x86_64 0:9.1.1-1PGDG.rhel6 set to be updated
---> Package postgresql91-libs.x86_64 0:9.1.1-1PGDG.rhel6 set to be updated
---> Package postgresql91-server.x86_64 0:9.1.1-1PGDG.rhel6 set to be updated
--> Finished Dependency Resolution

Dependencies Resolved

================================================================================
 Package                  Arch        Version                 Repository   Size
================================================================================
Installing:
 postgresql91             x86_64      9.1.1-1PGDG.rhel6       pgdg91      939 k
 postgresql91-devel       x86_64      9.1.1-1PGDG.rhel6       pgdg91      1.4 M
 postgresql91-libs        x86_64      9.1.1-1PGDG.rhel6       pgdg91      186 k
 postgresql91-server      x86_64      9.1.1-1PGDG.rhel6       pgdg91      3.4 M

Transaction Summary
================================================================================
Install       4 Package(s)
Upgrade       0 Package(s)

Total download size: 5.9 M
Installed size: 25 M
Is this ok [y/N]: y
Downloading Packages:
(1/4): postgresql91-9.1.1-1PGDG.rhel6.x86_64.rpm         | 939 kB     00:02
(2/4): postgresql91-devel-9.1.1-1PGDG.rhel6.x86_64.rpm   | 1.4 MB     00:01
(3/4): postgresql91-libs-9.1.1-1PGDG.rhel6.x86_64.rpm    | 186 kB     00:00
(4/4): postgresql91-server-9.1.1-1PGDG.rhel6.x86_64.rpm  | 3.4 MB     00:02
--------------------------------------------------------------------------------
Total                                           800 kB/s | 5.9 MB     00:07
Running rpm_check_debug
Running Transaction Test
Transaction Test Succeeded
Running Transaction
  Installing     : postgresql91-libs-9.1.1-1PGDG.rhel6.x86_64               1/4
  Installing     : postgresql91-9.1.1-1PGDG.rhel6.x86_64                    2/4
  Installing     : postgresql91-server-9.1.1-1PGDG.rhel6.x86_64             3/4
  Installing     : postgresql91-devel-9.1.1-1PGDG.rhel6.x86_64              4/4

Installed:
  postgresql91.x86_64 0:9.1.1-1PGDG.rhel6
  postgresql91-devel.x86_64 0:9.1.1-1PGDG.rhel6
  postgresql91-libs.x86_64 0:9.1.1-1PGDG.rhel6
  postgresql91-server.x86_64 0:9.1.1-1PGDG.rhel6

Complete!
[root@server1 yum.repos.d]#
```

**3. Initialize and Start PostgreSQL 9.1**

We can now initialize and Start PostgreSQL  
  
*NOTE: when using Webmin, please see 'Configuring Webmin to Manage PostgreSQL9 below*:

1. [root@server1 yum.repos.d]# service postgresql-9.1 initdb
2. Initializing database:                                     [  OK  ]
3. [root@server1 yum.repos.d]#

```
[root@server1 yum.repos.d]# service postgresql-9.1 initdb
Initializing database:                                     [  OK  ]
[root@server1 yum.repos.d]#
```

  
  
Start the PostgreSQL server:

1. [root@server1 yum.repos.d]# service postgresql-9.1 start
2. Starting postgresql-9.1 service:                           [  OK  ]
3. [root@server1 yum.repos.d]#

```
[root@server1 yum.repos.d]# service postgresql-9.1 start
Starting postgresql-9.1 service:                           [  OK  ]
[root@server1 yum.repos.d]#
```

  
  
If you encounter startup errors, check under /var/lib/pgsql/9.1/data/pg\_log for clues.

**4. Set PostgreSQL 9 Environment**

The deault home directory for the user postgres is at /var/lib/pgsql  
  
The bash\_profile for the user postgres will look like this:

1. [ -f /etc/profile ] && source /etc/profile
2. PGDATA=/var/lib/pgsql/9.1/data
3. export PGDATA

```
[ -f /etc/profile ] && source /etc/profile
PGDATA=/var/lib/pgsql/9.1/data
export PGDATA
```

  
  
This contains a path for the data directory, but no path for the executable/binary directory. To ammend this, add the path as below:

1. [ -f /etc/profile ] && source /etc/profile
2. PGDATA=/var/lib/pgsql/9.1/data
3. export PGDATA
4. PATH=$PATH:$HOME/bin:/usr/pgsql-9.1/bin
5. export PATH

```
[ -f /etc/profile ] && source /etc/profile
PGDATA=/var/lib/pgsql/9.1/data
export PGDATA
PATH=$PATH:$HOME/bin:/usr/pgsql-9.1/bin
export PATH
```

  
  
Placing the binary directory in the path for postgres will allow you to invoke pg\_ctl and other commands from the shell.

**5. Set postgres Password**

The superuser postgres has no password set by default.  
  
To set the password, switch to postgres user:

1. [root@server1 yum.repos.d]# su - postgres

```
[root@server1 yum.repos.d]# su - postgres
```

  
  
Connect as postgres to the postgres database and set the password for user postgres using alter user as below:

1. -bash-4.1$ psql postgres postgres
2. psql (9.1.1)
3. Type "help" for help.
4. postgres=# alter user postgres with password 'postgres';
5. ALTER ROLE
6. postgres=#

```
-bash-4.1$ psql postgres postgres
psql (9.1.1)
Type "help" for help.

postgres=# alter user postgres with password 'postgres';
ALTER ROLE
postgres=#
```

**6. Configure PostgreSQL 9 pg\_hba.conf File**

Locate your pg\_hba.conf file under /var/lib/pgsql/9.1/data  
  
On installation, your pg\_hba.conf file will look like this:

1. [root@server1 yum.repos.d]# vi /var/lib/pgsql/9.1/data/pg\_hba.conf
2. # Put your actual configuration here
3. # ----------------------------------
4. # If you want to allow non-local connections, you need to add more
5. # "host" records.  In that case you will also need to make PostgreSQL
6. # listen on a non-local interface via the listen\_addresses
7. # configuration parameter, or via the -i or -h command line switches.
8. # TYPE  DATABASE        USER            ADDRESS                 METHOD
9. # "local" is for Unix domain socket connections only
10. local   all             all                                     peer
11. # IPv4 local connections:
12. host    all             all             127.0.0.1/32            ident
13. # IPv6 local connections:
14. host    all             all             ::1/128                 ident
15. # Allow replication connections from localhost, by a user with the
16. # replication privilege.
17. #local   replication     postgres                                peer
18. #host    replication     postgres        127.0.0.1/32            ident
19. #host    replication     postgres        ::1/128                 ident

```
[root@server1 yum.repos.d]# vi /var/lib/pgsql/9.1/data/pg_hba.conf
# Put your actual configuration here
# ----------------------------------
#
# If you want to allow non-local connections, you need to add more
# "host" records.  In that case you will also need to make PostgreSQL
# listen on a non-local interface via the listen_addresses
# configuration parameter, or via the -i or -h command line switches.

# TYPE  DATABASE        USER            ADDRESS                 METHOD

# "local" is for Unix domain socket connections only
local   all             all                                     peer
# IPv4 local connections:
host    all             all             127.0.0.1/32            ident
# IPv6 local connections:
host    all             all             ::1/128                 ident
# Allow replication connections from localhost, by a user with the
# replication privilege.
#local   replication     postgres                                peer
#host    replication     postgres        127.0.0.1/32            ident
#host    replication     postgres        ::1/128                 ident
```

  
  
Change the METHOD to md5 as shown below:

1. # TYPE  DATABASE        USER            ADDRESS                 METHOD
2. # "local" is for Unix domain socket connections only
3. local   all             all                                     md5
4. # IPv4 local connections:
5. host    all             all             127.0.0.1/32            md5
6. # IPv6 local connections:
7. host    all             all             ::1/128                 md5

```
# TYPE  DATABASE        USER            ADDRESS                 METHOD

# "local" is for Unix domain socket connections only
local   all             all                                     md5
# IPv4 local connections:
host    all             all             127.0.0.1/32            md5
# IPv6 local connections:
host    all             all             ::1/128                 md5
```

  
  
In order for the change to take effect, reload the pg\_hba.conf file.  
  
As with any command, there are several ways you can reload the pg\_hba.conf file.  
  
Method 1: From the shell using pg\_ctl reload:

1. [root@server1 yum.repos.d]# su - postgres
2. -bash-4.1$ pg\_ctl reload
3. server signaled
4. -bash-4.1$

```
[root@server1 yum.repos.d]# su - postgres
-bash-4.1$ pg_ctl reload
server signaled
-bash-4.1$
```

  
  
Method 2: From psql using pg\_reload\_conf();

1. -bash-4.1$ psql postgres postgres
2. psql (9.1.1)
3. Type "help" for help.
4. postgres=# select pg\_reload\_conf();
5. pg\_reload\_conf
6. ----------------
7. (1 row)
8. postgres=#

```
-bash-4.1$ psql postgres postgres
psql (9.1.1)
Type "help" for help.

postgres=# select pg_reload_conf();
 pg_reload_conf
----------------
 t
(1 row)

postgres=#
```

Method 3: From the shell using -c switch to run select pg\_reload\_conf();

1. -bash-4.1$ psql postgres postgres -c "select pg\_reload\_conf();"
2. Password for user postgres:
3. pg\_reload\_conf
4. ----------------
5. (1 row)
6. -bash-4.1$

```
-bash-4.1$ psql postgres postgres -c "select pg_reload_conf();"
Password for user postgres:
 pg_reload_conf
----------------
 t
(1 row)

-bash-4.1$
```

**7. Configure Remote Access for PostgreSQL 9**

Locate the postgresql.conf file under /var/lib/pgsql/9.1/data.  
  
Look for CONNECTIONS AND AUTHENTICATION. It will look as below:

1. #------------------------------------------------------------------------------
2. # CONNECTIONS AND AUTHENTICATION
3. #------------------------------------------------------------------------------
4. # - Connection Settings -
5. #listen\_addresses = 'localhost'     # what IP address(es) to listen on;
6. # comma-separated list of addresses;
7. # defaults to 'localhost', '\*' = all
8. # (change requires restart)
9. #port = 5432                # (change requires restart)

```
#------------------------------------------------------------------------------
# CONNECTIONS AND AUTHENTICATION
#------------------------------------------------------------------------------

# - Connection Settings -

#listen_addresses = 'localhost'		# what IP address(es) to listen on;
					# comma-separated list of addresses;
					# defaults to 'localhost', '*' = all
					# (change requires restart)
#port = 5432				# (change requires restart)
```

  
  
By default, access is limited to local machine (localhost).  
  
To enable remote connections, uncomment listen\_addresses and change to '\*' as shown below.

1. #------------------------------------------------------------------------------
2. # CONNECTIONS AND AUTHENTICATION
3. #------------------------------------------------------------------------------
4. # - Connection Settings -
5. listen\_addresses = '\*'      # what IP address(es) to listen on;
6. # comma-separated list of addresses;
7. # defaults to 'localhost', '\*' = all
8. # (change requires restart)
9. #port = 5432                # (change requires restart)

```
#------------------------------------------------------------------------------
# CONNECTIONS AND AUTHENTICATION
#------------------------------------------------------------------------------

# - Connection Settings -

listen_addresses = '*'		# what IP address(es) to listen on;
					# comma-separated list of addresses;
					# defaults to 'localhost', '*' = all
					# (change requires restart)
#port = 5432				# (change requires restart)
```

  
  
You can also set the listen\_address limit to a specific IP (or IPs using a comma separated list).  
  
Note: For security, it is also a good idea to change the default port. To do this, uncomment port and set to a new port value.   
  
If you change the port, you will need to restart the service.  
  
Restart the postgresql service:

1. service postgresql-9.1 restart
2. Stopping postgresql-9.1 service:                           [  OK  ]
3. Starting postgresql-9.1 service:                           [  OK  ]
4. [root@server1 yum.repos.d]#

```
service postgresql-9.1 restart
Stopping postgresql-9.1 service:                           [  OK  ]
Starting postgresql-9.1 service:                           [  OK  ]
[root@server1 yum.repos.d]#
```

  
  
If you encounter startup errors, check under /var/lib/pgsql/9.1/data/pg\_log for clues.  
  
Verify the changes to listen\_address and port (if changed):

1. -bash-4.1$ psql
2. Password:
3. psql (9.1.1)
4. Type "help" for help.
5. postgres=# show listen\_addresses;
6. listen\_addresses
7. ------------------
8. (1 row)
9. postgres=# show port;
10. ------
11. (1 row)
12. postgres=#

```
-bash-4.1$ psql
Password:
psql (9.1.1)
Type "help" for help.

postgres=# show listen_addresses;
 listen_addresses
------------------
 *
(1 row)

postgres=# show port;
 port
------
 5432
(1 row)

postgres=#
```

**8. Create User and Database for PostgreSQL 9**

To check Check functionality, connect to postgres db as user postgres.

1. [root@server1 yum.repos.d]# psql postgres postgres
2. Password for user postgres:
3. psql (9.1.1)
4. Type "help" for help.
5. postgres=#

```
[root@server1 yum.repos.d]# psql postgres postgres
Password for user postgres:
psql (9.1.1)
Type "help" for help.

postgres=#
```

  
  
Create a user:

1. postgres=# create user myuser with password 'secret';
2. CREATE ROLE

```
postgres=# create user myuser with password 'secret';
CREATE ROLE
```

  
  
Create a database and give ownership to the new user:

1. postgres=# create database mytestdb owner=myuser;
2. CREATE DATABASE

```
postgres=# create database mytestdb owner=myuser;
CREATE DATABASE
```

  
  
Connect to the database as user:

1. postgres=# \c mytestdb myuser
2. Password for user myuser:
3. You are now connected to database "mytestdb" as user "myuser".

```
postgres=# \c mytestdb myuser
Password for user myuser:
You are now connected to database "mytestdb" as user "myuser".
```

  
  
Create a table and insert row(s):

1. mytestdb=> create table testtable (col1 varchar);
2. CREATE TABLE
3. mytestdb=> insert into testtable values('hello');
4. INSERT 0 1

```
mytestdb=> create table testtable (col1 varchar);
CREATE TABLE
mytestdb=> insert into testtable values('hello');
INSERT 0 1
```

  
  
Select on the table you created:

1. mytestdb=> select \* from testtable;
2. -------
3. hello
4. (1 row)
5. mytestdb=>

```
mytestdb=> select * from testtable;
 col1
-------
 hello
(1 row)

mytestdb=>
```

  
  
Describe table:

1. mytestdb=> \dt
2. List of relations
3. Schema |   Name    | Type  | Owner
4. --------+-----------+-------+--------
5. public | testtable | table | myuser
6. (1 row)

```
mytestdb=> \dt
          List of relations
 Schema |   Name    | Type  | Owner
--------+-----------+-------+--------
 public | testtable | table | myuser
(1 row)
```

  
  
Note that by default the schema used is Public. You should create a specific schema for your users.

**9. Configure PostgreSQL 9 Service to Start at Boot**

By default, the service postgresql-9.1 is added to chkconifg, but all run levels are set to off.  
  
Add for run levels 2,3, and 4 for the postgresql-9.1 service.

1. [root@server1 yum.repos.d]# chkconfig --level 234 postgresql-9.1 on

```
[root@server1 yum.repos.d]# chkconfig --level 234 postgresql-9.1 on
```

**10. Create Symlinks for Backward Compatibility from PostgreSQL 9 to PostgreSQL 8**

Many, if not most, third party software and modules are still be set to look for PoistgreSQL's conf file and data directory under their old (pre-version 9) locations.  
  
You can address this, and make life easier for yourself, by creating a few symlinks from the new locations to the old.  
  
Symlink 1: Symlink for the binary directory. This is particularly useful as this is the location of the pg\_config file

1. root@server1 [~]# ln -s /usr/pgsql-9.1/bin/pg\_config /usr/bin

```
root@server1 [~]# ln -s /usr/pgsql-9.1/bin/pg_config /usr/bin
```

  
  
Symlink 2: Symlink for the old data directory location of /var/lob/pgsql

1. root@server1 [~]# ln -s /var/lib/pgsql/9.1/data /var/lib/pgsql
2. root@server1 [~]# ln -s /var/lib/pgsql/9.1/backups /var/lib/pgsql

```
root@server1 [~]# ln -s /var/lib/pgsql/9.1/data /var/lib/pgsql  
root@server1 [~]# ln -s /var/lib/pgsql/9.1/backups /var/lib/pgsql
```

**11. Install PostGIS on PostgreSQL 9**

Using the postgresql repo, we can easily install PostGIS if we wish to.  
  
The installtion will also install Proj4 and Geos and required perl modules.

1. [root@server1 yum.repos.d]# yum install postgis91 postgis91-utils
2. Loaded plugins: fastestmirror
3. Loading mirror speeds from cached hostfile
4. \* base: mirror.us.leaseweb.net
5. \* extras: mirror.lug.udel.edu
6. \* updates: centos.mirror.choopa.net
7. Setting up Install Process
8. Resolving Dependencies
9. --> Running transaction check
10. ---> Package postgis91.x86\_64 0:1.5.3-2.rhel6 set to be updated
11. --> Processing Dependency: proj for package: postgis91-1.5.3-2.rhel6.x86\_64
12. --> Processing Dependency: geos for package: postgis91-1.5.3-2.rhel6.x86\_64
13. --> Processing Dependency: libgeos\_c.so.1()(64bit) for package: postgis91-1.5.3-2.rhel6.x86\_64
14. --> Processing Dependency: libproj.so.0()(64bit) for package: postgis91-1.5.3-2.rhel6.x86\_64
15. ---> Package postgis91-utils.x86\_64 0:1.5.3-2.rhel6 set to be updated
16. --> Processing Dependency: perl-DBD-Pg for package: postgis91-utils-1.5.3-2.rhel6.x86\_64
17. --> Running transaction check
18. ---> Package geos.x86\_64 0:3.3.0-1.rhel6 set to be updated
19. ---> Package perl-DBD-Pg.x86\_64 0:2.15.1-3.el6 set to be updated
20. --> Processing Dependency: perl(DBI) for package: perl-DBD-Pg-2.15.1-3.el6.x86\_64
21. ---> Package proj.x86\_64 0:4.7.0-1.rhel6 set to be updated
22. --> Running transaction check
23. ---> Package perl-DBI.x86\_64 0:1.609-4.el6 set to be updated
24. --> Finished Dependency Resolution
25. Dependencies Resolved
26. ================================================================================
27. Package                Arch          Version               Repository     Size
28. ================================================================================
29. Installing:
30. postgis91              x86\_64        1.5.3-2.rhel6         pgdg91        1.3 M
31. postgis91-utils        x86\_64        1.5.3-2.rhel6         pgdg91         21 k
32. Installing for dependencies:
33. geos                   x86\_64        3.3.0-1.rhel6         pgdg91        502 k
34. perl-DBD-Pg            x86\_64        2.15.1-3.el6          base          197 k
35. perl-DBI               x86\_64        1.609-4.el6           base          705 k
36. proj                   x86\_64        4.7.0-1.rhel6         pgdg91        157 k
37. Transaction Summary
38. ================================================================================
39. Install       6 Package(s)
40. Upgrade       0 Package(s)
41. Total download size: 2.9 M
42. Installed size: 11 M
43. Is this ok [y/N]: y
44. Running rpm\_check\_debug
45. Running Transaction Test
46. Transaction Test Succeeded
47. Running Transaction
48. Installing     : proj-4.7.0-1.rhel6.x86\_64                                1/6
49. Installing     : perl-DBI-1.609-4.el6.x86\_64                              2/6
50. Installing     : perl-DBD-Pg-2.15.1-3.el6.x86\_64                          3/6
51. Installing     : geos-3.3.0-1.rhel6.x86\_64                                4/6
52. Installing     : postgis91-1.5.3-2.rhel6.x86\_64                           5/6
53. Installing     : postgis91-utils-1.5.3-2.rhel6.x86\_64                     6/6
54. Installed:
55. postgis91.x86\_64 0:1.5.3-2.rhel6    postgis91-utils.x86\_64 0:1.5.3-2.rhel6
56. Dependency Installed:
57. geos.x86\_64 0:3.3.0-1.rhel6          perl-DBD-Pg.x86\_64 0:2.15.1-3.el6
58. perl-DBI.x86\_64 0:1.609-4.el6        proj.x86\_64 0:4.7.0-1.rhel6
59. Complete!
60. [root@server1 yum.repos.d]#

```
[root@server1 yum.repos.d]# yum install postgis91 postgis91-utils
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirror.us.leaseweb.net
 * extras: mirror.lug.udel.edu
 * updates: centos.mirror.choopa.net
Setting up Install Process
Resolving Dependencies
--> Running transaction check
---> Package postgis91.x86_64 0:1.5.3-2.rhel6 set to be updated
--> Processing Dependency: proj for package: postgis91-1.5.3-2.rhel6.x86_64
--> Processing Dependency: geos for package: postgis91-1.5.3-2.rhel6.x86_64
--> Processing Dependency: libgeos_c.so.1()(64bit) for package: postgis91-1.5.3-2.rhel6.x86_64
--> Processing Dependency: libproj.so.0()(64bit) for package: postgis91-1.5.3-2.rhel6.x86_64
---> Package postgis91-utils.x86_64 0:1.5.3-2.rhel6 set to be updated
--> Processing Dependency: perl-DBD-Pg for package: postgis91-utils-1.5.3-2.rhel6.x86_64
--> Running transaction check
---> Package geos.x86_64 0:3.3.0-1.rhel6 set to be updated
---> Package perl-DBD-Pg.x86_64 0:2.15.1-3.el6 set to be updated
--> Processing Dependency: perl(DBI) for package: perl-DBD-Pg-2.15.1-3.el6.x86_64
---> Package proj.x86_64 0:4.7.0-1.rhel6 set to be updated
--> Running transaction check
---> Package perl-DBI.x86_64 0:1.609-4.el6 set to be updated
--> Finished Dependency Resolution

Dependencies Resolved

================================================================================
 Package                Arch          Version               Repository     Size
================================================================================
Installing:
 postgis91              x86_64        1.5.3-2.rhel6         pgdg91        1.3 M
 postgis91-utils        x86_64        1.5.3-2.rhel6         pgdg91         21 k
Installing for dependencies:
 geos                   x86_64        3.3.0-1.rhel6         pgdg91        502 k
 perl-DBD-Pg            x86_64        2.15.1-3.el6          base          197 k
 perl-DBI               x86_64        1.609-4.el6           base          705 k
 proj                   x86_64        4.7.0-1.rhel6         pgdg91        157 k

Transaction Summary
================================================================================
Install       6 Package(s)
Upgrade       0 Package(s)

Total download size: 2.9 M
Installed size: 11 M
Is this ok [y/N]: y
Running rpm_check_debug
Running Transaction Test
Transaction Test Succeeded
Running Transaction
  Installing     : proj-4.7.0-1.rhel6.x86_64                                1/6
  Installing     : perl-DBI-1.609-4.el6.x86_64                              2/6
  Installing     : perl-DBD-Pg-2.15.1-3.el6.x86_64                          3/6
  Installing     : geos-3.3.0-1.rhel6.x86_64                                4/6
  Installing     : postgis91-1.5.3-2.rhel6.x86_64                           5/6
  Installing     : postgis91-utils-1.5.3-2.rhel6.x86_64                     6/6

Installed:
  postgis91.x86_64 0:1.5.3-2.rhel6    postgis91-utils.x86_64 0:1.5.3-2.rhel6

Dependency Installed:
  geos.x86_64 0:3.3.0-1.rhel6          perl-DBD-Pg.x86_64 0:2.15.1-3.el6
  perl-DBI.x86_64 0:1.609-4.el6        proj.x86_64 0:4.7.0-1.rhel6

Complete!
[root@server1 yum.repos.d]#
```

  
  
The required PostGIS sql files will be installed under /usr/pgsql-9.1/share/contrib/postgis-1.5  
  
Create a database.

1. -bash-4.1$ createdb pgisdb
2. Password:
3. -bash-4.1$

```
-bash-4.1$ createdb pgisdb
Password:
-bash-4.1$
```

  
  
Run the postgis.sql and spatial\_ref\_sys.sql files using below.

1. -bash-4.1$ psql -d pgisdb -f /usr/pgsql-9.1/share/contrib/postgis-1.5/postgis.sql

```
-bash-4.1$ psql -d pgisdb -f /usr/pgsql-9.1/share/contrib/postgis-1.5/postgis.sql
```

1. -bash-4.1$ psql -d pgisdb -f /usr/pgsql-9.1/share/contrib/postgis-1.5/spatial\_ref\_sys.sql

```
-bash-4.1$ psql -d pgisdb -f /usr/pgsql-9.1/share/contrib/postgis-1.5/spatial_ref_sys.sql
```

**12. Configuring Webmin to Manage PostegreSQL 9**

Due to the directory structure of PostgreSQL 9, you will need to make a few changes to the Webmin management interface it let Webmin know where the Postgre files are located.  
  
Under Servers>PostgreSQL Database Server
Click on Module Configuration.  
  
Make the following substitutions in the System Configuration Section:  
  
**1. Path to psql command:**
Original:

```
  /usr/bin/psql
```

Change to:

```
/usr/pgsql-9.1/bin/psql
```

**2. Command to start PostgreSQL**
Original:

1. if [ -r /etc/rc.d/init.d/rhdb ]; then /etc/rc.d/init.d/rhdb start; else /etc/rc.d/init.d/postgresql start; fi

```
if [ -r /etc/rc.d/init.d/rhdb ]; then /etc/rc.d/init.d/rhdb start; else /etc/rc.d/init.d/postgresql start; fi
```

Change to:

1. if [ -r /etc/rc.d/init.d/rhdb ]; then /etc/rc.d/init.d/rhdb start; else /etc/rc.d/init.d/postgresql-9.1 start; fi

```
if [ -r /etc/rc.d/init.d/rhdb ]; then /etc/rc.d/init.d/rhdb start; else /etc/rc.d/init.d/postgresql-9.1 start; fi
```

**3. Command to stop PostgreSQL** 
Original:

1. if [ -r /etc/rc.d/init.d/rhdb ]; then /etc/rc.d/init.d/rhdb stop; else /etc/rc.d/init.d/postgresql stop; fi

```
if [ -r /etc/rc.d/init.d/rhdb ]; then /etc/rc.d/init.d/rhdb stop; else /etc/rc.d/init.d/postgresql stop; fi
```

Change to:

1. if [ -r /etc/rc.d/init.d/rhdb ]; then /etc/rc.d/init.d/rhdb stop; else /etc/rc.d/init.d/postgresql-9.1 stop; fi

```
if [ -r /etc/rc.d/init.d/rhdb ]; then /etc/rc.d/init.d/rhdb stop; else /etc/rc.d/init.d/postgresql-9.1 stop; fi
```

**4. Command to initialize PostgreSQL**
Original:

1. if [ -r /etc/rc.d/init.d/rhdb ]; then /etc/rc.d/init.d/rhdb start; else /etc/rc.d/init.d/postgresql initdb ; /etc/rc.d/init.d/postgresql start; fi

```
if [ -r /etc/rc.d/init.d/rhdb ]; then /etc/rc.d/init.d/rhdb start; else /etc/rc.d/init.d/postgresql initdb ; /etc/rc.d/init.d/postgresql start; fi
```

Change to:

1. if [ -r /etc/rc.d/init.d/rhdb ]; then /etc/rc.d/init.d/rhdb start; else /etc/rc.d/init.d/postgresql-9.1 initdb ; /etc/rc.d/init.d/postgresql-9.1 start; fi

```
if [ -r /etc/rc.d/init.d/rhdb ]; then /etc/rc.d/init.d/rhdb start; else /etc/rc.d/init.d/postgresql-9.1 initdb ; /etc/rc.d/init.d/postgresql-9.1 start; fi
```

**5. Path to postmaster PID file**
Original:

```
/var/run/postmaster.pid
```

  
Change to:

```
/var/run/postmaster-9.1.pid
```

  
**6. Paths to host access config file**
Original:

1. /var/lib/pgsql/data/pg\_hba.conf

```
/var/lib/pgsql/data/pg_hba.conf
```

  
Change to:

1. /var/lib/pgsql/9.1/data/pg\_hba.conf

```
 /var/lib/pgsql/9.1/data/pg_hba.conf
```

  
**7. Default backup repository directory**
Original:

```
 /home/db_repository
```

  
Change to:

```
 /var/lib/pgsql/9.1/backups
```

  
Save the configuration.  
  
If you have not already initialized the database, do so now by clicking the initialize database button.  
  
Additional information and references:  
  
[Postgresql.Org/](http://www.postgresql.org/)   
  
[PostgreSQL 9.1 Documentation](http://www.postgresql.org/docs/9.1/static/release-9-1.html) 
  
  

![2544b95ef2e8712a60e710cb3bfa65fb.png](davidghedini-com--install-postgresql-9-on-centos/2544b95ef2e8712a60e710cb3bfa65fb.png)

  
  

![ec521c7397fca73b30772d1ae0c02973.png](davidghedini-com--install-postgresql-9-on-centos/ec521c7397fca73b30772d1ae0c02973.png)

Posted at [07:02AM Mar 01, 2011](http://www.davidghedini.com/pg/entry/install_postgresql_9_on_centos) 
by David in PostgreSQL  | 
[Comments[8]](http://www.davidghedini.com/pg/entry/install_postgresql_9_on_centos#comments)
| Tags: [centos](http://www.davidghedini.com/pg/tags/centos "$tag.count")  [postgis](http://www.davidghedini.com/pg/tags/postgis "$tag.count")  [postgresql](http://www.davidghedini.com/pg/tags/postgresql "$tag.count")  | Export to:
