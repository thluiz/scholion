---
url: "http://www.fngtps.com/2015/some-best-practices-for-authentication-in-ruby-on-rails/"
captured_at: "2015-01-28T09:35:52-03:00"
title: "Some best practices for authentication in Ruby on Rails"
domain: "fngtps-com"
---

# Some best practices for authentication in Ruby on Rails

Manfred Stienstra

26 Jan 2015

Authentication, one of the more mundane parts of a Ruby on Rails application, turns out to be pretty diverse. So what are the best practices?

First you need to realize that *authentication* and *authorization* are different things. Authentication is verifying an identity: who are you? Authorization is enforcing permissions: are you allowed to do this?

This means you never name methods and variables in your application *auth*. Nobody will know what you mean so just type out the entire name. *Authn* and *authz* is just weird and only needed when your programming language has length restrictions on names.

## Choosing a common interface

We need a way to fetch the authenticated entity so we need to think of a good name. Commonly used interfaces are methods called `user`, `authenticated`, and `current_user`, sometimes their instance variable counterparts.

Which one of these is plain wrong? I would advice against using `@user` or `user`, because it carries semantic weight.

1. It suggests that only people can be signed in.
2. When you have a `UsersController`, which is the record operated on and which is the authenticated?
3. It reminds me of drug (ab)users.

Please don't use `me`, it might trigger an existential breakdown in yourself or other programmers.

I also wouldn’t recommend using an instance variable in a more complex application, it forces you to use callbacks (e.g. `before_action`) to set the value.

Contact me if you want to hear a long rant about (the misuse of) callback chains.

I’ve seen applications use a mix of instance variable (i.e. `@current_user`) and an accessor method (i.e. `current_user`). This was possible because the method memoized into the instance variable. This is a side effect of the code and should never be expected!

# Defining your accessor

Methods allow you to abstract fetching of the authenticated model and thus do lazy loading. It also simplifies overloading the behavior on controllers.

In the example below we override a method to allow the use of tokens through HTTP Basic Authentication on a controller which is just used by admins.

```
class ApplicationController
protected
  # Cookie based authentication (a SessionsController sets cookie)
  def authentication_token
    cookies['authentication_token']
  end

  def authentication_session
    AuthenticationSession.valid.find_by(
      token: authentication_token
    )
  end

  def current_user
    @current_user ||= authentication_session.try(:user)
  end
end

class Admin::AccountsController < ApplicationController
protected
  # HTTP Basic Authentication with x:auth-enti-cati-iont-oken.
  def authentication_token
    token, options = ActionController::HttpAuthentication::Token.
        token_and_options(request)
    token
  end
end
```

A lot of Rails plugins seem to like using a method called `current_user`. I’m mostly alright with this name when your authenticated model is named `User` and it actually returns an instance of that model.

If you’re not using a `User` model might want to consider naming it something more fitting like `current_account`.

In some cases a session is created to represent the authentication person indirectly. Think OAuth or an administrator impersonating another user.

In the impersonating case you might want `current_user` to return the represented user and not the connected client or administrator. You could consider something like this:

```
def current_user
  if target = authentication_session.target
    case target
    when Client, Administrator
      target.represented_user
    when User
      target
    end
  end
end
```

I personally like the name `authenticated` because it allows you to have a more flexible authorization system (but that’s a discussion for another day).

The `authenticated` method would return `authentication_session.target` which could be a `User`, `Consumer`, `Client`, `Administrator`, or something totally different like a string with a name `"John"`. This is naturally complementary to also defining `current_user`.

For consistency this naming scheme should be used for values which are extracted from the `current_user` as well.

```
def current_organization
  current_user.try(:organization)
end
```

# Authentication sessions

You may have already spotted it in the code examples; model your authentication sessions as a separate record.

With an authentication session you can authenticate a person multiple times on multiple systems and for different purposes while still allowing complete control over each individual session.

Let’s imagine John is signed in with his laptop and phone. Now he wants to sign in with his desktop, but he forgot his password.

We create a new authentication session with the ‘password reset’ purpose and possibly a different validation length and send the token for this to his e-mail address. He uses the token to reset his password.

Now we can present John with an option to sign out all the other devices. We can just do this by trashing all his authentication sessions. This would not have been possible if we would have stored his user ID in an (encrypted) cookie instead of using a session.

Other neat possible features include API token authentication through the same mechanism, annotating sessions with IP address and browser or device identification, and explicit naming of authentication sessions when used for longer periods of time.

This solution also aligns really well with how OAuth works so we’ve potentially already simplified a possible future OAuth implementation as well.

# Using authentication Gems

I personally don’t like Gems for code that is close to business logic and messes with the database. It tends to either be too generic or too restrictive.

When it’s too restrictive you end up working around limitations in an ugly way or throwing away the gem after a few months and implementing something yourself anyway.

When it’s too generic you end up reading a lot of documentation and code to get it dialed in right. You will need to redo this process every time you upgrade to make sure your app is still safe. After a year or so you could have implemented your own code in less time.

I’m not exaggerating when I say that all applications I reviewed which used a Gem for authentication were less secure than possible with that Gem. Some even had pretty nasty security problems because of it.

One application used the default salt of the Gem instead of the per-user stored salt because it was configured improperly. Another application added an authentication method next to the Gem’s which caused authentication to be turned off entirely when the Gem was updated without anyone noticing for quite a while.

So what’s the verdict?

You can use Gems for authentication, but please make sure you have proper full-stack regression tests in place and do regular security audits.

Be prepared to pay technical debt when things suddenly fall apart after an upgrade or when you run into limitations.

# And then what?

We haven’t even discussed storing credentials, receiving credentials, and 2-factor authentication. Don’t worry, a lot of smart people have written about these subjects and search engines are your friend.
