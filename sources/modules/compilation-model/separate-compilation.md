## C++ compilation model: Separate Compilation {#separate-comp}

_Skeleton descriptions are typeset in italic text,_
_so please don't remove these descriptions when editing the topic._

### Overview

_Provides a short natural language abstract of the module’s contents._
_Specifies the different levels of teaching._

This module outlines the issues involved in using separate compilation on multiple program files.

------------------------------------------------------------------------
Level             Objective
----------------- ------------------------------------------------------
Foundational:      Awareness of the existence of separate compilation

Main:              Awareness of supporting mechanisms and tools

Advanced:          Awareness of technicalities and tools

------------------------------------------------------------------------

### Motivation

_Why is this important?_
_Why do we want to learn/teach this topic?_

Any non-trivial program will span more than one source file. This makes separate compilation necessary. Separate compilation also leads to quick build times in projects under development.

### Topic introduction

_Very brief introduction to the topic._

### Foundational: Using

#### Background/Required Knowledge

A student: 

1. needs to have the text editor skills to split a single-file program into multiple files.
2. needs to be able to split function and classes into their declaration and definition. [[C++ object model: declarations]][1] [[C++ object model: Definitions]][2]


#### Student outcomes

_A list of things "a student should be able to" after the curriculum._
_The next word should be an action word and testable in an exam._
_Max 5 items._

A student should be able to:

1. Split a single file program into main, one or more auxiliaries, and header files (or modules), all in one directory
2. Compile and link a program that is spread over multiple files (again, all in one directory), either on the commandline or with a build system.
3. Describe the functions of the various files involved: source, object, executable.


#### Points to cover

1. Necessity of having function be declared at the locus of use
2. Solving this by explicit declaration or by using header files.

#### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._

1. Explain differences (including in desirability) between having explicit declarations of functions in the main program versus using header files or modules.
2. Compilation on a single commandline versus multiple. Resolution order when linking.
3. What needs to be recompiled if only a function is altered? Altered in use syntax versus altered only in semantics.

### Main: implementing

#### Background/Required Knowledge

* All of the above.

#### Student outcomes

A student should be able to:

1. Use compile flags, including `-I` and `-L` search path flags.
2. Make header files for their own code, including using header guards.
3. Use include directives for the headers of external libraries.
5. Be able to declare `extern` variables.

#### Caveats

1. Build systems make things both easier and harder.

#### Points to cover

1. Cover the mechanisms for include and library paths to your own code, as well as discovery mechanisms for external libraries.

### Advanced

_These are important topics that are not expected to be covered but provide
guidance where one can continue to investigate this topic in more depth._

1. Language inter-operability: the `extern "C"` mechanism.
2. Linker conventions including name mangling.
3. The `nm` tool for inspection object files and libraries, including de-mangling.
4. Understand the issues involved in deciding between include guards and `#pragma once`.
