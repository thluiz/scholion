---
title: "Is your Rails app ready for Production?"
date: '2016-04-11T14:20:18-03:00'
category: webclip
summary: 'The article argues that a Rails production setup should favor managed deployment, proper web servers, monitoring, current dependencies, Postgresql, CDN use, and access control before a system grows or fails.'
tags: ["rails", "production", "monitoring", "deployment"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Is your Rails app ready for Production? | AkitaOnRails.com"
    url: "http://www.akitaonrails.com/2016/03/22/is-your-rails-app-ready-for-production"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-04/akitaonrails-com--is-your-rails-app-ready-for-production.md"
    kind: repo
---

The article argues that a Rails app should not be deployed on cheap infrastructure without ongoing monitoring and upgrades. It recommends Heroku or another PaaS, warns that security patches and library updates are still necessary, and says production support requires either dedicated staff or a managed platform.

## Reading notes

- Prefer a PaaS such as Heroku instead of unmanaged low-cost instances unless someone will monitor and upgrade them constantly.
- Use a real web server such as Passenger or Puma, not only `rails server`; Unicorn is presented as a weaker choice for slow clients.
- Watch memory use and R14 errors, especially on small Heroku dynos, and reduce worker counts or add capacity when needed.
- Monitor the app with metrics, logs, and APM tools such as New Relic, and use log storage tools when needed.
- Stay on supported Rails and Ruby versions; the text recommends Rails 4.0 to 4.2 and Ruby 2.2 or 2.3.
- Install common production dependencies such as rails_12factor, Rack-Cache, Rack-Attack, Rack-Protection, and Sprockets 3.3+.
- Use Postgresql and, for background jobs, small Redis instances with Sidekiq; avoid loading large datasets in memory and send read-heavy workers to a follower database.
- Use a CDN for assets, and for uploads prefer direct browser upload to Cloudinary through Attachinary rather than sending large files through Rails.
- Revoke access when developers leave, rotate passwords and keys, and keep one person who controls critical credentials.
- As the site grows, use monitoring data to prioritize bottlenecks instead of rewriting everything, and fix the worst performance problems first.
