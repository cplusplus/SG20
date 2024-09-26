## Module name: Build systems

_Skeleton descriptions are typeset in italic text,_
_so please don't remove these descriptions when editing the topic._

### Overview

_Provides a short natural language abstract of the module’s contents._
_Specifies the different levels of teaching._

------------------------------------------------------------------------
Level             Objective
----------------- ------------------------------------------------------
Foundational      --- Knowledge about build systems

Main              --- Usage of build system to compile a executable

Advanced          --- Usage of build system to compile a library or
                      add external libraries as a dependencies  

------------------------------------------------------------------------

### Motivation

_Why is this important?_
_Why do we want to learn/teach this topic?_

* Building complex C++ projects by hand is tricky
* Build systems can help to resolve dependencies
* Build systems can help do distribute C++ code and help other to compile the code
* Build systems can help to find and include libraries as dependencies
* Build systems faciliate project management 
* All major C++ projects are distributed with build systems 

### Topic introduction

_Very brief introduction to the topic._

Build systems are used to configure, build, and install complex C++ projects. 


### Foundational: Knowledge about build systems

#### Background/Required Knowledge

A student: 
* Should know how to compile and link C++ programs


#### Student outcomes

_A list of things "a student should be able to" after the curriculum._
_The next word should be an action word and testable in an exam._
_Max 5 items._

A student should be able to:

1. To explain what a build system is
2. To explain that a build systems resolves dependencies
3. To explain that a build system supports compilation for different operating systems and architectures

#### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._

None

#### Points to cover

_This section lists important details for each point._

* Mention that many build systems are available for C++ 
* Mention benefits and challenges
* Build system help to only compile the C++ files with code changes and not the complete project

### Main: Usage of build system to compile a executable

#### Background/Required Knowledge

* All of the above.

#### Student outcomes

A student should be able to:

1. Download a C++ package and build the package
2. Write a configuration file to compile a C++ executable
3. Pass compiler options via the build system
4. Use the build system to generate the executable

#### Caveats

The instructions are restricted to the chosen build system and
not easily transferable.


#### Points to cover

* Adding include paths to header files 
* Adding compiler flags
* How to build Release and Debug builds
* Linking external libraries to the C++ project
* Support different operating systems, compilers, and architectures 


### Advanced

_These are important topics that are not expected to be covered but provide
guidance where one can continue to investigate this topic in more depth._

* How to build libraries 
* Write a configuration file for your own library
* How to have external libraries be downloaded during the build process

