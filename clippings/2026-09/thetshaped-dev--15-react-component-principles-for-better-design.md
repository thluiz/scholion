---
url: "https://thetshaped.dev/p/15-react-component-principles-for-better-design"
captured_at: "2026-09-25T21:24:37+01:00"
title: "15 React Component Principles & Best Practices for Better Software Architecture & Design"
domain: "thetshaped-dev"
---

I’ve been using React since 2018, and since then, I’ve been talking with many colleagues about a set of good practices and principles for building React Applications. I’m planning to curate a series of articles that consist of a set of React principles and best practices for better software architecture and design. In the first article of the series, I’m focusing on React Components.

I’m bringing my curiosity and experience in Software Design & Architecture into building well-designed, maintainable, and scalable React applications.

The series of articles aims to bridge the gap between React beginners and those growing as React experts and engineers.

> _**Caution:**_ This is not a beginner’s guide, so most of the shared concepts require some React knowledge.

If you find yourself in that situation, refresh your fundamentals and continue.

As with every piece of advice and information on the Internet, don’t go to extremes without questioning it.

> **💡 Take everything as an opinion. Software can be built in multiple ways.**

In this article, we will go through:

*   Function Components vs. Class Components
    
*   Name of Components
    
*   Helper Functions
    
*   Repetitive Markup
    
*   Component’s Size and Length
    
*   Props
    
*   Ternary Operators
    
*   Lists Mapping
    
*   Hooks vs. HOCs and Render Props
    
*   Custom Hooks
    
*   Render Functions
    
*   Error Boundaries
    
*   Suspense
    

Class components can be verbose and harder to manage. Function components are simpler and easier to understand. With function components, you have better readability. The things you have to remember and think about are a lot smaller compared to class components’s state management, lifecycle methods, etc.

The only exception for using Class Components is when you want to use Error Boundaries.

**⛔ Avoid** using class components

```
class Counter extends React.Component {
  constructor(props) {
    super(props);
    this.state = { count: 0 };
  }
  
  increment() {
    this.setState(state => ({
      count: state.count + 1
    }));
  }

  return (
    <div>
      Count: {this.state.count}
      <button onClick={() => this.increment()}>Increment</button>
    </div>
  );
}
```

**✅ Prefer** using function components

```
function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      Count: {count}
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
```

Nameless components can make debugging difficult and reduce code readability. Named components improve the stack trace and make your codebase easier to navigate, manage, and understand. You can navigate between errors much easier when you use named components.

**⛔ Avoid** using nameless components

```
export default () => <div>Details</div>;
```

**✅ Prefer** naming your components

```
export default function UserDetails() {
  return <div>User Details</div>;
}
```

Nesting helper functions inside components can clutter the component and make it harder to read. Keeping helper functions outside the components improves readability and separates concerns.

**⛔ Avoid** nesting your helper functions inside your components if closure is not needed

```
function UserProfile({ user }) {
  function formatDate(date) {
    return date.toLocaleDateString();
  }
  return <div>Joined: {formatDate(user.joinDate)}</div>;
}
```

**✅ Prefer** moving these helper functions outside the component (before it, so you can read the file from top to bottom)

```
function formatDate(date) {
  return date.toLocaleDateString();
}

function UserProfile({ user }) {
  return <div>Joined: {formatDate(user.joinDate)}</div>;
}
```

Hardcoding repetitive markup makes the code harder to maintain and update. Extracting repetitive markup with maps/loops and configuration objects makes the code more maintainable and readable. It simplifies updates and additions, as changes only need to be made in one place (inside the configuration object).

**⛔ Avoid** hardcoding repetitive markup

```
function ProductList() {
  return (
    <div>
      <div>
        <h2>Product 1</h2>
        <p>Price: $10</p>
      </div>
      <div>
        <h2>Product 2</h2>
        <p>Price: $20</p>
      </div>
      <div>
        <h2>Product 3</h2>
        <p>Price: $30</p>
      </div>
    </div>
  );
}
```

**✅ Prefer** extracting repetitive markup with configuration objects and loops

