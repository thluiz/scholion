---
url: "https://web.archive.org/web/20201101014159id_/https://thewebdev.info/2020/01/16/how-to-add-browser-notifications-to-your-react-app/"
captured_at: "2026-11-16T07:56:18+00:00"
title: "How to Add Browser Notifications to Your React App - The Web Dev"
domain: "web-archive-org"
---

With the HTML5 Notification API, browsers can display native popup notifications to users. With notifications, you can display text and icons, and also play sound with them. The full list of options is located at [https://developer.mozilla.org/en-US/docs/Web/API/notification](https://developer.mozilla.org/en-US/docs/Web/API/notification). Users have to grant permission to display notifications when they visit a web app to see browser notifications.

Developers have done the hard work for us if we use React because a React component is created to display browser notifications. The React-Web-Notification package, located at [https://www.npmjs.com/package/react-web-notification](https://www.npmjs.com/package/react-web-notification) can let us display popups and handle the events that are associated with display the notifications like when use clicks on the notification or handle cases when permissions or granted or denied for display notifications.

In this article, we will build a password manager that lets you enter, edit and delete passwords to the websites and show notifications whenever these actions are taken. We will use React to build the app.

To start, we will run Create React App to create the app. Run:

```
npx create-react-app password-manager
```

to create the app. Next, we add our own libraries, we will use Axios for making HTTP requests to our back end, Formik and Yup for form value handling and form validation respectively, MobX for state management, React Bootstrap for styling, React-Copy-To-Clipboard for letting us copy data to the clipboard, and React Router for routing.

We install them by running:

```
npm i axios formik mobx mobx-react react-bootstrap react-copy-to-clipboard react-router-fom yup react-web-notifications
```

With all the libraries installed, we can start building our app. We create all the files in the `src` folder unless otherwise specified.

First, we replace the existing code in `App.css` with:

```
.bg-primary {  
  background-color: #09d3ac !important;  
}
```

to change the top bar’s background color. Next in `App.js` , replace the current code with:

```
import React from "react";  
import { Router, Route } from "react-router-dom";  
import HomePage from "./HomePage";  
import { createBrowserHistory as createHistory } from "history";  
import Navbar from "react-bootstrap/Navbar";  
import Nav from "react-bootstrap/Nav";  
import "./App.css";  
const history = createHistory();

function App({ passwordsStore }) {  
  return (  
    <div className="App">  
      <Router history={history}>  
        <Navbar bg="primary" expand="lg" variant="dark">  
          <Navbar.Brand href="#home">Password Manager</Navbar.Brand>  
          <Navbar.Toggle aria-controls="basic-navbar-nav" />  
          <Navbar.Collapse id="basic-navbar-nav">  
            <Nav className="mr-auto">  
              <Nav.Link href="/" active>Home</Nav.Link>  
            </Nav>  
          </Navbar.Collapse>  
        </Navbar>  
        <Route  
          path="/"  
          exact  
          component={props => (  
            <HomePage {...props} passwordsStore={passwordsStore} />  
          )}  
        />  
      </Router>  
    </div>  
  );  
}export default App;
```

to add our React Bootstrap top bar and our route to the home page. `passwordStore` is our MobX store for storing our password list in the front end.

Next create `HomePage.css` and add:

```
.home-page {  
  padding: 20px;  
}
```

to add some padding to our page.

Then create `HomePage.js` and add:

```
import React from "react";  
import { useState, useEffect } from "react";  
import Table from "react-bootstrap/Table";  
import ButtonToolbar from "react-bootstrap/ButtonToolbar";  
import Button from "react-bootstrap/Button";  
import Modal from "react-bootstrap/Modal";  
import PasswordForm from "./PasswordForm";  
import "./HomePage.css";  
import { deletePassword, getPasswords } from "./requests";  
import { observer } from "mobx-react";  
import { CopyToClipboard } from "react-copy-to-clipboard";  
import Notification from "react-web-notification";

function HomePage({ passwordsStore }) {  
  const [openAddModal, setOpenAddModal] = useState(false);  
  const [openEditModal, setOpenEditModal] = useState(false);  
  const [initialized, setInitialized] = useState(false);  
  const [selectedPassword, setSelectedPassword] = useState({});  
  const [notificationTitle, setNotificationTitle] = React.useState(""); const openModal = () => {  
    setOpenAddModal(true);  
  }; 

  const closeModal = () => {  
    setOpenAddModal(false);  
    setOpenEditModal(false);  
    getData();  
  }; 

  const cancelAddModal = () => {  
    setOpenAddModal(false);  
  }; 

  const editPassword = contact => {  
    setSelectedPassword(contact);  
    setOpenEditModal(true);  
  }; 

  const cancelEditModal = () => {  
    setOpenEditModal(false);  
  }; 

  const getData = async () => {  
    const response = await getPasswords();  
    passwordsStore.setPasswords(response.data);  
    setInitialized(true);  
  }; 

  const deleteSelectedPassword = async id => {  
    await deletePassword(id);  
    setNotificationTitle("Password deleted");  
    getData();  
  }; 

  useEffect(() => {  
    if (!initialized) {  
      getData();  
    }  
  }); 

  return (  
    <div className="home-page">  
      <h1>Password Manager</h1>  
      <Modal show={openAddModal} onHide={closeModal}>  
        <Modal.Header closeButton>  
          <Modal.Title>Add Password</Modal.Title>  
        </Modal.Header>  
        <Modal.Body>  
          <PasswordForm  
            edit={false}  
            onSave={closeModal.bind(this)}  
            onCancelAdd={cancelAddModal}  
            passwordsStore={passwordsStore}  
          />  
        </Modal.Body>  
      </Modal> <Modal show={openEditModal} onHide={closeModal}>  
        <Modal.Header closeButton>  
          <Modal.Title>Edit Password</Modal.Title>  
        </Modal.Header>  
        <Modal.Body>  
          <PasswordForm  
            edit={true}  
            onSave={closeModal.bind(this)}  
            contact={selectedPassword}  
            onCancelEdit={cancelEditModal}  
            passwordsStore={passwordsStore}  
          />  
        </Modal.Body>  
      </Modal>  
      <ButtonToolbar onClick={openModal}>  
        <Button variant="outline-primary">Add Password</Button>  
      </ButtonToolbar>  
      <br />  
      <div className="table-responsive">  
        <Table striped bordered hover>  
          <thead>  
            <tr>  
              <th>Name</th>  
              <th>URL</th>  
              <th>Username</th>  
              <th>Password</th>  
              <th></th>  
              <th></th>  
              <th></th>  
              <th></th>  
            </tr>  
          </thead>  
          <tbody>  
            {passwordsStore.passwords.map(c => (  
              <tr key={c.id}>  
                <td>{c.name}</td>  
                <td>{c.url}</td>  
                <td>{c.username}</td>  
                <td>******</td>  
                <td>  
                  <CopyToClipboard text={c.username}>  
                    <Button  
                      variant="outline-primary"  
                      onClick={() => setNotificationTitle("Username copied")}  
                    >  
                      Copy Username to Clipboard  
                    </Button>  
                  </CopyToClipboard>  
                </td>  
                <td>  
                  <CopyToClipboard text={c.password}>  
                    <Button  
                      variant="outline-primary"  
                      onClick={() => setNotificationTitle("Password copied")}  
                    >  
                      Copy Password to Clipboard  
                    </Button>  
                  </CopyToClipboard>  
                </td>  
                <td>  
                  <Button  
                    variant="outline-primary"  
                    onClick={editPassword.bind(this, c)}  
                  >  
                    Edit  
                  </Button>  
                </td>  
                <td>  
                  <Button  
                    variant="outline-primary"  
                    onClick={deleteSelectedPassword.bind(this, c.id)}  
                  >  
                    Delete  
                  </Button>  
                </td>  
              </tr>  
            ))}  
          </tbody>  
        </Table>  
      </div> {notificationTitle ? (  
        <Notification  
          title={notificationTitle}  
          options={{  
            icon:  
              "http://mobilusoss.github.io/react-web-notification/example/Notifications_button_24.png"  
          }}  
          onClose={() => setNotificationTitle(undefined)}  
        />  
      ) : null}  
    </div>  
  );  
}  
export default observer(HomePage);
```

This component is the home page of our app. We have a table to display the list of passwords, a button to add a login and password entry, and buttons in each row of the table to copy username and password, and edit and delete each entry. We have the name, URL, username and password columns. The `CopyToClipboard` component allows us to copy the data we copy to the `text` prop of the component. Any component can be inside this component. We have one React Bootstrap modal for add password and another one for edit. `PasswordForm` is our form for adding the password entries, which we will create later.

We show the notifications whenever a username or password is copied, and when an entry is deleted. We do this by setting the notification title with the `setNotificationTitle` function. We add an `onClose` handler in the `Notification` component so that the notification will display again once it is closed.

We have the `openModal` , `closeModal` , `cancelAddModal` , and `cancelEditModal` functions to open and close the modals. In the `editPassword` function, we call the `setSelectedPassword` function to set the password entry to be edited.

The `observer` we wrap around the `HomePage` component is for letting us watch the latest values from `passwordsStore`.

Next, we modify `index.js` to have:

```
import React from "react";  
import ReactDOM from "react-dom";  
import "./index.css";  
import App from "./App";  
import * as serviceWorker from "./serviceWorker";  
import { PasswordsStore } from "./store";  
const passwordsStore = new PasswordsStore();

ReactDOM.render(  
  <App passwordsStore={passwordsStore} />,  
  document.getElementById("root")  
);

// If you want your app to work offline and load faster, you can change  
// unregister() to register() below. Note this comes with some pitfalls.  
// Learn more about service workers: [https://bit.ly/CRA-PWA](https://bit.ly/CRA-PWA)  
serviceWorker.unregister();
```

We pass in our `PasswordStore` MobX store here, which will pass it to all the other components.

Next, we create `PasswordForm.js` and add:

```
import React from "react";  
import { Formik } from "formik";  
import Form from "react-bootstrap/Form";  
import Col from "react-bootstrap/Col";  
import Button from "react-bootstrap/Button";  
import * as yup from "yup";  
import PropTypes from "prop-types";  
import { addPassword, getPasswords, editPassword } from "./requests";  
import Notification from "react-web-notification";

const schema = yup.object({  
  name: yup.string().required("Name is required"),  
  url: yup  
    .string()  
    .url()  
    .required("URL is required"),  
  username: yup.string().required("Username is required"),  
  password: yup.string().required("Password is required")  
});

function PasswordForm({  
  edit,  
  onSave,  
  contact,  
  onCancelAdd,  
  onCancelEdit,  
  passwordsStore  
}) {  
  const [notificationTitle, setNotificationTitle] = React.useState(""); 
  const handleSubmit = async evt => {  
    const isValid = await schema.validate(evt);  
    if (!isValid) {  
      return;  
    }  
    if (!edit) {  
      await addPassword(evt);  
      setNotificationTitle("Password added");  
    } else {  
      await editPassword(evt);  
      setNotificationTitle("Password edited");  
    }  
    const response = await getPasswords();  
    passwordsStore.setPasswords(response.data);  
    onSave();  
  }; 

  return (  
    <>  
      <Formik  
        validationSchema={schema}  
        onSubmit={handleSubmit}  
        initialValues={contact || {}}  
      >  
        {({  
          handleSubmit,  
          handleChange,  
          handleBlur,  
          values,  
          touched,  
          isInvalid,  
          errors  
        }) => (  
          <Form noValidate onSubmit={handleSubmit}>  
            <Form.Row>  
              <Form.Group as={Col} md="12" controlId="name">  
                <Form.Label>Name</Form.Label>  
                <Form.Control  
                  type="text"  
                  name="name"  
                  placeholder="Name"  
                  value={values.name || ""}  
                  onChange={handleChange}  
                  isInvalid={touched.name && errors.name}  
                />  
                <Form.Control.Feedback type="invalid">  
                  {errors.name}  
                </Form.Control.Feedback>  
              </Form.Group> <Form.Group as={Col} md="12" controlId="url">  
                <Form.Label>URL</Form.Label>  
                <Form.Control  
                  type="text"  
                  name="url"  
                  placeholder="URL"  
                  value={values.url || ""}  
                  onChange={handleChange}  
                  isInvalid={touched.url && errors.url}  
                />  
                <Form.Control.Feedback type="invalid">  
                  {errors.url}  
                </Form.Control.Feedback>  
              </Form.Group> <Form.Group as={Col} md="12" controlId="username">  
                <Form.Label>Username</Form.Label>  
                <Form.Control  
                  type="text"  
                  name="username"  
                  placeholder="Username"  
                  value={values.username || ""}  
                  onChange={handleChange}  
                  isInvalid={touched.username && errors.username}  
                />  
                <Form.Control.Feedback type="invalid">  
                  {errors.username}  
                </Form.Control.Feedback>  
              </Form.Group> <Form.Group as={Col} md="12" controlId="password">  
                <Form.Label>Password</Form.Label>  
                <Form.Control  
                  type="password"  
                  name="password"  
                  placeholder="Password"  
                  value={values.password || ""}  
                  onChange={handleChange}  
                  isInvalid={touched.password && errors.password}  
                />  
                <Form.Control.Feedback type="invalid">  
                  {errors.password}  
                </Form.Control.Feedback>  
              </Form.Group>  
            </Form.Row>  
            <Button type="submit" style={{ marginRight: "10px" }}>  
              Save  
            </Button>  
            <Button type="button" onClick={edit ? onCancelEdit : onCancelAdd}>  
              Cancel  
            </Button>  
          </Form>  
        )}  
      </Formik>  
      {notificationTitle ? (  
        <Notification  
          title={notificationTitle}  
          options={{  
            icon:  
              "http://mobilusoss.github.io/react-web-notification/example/Notifications_button_24.png"  
          }}  
          onClose={() => setNotificationTitle(undefined)}  
        />  
      ) : null}  
    </>  
  );  
}

PasswordForm.propTypes = {  
  edit: PropTypes.bool,  
  onSave: PropTypes.func,  
  onCancelAdd: PropTypes.func,  
  onCancelEdit: PropTypes.func,  
  contact: PropTypes.object,  
  contactsStore: PropTypes.object  
};

export default PasswordForm;
```

Here, we add our form for letting users enter the username and password of their websites. We use the Yup `schema` object we created at the top of our code to make sure all fields are entered and check that the URL entered is actually a URL. We use the `Formik` component to handle the form of input changes and get the latest values.

Once the form is checked to be valid by `schema.validate` promise to resolve to `true` , then `addPassword` or `editPassword` functions from `requests.js` , which we will create later will be called depending if the user is adding or editing an entry. Once that succeeds, then the `getPasswords` from the same file is called, and then `setPasswords` from `passwordsStore` is called to store the passwords in the store. Finally, `onSave` passed in from the props in `HomePage` component is called to close the modal.

We show the notifications whenever an entry is added or edited, and when an entry is deleted. We do this by setting the notification title with the `setNotificationTitle` function. We add an `onClose` handler in the `Notification` component so that the notification will display again once it is closed.

Next, create `requests.js` and add:

```
const APIURL = 'http://localhost:3000';  
const axios = require('axios');

export const getPasswords = () => axios.get(`${APIURL}/passwords`);
export const addPassword = (data) => axios.post(`${APIURL}/passwords`, data);
export const editPassword = (data) => axios.put(`${APIURL}/passwords/${data.id}`, data);
export const deletePassword = (id) => axios.delete(`${APIURL}/passwords/${id}`);
```

to let us make the requests to our back end to save the password entries.

Then we create our MobX store by creating `store.js` and add:

```
import { observable, action, decorate } from "mobx";

class PasswordsStore {  
  passwords = [];
  setPasswords(passwords) {  
    this.passwords = passwords;  
  }  
}

PasswordsStore = decorate(PasswordsStore, {  
  passwords: observable,  
  setPasswords: action  
});

export { PasswordsStore };
```

We have the `passwords` field which can be observed for the latest value if we wrap the `observer` function provided by MobX outside a component. The `setPasswords` is used to set the latest password entries in the store so that they can be propagated to the components.

Finally, in `index.html` , we replace the existing code with:

```
<!DOCTYPE html>  
<html lang="en">  
  <head>  
    <meta charset="utf-8" />  
    <link rel="shortcut icon" href="%PUBLIC_URL%/favicon.ico" />  
    <meta name="viewport" content="width=device-width, initial-scale=1" />  
    <meta name="theme-color" content="#000000" />  
    <meta  
      name="description"  
      content="Web site created using create-react-app"  
    />  
    <link rel="apple-touch-icon" href="logo192.png" />  
    <!--  
      manifest.json provides metadata used when your web app is installed on a  
      user's mobile device or desktop. See [https://developers.google.com/web/fundamentals/web-app-manifest/](https://developers.google.com/web/fundamentals/web-app-manifest/)  
    -->  
    <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />  
    <!--  
      Notice the use of %PUBLIC_URL% in the tags above.  
      It will be replaced with the URL of the `public` folder during the build.  
      Only files inside the `public` folder can be referenced from the HTML.Unlike "/favicon.ico" or "favicon.ico", "%PUBLIC_URL%/favicon.ico" will  
      work correctly both with client-side routing and a non-root public URL.  
      Learn how to configure a non-root public URL by running `npm run build`.  
    -->  
    <title>Password Manager</title>  
    <link  
      rel="stylesheet"  
      href="[https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css](https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css)"  
      integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T"  
      crossorigin="anonymous"  
    />  
  </head>  
  <body>  
    <noscript>You need to enable JavaScript to run this app.</noscript>  
    <div id="root"></div>  
    <!--  
      This HTML file is a template.  
      If you open it directly in the browser, you will see an empty page. You can add webfonts, meta tags, or analytics to this file.  
      The build step will place the bundled scripts into the <body> tag. To begin the development, run `npm start` or `yarn start`.  
      To create a production bundle, use `npm run build` or `yarn build`.  
    -->  
  </body>  
</html>
```

to change the title and add the Bootstrap CSS.

Now we can run the app by running `set PORT=3001 && react-scripts start` on Windows or `PORT=3006 react-scripts start` on Linux.

To start the back end, we first install the `json-server` package by running `npm i json-server`. Then, go to our project folder and run:

```
json-server --watch db.json
```

In `db.json`, change the text to:

```
{  
  "passwords": [  
  ]  
}
```

So we have the `passwords` endpoints defined in the `requests.js` available.
