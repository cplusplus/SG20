## C++ compilation model: Translation units {#translunits}

_Skeleton descriptions are typeset in italic text,_
_so please don't remove these descriptions when editing the topic._

### Overview

_Provides a short natural language abstract of the module’s contents._
_Specifies the different levels of teaching._

------------------------------------------------------------------------
Level             Objective
----------------- ------------------------------------------------------
Foundational      

Main              ---

Advanced          ---

------------------------------------------------------------------------

### Motivation

_Why is this important?_
_Why do we want to learn/teach this topic?_

### Topic introduction

_Very brief introduction to the topic._

_TODO:
_introduce notion of object file

C++ Compilation model allows the developer to seperate their 
declarations and definitions into various files so as to:

* organize code logically,
* facilitate reuse,
* reduce rebuild times,
* reduce file sizes and scopes,
* avoid naming collisions,
* and produce compiled libraries. 


### Foundational: Building code from multiple files

#### Background/Required Knowledge

A student:

1. Is able to define a variable, function, or class
2. Is able to access declarations from either module import or header inclusion

Questions:
modules and/or functions?


#### Student outcomes

_A list of things "a student should be able to" after the curriculum._
_The next word should be an action word and testable in an exam._
_Max 5 items._

A student should be able to:

1. create a declaration for variables, functions, and classes separate from their definitions
2. compile and link code from multiple implementation files
3. explain how includes or imports work within their translation unit

#### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._

#### Points to cover

_This section lists important details for each point._

Declarations and definitions can be within same file

### Main: Organizing code across multiple translation units

#### Background/Required Knowledge

* All of the above.

#### Student outcomes

A student should be able to:

1. package code into libraries
2. explain trade-offs for placing code in header files vs implementation files
3.
4.
5.

#### Caveats

#### Points to cover

### Advanced

_These are important topics that are not expected to be covered but provide
guidance where one can continue to investigate this topic in more depth._

A student should be able to:

1. explain how an anonymous namespace functions within their translation unit
2. One-definition-rule shennanigans
3. Pimpl pattern
4. Template definitions in translation unit it's used in?

