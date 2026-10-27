---
url: "http://docs.webfaction.com/software/rails.html"
captured_at: "2014-01-05T17:21:18-03:00"
title: "Ruby on Rails — WebFaction Software Documentation"
domain: "docs-webfaction-com"
---

# **R**uby on Rails[¶](#ruby-on-rails "Permalink to this headline")

Ruby on Rails, also known as *Rails* or *RoR*, is an open source Ruby web
development framework**.** It enables developers to quickly design, develop, and
deploy web applications**.** You can learn more about Ruby on Rails at the [Rails](http://rubyonrails.org/) 
website**.**

Tip: Add bin to PATH

While working with a Ruby on Rails application, you may find it easier to add
the application’s bin directory to the PATH environment variable
and set the GEM\_HOME environment variable, instead of specifying complete
paths to $HOME/webapps/*app*/bin and
$HOME/webapps/*app*/gems**.**

To set the environment variables:

1. Switch to the directory of the Ruby application**.** Enter
   cd $HOME/webapps/{app} where *app* is the name of the application
   as it appears in the WebFaction control panel**.**
2. Enter export PATH=$PWD/bin:$PATH and press Enter**.**
3. Enter export GEM\_HOME=$PWD/gems and press Enter**.**
4. Enter export RUBYLIB=$PWD/lib and press Enter**.**

Now, programs like gem and rake will work as expected for that
application**.**

To revert the changes to PATH and GEM\_HOME (to work with a different Ruby
on Rails application, for example), just log out and log back in again**.**

## Installing Ruby on Rails[¶](#installing-ruby-on-rails "Permalink to this headline")

WebFaction’s Ruby on Rails installer creates an nginx instance running [Passenger](https://www.phusionpassenger.com/) **.**
To install a Rails application:

1. Log in to the control panel**.**
2. Click *Domains / websites ‣ Applications***.**
   The list of applications appears.
3. Click the *Add new application* button**.**
   The *Create a new application* form appears**.**
4. In the *Name* field, enter a name for the application**.**
5. In the *App Category* menu, click to select *Rails***.**
6. If applicable, in the *Machine* menu, click to select a web server**.**
7. Click the *Save* button**.**
   The application is installed and added to the list of applications**.**

To make the application available on the Web, [*add the application to a website record*](http://docs.webfaction.com/user-guide/websites.html#websites-create "(in WebFaction User Guide v)")**.**

## Upgrading RubyGems[¶](#upgrading-rubygems "Permalink to this headline")

You can upgrade any Passenger-based application to use a more recent version of
RubyGems. To upgrade Ruby Gems:

1. Open an SSH session to your account**.**
2. Switch to the Passenger-based application’s directory**.** Enter
   cd $HOME/webapps/*app*, where *app* is the name of your
   Passenger-based application, and press Enter**.**
3. Set the RUBYLIB environment variable**.** Enter
   export RUBYLIB=$PWD/lib and press Enter**.**
4. Set your GEM\_HOME environment variable**.** Enter
   export GEM\_HOME=$PWD/gems and press Enter**.**
5. Add the Passenger-based application’s bin directory to your
   PATH**.** Enter export PATH=$PWD/bin:$PATH and press Enter**.**
6. Create a directory to store the RubyGems files**.** Enter mkdir -p src and
   press Enter**.**
7. Switch to the new directory**.** Enter cd src and press Enter**.**
8. Download the RubyGems archive**.** Enter wget *url* where *url* is the
   download URL for RubyGems and press Enter**.** The RubyGems archive will
   be created in the current directory**.**

   Find the latest RubyGems download link at [Download RubyGems](http://rubygems.org/pages/download) **.**
9. Extract the RubyGems archive**.** Enter tar -xzf *archive*, where
   *archive* is the name of the RubyGems archive (for example,
   rubygems-1**.**7.2.tgz) and press Enter**.** tar extracts the RubyGems
   files to a directory, rubygems-*X**.**Y**.**Z* where *X.Y.Z* is the version
   number for RubyGems.
10. Switch to the RubyGems directory**.** Enter cd rubygems-*X.Y.Z* and press
    Enter**.**
11. Run the RubyGems setup file**.** Enter
    ruby setup**.**rb install --prefix=$HOME/webapps/*app* and press
    Enter**.**

The new version of RubyGems is now installed for your Passenger-based
application**.**

## Installing Gems[¶](#installing-gems "Permalink to this headline")

See also

To install gems in your home directory, see [*Installing Gems*](http://docs.webfaction.com/software/ruby.html#ruby-installing-gems) in our Ruby documentation**.**

To install a Ruby Gem in your Rails application:

1. Open an SSH session to your account**.**
2. Enter cd $HOME/webapps/*app*, where *app* is the name of your Ruby on
   Rails application, and press Enter**.**
3. Enter export GEM\_HOME=$PWD/gems and press Enter**.**
4. Enter export RUBYLIB=$PWD/lib and press Enter**.**
5. Enter export PATH=$PWD/bin:$PATH and press Enter**.**
6. Enter gem install *gem\_name*, where *gem\_name* is the name of the
   Ruby Gem you want to install, and press Enter**.**

   Common Gems

   To install some common gems:

   - MySQL adapter [MySQL/Ruby](http://www.tmtm.org/en/mysql/ruby/) :
     gem install mysql -- --with-mysql-config=$(which mysql\_config)
   - PostgreSQL adapter postgres:
     - For servers Web300 and Dweb89 or greater:
       gem install pg -- --with-pg-config=/usr/pgsql-9**.**1/bin/pg\_config
     - For other servers:
       gem install pg -- --with-pg-config=/usr/bin/pg\_config
   - Testing framework [RSpec](http://rspec.info/) : gem install rspec
   - Web framework [Sinatra](http://www.sinatrarb.com/) : gem install sinatra

   If you do not want to install the Rdoc or RI documentation, use this version
   of the command: gem install --no-rdoc --no-ri *gem\_name***.**

The gem and any of its specified dependencies will be downloaded and installed
automatically**.**

## Installing Multiple Gems with Bundler[¶](#installing-multiple-gems-with-bundler "Permalink to this headline")

You can use [Bundler](http://gembundler.com/)  to install multiple dependency gems in your Rails
application at once**.**
To use Bundler:

1. Open an SSH session to your account**.**
2. Enter cd $HOME/webapps/*app*, where *app* is the name of your Ruby on
   Rails application, and press Enter**.**
3. Enter export GEM\_HOME=$PWD/gems and press Enter**.**
4. Enter export RUBYLIB=$PWD/lib and press Enter**.**
5. Enter export PATH=$PWD/bin:$PATH and press Enter**.**
6. If you have not already installed Bundler for your Rails application,
   install Bundler**.**
   Enter gem install bundler and press Enter**.**
7. Switch to your Rails project directory**.**
   Enter cd *project*,
   where *project* is the name of your Rails project,
   and press Enter**.**
   For example, to use the default hello\_world Rails project,
   enter cd hello\_world and press Enter**.**
8. Install the gems specified in Gemfile**.**
   Enter bundle install and press Enter**.**

Bundler will download and install the specified gems.

## Installing ImageMagick and RMagick[¶](#installing-imagemagick-and-rmagick "Permalink to this headline")

[ImageMagick](http://www.imagemagick.org/)  is an open source image creation and editing package**.**

1. Install ImageMagick.
   1. Open an SSH session to your account**.**
   2. Download ImageMagick. Enter
      wget ftp://ftp.imagemagick.org/pub/ImageMagick/ImageMagick.tar**.**gz
      and press Enter. ImageMagick.tar**.**gz is created in the
      current directory.
   3. Unpack the ImageMagick archive**.** Enter tar -xf ImageMagick.tar.gz
      and press Enter**.** A new directory, ImageMagick-*version*,
      where *version* is the ImageMagick version number, is created**.**
   4. Switch to the ImageMagick directory**.** Enter
      cd ImageMagick-*version* and press Enter**.**
   5. Configure the ImageMagick build. Enter
      ./configure --prefix=$HOME --without-perl and press Enter**.**
   6. Compile ImageMagick. Enter make and press Enter**.** ImageMagick
      compiles. This step may take several minutes**.**
   7. Install ImageMagick to your home directory**.** Enter make install and
      press Enter**.**
   8. Return to your home directory. Enter cd and press Enter**.**
   9. Remove the installation files. Enter
      rm -r ImageMagick.tar**.**gz ImageMagick-*version* and press
      Enter**.**
2. Add $HOME/bin to your PATH**.**
   1. Enter echo "export PATH=$HOME/bin:\$PATH" >> .bash\_profile and
      press Enter**.**
   2. Reload your .bash\_profile**.** Enter source .bash\_profile and
      press Enter**.**
3. Install the RMagick gem**.**
   1. Enter export LD\_LIBRARY\_PATH=$HOME/lib and press Enter**.**
   2. Enter export PKG\_CONFIG\_PATH=$HOME/lib/pkgconfig/ and press
      Enter**.**
   3. [*Install the RMagick gem*](#rails-installing-gems) in your Ruby on
      Rails application**.**

The gem is now installed for your Rails application**.**

## Installing sqlite3-ruby[¶](#installing-sqlite3-ruby "Permalink to this headline")

By default, Rails is configured for use with SQLite version 3 databases**.** To use
a SQLite 3 database, the [sqlite3-ruby](http://rubyforge.org/projects/sqlite-ruby/)  gem must be installed**.** To install the
gem:

1. [*Install the latest version of SQLite from source*](http://docs.webfaction.com/software/sqlite.html#sqlite-install-from-source) in your home directory**.**
2. Install the sqlite3-ruby gem**.**
   1. Open an SSH session to your account**.**
   2. Enter cd $HOME/webapps/*app*, where *app* is the name of your Ruby
      on Rails application, and press Enter**.**
   3. Enter export GEM\_HOME=$PWD/gems and press Enter**.**
   4. Enter export RUBYLIB=$PWD/lib and press Enter**.**
   5. Enter export PATH=$PWD/bin:$PATH and press Enter**.**
   6. Enter export LD\_LIBRARY\_PATH=$HOME/lib/ and press Enter**.**
   7. Enter gem install sqlite3-ruby -- --with-sqlite3-dir=$HOME and
      press Enter**.**

## Deploying a Ruby on Rails Application[¶](#deploying-a-ruby-on-rails-application "Permalink to this headline")

To start using your own application with a Passenger-based Rails application:

1. Upload your application to your Rails application directory**.** For example, if
   you have an application, myapp, upload it to
   $HOME/webapps/*app*/myapp where *app* is the name of your Rails
   application as it appears in the WebFaction control panel**.**
2. Open an SSH session to your account**.**
3. Switch to the Rails application directory**.** Enter
   cd $HOME/webapps/*app* where *app* is the name of your Rails
   application, and press Enter**.**
4. Open ./nginx/conf/nginx.conf in a text editor**.**
5. Replace hello\_world in the line containing
   root /home/*username*/webapps/*app*/hello\_world/public with the
   name of your Rails app’s directory**.** In the earlier example, the line would
   contain root /home/*username*/webapps/*app*/myapp/public**.**

   You may now delete the provided hello\_world directory**.**
6. Reboot your Rails application**.** Enter ./bin/restart and press
   Enter**.**

## Deploying a Ruby on Rails Application with Capistrano[¶](#deploying-a-ruby-on-rails-application-with-capistrano "Permalink to this headline")

This section applies to Capistrano 2**.**x releases**.**
For information about using Capistrano 3.x releases, please refer to the official [Capistrano documentation](http://www.capistranorb.com/) **.**

1. If you have not already done so, install Capistrano on your local
   workstation**.** Typically, you can install Capistrano with
   gem install capistrano**.** See the Capistrano [Getting Started](https://github.com/capistrano/capistrano/wiki/2.x-Getting-Started) 
   documentation for details**.**
2. Create a deployment recipe for Ruby on Rails project**.**

   1. In a terminal session on your local workstation, switch to the directory
      containing your Rails project**.**
   2. Set up Capistrano for your project**.** Enter capify . and press
      Enter**.**
   3. Open config/deploy**.**rb in a text editor**.**
   4. Set the application name**.** In the line containing
      set :application, "set your application name here" replace
      set your application name here with a name for your project**.**
   5. Set the repository location**.** In the line containing
      set :repository,  "set your repository location here" replace
      set your repository location here with a URL (or path) to the version
      controlled (such as Git, Mercurial, Subversion, and others) Rails
      project**.**

      For example, for a Rails project stored on GitHub, you might enter
      https://*username*@github.com/*username*/*railsapp*.git**.**
   6. Set the version control type**.** In the line containing
      set :scm, :subversion replace subversion with the version control
      system used at the repository URL**.** Acceptable values include: accurev,
      bzr, cvs, darcs, git, mercurial, perforce, and subversion**.**
   7. Set the deploy\_to path**.** On a new line, insert
      set :deploy\_to, "/home/*username*/webapps/*railsapp*" where
      *username* is your WebFaction control panel user name and *railsapp* is
      the name of the Rails application as it appears on the control panel**.**
   8. Set the server name**.** In the lines containing:

      ```
      role :web, "your web-server here"
      role :app, "your app-server here"
      role :db,  "your primary db-server here", :primary => true
      ```

      replace your web-server here, your app-server here,
      your primary db-server here with the host name for your WebFaction
      server (for example, web100.webfaction.com)**.**
   9. Delete the line containing role :db,  "your slave db-server here"**.**
   10. Configure your user settings**.** Add these new lines:

       ```
       set :user, "webfaction_username"
       set :scm_username, "vcs_username"
       set :use_sudo, false
       default_run_options[:pty] = true
       ```

       where *webfaction\_username* is your WebFaction control panel user name
       and *vcs\_username* is the username for your version control repository**.**
   11. Add a task to restart Rails application’s nginx server after deployment**.**
       Add these lines:

       ```
       namespace :deploy do
         desc "Restart nginx"
         task :restart do
           run "#{deploy_to}/bin/restart"
         end
       end
       ```
   12. Save and close the file**.**
3. Prepare your Rails application for Capistrano deployment**.**

   1. Open $HOME/webapps/*app*/nginx/conf/nginx.conf where *app* is the
      name of your Rails application as it appears on the control panel**.**
   2. In the line containing
      root /home/*username*/webapps/*app*/hello\_world/public
      replace /home/*username*/webapps/*app*/hello\_world/public
      with /home/username/webapps/railsapp/current/public**.**
   3. Save and close the file.
   4. On your local workstation in the Rails project directory, enter
      cap deploy:setup and press Enter**.** Capistrano sets up
      the directories and permissions required for deployment**.**
   5. Verify your application is ready for deployment**.** Enter
      cap deploy:check and press Enter**.**
4. Deploy. Enter cap deploy and press Enter**.**

## Using a Database with a Ruby on Rails Application[¶](#using-a-database-with-a-ruby-on-rails-application "Permalink to this headline")

It’s easy to configure a MySQL or PostgreSQL for use with a Ruby on Rails application**.**

1. Create a database**.**

   1. Use the WebFaction control panel to create a MySQL or PostgreSQL database**.**

      See also

      For step-by-step directions, see [*Creating a New Database with the Control Panel*](http://docs.webfaction.com/user-guide/databases.html#databases-creating "(in WebFaction User Guide v)")**.**
   2. Make a note of the database name and password**.**
2. [*Install the Ruby database adapter gem*](#rails-installing-gems)**.**
   Install the mysql gem for MySQL.
   Install the postgres gem for PostgreSQL**.**
3. Configure the Ruby on Rails project to use the MySQL database**.**

   1. Switch to the directory of the Ruby on Rails project**.**
      Enter cd *project*, where *project* is the name of the project (for example, hello\_world),
      and press Enter**.**
   2. Open config/database.yml in a text editor**.**
   3. Edit the production section:

      ```
      production:
       adapter: sqlite3
       database: db/production.sqlite3
       pool: 5
       timeout: 5000
      ```

      to this:

      ```
      production:
       adapter: adapter_type
       database: database_name
       host: localhost
       username: database_user
       password: database_password
      ```

      such that

      - adapter\_type is either mysql for MySQL databases or postgresql for PostgreSQL databases,
      - database\_name is the name of the database as it appears in the WebFaction control panel,
      - database\_user is set to the name of a database user with access to the specified database, and
      - database\_password is the database user’s password**.**
   4. Save and close the file**.**

The Rails application is now configured and ready to use the specified database**.**

## Configuring Action Mailer[¶](#configuring-action-mailer "Permalink to this headline")

Configuring Action Mailer applies to Ruby on Rails 3**.**0 or later only.

To configure your Rails application:

1. Open
   $HOME/webapps/*rails*/*application*/config/environments/production**.**rb
   in a text editor, where *rails* is the name of the Ruby on Rails application
   as it appears in the WebFaction control panel and *application* is the name
   of your Ruby on Rails project (for example, hello\_world)**.**
2. In the *HelloWorld*::Application.configure do block, where
   *HelloWorld* corresponds to your Ruby on Rails application name, add this
   line:

   ```
   config.action_mailer.delivery_method = :sendmail
   ```

   See also

   For other Action Mailer settings, see [Action Mailer Basics](http://edgeguides.rubyonrails.org/action_mailer_basics.html#action-mailer-configuration)**.**
3. Save and close the file**.**

## Troubleshooting[¶](#troubleshooting "Permalink to this headline")

### Error: We're sorry, but something went wrong**.**[¶](#error-we-re-sorry-but-something-went-wrong "Permalink to this headline")

If you attempt to click Rails’ *About your application’s environment*
link, you may get an error like this:

> We’re sorry, but something went wrong**.**
>
> We’ve been notified about this issue and we’ll take a look at it shortly**.**

This error occurs when the link is clicked in production rather than
development mode**.** To switch your Rails application to development:

1. [*Install sqlite3-ruby*](#ruby-sqlite3)**.**
2. Open an SSH session to your account**.**
3. Open $HOME/webapps/*app*/nginx/conf/nginx.conf, where *app* is the
   name of the Rails application as it appears in the control panel, in a text
   editor**.**
4. In the server block, add rails\_env development; on a new line**.**
5. Save and close the file.
6. Restart the Rails application**.** Enter
   $HOME/webapps/*rails*/bin/restart and press Enter**.**

Rails development mode consumes dramatically more resources than
production**.** Be sure to return to production mode when development is no
longer needed**.**
