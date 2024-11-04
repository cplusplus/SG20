## Program Design: Containers {#cont}

_Skeleton descriptions are typeset in italic text,_
_so please don't remove these descriptions when editing the topic._

### Overview

_Provides a short natural language abstract of the module’s contents._
_Specifies the different levels of teaching._

------------------------------------------------------------------------
Level             Objective
----------------- ------------------------------------------------------
Foundational      Using standard containers

Main              Extending standard containers and day-to-day usages

Advanced          ---

------------------------------------------------------------------------

### Motivation

_Why is this important?_
_Why do we want to learn/teach this topic?_

Storing data is an essential part of computations.
We use abstractions to make it easier to reason about and work with the data.
This leads to grouping related data variables together in data structures to give the grouping a name and to be able to make multiple instances of that data structure.
Data structures are therefore foundational building blocks for program design and are present in almost every program. 

Data structures come in many different forms, but there are special data structures that group objects of related types together.
In C++ these collections of data are called containers.
The C++ standard library provides a wide range of such common containers.
To make algorithms more universally applicable to containers, the standard library defines a common interface.
This way, containers build a bridge between algorithms and how data is organized.


### Topic introduction

_Very brief introduction to the topic._

### Foundational: Using standard containers {#cont-found}

#### Background/Required Knowledge

A student:

* "for loops"
* "defining variables"
* "main function"

#### Student outcomes

_A list of things "a student should be able to" after the curriculum._
_The next word should be an action word and testable in an exam._
_Max 5 items._

A student should be able to:

1. setup and add objects to a container
2. work with objects that are stored in a container

#### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._

* On a foundational level, avoid using iterators when teaching containers to prevent problems, such as iterator invalidation or dangling iterators.
* Avoid going deep into the template notation
* Teach people to not use `vector<bool>`

#### Points to cover

_This section lists important details for each point._

* Creating containers, adding objects, iterating over them using range based or index based for loops.
* `vector`, `string`, `unordered_map`, `unordered_set`
* Notation for having container of different value types with angle brackets


### Main: Extending standard containers and day-to-day usages {#cont-main}

#### Background/Required Knowledge

* Basic understanding of standard algorithms [[Program Design: Algorithms - Foundational]][1]
* Basic understanding of classes and class templates [[User-defined Types: Class Templates - Foundational]][2]

#### Student outcomes

A student should be able to:

1. make effective use of the standard containers.
2. make use of iterators to iterate over a sequence and call algorithms.
3. make a proper choice what container to use based on its characteristics.
4. write a container class template for a specific need (based on a standard container).
5. make use of common container idioms.

#### Caveats

* Iterator invalidation
* When extending standard containers, prefer delegation over inheritance

#### Points to cover

* Alternative ways of iterating over a container using iterators
* Adapting or extending standard containers (e.g., writing wrapper types with additional semantics)
* Discuss the different characteristics and trade-offs of standard containers
* Common idioms (e.g., find-erase)
* Usage of end-of-sequence iterators [[Program Design: Iterators - Foundational]][3]
* [Optional] Using containers together with ranges [[Program Design: Ranges - Foundational]][4]


### Advanced

_These are important topics that are not expected to be covered but provide
guidance where one can continue to investigate this topic in more depth._

* creating your own STL compatible containers from the ground up
* using containers with non-default allocators

[1]: ../program-design/algorithms.md
[2]: ../user-defined-types/class-templates.md
[3]: ../program-design/iterators.md
[4]: ../program-design/ranges.md
