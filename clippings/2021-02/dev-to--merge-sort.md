---
url: "https://dev.to/code_regina/merge-sort-1boo"
captured_at: "2021-02-13T08:45:19-03:00"
title: "Merge Sort - DEV Community 👩‍💻👨‍💻"
domain: "dev-to"
---

# DEV Community ‍‍

```
                   -Merge Sort: Introduction
                   -Merge Arrays: Implementation
```

### Merge Sort: Introduction

Merge sorting is a combination of merging and sorting, works by decomposing an array into smaller arrays, also known as a divide and conquer strategy. The process split up larger array into smaller sub arrays all the way down until get to 0 or 1 element, then building up a newly sorted array.

[![8bvvaj8buvhnjc5djmlx.png](dev-to--merge-sort/c9399314f7fb4ce8ea5ca0a3192f9a18.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--34J17wHs--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/8bvvaj8buvhnjc5djmlx.png)

### Merge Arrays: Implementation

#### Merge Sort Example

```
function merge(arr1, arr2){
    let results = [];
    let i = 0;
    let j = 0;
    while(i < arr1.length && j < arr2.length){
        if(arr2[j] > arr1[i]){
            results.push(arr1[i]);
            i++;
        } else {
            results.push(arr2[j])
            j++;
        }
    }
    while(i < arr1.length) {
        results.push(arr1[i])
        i++;
    }
    while(j < arr2.length) {
        results.push(arr2[j])
        j++;
    }
    return results;
}
merge([100,200], [1,2,3,5,6])
```

#### Most merge sort implementation use recursion.

```
function merge(arr1, arr2){
    let results = [];
    let i = 0;
    let j = 0;
    while(i < arr1.length && j < arr2.length){
        if(arr2[j] > arr1[i]){
            results.push(arr1[i]);
            i++;
        } else {
            results.push(arr2[j])
            j++;
        }
    }
    while(i < arr1.length) {
        results.push(arr1[i])
        i++;
    }
    while(j < arr2.length) {
        results.push(arr2[j])
        j++;
    }
    return results;
}

//Recrusive Merge Sort
function mergeSort(arr){
    if(arr.length <= 1) return arr;
    let mid = Math.floor(arr.length/2);
    let left = mergeSort(arr.slice(0,mid));
    let right = mergeSort(arr.slice(mid));
    return merge(left, sright);
}

mergeSort([10,24,76,73])
```

## Discussion (1)

![cc5f4526-0872-4ee6-b0b3-6dfaad5eccea.jpeg](dev-to--merge-sort/2fe4e69336215c91df3a3dadf710cb6c.jpeg)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg'%3e%3ctitle id='abzjx0wyz3314rvpvgnkcpk6llwi4uc0'%3eCollapse%3c/title%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg'%3e%3ctitle id='alln4upnw8mo8dlxw134789roudj45p2'%3eExpand%3c/title%3e %3c/svg%3e)

You still use arr functions instead of pure use like C / C ++ language, I tried to implement mergesort with Typescript on tsplayground like it doesn't really work.

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg'%3e%3ctitle id='aj96qztm6rgz0t8jquk2my5x6f5hptqi'%3eComment button%3c/title%3e%3c/svg%3e)
Reply](https://dev.to/code_regina/merge-sort-1boo#/code_regina/merge-sort-1boo/comments/new/1bcco)
