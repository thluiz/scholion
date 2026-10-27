---
url: "http://robotmay.com/post/23161612605/everyone-should-be-using-low-level-caching"
captured_at: "2012-05-16T20:55:25-03:00"
title: "Everyone should be using low level caching in Rails | robotmay"
domain: "robotmay-com"
---

Everyone should be using low level caching in Rails

Low level caching is very easy to get started with in Rails 3, but it seems to be missing from [the official guides](http://guides.rubyonrails.org/). I personally use it all the time to help reduce the number of queries or API calls I’m making. [Heroku has a pretty good explanation](https://devcenter.heroku.com/articles/caching-strategies#low_level_caching) which, if you’re so far unfamiliar with low-level caching, is a good place to start.

Why should you use low level caching, and what should you use it for? Maybe you have some data which you need regularly over multiple pages, e.g. a list of categories for your blog. You might want to display them on every page but they’re not going to need to be entirely up to date for every request. You could stick this in controllers/application\_controller.rb:

class ApplicationController < ActionController::Base

protect\_from\_forgery

before\_filter do

@categories = Rails.cache.fetch("global/categories", expires\_in: 10.minutes) do

Category.where("posts\_count > 0").all

end

end

end

[view raw](https://gist.github.com/raw/2709589/eb255408696082b290474123042613e818b38a03/application_controller.rb)
[application\_controller.rb](https://gist.github.com/2709589#file_application_controller.rb)
[This Gist](https://gist.github.com/2709589) brought to you by [GitHub](http://github.com/).

If you haven’t used this style of caching before, note that I’m calling `.all` on the Category query. In Rails 3 ActiveRecord now uses lazy loading; it doesn’t perform the query until you try to use it. This is great for fragment caching in your views as it will prevent that query being called if a fragment cache already exists. However, if you’re using low level caching you’ll want to perform that query immediately so that the results, rather than just the query object you’ve built, are stored in the cache.

The mainstay of low level caching in Rails is [`Rails.cache.fetch`](http://api.rubyonrails.org/classes/ActiveSupport/Cache/Store.html#method-i-fetch). There’s something you need to know before you end up in a spiral of frustration; by default **this will cache in your development environment**. To remedy this, add this line to your config/environments/development.rb:

`config.cache_store = :null_store`

`Rails.cache.fetch` takes 3 arguments; the cache key, an options hash, and a block. It first tries to read a valid cache record based on the key; if that key exists and hasn’t expired it will return the value from the cache. If it can’t find a valid record it instead takes the return value from the block and stores it in the cache with your specified key. It’s well worth [reading the API docs for this method](http://api.rubyonrails.org/classes/ActiveSupport/Cache/Store.html#method-i-fetch), as it explains all the options you can pass to it.

I use low level caching most for API calls. On [Days Out Near Me](http://daysoutnearme.com/) I use the [Flickr API](http://www.flickr.com/services/api/) to find photographs of places. To do this I’m using the [Flickraw gem](http://hanklords.github.com/flickraw/):

class Place < ActiveRecord::Base

def flickr\_place

flickr = FlickRaw::Flickr.new

@flickr\_place ||= Rails.cache.fetch("places/#{self.id}-#{self.updated\_at}/flickr/place\_id", expires\_in: 7.days) do

unless self.latitude.blank? || self.longitude.blank?

begin

places = flickr.places.findByLatLon(lat: self.latitude, lon: self.longitude)

if places.blank?

nil

else

places.first

end

rescue Exception => e

logger.info "Exception occurred fetching Flickr place ID: #{e.to\_s}"

nil

end

end

end

end

end

[view raw](https://gist.github.com/raw/2709589/325aa581d89d515279d41dac9dbdb027297b836b/place.rb)
[place.rb](https://gist.github.com/2709589#file_place.rb)
[This Gist](https://gist.github.com/2709589) brought to you by [GitHub](http://github.com/).

This searches for a Flickr place based on the latitude & longitude of the one in my database. If it finds any matching places it returns the first entry, as that’s most likely to be the correct one. Unless we’re dealing with [a moving castle](https://en.wikipedia.org/wiki/Howl%27s_Moving_Castle) then it’s pretty safe to say that this place is going to be correct for quite a while, so it’s being cached for 7 days. It could however change if we update our record, or if someone adds it as a new place on Flickr where it was previously missing. By using `self.updated_at` inside the cache key we ensure that the cache is automatically invalidated if we update the place (which could include new co-ordinates).

Caching works best in layers. This is [nicely illustrated by 37signals](http://37signals.com/svn/posts/3112-how-basecamp-next-got-to-be-so-damn-fast-without-using-much-client-side-ui); don’t just use one type of caching, but instead layer one on top of another. You’ll end up with the same data cached in multiple places, but when the cache expires you won’t be hit with a totally uncached page load. Some of the pages of [Days Out Near Me](http://daysoutnearme.com/) would have pretty horrific response rates if I wasn’t using a variety of tricks to reduce how much time it spends in the database and API calls. I’ll be posting a few more of these tweaks in the near future.

**Edit:** This article makes the assumption that you’re using memcached or an equivalent (i.e. Redis) for your cache store. I’d highly recommend using the [Dalli gem](https://github.com/mperham/dalli) with memcached. [Thanks to wavesplash](http://news.ycombinator.com/item?id=3981917) for pointing out that I’d missed this section out.

*As this is essentially my first blog post, I would be very grateful for any critique or tips you have.*
