---
url: "http://www.salsify.com/blog/detect-failed-delayed-job-workers/1571?utm_source=rubyweekly&utm_medium=email"
captured_at: "2013-11-30T23:15:31-03:00"
title: "Detecting Failed Delayed Job Workers: Don't Fear the Reaper"
domain: "salsify-com"
---

# [Don’t Fear the Reaper: Detecting Failed Delayed Job Workers](http://www.salsify.com/blog/detect-failed-delayed-job-workers/1571 "Permalink to Don’t Fear the Reaper: Detecting Failed Delayed Job Workers")

**By [Joel Turkel](http://www.salsify.com/blog/author/jturkel "Posts by Joel Turkel")** 
October 30, 2013

![16dea1ecf2f0b6f912fac01efe244fcc.jpg](salsify-com--detecting-failed-delayed-job-workers-dont-fear-the-reaper/16dea1ecf2f0b6f912fac01efe244fcc.jpg)

Previously we’ve blogged about how to write Delayed Job [plugins](http://www.salsify.com/blog/delayed-jobs-callbacks-and-hooks-in-rails)  and how to aggregate jobs into [job groups](http://www.salsify.com/blog/adding-job-groups-to-delayed-job-in-rails) **.** In this post we’ll explore how to proactively detect failed Delayed Job workers so their jobs can be retried in a timely manner**.** This is useful if a worker crashes, is automatically restarted by your platform provider, or is shutdown by auto-scaling infrastructure**.**

## The Delayed Job Lock Model

Let’s start off with a brief introduction to how Delayed Job implements locking**.** We’ll only consider the Active Record Delayed Job backend but the Mongoid backend uses a similar scheme**.** Jobs are stored in a `delayed_jobs` table that includes a YAML encoding of the object that will do the job’s work, the time the job was locked, the name of the worker that locked the job, and some additional metadata like the number of job attempts**.** When a worker picks up a job, it sets the job’s `locked_at` to the current time and sets the job’s `locked_by` to the worker’s name (which should be unique across your pool of workers)**.** Jobs are eligible to be picked up by a worker if they are not locked by another worker or they’ve been locked by another worker for more than `max_run_time` seconds**.**

At this point you might be wondering why Delayed Job’s `max_run_time` setting isn’t sufficient to unlock jobs that have been locked by failed workers**.** Well, it is, as long as you don’t mind waiting that long for jobs to be unlocked**.** That doesn’t work for us since we have `max_run_time` set pretty high to accommodate some long running bulk import and export jobs**.**

## The Delayed Job Heartbeat Plugin Overview

There are two parts to how we’ll unlock jobs for failed workers:

1. A Delayed Job plugin that runs on each worker and periodically updates a database table with heartbeat information
2. A reaper process that periodically unlocks jobs locked by workers that haven’t updated their heartbeat recently

Now let’s dive into some details on each of these components**.**

##### The Delayed Job Heartbeat Plugin

Our heartbeat plugin will consist of a few classes:

- **Delayed::Heartbeat::WorkerModel** – A persistent model with the name and last heartbeat timestamp of each worker**.** In the future this could be extended to included additional information about workers like the version of the source code they’re running**.** (Note we chose the name WorkerModel rather than just Worker to avoid confusion with Delayed Job’s Worker class)
- **Delayed::Heartbeat::WorkerHeartbeat** – Asynchronously updates a workers heartbeat timestamp
- **Delayed::Heartbeat::Plugin** – A Delayed Job plugin that plugs into the worker’s lifecycle to start and stop the WorkerHeartbeat**.**

First we’ll need a database migration to create the table for our worker models:

|  |  |
| --- | --- |
| 1 2 3 4 5 6 7 8 9 10 11 | class CreateDelayedWorkers < ActiveRecord::Migration  def change  create\_table(:delayed\_workers) do |t|  t.string :name  t.timestamp :last\_heartbeat\_at  add\_index(:delayed\_workers, :name, unique: true) |

Next let’s create the `WorkerModel` class that provides methods for updating the worker’s heartbeat and some ActiveRecord scopes that we’ll need for the reaper:

|  |  |
| --- | --- |
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 | module Delayed  module Heartbeat  class WorkerModel < ActiveRecord::Base  self.table\_name = 'delayed\_workers'  attr\_accessible :name, :last\_heartbeat\_at  before\_create do |model|  model.last\_heartbeat\_at ||= Time.now.utc  def update\_heartbeat  update\_column(:last\_heartbeat\_at, Time.now.utc)  def self.dead\_workers(timeout\_seconds)  where('last\_heartbeat\_at < **?**', Time.now.utc - timeout\_seconds.seconds)  def self.active\_names  select(:name) |

So far this has all been standard Rails stuff**.** Now things get a little more interesting with the `WorkerHeartbeat` that uses a background thread to periodically update the worker’s heartbeat:

|  |  |
| --- | --- |
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 | module Delayed  module Heartbeat  class WorkerHeartbeat  def initialize(worker\_name)  @worker\_model = create\_worker\_model(worker\_name)  # Use a self-pipe to safely shutdown the heartbeat thread  @stop\_reader, @stop\_writer = IO.pipe  @heartbeat\_thread = Thread.new { run\_heartbeat\_loop }  # We don't want the worker to continue running if the  # heartbeat can't be written  @heartbeat\_thread.abort\_on\_exception = true  def alive**?**  @heartbeat\_thread.alive**?**  def stop  # Use the self-pipe to tell the heartbeat thread to cleanly  # shutdown  if @stop\_writer  @stop\_writer.write\_nonblock('stop')  @stop\_writer.close  @stop\_writer = nil  private  def create\_worker\_model(worker\_name)  WorkerModel.transaction do  # Just recreate the worker model to avoid the race condition where  # it gets deleted before we can update its last heartbeat  WorkerModel.where(name: worker\_name).destroy\_all  WorkerModel.create**!**(name: worker\_name)  def run\_heartbeat\_loop  while true  break if sleep\_interruptibly(heartbeat\_interval)  @worker\_model.update\_heartbeat  rescue Exception => e  Rails.logger.error("Worker heartbeat error: #{e.message}: #{e.backtrace.join('\n')}")  raise e  ensure  Rails.logger.info('Shutting down worker heartbeat thread')  @stop\_reader.close  @worker\_model.delete  Delayed::Backend::ActiveRecord::Job.clear\_active\_connections**!**  def heartbeat\_interval  Rails.configuration.jobs.heartbeat\_interval\_seconds  # Returns a truthy if the sleep was interrupted  def sleep\_interruptibly(secs)  IO.select([@stop\_reader], nil, nil, secs) |

Some of the code for telling the heartbeat thread to shutdown might look a bit funky but it’s just using the [self-pipe trick](http://www.sitepoint.com/the-self-pipe-trick-explained/)  to perform an interruptible sleep**.**

We’ve done all the heavy lifting required to implement the plugin**.** Now let’s plug into the worker’s lifecycle to start/stop the heartbeat:

|  |  |
| --- | --- |
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 | module Delayed  module Heartbeat  class Plugin < Delayed::Plugin  callbacks do |lifecycle|  lifecycle.before(:execute) do |worker|  @heartbeat = WorkerHeartbeat.new(worker.name) if Rails.configuration.jobs.heartbeat\_enabled  lifecycle.after(:execute) do |worker|  @heartbeat.stop if @heartbeat |

Finally let’s register the plugin with Delayed Job in an appropriate initializer:

|  |  |
| --- | --- |
| 1 | Delayed::Worker.plugins << Delayed::Heartbeat::Plugin |

## The Reaper

Now that we have a Delayed Job plugin that periodically updates a worker’s heartbeat, we can unlock jobs that have been locked by workers that we haven’t heard from recently:

|  |  |
| --- | --- |
| 1 2 3 4 5 6 7 8 9 10 11 | module Delayed  module Heartbeat  def self.unlock\_orphaned\_jobs(timeout\_seconds = Rails.configuration.jobs.heartbeat\_timeout\_seconds)  WorkerModel.dead\_workers(timeout\_seconds).delete\_all  orphaned\_jobs = Delayed::Job.where("locked\_at IS NOT NULL AND " \  "locked\_by NOT IN (#{WorkerModel.active\_names**.**to\_sql})")  orphaned\_jobs.update\_all('locked\_at = NULL, locked\_by = NULL, attempts = attempts + 1') |

We’re running in Heroku so we’ve configured a [clockwork](https://devcenter.heroku.com/articles/clock-processes-ruby)  process to periodically unlock orphaned jobs:

|  |  |
| --- | --- |
| 1 2 3 4 5 6 7 8 9 10 11 | require File.expand\_path('../../config/boot', \_\_FILE\_\_)  require File.expand\_path('../../config/environment', \_\_FILE\_\_)  require 'clockwork'  include Clockwork  if Rails.configuration.jobs.heartbeat\_enabled  every(Rails.configuration.jobs.dead\_worker\_polling\_interval\_seconds.seconds, 'Unlock orphaned jobs') do  Delayed::Plugins::HeartbeatPlugin.unlock\_orphaned\_jobs |

You should be able to do something similar with your favorite scheduler**.**

Finally update your application.rb with the appropriate configuration for the heartbeat plugin and reaper process:

|  |  |
| --- | --- |
| 1 2 3 4 5 6 7 8 9 | config.jobs = ActiveSupport::OrderedOptions.new  # Controls whether or not workers report heartbeats  config.jobs.heartbeat\_enabled = true  # How often workers should send heartbeats  config.jobs.heartbeat\_interval\_seconds = 60  # How long a worker can go without sending a heartbeat before they're considered dead  config.jobs.heartbeat\_timeout\_seconds = 3 \* 60  # How often to check for dead workers  config.jobs.dead\_worker\_polling\_interval\_seconds = 60 |

That’s it**!** We can now unlock orphaned jobs in a few minutes rather than waiting a job’s maximum runtime to elapse**.**

## Other Solutions to Detecting Failed Delayed Job Workers**?**

Have you had similar problems with retrying jobs locked by failed Delayed Job workers**?** We’d love to hear how you solved them and what you think about our solution**.**
