---
url: "http://blog.chaps.io/2015/11/13/role-based-authorization-in-rails.html"
captured_at: "2016-01-02T13:58:04-03:00"
title: "Role-based authorization in Rails"
domain: "blog-chaps-io"
---

# Role-based authorization in Rails

For many years, almost every Rails project I started included CanCan, the most popular authorization gem by Ryan Bates.
It was very easy to use in applications built from scratch as well as to include in existing projects. To make things even better, it left the programmer a lot of room for customization.

However, after working on dozens of Rails projects using CanCan, I started to notice some uncomfortable patterns.

While being extremely simple to use, it didn’t impose any structure inside the Abilities.
Over the years, it resulted in some **bad code practices**:

```
 moderator?
   :manage 
   :manage Topic
elsif member?
   :read 
   :read Topic

   :create 
   :create Topic

   :update :destroy   
    author  
  
elsif guest?
   :read 
   :read Topic

 banned?
  cannot :create 
  cannot :create Topic
```

If you look closely at the body of each role, you will notice that members and guests share some duplicated permissions. This is fine for very simple apps with few rules, but imagine maintaining and keeping the permissions synced in apps having dozens of models and actions. It becomes a burden really quickly.

Another popular *sin* I noticed is the use of `cannot` to override previously allowed behaviour. Firstly, we give users permission to create posts and topics, **but** if he is banned, we revoke his right to do this.
Some of the abilities I saw were giving and revoking permissions two or more times during one permission check. This is **highly inneficient** and hard to follow while debugging issues.

Writing secure apps is a hard task, which I decided to simplify by creating Access Granted gem. Keep reading if you want to make your life easier in future projects!

# Enter Access Granted

