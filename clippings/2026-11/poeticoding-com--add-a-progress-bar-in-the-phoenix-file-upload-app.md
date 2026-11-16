---
url: "https://poeticoding.com/add-a-progress-bar-in-the-phoenix-file-upload-app"
captured_at: "2026-11-16T04:15:41+00:00"
title: "Add a Progress Bar in the Phoenix File Upload app · Poeticoding"
domain: "poeticoding-com"
---

*   Part 1: [Step-by-Step Tutorial to Build a Phoenix App that Supports User Upload](https://poeticoding.com/step-by-step-tutorial-to-build-a-phoenix-app-that-supports-user-uploads/)
*   Part 2: [Creating Thumbnails of uploaded Images and PDF in Phoenix](https://poeticoding.com/creating-thumbnails-of-uploaded-images-and-pdf-in-phoenix/)
*   Part 3: this article

In the previous two parts we’ve seen how to create a Phoenix application with a multipart upload form, that creates thumbnails of images and PDF.

We select a file to upload and once uploaded we see it in the upload list with a thumbnail (if image or PDF). Since we are using it in localhost the upload is fast, even with large files.

But in a real world scenario the upload could take minutes (or even hours). We have to show a proper upload interface with a nice process bar.

To better follow this article, you can download the _part-2_ code at [poeticoding/phoenix\_uploads\_articles:part-2](https://github.com/poeticoding/phoenix_uploads_articles/tree/part-2).  
Once we have [started a Postgres server](https://poeticoding.com/step-by-step-tutorial-to-build-a-phoenix-app-that-supports-user-uploads/#postgres-docker) and [installed Imagemagick](https://poeticoding.com/creating-thumbnails-of-uploaded-images-and-pdf-in-phoenix/#imagemagick) (for thumbnails), we have an upload form that looks like this

![current upload form](https://poeticoding.com/add-a-progress-bar-in-the-phoenix-file-upload-app/0__initial_upload_form.jpg)

Current Upload Form

## Simulate slow connections with Chrome

With Chrome is possible to simulate a real case internet connection using throttling. You just need to open the Inspector, open the _Network conditions_ panel

![Chrome Network conditions](https://poeticoding.com/add-a-progress-bar-in-the-phoenix-file-upload-app/3__network_conditions.jpg)

Chrome Network conditions

and choose the throttling option you want, like _Slow 3G_. You can even add your custom throttling profile.

![Slow 3G Throttling](https://poeticoding.com/add-a-progress-bar-in-the-phoenix-file-upload-app/4__slow_3g.jpg)

Slow 3G Throttling

If you try to upload a file bigger than one megabyte, you’ll see that the interface is stuck, you wait … without knowing for how long.

At least the browser shows, on the bottom left, a small bar displaying the progress, but obviously it’s not enough for us and our app.

![Chrome progress bar](https://poeticoding.com/add-a-progress-bar-in-the-phoenix-file-upload-app/chrome_status_progress.png)

Chrome progress bar

To make a nice upload page we need to start playing a little bit with JavaScript and CSS.

## jQuery in Phoenix

There are great libraries out there that could do everything for us, like for example [DropzoneJS](https://www.dropzonejs.com/). But in this article I want to show you how, with JavaScript and the jQuery, we can take control of upload form events and build our progress bar.

So let’s start by adding [jQuery](https://jquery.com/) in our Phoenix app. The easiest way is to add `jquery` under _dependencies_ in `assets/package.json`

```
"dependencies": {
	...
	"jquery": "^3.4.1"
}
```

I’ve started recently to use [Visual Studio Code](https://code.visualstudio.com/) (before I was using [Sublime Text](https://www.sublimetext.com/)), which supports Elixir really well thanks to [ElixirLS](https://github.com/JakeBecker/elixir-ls). It has also a nice feature I’ve noticed while editing the `package.json` configuration file: when adding _jquery_ VS Code lists the packages available on [npmjs](https://www.npmjs.com/) and once selected _jquery_ it suggests the latest stable version. it’s a simple feature but a really helpful one.

![Visual Studio Code - package.json](https://poeticoding.com/add-a-progress-bar-in-the-phoenix-file-upload-app/5__jquery_autosuggestion.jpg)

Visual Studio Code - package.json

After adding this new dependency, we run `npm install` in the `assets/` directory, installing the missing packages which will be saved in the `assets/node_modules` folder.

Now, we create a new javascript file, `assets/js/upload.js` and we import it into `assets/js/app.js`. In this new _upload_ file we will write our JavaScript code that refers to the upload form.

```
// assets/js/app.js

import "phoenix_html"

import "./upload"
```

In this way `webpack`, which starts automatically in development with `mix phx.server`, includes the `upload.js` script in the `app.js` file served by Phoenix.

```
<body>
  ...
   <script type="text/javascript" src="/js/app.js"></script>
</body>
```

## Upload a file using jQuery and Ajax

Let’s now see how to submit the multipart form using jQuery, so we can monitor the upload’s progress with JavaScript.

At first we give an _id_ to the upload form to be able to easily refer to it with a jQuery selector. We find the form in `lib/poetic_web/templates/upload/new.html.eex`

```
<%= form_for @conn, Routes.upload_path(@conn, :create),
[multipart: true, id: "upload_form"], fn f-> %>
...
<% end %>
```

And then we focus on the `upload.js` file.

```
// assets/js/upload.js

import jQuery from "jquery"

jQuery(document).ready(function($){
    let $form = $("#upload_form");
    
    $form.submit(function(event){
        let formData = new FormData(this);
        startUpload(formData, $form);
        
        event.preventDefault();
    })
})
```

We start by importing `jQuery` and, when the document is loaded, we catch the form _submit_ event by passing a handler to the `submit` function.

Since we want to upload the file ourself using jQuery

*   we create a new [FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData), which we’ll use later
*   we pass `formData` to the `startUpload` function we are going to implement in a second
*   we also pass the `$form` jQuery object to `startUpload` - it will be useful later
*   at the end, we stop the form submission event with `event.preventDefault()`, so we can submit it ourself in the `startUpload` function.

Let’s see now the `startUpload` function

```
// assets/js/upload.js

function startUpload(formData, $form) {

    jQuery.ajax({
        type: 'POST',
        url: '/uploads',

        data: formData,
        processData: false, //IMPORTANT!

        cache: false,
        contentType: false,

        xhr: function () {
            let xhr = jQuery.ajaxSettings.xhr();
            if (xhr.upload) {
                
                xhr.upload.addEventListener(
                  'progress',handleProgressEvent, false
                );
			          
            }
            return xhr;
        },

        success: function (data) {
            console.log("SUCCESS", data)
        },

        error: function (data) {
            console.error(data);
        }
    })
}
```

We use the the `ajax` function to submit the form, making a `POST` request to `/uploads` path, sending `formData` to the server. To avoid any data transformation from jQuery it’s important to set `processData` to `false`.

The `xhr` parameter expects a callback function which creates and returns a [XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest) (XHR) object, used to make an HTTP request to the server. We pass a callback function which creates `xhr`, a XMLHttpRequest object, and with `xhr.upload.addEventListener(...)` we start listening to `progress` events, which are handled by `handleProgressEvent` function.

Almost there… last part before we are able to test this out. Let’s write a `handleProgressEvent` function that just prints the event.

```
// assets/js/upload.js
function handleProgressEvent(progressEvent) {
    console.log(progressEvent);
}
```

Let’s see what it’s printed when we upload a file. Remember to enable the throttling - with a slow connection you can see many more events printed on the console.

![ProgressEvent](https://poeticoding.com/add-a-progress-bar-in-the-phoenix-file-upload-app/6__console_ProgressEvent.jpg)

ProgressEvent

## Calculate and show the progress

The `ProgressEvent` object, passed to `handleProgressEvent()`, has everything we need to calculate the upload progress percentage.

```
ProgressEvent {
	total: 3698228,
	loaded: 49152
	...
}
```

`total` is the total file size (in byte) and `loaded` is the current uploaded size.

Let’s start with something simple showing in the upload page an HTML label with the progress percentage.

First, we need to add a label in the upload form in `new.html.eex` file

```
<%= form_for @conn, Routes.upload_path(@conn, :create), 
[multipart: true, id: "upload_form"], fn f-> %>

	<%= file_input f, :upload, class: "form-control" %>
	<%= submit "Upload", class: "btn btn-primary" %>

  <div class="upload-progress">
    <p>Upload progress: 
	    <label class="progress-percentage">0%</label>
    </p>
  </div>

<% end %>
```

Instead of using the selector `"#upload_form label.progress-percentage"` directly inside the `handleProgressEvent(e)` function, we define a new function called `createProgressHandler($form)` which accepts the form jQuery object and returns a handler function.

```
// assets/js/upload.js

function createProgressHandler($form) {
  let $label = $form.find("label.progress-percentage");

  return function handleProgressEvent(progressEvent) {
    let progress = progressEvent.loaded / progressEvent.total,
        percentage = progress * 100,
        percentageStr = `${percentage.toFixed(2)}%`;
            
    $label.text(percentageStr);
  }
}
```

In this way the handler function has access to `$label` and it’s able to update its text. The handler calculates the `progress` and updates the label text with the `percentageStr` string.

To make it work we need to also change a line in the `startUpload` function.

```
// assets/js/upload.js

function startUpload(formData, $form) {
  jQuery.ajax({
    ...
    xhr: function () {
      ...
      xhr.upload.addEventListener(
        'progress',		        
        createProgressHandler($form), 
        false
      );
    }
    ...
```

Instead of passing the handler function directly to `addEventListener`, we call `createProgressHandler($form)` which returns the handler function that will be called for each progress event.

Let’s try again to upload a file.

![Upload Progress](https://poeticoding.com/add-a-progress-bar-in-the-phoenix-file-upload-app/upload_progress_label.gif)

Upload Progress

🎉👩‍💻👨‍💻🎉

Great, it works! It’s not aesthetically pleasant, but at least it shows dynamically the upload’s progress.

You’ve maybe noticed that once reached 100%, the `success` callback is called printing the server response to the JavaScript console. This response is the upload list page HTML (`GET /uploads`). In our case, since we’ve receive the response via jQuery success callback, the browser isn’t redirected to`/uploads` and we just see a page with the progress stuck at 100%.

In general, it would be better to have an API that sends us a JSON response with the details of the created file - we could then show this data to confirm that the upload succeeded. For simplicity, in the case of success, we just ignore the data and redirect the browser to the uploads page.

```
// assets/js/upload.js

function startUpload(formData, $form) {
  ...
  jQuery.ajax({
    ...
    success: function (data) {
      window.location = "/uploads"
    },
    ...
  })
}
```

![Redirect after completion](https://poeticoding.com/add-a-progress-bar-in-the-phoenix-file-upload-app/7__page_redirect_on_success.gif)

Redirect after completion

## HTML5 progress bar

It’s now time to try to nicely show the progress with a progress bar. We can start using the `progress` HTML5 tag, without having to import any library.

```
<%= form_for @conn, Routes.upload_path(@conn, :create),
 [multipart: true, id: "upload_form"], fn f-> %>

	<%= file_input f, :upload, class: "form-control" %>
	<%= submit "Upload", class: "btn btn-primary" %>

    <div class="upload-progress">

        <progress max="100" value="0"></progress>

        <label class="progress-percentage"></label>
    </div>

<% end %>
```

By default, the result is a thin blue bar.

![HTM5 progress bar](https://poeticoding.com/add-a-progress-bar-in-the-phoenix-file-upload-app/8__html5_default_progress_bar.png)

HTM5 progress bar

I’m neither a front-end developer nor a CSS expert, but we can get a nicer progress bar just playing around with the bar’s CSS. We create a new [/assets/css/upload.css](https://github.com/poeticoding/phoenix_uploads_articles/blob/part-3_progress-bar/assets/css/upload.css) file adding the CSS below

```
/* assets/css/upload.css */

progress {
    position:relative;
    width: 100%;
    height: 25px;
    appearance: none;
    -webkit-appearance: none;
}

progress::-webkit-progress-bar {
    background-color: #eee;
    border-radius: 8px;
}

progress::-webkit-progress-value {
    background-color: #276bd1;
    border-radius: 8px;
}
```

We are able to customize size and colors using the `progress` element itself and some [CSS progress bar pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/::-webkit-progress-bar) (this code works on Chrome and Safari, to support Firefox and other browsers we’d need to add some extra CSS).

This progress bar doesn’t have an attribute to easily show a label at the center. But we can move our current label `label.progress-percentage` at the center of the bar.

```
/* assets/css/upload.css */

label.progress-percentage {
    position: absolute;
    top: 0;
    text-align: center;
    width: 100%;
    color: white;
    font-weight: bold;
    text-shadow: 1px 1px 1px #444;
}
```

Similarly to what we did for `upload.js`, we import it on `assets/css/app.css`

```
/* assets/css/app.css */

@import "./phoenix.css";

@import "./upload.css";
```

Adding the CSS `progress { display: none; }` hides the bar by default. We want to show the bar only when the upload starts. When the `startUpload(...)` JavaScript function is called, we show the progress bar.

```
// assets/js/upload.js

function startUpload(formData, $form) {
    let $progress = $form.find("progress");
    $progress.show()
    ...
}
```

We now need to amend the `createProgressHandler` and `handleProgressEvent` functions so they can update both the progress bar and the label.

```
// assets/js/upload.js

function createProgressHandler($form) {
    let $progress = $form.find("progress"),
        $label = $form.find("label.progress-percentage");

    return function handleProgressEvent(progressEvent) {
        let progress = progressEvent.loaded / progressEvent.total,
            percentage = progress * 100,
            percentageStr = `${percentage.toFixed(2)}%`; //xx.xx%
        
        $label.text(percentageStr)
        
        //PROGRESS BAR
        $progress
        .attr("max", progressEvent.total)
        .attr("value", progressEvent.loaded);
    }
}
```

As you can see, to update the progress bar we just need to set the `max` and `value` attributes, which are respectively _total size_ of the file and _current uploaded bytes_.

Time to see it in action!

![Fully working progress bar](https://poeticoding.com/add-a-progress-bar-in-the-phoenix-file-upload-app/9__final_progress_bar.gif)

Fully working progress bar

## Move the upload form

At the moment the upload form is in its own page `/uploads/new`. To have everything in the same place, we can move the form into the upload list page.

Instead of copying & pasting the code inside the upload list page, we remove the action `:new` from the routes and rename the template file `new.html.eex` to `upload_form.html.eex`.

We can now render the form into `templates/upload/index.html.eex`, using the `PoeticWeb.UploadView.render` function and passing the connection

```
<%= PoeticWeb.UploadView.render("upload_form.html", conn: @conn) %>

<table class="table">
  <thead>
    <th>Thumbnail</th>
    <th>ID</th>
    <th>Filename</th>
    <th>Size</th>
    <th>Type</th>
    <th>Time</th>
  </thead>
  <tbody>
  ...
```

![Upload form in upload list page](https://poeticoding.com/add-a-progress-bar-in-the-phoenix-file-upload-app/10__upload_form_index_page.jpg)

Upload form rendered in the upload list page

## File input and Upload button

An extra small change: it would be nice to have just one _Upload_ button to choose the file and, once the file is selected, to automatically start the upload.

We start by changing the `upload_form.html.eex` file, wrapping the `file_input` and a `button` inside a div with class `upload-btn-wrapper`. We also remove the `submit` button.

```
<%= form_for ... %>

  <div class="upload-btn-wrapper">
    <button class="btn btn-primary">Upload a file</button>
    <%= file_input f, :upload, class: "form-control" %>
  </div>

    ...
<% end %>
```

We add to `upload.css` some CSS specific to the wrapper, overlaying the _file input_ with the _button_.

```
.upload-btn-wrapper {
  position: relative;
  overflow: hidden;
  display: inline-block;
}
.upload-btn-wrapper input[type=file] {
  width: 100%;
  height: 100%;
  position: absolute;
  left: 0;
  top: 0;
  opacity: 0;
}
```

And we add in `upload.js` the JavaScript code to automatically start the upload once the file is selected.

```
// assets/js/upload.js

jQuery(document).ready(function ($) {
    let $form = $("#upload_form"),
        $fileInput = $form.find("input[type='file']");
    
    $form.submit(function (event) { ... }

    $fileInput.on("change", function (e) {
        $form.trigger("submit");
    });
});
```

![Upload form with progress bar](https://poeticoding.com/add-a-progress-bar-in-the-phoenix-file-upload-app/11_automatic_upload_small.gif)

Upload form with progress bar

## Wrap Up

If you want to try the code of this part, you find it on the GitHub repo [poeticoding/phoenix\_uploads\_articles:part-3\_progress-bar](https://github.com/poeticoding/phoenix_uploads_articles/tree/part-3_progress-bar).

In this article I preferred to use only jQuery, so we could interact ourself with the upload JavaScript events and understand the dynamics. But when building an application we can’t reinvent the wheel every time. There are a lot of great JavaScript libraries out there that can make our life easier.

If you want to bring the progress bar a step further, give a try to [progressbar.](https://kimmobrunfeldt.github.io/progressbar.js/)[j](https://kimmobrunfeldt.github.io/progressbar.js/)[s](https://kimmobrunfeldt.github.io/progressbar.js/) which is a JavaScript library that displays beautiful progress bars with different shapes, colors and animations. To use it, you just need to include it in the dependencies in `package.json` and import it in `upload.js`, like we did with jQuery.

[jQuery File Upload](https://blueimp.github.io/jQuery-File-Upload/) is a pretty famous JavaScript library (it has more than 30,000 stars on GitHub) which handles the upload and progress bar. It’s really well documented and it’s still maintained.

A library I mentioned at the beginning is [DropzoneJS](https://www.dropzonejs.com/). I haven’t played a lot with it yet, but it seems a great full-optional library. It creates a drop-zone box in the page where we can drag & drop our files - DropzoneJS will take care of the rest sending the file to the server and showing a nice UI with progress bar and thumbnails. With this library we can easily set the maximum file size, choose the supported file types, generate thumbnails on the client side and [many other things](https://www.dropzonejs.com/#configuration).
