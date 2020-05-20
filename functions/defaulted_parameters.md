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
    <td>can make calls to functions with or without defaulted parameters</td>
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

Default parameters allow the omission of parameters with obvious or common values. Also may be utilized to extend an existing function signature without forcing changes to existing calling code.

## Topic introduction

Explain how default parameters work and how to define them.

## Foundational knowledge: Using *

### Background/Required Knowledge

A student is able to:

* Make calls to existing functions, passing parameters
* Declare member and non-member functions, separate from definitions
* Define member and non-member functions
* Explain what a default constructor is and does

### Student outcomes

A student should be able to:

1. Call to a function with a default parameter with or without that parameter specified
2. Explain what the requirements are for a type to be usable with a default parameter
3. Explain when the lifetime of a defaulted parameter begins and ends


### Caveats

* When no forward-declaration exists, the definition serves as the declaration
* When multiple declarations exist, only one may specify the default for any particular parameter, but multiple declarations may specify the defaults for different parameters.
* Additional default values may be specified for other parameters in repeat declarations
* Calling an overloaded function with fewer parameters may be ambiguous with regard to an overload with defaulted parameters

### Points to cover

* Default value may only be specified once for each parameter among all declarations

## Advanced: implementing *

### Background/required knowledge

* All of the above.

### Student outcomes

A student should be able to:

1. Declare a function with a default parameter, and omit the default in the definition's signature

### Caveats

* Default values must start from the right-most parameter and continue left-ward without gaps

### Points to cover

## Further studies

Learning the extent to which you may further specify new default values and rules related to what is necessary for a consumer to take advantage of additionally defaulted values.