[Access Granted](https://github.com/chaps-io/access-granted) solves these drawbacks by implementing support for roles and permission inheritance. It allows you to keep roles as simple as possible without having to repeat yourself and forbids defining two identical permissions inside one role.

Those two seemingly simple features make writing secure permissions systems exceptionally easy.
In this blog post, we will implement permission system for our imaginary forum app in Rails to demonstrate its benefits.

Simply add `access-granted` to your Gemfile:

```
 'access-granted' '~> 1.0.0'
```

then bundle and run the generator to create your starter AccessPolicy:

```
rails generate access_granted:policy
```

which you can find in `app/policies/access_policy.rb`.

Forums are a good showcase of user hierarchy I mentioned above, because they usually need a hierarchical permission system based on the following roles:

- moderators
- registered users
- guests

The order in which roles are sorted is also the order of importance. The moderator is the role with the most permissions and the guest is the role with the least.

In Access Granted roles are defined in the same, top-to-bottom, order:

```
class AccessPolicy
  include AccessGrantedPolicy

   configure
     :moderator    moderator?  
      # permissions will go here
    

     :member    registered?  
      # permissions will go here
    

     :guest 
      # permissions will go here
```

Every role has a name and an optional predicate to check if it’s active for the user.

*Note:* Above you can see me using `.moderator?` and `.registered?` methods inside the Procs - these are app-specific and may come from, for example, [ActiveRecord::Enum](http://api.rubyonrails.org/classes/ActiveRecord/Enum.html) module.

# Implementing permissions

Defining permissions happens inside role blocks. The syntax is exactly the same as with CanCan, allowing for almost seamless transition to Access Granted.

Let’s define some basic permissions for the `:guest` role we bootstrapped above. In our forum app, guests can only read topics and posts. Let’s tell Access Granted to allow them to do only that:

```
 :guest 
   :read 
   :read Topic
```

The second argument expects a class of the entity we are checking permissions against. In Rails apps it is usually a descendant of ActiveRecord::Base, but it works with any Ruby class.

Now that guests can browse our forums, time to move one level up in our user hierarchy and define what registered members are allowed to do.

Roles inherit from less important roles below them, **but only from roles which apply to the given user**.
So we only need to add additional permissions on top of them. In this case, we will let members create posts and topics:

```
 :member    registered?  
   :create 
   :create Topic
```

So far everything is straightforward and easy to read. But users should be able to edit their own posts, right?

This feature requires defining dynamic permissions using blocks. Access Granted runs the blocks and allows the user to perform the action only if the block evaluates to true.

```
 :update    
  author
```

The gem lets you do more complex logic by running your own Proc and checking if it evaluates to true.

In this case, we check if `post`’s author is equal to the current `user` (available to developers as the second argument).

What about removing posts? The same conditions as with updating should apply.

We can avoid repeating ourselves by supplying an array of actions in the first argument. Access Granted will create a permission for each one of them.

```
 :update :destroy    
  author
```

The easiest one to define is `moderator`. Moderators should be able to do everything, regardless of whether they created it or not:

```
 :moderator    moderator?  
   :read :create :update :destroy 
   :manage Topic
```

`:manage` is a meta-action borrowed from CanCan, which is just a shortcut for defining all default CRUD actions (`[:read, :create, :update, :destroy]`).

To summarize, this is how our AccessPolicy should look like by now:

```
class AccessPolicy
  include AccessGrantedPolicy

   configure
     :moderator    moderator?  
       :read :create :update :destroy 
       :manage Topic
    

     :member    registered?  
       :create 
       :create Topic
       :update :destroy    
        author  
      
    

     :guest 
       :read 
       :read Topic
```

A lucky little side-effect of having native support for roles is that they serve as hash buckets for permissions making it up to 2 times faster than CanCan.

CanCan has to evaluate every `can` and `cannot` method in its ability to make sure nothing cancels out any of the previously defined permissions.

AccessGranted is lazy about it and rarely has to check every role that applies to a user.

# Permission checking

Now that we have all the basic permissions, I will explain how AccessGranted checks them for a given user.

For compatibility reasons and because Ryan has done a great job in CanCan, in Access Granted checking permissions is exactly the same.
There are two methods available in controllers and views: `can?` and `cannot?`.

In views you can check for creation permissions to decide if to show “Create new topic” buttons like this:

```
   :create Topic
   link_to "Create new topic" new_topic_path
```

`can?` also works on instances of classes.

A real life example would be checking if the current user can edit a Post.
We made sure that only owners of posts and admins can edit Posts. Now it’s time to let users see that they can do that.

```
   :update @topic
   link_to "Edit topic" edit_topic_path@topic
```

This will hide the button from non-owners of the topic, but show it to moderators and the author.

Perceptive and/or experienced readers will notice that users can still go to the URL and edit the topic, even though we don’t show the button.

Every sensitive controller action should check these permissions, too. That’s where `authorize!` method comes to play.
Continuing with Topics, let’s make sure TopicsController is protected.

For demonstration, we will secure the `destroy` action, so no one else can remove our topics. This is how the action looks like in newly generated scaffolding:

```
class TopicsController  ApplicationController
  # (...)

   destroy
    @topicdestroy
    redirect_to topics_path notice: 'Topic was successfully destroyed.'
  

  # (...)
```

All we need to do is add `authorize! :destroy, @topic` to the action before actual destruction happens:

```
 destroy
  authorize! :destroy @topic
  @topicdestroy
  redirect_to topics_path notice: 'Topic was successfully destroyed.'
```

Great, so now we check if `current_user` is allowed to visit that action… and what if he isn’t?
Access Granted throws a handy `AccessGranted::AccessDenied` exception from which we can `rescue` in our controllers.
`ApplicationController` is a good place since all other controllers inherit from it:

```
class ApplicationController  ActionController
  rescue_from AccessGrantedAccessDenied  exception
    redirect_to root_path alert: "You don't have permissions to access this page."
```

Now, every time someone tries to get sneaky and go to where he isn’t wanted, he will be redirected to `root_path` with an error message.

**Important:** Don’t forget to add `authorize!` to every security-sensitive action!

# Use outside of Rails

This post describes integrating Access Granted with Rails apps, but you are free to use it wherever you like, even non-web applications.

Policies are Plain Old Ruby Objects and respond to `can?` and `cannot?` methods.

```
policy  AccessPolicyuser_instance

policy:create Topic #=> true

policy:update topic #=> false
```

[Specs on GitHub](https://github.com/chaps-io/access-granted/blob/master/spec/policy_spec.rb) are a good way of learning what can be done with Access Granted in pure Ruby.

# Summary

If you have arrived at this point and like what you see, I recommend creating a new branch in your current project, migrating your CanCan code to AccessGranted, and enjoying your trivially simple permissions!

There’s more to permissions than I have described here, so check out the repository on [GitHub](https://github.com/chaps-io/access-granted#accessgranted--) and, in case you have any problems, create an issue there. I’d be happy to help and explain!
