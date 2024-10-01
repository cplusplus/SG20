# Module name: Passing Parameters by Reference
_Skeleton descriptions are typeset in italic text,_
_so please don't remove these descriptions when editing the topic._

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
    <td>Avoiding copies using const-reference modifiers</td>
  </tr>
  <tr>
    <td>Main</td>
    <td>Using references to modify external data</td>
  </tr>
  <tr>
    <td>Advanced</td>
    <td></td>
  </tr>
</table>

## Motivation

_Why is this important?_
_Why do we want to learn/teach this topic?_

## Topic introduction

_Very brief introduction to the topic._

Explain what a reference type is and how it constrasts with a value type.

## Foundational: Using reference types to avoid copies

### Background/Required Knowledge

A student is able to:

* Define and call a function with parameters

### Student outcomes

_A list of things "a student should be able to" after the curriculum._
_The next word should be an action word and testable in an exam._
_Max 5 items._

A student should be able to:

1. Use const-refernce types for function arguments
2. Explain what considerations to take when deciding whether or not to use a const-reference type

### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._

### Points to cover

_This section lists important details for each point._

* No copy of the data is made when taken by constant reference
* A constant reference value cannot be modified
* The lifetime of a constant reference cannot be expected to extend beyond the lifetime of the function, so the reference should not be saved off for future use.
* Taking a reference is not always a time or space savings. Modern machines may use 8-bytes to reference a 4-byte integer, for instance.

## Main: Using references to modify external data 

### Background/Required Knowledge

* All of the above

### Student outcomes

A student should be able to:

1. Define and utilize a non-const reference for passing values out of a function

### Caveats

### Points to cover

* If the function does not intend to modify the value, const-references should be preferred
* A reference value may be modified
* The lifetime of a reference cannot be expected to extend beyond the lifetime of the function, so the reference should not be saved off for future use.
* Taking a reference is not always a time or space savings. Modern machines may use 8-bytes to reference a 4-byte integer, for instance.

## Advanced

_These are important topics that are not expected to be covered but provide
guidance where one can continue to investigate this topic in more depth._

