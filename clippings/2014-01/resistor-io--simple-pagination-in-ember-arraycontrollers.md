---
url: "http://resistor.io/blog/2013/10/01/simple-pagination-in-ember-arraycontrollers/"
captured_at: "2014-01-12T14:08:23-03:00"
title: "Simple pagination in Ember ArrayControllers - Resistor"
domain: "resistor-io"
---

# **S**imple Pagination in Ember ArrayControllers

One of the projects that I have been working on recently had a (fairly common)
requirement to paginate a list of news items. The original controller and route
looked something like this:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` App.NewsController = Em.ArrayController.extend   sortProperties: ['postedAt']   sortAscending:  false  App.NewsRoute      = Em.Route.extend   model: ->     @modelFor('currentUser').get('news') ``` |

This is pretty simple, and it’s obviously making use of `Ember.SortableMixin`
to sort each news item in reverse chronological order**.**

So the first thing we need is a two properties which will specify the current
page and the number of items to show per page:

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` App.NewsController = Em.ArrayController.extend   # ...   page:           1   perPage:        25 ``` |

Straight forward enough**.** Now we need a computed property that contains only
the news items for the current page:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` App.NewsController = Em.ArrayController.extend   # ...   paginatedContent: (->     page    = @get('page')     perPage = @get('perPage')     start   = (page - 1 ) * perPage     end     = page * perPage     @get('content').slice(start, end)   ).property('content.[]', 'page', 'perPage') ``` |

