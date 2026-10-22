---
url: "https://thewebdev.info/2020/08/13/node-js-best-practices%e2%80%8a-%e2%80%8acaching-and-rest/"
captured_at: "2020-09-09T18:03:48-03:00"
title: "Node.js Best Practices — Caching and REST - The Web Dev"
domain: "thewebdev-info"
---

# Node.js Best Practices — Caching and REST

Spread the love

Like any kind of apps, JavaScript apps also have to be written well.

Otherwise, we run into all kinds of issues later on.

In this article, we’ll look at some best practices we should follow when writing Node apps.

### Enabling Caching with Redis

We can enable caching with Redis to speed up our Express app.

To do this, we can install Redis by running:

```
apt update
apt install redis-server
```

Then in `/etc/redis/redis.conf` we change:

```
supervised no
```

to:

```
supervised systemd
```

Then Redis will run under Systemd.

Then we restart Redis to make the change take effect:

```
systemctl restart redis
systemctl status redis
```

Then we install the redis NPM module by running:

```
npm i redis
```

Then we can use it by writing:

```
const express = require('express')
const app = express()
const redis = require('redis')
​
const redisClient = redis.createClient(6379)
​
async function getData(req, res, next) {
  try {
    //...
    redisClient.setex(id, 3600, JSON.stringify(data))
    res.status(200).send(data)
  } catch (err) {
    console.error(err)
    res.status(500)
  }
}
​
function cache (req, res, next) {
  const { id } = req.params
​
  redisClient.get(id, (err, data) => {
    if (err) {
      return res.status(500).send(err)
    }
    if (data !== null) {
      return res.status(200).send(data)
    }
    next()
  })
}
​
​
app.get('/data/:id', cache, getData)
app.listen(3000, () => console.log(`Server running on Port ${port}`))
```

We use the Redis client for Node apps to create the Redis client.

Then we create the `cache` middleware that gets the data from the Redis cache if it exists.

We send the response data from Redis if it exists.

If it’s not, then we call our `getData` route middleware to get the data from the database.

This is done with the `redisClient.setex` method to set the data.

### Enable VM/Server-Wide Monitoring and Logging

We can enable server or virtual machine monitoring and logging with various tools.

This way, we can watch for any issues that arise from the app.

### The Hidden Powers of NODE\_ENV

`NODE_ENV` can make a big difference in the performance of our Node app.

If we set it to `production` , caching is enabled so that data will be cached.

We don’t want that in development since we always want to see the latest data.

Views are cached in production but not in development node.

We can run it with the given `NODE_ENV` with:

```
NODE_ENV=<environment> node server.js
```

where `server.js` is the entry point of our app.

With production mode on, Express apps aren’t busy processing Pug templates all the time.

The CPU is free to do other things because of caching.

We can set the `NODE_ENV` by running:

```
export NODE_ENV=production
```

in Linux and Mac OS.

In Windows, we can run:

```
SET NODE_ENV=production
```

We can run:

```
NODE_ENV=production node my-app.js
```

in all platforms.

### Use HTTP Methods and API Routes

We should use HTTP methods and API routes that matches REST conventions.

For example, we can write:

- `POST /article` or `PUT /article:/id` to create a new article
- `GET /article` to retrieve a list of article
- `GET /article/:id` to retrieve an article
- `PATCH /article/:id` to modify an existing `articlerecord`
- `DELETE /article/:id` to remove an article

If we get by ID, we have the ID parameter at the end.

### Conclusion

Caching and setting NODE\_ENV to `production` speed up our app.

REST conventions are useful for keeping our APIs consistent.
