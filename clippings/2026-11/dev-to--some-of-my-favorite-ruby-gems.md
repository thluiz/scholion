---
url: "https://dev.to/justalever/some-of-my-favorite-ruby-gems-3ji0"
captured_at: "2026-11-16T19:21:11+00:00"
title: "Some Of My Favorite Ruby Gems"
domain: "dev-to"
---

There are thousands of Ruby gems out in the wild. I use many on almost every Ruby on Rails project I create. This is an impromptu list of some of my favorite Ruby gems I recommend you check out if you haven’t yet. I would love to hear some of your favorites. Share some in the comments!

### [](#devise)[Devise](https://github.com/plataformatec/devise)

Without a doubt one of the best solutions for authentication within Ruby on Rails. It’s extendable, flexible, and easy to get up and running. I use this in every project.

### [](#cancancan)[CanCanCan](https://github.com/CanCanCommunity/cancancan)

Need permission amongst your userbase? CanCanCan makes it a breeze to add custom abilities and roles.

### [](#chartkick)[Chartkick](https://chartkick.com/)

Need visual analytics? Chartkick makes it extremely easy to extend your existing app to include some charts. It works with Rails 6 via webpacker or Rails 5 using sprockets.

### [](#annotate)[Annotate](https://github.com/ctran/annotate_models)

As your ActiveRecord models gain database columns this gem appends comments within your model files directly to help document the schema during migrations. It’s a great way to not have to hunt for fields that may or may not exist on a given table in the database or via the `schema.rb` file that gets generated during active record migrations.

### [](#friendlyid)[FriendlyID](https://github.com/norman/friendly_id/)

By default Ruby on Rails will create dynamic URLs to records using its corresponding ID. While this works extremely well, it’s not always easy to remember or great for SEO. FriendlyID lets you create pretty URLs and work with human-friendly strings as if they were numeric ids.

### [](#metatags)[MetaTags](https://dev.to/scottw/rails-meta-tags-3h99)

Dynamically and easily insert meta information to your Ruby on Rails app that makes SEO so much less of a chore. You can define default values, dynamic values, social media values and more in a view method. This is a time-saver you shouldn’t ignore in a production app if you’re looking to grow traffic organically.

### [](#impressionist)[Impressionist](https://github.com/charlotte-ruby/impressionist)

A super cool gem for tracking your own impressions or page views in an app. I found this useful for tutorial or art-based sites like Dribbble where you can see/rank by views.

### [](#draftsman)[Draftsman](https://github.com/copasetickid/draftsman)

Creating a “draft” state isn’t too terribly hard but if you want to take that much further then Draftsman is a great gem. It’s inspired by the PaperTrail gem which is probably a little more popular. It includes popular scopes you might use for publishing content and a number of handy instance methods. The documentation is great, unlike many other gems that leave you to find your own way.

### [](#pryrails-amp-pry)[Pry-rails](https://github.com/rweng/pry-rails) & [Pry](http://pryrepl.org/)

While bye-bug comes with by default in new Ruby on Rails apps I much prefer Pry. If you ever need to debug some logic this is the perfect gem for you. It features some handy `rails console` based methods that return rich information about your app. The pry-rails gem just makes it much easier to add to a given app.

### [](#pay)[Pay](https://github.com/pay-rails/pay)

Accepting payments isn’t always an easy integration. Services like Stripe make it much easier but what if you need PayPal too? Pay helps with that and makes the process of integrating a full subscription engine into your app a breeze. Pay uses Stripe and Braintree for now with possible support for more to come.

### [](#mailcatcher)[Mailcatcher](https://mailcatcher.me/)

Since starting my deep dive into Ruby on Rails I’ve always been drawn to mailcatcher. It’s super easy to set up and run with any Rails app. There are more modern-looking alternatives out there but as they say, “If it ain’t broke, don’t fix it”.

### [](#redcarpet)[RedCarpet](https://github.com/vmg/redcarpet)

Process markdown to HTML with tons of options. It’s that simple.

### [](#actsasvotable)[ActsAsVotable](https://github.com/ryanto/acts_as_votable)

Even though it seems like a one-trick pony I love this gem. It’s great for comment voting, post voting, general feedback on content and more where you need it. I once used it as a way to favorite certain posts on a given rails app that feed a new type of feed to a given user’s account.

### [](#actsastaggable)[ActsAsTaggable](https://github.com/mbleigh/acts-as-taggable-on)

Before I knew how to implement tags on my own I leveraged this gem. It’s a big time-saver for adding tagging to any type of model that might require it. It’s quick and easy to extend and is easy to use.

### [](#unread)[Unread](https://github.com/ledermann/unread)

If you do any type of in-app messaging that’s not JavaScript-driven I definitely recommend this gem.

*   Manages unread records for anything you want readers (e.g. users) to read (like messages, documents, comments etc.)
*   Supports _mark as read_ to mark a **single** record as read
*   Supports _mark all as read_ to mark **all** records as read in a single step
*   Gives you a scope to get the unread records for a given reader
*   Needs only one additional database table
*   Most important: Great performance

### [](#homebrew-and-homebrewcask)[Homebrew](https://github.com/Homebrew/brew) and [Homebrew-cask](https://github.com/caskroom/homebrew-cask)

Without a doubt my number one ruby gem. Gone are the days where I install apps or software via DMG files. Using this gem is highly productive and well worth the fuss.

### [](#pagy)[Pagy](https://github.com/ddnexus/pagy)

For a long time, I used will\_paginate but started to notice the dramatic performance boosts you get from Page. Combine the performance with the ease of use and it’s an obvious contender for pagination in a Ruby on Rails app.

### [](#sidekiq)[Sidekiq](https://sidekiq.org/)

In a production app, you absolutely need background processing to keep your servers healthy. Sidekiq integrates very nicely as an active job adapter and makes things like sending thousands of emails a breeze. You can build up your own queues and define how they get sent.

### [](#whenever)[Whenever](https://github.com/javan/whenever)

The defacto cron job scheduler gem. If you need to automate jobs/logic in a ruby on rails app look no further.

The post [Some Of My Favorite Ruby Gems](https://web-crunch.com/some-of-my-favorite-ruby-gems/) appeared first on [Web-Crunch](https://web-crunch.com/).
