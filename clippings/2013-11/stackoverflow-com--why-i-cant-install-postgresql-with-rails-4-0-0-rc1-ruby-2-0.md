---
url: "http://stackoverflow.com/questions/17003917/why-i-cant-install-postgresql-with-rails-4-0-0-rc1-ruby-2-0"
captured_at: "2013-11-12T22:28:31-03:00"
title: "Why I can't install postgresql with rails 4.0.0.rc1 (ruby 2.0) - Stack Overflow"
domain: "stackoverflow-com"
---

|  |
| --- |
| Windows 7 x64, Ruby2.0.0p247-x64, Rails4.0.0, Postgresql 9.2.4 x64, pg 0.15.1, mysql2 0.3.11) There seems to be a platform detection/verification problem with bundler. While what I did *is* a hack of the Gemfile.lock file (I know, I know...), I have a (hopefully) temporary solution:  Edit Gemfile.lock, and   - Find the line for 'pg':   ```  multi_json (1.7.7) pg (0.15.1-x86-mingw32) polyglot (0.3.3) ```   - Copy the line, and modify the new copy to :   ```  multi_json (1.7.7) pg (0.15.1-x64-mingw32) pg (0.15.1-x86-mingw32) polyglot (0.3.3) ``` |
