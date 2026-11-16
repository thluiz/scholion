---
url: "https://gist.github.com/henrik/c70e32544e09c1a79841"
captured_at: "2026-11-16T03:04:16+00:00"
title: "Deploying Elixir's Phoenix Framework on Dokku."
domain: "gist-github-com"
---

Deploying Elixir's Phoenix Framework on Dokku.

Worked 2015-09-08 for Phoenix 1.0.1 on Dokku 0.3.25.

These instructions assume you've set up Dokku. If not, go find a tutorial for that part. [My notes for setting it up on Digital Ocean.](https://gist.github.com/henrik/26bb73091712aa42abf2)

## On your local machine, in the app's repo

[](#on-your-local-machine-in-the-apps-repo)

Create a Dokku app:

```
$ ssh dokku apps:create my_app_name
```

Make it support multiple buildpacks:

```
$ ssh dokku config:set my_app_name BUILDPACK_URL=https://github.com/ddollar/heroku-buildpack-multi.git
```

List the two buildpacks you need:

```
$ echo "https://github.com/HashNuke/heroku-buildpack-elixir.git" >> .buildpacks
$ echo "https://github.com/gjaldon/heroku-buildpack-phoenix-static.git" >> .buildpacks
$ cat .buildpacks
https://github.com/HashNuke/heroku-buildpack-elixir.git
https://github.com/gjaldon/heroku-buildpack-phoenix-static.git
```

For Phoenix 1.1, you may need to [configure the static buildpack](https://github.com/gjaldon/heroku-buildpack-phoenix-static#configuration) to use node 5+:

```
echo node_version=5.3.0 > phoenix_static_buildpack.config
```

If you want to lock down the versions or Erlang and/or Elixir, you can [configure the Elixir buildpack](https://github.com/HashNuke/heroku-buildpack-elixir#configuration).

Get rid of a locale-related warning ("warning: the VM is running with native name encoding of latin1 which may cause Elixir to malfunction as it expects utf8. Please ensure your locale is set to UTF-8 (which can be verified by running "locale" in your shell)"):

```
$ ssh dokku config:set my_app_name LC_ALL=en_US.utf8
```

Put your `SECRET_KEY_BASE` in Dokku config:

```
# Change these values as appropriate…
$ ssh dokku config:set my_app_name SECRET_KEY_BASE=the_value_in_my_prod_secret_file
```

In `config/prod.secret.exs`, read from that config (replacing the old hard-coded value):

```
secret_key_base: System.get_env("SECRET_KEY_BASE")
```

Set the domain/host of your site in the same way:

```
# Change these values as appropriate…
$ ssh dokku config:set my_app_name HOSTNAME=my_hostname.example.com
```

In `prod.exs`, read from that config (replacing "example.com"):

```
url: [host: System.get_env("HOSTNAME"), port: 80]
```

If you're using a database, read that from config as well, like you did above.

```
# This varies depending on what you use for DBs in Dokku.
$ ssh dokku psql:create my_app_name

config :hello_phoenix, HelloPhoenix.Repo,
  adapter: Ecto.Adapters.Postgres,
  url: System.get_env("DATABASE_URL"),
  pool_size: 20
```

In `.gitignore`, comment this out:

```
#/config/prod.secret.exs
```

Now your secret-less `prod.secret.exs` can be committed and deployed.

So, commit! Push to Dokku! Done:

```
git commit -am "All done"
git remote add dokku dokku@example.com:my_app_name
git push dokku
```

### Sources

[](#sources)

*   [http://www.phoenixframework.org/docs/heroku](http://www.phoenixframework.org/docs/heroku)
*   [http://hady.svbtle.com/setting-up-elixir-on-digitalocean](http://hady.svbtle.com/setting-up-elixir-on-digitalocean)
*   [http://wsmoak.net/2015/07/05/phoenix-on-heroku.html](http://wsmoak.net/2015/07/05/phoenix-on-heroku.html)
*   [http://snltranscripts.jt.org/99/99adillon.phtml](http://snltranscripts.jt.org/99/99adillon.phtml)
