## Debugging errors: Run-time errors {#runtimeerr}

_Skeleton descriptions are typeset in italic text,_
_so please don't remove these descriptions when editing the topic._

### Overview

_Provides a short natural language abstract of the module’s contents._
_Specifies the different levels of teaching._

------------------------------------------------------------------------
Level             Objective
----------------- ------------------------------------------------------
Foundational      Identifying the run-time error cause

Main              Introspection methodologies to trackdown run-time errors

Advanced          ---

------------------------------------------------------------------------

### Motivation

_Why is this important?_
_Why do we want to learn/teach this topic?_

Code correctness is important, as erroneous programs can lead to real-world catastrophes, take for example, medical equipment failures that lead to people being exposed to too much radiation.
Techniques, such as, testing or fuzzing, help developers to identify erroneous states of the program.
However, when these techniques discover a run-time error, it’s up to the programmer to reason about and find the root cause of such run-time errors, so they need a well established process to debug run-time errors.

### Topic introduction

_Very brief introduction to the topic._

There exists a wide variety of methodologies, techniques, and tools to debug run-time errors.
In this topic, we give an overview of these and highlight how they can be applied to track down run-time errors in C++ programs.

### Foundational: Identifying the run-time error cause {#runtimeerr-found}

#### Background/Required Knowledge

A student:

* should be able to produce a basic running program.

#### Student outcomes

_A list of things "a student should be able to" after the curriculum._
_The next word should be an action word and testable in an exam._
_Max 5 items._

A student should be able to:

1. verify the output of the program and identify incorrect outcomes.
2. phrase hypothesis what could cause the run-time error.
3. observe and extract program state at specific points of the program, to verify hypotheses.
4. make their program as observable as possible.

#### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._

* run-time debugging can be domain specific
* not everything about the program state can be easily observed, students should be aware of that and learn basic techniques to make programs more observable
* students should be aware that the compilation mode (optimized vs debug) affects the debugging experience and also the program state itself


#### Points to cover

_This section lists important details for each point._

* the basics of using a debugger
* compiling with debug information
* observability techniques, such as, logging output or even `printf` statements

### Main: Introspection methodologies to trackdown run-time errors {#runtimeerr-main}

#### Background/Required Knowledge

* All of the above.

#### Student outcomes

A student should be able to:

1. use a debugger to inspect and manipulate program state
2. extract crash information using proper libraries
3. can create a minimal reproducible example

#### Caveats

* Different forms of multiprocessing programs can have varying impact on debuggability, such as:
    * parallel stl algorithms
    * multi threading
    * coroutines
    * vector parallelism


#### Points to cover

* How to use debuggers and the multitude of features they offer to manipulate and observe program state (e.g., break points, trap points, stack traces, manipulating program state).
* Use (non) standard library support for crash information extraction, e.g., logging libraries, libraries to capture crash reports, and sanitizer libraries (asan/ubsan/tsan).
* Creating minimal reproducible example and regressions tests from the extracted crash information.


### Advanced {#runtimeerr-advanced}

_These are important topics that are not expected to be covered but provide
guidance where one can continue to investigate this topic in more depth._

* ABI incompatibilities can have impact debugging experience where even observability tools, such as, debuggers, cannot correctly show the state of the program.
* Debugging in embedded environments.
