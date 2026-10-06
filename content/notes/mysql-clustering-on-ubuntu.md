---
title: "MySQL Clustering on Ubuntu"
date: '2012-01-24T17:07:40-03:00'
category: webclip
summary: 'The post walks through setting up a three-machine MySQL Cluster on Ubuntu, configuring the management node and storage nodes, testing replication with a sample table, and converting existing tables to NDB.'
tags: ["mysql", "ubuntu", "clustering", "ndbcluster"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "MySQL Clustering on Ubuntu « Bieg"
    url: "http://bieg.wordpress.com/2008/08/03/mysql-clustering-ubuntu/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-01/bieg-wordpress-com--mysql-clustering-on-ubuntu.md"
    kind: repo
---

The post explains how to set up MySQL Cluster on a fresh Ubuntu installation with three machines: one management node and two storage nodes. It uses MySQL server from apt, edits the cluster configuration files on the management and storage machines, and starts the services needed for the cluster to accept connections.

## Reading notes

- Use one machine as the management node and two as storage nodes.
- Install MySQL server on all three machines with apt-get install mysql-server.
- Create /etc/mysql/ndb_mgmd.cnf on the management node with the cluster settings and the IP addresses for the manager and both storage nodes.
- On each storage node, create /var/lib/mysql-cluster/backup and change ownership of /var/lib/mysql-cluster to mysql:mysql.
- Edit /etc/mysql/my.cnf on each storage node, add ndbcluster under [mysqld], and set ndb-connectstring to the management node IP.
- Start the management node with /etc/init.d/mysql-ndb-mgm restart, then check the cluster with ndb_mgm and show;.
- Start MySQL and the NDB data node service on both storage nodes with /etc/init.d/mysql restart and /etc/init.d/mysql-ndb restart.
- Test the cluster by creating the same database on both data nodes, then creating a table with engine=ndbcluster on one node and checking that the table and row appear on the other node.
- To move an existing table into the cluster, run alter table my_test_table engine=ndbcluster; on each table.
