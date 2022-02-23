## Module name: topic name

_Skeleton descriptions are typeset in italic text,_
_so please don't remove these descriptions when editing the topic._

### Overview

_Provides a short natural language abstract of the module’s contents._
_Specifies the different levels of teaching._

------------------------------------------------------------------------
Level             Objective
----------------- ------------------------------------------------------
Foundational      Including code through standard library headers

Main              Organize function and class declarations into reusable
                  files for inclusion into others

Advanced          --- (inlining? templates? hygiene, such as using namespace?)

------------------------------------------------------------------------

### Motivation

_Why is this important?_
_Why do we want to learn/teach this topic?_

Understanding and using header files allows for common declarations to 
be used across multiple files without copying-and-pasting the text. Also,
understanding headers allows re-use of most existing 3rd-party libraries,
as well as the C++ standard library.

### Topic introduction

_Very brief introduction to the topic._

The contents of header files are injected into a source file to allow 
multiple distinct source files to share a single source of common 
declarations. 

### Foundational: Including code through standard library headers

#### Background/Required Knowledge

A student is able to:

* Invoke the compiler on a single source file to build an executable


#### Student outcomes

_A list of things "a student should be able to" after the curriculum._
_The next word should be an action word and testable in an exam._
_Max 5 items._

A student should be able to:

1. Include common standard library headers to get access to commonly used declarations

#### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._

#### Points to cover

_This section lists important details for each point._

* Usage of standard library code requires inclusion of various header files
* Give examples of various header files and when they may be needed for inclusion
* Include links to reference materials for finding out what headers are used for various feature sets

### Main: Organizing function and class declarations for reuse

#### Background/Required Knowledge

* All of the above.
* Define a function and write a separate, matching, declaration
* Distinguish between a declaration and a definition
* Compile multiple translation units and link them together into a single executable

#### Student outcomes

A student should be able to:

1. Create a declaration for an existing function, placed in a separate file
2. Include a header within the same directory
3. Include a header locatable within the compiler's include directories
4. Explain the meaning of the one-definition rule and how it applies to headers
5. Protect a header with include guards and explain why they are necessary

#### Caveats

* #pragma is useful, but not standardized and so may not be fully supported on all systems
* Reusing the same include guards may cause confusion. Naming conventions based on file paths can help
* Accidentally putting a definition in a header file may or may not introduce undefined behavior
* Circular dependencies can cause confusion. Care should be taken in identifying such
* 

#### Points to cover

### Advanced

_These are important topics that are not expected to be covered but provide
guidance where one can continue to investigate this topic in more depth._
