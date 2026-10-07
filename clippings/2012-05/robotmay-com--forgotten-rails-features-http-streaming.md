---
url: "http://robotmay.com/post/24054884390/forgotten-rails-features-http-streaming"
captured_at: "2012-05-30T23:57:52-03:00"
title: "Forgotten Rails features: HTTP Streaming"
domain: "robotmay-com"
---

# Forgotten Rails features: HTTP Streaming

The Ruby on Rails community is often fast changing; particularly when it comes to features or libraries. This series of posts will look at some of the components of Rails which aren’t talked about much any more. Especially those for which the existing blog posts and screencasts are out of date.

### HTTP Streaming/Chunking

I’d be willing to bet that the vast majority of Rails developers have never bothered with the HTTP Streaming support [added in Rails 3.1](http://weblog.rubyonrails.org/2011/4/18/why-http-streaming). It’s a fairly niche feature and there are a variety of problems (which I’ll explain below) which may cause you a bit of suffering should you try to explore it.

HTTP streaming sends the response to the browser in chunks rather than in one go; in Rails this is implemented by sending everything before the `yield` in your layout first, then sending the rest of the page when the specific view (e.g. “posts/index.html.erb”) finishes rendering. It’s not for every request, but it can significantly improve the experience for your end user by making the page *appear* to load faster.

[The official blog post](http://weblog.rubyonrails.org/2011/4/18/why-http-streaming/) explains the benefits of HTTP streaming quite neatly:

> Streaming doesn’t cut latency, neither it cuts the time a dynamic response needs to be generated. But since the application sends content right away instead of waiting for the whole response to be rendered, the client is able to request assets sooner. In particular, if you flush the head of an HTML document CSS and JavaScript files are going to be fetched in parallel, while the server works on generating content. The consequence is that pages load faster.

#### Changes from existing examples

If you search for information on streaming support in Rails you’ll no doubt come across [the relevant Railscast](http://railscasts.com/episodes/266-http-streaming). This is a great intro to using streaming in your application but there are a couple of changes you’ll need to make:

There is no longer a method of `stream`, seen in this example:

```ruby
class ProjectsController < ApplicationController
  stream

  def index
    # rest of controller code
  end
end
```

Instead you’ll need to pass `stream: true` to your render call. The Railscast illustrates this using the following example:

```ruby
def index
  @projects = Project.all
  render :stream => true
end
```

That will still work fine, however if you’re using `respond_to` & `respond_with`, you can do the following:

```ruby
class ProjectsController < ApplicationController
  respond_to :html

  def index
    @projects = Project.scoped
    respond_with @projects, stream: true
  end
end
```

Also note that you’ll want to use ActiveRecord’s delayed query execution as much as possible (in this case using Project.scoped instead of Project.all) as this will mean that your header will return far faster as the queries are performed during view rendering.

### Problems you’ll quite likely encounter:

#### NewRelic

[NewRelic](http://newrelic.com/), that beau of application monitoring, is going to ruin your day. This was causing me no end of trouble until I stumbled across [an excellent blog post from Icelab](http://icelab.com.au/articles/new-relic-heroku-and-rails-streaming-responses/). The gist being that NewRelic’s end user monitoring system is injecting JavaScript in a variety of places and will rain all over your parade; it causes the response to block, rendering streaming pointless. Icelab recommend the following tweak:

```yaml
browser_monitoring:
  auto_instrument: false
```

#### Action Caching

I forgot to screenshot what happens when you do this; just don’t do it. It prints what I believe to be the chunk byte counts (I’d really like to know if I’m right or wrong here) onto the page. Which will then be cached. *Lovely*.

#### HAML

[HAML doesn’t work with HTTP streaming](https://github.com/haml/haml/issues/436) as of today (2012-05-30). I personally use [Slim](http://slim-lang.com/) but ERB will work fine too.

#### content\_for

`content_for` won’t work, as your layout will already have been sent to the browser before the view. Instead you can use `provide`, [as demonstrated in the Rails Streaming API docs](http://api.rubyonrails.org/classes/ActionController/Streaming.html#label-Communication+between+layout+and+template).

### Other things to note

If you decide to use streaming in your application, it’s time to go against everything you’ve been told in the past few years: put your JavaScript include tags in your `head` tag (not at the bottom just inside the `body` tag) so that they’re loaded by the browser while the rest of the chunks fly in.

As the RailsCast pointed out, you’ll be wanting to use [Unicorn](http://unicorn.bogomips.org/) (or another server that supports streaming). For conciseness, and so that hopefully others can get up and running quickly, here is my config file assembled from various places (though most particularly [railsonfire](http://blog.railsonfire.com/2012/05/06/Unicorn-on-Heroku.html)) which I use for [Days Out Near Me](http://daysoutnearme.com) on Heroku:

```ruby
worker_processes 3
timeout 30
preload_app true
port = ENV["PORT"].to_i
listen port, tcp_nopush: false

before_fork do |server, worker|
  if defined?(ActiveRecord::Base)
    ActiveRecord::Base.connection.disconnect!
    Rails.logger.info('Disconnected from ActiveRecord')
  end
  
  sleep 1
end

after_fork do |server, worker|
  if defined?(ActiveRecord::Base)
    ActiveRecord::Base.establish_connection
    Rails.logger.info('Connected to ActiveRecord')
  end
  
  if defined?(ActiveSupport::Cache::DalliStore) && Rails.cache.is_a?(ActiveSupport::Cache::DalliStore)
    # Reset Rails's object cache
    # Only works with DalliStore
    Rails.cache.reset

    # Reset Rails's session store
    # If you know a cleaner way to find the session store instance, please let me know
    ObjectSpace.each_object(ActionDispatch::Session::DalliStore) { |obj| obj.reset }
  end
end
```

Note the references to [Dalli](https://github.com/mperham/dalli) which I lifted from [a recent commit](https://github.com/mdesjardins/dalli/commit/ffbbbbb18c45f4deb1b6e8b4fb7c2e1595093b60). I’ll hopefully go into more depth with how Unicorn has improved the application performance in the future.

### Example use case

I recently switched how [Days Out Near Me](http://daysoutnearme.com) calculates the nearest places to you from a straightforward geodistance to using a travel time API (more on this soon). This resulted in a lot of performance tweaking to get the search results (e.g. [searching for days out near Liverpool](http://daysoutnearme.com/hubs/city/cardiffl)) to continue displaying at a reasonable speed (as it now uses up to 3 different services in the action). The adjustments are far from complete but the first step was to use HTTP streaming to improve how fast the page feels. Streaming is only used on the homepage and the search results page currently, as those most benefit from it. However I can see it being useful to roll out on individual place & event pages as those are often the entry points to the site for many users.

### Feedback

I’d love any feedback or other suggestions/problems you’ve come across while using HTTP streaming.
And if anyone knows of a better theme for programming on Tumblr then I’d be very interested.
