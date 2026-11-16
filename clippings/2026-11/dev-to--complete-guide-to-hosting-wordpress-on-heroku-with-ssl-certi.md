---
url: "https://dev.to/aryaziai/complete-guide-to-hosting-wordpress-on-heroku-with-ssl-certification-4f2l"
captured_at: "2026-11-16T01:36:21+00:00"
title: "Complete Guide To Hosting Wordpress On Heroku With SSL Certification"
domain: "dev-to"
---

I recently moved all of my self-hosted [Wordpress](https://wordpress.org/) websites to [Heroku](https://www.heroku.com/) and I'm now spending $0 a month, happily saving over $300 a year in hosting and SSL Certificate fees! I've put together this guide for anyone who manages a self-hosted Wordpress site and is looking to not a dime (aside from annual domain fees). A special shoutout to Philipp Heuer for making this all possible.

**Disclaimer:** You are limited to a 5MB database, which is more than enough for most people unless you plan on having over 1,000 posts and/or plugins that generate new rows anytime that you publish a new post (not common). For anyone who may not know this: images, code, etc. are not stored in the database, they are simply referenced. I'll share a tool you should use to manage your database size later in this guide. You will also not be able to update the Wordpress version or add new plugins/themes from the WP Admin Dashboard. You're required to update the Wordpress version number in our Composer.json file, and manually add themes/plugins into our local Wordpress repo before pushing to heroku. This may sound time consuming, but it'll only require an extra 1-2 minutes each time that you need to make a Wordpress version, theme, or plugin update.

### Steps

1) [Register](https://signup.heroku.com/) a Heroku account for your respective site. Select "PHP" for primary development language. Adding credit card information is required for us to install Wordpress. It'll also improve our free plan by increasing our 500 free dyno hours to 1000. If you want to learn more about dyno hours work, I highly recommend reading Andrey Azimov's blog [post](https://medium.com/@AndreyAzimov/how-free-heroku-really-works-and-how-to-get-maximum-from-it-daa53f2b3c57). My Wordpress installation wouldn't complete without adding the CC. I've never been charged and my sites are very active. You can check your usage [here](https://dashboard.heroku.com/account/billing). Also try to keep a separate heroku account for each website, unless you don't expect much traffic.

2) Click the [Deploy to Heroku](https://github.com/PhilippHeuer/wordpress-heroku) button in Philipp Heuer's repo. I've tested several different Heroku/Wordpress installations and this is by far the best.

3) Visit your new app from your heroku [dashboard](https://dashboard.heroku.com/apps/) and open the settings. Clone the Heroku git URL onto your computer.

4) Clone [wordpress-heroku](https://github.com/PhilippHeuer/wordpress-heroku) onto your computer. Afterwards, move the contents of wordpress-heroku into your empty app's repo. CD into your app, git add, commit, and push. You can now remove the empty wordpress-heroku folder from your computer.

5) [Register](https://dash.cloudflare.com/sign-up) a Cloudflare account. Cloudflare will provide the appropriate instructions for updating your nameservers. i.e. Login to GoDaddy, edit DNS settings, update nameservers.

Example nameservers:  
**NS** aldo.ns.cloudflare.com  
**NS** josephine.ns.cloudflare.com

You can now check cloudflare to see if your nameservers are pointing to Cloudflare. I recommend waiting at least 5-10 minutes for it to update.

6) This step is optional but highly recommended. Click the "Page Rules" tab on Cloudflare and enter the following three page rules:

1.  \*YOURDOMAIN.com/\*  
    Always Use HTTPS
    
2.  [www.YOURDOMAIN.com/\*](http://www.yourdomain.com/*)  
    Forwarding URL - 301 Permanent Redirect  
    [https://YOURDOMAIN.com/$1](https://yourdomain.com/$1)
    
3.  YOURDOMAIN.com/\*  
    • Auto-minify Html, Css, Js  
    • Rocket Loader On  
    • Browser Cache TTL - 1 month
    

7) Open a new tab and visit your heroku app's settings again. Click "Add Domain" and enter your domain name without "www" or "https". Copy the DNS target. Go to your Cloudflare dashboard and click the DNS tab. We'll only need the following two rows. You can remove the other rows if you'd like.

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fr54ezmx6pp6hipoovhqg.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fr54ezmx6pp6hipoovhqg.png)

**Note:** Your DNS Target will most likely be different from than the one provided in the screenshot.

#### Congrats you can now visit your new Wordpress site!

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F5py6preg93uk86786u3x.jpeg)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F5py6preg93uk86786u3x.jpeg)  

