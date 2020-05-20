# Module name: topic name
_Skeleton instructions are typeset in italic text._

## Overview

Functions in C++ may be overloaded with different numbers and types of parameters. It may be of value to specify default values for some number of parameters, to allow a consumer to avoid specifying parameters that rarely change, or to enable expanding the set of parameters while maintaining backward compatibility with existing consumers.

<table>
  <thead>
    <th>Level</th>
    <th>Objectives</th>
  </thead>
  <tr>
    <td>Foundational knowledge</td>
    <td>can make calls to functions with defaulted parameters, with or without defaulted parameters</td>
  </tr>
  <tr>
    <td>Advanced</td>
    <td>declares and defines functions with defaulted parameters</td>
  </tr>
  <tr>
    <td>Further studies</td>
    <td>refinement of defaulted parameters through multiple declarations</td>
  </tr>
</table>

## Motivation

Default parameters allow the omission of explicitly stating commonly defined parameters, using sensible defaults. Also allows expansion of function signature without forcing existing consumers to modify their calls.

## Topic introduction

Explains how default parameters work and how to define them.

## Foundational knowledge: Using *

### Background/Required Knowledge

A student is able to:

* Make calls existing functions using parameters
* Declare member and non-member functions, separate from definitions
* Define member and non-member functions
* Explain what a default constructor is and does

### Student outcomes

A student should be able to:

1. Call to a function with a default parameter with or without that parameter specified
2. Explain what the requirements are for a type to be usable with a default parameter

### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._

* When no forward-declaration exists, the definition serves as the declaration
* When multiple declarations exist, only one may specify the default for any particular parameter, but multiple declarations may specify the defaults for different parameters.
* Default values may be specified for new parameters in new declarations
* Calling an overloaded function with fewer parameters may be ambiguous with regard to an overload with defaulted parameters

### Points to cover

_This section lists important details for each point._

* Default value may only be specified once for each parameter
* Default values must start from the right

## Advanced: implementing *

### Background/required knowledge

* All of the above.

### Student outcomes

A student should be able to:

1. Declare a function with a default parameter, and omit the default in the definition's signature

### Caveats

### Points to cover

## Further studies

_These are important topics that are not expected to be covered but provide
guidance where one can continue to investigate this topic in more depth._
