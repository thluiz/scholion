---
title: "Large Ruby File Downloads Done Right!"
date: '2012-01-02T12:22:30-03:00'
category: webclip
summary: 'The post shows how to download very large files in Ruby without loading the full HTTP response into memory. It streams each response segment straight to disk to avoid running out of RAM.'
tags: ["ruby", "file-downloads", "memory-management"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Large Ruby File Downloads Done Right! - Dan Watsons Coding Zen"
    url: "http://www.dotnetguy.co.uk/post/2011/09/27/large-ruby-file-downloads-done-right?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+railsquicktips+%28Rails+Quick+Tips%29"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-01/dotnetguy-co-uk--large-ruby-file-downloads-done-right-dan-watsons-coding-zen.md"
    kind: repo
---

The post explains that large file transfers need to account for limited RAM. In the example, a Ruby utility moves files from Rackspace Cloud to Amazon S3 on a small EC2 instance, so the download has to be written to disk as it arrives instead of being kept in memory.

## Reading notes

- The utility downloads large files from Rackspace and uploads them to Amazon S3.
- Some of the files are 1 GB or larger.
- The server used is an Amazon Micro EC2 instance with 613 MB of RAM.
- Loading the full HTTP response into memory would risk exhausting RAM and stopping the download.
- The code uses Net::HTTP to request the file.
- The response body is read in segments.
- Each segment is written directly to a file on disk.
- The file handle is closed in an ensure block.
