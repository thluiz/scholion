---
url: "https://thetshaped.dev/p/9-react-testing-best-practices-for-better-test-design-quality"
captured_at: "2026-09-25T21:27:44+01:00"
title: "9 React Testing Best Practices for Better Design and Quality of Your Tests"
domain: "thetshaped-dev"
---

Many developers struggle to make their tests both effective and efficient.

Solid testing is a must-have if you care about your application, customers, and business.

As a Senior Software Engineer with experience in testing and software design, I’ve read, reviewed, and written many tests.

Over the years, I’ve distilled a set of best practices that significantly improved the quality and maintainability of my tests.

In this blog post, I will share 9 tips to help you write and design better tests in your React applications.

The Arrange-Act-Assert (AAA) pattern brings clarity and structure to your tests.

By dividing your test into three distinct parts, you make it easier to read, follow, understand, and maintain.

This pattern helps prevent tests from becoming complex and 🍝.

This ensures that each test focuses on a specific behavior of the app.

In summary, the Arrange-Act-Assert (AAA) pattern helps with readability and consistency, allowing you to grasp what the test is verifying for others and future you.

```
it('should toggle create payment profile dialog', async () => {
  // Arrange
  render(<PaymentProfiles />);

  // Act
  fireEvent.click(await screen.findByTestId(testIds.addButton));

  // Assert
  const dialog = await screen.findByRole('dialog');
  expect(dialog).toBeInTheDocument();
});
```

Sometimes we might not need the Act and that’s fine.

```
it('should display server error', async () => {
  // Arrange
  server.use(
    graphql.query('GetCardPaymentProfiles', (_, __, ctx) =>
      resDelay(ctx.status(500)),
    ),
  );
  render(<PaymentProfiles />);

  // Assert
  expect(await screen.findByTestId(testIds.error)).toBeInTheDocument();
});
```

Testing multiple functionalities in a single test can make bugs and issues hard to find.

It’s better to write smaller, focused tests that cover only one aspect of the component’s behavior and functionality.

This simplifies debugging and ensures each test has a clear purpose.

It also reduces the cognitive load when maintaining the tests since you’re focused only on one scenario.

**⛔ Avoid** testing too many things at once.

```
it('should increment and decrement the counter', () => {
  render(<Counter initialCount={0} />);
  
  fireEvent.click(screen.getByText('Increment'));
  
  expect(screen.getByTestId('count')).toHaveTextContent('1');
  
  fireEvent.click(screen.getByText('Decrement'));
  
  expect(screen.getByTestId('count')).toHaveTextContent('0');
});
```

**✅ Prefer** testing only one aspect of the component’s behavior and functionality.

```
it('should increment the counter', () => {
  render(<Counter initialCount={0} />);
  
  fireEvent.click(screen.getByText('Increment'));
  
  expect(screen.getByTestId('count')).toHaveTextContent('1');
});

it('should decrement the counter', () => {
  render(<Counter initialCount={1} />);
  
  fireEvent.click(screen.getByText('Decrement'));
  
  expect(screen.getByTestId('count')).toHaveTextContent('0');
});
```

Snapshot tests can be helpful but they can also become a maintenance headache.

They should be treated carefully.

Over-reliance on snapshots can lead to neglecting tests that don’t effectively test components’s scenarios and catch regressions.

If you have snapshots that are too broad, they will always fail due to insignificant changes.

