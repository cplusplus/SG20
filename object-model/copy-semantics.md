# C++ object model: copy semantics

## Overview

_Provides a short natural language abstract of the module’s contents.
Specifies the different levels of teaching._

<table>
  <thead>
    <th>Level</th>
    <th>Objectives</th>
  </thead>
  <tr>
    <td>Foundational knowledge</td>
    <td></td>
  </tr>
  <tr>
    <td>Advanced</td>
    <td></td>
  </tr>
  <tr>
    <td>Further studies</td>
    <td></td>
  </tr>
</table>

This module explains the concept of copying values and its varieties.
It introduces:

* copy constructor
* copy-assingment operator
* default implementations
* to be completed...

## Motivation

_Why is this important? Why do we want to learn/teach this topic?_

Copy semantics allows the user to determine how objects of a class get
replicated and interact on a value level.

## Topic introduction

_Very brief introduction to the topic._

## Foundational knowledge: *TODO*

### Background/Required Knowledge

_What do students need to know before starting this topic? (Dependencies)_

* What is a type? [C++ object model: types]
* What is an object? [C++ object model: objects],
  [C++ object model: constant objects]
* What are class invariants?
* How to express class invariants?
* How is object identity established? (i.e. understanding what this is;
  very basic pointer knowledge)

_What knowledge will help in understanding certain aspects but is not
necessarily required? (Soft Dependencies)_

* [C++ object model: move semantics]
* [C++ object model: special member functions]
* Value types
* Reference types

_What other modules contain related information?  (Related topics)_

* [C++ object model: value semantics]
* [C++ object model: rule-of-five]
* [C++ object model: rule-of-zero]

### Student outcomes

_A list of things “a student should be able to” after the curriculum. The next
word should be an action word and testable in an exam. Max 5 items._

1. Explain what copy semantics accomplish
  1. Establishing “equivalent” object state in another object
2. Explain when they have to implement the copy operations for their own type
  1. Copy constructor
  2. Copy assignment operator
3. Implement copy operations for their own types
4. Explain difference between deep and shallow copy
  1. Explain correspondence to value and reference types (not just
     lvalue-references)
5. Optional: Implement copy operations with both basic and strong exception
   guarantee

### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._

* Compiler-provided (shallow) copies may result in ownership problems
  (e.g. `char*`).
* Maybe: Copying going wrong? (e.g. `std::auto_ptr`).

### Points to cover

_This section lists important details for each point._

* Principle of copying
  * Copying of trivially copyable types
  * Copying of non-trivial class types
  * Copying an object does not change the original
* Copy Flavours
  * Shallow copy
  * No copy
  * Transfer copy
  * Deep copy
  * Shared copy
* Copy constructors and copy assignment operators
  * How compiler generates default copy operations
  * `=default`, `=delete` (No copy)
  * How to write your own copy operations
  * Rule-of-five
  * Copy assignment operators can be ref-qualified to avoid assigning into
    temporary objects. (See example #1)
* Practical applications
  * `std::unique_ptr`  (no copy)
  * `std::auto_ptr` (transfer copy)
  * `std::shared_ptr` (shared copy)
  * strings (deep copy) 

## Advanced

TODO

## Further studies

_These are not expected to be covered but provide guidance where one can
continue to investigate this topic in more depth._
