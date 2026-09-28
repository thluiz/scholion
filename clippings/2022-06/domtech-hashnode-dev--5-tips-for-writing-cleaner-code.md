---
url: "https://domtech.hashnode.dev/5-tips-for-writing-cleaner-code"
captured_at: "2022-06-01T22:26:59-03:00"
title: "5 Tips For Writing Cleaner Code"
domain: "domtech-hashnode-dev"
---

# 5 Tips For Writing Cleaner Code

Featured on Hashnode

### Table of contents

Hello everyone, in the past I have been guilty of writing code that was not so clean, and I'm sure I am not alone here. Over the years I have learnt from my mistakes and I thought I'd share with you some tips to help you improve your coding practices too.

### 1. Avoid Unnecessary Nesting

Nesting in code is something we do all the time, and although there's nothing inherently wrong with nesting, it can sometimes make code harder to read. One approach to help avoid this is to use the "Return Early" design pattern. It allows us to use the if statement as a guard clause to check for errors and return before executing any further code. It helps avoid the use of if/else and unnecessary nesting.

Let's assume we have a function where the if statement wraps the entire function:

```
function deleteItem(item) {
  if (item != null) {
    console.log("Deleting item");
    item.delete();
  }
}
```

Although there is essentially nothing wrong with this, we can make it cleaner by using a guard clause. So instead of checking to see if the item is not null, we negate this and return nothing if the item is null:

```
function deleteItem(item) {
  if (item == null) return;

  console.log("Deleting item");
  item.delete();
}
```

Both implementations behave identically, but as you can see the second implementation is obviously cleaner. Now let's look at an example of a nested if statement:

```
function saveItem(item) {
  if (item != null) {
    console.log("Validating");

    if (item.isValid()) {
      console.log("Saving item");
      item.save();
    }
}
```

Again, there is nothing really wrong with this implementation, but we can change the way we use the if statements to completely remove the nesting from this function:

```
function saveItem(item) {
  if (item == null) return;

  console.log("Validating");
  if (!item.isValid) return;

  console.log("Saving item");
  item.save();
}
```

As you can see, the "return early" approach can help make your code more linear, cleaner, and more readable. It's a simple technique that is easy to implement.

### 2. Use Object Destructuring For Function Parameters

Let's assume we have a function that takes an object as the parameter and performs some kind of operation on that object to return a new value. Without using object destructuring, we might get something like this:

```
// not so good
function getFullName(person) {
  const firstName = person.firstName;
  const lastName = person.lastName;
  return `${firstName} ${lastName}`;
}
```

This implementation works just fine, but we are creating two temporary references `firstName` and `lastName` when we don't really need to.

A better way to implement this is to use object destructuring. We can destruct the person object to get both the first name and last name in one line:

```
// better
function getFullName(person) {
  const { firstName, lastName } = person;
  return `${firstname} ${lastName}`;
}
```

We are able to take this a step further by destructuring the parameter directly, eliminating another line of code.

```
// even better
function getFullName({ firstName, lastName }) {
  return `${firstName} ${lastName}`;
}
```

A much more elegant way of writing the same function.

### 3. Avoid Side Effects By Using Pure Functions

When writing functions, it is best to avoid modifying any variables outside of that function.

```
// bad
let items = 5;
function changeNumber(number) {
  items = number + 3;
  return items;
}
changeNumber(5);
```

Here whenever we call this function, it will modify the `items` variable which is best to avoid doing, since we are technically modifying our code which can lead to unpredictable or undesirable behaviour. The other thing we want to avoid is reliance on external variables within a function. If the `items` variable suddenly didn't exist or changed it's data type, it will obviously cause problems we want to avoid.

So instead, using a pure function, we can rewrite the function to the following:

```
// good
function addThree(number) {
  return number + 3;
}
```

Here we have removed the dependency of the external variable and made the function return a new value. It's functionality is now fully self contained therefore it's behaviour is now fully predictable. A much better approach.

### 4. Keep Functions Simple

When writing functions, it can be tempting to put multiple things in one place:

```
function signUpAndValidate() {
// Do a heap of stuff here
}
```

but this can quickly lead to spaghetti code and unwanted bugs. It is best to keep functions responsible for one thing only. This is a better approach:

```
function signUp() {
}
function validate() {
}
```

### 5. Always Use Meaningful Variable Names

When coding it can be easy to be lazy and use single letter variable names at times, but this just causes you headaches down the track. here are a few tips to help you out.

1. Functions perform actions, so use **verbs** when naming them.

   ```
   // bad
   function passwordValidation() {
   }
   // good
   function validatePassword() {
   }
   ```
2. Use **is** when using boolean type:

   ```
   const isValidPassword = validatePassword("abcd");
   ```
3. Use plurals for arrays:

   ```
   const animal = ["cat", "dog", "bird"];
   const animals = ["cat", "dog", "bird"];
   ```
4. When using callback functions, always use a meaningful name when iterating:

   ```
   // don't do this
   animals.forEach((a) => {
   console.log(a);
   });
   // do this
   animals.forEach((animal) => {
   console.log(animal);
   });
   ```
