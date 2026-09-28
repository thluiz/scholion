---
url: "https://golangdocs.com/errors-exception-handling-in-golang"
captured_at: "2022-03-29T11:02:30-03:00"
title: "Errors and Exception Handling in GoLang - GoLang Docs"
domain: "golangdocs-com"
---

# Errors and Exception Handling in GoLang

Errors are a language-agnostic part that helps to write code in such a way that no unexpected thing happens. When something occurs which is not supported by any means then an error occurs. Errors help to write clean code that increases the maintainability of the program.

## What is an error?

An error is a well developed abstract concept which occurs when an exception happens. That is whenever something unexpected happens an error is thrown. Errors are common in every language which basically means it is a concept in the realm of programming.

## Why do we need Error?

Errors are a part of any program. An error tells if something unexpected happens. Errors also help maintain code stability and maintainability. Without errors, the programs we use today will be extremely buggy due to a lack of testing.

## Errors in GoLang

GoLang has support for errors in a really simple way. Go functions returns errors as a second return value. That is the standard way of implementing and using errors in Go. That means the error can be checked immediately before proceeding to the next steps.

## Simple Error Methods

There are multiple methods for creating errors. Here we will discuss the simple ones that can be created without much effort.

### 1. Using the New function

GoLang errors **package** has a function called **New()** which can be used to create errors easily. Below it is in action.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22 | `package` `main`  `import` `(`  `"fmt"`  `"errors"`  `)`  `func e(v` `int``) (``int``, error) {`  `if` `v ==` `0` `{`  `return` `0``, errors.New(``"Zero cannot be used"``)`  `}` `else` `{`  `return` `2``*v, nil`  `}`  `}`  `func main() {`  `v, err := e(``0``)`  `if` `err != nil {`  `fmt.Println(err, v)` `// Zero cannot be used 0`  `}`  `}` |

### 2. Using the Errorf function

The fmt package has an Errorf() method that allows formatted errors as shown below.

|  |  |
| --- | --- |
| 1 | `fmt.Errorf(``"Error: Zero not allowed! %v"``, v)` `// Error: Zero not allowed! 0` |

## Checking for an Error

To check for an error we simply get the second value of the function and then check the value with the nil. Since the **zero value of an error is nil**. So, we check if an error is a nil. If it is then no error has occurred and all other cases the error has occurred.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18 | `package` `main`  `import` `(`  `"fmt"`  `"errors"`  `)`  `func e(v` `int``) (``int``, error) {`  `return` `42``, errors.New(``"42 is unexpected!"``)`  `}`  `func main() {`  `_, err := e(``0``)`  `if` `err != nil {` `// check error here`  `fmt.Println(err)` `// 42 is unexpected!`  `}`  `}` |

## Panic and recover

Panic occurs when an unexpected wrong thing happens. It stops the function execution. Recover is the opposite of it. It allows us to recover the execution from stopping. Below shown code illustrates the concept.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23 | `package` `main`  `import` `(`  `"fmt"`  `)`  `func f(s string) {`  `panic(s)` `// throws panic`  `}`  `func main() {`  `// defer makes the function run at the end`  `defer func() {` `// recovers panic`  `if` `e := recover(); e != nil {`  `fmt.Println(``"Recovered from panic"``)`  `}`  `}()`  `f(``"Panic occurs!!!"``)` `// throws panic`  `// output:`  `// Recovered from panic`  `}` |

## Creating custom errors

As we have seen earlier the function errors.New() and fmt.Errorf() both can be used to create new errors. But there is another way we can do that. And that is implementing the error interface.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7 | `type CustomError struct {`  `data string`  `}`  `func (e *CustomError) Error() string {`  `return` `fmt.Sprintf(``"Error occured due to... %s"``, e.data)`  `}` |

## Returning error alongside values

Returning errors are pretty easy in Go. Go supports [multiple return values](https://golangdocs.com/multiple-return-values-in-golang-functions). So we can return any value and error both at the same time and then check the error. Here is a way to do that.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15 | `import` `(`  `"fmt"`  `"errors"`  `)`  `func returnError() (``int``, error) {` `// declare return type here`  `return` `42``, errors.New(``"Error occured!"``)` `// return it here`  `}`  `func main() {`  `v, e := returnError()`  `if` `e != nil {`  `fmt.Println(e, v)` `// Error occured! 42`  `}`  `}` |

## Ignoring errors in GoLang

Go has the skip (-) operator which allows skipping returned errors at all. Simply using the skip operator helps here.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16 | `package` `main`  `import` `(`  `"fmt"`  `"errors"`  `)`  `func returnError() (``int``, error) {` `// declare return type here`  `return` `42``, errors.New(``"Error occured!"``)` `// return it here`  `}`  `func main() {`  `v, _ := returnError()` `// skip error with skip operator`  `fmt.Println(v)` `// 42`  `}` |
