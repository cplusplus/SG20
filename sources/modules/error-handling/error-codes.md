## Error handling: Error codes {#ecodes}

_Skeleton descriptions are typeset in italic text,_
_so please don't remove these descriptions when editing the topic._

### Overview

_Provides a short natural language abstract of the module’s contents._
_Specifies the different levels of teaching._

------------------------------------------------------------------------
Level             Objective
----------------- ------------------------------------------------------
Foundational      Handling error codes with `std::error_code`

Main              Designing APIs around `std::error_code`

Advanced          ---

------------------------------------------------------------------------

### Motivation

_Why is this important?_
_Why do we want to learn/teach this topic?_

C++ offers a type safe way of passing around errors, contrary to the C-style of error handling, by this, we prevent bugs when passing error codes.
Furthermore, error handling with error codes is more commonly used than exception handling, which only should be used in exceptional situations and in some environments is not feasible at all, e.g., in embedded or performance critical software.

### Topic introduction

_Very brief introduction to the topic._

C++ offers `std::error_code`, which encapsulates error codes in a type safe way.
This topic describes how to use these error codes.

### Foundational: Handling error codes with `std::error_code` {#eh-found}

#### Background/Required Knowledge

A student:

* should know that there are different ways of error handling [[Error handling: Categories of errors]][1]
* should know function return values

#### Student outcomes

_A list of things "a student should be able to" after the curriculum._
_The next word should be an action word and testable in an exam._
_Max 5 items._

A student should be able to:

1. write code to handle errors with `std::error_code`, e.g., obtain the message of the error code or check if an error occurred.
2. distinguish between the different categories and make justified decisions when to use which

#### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._

#### Points to cover

_This section lists important details for each point._

* a brief overview of `std::error_code` and how to use it

### Main: Designing APIs around `std::error_code` {#eh-main}

#### Background/Required Knowledge

* should know how to use reference parameters as an output parameter

#### Student outcomes

A student should be able to:

1. create an `error_code` and design API that work with `std:error_code`
2. write code that utilizes `std::error_category`
3. explain the difference between C-style error handling with errno and `std::error_code`
4. make effective use of the interface of `std::error_code`

#### Caveats

* reset errno before calling a function that might set errno (better pass an input parameter `std::error_code`)

#### Points to cover

* provide a full picture of `std::error_code` and it’s APIs
* `std::error_category` (explorative)

### Advanced

_These are important topics that are not expected to be covered but provide
guidance where one can continue to investigate this topic in more depth._

* implementing your own `error_category`

[1]: error-handling/categories-of-errors.md
