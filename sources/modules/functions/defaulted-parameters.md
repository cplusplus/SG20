## Functions: default argument {#func-args}

_Skeleton descriptions are typeset in italic text,_
_so please don't remove these descriptions when editing the topic._

### Overview

_Provides a short natural language abstract of the module’s contents._
_Specifies the different levels of teaching._

Functions in C++ may be overloaded with different numbers and types of 
parameters. It may be of value to specify default arguments for some number 
of parameters, to allow a caller to avoid specifying arguments that 
rarely change, or to enable expanding the set of parameters while 
maintaining backward compatibility with existing callers.

------------------------------------------------------------------------
Level             Objective
----------------- ------------------------------------------------------
Foundational      Define and use functions with default arguments

Main              ---

Advanced          refinement of default arguments through multiple
                  declarations
------------------------------------------------------------------------

### Motivation

_Why is this important?_
_Why do we want to learn/teach this topic?_

Default arguments allow the omission of arguments with obvious or common
values. Also may be utilized to extend an existing function signature 
without forcing changes to existing calling code.

### Topic introduction

_Very brief introduction to the topic._

Explain how default arguments work and how to define them.

### Foundational: Using and defining functions with default arguments {#func-args-basic}

#### Background/Required Knowledge

A student is able to:

* Make calls to existing functions, passing arguments [[Functions: calling functions]][1]
* Declare member and non-member functions, separate from definitions
* Define member and non-member functions [[Functions: member functions]][2]
* Explain what a default constructor is and does [[C++ object model: constructors]][3]

#### Student outcomes

_A list of things "a student should be able to" after the curriculum._
_The next word should be an action word and testable in an exam._
_Max 5 items._

A student should be able to:

1. Call to a function with a default argument with or without that argument specified
2. Declare a function with a default argument, and omit the default in the definition's signature
3. Explain when the lifetime of a default argument begins and ends


#### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._

* When no forward-declaration exists, the definition serves as the declaration
* When multiple declarations exist, only one may specify the default for any particular parameter, but multiple declarations may specify the defaults for different parameters.
* Additional default values may be specified for other parameters in repeat declarations
* Calling an overloaded function with fewer arguments may be ambiguous with regard to an overload with default arguments

#### Points to cover

_This section lists important details for each point._

* Default value may only be specified once for each parameter among all declarations
* Default values must start from the rightmost parameter and continue leftward without gaps
* Considerations of when to use default arguments vs overload set

### Main: implementing * {#func-args-intermediate}

#### Background/required knowledge

* All of the above.

#### Student outcomes

_A list of things "a student should be able to" after the curriculum._
_The next word should be an action word and testable in an exam._
_Max 5 items._

A student should be able to:

#### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._

#### Points to cover

_This section lists important details for each point._

### Advanced {#func-args-advanced}

_These are important topics that are not expected to be covered but provide
guidance where one can continue to investigate this topic in more depth._

Subsequent redeclarations of the same function may add default argument
values, which are then usable by callers.
Though a single parameter cannot be given a default argument twice in the same 
translation unit, it is legal, though ill-advised, to give the same
function different default arguments in different translation units.


[1]: ../functions/calling-functions.md
[2]: ../functions/member-functions.md
[3]: ../object-model/constructors.md
