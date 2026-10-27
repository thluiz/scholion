---
url: "http://www.ramavadakattu.com/top-10-tips-to-a-new-django-developer"
captured_at: "2012-12-19T22:36:38-03:00"
title: "Top 10 tips to a new django developer - Move On"
domain: "ramavadakattu-com"
---

# [Top 10 tips to a new django developer](http://www.ramavadakattu.com/top-10-tips-to-a-new-django-developer "Permalink")

1.Don’t put project name  in the imports

For example suppose say you have an app **“xyz”** in  the project say **“project3”** then don’t say

```
1: from project3.xyz.models import Author
```

It ties the project name to your app which has several disadvantages like

1.You can’t easily reuse the app**.**

2.In future if you want to change the project name it becomes difficult**.**

Instead do this.

```
1: from xyz.models import Author
```

You can write the above statement as the django project is there on the  python path**.**

# 2.Don’t hard code MEDIA\_ROOT and TEMPLATE\_DIRS

In settings**.**py don’t write **MEDIA\_ROOT** and **TEMPLATE\_DIRS** as below

```
1: TEMPLATE_DIRS = ( "/home/html/project/templates",)
```

```
2: MEDIA_ROOT = "/home/html/project/appmedia/"
```

The above will cause problem when you move your project to deployment servers (changing from one server to another server) , changing from one OS to another OS  as you need to take of proper directory structure**.**

By following the below technique  you can easily avoid the above problems

```
1: SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
```

```
2: MEDIA_ROOT = os.path.join(SITE_ROOT, 'appmedia')
```

```
3: TEMPLATE_DIRS = ( os.path.join(SITE_ROOT, 'templates'),)
```

