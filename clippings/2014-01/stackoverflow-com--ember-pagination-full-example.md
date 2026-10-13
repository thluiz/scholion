---
url: "http://stackoverflow.com/questions/13008838/ember-pagination-full-example"
captured_at: "2014-01-12T14:07:03-03:00"
title: "ember.js - Ember pagination full example - Stack Overflow"
domain: "stackoverflow-com"
---

# **E**mber pagination full example

**The updated example below works with ember**.**js RC1** -- 03/14/2013

First you need to add a pagination like mixin as one doesn't yet exist in the ember core

```
var get = Ember.get, set = Ember.set;

Ember.PaginationMixin = Ember.Mixin.create({

  pages: function() {

    var availablePages = this.get('availablePages'),
    pages = [],
    page;

    for (i = 0; i < availablePages; i++) {
      page = i + 1;
      pages.push({ page_id: page.toString() });
    }

    return pages;

  }.property('availablePages'),

  currentPage: function() {

    return parseInt(this.get('selectedPage'), 10) || 1;

  }.property('selectedPage'),

  nextPage: function() {

    var nextPage = this.get('currentPage') + 1;
    var availablePages = this.get('availablePages');

    if (nextPage <= availablePages) {
        return Ember.Object.create({id: nextPage});
    }else{
        return Ember.Object.create({id: this.get('currentPage')});
    }

  }.property('currentPage', 'availablePages'),

  prevPage: function() {

    var prevPage = this.get('currentPage') - 1;

    if (prevPage > 0) {
        return Ember.Object.create({id: prevPage});
    }else{
        return Ember.Object.create({id: this.get('currentPage')});
    }

  }.property('currentPage'),

  availablePages: function() {

    return Math.ceil((this.get('content.length') / this.get('itemsPerPage')) || 1);

  }.property('content.length'),

  paginatedContent: function() {

    var selectedPage = this.get('selectedPage') || 1;
    var upperBound = (selectedPage * this.get('itemsPerPage'));
    var lowerBound = (selectedPage * this.get('itemsPerPage')) - this.get('itemsPerPage');
    var models = this.get('content');

    return models.slice(lowerBound, upperBound);

  }.property('selectedPage', 'content.@each')

});
```

Next you need to use the mixin above in your ArrayController like so

```
PersonApp.PersonController = Ember.ArrayController.extend(Ember.PaginationMixin, {  
    itemsPerPage: 2
});
```

Next you can add a simple helper view to display the page numbers as li tags

```
PersonApp.PaginationView = Ember.View.extend({
    templateName: 'pagination',
    tagName: 'li',

    page: function() {
        return Ember.Object.create({id: this.get('content.page_id')});
    }.property()
});
```

Your routes might look something like this (nested page under the parent)

```
PersonApp.Router.map(function(match) {
    this.resource("person", { path: "/" }, function() {
        this.route("page", { path: "/page/:page_id" });
    });
});

PersonApp.PersonPageRoute = Ember.Route.extend({
    model: function(params) {
        return Ember.Object.create({id: params.page_id});
    },
    setupController: function(controller, model) {
        this.controllerFor('person').set('selectedPage', model.get('id'));
    }
});

PersonApp.PersonRoute = Ember.Route.extend({
    model: function(params) {
        this.controllerFor('person').set('selectedPage', 1);
        return PersonApp.Person.find();
    }
});
```

And finally, you need to add some html to display it

```
<script type="text/x-handlebars" data-template-name="application">

  <div id="main">
    {{ outlet }}
  </div>

</script>

<script type="text/x-handlebars" data-template-name="person">

<table width="250px">                                                               
<thead>
<th>id</th>
<th>username</th>
</thead>
<tbody>
   {{#each person in controller.paginatedContent}}
    <tr>
      <td>{{person.id}}</td>
      <td>{{view Ember.TextField valueBinding="person.username"}}</td>
    </tr>
   {{/each}}
</tbody>
</table>

<div name="prev">{{#linkTo 'person.page' prevPage target="controller"}}Prev{{/linkTo}}</div>
<ul class="pagination gui-text">
  {{#each pages}}
    {{view PersonApp.PaginationView contentBinding="this"}}
  {{/each}}
</ul>
<div name="next">{{#linkTo 'person.page' nextPage target="controller"}}Next{{/linkTo}}</div>

</script>

<script type="text/x-handlebars" data-template-name="pagination">

{{#with view}}
{{#linkTo 'person.page' page}}
  {{content.page_id}}
{{/linkTo}}                                                                         
{{/with}}

</script>
```

Here is a full working project with this in action if you want to see it work

<https://github.com/toranb/ember-pagination-example>
