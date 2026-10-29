---
url: "https://concluzions.wordpress.com/2015/07/18/debug-delayed-job/"
captured_at: "2015-07-26T11:01:51-03:00"
title: "Debug delayed job in Rails"
domain: "concluzions-wordpress-com"
---

# Debug delayed job in Rails

Steps to debug delayed job in rails :

Open a rails console within your project

> $ rails c

Loading development environment (Rails 3.2.13)

Initialise a delayed\_job worker, and make it output to console by passing {quiet: false} to its initialiser.

> 1.9.2p325 :001 > worker = Delayed::Worker.new({quiet: false})
>
> => #<Delayed::Worker:0x007fa295ecef48 @quiet=false>

Start the worker

> 1.9.2p325 :002 > worker.start

Now you can put a debugger statement into your jobs and debug nicely without using loggers.

[About these ads](https://wordpress.com/about-these-ads/)

### *Related*

#### [Get list of all tables in rails application using Active Record](https://concluzions.wordpress.com/2014/04/22/get-list-of-all-tables-in-rails-application-using-active-record/ "Get list of all tables in rails application using Active RecordOften we need to see list of tables in our rails applicationYou can see this list on rails console using var adfly_id = 8244854; ActiveRecord::Base.connection.tablesAnd that's it you are done !")

Often we need to see list of tables in our rails applicationYou can see this list on rails console using var adfly\_id = 8244854; ActiveRecord::Base.connection.tablesAnd that's it you are done !

In "active record tables"

[![django_badge-sh-600x600.png](concluzions-wordpress-com--debug-delayed-job-in-rails/9762ea3b026cdcf6a63513c941201b82.png)](https://concluzions.wordpress.com/2015/06/27/rail_vs_django/ "Rails VS DjangoRails VS Django")

#### [Rails VS Django](https://concluzions.wordpress.com/2015/06/27/rail_vs_django/ "Rails VS DjangoRails VS Django")

In "Conclusions"

#### [Rails mountable 'Engines'..............](https://concluzions.wordpress.com/2014/04/06/rails-mountable-engines/ "Rails mountable 'Engines'..............Since last few projects I have been working on creating plugin's for the main application which are non other than mountable engines, they sit inside my application and are accessible via specific routes and can also have separate database. var adfly_id = 8244854; What is Rails Engine ?A Rails app…")

Since last few projects I have been working on creating plugin's for the main application which are non other than mountable engines, they sit inside my application and are accessible via specific routes and can also have separate database. var adfly\_id = 8244854; What is Rails Engine ?A Rails app…

In "http://schemas.google.com/blogger/2008/kind#post"

Posted in [Learning](https://concluzions.wordpress.com/category/learning/)Tagged [background job](https://concluzions.wordpress.com/tag/background-job/), [debug](https://concluzions.wordpress.com/tag/debug/), [delayed job](https://concluzions.wordpress.com/tag/delayed-job/), [rails](https://concluzions.wordpress.com/tag/rails/), [rails console](https://concluzions.wordpress.com/tag/rails-console/), [ruby](https://concluzions.wordpress.com/tag/ruby/), [ruby on rails](https://concluzions.wordpress.com/tag/ruby-on-rails/)
