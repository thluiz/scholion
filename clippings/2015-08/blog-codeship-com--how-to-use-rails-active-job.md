---
url: "http://blog.codeship.com/how-to-use-rails-active-job/"
captured_at: "2015-08-27T09:03:46-03:00"
title: "How to use Rails Active Job"
domain: "blog-codeship-com"
---

# How to use Rails Active Job

2015-08-26

You’re always striving to give your users a better experience when they use your website or application. One of the most important ways to achieve this is by giving them quick server response times. In this article, we’ll explore how to use Rails Active Job to enable us to do this through the use of a queuing system. You can also use queues to help normalize traffic spikes or load on the server, allowing work to be done when the server is less busy.

Active Job was first included in [Rails 4.2](http://weblog.rubyonrails.org/2014/8/20/Rails-4-2-beta1/) as a way to standardize the interface to a number of queueing options which already existed. The most common queues used within Rails applications are [Sidekiq](http://sidekiq.org/), [Resque](https://github.com/resque/resque), and [Delayed Job](https://github.com/collectiveidea/delayed_job).

Active Job allows your Rails app to work with any one of them (as well as with other queues) through a single standard interface. For the full list of which backends you can use with Rails Active Job, [refer to this page](http://api.rubyonrails.org/classes/ActiveJob/QueueAdapters.html). It’s also important to see which features are supported by which queueing system; some don’t support delayed jobs for example.

Even if you aren’t ready to use a queue in your application, you can still use Active Job with the default Active Job Inline backend. Jobs enqueued with the Inline adapter get executed immediately.

## Using Rails Active Job

Active Job has a fairly simple interface and set of configuration settings. Here’s how to make use of its various features:

### Generating a job

Active Job comes with a generator which will create not only your job class but also a test stub for it.

```
rails g job TweetNotifier
  invoke  test_unit
  create  testjobstweet_notifier_job_testrb
  create  appjobstweet_notifier_jobrb
```

### Adding an item to the queue

If you want to process the job as soon as possible, you can use the `perform_later` method. As soon as a worker is available it will process the job.

```
UpdateUserStatsJobperform_later user
```

### Queueing for later

If you would rather have the job performed a week from now, some queue backends allow you to pass additional time parameters when adding a job.

```
UserReminderJobwait weekperform_later user
```

### What goes in a job class?

The job class is where you put the code that will be executed by the queue. There is a `perform` method which is called and sent whatever parameters were sent when the job was first enqueued (when you called the `perform_later` method).

```
class UpdateUserStatsJob  ActiveJob:Base 
  queue_as :default

   performuser 
    userupdate_stats
```

### Using Rails Active Job with Sidekiq and Resque

Both Sidekiq and Resque rely on having Redis installed, which is where they store the items in the queue. To use either of these, I recommend following the instructions found on the [Resque GitHub page](https://github.com/resque/resque) or the [Sidekiq wiki](https://github.com/mperham/sidekiq/wiki).

We will need to tell Active Job which queue we are using, which can be done in the application config file. In this example, we’ll be working with Sidekiq.

```
module MyApp
  class Application  Rails:Application
    configactive_jobqueue_adapter  :sidekiq
```

Sidekiq and Resque both come with web interfaces to view information about the workers and which jobs are in the queue. Sidekiq is more efficient and quick than Resque but requires that your Ruby code is [thread-safe](https://bearmetal.eu/theden/how-do-i-know-whether-my-rails-app-is-thread-safe-or-not/). Also, even though this is somewhat down to my own personal preference, Sidekiq has a nicer web interface than Resque does.

## Common Patterns for Queueing

There are a number of common patterns or types of jobs that you want to process in the queue. The basic rule I follow is to ask whether it needs to happen right now and/or if it might take a long time to process.

If it has to happen right now (for example, whether someone’s credit card information is correct), you’ll more than likely have to bite the bullet and process it before the response can go back to the user. Even still, you should think about the user experience by displaying a message letting them know that you’re processing their information and it may take a little while.

### Sending email

Sending email is the most common task that can and should be done in the background job. There is no reason to send emails immediately (before the response is rendered), and I always move all emails to the queue. Even if the email server responds in 100ms, that’s still 100ms that you’re making your user wait when they don’t need to.

Sending emails via a background job is super simple with Active Job, mainly because it comes built-in to ActionMailer.

By changing the method `deliver_now` to `deliver_later`, Active Job will automatically send this email asynchronously in the queue.

```
UserMailerwelcome@userdeliver_later
```

### Processing images

Images can take a while to be processed. This is especially true if you have a few (or more) different styles and sizes that need to be created. Luckily, both [Paperclip](https://github.com/thoughtbot/paperclip) and [CarrierWave](https://github.com/carrierwaveuploader/carrierwave) have additional gems which can help them process these images in the queue rather than at the time of uploading.

Paperclip uses a gem called [Delayed Paperclip](https://github.com/jrgifford/delayed_paperclip), which supports Active Job, and CarrierWave uses a gem called [CarrierWave Backgrounder](https://github.com/lardawge/carrierwave_backgrounder). That doesn’t yet support Active Job at the time of this article, but there is an [open pull request](https://github.com/lardawge/carrierwave_backgrounder/pull/217) looking to add this functionality.

For Delayed Paperclip, you simply call an additional method letting it know what you would like to process in the background, and the gem will handle the rest. You can even have it process some styles right away, while other styles get processed in the queue.

```
class   ActiveRecord:Base
  has_attached_file :avatar styles  small "25x25#", medium: "50x50#", large: "200x200#" }, only_process: [:small]

  process_in_background :avatar only_process :medium :large
```

This would allow us to show the `:small` image right away, while the `:medium` and `:large` images are done in the background.

### User uploaded content

Often when you have user uploaded content it needs to be processed. This may be a CSV file that needs to be imported into the system, an image which needs to have thumbnails generated, or a video that needs to be processed.

A large CSV file may take a few minutes to process, in which time the browser’s connection may time out. I’ve taken to processing most data uploads asynchronously in the queue.

The process I use is as follows:

1. Accept the file and upload it to S3 (or wherever you are storing user generated content).
2. Add a job to the queue to process this file.
3. The user will immediately see a success page letting them know that their file has been submitted for processing.
4. The worker will download the file, process it, and mark it as having been processed.

Another thing to keep in mind is that you will want to store a report of the import in the database. This may include any records that couldn’t be processed due to invalid data. What I do is create a second error file for each import that the user can download.

### Generating reports

Large reports can often take longer to generate than you want your user to wait for. You also might not want to put this sort of load on your app servers. You can generate a report in the queue and then email a link to the user to be able to download it when it is ready. I’ve seen this be incredibly useful when producing reports for the accounting department, which often needs to download reports with millions of records in them.

The flow for generating this type of report is as follows:

1. Allow user to specify which report they wish to generate along with all of its filters.
2. Add a job to the queue to produce this report.
3. The user will immediately see a page or notification letting them know that their report has been submitted for processing and how they can expect to receive it.
4. The user will either be notified within the user interface of the website/app that the file is ready to download, and/or they will receive an email with a link to download the finished report.

### Talking with external APIs

External APIs can be flaky and slow, and your users’ experience should not depend on them whenever possible. Take this example below where we use their IP address to find out some geo information about them using the [Telize](http://www.telize.com/) API. It generally responds in 200ms to 500ms, which, added to your current response time, can make a large difference. This is something that can wait to be done, especially when used for reporting purposes. Even though this is showing IP geo information, all external APIs should be treated the same way. Talk to them in the background if at all possible.

First we’ll schedule a job to be done, passing in the IP address of the current request.

```
LogIpAddressJobperform_laterrequestremote_ip
```

Our job class will accept an IP address, change it to a default if `"::1"` (localhost) for testing purposes, and then call the LogIpAddress class to actually do the work.

```
class LogIpAddressJob  ActiveJob:Base
  queue_as :default

   performip 
    ip  "66.207.202.15"  ip  "::1" 
    LogIpAddressip
```

Here we perform the actual work to be done. This code doesn’t implement actually logging the geo info to a log or database. It makes a real remote call to the API to show how long requests like this can take.

```
class LogIpAddress

   ip 
    iplog 
  

   initializeip 
      ip 
  

   get_geo_info 
    HTTParty"httpwwwtelizecom/geoip/#{@ip}").parsed_response 
  

   log 
    geo_info  get_geo_info 
    Railsloggerdebuggeo_info 
    # log response to database
```

In our Rails logs we can see what’s happening. It enqueues the job with the argument `"::1"`, performs the job right away (because we are using the Inline queue), outputs some debug info from our class, and then lets us know when the job is finished. It also shows that it took 572.39ms.

```
ActiveJob Enqueued LogIpAddressJob   839db96228a04e9d-9168b08674ba192f to Inlinedefault with arguments "::1"
ActiveJob LogIpAddressJob 839db96228a04e9d-9168b08674ba192f Performing LogIpAddressJob from Inlinedefault with arguments "::1"
ActiveJob LogIpAddressJob 839db96228a04e9d-9168b08674ba192f "longitude"79.4167 "latitude"43.6667 "asn""AS21949" "offset" "66.207.202.15" "area_code" "continent_code" "dma_code" "city""Toronto" "timezone""America/Toronto" "region""Ontario" "country_code" "isp""Beanfield Technologies Inc." "postal_code""M6G" "country""Canada" "country_code3""CAN" "region_code"
ActiveJob LogIpAddressJob 839db96228a04e9d-9168b08674ba192f Performed LogIpAddressJob from Inlinedefault  39ms
```

### Notifying others of changes

When a user creates new content (for example, they tweet something), you often have to let others know of that change. Determining who to notify can be a difficult (slow) process, and there is no reason to slow down the experience of the user who is creating this content.

If the tweet is created successfully, you can add a job in the controller to notify users that were mentioned or who follow this user.

```
 create 
  @tweet  Tweettweet_params

  respond_to  format 
     @tweetsave 
      TweetNotifierJobperform_later@tweet 
      formathtml  redirect_to @tweet notice 'Tweet was successfully created.'     
      formatjson  render :show status :created location @tweet  
     
      formathtml  render   
      formatjson  render json @tweeterrors status :unprocessable_entity
```

In the Job class, we can simply pass the work off to a specialized class for notifying users about this tweet.

```
class TweetNotifierJob  ActiveJob:Base 
  queue_as :default

   performtweet 
    TweetNotifiertweetnotify
```

Our TweetNotifier class does the bulk of the work. It parses the Tweet looking for who was @ mentioned and also adds this Tweet to the timeline of any User which follows this User.

```
class TweetNotifier

   initializetweet 
    @tweet  tweet 
  

   notify 
    notify_mentions 
    notify_followers 
  

  private

     notify_mentions
      # search for @ mentions and notify users
    
    
     notify_followers
      # add tweet to timelines of user's followers
```

## GlobalID for Object Serialization

You’ll notice in the last example that I actually just passed the entire tweet object to the worker. It used to be quite common to have to pass the tweet ID and then query for that tweet once inside the worker, but [GlobalID](https://github.com/rails/globalid) allows us to pass the entire object and handles the serialization and deserialization for us.

## In Conclusion

Active Job is a great addition to Rails. It won’t get you out of having to learn how to best use the queue backend that you end up going with, but it will provide a clean and single interface for adding jobs and processing those jobs, no matter the backend. If you’re starting a new Rails project or adding a queueing system to an existing one, definitely think about using Active Job rather than talking directly to the queue.

Using queues can increase your website usability (by lowering response times), provide more consistent response times and server loads (by spreading the heavy lifting over various servers and workers), and open new doors to what your website can do (by allowing more complex processing out of the user request/response flow).
