---
title: "How to speed up your Rails app with Cloudfront and the asset pipeline"
date: '2015-10-14T14:25:23-03:00'
category: webclip
summary: 'The post explains how to speed up a Rails app by serving fingerprinted assets through a Cloudfront distribution, using a custom origin and an asset_host in production.'
tags: ["rails", "cloudfront", "asset-pipeline", "cdn"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to speed up your Rails app with Cloudfront and the asset pipeline | Happy Bear Software | Web Application Development"
    url: "http://www.happybearsoftware.com/use-cloudfront-and-the-rails-asset-pipeline-to-speed-up-your-app.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-10/happybearsoftware-com--how-to-speed-up-your-rails-app-with-cloudfront.md"
    kind: repo
---

The article argues that using Cloudfront as an asset host can make Rails apps feel faster, especially for users with a fresh cache. It relies on the Rails asset pipeline fingerprinting files so Cloudfront can cache each version without cache invalidations.

## Reading notes

- It recommends Cloudfront for static assets such as CSS, JavaScript, and images.
- It warns against serving static assets directly from S3 because S3 is for storing files, not serving web traffic.
- Cloudfront serves files from edge cache locations close to the user.
- A distribution is set up with an origin, and requests are forwarded to the origin when Cloudfront does not have a cached copy.
- The post says Cloudfront can use a custom origin, not just S3 buckets.
- It suggests creating a distribution in the AWS management interface and testing asset URLs before changing Rails configuration.
- In Rails, setting `asset_host` in `production.rb` makes asset links point to the Cloudfront distribution.
- The asset pipeline appends a hash to asset filenames, so new file versions become distinct resources.
- Because of that fingerprinting, the post says syncing assets to S3 is not needed.
- The same fingerprinting also removes the need for cache invalidations when assets change.
