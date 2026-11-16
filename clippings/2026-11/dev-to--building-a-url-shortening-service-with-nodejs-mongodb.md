---
url: "https://dev.to/olamideaboyeji/building-a-url-shortening-service-with-nodejs-and-mongobb-deploy-to-azure-oep"
captured_at: "2026-11-16T19:41:13+00:00"
title: "Building a URL shortening service with NodeJS and MongoDB. Deploy to Azure."
domain: "dev-to"
---

Hey there, we would be building a URL shortening service with NodeJS, Express, and MongoDB. We would then go ahead and deploy our web application to Azure. It would be code a along tutorial and I would be explaining each line of code.

Link to the demo and GitHub repository would be added at the end.

Excited right ?  
[![Excited](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fmedia0.giphy.com%2Fmedia%2FUO5elnTqo4vSg%2Fgiphy.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fmedia0.giphy.com%2Fmedia%2FUO5elnTqo4vSg%2Fgiphy.gif)

## [](#what-should-i-knowhave)What should I know/have

*   Basic understanding of HTML, CSS, and Javascript
*   Have NodeJS installed on your computer (install [here](https://nodejs.org/))
*   Have MongoDB installed on your computer (install [here](https://docs.mongodb.com/manual/installation/))
*   Experience creating GitHub repositories, and pushing your local repository to the remote one.

## [](#lets-get-started)Let's get started

First, let's create a folder for our application. We'd call it url-shortener.  
[![Mkdir && cd](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fres.cloudinary.com%2Folamideaboyeji%2Fimage%2Fupload%2Fv1586718081%2Fmkdir_tfdsgp.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fres.cloudinary.com%2Folamideaboyeji%2Fimage%2Fupload%2Fv1586718081%2Fmkdir_tfdsgp.png)

Then in the terminal run **npm init**.  
[![npm run init](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fres.cloudinary.com%2Folamideaboyeji%2Fimage%2Fupload%2Fv1586718082%2FnpmInit_d3cmvq.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fres.cloudinary.com%2Folamideaboyeji%2Fimage%2Fupload%2Fv1586718082%2FnpmInit_d3cmvq.png)  
This would create a package.json file for us.

Now let's install the packages we would be using.  
[![npm i](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fres.cloudinary.com%2Folamideaboyeji%2Fimage%2Fupload%2Fv1586718081%2FnpmIdeps_oeqvws.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fres.cloudinary.com%2Folamideaboyeji%2Fimage%2Fupload%2Fv1586718081%2FnpmIdeps_oeqvws.png)  
[![npm I dev](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fres.cloudinary.com%2Folamideaboyeji%2Fimage%2Fupload%2Fv1586718082%2FnpmIdevdeps_nuthgh.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fres.cloudinary.com%2Folamideaboyeji%2Fimage%2Fupload%2Fv1586718082%2FnpmIdevdeps_nuthgh.png)  
**express**: Node.js framework that provides a robust set of features for web and mobile applications.

**body-parser**: To parse incoming request bodies before your handlers.

**mongoose**: Mongoose is a MongoDB object modeling tool designed to work in an asynchronous environment.

**nodemon**: This is used to automatically restart our server, so we would not have to stop and restart the server each time we make a change. We are installing this as a dev dependency because we only need it in development.

When the installs are done, edit the main and scripts of your package.json to look like below.  

```
{
  "name" : "url-shortener",
  "version" : "1.0.0",
  "description" : "URL shotener web app",
  "main" : "server.js",
  "scripts" : {
    "dev" : "nodemon server.js",
    "start" : "node server.js"
  },
  "keywords" : ["URL", "shortener"],
  "author" : "Your name",
  "dependencies" : {
    "express" : "^4.17.1",
    "mongoose" : "^5.9.7",
    "body-parser" : "^1.19.0"
  },
  "devDependencies" : {
    "nodemon" : "^2.0.2"
  }
}
```

Enter fullscreen mode Exit fullscreen mode

## [](#front-end)Front end

We would be using a very basic UI.  
For the front end of the app, create a folder called public in our working directory. This is where we would have our front end files(HTML, CSS, and Javascript). Create files named index.html, style.css, and main.js in the public folder. The content of our index.html and style.css are shown below :

#### [](#indexhtml-)index.html :

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" 
              content="width=device-width, 
              initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <link rel="stylesheet" href="style.css">
        <title>URL shortener</title>
    </head>
    <body>
        <form id="url-form">
            <h1 class="header">URL SHORTENER</h1>
            <p class="desc">Shorten your long URL to 
             <span class="domain">mydomain.com</span>/unique_name
            </p>
            <p>
                <input required class="url-input" 
                id="original-url" type="url" 
                placeholder="paste original URL here">
            </p>
            <input disabled class="base-url" value="">
            <input required class="unique-input" id="unique-name" 
             type="text" placeholder="unique name">
            <p id='status'><button>SHORTEN</button></p>
            <p id="confirmationShow"></p>
        </form>
    </body>
    <script>
      const domain = window.location.host;
      document.querySelector('.domain').innerText = domain;
      document.querySelector('.base-url').value = domain;
    </script>
    <script src="main.js"></script>
</html>
```

Enter fullscreen mode Exit fullscreen mode

#### [](#stylecss-)style.css :

```
body{
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background : linear-gradient(to right, #aa5f15, #542008);
}
html, body {
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    overflow: hidden;
    height: 100%;
}
form{
    border: red;
    padding-top: 15vh
}
.a {
    color : white;
}
.header{
    color: bisque;
    letter-spacing: 3px;
    font-size: 3rem;
    margin-bottom: 1px;
}
.header span {
    font-style: italic;
}
.desc{
    margin-top :2px;
    color: bisque;
}
.base-url{
    padding: 10px;
    background-color: #a7a7a7;
    border-radius: 8px 0 0 8px;
    border: 1px solid black;
    width: 100px;
    font-weight: bold
}

.unique-input{
    padding: 10px;
    border-radius: 0 8px 8px 0;
    outline: none;
    border: 1px solid black;
}
.url-input{
    border-radius: 8px;
    padding: 10px;
    width: 300px;
    outline : none;
}

button{
    background-color: burlywood;
    padding: 10px;
    border-radius: 10px;
    outline: none;
    cursor: pointer;
}

#confirmationShow {
    font-style: italics;
}

.loader {
    border: 8px solid #f3f3f3;
    border-radius: 50%;
    border-top: 8px solid orange;
    width: 10px;
    height: 10px;
    -webkit-animation: spin 2s linear infinite;
    animation: spin 2s linear infinite;
    margin: 8px auto !important;
}

@-webkit-keyframes spin {
    0% { -webkit-transform: rotate(0deg); }
    100% { -webkit-transform: rotate(360deg); }
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}
```

Enter fullscreen mode Exit fullscreen mode

## [](#server)Server

Create a file server.js in the root directory. And add the following

#### [](#serverjs-)server.js :

```
//Import modules
const path = require('path');
const express = require('express');
const bodyParser = require('body-parser');

//Call the express function to initiate an express app
const app = express();

//This tells express to parse incoming requests
app.use(bodyParser.json());

//This tells express we are serving static files (front end files)
app.use(express.static(path.join(__dirname, 'public')));

/** NB: process.env.PORT is required as you would 
not be able to set the port manually in production */
const PORT = process.env.PORT || 3000;

//app to listen to specified port
app.listen(PORT, () => {
  console.log(`Server running on port${PORT}`);
});
```

Enter fullscreen mode Exit fullscreen mode

###### [](#note-that-path-is-an-inbuilt-node-module-and-does-not-need-to-be-installed)Note that _path_ is an inbuilt node module and does not need to be installed

In the terminal, run _npm run dev_.  
You should see this  
[![terminalResult](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fres.cloudinary.com%2Folamideaboyeji%2Fimage%2Fupload%2Fv1586718082%2FnpmRunDev_t4eywd.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fres.cloudinary.com%2Folamideaboyeji%2Fimage%2Fupload%2Fv1586718082%2FnpmRunDev_t4eywd.png)

Open your browser and go to [http://localhost:3000](http://localhost:3000/). This should show up.  
[![FrontEnd](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fres.cloudinary.com%2Folamideaboyeji%2Fimage%2Fupload%2Fv1586718081%2FhomePageLoaded_g6p4zc.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fres.cloudinary.com%2Folamideaboyeji%2Fimage%2Fupload%2Fv1586718081%2FhomePageLoaded_g6p4zc.png)

_Yayy, our public page is being served._

### [](#now-to-the-next-part)Now to the next part

## [](#lets-connect-to-our-mongodb)Let's connect to our MongoDB

Create a file called db.js in the root directory, and put this in it.

#### [](#dbjs-)db.js :

```
//import mongoose library
const mongoose = require('mongoose');

//MONGO_URI 
const MONGO_URI = process.env.MONGO_URI || 'mongodb://localhost:27017/url'; 

//Connect to DB function
const connect = () => {
  mongoose.connect(MONGO_URI, {useNewUrlParser : true, useUnifiedTopology : true})
  .then(() => console.log('DB connected'))
  .catch(err => console.log(err));
  //On connection error, log the message
  mongoose.connection.on('error', err => {
    console.log(`DB connection error : ${err.message}`);
  });
}

//export the connect function, to use in server.js
module.exports = { connect }; 
```

Enter fullscreen mode Exit fullscreen mode

Now let's go back to our server.js, and implement the connection to database feature

#### [](#serverjs-)server.js :

```
//Import modules
const path = require('path');
const express = require('express');
const bodyParser = require('body-parser');

//Import db module
const db = require('./db.js');

//Call the express function to initiate an express app
const app = express();

//Connect to database by calling our connect method
db.connect();

//This tells express to parse incoming requests
app.use(bodyParser.json());

//This tells express we are serving static files (front end files)
app.use(express.static(path.join(__dirname, 'public')));

/** NB: process.env.PORT is required as you would 
not be able to set the port manually in production */
const PORT = process.env.PORT || 3000;

//app to listen to specified port
app.listen(PORT, () => {
  console.log(`Server running on port${PORT}`);
});
```

Enter fullscreen mode Exit fullscreen mode

Make sure your local Mongo server is running.  
On server restart, you should see this in terminal  
[![terminal](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fres.cloudinary.com%2Folamideaboyeji%2Fimage%2Fupload%2Fv1586718080%2FdbConnected_zey4t4.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fres.cloudinary.com%2Folamideaboyeji%2Fimage%2Fupload%2Fv1586718080%2FdbConnected_zey4t4.png)

## [](#create-url-model)Create URL Model

Now that we have successfully connected to our database, let's create the URL model that would hold the format of how we want to store URLs in the database.

Create a file called url.model.js, and put this.

### [](#urlmodeljs-)url.model.js :

```
const mongoose = require('mongoose');

//create Url Schema (format)
const urlSchema = new mongoose.Schema({
    originalUrl: {
        type : String,
        required : true
    },
    shortUrl : {
        type : String,
        required : true
    },
    unique_name : {
        type : String,
        required : true
    },
    dateCreated : {
        type : Date,
        default : Date.now
    }  
});
//Use schema to create a Url model
const Url = mongoose.model('Url', urlSchema);

//Export Url Model
module.exports = Url;
```

Enter fullscreen mode Exit fullscreen mode

## [](#create-controllers-to-handle-all-routes)Create Controllers to handle all routes

We would now create controllers that would handle our two routes :

*   createShortLink
*   openShortLink Create a file called url.controllers.js and add code below :

### [](#urlcontrollerjs-)url.controller.js :

```
//import Url model
const Url = require('./url.model.js');

//This is basically your domain name
const baseUrl = process.env.BASE_URL || 'http://localhost:3000';

const createShortLink = async (req, res) => {
    //get the originalUrl and unique_name from the request's body
    let { originalUrl, unique_name } = req.body;

    try {
        //check if unique_name alredy exists
        let nameExists = await Url.findOne({ unique_name });
        /** if unique_name already exists, send a response with an
        error message, else save the new unique_name and originalUrl */
        if(nameExists){
            return res.status(403).json({
                error: "Unique name already exists, choose another",
                ok : false
            }) 
        }
        else {
            const shortUrl = baseUrl + '/' + unique_name;
            url = new Url({
                originalUrl,
                shortUrl,
                unique_name
            });
            //save
            const saved = await url.save();
            //return success message shortUrl
            return res.json({
                message : 'success',
                ok : true,
                shortUrl
            });
        }
    } catch (error) {
        ///catch any error, and return server error
        return res.status(500).json({ok : false, error : 'Server error'});
    }
};

const openShortLink = async (req, res) => {
    //get the unique name from the req params (e.g olamide from shorten.me/olamide)
    const { unique_name } = req.params;

    try{
      //find the Url model that has that unique_name
      let url = await Url.findOne({ unique_name });

       /** if such Url exists, redirect the user to the originalUrl 
       of that Url Model, else send a 404 Not Found Response */
        if(url){
            return res.redirect(url.originalUrl);
        } else {
            return res.status(404).json({error : 'Not found'});
        }  
    } catch(err) {
       //catch any error, and return server error to user
        console.log(err);
        res.status(500).json({error : 'Server error'});
    } 
};

module.exports = {
    createShortLink, openShortLink
}
```

Enter fullscreen mode Exit fullscreen mode

## [](#configure-routes)Configure routes

Let's go back to server.js and use these controllers we just created in our routes.  
We would first import them and use as shown below.

### [](#serverjs-)server.js :

```
//Import modules
const path = require('path');
const express = require('express');
const bodyParser = require('body-parser');

//Import db module
const db = require('./db.js');

//Import controllers
const { createShortLink, openShortLink } = require('./url.controller.js');

//Call the express function to initiate an express app
const app = express();

//Connect to database by calling our connect method
db.connect();

//This tells express to parse incoming requests
app.use(bodyParser.json());

//This tells express we are serving static files (front end files)
app.use(express.static(path.join(__dirname, 'public')));

//USE CONTROLLERS
//route to create short link
app.post('/createShortLink', createShortLink);
//route to open short link, ':' means unique_name is a param
app.get('/:unique_name', openShortLink);

/** NB: process.env.PORT is required as you would 
not be able to set the port manually in production */
const PORT = process.env.PORT || 3000;

//app to listen to specified port
app.listen(PORT, () => {
  console.log(`Server running on port${PORT}`);
});
```

Enter fullscreen mode Exit fullscreen mode

## [](#yayy-we-have-come-a-long-way)Yayy we have come a long way!!

Now let us start making requests from our frontend.

Open the public/main.js file and add this :

### [](#mainjs-)main.js :

```
const urlForm = document.getElementById('url-form');
const originalUrl = document.getElementById('original-url');
const uniqueName = document.getElementById('unique-name');
const confirmationShow = document.getElementById('confirmationShow');
const status = document.getElementById('status');

const formSubmit = e => {
    e.preventDefault();
    status.innerHTML = '<button type="button" class="loader"></button>'
    fetch('/createShortLink', {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          originalUrl : originalUrl.value,
          unique_name : uniqueName.value
        })
    })
    .then(data => data.json())
    .then(response => {
        status.innerHTML = '<button>SHORTEN</button>'
        if(!response.ok){
            confirmationShow.innerText = response.error;
        }
        else {
            confirmationShow.innerHTML = `Hooray!!! The link can now be visited 
            through <a target="_blank" 
            href=${response.shortUrl} rel = "noopener noreferer" > 
            ${response.shortUrl} </a>`;
        }
    })
    .catch(err => {
        console.log('oops', err);
        status.innerHTML = '<button>SHORTEN</button>';
        confirmationShow.innerText = 'Network error, retry'
    })
};

urlForm.addEventListener('submit', formSubmit);
```

Enter fullscreen mode Exit fullscreen mode

## [](#thats-it-)THAT'S IT !!!

Now make sure your server is running, open up your browser, go to [http://localhost:3000](http://localhost:3000/). Type a long URL in the original URL field, and a unique name in the unique name field. Submit your form and watch the magic happen.

[![donee](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fres.cloudinary.com%2Folamideaboyeji%2Fimage%2Fupload%2Fv1586912827%2Fazure-node1_ctgpgl.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fres.cloudinary.com%2Folamideaboyeji%2Fimage%2Fupload%2Fv1586912827%2Fazure-node1_ctgpgl.gif)

## [](#next-step)NEXT STEP

## [](#github-repository)GitHub Repository

Create a GitHub repository for the project and push your project to the remote repository ([Follow this guide](https://help.github.com/en/github/importing-your-projects-to-github/adding-an-existing-project-to-github-using-the-command-line))

## [](#mongodb-server)MongoDB Server

Before we deploy our project to Azure, we need to have a remote MongoDB server, because Azure cannot connect to the database on our local server. Head over to [MongoDB Atlas](https://cloud.mongodb.com/) and get your connection string. This would be our MONGO\_URI variable on the server. (Remember when we added process.env.MONGO\_URI) to our app. You can follow this [guide](https://codeforgeek.com/mongodb-atlas-node-js) to get your connection string.

## [](#last-step)LAST STEP!!!

## [](#deloy-to-azure)Deloy to Azure

*   Head over to [Azure Portal](https://portal.azure.com/) and create an account. NOTE : When you register on Azure, you would get $200 credits to try Azure for 30 days. A credit card validation would be required. If you are a student, [Click here](https://azure.microsoft.com/en-us/free/students/) to create an account for free with no credit card required.

[![thank you](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fres.cloudinary.com%2Folamideaboyeji%2Fimage%2Fupload%2Fv1586911070%2Fazure-node_ivebtc.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fres.cloudinary.com%2Folamideaboyeji%2Fimage%2Fupload%2Fv1586911070%2Fazure-node_ivebtc.png)

## [](#and-thats-it-our-app-is-liveeeee)And that's it. Our app is liveeeee!!!

Go to your site's URL and test it out.

Follow this [guide](https://docs.microsoft.com/en-us/azure/app-service/manage-custom-dns-buy-domain) to buy and set up an actual short custom domain for the app. I got [rdre.me](https://rdre.me/) for mine.

You can go on and add more features to your app, such as registering users before they can create a short link, short link expiry date, etc.

Thank you for coming this far.

[![thank you](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fmedia1.tenor.com%2Fimages%2F46d2189f4e8189b0ee866110ad109d9b%2Ftenor.gif%3Fitemid%3D11070439)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fmedia1.tenor.com%2Fimages%2F46d2189f4e8189b0ee866110ad109d9b%2Ftenor.gif%3Fitemid%3D11070439)

Link to Demo : [https://rdre.me](https://rdre.me/)

Link to GitHub repository : [https://github.com/aolamide/shorten-url](https://github.com/aolamide/shorten-url)

Please drop your comments and questions.

You can reach me on [LinkedIn](https://linkedin.com/in/aolamide) and [Twitter](https://twitter.com/olamideaboyeji).