But wait, what’s happenned here**?** We’ve lost our sorting! A quick read of
[the `Em.SortableMixin` source](https://github.com/emberjs/ember.js/blob/v1.0.0/packages/ember-runtime/lib/mixins/sortable.js#L8)
shows us that the property `arrangedContent` is where the sorted contents of
our controller are stored, so let’s change our code to use that property instead:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` App.NewsController = Em.ArrayController.extend   # ...   paginatedContent: (->     page    = @get('page')     perPage = @get('perPage')     start   = (page - 1 ) * perPage     end     = page * perPage     @get('arrangedContent').slice(start, end)   ).property('arrangedContent.[]', 'page', 'perPage') ``` |

In order to build our pagination links, we probably want to know how many pages
are available also, so let’s add a `pages` property:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` App.NewsController = Em.ArrayController.extend   # ...   pages: (->     result = parseInt(@get('content.length') / @get('perPage'))     ++result if @get('content.length') % @get('perPage') > 0     result   ).property('content.[]', 'perPage') ``` |

“But James**!**” you cry, “you forgot to depend on `arrangedContent`**.**” Nope.
The number of items doesn’t change when the sort order changes, so we forgo
the cost of recalculating the number of pages if the controller changes the
sort order**.**

This is pretty cool, but let’s extract this into a mixin so that we can re-use
this in other ArrayControllers:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``` | ``` App.PaginatableMixin = Em.Mixin.create   paginatedContent: (->     page    = @get('page')     perPage = @get('perPage')     start   = (page - 1 ) * perPage     end     = page * perPage     @get('arrangedContent').slice(start, end)   ).property('arrangedContent.[]', 'page', 'perPage')    pages: (->     result = parseInt(@get('content.length') / @get('perPage'))     ++result if @get('content.length') % @get('perPage') > 0     result   ).property('content.[]', 'perPage')  App.NewsController = Em.ArrayController.extend App.PaginatableMixin,   sortProperties: ['postedAt']   sortAscending:  false   page:           1   perPage:        25 ``` |

One thing to note about the `paginatedContent` property is that it might not
be very performant on very large collections - because it creates a new array
every time the original `content` is changed**.** That’s because we’re creating a
simple `Ember.computed` instead of an `Ember.arrayComputed` to handle adding
and removing elements without iterating the entire collection**.** This
functionality will be appearing (alongside a handy `paginate()` function) soon in
an updated version of [ember-enumerology](https://github.com/jamesotron/ember-enumerology) 
as a result of a bunch of peer-coding with [David J. Hamilton](https://twitter.com/hjdivad) **.**
Thanks David!

So now we have our pagination taken care of, we need to show our pagination
links**.** This is an excellent use-case for [Ember’s Components](http://emberjs.com/guides/components/) **.**

Let’s start by creating a `pagination-links` component, to house all our
controls**.** First a template using simple Bootstrap controls
(`templates/components/pagination-links.handlebars`):

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ``` | ``` {{# if showPagination}}   <div class="pagination pagination-centered">     <ul>       <li {{bind-attr class="hasPrevious::disabled"}}>         <a {{action goToPreviousPage}}>«</a>       </li>       {{#if showBeforeEllipsis}}         {{pagination-page page=1 currentPage=page}}         <li class="disabled"><a>…</a></li>       {{/if}}       {{#each pageNumber in visiblePages}}         {{pagination-page page=pageNumber currentPage=page}}       {{/each}}       {{#if showAfterEllipsis}}         <li class="disabled"><a>…</a></li>         {{pagination-page page=lastPage currentPage=page}}       {{/if}}       <li {{bind-attr class="hasNext::disabled"}}>         <a {{action goToNextPage}}>           »         </a>     </ul>   </div> {{/if}} ``` |

So, this is pretty straight forward, and we’ve discovered that in order to dry
up our template we need an additional component, which I’ve called
`pagination-page`**.**

> At this point I’d like to point out the fact that Ember requires you to
> to have at least one `-` in the name of your component, thus we have a
> component named `pagination-links` instead of just `paginate`**.**

Our `pagination-page` template looks pretty simple:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` <a {{action pageClicked}}>{{page}}</a> ``` |

Wait, where’s the `<li>`**?** We’ll tell our component to call itself `li` instead
of `div` as having spurious `div`s lying around will interfere with Bootstrap’s
CSS**.**

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` App.PaginationPageComponent = Em.Component.extend   isCurrent: (-> @get('currentPage') == @get('page')).property('currentPage', 'page')   tagName: 'li'   classNameBindings: 'isCurrent:disabled' ``` |

So now our `pagination-page` component will appear inside an `li` tag, with a
class of `disabled` if the page we’re linking to is the current page**.**

> Actions triggered on a component do not bubble up**.** This makes sense from
> a certain point of view (in that components are actually just views with
> a little sugar on top), however this certainly violated the principle of
> least surprise for me**.**

Since actions don’t bubble from within components, my initial plan of leaving
the `pageClicked` action to the `PaginationLinksComponent` to deal with won’t
work**.** So we need to teach the `PaginationPageComponent` how to deal with it:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` App.PaginationPageComponent = Em.Component.extend   #...   actions:     pageClicked: ->       @get('parentView').send('goToPage', @get('page')) ``` |

The trick here is that the enclosing component (in this case `pagination-links`)
is really the `parentView` of our component, we can call `send` on it to send
an action**.**

Next lets start implmenting our `PaginationLinksComponent`**.** Let’s start by
doing the simplest properties first:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` App.PaginationLinksComponent = Em.Component.extend   hasPrevious:    (-> @get('page') > 1).property('page')   hasNext:        (-> @get('page') + 1 < @get('pages')).property('page', 'pages')   showPagination: Em.computed.gt('pages', 1)   lastPage:       Em.computed.alias('pages') ``` |

This is pretty cool**.** What about `visiblePages`**?** This is a slightly complicated
function, it needs to:

1. If there are more than five pages, then only show five pages to link to**.**
2. If there are less than five pages, then only show the pages there are**.**
3. Center the list of pages around the current page, unless that would show
   negative page numbers, or numbers greater than the total number of pages**.**

Let’s give this a go:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``` | ``` App.PaginationLinksComponent = Em.Component.extend   # ...   visiblePages: (->     pages = @get('pages')     page  = @get('page')      # limit the number of pages to five, or the number of pages     # if that is smaller.     limit = 5     limit = pages if pages < 5      # function to calculate the last page given a start position     # and a limit     finish   = (start,limit)-> start + limit - 1      # start at page - half the limit     start = page - parseInt(limit / 2)     # if that puts the last page shown as greater than the number     # of pages, then move it back to the first start point that     # doesn't cause an overrun.     start = pages - limit + 1 if finish(start,limit) > pages     # force start to the first page if the start is less than 1.     start = 1 if start < 1      [start..finish(start,limit)]   ).property('page', 'pages') ``` |

The only other properties we need now are our `show{Before,After}Ellipsis`
properties**.** These are pretty straight forward now that we know which pages
are being shown:

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` App.PaginationLinksComponent = Em.Component.extend   # ...   showBeforeElipsis: (-> @get('visiblePages.firstObject') > 3).property('visiblePages.[]')   showAfterElipsis:  (-> Math.abs(@get('lastPage') - @get('visiblePages.lastObject')) > 2).property('visiblePages.[]', 'lastPage') ``` |

Cool, now we can insert our `pagination-links` component into our news template:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` {{#each newsItem in paginatedContent}}   {{render news newsItem}} {{/each}}  {{pagination-links page=page pages=pages}} ``` |

Lastly, we need to add actions to our `PaginationLinksComponent`:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 ``` | ``` App.PaginationLinksComponent = Em.Component.extend   # ...   actions:     goToNextPage: ->       @incrementProperty('controller.page') if @get('hasNext')      goToPreviousPage: ->       @decrementProperty('controller.page') if @get('hasPrevious')      goToPage: (pageNumber)->       @set('controller.page', pageNumber) if pageNumber >= 1 && pageNumber <= @get('lastPage') ``` |

> A note on performance: loading a large collection from your server into the
> client as JSON isn’t going to be terribly performant, and because we’ve not
> used `arrayComputed` Ember isn’t able to show incremental results as that
> data streams in**.** This solution works fine for smaller datasets, but when the
> amount of data grows you will need to look at ways of loading the data in a
> paginated way also**.** This should be do-able without rewriting any of our
> pagination code**.**

Well, we’ve come to the end of our little exploration of building pagination
with Ember**.** There’s been a couple of niggles along the way, but we got there**.**
I hope this comes in handy to others, and I’d love to read any comments you
may have**.**