```
const products = [
  { id: 1, name: 'Product 1', price: 10 },
  { id: 2, name: 'Product 2', price: 20 },
  { id: 3, name: 'Product 3', price: 30 }
];
  
function ProductList() {
  return (
    <div>
      {products.map(product => (
        <div key={product.id}>
          <h2>{product.name}</h2>
          <p>Price: ${product.price}</p>
        </div>
      ))}
    </div>
  );
}
```

Large and lengthy components can be difficult to understand, maintain, and test. Smaller and more focused components are easier to read, test, and maintain. Each component has a single responsibility, reason to change and rerender, making the codebase more modular and easier to manage.

**⛔ Avoid** big and nasty components

```
function UserProfile({ user }) {
  return (
    <div>
      <div>
        <img src={user.avatar} alt={`${user.name}'s avatar`} />
        <h2>{user.name}</h2>
      </d
      <div>
        <h3>Contact</h3>
        <p>Email: {user.email}</p>
        <p>Phone: {user.phone}</p>
      </div>
    </div>
  );
}
```

**✅ Prefer** small and easy-to-read components

```
function UserProfile({ user }) {
  return (
    <div>
      <ProfileHeader avatar={user.avatar} name={user.name} /
      <ProfileContact email={user.email} phone={user.phone} />
    </div>
  );
}
```

Repeating props can make the component harder to read and maintain. Destructuring the props improves readability and makes the code more consious. It reduces repetition and makes it clear which props are being used.

**⛔ Avoid** repeating props everywhere in your component

```
function UserProfile(props) {
  return (
    <>
      <div>Name: {props.name}</div>
      <div>Email: {props.email}</div>
    </>
  );
}
```

**✅ Prefer** destructuring your props

```
function UserProfile({ name, email }) {
  return (
    <>
      <div>Name: {name}</div>
      <div>Email: {email}</div>
    </>
  );
}
```

Having too many props can make a component complex and harder to understand. Fewer props makes a component easier to use and understand.

Most of the time, when we have a component with > 5 props, it’s a sign that it can be splitted. But that’s not a hard rule to follow because as an “okay” example the `input` field has many props but it’s not needed to be splitted.

When we have < 5 props, it’s a sign that something can be extracted. Maybe we have too much data into a single component.

> **Less props ⇒ less reasons to change and rerender.**

**⛔ Avoid** using many props (maybe > 5, you should split it, but not always, ex: `input`)

```
function UserProfile({ 
  name, email, avatarUrl, address, paymentProfiles 
}) {
  return (
    <div>
      <img src={avatarUrl} alt={`${name}'s avatar`} />
      <h1>{name}</h1>
      <p>Email: {email}</p>
      <p>Address: {address}</p>
      <ul>
        {paymentProfiles.map(paymentProfile => (
          <li key={paymentProfile.id}>
	    <h2>{paymentProfile.cardNumber}</h2>
	    <p>{paymentProfile.cardName}</p>
	  </li>
        ))}
      </ul>
    </div>
  );
}
```

**✅ Prefer** using small number of props (maybe < 5)

```
function UserProfile({ user }) {
  return (
    <Info name={user.name} email={user.email} avatarUrl={user.avatarUrl} />
    <Address address={user.address} />
    <PaymentProfiles paymentProfiles={user.paymentProfiles} />
  );
}
```

Passing many primitives can clutter the component and make it harder to manage related data. Grouping related props into an object simplifies the component interface and improves readability. It makes the code cleaner and easier to understand by logically grouping related data.

**⛔ Avoid** passing primitives when props are somehow related

```
function Address({ street, city, state, zip }) {
  return (
    <div>
      <p>Street: {street}</p>
      <p>City: {city}</p>
      <p>State: {state}</p>
      <p>ZIP: {zip}</p>
    </div>
  );
}
```

**✅ Prefer** passing an object, grouping the props

```
function Address({ address }) {
  const { street, city, state, zip } = address;

  return (
    <div>
      <p>Street: {street}</p>
      <p>City: {city}</p>
      <p>State: {state}</p>
      <p>ZIP: {zip}</p>
    </div>
  );
}
```

Nested ternary operators can make the code difficult to read and maintain. Clear if-else statements enhance hode readability and maintainability. They make the control flow easier to understand and debug.

**⛔ Avoid** nested or multiple ternary operators - hard to read and follow

```
function Greeting({ isLoggedIn, age }) {
  return (
    <div>
      {isLoggedIn ? (
       age > 18 ? (
          "Welcome back!"
        ) : (
          "You are underaged!"
        )
      ) : (
        "Please log in."
      )}
    </div>
  );
}
```

**✅ Prefer** if-else blocks and explicit return statements in your component

```
function Greeting({ isLoggedIn, age }) {
  if (!isLoggedIn) {
    return <div>Please log in.</div>;
  }

  if (age > 18) {
    return <div>Welcome back!</div>;
  }

  return <div>You are underaged!</div>;
}
```

Directly mapping over lists in the return statement can make the component cluttered and harder to read. Separating the map operation from the main component into individual component from makes the code cleaner and easier to read. The main component’s boilerplate becomes simpler. It separates the rendering logic from the component’s main structure, enhancing readability.

> **The main component doesn’t care about the details.**

**⛔ Avoid** using map function over a list inside your component

```
function PaymentProfilesPage({ paymentProfiles }) {
  return (
    <h1>Payment Profiles:</h1>
    <ul>
      {paymentProfiles.map(paymentProfile => (
        <li key={paymentProfile.id}>
          <h2>{paymentProfile.cardNumber}</h2>
          <p>{paymentProfile.cardName}</p>
        </li>
      ))}
    </ul>
  );
}
```

**✅ Prefer** moving the map function outside the component - easy to read. The main component doesn’t care about the details.

```
function PaymentProfilesPage({ paymentProfiles }) {
  return (
    <h1>Payment Profiles:</h1>
    <PaymentProfilesList paymentProfiles={paymentProfiles} />
  );
}
```

HOCs (Higher-Order Components) and render props patterns have been traditionally used for sharing logic and behavior across components. However, these patterns can lead to complex and deeply nested component trees, making the code harder to read, debug, and maintain. Hooks offer a more straightforward and declarative approach to encapsulating and reusing logic within functional components.

Hooks offer a more simpler mental model - we compose a set of functions to access external logic and behavior, making the overall JSX template simpler to read and understand.

**⛔ Avoid** using HOCs and render props

```
function UserProfileForm() {
  return (
    <Form>
      {({ values, handleChange }) => (
        <input
          value={values.name}
          onChange={e => handleChange('name', e.target.value)}
        />
        <input
          value={values.password}
          onChange={e => handleChange('password', e.target.value)}
        />
      )}
    </Form>
  );
}
```

**✅ Prefer** using hooks

```
function UserProfileForm() {
  const { values, handleChange } = useForm();

  return (
    <Form>
      <input
        value={values.name}
	onChange={e => handleChange('name', e.target.value)}
      />
      <input
        value={values.password}
	onChange={e => handleChange('password', e.target.value)}
      />
    </Form>
  );
}
```

Duplicating logic leads to code redundancy and makes maintaince harder. Custom hooks allow for code reuse, making components cleaner and more maintainable. With custom hooks, the logic is encapsulated, reducing duplication and improving readability. It also makes its testing much easier.

**⛔ Avoid** duplicating logic across components

```
function UserList() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch('/api/users')
      .then(response => response.json())
      .then(data => setUsers(data));
  }, []);

  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}

