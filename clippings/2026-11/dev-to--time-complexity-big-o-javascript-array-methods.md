---
url: "https://dev.to/lukocastillo/time-complexity-big-0-for-javascript-array-methods-and-examples-mlg"
captured_at: "2026-11-16T01:11:14+00:00"
title: "Time complexity Big 0 for Javascript Array methods and examples."
domain: "dev-to"
---

Hello everyone, some weeks ago I started to study some computer science algorithms using JavaScript as the programming language, and normally after finished to implement an algorithm I like to calculated complexity with the Big 0 notation. That is the reason why I wanted to write this post, to understand the time complexity for the most used JS Array methods.

So, let's start with a quick definition of the method, his time complexity, and a small example.

## [](#mutator-methods)Mutator Methods.

**1\. `push()` - 0(1)**  
Add a new element to the end of the array.  

```
const names = ['Luis','John','Jose'];
names.push("Aaron");
console.log(names); // (4) ["Luis", "John", "Jose", "Aaron"]
```

**2\. `pop()` - 0(1)**  
Delete the last element of the array  

```
const names = ['Luis','John','Jose','Aaron'];
console.log(names.pop()); //Aaron
console.log(names); // (3) ["Luis", "John", "Jose"]
```

**3\. `shift()` - 0(n)**  
Delete the first element of the array  

```
const names = ['Luis','John','Jose','Aaron'];
console.log(names.shift()); // Luis
console.log(names); // (3) ["John", "Jose", "Aaron"]
```

**4\. `unshift()` - 0(n)**  
Add one or more elements in the beginning of the array  

```
const names = ['Luis','John','Jose'];
console.log(names.unshift("Aaron")); // 4
console.log(names); // (4) ["Aaron", "Luis", "John", "Jose"]
```

**5\. `splice()` - 0(n)**  
Remove, add or replace a new element indicate by index.  

```
const names = ['Luis','John','Jose','Aaron'];
console.log(names.splice(0,0,"Fernando")); // Add Michelle
console.log(names.splice(0,1,"Michelle")); // replace Fernando to Michelle
console.log(names.splice(0,1)); // remove Michelle
console.log(names);
```

**6\. `sort()` - 0(n log(n))**  
Modify the array, ordered by a compare Function, or if this compare function is not provided the default order is by the position of the Unicode values in the array.  

```
const names = ['Luis','Jose','John','Aaron'];
console.log(names.sort()); // (4) ["Aaron", "John", "Jose", "Luis"]

/*complex sorting*/
const users = [
    {name:'Luis', age:25},
    {name:'Jose', age:20},
    {name:'Aaron', age:40}
];
const compareFuc = (item1,item2) => {
  return item1.age - item2.age;
};
console.log(users.sort(compareFuc));
/**
 [{name: "Jose", age: 20}, {name: "Luis", age: 25}, {name: "Aaron", age:40}]
 */
```

## [](#accessor-methods)Accessor methods

**1\. `concat()` - 0(n)**  
Create a new array with the union of two or more arrays.  

```
const names1 = ["Luis","Jose"];
const names2 = ["John","Aaron"];
const newArray = names1.concat(names2,["Michelle"]);
console.log(newArray); // (5) ["Luis", "Jose", "John", "Aaron", "Michelle"]
```

**2\. `slice()` - 0(n)**  
Return a copy of a sub array between two index, start and end.  
_Important Note:_ if you modify the original array, the value also will be modify in the copy array.  

```
const users = [
  {name:'Luis', age:15},
  {name:'Jose', age:18},
  {name:'Aaron', age:40}
];

const  adults = users.slice(1, users.length);
console.log(adults); // (2) [{name: "Jose", age: 18}, {name: "Aaron", age: 40}]
```

**3\. `indexOf()` - 0(n)**  
Return the first index of the element that exists in the array, and if not exists return`-1`.  

```
const names = ['Luis','Jose','John','Aaron'];
console.log(names.indexOf("John")); // 2
console.log(names.indexOf("Michelle")); // -1
```

## [](#iteration-methods)Iteration methods

**1\. `forEach()` - 0(n)**  
Just execute a function for each element in the array.  

```
const names = ['Luis','Jose','John','Aaron'];

names.forEach(item => {
    console.log(item);
}); 
/* Print all user names
  Luis Jose John  Aaron 
*/ 
```

**2\. `map()` - 0(n)**  
Create a new array with the result of the callback function (this function is executed for each item same as forEach)  

```
const users = [
    {name:'Luis', age:15},
    {name:'Jose', age:18},
    {name:'Aaron', age:40}
];
const userDescriptions = users.map(item => {
   return `Hello my name is ${item.name} and I have ${item.age} years old.`
});
console.log(userDescriptions); 
/*["Hello my name is Luis and I have 15 years old.",
 "Hello my name is Jose and I have 18 years old.",
 "Hello my name is Aaron and I have 40 years old."] */
```

**3\. `filter()` - 0(n)**  
Create a new array with the elements that apply the given filter condition as true.  

```
const users = [
  {name:'Luis', admin:true},
  {name:'Jose', admin:true},
  {name:'Aaron'}
];
const adminUsers =  users.filter(item => item.admin);
console.log(adminUsers); // [{name: "Luis", admin: true},{name: "Jose", admin: true}]
```

**4\. `reduce()` - 0(n)**  
Return a single value after applying the reduction function for each element.  

```
const users = [
  {name:'Luis', age:15},
  {name:'Jose', age:18},
  {name:'Aaron', age:40}
];

const reducer= (accumulator, item)=> accumulator + item.age;
const totalAge =  users.reduce(reducer,0);
const ageAverage = totalAge / users.length;
console.log(`Total ${totalAge}, Average ${ageAverage}`); // Total 73, Average 24.333333333333332
```

## [](#bonus)Bonus!!!

**1\. `some()` - 0(n)**  
Return a boolean value as true if found one or more item that apply the given condition, and return false if not (also if the array is empty).  

```
const users = [
  {name:'Luis', admin:true},
  {name:'Jose'},
  {name:'Aaron'}
];
const adminExists = users.some(item => item.admin);
console.log(adminExists); // true
```

**2\. `every()` - 0(n)**  
This function Return a boolean value as true if all the items apply the given condition, and false if not.  

```
const users = [
  {name:'Luis', active:true},
  {name:'Jose', active:true},
  {name:'Aaron', active:false}
];
const isAllUsersActive = users.every(item => item.active);
console.log(isAllUsersActive); // false
```

## [](#conclusion)Conclusion

I think that it is very important to understand the time complexity for the common Array methods that we used to create our algorithms and in this way we can calculte the time complexity of the whole structure.

I hope that this information was helpful for you. If you have any questions please, left in the comment section. All the comments are welcome.😉
