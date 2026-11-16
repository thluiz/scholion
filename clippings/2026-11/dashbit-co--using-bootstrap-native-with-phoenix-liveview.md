---
url: "https://dashbit.co/blog/using-bootstrap-native-with-live-view"
captured_at: "2026-11-16T03:32:16+00:00"
title: "Using Bootstrap Native with Phoenix LiveView"
domain: "dashbit-co"
---

*   José Valim
*   June 16th, 2020
*   [bootstrap](https://dashbit.co/blog/tags/bootstrap) , [forms](https://dashbit.co/blog/tags/forms) , [phoenix](https://dashbit.co/blog/tags/phoenix)

Over the last months we have been working on a LiveView app and we have decided to use [Bootstrap](https://getbootstrap.com/) with it. While Bootstrap is mostly focused on CSS, it does have some components that rely on JavaScript. In this article, we will cover how to make Bootstrap and LiveView work side by side. These steps may be applicable with other front-end frameworks too. We will be using Bootstrap to handle animations that depend only on the front-end, such as a dropdown, while everything else is powered by LiveView.

## Bootstrap Native

While Bootstrap does ship with JavaScript components, Bootstrap also adds a dependency on jQuery and other libraries. However, since most of our app is powered by LiveView, we thought bringing jQuery as a whole would be an overkill. That’s why we were really glad to find the [Bootstrap Native](https://thednp.github.io/bootstrap.native/) project, which implements the Bootstrap components in vanilla JavaScript.

> UPDATE #1: this post was written for Bootstrap v4. Bootstrap v5 does away with the jQuery dependency. Hooray! Regardless of your chouce, you will still need the steps below (or similar) to make Bootstrap and LiveView work together.

### Configuring Webpack

We will have to install Bootstrap, Bootstrap Native, and, since we are using Webpack, the Bootstrap Native loader. Let’s do that:

```
$ cd assets
$ npm install --save bootstrap bootstrap.native
$ npm install --save-dev bootstrap.native-loader
```

Now open up `assets/webpack.config.js`. Under the `module.rules` key, we will add a new entry at the top to load bootstrap native:

```
{
  test: /bootstrap\.native/,
  use: {
    loader: 'bootstrap.native-loader',
    options: {
      only: ['collapse', 'dropdown', 'tooltip']
    }
  }
},
```

We are passing the `only` option to explicitly control which components we want to load. See [the loader docs](https://github.com/fleck/bootstrap.native-loader) for more information. Remove the option if you would rather load everything and not worry about it.

Now open up `assets/css/app.scss` and load Bootstrap’ CSS:

```
@import "~bootstrap/scss/bootstrap";
```

And open up `assets/js/app.js` to load Bootstrap Native’s JavaScript:

```
import "bootstrap.native"
```

> Note: this article assumes your app was generated with Phoenix v1.5, which has a SCSS/SASS loader already configured. Bootstrap requires it to work. If you don’t have it installed, you can find many tutorials online with the precise steps.

## Configuring LiveView

Since LiveView dynamically injects content on the page, we need to tell Bootstrap Native to reapply its JavaScript hooks whenever new content is added to the page. This is very important. If you don’t do this, any Bootstrap component dynamically added to the page won’t work as expected.

Back to your `assets/js/app.js`, make sure you have this:

```
window.addEventListener("phx:page-loading-stop", info => {
  BSN.initCallback(document.body)
  NProgress.done()
})
```

And that’s it! Before we go, here are some useful tips that we have learned.

## Protip #1: Mouse events and `phx-update=ignore`

For content that appears and disappears on the page based on mouse events, such as a dropdown, make sure to add the `phx-update="ignore"` attribute to its root, like this:

```
<div class="collapse navbar-collapse" id="orgnav" phx-update="ignore">
  <ul class="navbar-nav">
```

Without this attribute, if you are using the dropdown and LiveView updates the page, the dropdown will close - as the dropdown is only opened on the client and not the server. `phx-update="ignore"` tells the LiveView client to not touch it.

## Protip #2: Forms with `phx-feedback-for`

We use LiveView to provide dynamic input validation as users fill in the form. With Bootstrap, you can provide this feedback to users by annotating the input with the `is-valid` or `is-invalid` classes. If the input has `is-valid`, it is contoured in green, and in red for `is-invalid`. Your markup would typically look like this:

```
<div class="form-group">
  <label for="user_email">E-mail</label>
  <input type="text" class="form-control is-valid" id="user_email" placeholder="E-mail">
  <div class="invalid-feedback">can't be blank</div>
</div>
```

Note it also has a `div` with class `invalid-feedback` for showing error messages.

However we only want to color a given input and show its error messages when the user effectively typed something in that particular input. LiveView controls this by using the `phx-feedback-for` attribute. `phx-feedback-for` must point to an input `id`. If the input has not been focused yet, a `phx-no-feedback` class is added to the element with the `phx-feedback-for` annotation. This allows you to hide or undo any user feedback until the input is used. In our app, we added `phx-feedback-for` to the wrapping `div`:

```
<div class="form-group" phx-feedback-for="user_email">
```

Now we added the following rules to our CSS

```
.phx-no-feedback .invalid-feedback, .phx-no-feedback .valid-feedback {
  display: none;
}

.phx-no-feedback input {
  border-color: #dee2e6 !important;
  padding-right: 0 !important;
  background-image: none !important;
}
```

In a nutshell, we hide the feedback classes, and remove any color from the input. Once the input is used, LiveView removes the `phx-no-feedback` class from the wrapping `div`, showing errors messages and giving visual feedback to the user.

At this point, it is worth mentioning our whole `input` generation is guided by a single `input` function. For example, our organization creation form looks like this:

```
<%= f = form_for @changeset, "#",
          id: "form-org",
          phx_target: @myself,
          phx_change: "validate",
          phx_submit: "save" %>
  <%= input f, :name %>
  <%= input f, :slug %>
  <%= input f, :address %>
  <%= submit("Submit", phx_disable_with: "Submitting...") %>
</form>
```

We have written about how to implement such `input` function in [a previous article about Dynamic Forms in Phoenix](https://dashbit.co/blog/dynamic-forms-with-phoenix).

## Protip #3: Live Bootstrap modals

When you scaffold your a `live` resource with `phx.gen.live`, Phoenix generates a `ModalComponent` for you. However, you may now want your modals to be styled with Bootstrap. We have achieved this in our apps by introducing a `live-modal` class, an alternative to Bootstrap’s `modal` class, to be used at top of your modal. Our `ModalComponent` now looks like this:

```
<div id="<%= @id %>" class="live-modal" tabindex="-1"
      phx-capture-click="close"
      phx-window-keydown="close"
      phx-key="escape"
      phx-target="<%= @myself %>"
      phx-page-loading>

  <div class="modal-dialog modal-lg" role="document">
    <div class="modal-content">
      <%= live_patch raw("&times;"), to: @return_to, class: "close" %>
      <%= live_component @socket, @component, @opts %>
    </div>
  </div>
</div>
```

Inside the modal itself, we simply use the remaining Bootstrap classes for modals. Finally, we added this bit of CSS, based on Phoenix’ modal:

```
.live-modal {
  opacity: 1 !important;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgb(0,0,0);
  background-color: rgba(0,0,0,0.4);
}

.live-modal .modal-title {
  margin-top: 0;
}

.live-modal .close {
  position: absolute;
  right: 1rem;
  top: 1rem;
}
```

## Summary

In this article, we followed the basic steps for using Bootstrap Native with LiveView. We have also shared some tips on how to fully integrate many Bootstrap components with your LiveView application, so everything just works™.
