---
title: "Role-based authorization in Rails"
date: '2016-01-02T13:58:04-03:00'
category: webclip
summary: 'The post argues that CanCan makes permissions easy but encourages duplicated rules and repeated overrides, and presents Access Granted as a role-based alternative with inheritance, dynamic checks, and controller protection.'
tags: ["rails", "authorization", "cancan", "access-granted"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Role-based authorization in Rails"
    url: "http://blog.chaps.io/2015/11/13/role-based-authorization-in-rails.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-01/blog-chaps-io--role-based-authorization-in-rails.md"
    kind: repo
---

The post says CanCan was easy to adopt in Rails projects, but over time it led to duplicated permissions and repeated use of `cannot` to cancel earlier rules. Access Granted is introduced as a gem that adds role inheritance, prevents identical permissions inside one role, and keeps permission rules simpler.

## Reading notes

- CanCan was easy to use in new and existing Rails apps, but it left room for weak structure inside abilities.
- The author noticed duplicated permissions across roles, especially between members and guests, and says this becomes hard to maintain in larger apps.
- The author also points to `cannot` being used to override earlier permissions, sometimes several times in one check, which is described as inefficient and hard to debug.
- Access Granted is presented as a gem that supports roles and permission inheritance, keeps roles simple, and forbids identical permissions inside one role.
- The example forum app uses a hierarchy of moderator, registered user, and guest, with roles ordered from most permissive to least permissive.
- Roles are defined top to bottom, and each role can have a name plus an optional predicate that decides whether it applies to the current user.
- Permissions are declared inside role blocks with the same syntax as CanCan, which is meant to make migration easier.
- Guests can only read topics and posts.
- Members inherit from lower roles that apply to the user and add permissions such as creating posts and topics.
- Dynamic permissions can use blocks, such as allowing updates only when the post author matches the current user.
- Multiple actions can be listed in one rule, so update and destroy can share the same condition.
- Moderators can read, create, update, and destroy, and can also manage topics through the `:manage` shortcut.
- The author says native roles make permissions act like hash buckets and can be up to twice as fast as CanCan because Access Granted does not need to evaluate every `can` and `cannot` rule.
- Permission checks in controllers and views use `can?` and `cannot?`, including checks against instances.
- Sensitive controller actions should also call `authorize!`, not just hide buttons in the view.
- If access is denied, Access Granted raises `AccessGranted::AccessDenied`, which can be rescued in `ApplicationController` to redirect users with an error message.
- The same policies can be used outside Rails because they are plain Ruby objects that respond to `can?` and `cannot?`.
- The post ends by recommending migrating CanCan code to Access Granted and pointing readers to the GitHub repository and specs.
