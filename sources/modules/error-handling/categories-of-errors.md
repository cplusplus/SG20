## Error handling: Categories of errors

_Skeleton descriptions are typeset in italic text,_
_so please don't remove these descriptions when editing the topic._

### Overview

_Provides a short natural language abstract of the module’s contents._
_Specifies the different levels of teaching._

------------------------------------------------------------------------
Level             Objective
----------------- ------------------------------------------------------
Foundational      Categories of errors

Main              Handling different categories of errors

Advanced          ---

------------------------------------------------------------------------

### Motivation

_Why is this important?_
_Why do we want to learn/teach this topic?_

Programs can run in a normal state or erroneous state. Students should be able
to identify different types of erroneous state and how to best handle them.

### Topic introduction

_Very brief introduction to the topic._

This topic is an umbrella topic that refers to the different topics for types of errors and error handling.

### Foundational: Categories of errors {#coe-found}

#### Background/Required Knowledge

A student:

* should know the basics about compilation [[C++ compilation model: Translation units - Foundational]][1]
* should know the basics about linkage [[C++ compilation model: Linkage - Foundational]][2]

#### Student outcomes

_A list of things "a student should be able to" after the curriculum._
_The next word should be an action word and testable in an exam._
_Max 5 items._

A student should be able to:

1. Describe different kinds of errors and exceptional situations that require different approaches of error handling.
2. Provide some examples of the different error categories.
3. Identify potential erroneous code sections and attribute them to different error categories.


#### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._

No caveats at present.

#### Points to cover

_This section lists important details for each point._

Errors can happen at different times during software lifetime.

* Compile-time errors
* Link-time errors
* Execution-time errors

There are different types of errors

* Logic errors (violations of logical preconditions)
* Run-time errors (errors during code execution)


### Main: Handling different categories of errors {#coe-main}

#### Background/Required Knowledge

#### Student outcomes

A student should be able to:

1. pick the right error handling approach for a given problem.
2. enumerate different error handling strategies.
3. make a clear distinction between error-handling code and normal-case handling code


#### Caveats

* The different error handling strategies have different trade-offs (runtime performance, readability, ...)
* The tradeoff space depends on the runtime context (embedded, ...)
* There also exist unhandable errors (e.g., ODR violations, undefined behavior)

#### Points to cover

* Exception handling [[Error handling: Exception handling - Foundational]][3]
* Returning a value indication failure [[Error handling: C-style error-codes - Foundational]][4]
* Terminating the program
* Improving error handling by having the error occur at an earlier stage in the software development cycle [[Error handling: Static assert - Foundational]][5]

### Advanced {#coe-advanced}

_These are important topics that are not expected to be covered but provide
guidance where one can continue to investigate this topic in more depth._

[1]: ../compilation-model/translation-units.md
[2]: ../compilation-model/linkage.md
[3]: ../error-handling/exception-handling.md
[4]: ../error-handling/c-style-error-codes.md
[5]: ../error-handling/static-assert.md
