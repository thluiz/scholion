---
url: "http://blog.bigbinary.com/2016/01/25/caching-in-development-environment-in-rails5.html"
captured_at: "2016-02-07T22:38:28-03:00"
title: "Caching in development environment in Rails 5 | BigBinary Blog"
domain: "blog-bigbinary-com"
---

# Caching in development environment in Rails 5

January 25, 2016 -
Mohit Natoo

*This blog is part of our [Rails 5 series](http://blog.bigbinary.com/categories/Rails%205).*

In Rails 4 if I’m doing work related to caching then first I need
to turn caching “on” by opening file `config/environments/development.rb`
and changing following line.

```
configaction_controllerperform_caching  false
```

After changing the value from `false` to `true`, I need to restart the
server.

This means that if I am testing caching behavior locally then every time I turn
caching “on” or “off”
I need to restart the server.

### New command to create development cache in Rails 5

Rails 5 has introduced a new command to
create development cache
and help us test how caching behaves in development mode.
Here is the [issue](https://github.com/rails/rails/issues/18875)
and
here is the [pull request](https://github.com/rails/rails/pull/20961).

```
$ rails dev:cache
Development mode is now being cached.
```

Execution of the above command creates file `caching-dev.txt` in `tmp` directory.

### How does it work?

In Rails 5 when a brand new Rails app is created then
`config/environments/development.rb` file will have the following
snippet of code.

```
 Rails'tmp/caching-dev.txt'exist?
  configaction_controllerperform_caching  
  configstatic_cache_control  "public, max-age=172800"
  configcache_store  :mem_cache_store

  configaction_controllerperform_caching  false
  configcache_store  :null_store
```

In the above code we are checking if the file `tmp/caching-dev.txt`
is present and then use `:mem_cache_store` to enable caching only if the file is found.

Also, here is a snippet from the
[dev cache source code](http://github.com/rails/rails/blob/master/railties/lib/rails/commands/dev_cache.rb).

```
 dev_cache
   exist? 'tmp/caching-dev.txt'
    delete 'tmp/caching-dev.txt'
     'Development mode is no longer being cached.'
  
    FileUtilstouch 'tmp/caching-dev.txt'
     'Development mode is now being cached.'
  

  FileUtilstouch 'tmp/restart.txt'
```

### What is the advantage

The advantage is that we do not need to restart the
server manually if we want to turn caching “on” or “off”.
It is internally taken care by the `dev_cache` method
that is executed when `rails dev:cache` is executed.
You can see in the source code that `tmp/restart.txt` is being **touched**.

Please note that **this feature is not supported** by unicorn, thin and
webrick. My guess is that DHH wants this feature because his team uses
[pow](http://pow.cx/) and pow restarts when `tmp/restart.txt` is touched.
He also created an issue for
[spring to watch tmp/restart.txt](https://github.com/rails/rails/issues/18874)
long time
back.

### Disabling development cache

Execute the same command that was used to enable caching. If caching was
previously enabled then it will be turned “off” now.

```
$ rails dev:cache
Development mode is no longer being cached.
```
