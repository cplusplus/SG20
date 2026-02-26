## Module name: Scoped Enumerations

_Skeleton descriptions are typeset in italic text,_
_so please don't remove these descriptions when editing the topic._

### Overview

_Provides a short natural language abstract of the module’s contents._
_Specifies the different levels of teaching._

------------------------------------------------------------------------
Level             Objective
----------------- ------------------------------------------------------
Foundational      Define and use scoped enumerations to provide named constants without collisions of values 

Main              Define and use scoped enumerations with special or particular values

Advanced          Compare and contrast scoped enumerations with legacy enumeration types

------------------------------------------------------------------------

### Motivation

_Why is this important?_
_Why do we want to learn/teach this topic?_

The use of scoped enumerations helps to avoid pollution of namespaces while grouping related constants within a type that can be referenced within code, itself. 

### Topic introduction

_Very brief introduction to the topic._

### Foundational: Defining and using scoped enumerations

#### Background/Required Knowledge

A student should have a foundational knowledge of [namespaces](TODO) and [control flow](TODO)

#### Student outcomes

_A list of things "a student should be able to" after the curriculum._
_The next word should be an action word and testable in an exam._
_Max 5 items._

A student should be able to:

1. define a scoped enumeration with multiple enumerators
2. define a scoped enumeration function parameter
3. use a scoped enumeration as a variable initialized to a enumerator of the scoped enumeration
4. define a switch statement with cases corresponding to various scoped enumeration enumerators
5. define enumerators with explicit integral values
6. predict the values of enumerators with no explicit value
7. describe the advantages of using scoped enumerations rather than global variables

#### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._

#### Points to cover

_This section lists important details for each point._

1. an implementation can recognize and warn when a switch statement is missing cases for a scoped enumeration
2. conversion to and from the underlying type must be done explicitly with a scoped enumeration

### Main: implementing *

#### Background/Required Knowledge

* All of the above.

#### Student outcomes

A student should be able to:

1. explicitly specify the value for some or all enumerators of a scoped enumeration
2. predict the value assigned for enumerators of a scoped enumeration following an explicitly assigned enumerator

#### Caveats

#### Points to cover

### Advanced

TODO : next time
1. implemenations may provide warnings when comparing values fo different 
2. comparison to old style enumerations

_These are important topics that are not expected to be covered but provide
guidance where one can continue to investigate this topic in more depth._
