## C++ object model: Definitions {#def}

_Skeleton descriptions are typeset in italic text,_
_so please don't remove these descriptions when editing the topic._

### Overview

_Provides a short natural language abstract of the module’s contents._
_Specifies the different levels of teaching._

------------------------------------------------------------------------
Level             Objective
----------------- ------------------------------------------------------
Foundational      Defining variables and ODR

Main              Defining for programs

Advanced          Special cases and peculiarities

------------------------------------------------------------------------

### Motivation

_Why is this important?_
_Why do we want to learn/teach this topic?_

* A definition is a declaration that supplies all that is needed for a complete entity
* `int baz = 42;`
* `void bar() { /* implementation */ }`
* `class Foo { /* class body */ };`

### Topic introduction

_Very brief introduction to the topic._

A definition extends a declaration, providing all that is needed for a complete
entity ,e.g., allocate memory for variables, provide the implementation for
functions, complete definitions of data and function members of a class.

### Foundational: Defining variables and ODR {#def-found}


#### Background/Required Knowledge


A student:

* is familiar with declarations [[C++ object model: declarations]][1]

#### Student outcomes

_A list of things "a student should be able to" after the curriculum._
_The next word should be an action word and testable in an exam._
_Max 5 items._

A student should be able to:

1. define a variable with a specific type `int baz = 42;`
2. define a function `void bar() {}`
3. define a class `class Foo {};`
4. explain the one definition rule


#### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._

No caveats at present.

#### Points to cover

_This section lists important details for each point._

* One definition rule (ODR)

### Main: Defining for programs {#def-main}


#### Background/Required Knowledge


* All of the above.
* is familiar with declarations [[C++ object model: declarations]][1]

#### Student outcomes

_A list of things "a student should be able to" after the curriculum._
_The next word should be an action word and testable in an exam._
_Max 5 items._

A student should be able to:

1. organize variables, functions, classes into multiple translation units, describing interface with declarations and providing the implementations with definitions without violating ODR.
2. distinguish between template declaration and definition

#### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._

* Putting a definition into a header file that is included more than once leads to ODR violations, possibly resulting in linker errors. 

#### Points to cover

_This section lists important details for each point._

### Advanced: Special cases and peculiarities {#def-advanced}

_These are important topics that are not expected to be covered but provide
guidance where one can continue to investigate this topic in more depth._

* ABI Incompatibilities: Different definitions of the same type in multiple object files can lead to subtle program errors.

[1]: ../object-model/declarations.md
