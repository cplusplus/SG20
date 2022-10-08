## C++ object model: Declarations

_Skeleton descriptions are typeset in italic text,_
_so please don't remove these descriptions when editing the topic._

### Overview

_Provides a short natural language abstract of the module’s contents._
_Specifies the different levels of teaching._

------------------------------------------------------------------------
Level             Objective
----------------- ------------------------------------------------------
Foundational      Declaring variables

Main              Declaring for programs

Advanced          Special cases and peculiarities

------------------------------------------------------------------------

### Motivation

_Why is this important?_
_Why do we want to learn/teach this topic?_

* Introduces a name and it’s type
* `int baz;`
* `void bar();`
* `class Foo;`

### Topic introduction

_Very brief introduction to the topic._

Introduce names and their associated type in a scope.

### Foundational: Declaring variables


#### Background/Required Knowledge


A student:

* is familiar with the basic C++ types:
    * bool (Boolean type)
    * int (Integer type)
    * double (Floating-point type)

#### Student outcomes

_A list of things "a student should be able to" after the curriculum._
_The next word should be an action word and testable in an exam._
_Max 5 items._

A student should be able to:

1. declare a variable with a specific type ‘int baz;’
2. declare a function ‘void bar();’
3. declare a class ‘class Foo;’
4. forward declare a user-defined type or a function
5. explain the difference between a definition and a declaration

#### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._

No caveats at present.

#### Points to cover

_This section lists important details for each point._

### Main: Declarations for programs


#### Background/Required Knowledge


* All of the above.
* Basic template syntax

#### Student outcomes

_A list of things "a student should be able to" after the curriculum._
_The next word should be an action word and testable in an exam._
_Max 5 items._

A student should be able to:

1. create header and source files with a declaration in the former and definition of a variable/function in the latter
2. declare type aliases to introduce a type with an alternative name ‘using std::string;’
3. write a forward template declaration

#### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._

* Declaring aliases can introduce name clashes
* Prefer using declaration’s over using directives in header files [link]
* The order of declarations dictates the order of initialization

#### Points to cover

_This section lists important details for each point._

### Advanced

_These are important topics that are not expected to be covered but provide
guidance where one can continue to investigate this topic in more depth._

* asm declaration
* using-enum-declaration
* extern "C" declarations
