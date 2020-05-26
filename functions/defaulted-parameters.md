# Module name: defaulted parameters
_Skeleton instructions are typeset in italic text._

## Overview

Functions in C++ may be overloaded with different numbers and types of 
parameters. It may be of value to specify default values for some number 
of parameters, to allow a caller to avoid specifying parameters that 
rarely change, or to enable expanding the set of parameters while 
maintaining backward compatibility with existing callers.

<table>
  <thead>
    <th>Level</th>
    <th>Objectives</th>
  </thead>
  <tr>
    <td>Foundational knowledge</td>
    <td>Define and use functions with defaulted parameters</td>
  </tr>
  <tr>
    <td>Advanced</td>
    <td></td>
  </tr>
  <tr>
    <td>Further studies</td>
    <td>refinement of defaulted parameters through multiple declarations</td>
  </tr>
</table>

## Motivation

Default parameters allow the omission of parameters with obvious or common
values. Also may be utilized to extend an existing function signature 
without forcing changes to existing calling code.

## Topic introduction

Explain how default parameters work and how to define them.

## Foundational knowledge: Using and defining functions with default arguments

### Background/Required Knowledge

A student is able to:

* Make calls to existing functions, passing parameters [[Functions: calling functions]][1]
* Declare member and non-member functions, separate from definitions
* Define member and non-member functions [[Functions: member functions]][2]
* Explain what a default constructor is and does [[C++ object model: constructors]][3]

### Student outcomes

A student should be able to:

1. Call to a function with a default parameter with or without that parameter specified
2. Declare a function with a default parameter, and omit the default in the definition's signature
3. Explain what the requirements are for a type to be usable with a default parameter
4. Explain when the lifetime of a defaulted parameter begins and ends


### Caveats

* When no forward-declaration exists, the definition serves as the declaration
* When multiple declarations exist, only one may specify the default for any particular parameter, but multiple declarations may specify the defaults for different parameters.
* Additional default values may be specified for other parameters in repeat declarations
* Calling an overloaded function with fewer parameters may be ambiguous with regard to an overload with defaulted parameters

### Points to cover

* Default value may only be specified once for each parameter among all declarations
* Default values must start from the rightmost parameter and continue leftward without gaps
* Considerations of when to use default arguments vs overload set

## Advanced: implementing *

### Background/required knowledge

* All of the above.

### Student outcomes

A student should be able to:

### Caveats


### Points to cover

## Further studies

Subsequent redeclarations of the same function may add default argument
values, which are then usable by callers.
Though a single argument cannot be given a default twice in the same 
translation unit, it is legal, though ill-advised, to give the same
function different default parameters in different translation units.


[1]: ../functions/calling-functions.md
[2]: ../functions/member-functions.md
[3]: ../object-model/constructors.md

