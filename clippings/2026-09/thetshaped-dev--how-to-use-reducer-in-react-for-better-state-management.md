---
url: "https://thetshaped.dev/p/how-to-use-reducer-in-react-for-better-and-simpler-state-management"
captured_at: "2026-09-25T21:29:05+01:00"
title: "How to use Reducer in React for better State Management: 2 effective ways for simpler design and architecture"
domain: "thetshaped-dev"
---

Managing a complex state in React can be tricky.

Using multiple _useState_ hooks for related data often results in nasty and hard-to-maintain components.

**By leveraging the** _**useReducer**_ **hook for related state variables, you can simplify your code.**

We can make it even simpler by **abstracting the reducer details** and **provide a deep and simpler interface to our components**.

Understanding these techniques is important.

**It will help you write more maintainable and scalable React components and applications.**

**⛔ Avoid using multiple \`useState\` hooks for states when they are somehow related.**

Managing related state variables with multiple _useState_ hooks can lead to messy and hard-to-maintain code.

This approach makes it difficult to update a state which depends on multiple state variables. It also increases the potential for bugs since it’s harder to trace how the state is updating.

**The more state variables you have, the more cluttered the component will be, and the less readable and maintainable.**

```
const App = () => {
  const [locationFilter, setLocationFilter] = useState("");
  const [queryFilter, setQueryFilter] = useState("");
  const [pageFilter, setPageFilter] = useState("");
  
  const handleLocationChange = (location) => {
    setLocationFilter(location);
  };
  
  const handleQueryChange = (query) => {
    setQueryFilter(query);
  };
  
  const handlePageChange = (page) => {
    setPageFilter(page);
  };
  
  return (
    ...
  );
};
```

**✅ Prefer using useReducer hook for states that can be grouped.**

By using _useReducer_, you can group the related state together into a single object which will be managed by a reducer function.

This way, we centralize the state logic.

**We make the code more organized, and easier to follow and understand.**

This also **simplifies complex state updates** and **reduces the potential for errors**.

By having this, we enhance the maintainability and scalability of our components.

```
const FILTERING_ACTION_TYPES = {
  selectLocation: 'SELECT_LOCATION',
  selectQueryFilter: 'SELECT_QUERY_FILTER',
  selectPage: 'SELECT_PAGE',
  ...
};

const initialState = {
  ...
};

const reducer = (state, action) => {
  switch (action.type) {
    case FILTERING_ACTION_TYPES.selectLocation: {
      return {
        ...
      }
    }
	  ...
  }
};


const App = () => {
  const [state, dispatch] = useReducer(reducer, initialState);
  
  const handleLocationChange = (location) => {
    dispatch({
      type: FILTERING_ACTION_TYPES.selectLocation,
      payload: location,
    })
  };
  
  ...
  
  return (
    ...
  );
};
```

**⛔ Avoid having a shallow hook for exposing the reducer details and functionality.**

Exposing the reducer’s internal details and the dispatch function in the components can lead to **tight coupling between our state management logic and our UI components**.

This can make the components more complex and less reusable since they become responsible for handling action types and payloads.

It also exposes implementation details that should remain encapsulated.

We also violate three SOLID principles - SRP, DIP, and ISP.

```
const App = () => {
  const [state, dispatch] = useReducer(reducer, initialState);
  
  const handleLocationChange = (location) => {
    dispatch({
      type: FILTERING_ACTION_TYPES.selectLocation,
      payload: location,
    })
  };
  
  ...
  
  return (
    ...
  );
};
```

**✅ Prefer abstracting the reducer details with a deep custom hook.**

By encapsulating the reducer logic and details within a custom hook, we **hide the implementation details**.

We provide a clean interface for the components and expose only what is needed to get the job done.

We **separate the state logic from the UI and component**.

This makes our components more clear, readable, maintainable, and focused only on the rendering logic and user interface.

Now, the SRP, DIP, and ISP are satisfied.

```
const useFilters = () => {
  const [state, dispatch] = useReducer(reducer, initialState);
  
  const updateLocationFilter = (location) =>
    dispatch({
      type: FILTERING_ACTION_TYPES.selectLocation,
      payload: location,
    });
    
  const updatePageFilter = (page) =>
    dispatch({
      type: FILTERING_ACTION_TYPES.selectPage,
      payload: page,
    });
    
  const updateQueryFilter = (query) =>
    dispatch({
      type: FILTERING_ACTION_TYPES.selectQuery,
      payload: query,
    });
    
  return {
    filteringState: state,
    updateLocationFilter,
    updatePageFilter,
    updateQueryFilter,
  };
};


