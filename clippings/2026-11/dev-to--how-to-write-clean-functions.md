---
url: "https://dev.to/manu4216/how-to-write-clean-functions-bmh"
captured_at: "2026-11-16T01:34:30+00:00"
title: "How to write clean functions"
domain: "dev-to"
---

The following ideas are inspired by the book [Clean Code](https://www.amazon.com/Robert-Martin-Clean-Code-Collection-ebook/dp/B00666M59G) by Robert C. Martin.

## [](#introduction)Introduction

This tutorial will demonstrate a set of basic principles that will help you write cleaner functions, that is, easy to read and easy to update.

Most coding articles usually focus on the latest hot topics. There are not many articles about simple and sometimes undervalued ideas, like how to write clean code and clean functions.

In this tutorial, you will practice writing clean functions, starting from an initial code sample, and improving it step by step using the following principles:

1.  Small
2.  Do one thing
3.  One level of abstraction
4.  Less arguments the better
5.  No side effects

These principles are relevant for any programming language, however the code samples will use JavaScript.

## [](#prerequisites)Prerequisites

Basic knowledge of JavaScript.

## [](#step-0-starting-code)Step 0 — Starting code

You will start with the following code sample, which does not satisfy any of the principles of clean functions:  

```
const getProductPrice = async (product, isSaleActive, coupon) => {
  let price;

  try {
    price = await getPrice(product);
    product.userCheckedPrice = true;
  } catch (err) {
    return { result: null, error: err };
  }

  if (coupon && coupon.unused && coupon.type === product.type) {
    price *= 0.5;
  } else if (isSaleActive) {
    price *= 0.8;
  }

  return { result: Math.round(price * 100) / 100, error: null };
};
```

Enter fullscreen mode Exit fullscreen mode

## [](#step-1-small)Step 1 — Small

Making an effort to keep your functions small, ideally between 1–5 lines, is the easiest way to make a function cleaner. Keeping this principle in mind will force you to reduce your function to its bare minimum.

Go ahead, try to refactor this functions on your own first, then come back here and compare with the solution proposed bellow.

We can make the main `getProductPrice` function smaller by simply extracting some of its functionality into another `getPriceWithCouponOrSale` function.  

```
const getPriceWithCouponOrSale = (price, product, isSaleActive, coupon) => {
  if (coupon && coupon.unused && coupon.type === product.type) {
    return price * 0.5;
  }
  if (isSaleActive) {
    return price * 0.8;
  }
  return price;
}

const getProductPrice = async (product, isSaleActive, coupon) => {
  let price;

  try {
    price = await getPrice(product);
    product.userCheckedPrice = true;
  } catch (err) {
    return { result: null, error: err };
  }

  const price = getPriceWithCouponOrSale(price, product, isSaleActive, coupon);

  return { result: Math.round(price * 100) / 100, error: null };
};
```

Enter fullscreen mode Exit fullscreen mode

## [](#step-2-do-one-thing)Step 2 — Do one thing

In the starting code sample, the function `getProductPrice` does many things, all contained in the body of the function:

*   it gets the original price
*   it updates a product boolean
*   it handles the error
*   it applies a coupon or a sale
*   it rounds the result

In order to make a function do less things, you have 2 options:

*   move functionality one level down, by extracting a separate specialized function, like you did in step 1 with `getPriceWithCouponOrSale` function.
*   or move functionality one level up, at the caller level. By applying this approach, we could move the error handling out, and have a `getProductPrice` function focused on one thing: getting the product price.

```
const getProductPrice = async (product, isSaleActive, coupon) => {
  const originalPrice = await getPrice(product);
  product.userCheckedPrice = true;
  const actualPrice = getPriceWithCouponOrSale(originalPrice, product, isSaleActive, coupon);
  return Math.round(actualPrice * 100);
};
```

Enter fullscreen mode Exit fullscreen mode

For simplicity, the error handling on the caller level, is not reproduced.

## [](#step-3-one-level-of-abstraction)Step 3 — One level of abstraction

This is something often overlooked, but it can make a major difference in achieving a clean, readable function. Mixing levels of abstraction inside a function is always confusing.

For instance, in the starting code sample, besides the main level of abstraction (getting the final price), there is a mix of other levels of abstractions: error handling, details of price calculation, details of rounding up.

The first 2 have already been removed in the previous steps. Go ahead and make the function cleaner by getting rid of the low level details of rounding up. The improved version will then look like so:  

```
const getProductPrice = async (product, isSaleActive, coupon) => {
  const originalPrice = await getPrice(product);
  product.userCheckedPrice = true;
  const actualPrice = getPriceWithCouponOrSale(originalPrice, product, isSaleActive, coupon);
  return getRoundedValue(actualPrice);
};
```

Enter fullscreen mode Exit fullscreen mode

This might not look like a big difference, but in reality, such things are like broken windows: once you have one in your code, new ones will add up.

## [](#step-4-less-arguments-the-better)Step 4 — Less arguments the better

The ideal number of arguments is, in order: 0, 1, 2 arguments. Having more than 2 arguments becomes increasingly difficult to reason about, and it might be a sign that your function is doing too many things.

In the previous step, `getProductPrice` and `getPriceWithCouponOrSale` use 3, and 4 arguments respectively. This is without doubt difficult to reason about. This can be simplified by simply extracting some of the arguments on top.

Go ahead and try to find ways to pass less arguments to these functions.

In the following proposed solution, this will be done by:

*   lifting `price` argument on top of `getPriceWithCouponOrSale` and make it return a fraction. This function will be renamed to `getReducedPriceFraction`.
*   lifting `isSaleActive` and `coupon` on top of `getProductPrice`. They will be replaced with the new `reducedPriceFraction`.

Here is how the improved code will look like:  

```
const getReducedPriceFraction = (product, isSaleActive, coupon) => {
  if (coupon && coupon.unused && coupon.type === product.type) {
    return 0.5;
  }
  if (isSaleActive) {
    return 0.8;
  }
  return 1;
}

const reducedPriceFraction = getReducedPriceFraction(product, isSaleActive, coupon);

const getProductPrice = async (product, reducedPriceFraction) => {
  const originalPrice = await getPrice(product);
  product.userCheckedPrice = true;
  const actualPrice = originalPrice * reducedPriceFraction;
  return getRoundedValue(actualPrice);
};
```

Enter fullscreen mode Exit fullscreen mode

This approach can be taken further by repeating it one more time, which leads to the following code, in which `getReducedPriceFraction` only uses 2 arguments, thus becoming much cleaner:  

```
const isCouponCompatible = (product, coupon) => coupon.type === product.type;

const getReducedPriceFraction = (isSaleActive, isCouponValid) => {
  if (isCouponValid) {
    return 0.5;
  }
  if (isSaleActive) {
    return 0.8;
  }
  return 1;
}

const isCouponValid = coupon && coupon.unused && isCouponCompatible(product, coupon);
const reducedPriceFraction = getReducedPriceFraction(isSaleActive, isCouponValid);

const getProductPrice = async (product, reducedPriceFraction) => {
  const originalPrice = await getPrice(product);
  product.userCheckedPrice = true;
  const actualPrice = originalPrice * reducedPriceFraction;
  return getRoundedValue(actualPrice);
};
```

Enter fullscreen mode Exit fullscreen mode

## [](#step-5-no-side-effects)Step 5 — No side effects

Side effects make a function do unexpected things. Without having a closer look, you might have missed that `getProductPrice` function also has a side effect: updating the `product` object.

This is dangerous because it can cause unexpected behaviours. For instance, in some other part of your code base, you might need to literally only get the product price, and introduce a bug because of this unexpected side effect.

A clean function should do only one thing, without any hidden side effects. Such side effect should instead be done in plain sight, such as at the caller level, or in a separate function called `updateProduct`.

In our previous code, you can remove the side effect and have it at the caller level (not reproduced). Once removed, you are left with a very clean function:  

```
const getProductPrice = async (product, reducedPriceFraction) => {
  const originalPrice = await getPrice(product);
  const actualPrice = originalPrice * reducedPriceFraction;
  return getRoundedValue(actualPrice);
};
```

Enter fullscreen mode Exit fullscreen mode

## [](#conclusion)Conclusion

Congratulations! You succeeded in drastically improving the starting code sample by applying these 5 easy principles one by one.

Hopefully this will help you identify opportunities to improve your own code base.

Clean code and clean functions are a joy to read and work on. Spread that joy by writing clean functions!
