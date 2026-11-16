---
url: "https://bridge-global.com/blog/the-magic-of-a-single-integer-number-to-contain-huge-information"
captured_at: "2026-11-16T02:05:23+00:00"
title: "How To Store Huge Information in A Single Integer Value"
domain: "bridge-global-com"
---

Here I am trying to explain how we can effectively store huge pieces of information by consuming less space.

For this, I am taking an example of **“How to store all roles of a user in a single integer value.”**

When developing application software, a programmer should write a module for handling Roles and Permissions for the users. Suppose we have the following roles.

**Role**

Anonymous

Admin

SuperAdmin

General Manager

Senior Manager

Data Entry

View Only

ReportsOnly

 The programmer will usually assign an integer ID to each role like the following:

**Id**

**Role**

1

Anonymous

2

Admin

3

SuperAdmin

4

General Manager

5

Senior Manager

6

Data Entry

7

View Only

8

ReportsOnly

Suppose the user with ID 1 has the roles of **Data Entry** and **View Only.**

In this case, the programmer can save user permissions in two different ways:

1.  Create a string with roles separated by a comma, for example, **6,7** and this can be stored in the column. While retrieving back, we can split the string by comma and find the role IDs. (The problem with this approach is that the permission data will end up with a big string)
2.  Each role IDs can be stored against user id by consuming each column for each role ID as follows:

**User ID**

**Role ID**

1

6

1

7

In this case, we need a separate table for storing information on user roles.

But there is another better way we can store any combination of user roles as a single integer value. For this, the Role ID should be a number which is the power of 2.

**Id**

**Role**

**2****0** = 1

Anonymous

**2****1** \= 2

Admin

**2****2** = 4

SuperAdmin

**2****3** \= 8

General Manager

**2****4** \= 16

Senior Manager

**2****5** \= 32

Data Entry

**2****6** \= 64

View Only

In this case, the user with Id 1 has the roles of **Data Entry** and **View Only** can be stored as 32 + 64 = **96**.

In one single integer column, we can store the user roles combination. Here we can store **96** as user permission.

Well, We have stored the user roles information, Now we need to extract the roles from the single integer number. Let find out how we can do this.

We need a reverse algorithm to do this.

For example, user permission is **96**.

*   Divide the number with 2 and record the remainder of it,
*   Divide the answer again and again until you get answer zero
*   Take the iteration number of all items in which that the remainder is 1
*   Take the power 2 of that number

**Eg:**

**Iteration**

1

96

96/2

Answer: 48, Remainder: 0

2

48

48/2

Answer: 24, Remainder: 0

3

24

24/2

Answer: 12, Remainder: 0

4

12

12/2

Answer: 6, Remainder: 0

5

6

6/2

Answer: 3, Remainder: 0

**6**

3

3/2

Answer: 1, Remainder: **1**

**7**

1

1/2

Answer: 0, Remainder: **1**

Now find the items which have remainder 1, we have 6th and 7th iteration. So the split items can be calculated by

6th power of 2: 26\=32

7th power of 2: 27\=64

The C# code for splitting the values into corresponding power of 2 is given below

`public static List<long> GetSumOfPowerOfTwo(long n)     {         var remainders = new List<int>();         var powerOfTwo = new List<long>();         while (n > 0)         {             remainders.Add((int)n % 2);             n = n / 2;         }         for (var i = 0; i < remainders.Count; i++)         {             if (remainders[i] == 1)             {                 powerOfTwo.Add((long)Math.Pow(2, i));             }         }         return powerOfTwo;     }`

**_\* You can store any type of combination information in this way apart from user roles_**