const App = () => {
  const { 
    filteringState, 
    updateLocationFilter,
    updatePageFilter,
    updateQueryFilter
  } = useFilters();
  
  ...
  
  return (
    ...
  );
};
```

1.  **⛔ Avoid** using multiple _useState_ hooks for states when they’re are somehow related.
    
2.  **✅ Prefer** using _useReducer_ hook for states that can be grouped.
    
3.  **⛔ Avoid** having a shallow hook for exposing the reducer details and functionality.
    
4.  **✅ Prefer** abstracting the reducer details with a deep custom hook.
    

You can find me on **[LinkedIn](https://www.linkedin.com/in/petarivanovv9/)** or **[Twitter](https://twitter.com/petarivanovv9)**.

I share daily practical tips to level up your skills and become a better engineer.

_Thank you for being a great supporter, reader, and for your help in growing to 13.1K+ subscribers this week 🙏_

This newsletter is funded by paid subscriptions from readers like yourself.

If you aren’t already, consider becoming a paid subscriber to receive the full experience!

Think of it as buying me a coffee twice a month, with the bonus that you also get all my templates and products for FREE.

[Check the benefits of the paid plan](https://thetshaped.dev/about#%C2%A7why-subscribe)

_You can also hit the like ❤️ button at the bottom to help support me or share this with a friend to [get referral rewards](https://thetshaped.dev/?r=643nm). It helps me a lot! 🙏_

*   [How Google Search Works](https://newsletter.systemdesign.one/p/search-engine-architecture?r=643nm&utm_campaign=post&utm_medium=web) by [Neo Kim](https://open.substack.com/users/135589200-neo-kim?utm_source=mentions)
    
*   [Out With the Old: 3 Steps for a Successful Software Migration Plan](https://read.highgrowthengineer.com/p/3-steps-for-a-successful-migration?r=643nm&utm_campaign=post&utm_medium=web) by [Jordan Cutler](https://open.substack.com/users/58854493-jordan-cutler?utm_source=mentions) and [Maxi Ferreira](https://open.substack.com/users/86983746-maxi-ferreira?utm_source=mentions)
    

*   [Happy paths only exists in YouTube tutorials](https://newsletter.systemdesignclassroom.com/p/happy-paths-only-exists-in-youtube?r=643nm&utm_campaign=post&utm_medium=web) by [Raul Junco](https://open.substack.com/users/98661477-raul-junco?utm_source=mentions)
    
*   [How to have 27 hours in your day](https://open.substack.com/pub/zaidesanton/p/how-to-have-27-hours-in-your-day?r=643nm&utm_campaign=post&utm_medium=web) by [Anton Zaides](https://open.substack.com/users/121956618-anton-zaides?utm_source=mentions)
    
*   [Why Engineers Should Be at the Product Strategy Table?](https://open.substack.com/pub/thehustlingengineer/p/why-engineers-should-be-at-the-product?r=643nm&utm_campaign=post&utm_medium=web) by [Hemant Pandey](https://open.substack.com/users/58770480-hemant-pandey?utm_source=mentions) and [Wayne Chen](https://open.substack.com/users/249981550-wayne-chen?utm_source=mentions)
    
*   [Simple code is the best code](https://newsletter.eng-leadership.com/p/simple-code-is-the-best-code?r=643nm&utm_campaign=post&utm_medium=web) by [Gregor Ojstersek](https://open.substack.com/users/106098672-gregor-ojstersek?utm_source=mentions)
