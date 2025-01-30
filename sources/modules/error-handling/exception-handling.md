### Overview

_Provides a short natural language abstract of the module’s contents._
_Specifies the different levels of teaching._

------------------------------------------------------------------------
Level             Objective
----------------- ------------------------------------------------------
Foundational      Standards exception hierarchy

Main              Exception guarantees

Advanced          ---

------------------------------------------------------------------------

### Motivation

_Why is this important?_
_Why do we want to learn/teach this topic?_

Exception handling is used to be able to continue the program in case of
exceptional situations (like requesting a ridiculous amount of memory:
`bad_alloc`).

### Topic introduction

_Very brief introduction to the topic._

There are other forms of handling difficult situations, but here we concentrate
on exception handling and the peculiarities/characteristics of it. Because
there are different forms, we should know when to use which type of handling
special situations.

### Foundational: Standards exception hierarchy {#eh-found}

#### Background/Required Knowledge

A student:

* should know about basic and user-defined types [[Type system: fundamental types]][1] [[Type system: user-defined types]][2]
* should know about flow of control [???]
* should know about blocks and statements [???]

#### Student outcomes

_A list of things "a student should be able to" after the curriculum._
_The next word should be an action word and testable in an exam._
_Max 5 items._

A student should be able to:

1. Explain how some `std::` calls may cause an exception
2. Discern the different standard exception types
3. Write simple try … except code (e.g., out of memory, vector at indexing)
4. Explain on a “simplified” conceptual level what happens when an exception is thrown and is bubbled up through the callers until it is caught


#### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._

* Exceptions should be used for exceptional situations and should not be used to manage normal control flow.

#### Points to cover

_This section lists important details for each point._

* Exception hierarchy from the standard library
* Common library functions that may throw exceptions
* Basic handling exceptions: try/catch/throw
* How exceptions bubble up until caught


### Main: Exception guarantees {#eh-main}

#### Background/Required Knowledge

* RAII
* Order of construction/destruction of class members

#### Student outcomes

A student should be able to:

1. Explain the four different exception guarantees
2. Explain the exception guarantees that the standard library containers offer.
3. Explain what happens when a exception is thrown in constructor


#### Caveats

* Make sure code is designed with RAII in mind to prevent resources leaking during exception handling, when the stack is unwound.
* Care should be taken in constructor design to make all fully constructed members deleted when the stack unwinding mechanism is activated.

#### Points to cover

* Exception guarantees: Nothrow/Strong/Basic/No
* Rethrowing an exception

### Advanced: Exception-safe containers and edge cases {#eh-advanced}

_These are important topics that are not expected to be covered but provide
guidance where one can continue to investigate this topic in more depth._

* Rethrowing a modified exception
* Writing exception safe containers

[1]: ../type-system/fundamental-types.md
[2]: ../type-system/user-defined-types.md