### Updating Wordpress Version

You'll be updating Wordpress via Composer.json. If you do not have Composer installed on your computer, simply run **brew install composer** from the terminal. Open Composer.json in your repo's directory and look for: johnpbloch/wordpress. Change the version number to the latest wordpress version number.  
i.e. "johnpbloch/wordpress": "4.9.2" -> "johnpbloch/wordpress": "5.4"

Advanced: Comment-out any plugins that you won't be using. Make sure that you're not missing any commas, or ending the last key-value pair in an object with a comma! I personally don't care for the Wordfence or All in One SEO plugin.

Once your done, run **composer update** from the terminal. Don't forget to push your changes.

### Adding/Removing Plugins & Themes

To make changes to your plugins/themes, go to your repo /web/app. Here you will find your Theme and Plugin folders. Unzip your theme and plugins and place them inside these two folders. Once you've made the appropriate changes: git add, commit, and push to see changes.  
Official Directory: Wordpress [Themes](https://wordpress.org/themes/) and [Plugins](https://wordpress.org/plugins/).

**Note:** The mu-plugins folder stands for Must-Use plugins. These plugins are automatically enabled and will be hidden from your plugin dashboard.

### Preventing Redirect Loops/HTTPS Issues

If you're unable to login to the backend or getting "Not secure" errors, don't worry, there is a quick fix! Install [Cloudflare Flexible SSL](https://wordpress.org/plugins/cloudflare-flexible-ssl/) and update you SSL/TLS setting in Cloudflare to "Flexible".

Advanced: Replace any instances of "http" to "https" inside your repo's config/application.php file. You may now remove the plugin. Just be sure to use "https" links or the connection to your site will not be secure.

### Managing Database

I recommend using [MySQL Workbench](https://dev.mysql.com/downloads/workbench/) by Oracle to manage your database. To get your database credentials, visit your app's dashboard in Heroku and click the "JawsDB Maria" link. Whenever you make a change in MySQL Workbench, be sure to apply changes.

If you're not comfortable with optimizing your database with manual SQL queries, I recommend using the [WP Optimize](https://wordpress.org/plugins/wp-optimize/) plugin in Wordpress. The plugin will optimize your tables and help reduce your database size.

### Uploading Images

Each time that we make any changes to our Wordpress files and push our code, we are overwriting our uploads folder. Therefore any images that we uploaded inside our Wordpress dashboard will be overwritten. Sure you can manually add images to the web/app/uploads folder on your computer, push it up, and link to the images inside your post.. but this eventually become very tiring. The solution is AWS - S3 Storage.

1.  Install [WP Offload Media Lite](https://wordpress.org/plugins/amazon-s3-and-cloudfront/).
2.  Create an [AWS account](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=default&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start).
3.  Follow these [instructions](https://deliciousbrains.com/wp-offload-media/doc/amazon-s3-quick-start-guide/). Please do not skip any of the steps. It's very short, and will save you a lot of hassle from debugging the permission settings later on.
4.  You can store the access keys inside the database and change this option later.

**Important:** While recently debugging this plugin for a client, I noticed that the URL's of the uploaded images were not updating to the S3 bucket URL's. I figured that the plugin is incompatible with the latest version of Wordpress in our Heroku configuration. To be on the safe side, stick to Wordpress 5.2 until this issue is resolved. You can downgrade Wordpress in the Composer.json.

### Debugging

If you run into any issues, visit YOURAPPNAME.herokuapp.com rather than your custom domain. This eliminates Cloudflare from the picture and any potential caching or SSL issues. Ignore your wp-config file, it's almost useless to our configuration. Instead use your repo's config/application.php file if you want to add a PHP constant such as [WP\_DEBUG](https://codex.wordpress.org/WP_DEBUG). Also, disabling plugins one by one is always a smart choice in Wordpress but don't forget about the mu-plugins that are hidden from the dashboard. It's common for the redis-cache/object-cache.php to create issues. Comment-out all three lines pertaining to redis-cache in your composer.json before running an update, as well as deleting it from your mu-plugins folder if it's creating issues.

### Prevent Sleeping

Heroku's free plan will put an app to sleep after 30 minutes of inactivity. This will force the next visitor to wait several extra seconds before they can view your site. In order to prevent this from occuring, create a free account on [Cron-job.org](https://cron-job.org/), enter your site link, and set the schedule to every 30 minutes.

### The End

I hope that you found my guide useful, please let me know if you have any questions and I'll be more than happy to help 🙂
