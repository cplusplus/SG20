## Debugging errors: Build errors {#builderr}

_Skeleton descriptions are typeset in italic text,_
_so please don't remove these descriptions when editing the topic._

### Overview

_Provides a short natural language abstract of the module’s contents._
_Specifies the different levels of teaching._

------------------------------------------------------------------------
Level             Objective
----------------- ------------------------------------------------------
Foundational      Common build errors

Main              Complex build errors

Advanced          ---

------------------------------------------------------------------------

### Motivation

_Why is this important?_
_Why do we want to learn/teach this topic?_

Code that is written should follow the rules set in the standard to be correct.
Compilers and linkers will complain when you don’t follow the rules, sometimes in hard to understand language to precisely match the standard's definitions.
Hence, we should enable students to understand these error messages and extract the necessary information to help them fix their problem.

### Topic introduction

_Very brief introduction to the topic._

In the C++ ecosystem there are a multitude of build systems (TODO: link) and tools to produce programs.
Building these programs from source code involves multiple steps and in each of these steps problems can occur.

### Foundational: Common build errors {#builderr-found}

#### Background/Required Knowledge

A student:

* should be familiar with the build system (link)
* definitions (link def:found)

#### Student outcomes

_A list of things "a student should be able to" after the curriculum._
_The next word should be an action word and testable in an exam._
_Max 5 items._

A student should be able to:

1. extract the necessary information from an error message (compiler/linker) to fix the problem
2. differentiate build errors from other types of errors (e.g., run-time errors)

#### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._

* Introduce the concept of ODR violations [TODO: insert link to ODR in definitions]
* There exist different approaches to describe how software projects should be compiled (e.g., cmake). Students should be introduced to at least one and given an introduction to work and debugging this approach.


#### Points to cover

_This section lists important details for each point._

* Different types of build errors
  * Compiler errors
    * Reason: Illformed constructs that are not valid in the language.
    * code/error example (TODO)
  * Compiler warnings (-Werror)
    * Reason: Constructs that are officially “legal” in the language but can be dangerous, e.g., they could potentially lead to UB.
    * code/error example  (TODO)
  * Linker errors
    * Reason: Symbols from other translation units that are required can not be found or are defined multiple times.
    * code/error example  (TODO)
* Tools
  * Give overview
  * Differences between them
    * code/error example where clang and gcc disagree (TODO)
* Interpreting error messages: Explain how error messages can be read and interpreted.


### Main: Complex build errors {#builderr-main}

#### Background/Required Knowledge

* name mangling (link)

#### Student outcomes

A student should be able to:

1. debug more complex system build problems
2. pinpoint the exact issue in a large and complex error message
3. identify run-time problems that rise from build-time errors where the compiler/linker does not warn about “no diagnostic required” (e.g., ODR violations)

#### Caveats

* Linking problems due to weak vs strong symbols (TODO: link linkage)

#### Points to cover

* Discuss the role that name mangling in error messages and problems
* Mention that more specialized forms of debugging exist [[Debugging Errors: Compile-Time Debugging]][1]
* Linking order problems, e.g., static initialization order (i.e., global initialization order depends on linking order)
* Discuss how one could debug/detect ODR violations


### Advanced

_These are important topics that are not expected to be covered but provide
guidance where one can continue to investigate this topic in more depth._

* Problems with debugging the linking to different languages (e.g, C, Rust) [TODO: link extern “C”]
* Problems due to incompatible ABIs

[1]: ../debugging_errors/compile-time-debugging.md
