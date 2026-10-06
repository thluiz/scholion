---
url: "http://bieg.wordpress.com/2008/08/03/mysql-clustering-ubuntu/"
captured_at: "2012-01-24T17:07:40-03:00"
title: "MySQL Clustering on Ubuntu « Bieg"
domain: "bieg-wordpress-com"
---

### MySQL Clustering on Ubuntu

Posted August 3, 2008  
Filed under: [Clustering](http://bieg.wordpress.com/category/clustering/ "View all posts in Clustering"), [MySQL](http://bieg.wordpress.com/category/mysql/ "View all posts in MySQL"), [Uncategorized](http://bieg.wordpress.com/category/uncategorized/ "View all posts in Uncategorized") |

I spent some time getting MySQL clustering working with Ubuntu after reading a guide on Howto Forge. The guide however went into the details of compiling and installing MySQL from source so I’m creating this to show the steps needed to get it set up on a fresh Ubuntu installation.

For a correct setup you will need 3 machines. The first machine will serve as the management node, and the other two will be storage nodes.

At the time of writing, the current stable version of Ubuntu is 8.04.1 and the MySQL version that is installed is 5.0.51

During the configuration I log onto the machines and use the command

```
sudo su -
```

to gain permanent root access and saving myself from having to type sudo in front of every command. Use your own discretion.

### Installing MySQL

Using apt this is straight forward. Just type the following command on all three machines to install MySQL server.

```
apt-get install mysql-server
```

Once asked to, set the root password to the MySQL database. You’ll need to remember this one. Once MySQL server is installed we’ll proceed to configure the management node.

### Configuring the Management Node

Create and edit the file **/etc/mysql/ndb\_mgmd.cnf**. Copy and paste the text bellow changing the ip addresses to match your setup as necessary.

```
[NDBD DEFAULT]
NoOfReplicas=2
DataMemory=80M    # How much memory to allocate for data storage
IndexMemory=18M   # How much memory to allocate for index storage
# For DataMemory and IndexMemory, we have used the
# default values. Since the "world" database takes up
# only about 500KB, this should be more than enough for
# this example Cluster setup.
[MYSQLD DEFAULT]
[NDB_MGMD DEFAULT]
[TCP DEFAULT]
# Section for the cluster management node
[NDB_MGMD]
# IP address of the management node (this system)
HostName=192.168.1.5

# Section for the storage nodes
[NDBD]
# IP address of the first storage node
HostName=192.168.1.6
DataDir=/var/lib/mysql-cluster
BackupDataDir=/var/lib/mysql-cluster/backup
DataMemory=512M
[NDBD]
# IP address of the second storage node
HostName=192.168.1.7
DataDir=/var/lib/mysql-cluster
BackupDataDir=/var/lib/mysql-cluster/backup
DataMemory=512M

# one [MYSQLD] per storage node
[MYSQLD]
[MYSQLD]
```

### Configuring the Storage Nodes

As you can see in the file we created in the previous step, the cluster will be using **/var/lib/mysql-cluster** on the storage machines. This path is created when you install MySQL server but they are owned by root. We want to create the backup directory and change ownership to mysql.

```
mkdir /var/lib/mysql-cluster/backup
```

```
chown -R mysql:mysql /var/lib/mysql-cluster
```

Now we’ll need to edit the MySQL configuration so that the storage nodes will communicate with the Management Node.

Edit **/etc/mysql/my.cnf**

Search for **[mysqld]** and add the following.

```
[mysqld]
ndbcluster
# IP address of the cluster management node
ndb-connectstring=192.168.1.5
```

Then scroll down to the bottom until you see **[MYSQL\_CLUSTER]**. Uncomment the line and edit so it looks like

```
[MYSQL_CLUSTER]
ndb-connectstring=192.168.1.5
```

The reason the connect string it found twice in the mysql file is because one is used by mysql server, and the other is used by the ndb data node app. Save the changes to the file.

Make sure you complete the changes on both data nodes.

### Start the Management Node

Start the Management Node using

```
/etc/init.d/mysql-ndb-mgm restart
```

The process shouldn’t be running but using restart doesnt hurt. Once it is started we can access the management console using the command **ndb\_mgm**. At the prompt type **show;** and you will see

```
ndb_mgm> show;
Connected to Management Server at: localhost:1186
Cluster Configuration
---------------------
[ndbd(NDB)]    2 node(s)
id=2 (not connected, accepting connect from 192.168.1.6)
id=3 (not connected, accepting connect from 192.168.1.7)

[ndb_mgmd(MGM)]    1 node(s)
id=1    @192.168.1.5  (Version: 5.0.51)

[mysqld(API)]    2 node(s)
id=4 (not connected, accepting connect from any host)
id=5 (not connected, accepting connect from any host)
```

As you can see the management node is waiting for connections from the data nodes.

### Start the Data Nodes

On the data nodes, issue the commands

```
/etc/init.d/mysql restart
/etc/init.d/mysql-ndb restart
```

Go back to the management node, type show; again, and now you should see something similar to

```
id=2    @192.168.1.6  (Version: 5.0.51, starting, Nodegroup: 0)
id=3    @192.168.1.7  (Version: 5.0.51, starting, Nodegroup: 0)
```

Once they have started properly, the show command should display

```
ndb_mgm> show;
Cluster Configuration
---------------------
[ndbd(NDB)]    2 node(s)
id=2    @192.168.1.6  (Version: 5.0.51, Nodegroup: 0, Master)
id=3    @192.168.1.7  (Version: 5.0.51, Nodegroup: 0)
[ndb_mgmd(MGM)]    1 node(s)
id=1    @192.168.1.5  (Version: 5.0.51)
[mysqld(API)]    2 node(s)
id=4    @192.168.1.7  (Version: 5.0.51)
id=5    @192.168.1.6  (Version: 5.0.51)
```

Congratulations, your cluster is now setup.

### Testing the cluster

Issue the following on both data nodes to create the test database. Since clustering is done on a table basis in MySQL we have to create the database manually on both data nodes.

```
$> mysql -u root -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 5.0.51a-3ubuntu5.1 (Ubuntu)

Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

mysql> create database clustertest;
Query OK, 1 row affected (0.00 sec)
```

Once this i done, on ONE of the data nodes, create a test table and add an entry.

```
mysql> use clustertest;
Database changed
mysql> create table test (i int) engine=ndbcluster;
Query OK, 0 rows affected (0.71 sec)

mysql> insert into test values (1);
Query OK, 1 row affected (0.05 sec)

mysql> select * from test;
+------+
| i    |
+------+
|    1 |
+------+
1 row in set (0.03 sec)
```

We’ve just created a table test, added a value to this table and made sure that the table contains one entry. Note that **engine=ndbcluster** must be used to let MySQL know that this table should be clustered among the data nodes. Let’s make sure that the table is infact created on the other data node, and contains one entry.

```
mysql> use clustertest;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+-----------------------+
| Tables_in_clustertest |
+-----------------------+
| test                  |
+-----------------------+
1 row in set (0.01 sec)

mysql> select * from test;
+------+
| i    |
+------+
|    1 |
+------+
1 row in set (0.04 sec)
```

As you can see, the cluster is working.

### Moving an existing database to the cluster

Now that we have the cluster working, we can easily change an existing database to be clustered. All you need to do is run the following command on each of the tables.

```
alter table my_test_table engine=ndbcluster;
```

The table, and all it’s data will be copied to the datanodes and you can now access/change then through any nodes in the cluster. Very simple.
