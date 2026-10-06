---
url: "https://www.digitalocean.com/community/tutorials/digitalocean-backups-and-snapshots-explained"
captured_at: "2015-05-01T13:29:41-03:00"
title: "DigitalOcean Backups and Snapshots Explained | DigitalOcean"
domain: "digitalocean-com"
---

# DigitalOcean Backups and Snapshots Explained

Tags:
[DigitalOcean](https://www.digitalocean.com/community/tags/digitalocean?type=tutorials), [Backups](https://www.digitalocean.com/community/tags/backups?type=tutorials)

### About Backups

Backups are an important part of any secure system. DigitalOcean offers two main backup types, snapshots and backups, that can be used to not only save and restore important data in case of a server issues, but also to scale servers or duplicate helpful configurations.

Please note that automated backups running on a server with an active database can result in an incomplete backup of your database. If you are relying on the automated backups to back up a database server, we highly suggest that you use a tool to periodically export your database, such as mysqldump or pg\_dump. The exported file can be safely backed up and can be used to perform a database restore.

## Backups vs. Snapshots

DigitalOcean users have the option of backup and snapshot features. The main difference between the two is that snapshots can be generated manually and can be enabled at any time, while backups are run automatically weekly, and must be enabled during the droplet's creation.

Additionally, *the server shuts down during snapshots, but stays powered on during backups, which happen in the background*.

Once the files are saved, both the snapshots and backups are stored on hardware separate from the droplet resources.

## Snapshots and Backups Pricing

The pricing for backups is 20% of the cost of the virtual server. So if you want to enable backups for a $5/mo virtual server, the cost for backups will be $1/mo.

The 20% cost for backups assumes at least four successful backups per month. If for any reason one of those backups should fail, you will not be charged for that backup. For example, if 3 out of 4 backups are successful, your backups will cost 15% the cost of your server that month. You will not be charged beyond the fourth backup in a single month. For more information about DigitalOcean backups, [click here](https://www.digitalocean.com/community/tutorials/understanding-digitalocean-droplet-backups).

The price for snapshots will be $0.02 per GB of snapshot storage per month.

## Snapshot Uses

**Scaling:**Snapshots can provide an easy way to scale out a system: you can take a snapshot of a current server and spin up a new droplet from the snapshot. As soon as the process completes, you will have two identical servers to bolster your setup.

**Occasional Usage:** Snapshots can also provide a way to use droplets for a limited time without having to pay for hours when the server is not in use. Should you only need to use a server for a certain time every so often, you can take a snapshot of your current configuration, delete the droplet, and spin the system back up as soon as you need it once again—the image will remain in your account. In such a way, you only have to pay for the amount of time that you will actually use the droplet each month.

**Backups:** While automated backups make sure that is always a version of your system available in case of trouble, snapshots have the added benefit of being possible at any time. A snapshot could be taken prior to making any drastic changes to a server configuration, so that, should the changes be unsuccessful, you will have a version to revert back to.
