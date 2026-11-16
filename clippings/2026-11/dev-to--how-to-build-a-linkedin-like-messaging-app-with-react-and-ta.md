---
url: "https://dev.to/talkjs/how-to-build-a-linkedin-like-messaging-app-with-react-and-talkjs-part-1-n9c"
captured_at: "2026-11-16T19:17:26+00:00"
title: "How to build a LinkedIn-like Messaging App with React and TalkJS - Part 1"
domain: "dev-to"
---

Chat is an integral part of most modern web applications today. Whether it is a company website, an online market place or an online community, the ability for users to communicate with a company representative or other users on a platform greatly improves user experience.  
However, building a chat feature from scratch might be tasking for a developer. Thankfully, with TalkJS, adding chat to your app is one less thing you have to worry about as a developer.

This tutorial will show you how you can easily integrate a chat feature into an app using TalkJS. It will serve as a step-by-step guide to integrate TalkJS into any React application. We will use a practical and real-world use case to do this demonstration. We will build a LinkedIn-like messaging app. Here is a link to the [repository of the messaging app](https://github.com/talkjs/talkjs-examples/tree/master/react/linkedin-like-app). You can follow [the guide](https://github.com/talkjs/talkjs-examples/tree/master/react/linkedin-like-app#getting-started) to set it up and see how it works.

This tutorial is divided into two parts. In the first part, we will build a LinkedIn-like app without any chat. In the second part, we will integrate chat into the app using TalkJS.

First, though, let us discuss what TalkJS is and some features it provides out of the box.

## [](#an-introduction-to-talkjs)An Introduction To TalkJS

[TalkJS](https://talkjs.com/) makes it easy to integrate full-featured chat into your websites and mobile apps. With the TalkJS chat API + SDK, developers can easily add chat between users on your platform in hours instead of months. Here are some features of TalkJS that makes it a great choice for your next chat integration.

1.  **Real-time messaging**: TalkJS provides more than just real-time messaging, it provides features that bring such messaging to live. With TalkJS, you can easily enable features like file sharing, location sharing, emoji in your chat application.
2.  **Email and SMS fallback**: In this busy world, users of your application may not always be online. TalkJS sends emails and/or SMS to your offline users so that never miss messages.
3.  **Chat Pop-up**: With the TalkJS chat pop-up, you can bring a single conversation into focus from anywhere on your platform.
4.  **Full Conversation History**: With the TalkJS Inbox view, your users can get back to a conversation whenever they want. TalkJS Inbox provides users with a history of all their conversations in a beautiful and well-designed interface.
5.  **Responsive cross-browser UX**: With TalkJS, you do not have to bother about writing complex media queries to make your chat interface responsive. By default, TalkJS interfaces look great on all screen sizes and modern browsers.
6.  **Multi-Language User Interface**: With the in-built localisation features of TalkJS, you can display the text of the interfaces in the user's language.

These are just some of the features that make TalkJS the best choice for your chat integrations. Now let us see how we can integrate TalkJS in your React or JavaScript application.

### [](#prerequisites)Prerequisites

To follow along with this tutorial, you will need the following:

*   Basic knowledge of JavaScript.
*   An understanding of React and its component lifecycle methods.
*   Node >= version 6 and NPM >= version 5.2 (or yarn if you prefer yarn) running on your machine.

### [](#what-we-will-be-building)What we will be building

We will be building an app like the messaging feature of LinkedIn.

LinkedIn messaging has two major parts.

*   The chat widget that pops up when you want to send a message to a connection.
*   The main messaging page. This page shows the list of all the conversations you have with your connections.

We will be building a messaging app similar to this. There are three major parts of this app.

1.  **The login page**: This is a simple form that takes basic user data TalkJS will use for the chats.

[![User Interface for the Login page](https://res.cloudinary.com/practicaldev/image/fetch/s--7YIzrZsa--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://thepracticaldev.s3.amazonaws.com/i/mvy40du4f8amftmt8uju.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--7YIzrZsa--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://thepracticaldev.s3.amazonaws.com/i/mvy40du4f8amftmt8uju.png)

2.**The MyNetwork page**: This is an interface that displays a list of users that represent your connections on LinkedIn. For this tutorial, we will be using dummy data. In a real app, this user list can be gotten from your database. Each user on the list has a “Message” button which you can use to start a conversation with that user. Clicking on this button brings up a Chatbox similar to that found on LinkedIn.

[![The MyNetwork Page](https://res.cloudinary.com/practicaldev/image/fetch/s--PYjY9O6N--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://thepracticaldev.s3.amazonaws.com/i/yhbkdi3cmx7vnwhs2o2u.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--PYjY9O6N--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://thepracticaldev.s3.amazonaws.com/i/yhbkdi3cmx7vnwhs2o2u.png)

3.**The Messaging page**: This is similar to the messaging page of LinkedIn that shows all the conversations a user has had with other connections. This will be accomplished using the Inbox feature of TalkJS.  
[![The messaging page](https://res.cloudinary.com/practicaldev/image/fetch/s--jX7aJbib--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://thepracticaldev.s3.amazonaws.com/i/0j0c880vzb9e8ng80vr4.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--jX7aJbib--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://thepracticaldev.s3.amazonaws.com/i/0j0c880vzb9e8ng80vr4.png)

Here is a [live demo of this application](https://talkjs.com/demos/react/linkedin-messaging-app).

Let us start building. First, we need to do a basic setup for the application.

## [](#setting-up-the-app-using-create-react-app-boilerplate)Setting up the App using Create React App Boilerplate

To set up the app, we will be using the create-react-app boilerplate which makes it very easy to set up any React app. If you do not already have it installed, then run the command below to install it globally on your machine.  

```
npm install -g create-react-app
```

Enter fullscreen mode Exit fullscreen mode

After installing this, you can easily create react apps on your machine. Let us create one for the app we are building. We will call it `messaging-app`.  

```
create-react-app messaging-app
```

Enter fullscreen mode Exit fullscreen mode

When we do that, we are ready to start building our project. Next, we navigate to the folder we created.  

```
cd messaging-app
```

Enter fullscreen mode Exit fullscreen mode

To start the application, run the following command.  

```
npm start
```

Enter fullscreen mode Exit fullscreen mode

The app should be running now on your default browser. That is it for setting up the React application. Now, let us move over to set up routes for the app using react-router.

### [](#structuring-the-files-and-adding-routes)Structuring the files and adding routes

This is the file structure of the project we will be building. We will keep this as simple as possible.  

```
/
|-- node_modules
|-- /public
|-- /src
    |-- /Components
        |-- Messaging.js
        |-- Login.js
        |-- MyNetwork.js
        |-- Users.js
|-- App.css
|-- App.js
|-- index.css
|-- index.js
```

Enter fullscreen mode Exit fullscreen mode

Create the files to make your project structure similar to the file structure above. We will be using react-router to add basic routes for our components in our `App.js` file. So next, we will install react-router.  

```
npm install --save react-router react-router-dom
```

Enter fullscreen mode Exit fullscreen mode

Then, we replace the content of the App.js file with the following code.  

```
import React, { Component } from 'react';
import { BrowserRouter as Router, Link, Route } from 'react-router-dom';

import './App.css';

class App extends Component {
    render() {  
        return (
            <div>
                <Router>
                    <nav className="navbar"> 
                        <ul className="navbar-list">
                            <li className="navbar-item">
                                <Link to="/mynetwork" className="navbar-link">My Network</Link>
                            </li>
                            <li className="navbar-item">
                                <Link to="/messaging" className="navbar-link">Messaging</Link>
                            </li>
                        </ul>

                    </nav>
                </Router>
            </div>
        );
    }
}
export default App;
```

Enter fullscreen mode Exit fullscreen mode

The `App.js` contains the `navbar` that we can use to access the parts of the app. For now, the links do nothing because we have not added routes. We will add these routes as the create the components.

Since we assume that you have a basic knowledge of React, we will not be explaining every part of the code. Let us add some CSS styles for the `navbar` in the `App.css` file.  

```
body {
  background-color: #F5F5F5;
}
li {
  list-style-type: none;
}
* {
  box-sizing: border-box;
}
.navbar {
  display: flex;
  align-items: center;
  height: 52px;
  background-color: #283E4A;
  margin-bottom: 50px;
}
.navbar-list {
  display: flex;
  margin: 0 auto;
}
.navbar-item {
  color: #ffffff;
}
.navbar-link {
  color: #ffffff;
  text-decoration: none;
  margin-right: 20px
}
```

Enter fullscreen mode Exit fullscreen mode

Next, we will create the Login component.

### [](#creating-the-login-component)Creating the Login Component

As shown in the login image, the login interface is a form used to take basic user data. TalkJS will use this data to create a new user. This user data includes the user’s name, email and a short description to make it look more LinkedIn-like. We will store this data in the browser’s local storage. We can retrieve it from the local storage whenever we need it.

To create a new user, we assign a number to the user as the ID of the user. TalkJS will use this ID to identify each user and retrieve messages by that user. In this tutorial, we will assign a random number to each new user as shown in the code below.

First, in the login component, we add the form.  

```
import React from "react";

class Login extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            name: "",
            email: "",
            description: "",
        }
        this.handleChange = this.handleChange.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
    }
    handleChange(e) {
        const target = e.target;
        this.setState({
            [target.name] : target.value
        })
    }
    handleSubmit(event) {
        event.preventDefault();
        const { name, email, description } = this.state;

        /* Generate random number that will be serve as the ID of the user */
        const randomNum  = Math.ceil(Math.random() * 10000);
        const userData = {
            name,
            email,
            description,
            id: randomNum,
            role: "Member",
            photoUrl: "https://talkjs.com/docs/img/ronald.jpg"
        }

        /* Store user data in browser's local storage */
        localStorage.setItem("currentTalkjsUser", JSON.stringify(userData))
        /*Redirect to the my network page */
        this.props.history.push("/mynetwork");
    }
    render() {
        return (
            <div className="login-container">
                <div className="login-form">
                    <form onSubmit={this.handleSubmit}>
                        <input type="text"
                           name="name"
                           onChange={this.handleChange}
                           placeholder="Name"
                           className="input" 
                           required
                         />
                         <input
                           type="email"
                           name="email"
                           onChange={this.handleChange}
                           placeholder="Email"
                           className="input"
                           required
                          />
                         <textarea type="text"
                           name="description"
                           onChange={this.handleChange}
                           placeholder="Short Description"
                           className="input textarea">
                         </textarea>
                         <input type="submit"
                           className="button" 
                           placeholder="submit"
                         />
                    </form>
                </div>
            </div>
        )
    }
}
export default Login
```

Enter fullscreen mode Exit fullscreen mode

The form takes the user's data and stores it in the local storage using the `handleSubmit` method. Then, it redirects the user to the MyNetwork page. Let us import this to our `App.js` file and create a route for it there. This will enable us to see the login page.  

```
import React, { Component } from 'react';
import { BrowserRouter as Router, Link, Route } from 'react-router-dom';
import Login from './Components/Login';

...

...
                <li className="navbar-item">
                    <Link to="/messaging" className="navbar-link">Messaging</Link>
                </li>
            </ul>
        </nav>

        <Route path="/" exact component={Login}/> 
    </Router>
</div>
...
```

Enter fullscreen mode Exit fullscreen mode

At this point, your screen should look like this.

[![Unstyled login page](https://res.cloudinary.com/practicaldev/image/fetch/s--uIWPvV1d--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://paper-attachments.dropbox.com/s_E7612E1A04D31375D81EE173B96C13C086977BA1E8A29BE4374DBC2130C73390_1567118367046_Screen%2BShot%2B2019-08-29%2Bat%2B11.38.53%2BPM.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--uIWPvV1d--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://paper-attachments.dropbox.com/s_E7612E1A04D31375D81EE173B96C13C086977BA1E8A29BE4374DBC2130C73390_1567118367046_Screen%2BShot%2B2019-08-29%2Bat%2B11.38.53%2BPM.png)

Ugly right? To make it look more appealing, add the following styles to the `App.css` file.  

```
.login-container {
  width: 40%;
  margin: 0 auto;
  text-align: center;
}
.login-form {
  background: #ffffff;
  padding: 40px 20px;
}
.input {
  display: block;
  height: 42px;
  width: 80%;
  margin: 0 auto 20px;
  padding: 10px;
  font-size: 14px;
  border-radius: 4px;
  border: 1px solid #8F7474;
}
.button {
  width: 150px;
  border-radius: 4px;
  height: 42px;
  font-size: 14px;
  background-color: #283E4A;
  color: #ffffff;
}
.textarea {
  height: 100px;
}

```

Enter fullscreen mode Exit fullscreen mode

It looks much better now.

[![Styled login page](https://res.cloudinary.com/practicaldev/image/fetch/s--dhB7m8cJ--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://paper-attachments.dropbox.com/s_E7612E1A04D31375D81EE173B96C13C086977BA1E8A29BE4374DBC2130C73390_1567118493159_Screen%2BShot%2B2019-08-29%2Bat%2B11.40.49%2BPM.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--dhB7m8cJ--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://paper-attachments.dropbox.com/s_E7612E1A04D31375D81EE173B96C13C086977BA1E8A29BE4374DBC2130C73390_1567118493159_Screen%2BShot%2B2019-08-29%2Bat%2B11.40.49%2BPM.png)

Clicking on the submit button will redirect to the `mynetwork` page which has no content for now.  
Let us move on to this page then. This is where we get to use TalkJS.

### [](#creating-the-my-network-component)Creating the “My Network” Component

This will be similar to the “my network” page on LinkedIn, where you see a list of all connections. In this case though, we will be using dummy data to fetch these users. Below is a list of dummy connections. We will add this list to the `Users.js` file and import it in the `MyNetwork` file.  

```
export const dummyUsers = [ 
    {
        id: "2",
        name: "Kelvin Samson",
        email: "kelvin@sample.com",
        photoUrl: "https://randomuser.me/api/portraits/men/32.jpg",
        role: "Member",
        info: "Product Designer at Facebook",
        welcomeMessage: "Hey there! Love to chat :-)"
    },
    {
        id: "3",
        name: "Annabel Stone",
        email: "annie@sample.com",
        photoUrl: "https://randomuser.me/api/portraits/women/65.jpg",
        role: "Member",
        info: "Digital Marketer at Microsoft",
        welcomeMessage: "Hey there! Love to chat :-)"
    },
    {
        id: "4",
        name: "Grace Loveday",
        email: "grace@sample.com",
        photoUrl: "https://randomuser.me/api/portraits/women/44.jpg",
        role: "Member",
        info: "Product Designer at Google",
        welcomeMessage: "Hey there! Love to chat :-)"
    },
    {
        id: "5",
        name: "Angela Jobs",
        email: "angela@sample.com",
        photoUrl: "https://pbs.twimg.com/profile_images/834493671785525249/XdLjsJX_.jpg",
        role: "Member",
        info: "Software Engineer at TalkJS",
        welcomeMessage: "Hey there! Love to chat :-)"
    },
]
```

Enter fullscreen mode Exit fullscreen mode

Next up, we will create the `MyNetwork` component and display the list of users.

### [](#rendering-the-list-of-users)Rendering the list of users

Create the `MyNetwork.js` file if you have not already done so. Add the following code to it.  

```
import React, { Component } from 'react';
import { dummyUsers } from "./Users";

class MyNetwork extends Component {
    render() {
        return (
            <div className="users">
                <div className="users-container"> 
                    <ul>
                        { dummyUsers.map(user => 
                          <li key={user.id} className="user">
                              <picture className="user-picture">
                                  <img src={user.photoUrl} alt={`${user.name}`} />
                              </picture>
                              <div className="user-info-container">
                                  <div className="user-info">
                                      <h4>{user.name}</h4>
                                      <p>{user.info}</p>
                                  </div>
                                  <div className="user-action">
                                      <button >Message</button>
                                  </div>
                              </div>
                          </li>
                        )}
                    </ul>
                </div>
           </div>
        )
    }
}
    export default MyNetwork;
```

Enter fullscreen mode Exit fullscreen mode

We added a map that loops through each user and displays their basic data.

Let us import this file and create a route for it in the `App.js` file.  

```
import React, { Component } from 'react';
import { BrowserRouter as Router, Link, Route } from 'react-router-dom';
import Login from './Components/Login';
import MyNetwork from './Components/MyNetwork';

...

...

            <Route path="/" exact component={Login}/> 
            <Route path="/mynetwork" component={MyNetwork}/>
         </Router>
      </div>
    ...
```

Enter fullscreen mode Exit fullscreen mode

If you click on the “my network” link on the navbar, you will see that the name, user description and image of each user is being displayed. You will also notice that there is a message button for each user. This is the button we will use to call up the TalkJS chatbox. Before we do this, let us add some styles to the `App.css` file for this page.  

```
.users {
  display: flex;
  width: 55%;
  margin: 0 auto;
  justify-content: space-around;
}
.users-container {
  background-color: #ffffff;
  width: 65%;
  padding: 20px 0;
}
.user {
  display: flex;
  margin-bottom: 20px;
  position: relative;
  border-bottom: 1px solid #e6e9ec;
}
.user:last-of-type {
  border: 0;
}
.user::after {
  content: '';
  width: 92px;
  height: 2px;
  background: #fff;
  position: absolute;
  bottom: -1px;
  left: 0;
}
.user-picture img {
  height: 72px;
  width: 72px;
  border-radius: 50%;
  margin-right: 20px;
}
.user-info {
  width: 70%;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.user-info-container {
  display: flex;
  width: 100%;
}
.user-info h4 {
  margin: 0;
}
.user-info p{
  margin-top: 7px;
  color: #676767;
  font-size: 14px;
}
.user-action {
  width: 25%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.user-action button {
  background-color: transparent;
  color: #0073b1;
  border: 1px solid #0073b1;
  height: 32px;
  width: 92px;
  font-size: 14px;
  font-weight: bold;
  border-radius: 2px;
  cursor: pointer;
}

```

Enter fullscreen mode Exit fullscreen mode

The network page should look like this now.

[![The MyNetwork page so far](https://res.cloudinary.com/practicaldev/image/fetch/s--tIB7RoVq--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://paper-attachments.dropbox.com/s_E7612E1A04D31375D81EE173B96C13C086977BA1E8A29BE4374DBC2130C73390_1567119719531_Screen%2BShot%2B2019-08-30%2Bat%2B12.01.08%2BAM.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--tIB7RoVq--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://paper-attachments.dropbox.com/s_E7612E1A04D31375D81EE173B96C13C086977BA1E8A29BE4374DBC2130C73390_1567119719531_Screen%2BShot%2B2019-08-30%2Bat%2B12.01.08%2BAM.png)

#### [](#displaying-the-current-user)Displaying the current user

Before we will be able to send messages, we need to get the current user. TalkJS will use this to set up the conversation between the current user and the user that you want to send a message to. Remember we saved the logged-in user in the local storage. Let us retrieve it an add it to our component’s state. We can even get fancier by adding the current user’s data to the user interface. That way the user will know who he is logged in as.

Let us do this by adding the following code to the constructor method of our component.  

```
class MyNetwork extends Component {
    constructor(props) {
        super(props); 
        let currentUser;
        const currentTalkjsUser = localStorage.getItem('currentTalkjsUser');
        if (currentTalkjsUser) {
            currentUser = JSON.parse(currentTalkjsUser)
        }
        this.state = {
            currentUser
        }
    }
...
```

Enter fullscreen mode Exit fullscreen mode

Next, we will use the data to display the current user’s information in the render function.  

```
...   
 render() {
     const { currentUser } = this.state;
     return (
         <div className="users">
             <div className="current-user-container">
                 {currentUser &&
                     <div>
                         <picture className="current-user-picture">
                             <img alt={currentUser.name} src={currentUser.photoUrl} />
                         </picture>
                         <div className="current-user-info">
                             <h3>{currentUser.name}</h3>
                             <p>{currentUser.description}</p>
                         </div>
                     </div>
                 }
             </div>
             <div className="users-container"> 
    ...
```

Enter fullscreen mode Exit fullscreen mode

Now you should have some user data on the interface. Let us add some styles for it. Add the following CSS to the `App.css` file.  

```
.current-user-container {
  width: 28%;
}
.current-user-container>div {
  background-color: #ffffff;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 300px;
}
.current-user-info {
  text-align: center;
}
.current-user-info h3 {
  margin-bottom: 10px;
}
.current-user-info p {
  margin-bottom: 0;
}
.current-user-picture img {
  width: 120px;
  height: 120px;
  border-radius: 50%;
}
```

Enter fullscreen mode Exit fullscreen mode

It should look great now. We have made good progress.

So far, we have been able to build a LinkedIn-like app with a login page and the "My Network" page. In the next part of this tutorial, we will set up TalkJS and add chat to the application.