function ProductList() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch('/api/products')
      .then(response => response.json())
      .then(data => setProducts(data));
  }, []);

  return (
    <ul>
      {products.map(product => (
        <li key={product.id}>{product.name}</li>
      ))}
    </ul>
  );
}
```

**✅ Prefer** encapsulating and reusing logic with custom hooks

```
function useFetch(url) {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch(url)
      .then(response => response.json())
      .then(data => setData(data));
  }, [url]);

  return data;
}

function UserList() {
  const users = useFetch('/api/users');

  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}

function ProductList() {
  const products = useFetch('/api/products');

  return (
    <ul>
      {products.map(product => (
        <li key={product.id}>{product.name}</li>
      ))}
    </ul>
  );
}
```

Nesting complex render functions inside components can clutter the component and make it harder to read, test, and maintain. Defining render functions outside the component or using separate components improvemes readability and maintainability. It keeps the main component clean and focuses on its primary purpose.

**⛔ Avoid** nesting your render functions inside your components

```
function UserProfile({ user }) {
  function renderProfileDetails() {
    return <div>{user.name} - {user.age}</div>;
  }

  return <div>{renderProfileDetails()}</div>;
}
```

**✅ Prefer** extracting your render functions outside your components - on top of them or separate components.

```
function renderProfileDetails(user) {
  return <div>{user.name} - {user.age}</div>;
}

