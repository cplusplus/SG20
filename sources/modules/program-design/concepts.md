## Program Design: Concepts {#concepts}

_Skeleton descriptions are typeset in italic text,_
_so please don't remove these descriptions when editing the topic._

### Overview

_Provides a short natural language abstract of the module’s contents._
_Specifies the different levels of teaching._

------------------------------------------------------------------------
Level             Objective
----------------- ------------------------------------------------------
Foundational      Using constraints

Main              Designing concepts

Advanced          Testing concepts

------------------------------------------------------------------------

### Motivation

_Why is this important?_
_Why do we want to learn/teach this topic?_

When writing generic code it is important to specify what set of types are supported, to prevent users from misusing it. That is, we want to prevent generic code from compiling for types that are not supported. Furthermore, we also then want to return useful error messages that describe why a type was not usable.

Concepts allow us to provide different specialized implementations for a function or class. These implementations can then make use of specific characteristics of the chosen subset of the allowed types without relying on hacky tricks. Overall, concepts allow us to write better documenting and more expressive code, making it easier to write, read, and maintain generic code. 


### Topic introduction

_Very brief introduction to the topic._

### Foundational: Using constraints {#concepts-found}

#### Background/Required Knowledge

A student:

* [[Functions: Function Templates - Foundational]][1]
* [[User-defined Types: Class Templates - Foundational]][2]

#### Student outcomes

_A list of things "a student should be able to" after the curriculum._
_The next word should be an action word and testable in an exam._
_Max 5 items._

A student should be able to:

1. write code that calls a concept function
2. write a simple template that is constrained
3. write code that composes multiple constraints
4. enumerate some standard defined concepts


#### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._

* There used to be workarounds that were used to constrain interfaces (e.g., partial specialization, SFINAE) but they were cumbersome and hard to debug. In modern C++ `concepts` should be used instead.

#### Points to cover

_This section lists important details for each point._

* Simple example where we need constraints (e.g., min/max, sqrt, printing, …)
* Why constraints at all: 
    * Can express conceptual design directly
    * get better compile time checking with good error messages
        * can add constraints that are not in the type system
    * unconstrained templates are too generic, constraints allow us to restrict what types are applicable for a template
    * make important properties of an algorithm part of the type interface (e.g., that a collection needs to be sortable)
* Constraints can be composed with && and ||
* The standard has some named constraints, i.e., `concepts`


### Main: Designing concepts {#concepts-main}

#### Background/Required Knowledge

* [Optional] Overload resolution [[Functions: Overloading]][3]
* [Optional] Template specializations [[Compile-time programming: Template Meta Programming]][4]

#### Student outcomes

A student should be able to:

* make an educated decision on whether to create a new concept or use preexisting one (e.g., from the standard)
* design a new concept following best practices
* use concepts to build overload sets/specialize templates [Optional]


#### Caveats

* further constraining previously published concepts can break user code
* `requires requires`: consider that a single requires only checks if an expression is syntactically correct and that `requires requires` allows one to check if the logical value on an expression is true.

#### Points to cover

* Design rules for concepts
    * first, check if the desired set of constraints already exists in a standard provided concept
    * prefer refining concepts over expressing all constraints directly
    * try to not further constrain previously published concepts, as this can break user code
    * consider that under-specified constraints can be too generic but also that over-constraining a template limits its applicability (i.e., select only the constraints that are important for a template to work in a generic context)
* [Optional] if a more specialized implementation is possible for a constrained group of types (i.e., given the constraint from a concept we have strong guarantees for the implementation), use "overloading"/template specialization on concepts to select the specialized implementations (e.g., std::advance())
    * most constrained template is chosen
    * prefer concepts over “SFINAE” when constraining overload sets


### Advanced

_These are important topics that are not expected to be covered but provide
guidance where one can continue to investigate this topic in more depth._

* Writing tests for concepts to ensure they specify exactly what was intended.

[1]: ../functions/function-templates.md
[2]: ../user-defined-types/class-templates.md
[3]: ../functions/overloading.md
[4]: ../compile-time-programming/template-meta-programming.md