As a rule of thumb, I prefer to add snapshot tests for “dummy” or [stateless](https://thetshaped.dev/p/react-component-mental-models) UI components and not for [stateful](https://thetshaped.dev/p/react-component-mental-models) ones.

This way if a style is not applied or changed due to a bug, the snapshot test will fail and someone will have to look into it.

Another place where snapshot tests can be useful is for critical components with stable structures.

> **Keep snapshot tests small and focused.**

```
it('should load and display invoices', async () => {
  renderComponent();

  expect(screen.getByTestId(testIds.loading)).toBeInTheDocument();

  await waitForElementToBeRemoved(() =>
    screen.getByTestId(testIds.loading),
  );

  expect(await screen.findByTestId(testIds.invoices)).toBeInTheDocument();
  expect(screen.getByTestId(testIds.invoices)).toMatchSnapshot();
});
```

Start by testing the most common and expected use cases of your components.

Ensure that the core functionality and business logic works as expected before diving into edge cases.

This way you verify that the component behaves correctly in the main case with normal conditions, providing a solid foundation for further testing.

> **If the core business case doesn’t work, what’s the chance that other edge cases will work as expected?**

```
describe('Invoices', () => {
  //
  // Happy Path
  //
  it('should load and display invoices', async () => {
    renderComponent();

    expect(screen.getByTestId(testIds.loading)).toBeInTheDocument();

    await waitForElementToBeRemoved(() =>
      screen.getByTestId(testIds.loading),
    );

    expect(await screen.findByTestId(testIds.invoices)).toBeInTheDocument();
    expect(screen.getByTestId(testIds.invoices)).toMatchSnapshot();
  });
});
```

After you verified that the happy path works as expected, continue with testing how your component handles edge cases and errors like invalid inputs, delayed requests, etc.

This ensures correctness and robustness by verifying that the component can handle real-world scenarios gracefully.

```
describe('Invoices', () => {
  //
  // Edge Cases
  //
  it('should load and display empty message', async () => {
    server.use(
      graphql.query('GetInvoices', (_, __, ctx) =>
        resDelay(
          ctx.status(200),
          ctx.data({
            viewer: { account: { invoices: { nodes: [] } } },
          }),
        ),
      ),
    );

    renderComponent();

    expect(await screen.findByText(/No Invoices/)).toBeInTheDocument();
  });
  
  it('should not display empty message if refetching data', async () => {
    queryClient.setDefaultOptions({
      queries: {
        refetchOnMount: 'always',
        initialData: [],
      },
    });

    renderComponent();

    expect(screen.getByTestId(testIds.loading)).toBeInTheDocument();

    expect(screen.queryByText(/No Invoices/)).toBeNull();

    await waitForElementToBeRemoved(() =>
      screen.getByTestId(testIds.loading),
    );

    expect(await screen.findByTestId(testIds.invoices)).toBeInTheDocument();

    expect(screen.queryAllByText(/PDF/)[0]).toBeInTheDocument();
  });
  
  //
  // Errors
  //
  it('should display server error', async () => {
    server.use(
      graphql.query('GetInvoices', (_, __, ctx) =>
        resDelay(ctx.status(500)),
      ),
	  );

	  renderComponent();

    expect(await screen.findByTestId(testIds.error)).toBeInTheDocument();
  });
});
```

Integration tests verify that different parts of your application work together as expected.

These type of tests have a higher chance to catch issues that unit tests might miss.

> **Integration tests provide confidence that the system works as a whole, not just isolated units.**

The ROI (Return on Investment) of the integration tests is much higher compared to unit tests and E2E tests.

This doesn’t mean you don’t need them but for sure you should have more integration tests.

> **The more your tests resembles the way your software is used, the more confidence they can give you.**

```
it('should log in and see the dashboard', async () => {
  render(<App />);
  
  fireEvent.change(screen.getByLabelText('Username'), { target: { value: 'testuser' } });
  fireEvent.change(screen.getByLabelText('Password'), { target: { value: 'password' } });
  fireEvent.click(screen.getByText('Log In'));
  
  expect(await screen.findByText('Welcome to your dashboard')).toBeInTheDocument();
});
```

Your tests should focus on your code and application, not the internal functionality of external libraries.

Trust that well-maintained libraries have their own tests.

Testing third-party modules can lead to fragile tests which can break when the library updates, no matter if you haven’t changed their usage.

**⛔ Avoid** testing the internals of third-party modules.

**✅ Prefer** testing how your component works with the third-party library.

```
it('should not display empty message if refetching data', async () => {
  queryClient.setDefaultOptions({
    queries: {
      refetchOnMount: 'always',
      initialData: [],
    },
  });

	renderComponent();

  expect(screen.getByTestId(testIds.loading)).toBeInTheDocument();

  expect(screen.queryByText(/No Invoices/)).toBeNull();

  await waitForElementToBeRemoved(() =>
    screen.getByTestId(testIds.loading),
  );

  expect(await screen.findByTestId(testIds.invoices)).toBeInTheDocument();

  expect(screen.queryAllByText(/PDF/)[0]).toBeInTheDocument();
});
```

If you have 100% test coverage, this doesn’t mean high-quality tests or no bugs at all.

It’s better to focus on meaningful tests, instead of adding tests chasing coverage metrics.

**⛔ Avoid** writing tests that only serve to increase test coverage.

```
//
// Meaningless test only to satisfy test coverage metrics
//
it('should log in and see the dashboard', async () => {
  render(<App />);
  // No assertions
});
```

**✅ Prefer** adding valuable tests that verify the component’s behavior and functionality.

```
it('should log in and see the dashboard', async () => {
  // Arrange
  render(<App />);
  
  // Act
  fireEvent.change(screen.getByLabelText('Username'), { target: { value: 'testuser' } });
  fireEvent.change(screen.getByLabelText('Password'), { target: { value: 'password' } });
  fireEvent.click(screen.getByText('Log In'));
  
  // Assert
  expect(await screen.findByText('Welcome to your dashboard')).toBeInTheDocument();
});
```

As your application and codebase evolve, some tests might become redundant or irrelevant.

Regularly review and clean up your tests.

> **Tests are part of the codebase, so they should be treated as such - regularly reviewed and updated.**

This reduces maintenance overhead and keeps your tests lean and efficient.

So when a feature is deprecated or a component is removed, delete the related tests.

[

![](https://substackcdn.com/image/fetch/$s_!Y2lg!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fef3b5ba4-e754-4a39-9a26-2213ca85269f_1280x720.png)

](https://substackcdn.com/image/fetch/$s_!Y2lg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fef3b5ba4-e754-4a39-9a26-2213ca85269f_1280x720.png)

[I want this!](https://petarivanovv9.gumroad.com/l/kltua)

Paid subscribers, you can get it here: **[🎁 Products for Paid Subscribers](https://thetshaped.dev/p/100-discount-code-for-products)**.

1.  Favor Arrange-Act-Assert (AAA) pattern
    
2.  Avoid testing too many things at once
    
3.  Be careful with snapshot tests
    
4.  Test the Happy Path first
    
5.  Test Edge Cases and Errors
    
6.  Focus on Integration tests
    
7.  Don’t test third-party libraries
    
8.  Don’t focus on test coverage percentage
    
9.  Remove unnecessary tests
    

You can find me on **[LinkedIn](https://www.linkedin.com/in/petarivanovv9/)** or **[Twitter](https://twitter.com/petarivanovv9)**.

I share daily practical tips to level up your skills and become a better engineer.

_Thank you for being a great supporter, reader, and for your help in growing to 11.9K+ subscribers this week 🙏_

This newsletter is funded by paid subscriptions from readers like yourself.

If you aren’t already, consider becoming a paid subscriber to receive the full experience!

Think of it as buying me a coffee twice a month, with the bonus that you also get all my templates and products for FREE.

[Check the benefits of the paid plan](https://thetshaped.dev/about#%C2%A7why-subscribe)

_You can also hit the like ❤️ button at the bottom to help support me or share this with a friend to [get referral rewards](https://thetshaped.dev/?r=643nm). It helps me a lot! 🙏_

*   **[7 Must-Know Lessons To Be A Better Engineer From Top Industry Leaders](https://read.highgrowthengineer.com/p/month-of-collabs-recap-2024?r=643nm&utm_campaign=post&utm_medium=web)** by [Jordan Cutler](https://open.substack.com/users/58854493-jordan-cutler?utm_source=mentions)
    
*   **[Amazon Frugal Architecture Explained](https://newsletter.systemdesign.one/p/frugal-architecture?r=643nm&utm_campaign=post&utm_medium=web)** by [Neo Kim](https://open.substack.com/users/135589200-neo-kim?utm_source=mentions)
    
*   **[Master The 5 Types of Mocks](https://craftbettersoftware.com/p/master-the-5-types-of-mocks?r=643nm&utm_campaign=post&utm_medium=web)** by [Daniel Moka](https://open.substack.com/users/5505375-daniel-moka?utm_source=mentions)
    
*   **[You don’t need to be a manager to have a successful career in the engineering industry](https://newsletter.eng-leadership.com/p/you-dont-need-to-be-a-manager-to?r=643nm&utm_campaign=post&utm_medium=web)** by [Gregor Ojstersek](https://open.substack.com/users/106098672-gregor-ojstersek?utm_source=mentions)
    
*   **[System design isn't a Cut & Paste job](https://newsletter.systemdesignclassroom.com/p/system-design-isnt-a-cut-and-paste?r=643nm&utm_campaign=post&utm_medium=web)** by [Raul Junco](https://open.substack.com/users/98661477-raul-junco?utm_source=mentions)
    
*   **[SQL vs NoSQL - 7 Key Differences You Must Know](https://blog.algomaster.io/p/sql-vs-nosql-7-key-differences?r=643nm&utm_campaign=post&utm_medium=web)** by [Ashish Pratap Singh](https://open.substack.com/users/83602743-ashish-pratap-singh?utm_source=mentions)
