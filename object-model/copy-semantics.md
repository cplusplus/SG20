# C++ object model: copy semantics
_Skeleton instructions are typeset in italic text._

## Overview

_Provides a short natural language abstract of the module’s contents._
_Specifies the different levels of teaching._

<table>
  <thead>
    <th>Level</th>
    <th>Objectives</th>
  </thead>
  <tr>
    <td>Foundational</td>
    <td>understanding how and when are copies made</td>
  </tr>
  <tr>
    <td>Main</td>
    <td>implementing user-defined copy operations</td>
  </tr>
  <tr>
    <td>Advanced</td>
    <td>special cases: copy elision</td>
  </tr>
</table>

## Motivation

_Why is this important?_
_Why do we want to learn/teach this topic?_

Copy semantics allows the user to define how objects of a class get replicated and interact on a value level.

## Topic introduction

_Very brief introduction to the topic._

Explains when and how objects are copied.

## Foundational: How and when are copies made

### Background/Required Knowledge

A student is able to:
* explain what a C++ type is?               [[C++ object model: types]][1]
* explain what an object is?                [[C++ object model: objects]][2], [[C++ object model: constant objects]][3]
* define and understand class invariants?

It helps when a student is able to:
* use move semantics                        [[C++ object model: move semantics]][4]
* explain special member functions          [[C++ object model: special member functions]][5]

### Student outcomes

_A list of things "a student should be able to" after the curriculum._
_The next word should be an action word and testable in an exam._
_Max 5 items._

A student should be able to:

1. explain what copy semantics accomplish
  * establishing "equivalent" object state in another object
2. explain difference between copying a reference and copying a value\*
3. explain where copies are made

\* In other languages these differences are sometimes referred to as shallow and deep copy.

### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._

* Compiler-provided copy operations may result in ownership problems (e.g., `char*`). These ownership problems can generally be solved by using types whose copy operations have the appropriate semantics, e.g., `std::string` instead of `char*` to hold string values.

### Points to cover

_This section lists important details for each point._

* Principle of copying
  * Copying of types, which follow the rule of zero
  * Copying of types, with user defined copy operations
  * Copying an object does not change the original
* Practical applications
  * `std::unique_ptr`  (has no copy)
  * Strings (copies the value) 


## Main: Implementing user-defined copy operations

### Background/Required Knowledge

A student is able to:
* identify special member functions       [[C++ object model: special member functions]][5]

It helps when a student is able to:
* use move semantics                      [[C++ object model: move semantics]][4]
* explain the rule of zero                [[C++ object model: rule-of-zero]][7]
* explain the rule of five                [[C++ object model: rule-of-five]][6]

### Student outcomes

_A list of things "a student should be able to" after the curriculum._
_The next word should be an action word and testable in an exam._
_Max 5 items._

A student should be able to:
* explain when they have to implement the copy operations for their own type
  * Copy constructor
  * Copy assignment operator
* implement copy operations for their own types
* _Optional_: explain when copying with basic and strong exception guarantees is useful

### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._

* Intricacies when implementing copy operations:
  * Examples of how _not_ to write copy operations (e.g., C++03 `std::auto_ptr`)

### Points to cover

_This section lists important details for each point._

* Copy constructors and copy assignment operators
  * How compiler generates default copy operations
  * =default, =delete (No copy)
  * How-to write your own copy operations
  * Rule-of-five
  * Copy assignment operators can be ref-qualified to avoid assigning into temporary objects.

## Advanced

_These are not expected to be covered but provide guidance where one can
continue to investigate this topic in more depth._

When can copies be elided and when does the standard guarantee copy elision.
References:
* [Abseil tip of the Week #166](https://abseil.io/tips/166)
* [cppreference - Copy elision](https://en.cppreference.com/w/cpp/language/copy_elision)

[1]: ../object-model/types.md
[2]: ../object-model/objects.md
[3]: ../object-model/constant-objects.md
[4]: ../object-model/move-semantics.md
[5]: ../object-model/special-member-functions.md
[6]: ../object-model/rule-of-five.md
[7]: ../object-model/rule-of-zero.md