// OR using a separate component
function ProfileDetails({ user }) {
  return <div>{user.name} - {user.age}</div>;
}

function UserProfile({ user }) {
  return (
    <div>
      {renderProfileDetails(user)}
      // OR
      <ProfileDetails user={user} />;
    </div>
  );
}
```

Unhandled errors can crash the whole application, affecting the user experience. Error Boundaries allow you to catch and handle errors gracefully, improving the application’s resilience. This ensures a better user experience by displaying fallback UIs, instead of crashing the entire app.

**⛔ Avoid** allowing errors in child components to crash the entire application

```
function App() {
  return <UserProfile />;
}
```

**✅ Prefer** using error boundaries to catch and handle errors in child component trees

```
function App() {
  return (
    <ErrorBoundary>
      <UserProfile />
    </ErrorBoundary>
  );
}
```

Manually managing loading states can be repetitive and error-prone. Suspense simplifies the handling of async operations by providing a declarative way to manage loading states. This reduces boilerplate code and makes the component logic cleaner.

**⛔ Avoid** manually handling loading states for async operations

```
function UserProfile() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/user')
      .then(response => response.json())
      .then(data => {
        setUser(data);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>{user.name}</h1>
      <p>{user.bio}</p>
    </div>
  );
}
```

**✅ Prefer** using Suspense to handle async operations and loading states gracefully

```
import { UserProfile } from './UserProfile';

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <UserProfile />
    </Suspense>
  );
}
```

1.  Favor Function Components over Class Components
    
2.  Name your Components
    
3.  Move Helper Functions Outside of Components
    
4.  Extract Repetitive Markup with Config Objects
    
5.  Manage the Component’s Size
    
6.  Destructure Props
    
7.  Manage the Number of Props
    
8.  Props - Objects vs. Primitives
    
9.  Manage Ternary Operators
    
10.  Abstract Lists Mapping into Separate Components
     
11.  Favor Hooks over HOCs and Render Props
     
12.  Reuse and Encapsulate Logic with Custom Hooks
     
13.  Extract Render Functions
     
14.  Use Error Boundaries
     
15.  Use Suspense
     

In upcoming articles, we will dive deeper into other crucial areas of React development, including state management, testing, application’s organization, and much more. Stay tuned to continue improving your skills and building better React apps.

[

![GraphQL Intro 101 (part 1)](https://substackcdn.com/image/fetch/$s_!WOrE!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fab4c8a87-7221-44d9-9baa-59b7014456ba_1456x1048.png)

](https://thetshaped.dev/p/graphql-intro-101-part-1)

[

![Step by Step Guide: Migrate a React App from Bootstrap to Tailwind CSS](https://substackcdn.com/image/fetch/$s_!d79_!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4c038258-27be-48d0-a395-46f2b216a966_5124x3452.jpeg)

](https://thetshaped.dev/p/step-by-step-guide-migrate-a-react-app-from-bootstrap-to-tailwind-css)

[

![Comparison Guide: Bootstrap vs. Tailwind CSS. When and What to choose?](https://substackcdn.com/image/fetch/$s_!VNyO!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7951a253-98ca-458f-9f5b-ff429abbe3db_1280x720.jpeg)

](https://thetshaped.dev/p/comparison-guide-bootstrap-vs-tailwind-css-when-what-to-choose)
