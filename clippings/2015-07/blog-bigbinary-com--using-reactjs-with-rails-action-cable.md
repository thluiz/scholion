---
url: "http://blog.bigbinary.com/2015/07/19/using-reactjs-with-rails-actioncable.html"
captured_at: "2015-07-26T10:20:51-03:00"
title: "Using ReactJS with Rails Action Cable | BigBinary Blog"
domain: "blog-bigbinary-com"
---

# Using ReactJS with Rails Action Cable

July 19, 2015 -
Vipul

Recent DHH, announced availability of alpha version of Action Cable.

[Action Cable](https://github.com/rails/actioncable) is still under
heavy development but it comes with [examples](https://github.com/rails/actioncable-examples)
to demonstrate its usage.

Action Cable integrates websocket based real-time communication in Ruby on Rails applications.
It allows building realtime applications like Chats, Status updates, etc.

### Action Cable + React

Action Cable provides real time communication. ReactJS is a good tool to
manage view complexity on the client side. Together they make it easy to
develop snappy web applications which requires state management on
the client side without too much work.

Anytime data changes the new data is instantly provided by Action Cable
and the new data is shown on the view without user doing anything on the
application by ReactJS.

### Integrating React

The official Action Cable Example is a chat application. We will be
building the same application using [ReactJS](https://facebook.github.io/react).

First follow the [instructions mentioned](https://github.com/rails/actioncable-examples) to get a working chat application using Action Cable.

Now that the chat application is working let’s get started with adding
ReactJS to the application.

*Please note that we have also posted a number of
[videos](http://bigbinary.com/videos)
on learning
ReactJS. Check them out if you are intereted.*

### Step 1 - Add required gems to Gemfile

```
# react-rails isn't compatible yet with latest Sprockets.
# https://github.com/reactjs/react-rails/pull/322
 'react-rails' github 'vipulnsward/react-rails' branch 'sprockets-3-compat'

# Add support to use es6 based on top of babel, instead of using coffeescript
 'sprockets-es6'
```

### Step 2 - Add required JavaScript files

Follow [react-rails installation](https://github.com/reactjs/react-rails#installation) and run `rails g react:install`.

This will

- create a components.js file.
- create `app/assets/javascripts/components/` directory.

Now put following lines in your application.js:

```
//= require react
//= require react_ujs
//= require components
```

Make sure your `app/assets/javascripts/application.js` looks like this

```
//= require jquery
//= require jquery_ujs
//= require turbolinks
//= require react
//= require react_ujs
//= require components
//= require cable

//= require channels
//= require_tree .
```

### Step 3 - Setup Action Cable to start listening to events

We will be using es6, so lets replace the file `app/assets/javascripts/channels/index.coffee`, with `app/assets/javascripts/channels/index.es6` and add following code.

```
cable  CablecreateConsumer'ws://localhost:28080'
```

Also remove file `app/assets/javascripts/channels/comments.coffee`, which is used to setup subscription. We will be doing this setup from our React Component.

### Step 4 - Create CommentList React Component

Add following code to `app/assets/javascripts/components/comments_list.js.jsx`.

```
var CommentList = React.createClass({
  getInitialState(){
    let message = JSON.parse(this.props.message);
    return {message: message};
  },

  render() {
    let comments = this.state.message.comments.map((comment) => {
      return this.renderComment(comment);
    });

    return (
      <div>{comments}</div>
    );
  },

  renderComment(comment) {
    return (
      <article key={comment.id}>
        <h3>Comment by { comment.user.name }</h3>
        <p>{ comment.content }</p>
      </article>
    );
  }
});
```

Here we have defined a simple component to display a list of comments associated with a message.
Message and associated comments are passed as props.

### Step 5 - Create message JSON builder

Next we need to setup data needed to be passed to the component.

Add following code to `app/views/messages/_message.json.jbuilder`.

```
json.(message, :created_at, :updated_at, :title, :content, :id)
json.comments(message.comments) do |comment|
  json.extract! comment, :id, :content
  json.user do
    json.extract! comment.user, :id, :name
```

This would push JSON data to our `CommentList` component.

### Step 6 - Create Rails Views to display component

We now need to setup our views for Message and display of Comments.

We need form to create new Comments on messages. This already exists in `app/views/comments/_new.html.erb` and we will euse it as is.

```
<%= form_for  message Comment  remote    %>
<%= text_area :content  '100x20' %><br>
<%= submit 'Post comment' %>
<%  %>
```

After creating comment we need to replace current form with new form, following view takes care of that.

From the file `app/views/comments/create.js.erb` *delete* the line
containing following code. Please note that below line needs to be
deleted.

```
$('#comments').append('<%= render @comment %>
```

We need to display the message details and render our component to display comments.
Insert following code in `app/views/messages/show.html.erb` just before `<%= render 'comments/comments', message: @message %>`

```
<%= react_component 'CommentList' message renderpartial 'messages/message.json' locals message @message %>
```

After inserting the code would look like this.

```
<h1><%= @messagetitle %></h1>
<p><%= @messagecontent %></p>
<%= react_component 'CommentList' message renderpartial 'messages/message.json' locals message @message %>
<%= render 'comments/new' message @message %>
```

Notice how we are rendering CommentList, based on Message json content from jbuilder view we created.

### Step 7 - Setup Subscription to listen to Action Cable from React Component

To listen to new updates to comments, we need to setup subscription from Action Cable.

Add following code to `CommentList` component.

```
setupSubscription

  comments  cablesubscriptionscreate"CommentsChannel" 
    message_id statemessage

    connected function  
      setTimeout => perform'follow'
                                     message_id message_id  
    

    received function  
      updateCommentListcomment
    

    updateCommentList updateCommentList
```

We need to also setup related AC Channel code on Rails end.

Make following code exists in `app/channels/comments_channel.rb`

```
class CommentsChannel  ApplicationCableChannel
   follow
    stop_all_streams
    stream_from "messages:'message_id':comments"
  

   unfollow
    stop_all_streams
```

In our React Component, we use `App.cable.subscriptions.create` to create a new subscription for updates, and pass the
channel we want to listen to. It accepts following methods for callback
hooks.

- `connected`: Subscription was connected successfully. Here we use `perform` method to call related action,
  and pass data to the method. `perform('follow', {message_id: this.message_id}), 1000)`, calls `CommentsChannel#follow(data)`.
- `received`: We received new data notification from Rails. Here we take action to update our Component.
  We have passed `updateCommentList: this.updateCommentList`, which is a Component method that is called with data received from Rails.

### Complete React Component

Here’s how our complete Component looks like.

```
var CommentList = React.createClass({
  getInitialState(){
    let message = JSON.parse(this.props.message);
    return {message: message};
  },

  render() {
    let comments = this.state.message.comments.map((comment) => {
      return this.renderComment(comment);
    });

    return (
        <div>{comments}</div>
    );
  },

  renderComment(comment) {
    return (
        <article key={comment.id}>
          <h3>Comment by { comment.user.name } </h3>
          <p>{ comment.content }</p>
        </article>
    );
  },

  componentDidMount() {
    this.setupSubscription();
  },

  updateCommentList(comment) {
    let message = JSON.parse(comment);
    this.setState({message: message});
  },

  setupSubscription() {

    App.comments = App.cable.subscriptions.create("CommentsChannel", {
      message_id: this.state.message.id,

      connected: function () {
        // Timeout here is needed to make sure Subscription
        // is setup properly, before we do any actions.
        setTimeout(() => this.perform('follow',
                                      {message_id: this.message_id}),
                                      1000);
      },

      received: function(data) {
        this.updateCommentList(data.comment);
      },

      updateCommentList: this.updateCommentList
    });
  }
});
```

### Step 7 - Broadcast message when a new comment is created.

Our final piece is to broadcast new updates to message to the listeners, that have subscribed to the channel.

Add following code to `app/jobs/message_relay_job.rb`

```
class MessageRelayJob  ApplicationJob
   performmessage
    comment   MessagesControllerrenderpartial 'messages/message'
                                         locals message message
    ActionCableserverbroadcast "messages:message:comments"
                                 comment comment
```

which is then called from `Comment` model, like so-

Add this line to `Comment` model file `app/model/comment.rb`

```
after_commit  MessageRelayJobperform_latermessage
```

We are using message relay here, and will be getting rid of existing comment relay file - `app/jobs/comment_relay_job.rb`.
We will also remove reference to CommentRelayJob from `Comment` model, since after\_commit it now calls the `MessageRelayJob`.

### Summary

Hopefully we have shown that Action Cable is going to be a good friend
of ReactJS in future. Only time will tell.

Complete working example for Action Cable + ReactJS can be found [here](https://github.com/vipulnsward/actioncable-examples/tree/es6).

Vipul
*wrote on* **19 Jul 2015**
  

Tags:
