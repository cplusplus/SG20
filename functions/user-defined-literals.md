# Functions: user-defined literals
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
    <td>Foundational knowledge</td>
    <td>using and understanding UDLs</td>
  </tr>
  <tr>
    <td>Advanced</td>
    <td>implementing your own UDLs</td>
  </tr>
  <tr>
    <td>Further studies</td>
    <td>Advanced use (<code>"{}, {}!"_fmt("Hello", "World")</code>)</td>
  </tr>
</table>

## Motivation

_Why is this important?_
_Why do we want to learn/teach this topic?_

* Allows clearer expression of intent in C++.
* `std::string`: `"Hello, world!"s`
* `std::chrono`: `3h + 10m + 5s`

## Topic introduction

_Very brief introduction to the topic._

* Explain the existence of user defined literals. Example: `12m + 17s` is terse,
  expressive and type safe.

## Foundational knowledge: Using UDLs

### Background/Required Knowledge

A student:
* knows how to form numeric literals e.g. `1.5f` means a `float` of value `1.5`.
* is familiar with the major C++ types:
  * `bool` (Boolean type)
  * `int`  (Integer type)
  * `double` (Floating-point type)
  * `std::string` (Text type)
  * `std::vector` (Collection type)
* knows that namespaces exist, and namespace `std`.
* knows what using-declarations and using-directives are.

### Student outcomes

_A list of things “a student should be able to” after the curriculum._
_The next word should be an action word and testable in an exam._
_Max 5 items._

A student should be able to:

1. use `using namespace std::string_literals`\[1].
2. recognise UDLs in code that they are reading.
3. figure out which UDL definitions for a used type exist.
4. identify parts of the standard library that make use of UDLs.
5. prevent the dangers of temporaries created with `"blah"s` as well as with
   `std::string{"blah"}`.
6. effectively selects the right set of namespaces in using-directives from the
   sub-namespaces `std::literals`.

\[1]: explain that it's okay to use a using-directive to "activate" UDLs.

### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._

* A student gets confused by the similarities and differences between built-in
  suffixes and UDLs and between UDLs from different namespaces.
* A student "activates" two suffixes with the same signature from different
  namespaces.

### Points to cover

_This section lists important details for each point._

## Advanced: implementing UDLs

### Background/required knowledge

* All of the above.

### Student outcomes

A student should be able to:

1. write a UDL operator of their own.
2. separate unrelated UDLs into distinct namespaces.

### Caveats

### Points to cover

## Further studies

_These are important topics that are not expected to be covered but provide
guidance where one can continue to investigate this topic in more depth._