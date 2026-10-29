---
url: "http://devdungeon.com/content/writing-mumble-bot-ruby"
captured_at: "2015-08-03T16:40:40-03:00"
title: "Writing a Mumble Bot in Ruby"
domain: "devdungeon-com"
---

# Writing a Mumble Bot in Ruby

Mumble is an open-source voice communication tool with low latency ideal for gaming.
It is an alternative to the non-free TeamSpeak and Skype options. The Ruby gem **mumble-ruby**
provides a library to connect and interact with Mumble as a client. These code snippets demonstrate how to connect and communicate in a chat room and private messages. At the very end, there is a fully functional command line chat client that is ready to use to chat on the DevDungeon.com Mumble server!

For more documentation, see the official [GitHub mumble-ruby project](https://github.com/mattvperry/mumble-ruby). Note that it requires Ruby 2.1.0 or greater and the OPUS codec.

## Install Prerequisites

```
# For Debian based distributions like Ubuntu/Linux Mint  
# I couldn't get it to work on Windows  
sudo apt install libopus0  
sudo apt install libopus  
  
# Install the gem  
sudo gem install mumble
```

## Connecting and Disconnecting

```
require'mumble-ruby'  
  
# Create a new client with a few configuration  
# values to override the defaults  
client MumbleClient'devdungeon.com'  
# Avoid spaces in username  
username "DevDungeonNeophyte"  
password "s3cretPassw0rd"  
  
  
clientconnect  
  
# Wait a couple seconds to establish connection  
sleep   
  
# Do something with client here...  
  
clientdisconnect
```

## Configuring All Clients Globally

To configure all clients globally use the following code. New clients created after this will inherit these new defaults. All of the values used here
Are the actual defaults, so these won't change anything. If you did want to change the values though this is how you would do it.

```
Mumbleconfigure   
# Audio configuration  
sample_rate 48000  
bitrate 32000# Kb/sec  
  
# The cert_dir specifies where to look for Certificates  
# It will create a subfolder for each user  
ssl_cert_optscert_direxpand_path  
ssl_cert_optscountry_code  
ssl_cert_optsorganization'github.com'  
ssl_cert_optsorganization_unit'Engineering'
```

## Join Channel

```
# Accepts the room name or ID  
clientjoin_channel'The Cellar'
```

## List All Channels

```
clientchannelschannel  
	puts channelinspect
```

## List Users

```
clientusers  
	puts userinspect
```

## Sending Messages

```
# Text message to user  
clienttext_user'NanoDano''Hello NanoDano from the Ruby bot!'  
  
# Image message to user  
clienttext_user_img'NanoDano''image.png'  
  
# Text message to channel  
clienttext_channel'The Cellar''Hello channel from the Ruby bot!'  
  
# Image message to channel  
clienttext_channel_img'The Cellar''image.png'
```

## Receiving Messages

```
# This callback needs to be set up BEFORE  
# the client.connect. Set it up once and every  
# time a message is received it will run  
# This handles chat and private messages   
clienton_text_message message  
    puts messageinspect
```

## Mute and Deafen

```
# Mute and unmute output of client  
client  
clientfalse# unmute  
  
# Silence incoming sound to client  
clientdeafen  
clientdeafenfalse# undeafen
```

## Playing Wav Files (Experimental)

```
# The WAV file sample rate needs to match client config  
clientplayerplay_file'/home/NanoDano/test.wav'
```

## Recording Audio (Experimental)

```
clientrecorderstart'/home/NanoDano/test.wav'  
sleep  
clientrecorder
```

## Streaming Raw PCM Data

```
# Start streaming from a FIFO queue of raw PCM data  
# Uses Music Player Daemon (MPD)  
# MPD can be installed on Debian based distros with  
# sudo apt-get install mpd  
clientplayerstream_named_pipe'/tmp/mpd.fifo'
```

## Keeping Bot Alive

You'll need to add a loop to keep the program alive. **CTRL-C** can
be used to interrupt the program and end execution. You could also create some
kind of condition upon which to exit. For example, you could have the bot exit after receiving a specific message.

Additionally, you could look in to using the [Ruby Deamons gem](http://daemons.rubyforge.org/).
That gem allows you to easily create daemonized services to run on your server.

```
# Configure and connect the client before this loop  
  
while  
# Just stay online until interrupted  
# Do bot things
```

## Fully Functional Command Line Chat

This program can be run out-of-the-box, assuming you have installed prerequisites listed at the beginning of the page. You can configure the variables but they will also work with the defaults. It connects to the devdungeon.com Mumble server where you can chat with other people. I recommend at least customizing your user name. When you run it, it will connect, list all the users and channels, and then join a channel. You will see any incoming private or channel messages in your console, and you can type in messages and press enter to send messages to the channel. Have fun and hope to see you on Mumble!

I ran this with Ruby 2.2 on Linux Mint(Debian) after installing the **libopus0** and **libopus-dev** packages with **apt-get**. I also had to install the **mumble-ruby** gem. I used RVM to install the latest version of Ruby. Follow the installation instructions on [rvm.io](https://rvm.io/) if you've never used it. You can then use **rvm install 2.2** and **rvm use 2.2 --default**. If you run in to problems regarding the 'login shell", edit the Gnome Terminal profile settings to turn on login shell option.

```
# This Ruby program will join the devdungeon.com Mumble  
# server and list all the channels and users   
require'mumble-ruby'  
  
# Set these variables  
channel_name 'The Cellar'  
server_host 'devdungeon.com'  
username "DevDungeonNeophyte"# Avoid spaces in username  
password "s3cretPassw0rd"  
  
client MumbleClientserver_host  
username  username  
password  password  
  
  
"Connecting. One moment..."  
clientconnect  
  
# Wait a couple seconds to establish connection  
sleep   
  
# Set up callback that will run every time a chat  
# or private message is received  
clienton_text_message message  
"Message Received: " messageinspect  
  
  
# One time actions after joining  
client  
clientdeafen  
  
"Server Channels:"  
clientchannelschannel  
	puts channelinspect  
  
"Users Online:"  
clientusers  
	puts userinspect  
  
  
clientjoin_channelchannel_name  
clienttext_channelchannel_name'Hello, I am taking my bot for a test run!'  
  
"Now waiting for private or channel messages..."  
"Use CTRL-C to end the program."  
  
# Just stay alive until killed  
while  
"Enter a message to send to the channel:"  
	outgoing_message   
	clienttext_channelchannel_name outgoing_message  
"Message sent."  
  
  
clientdisconnect
```
