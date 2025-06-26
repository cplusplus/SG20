## Debugging Errors: Compile-time errors {#compiletimeerr}

_Skeleton descriptions are typeset in italic text,_
_so please don't remove these descriptions when editing the topic._

### Overview

_Provides a short natural language abstract of the module’s contents._
_Specifies the different levels of teaching._

------------------------------------------------------------------------
Level             Objective
----------------- ------------------------------------------------------
Foundational      Understanding elementary error messages

Main              Dealing with most error messages

Advanced          ---

------------------------------------------------------------------------

### Motivation

_Why is this important?_
_Why do we want to learn/teach this topic?_

Compiler error messages can be hard to read and even compiler specific.
However, they contain valuable information for determining the cause of the compile-time errors.
Oftentimes the error messages are very verbose to give you the most precise information about the error context, so learning how to extract the valuable information from the error message is an important skill that one should acquire.

### Topic introduction

_Very brief introduction to the topic._

C++ compilers try to statically determine errors at compile time to shift detection of problems that would occur later on (e.g., at link time or run time) to earlier point in time, where they can be addressed in an earlier stage of the development process.
The error message that the compiler generates directly relates to the C++ language definition and precisely lays out why the code is not valid and where it does not comply with the language rules.

### Foundational: Understanding elementary error messages {#compiletimeerr-found}

#### Background/Required Knowledge

A student:

* definitions [[C++ Object Model: Definitions - Foundational]][1]

#### Student outcomes

_A list of things "a student should be able to" after the curriculum._
_The next word should be an action word and testable in an exam._
_Max 5 items._

A student should be able to:

1. distill the core of an elementary error message.
2. act on elementary error messages.
3. differentiate between different error kinds (e.g., type errors, syntax errors, ...).
4. give examples for different kinds of errors.


#### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._

* names mentioned in error message are presented in full detail and may not look exactly like specified by the programmer (e.g., `std::string` -> `std::basic_string<char>`)

#### Points to cover

_This section lists important details for each point._

* methodology of reading error messages
    * start with the first error
    * read top down
    * parse error message / pattern matching to error kinds
* linker errors [[Debugging Errors: Build errors - Foundational]][2]


### Main: Dealing with most error messages {#compiletimeerr-main}

#### Background/Required Knowledge

* compile-time programming [Soft dependency]

#### Student outcomes

A student should be able to:

1. locate the principle template involved in a template error message.
2. determine why a specific overload is chosen, from the compiler’s error message.
3. apply common debugging techniques in a constexpr context.

#### Caveats

* argument dependent lookup
* there is currently no good debugger support for constexpr context

#### Points to cover

* templates related error messages
* overload resolution related errors
* reasoning about errors during constexpr execution (consteval)
    * reverting to non-constexpr run-time debugging
    * employing static_assert

### Advanced

_These are important topics that are not expected to be covered but provide
guidance where one can continue to investigate this topic in more depth._

* Full error analysis, there are error messages that are out of the scope for students.
    * Complicated SFINAE constructs

[1]: ../object-model/definitions.md
[2]: ../debugging-errors/build-errors.md
