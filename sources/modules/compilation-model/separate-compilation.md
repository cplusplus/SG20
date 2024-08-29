## Module name: Separate Compilation

_Skeleton descriptions are typeset in italic text,_
_so please don't remove these descriptions when editing the topic._

### Overview

_Provides a short natural language abstract of the module’s contents._
_Specifies the different levels of teaching._

------------------------------------------------------------------------
Level             Objective
----------------- ------------------------------------------------------
Foundational      Awareness of the existence of separate compilation

Main              Awareness of supporting mechanisms and tools

Advanced          Awareness of technicalities and tools

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

1. needs to be able to split a single-file program into multiple files.
2. needs to understand the difference between declaration and definition.



#### Student outcomes

_A list of things "a student should be able to" after the curriculum._
_The next word should be an action word and testable in an exam._
_Max 5 items._

A student should be able to:

1. Split a single file program into main, one or more auxiliaries, and header files (or modules), all in one directory
2. Compile and link a program that is spread over multiple files (again, all in one directory), either on the commandline or with a build system.
3.
4.
5.

#### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._

1. Explain differences (including in desirability) between having explicit declarations of functions in the main program versus using header files or modules.
2. Compilation on a single commandline versus multiple
3. What needs to be recompiled if only a function is altered? Altered in use syntax versus altered only in semantics.

#### Points to cover

_This section lists important details for each point._

### Main: implementing

#### Background/Required Knowledge

* All of the above.

#### Student outcomes

A student should be able to:

1. Use compile flags, including `-I` and `-L` search path flags, and the relation with corresponding include directives in the source.
2. Understand search paths to use header files of external libraries.
3. Be able to declare `extern` variables.
4.
5.

#### Caveats

1. CMake makes things both easier and harder. If CMake is used, cover the various `target_include/link` statements and discovery mechanisms for external libraries.

#### Points to cover

### Advanced

_These are important topics that are not expected to be covered but provide
guidance where one can continue to investigate this topic in more depth._

1. Language inter-operability: the `extern "C"` mechanism.
2. Linker conventions including name mangling.
3. The `nm` tool for inspection object files and libraries.
