## C++ compilation model: Separate Compilation {#separate-comp}

_Skeleton descriptions are typeset in italic text,_
_so please don't remove these descriptions when editing the topic._

### Overview

_Provides a short natural language abstract of the module’s contents._
_Specifies the different levels of teaching._

------------------------------------------------------------------------
Level             Objective
----------------- ------------------------------------------------------
Foundational:      Basic use of separate compilation

Main:              Command of supporting mechanisms and tools

Advanced:          Technicalities and tools

------------------------------------------------------------------------

### Motivation

_Why is this important?_
_Why do we want to learn/teach this topic?_

This module outlines the issues involved in using separate compilation on multiple program files.

Any non-trivial program will span more than one source file. This makes separate compilation necessary. Separate compilation also leads to quick build times in projects under development.

### Topic introduction

_Very brief introduction to the topic._

### Foundational: Basic use of separate compilation

#### Background/Required Knowledge

A student: 

1. needs to be able to split function and classes into their declaration and definition. [[C++ object model: declarations]][1] [[C++ object model: Definitions]][2]


#### Student outcomes

_A list of things "a student should be able to" after the curriculum._
_The next word should be an action word and testable in an exam._
_Max 5 items._

A student should be able to:

1. split a single file program into main, one or more auxiliaries, and header files (or modules), all in one directory
2. compile and link a program that is spread over multiple files (again, all in one directory), either on the commandline or with a build system.
3. describe the functions of the various files involved: source, object, executable.


#### Points to cover

* Necessity of having function be declared at the locus of use
  * Solving this by explicit declaration or by using header files.

#### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._

* Explain differences (including in desirability) between having explicit declarations of functions in the main program versus using header files or modules.
* Compilation on a single commandline versus using multiple commands.
* What needs to be recompiled if only a function is altered? Altered in use syntax versus altered only in semantics.

### Main: Command of supporting mechanisms and tools

#### Background/Required Knowledge

* All of the above.

#### Student outcomes

A student should be able to:

1. Explain what a translation unit is, and its relation to header files.
2. Use compile flags, including `-I` and `-L` to specify search paths.
3. Make header files for their own code, including using header guards.
4. Use include directives for the headers of external libraries.

#### Caveats

* Build systems make things both easier and harder.
  * Student does not have to set include/library paths.
  * Build systems prevent unnecessary recompilation.
  * Build systems have a separate learning curve.
  * Build systems will pay off when using libraries, less with self-contained student code.

#### Points to cover

* Cover the mechanisms for include and library paths to your own code, as well as discovery mechanisms for external libraries.

### Advanced: Technicalities and tools

_These are important topics that are not expected to be covered but provide
guidance where one can continue to investigate this topic in more depth._

* Language inter-operability: the `extern "C"` mechanism.
*  Linker conventions including name mangling.
* The `nm` tool for inspection object files and libraries, including de-mangling.
* Understand the issues involved in deciding between include guards and `#pragma once`.

[1]: ../object-model/declarations.md
[2]: ../object-model/definitions.md