This technique which  i have learned from [Rob Hudson](http://rob.cogit8.org/blog/)  and more details you can find at the below link:

<http://rob.cogit8.org/blog/2009/May/05/django-and-relativity-updated/>

# 3.Don’t hard code static files in your templates**.**

What i mean by above is :

When you want to link static files like (java script  files,css files,images) don’t do the below

( Let us assume that MEDIA\_URL is “/appmedia/” )

```
1: <link rel="stylesheet" type="text/css" href="/appmedia/wysiwyg/jHtmlArea.css" />
```

```
2: <script type="text/javascript" src="/appmedia/wysiwyg/jHtmlArea.js"></script>
```

```
3: <script type="text/javascript" src="/appmedia/scripts/editor.js"></script>
```

```
4: <script type="text/javascript" src="/appmedia/scripts/comments.js"></script>
```

```
5: <script type="text/javascript" src="/appmedia/scripts/voting.js"></script>
```

The problem with above approach  is say, suppose if you want to server static content via another server (or) with amazon S3 from now let us  say from (<http://cdn.xyz.com/>)  then you need to rewrite every template replacing  **“/appmedia/” with   <http://cdn.xyz.com> Ah………… so tedious**.****

You can eliminate the above tedious process by following the simple technique**.**(i**.**e) Use the  context variable **{{MEDIA\_URL}}** instead of hard coding as **“/appmedia/”** as below

```
1: <link rel="stylesheet" type="text/css" href="{{ MEDIA_URL }}wysiwyg/jHtmlArea.css" />
```

```
2: <script type="text/javascript" src="{{ MEDIA_URL }}wysiwyg/jHtmlArea.js"></script>
```

```
3: <script type="text/javascript" src="{{ MEDIA_URL }}scripts/editor.js"></script>
```

```
4:
```

```
5: <script type="text/javascript" src="{{ MEDIA_URL }}scripts/comments.js"></script>
```

```
6: <script type="text/javascript" src="{{ MEDIA_URL }}scripts/voting.js"></script>
```

Using the above approach when you change the  MEDIA\_URL from “/appmedia/” to “<http://cdn.xyz.com/>”**.**It is  automatically reflected in all templates**.**No tedious process to changing all the templates.

**How do we get the Context variable**?****

Very simple.You can pass various useful context variables (like user,requested page)  to templates by adding  RequestContext(request)  to render\_to\_response as below

```
1: return render_to_response("my_app/my_template.html", {'some_var': 'foo'},
```

```
2: context_instance=RequestContext(request))
```

##### More details:

[http://www**.**b-list.org/weblog/2006/jun/14/django-tips-template-context-processors/](http://www.b-list.org/weblog/2006/jun/14/django-tips-template-context-processors/)

# 4.Don’t write core business logic in your views **!**

It is really not a good idea to put down your core business logic  into the views (suppose say logic for adding P amount from bank X and removing P  amount from bank Y)**.**

**Why?**

1. We can’t  unit test the code**.**
2. We can’t  reuse the code.

**Then where to put**?****

Putting down in models or in an helper function is a good idea**.**

**What about very basic logic**?****

I think we can put very basic stuff like retrieving an object (of some model) ,fetching and passing a list etc…**.** into the views.

# 5**.**It is tedious to change DEBUG=False (settings.py) when moving to production server

Often we forget to change DEBUG to False when we move from local environment to production environment**.** (Changing DEBUG = False has many benefits ).And it is tedious**.**

The simple technique to deal with the above is to check the hostname and then set the DEBUG variable as below **.**

```
1: import socket
```

```
2:
```

```
3: if socket.gethostname() == 'productionserver.com':
```

```
4: DEBUG = False
```

```
5: else:
```

```
6: DEBUG = True
```

It is first pointed out by [Jokull](http://www.solberg.is/blogg/)

Moredetails at the below link:

<http://nicksergeant.com/blog/django/automatically-setting-debug-your-django-app-based-server-hostname>

Other technique is to use different settings file (with DEBUG =True) for the local environment as below**.**

```
1: #Filename settings_debuy.py
```

```
2: #It contains all variables from settings and it overrides the DEBUG variable to True
```

```
3: #we use settings_debug.py to run the server locally python manage.py runserver settings=settings_debug.py
```

```
4:
```

```
5: from settings import *
```

```
6: DEBUG = True
```

```
7:
```

```
8: #you can also add other things which helps you to do the debugging easily
```

```
9: #like Debug toolbar etc...
```

```
10:
```

More details :

<http://blog.dpeepul.com/2009/07/02/from-now-you-will-never-forget-to-put-debug-true-in-django-production-environment/>

# 6.Load template tags  belonging to third party apps  only once

Before using  the template tags in a template from  third party apps we need to do

```
1: {% load template_tags %}
```

We need to do the above for every template  in which we need to use the third party template tags**.**It violates the DRY principle**.**We fix this by using the below code…………….

```
1: from django import template
```

```
2: template.add_to_builtins('project.app.templatetags.custom_tag_module')
```

Just put the above code in any file which automatically loads at the start like (settings**.**py,urls.py,every app models**.**py).

The above code loads the template tags at the start and you can use the template tags in any templates without using the code  {% load template\_tags %}

# 7.Urls**.**py

1.Don’t write all yours urls in project/urls**.**py

```
1: urlpatterns = patterns('',
```

```
2: url(r'^askalumini/question/$','.....registerInstitution',name='iregister'),
```

```
3: url(r'^askalumin/answer/$','someview.....',name='newmemberurl'),
```

```
4: url(r'^institution/member/$','someview.....',name="dashboardurl"),
```

```
5: url(r'^institution/faculty/$','editInstitute',name="editinstituteurl"),
```

```
6: url(r'^memeber/editprofile/$','editProfile',name="editprofileurl"),
```

```
7: url(r'^member/changepassword/$','changePassword',name="changepasswordurl"),
```

```
8: url(r'^member/forgotpassword/$','forgotPassword',name="forgotpasswordurl"),
```

```
9: url(r'^member/changepicture/$','changePicture',name="changepictureurl"),
```

```
10: url(r'^member/logout/$','memeberlogout',name="logouturl"), ,
```

```
11: )
```

Instead segregate across multiple apps like below (the below file  will go into project**.**/urls.py)**.****This helps to reuse the app for a different project without doing tedious modifications**.****

```
1:
```

```
2: urlpatterns = patterns('',
```

```
3: # Example:
```

```
4: (r'^$', include('institution.urls')),
```

```
5: (r'^institution/', include('institution.urls')),
```

```
6: (r'^askalumini/', include('askalumini.urls')),
```

```
7: (r'^member/', include('member.urls')),
```

```
8: )
```

and then create urls**.**py in every app and add the corresponding urls as below (sample is show for **askalumini** app)

```
1: urlpatterns = patterns('askalumini.views',
```

```
2: url(r'^$','askHome',name='askaluminiurl'),
```

```
3: url(r'^questions/(?P<questionno>\d+)/$','displayQuestion',name='askquestiondisplay'),
```

```
4: url(r'^askquestions/$','askQuestion',name='askquestionurl'),
```

```
5: url(r'^postcomment/$','postComment',name="askquestioncomment")
```

## Use URL function to define the URL

As you might have noticed we are using url function to define every url which allows us to name the url**.**In every url which we have defined above you can see the urlname at the last (like name=”**.**,…………”)**.** This name will help us in efficiently forming a url in views,templates and models  without hardcoding**.**

To maintain uniqueness in the names of urls across different apps just following the convention to name the url like “<apppname><somelabel>” (please see the above code)

## Don’t hardcode urls

Suppose if you change the url structure in  url**.**py you also need to apply the same change at all places where you have  hardcoded the url**.**(so tedious ………**.**)

#### In views.py

Instead of writing the hardcode url  as below

```
1: HttpResponseRedirect("/askalumini/questions/54")
```

use the reverse lookup function to form the url by means of urlname………**.**

```
1: from django.core.urlresolvers import reverse
```

```
2: HttpResponseRedirect(reverse('askquestiondisplay',kwargs={'questionno':q.id}))
```

#### In models**.**py

in models.py for forming absolute urls in addition to reverse lookup you can also use **models.permalink decorator** as below

```
1: @models.permalink
```

```
2: def get_absolute_url(self):
```

```
3: return ('profileurl2',(),{'userid': self.user.id})
```

The above decorator also uses the name to form a url**.**

#### In templates**.**py

By using a **url tag** you can also form a url by means of url name instead of hardcoding which has several serious disadvantages**.**

```
1: {% url askquestiondisplay 345 %}
```

```
2:  Ask Question
```

# 8.Debugging

a.Use  [django-debug-toolbar](http://github.com/robhudson/django-debug-toolbar/tree/master)  to find various information like

> **1.How many sql statements executed **?** Total time?**
>
> **2,.Template name , logging  ,cookie/session information etc………**.****

You can see the  full features of debug-toolbar at the below link

<http://github.com/robhudson/django-debug-toolbar/tree/master>

b.Use Werkzeug debugger which allows you to open python shell right on the error page.and which helps you to quickly debug the things**.**

See below link for more details.

<http://blog.dpeepul.com/2009/07/14/python-shell-right-on-the-django-error-page/>

c.Use **pdb** a powerful utility to debug things**.**

More details:

[http://ericholscher.com/blog/2008/aug/31/using-pdb-python-debugger-django-debugging-series-/](http://ericholscher.com/blog/2008/aug/31/using-pdb-python-debugger-django-debugging-series-/ "http://ericholscher.com/blog/2008/aug/31/using-pdb-python-debugger-django-debugging-series-/")

# 9.Know about pinax if possible use it**.**

One of the biggest advantage of using django is its ability to reuse the apps **.**Dj**ango is not geared towards monolithic design as other frameworks do**.** Django facilitates reusability.This is one of the important argument to use Django instead of other frameworks.And Pinax is one such fruit  of above design decision**.****

What is Pinax?

[![pinax](http://blog.dpeepul.com/wp-content/uploads/2009/08/pinax_thumb.jpg "pinax")](http://blog.dpeepul.com/wp-content/uploads/2009/08/pinax.jpg)

In the present day world every website require components like regisration,openid support,some kind groups/ tribes,user profiles etc…**.**.Almost every site has to code logic for these components**.** As they are reusable across many sites what if we have a platform (means a django project) which provides all these reusable components outof box and asks the developer to built on top of it.Such a platform help the developers to rapidly build the websites , it helps them to focus on core aspects of their site**.**

See the above diagram (especially 2nd one)  with pinax you only focuses on the cores aspects of app the common components are taken care by pinax hence you can develop the app very quickly**.**

Pinax is such a (django) platform which provides a collection of integrated reusable django apps.Out of box pinax provides several reusable components/apps like

1. openid support
2. contact import (from vCard, Google or Yahoo)
3. notification framework etc…More details at <http://pinaxproject.com/>

Pinax is powerful idea from [James Tauber](http://jtauber.com/) **.** Try to use this if you can which helps you to rapidly build a webapp**.**

More details you can find at the below link which i have written earlier:

<http://uswaretech.com/blog/2009/03/create-a-new-social-networking-site-in-few-hours-using-pinax-platform-django/>

# 10.Important third party apps to know

Various important third party of app to get you started:

**1.Migrations :**

What are (schema/data)  migrations**?**

you have done syncdb

At this time the structure of  models  is reflected in the database**.**

After some days/hours ……………..

you have to change some model structure like adding a field ,removing a field .And you have changed.Now the important question is how do you reflect those changes into the database.Some possible options are

> Doing the syncdb again**.** (tedious)
>
> Manually writing the alter database statements (tedious)

These movements of database from one state to another state is called migration.There are several third party apps which helps you to do this migrations like
> [django-evolutions](http://code.google.com/p/django-evolution/)  (easy to use, Automagically does every thing but is not robust)
>
> [South](http://south.aeracode.org/)  (is more robust but a bit of learning is needed)

**2.templates**

if you feel django template language is very restricted then  you can use the below

> 1**.** [template-utils](http://django-template-utils.googlecode.com/svn/trunk/docs/)  (enhances the template functionality with comparison template tags, other template utilities)
>
> 2**.** [Jinja](http://jinja.pocoo.org/2/)  (third party template system , which use same syntax as django template, which you can plugin to your Django project and it offers more flexibility and features in writing the template logic)

**3.Other third party apps**

**1**.** [django command extensions](http://code.google.com/p/django-command-extensions/)  which allows you do several helpful things via command line like**

> 1.shell\_plus : loads all the django models
>
> 2.runserver\_plus integrates with  Werkzeug  debugger
>
> 3.generating models graph to show it to your boss
>
> More detals at the below link:
>
> <http://ericholscher.com/blog/2008/sep/12/screencast-django-command-extensions/>

2**.**[Sorl](http://code.google.com/p/sorl-thumbnail/)  for generating thumbnails.

etc………………..

Other resources:

1**.**[http://stackoverflow.com/questions/550632/favorite-django-tips-features](http://stackoverflow.com/questions/550632/favorite-django-tips-features "http://stackoverflow.com/questions/550632/favorite-django-tips-features")

If you know any important  tips to a new django developers please let me know in comments**.**,
