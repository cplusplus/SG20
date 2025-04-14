## Program Design: Algorithms {#algo}

_Skeleton descriptions are typeset in italic text,_
_so please don't remove these descriptions when editing the topic._

### Overview

_Provides a short natural language abstract of the module’s contents._
_Specifies the different levels of teaching._

------------------------------------------------------------------------
Level             Objective
----------------- ------------------------------------------------------
Foundational      Using algorithms

Main              Writing generic algorithms

Advanced          ---

------------------------------------------------------------------------

### Motivation

_Why is this important?_
_Why do we want to learn/teach this topic?_

Algorithms make it possible to write code saying what you want done and not how you want it to be done. To make that happen, algorithms need to be small and composable building blocks. The C++ standard already offers a wide set of algorithms to choose from. These algorithms form an important part of the standard and get shipped alongside the compiler, so they are well tested and optimized. Hence, prefer to use the standard algorithms when applicable or if you build your own, follow the design principles behind the STL algorithms, so one's own code intertwines well with the standard algorithms.


### Topic introduction

_Very brief introduction to the topic._

### Foundational: Using algorithms {#algo-found}

#### Background/Required Knowledge

A student:

* [[Program Design: Containers - Foundational]][1]
* [[Program Design: Iterators - Foundational]][2]

#### Student outcomes

_A list of things "a student should be able to" after the curriculum._
_The next word should be an action word and testable in an exam._
_Max 5 items._

A student should be able to:

1. find and use an appropriate algorithm from the standard library.
2. combine multiple algorithms together to solve a problem.
3. refactor traditional style for/while loops into algorithms.
4. make an informed choice when using different algorithm flavors (mod/non-mod, iterator/range based, member/free-standing).


#### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._


#### Points to cover

_This section lists important details for each point._

* Show how containers and algorithms are conceptually decoupled
    * Discuss the tradeoffs between member algorithms and non-member (free functions) algorithms
* Flavors of algorithms:
    * modifying/non modifying (e.g., transform vs accumulate)
    * requirements on the type iterator (forward/random-access)
    * iterator-based algorithms vs range-based algorithms
* Composability of algorithms:
    * composing algorithms by making use of the returning iterator (i.e., find-erase idiom).
    * sequential composability of algorithms (e.g., partition-based quicksort implementation)
* Customizability of algorithms
    * exchanging default operations in algorithms with user-defined semantics (e.g., find_if or accumulate with another binary operation) [dep: lambdas]
* expressiveness of code using algorithm (functional programming patterns)
    * std::accumulate
    * write what you want done instead of how


### Main: Writing generic algorithms {#algo-main}

#### Background/Required Knowledge

* [[Program Design: Concepts - Foundational/Main]][3]
* Callables
* [Optional] Foundational/Main: type-traits (templates)


#### Student outcomes

A student should be able to:

1. write a generic algorithm, such as `std::copy` or `std::transform`.
2. determine the time/space complexity of their algorithm.
3. write an algorithm that is available to the largest set of applicable types.
4. specify the interface and compile-time requirements of an algorithm using concepts.
5. implement customization choices for an algorithm (e.g., specialize an algorithm’s implementation with regard to the given iterator type, policy class, type trait, …).


#### Caveats

* Reinventing the wheel: try not implement algorithms that already exist

#### Points to cover

* Try to use the smallest set of specified operations (e.g., iterators) to make algorithms apply to many cases.
* Patterns to implement customization choices
    * policy classes
    * type traits (link [optional] type traits)
    * defining requirements/specializations and their connection to the design/implementation of the algorithm (e.g., `std::advance()` is different for forward/random-access iterators)
* When defining generic parameters, prefer concepts to specify the required interface of the generic type if possible (see: link to concepts).
* Algorithms should be composable building blocks: focus on a specific task and do it well compared to building one large algorithm that solves multiple problems (e.g., `std::sort` and `std::unique` and not `std::sort_unique`).

### Advanced

_These are important topics that are not expected to be covered but provide
guidance where one can continue to investigate this topic in more depth._

* Parallel algorithms through execution policies

[1]: ../program-design/containers.md
[2]: ../program-design/iterators.md
[3]: ../program-design/concepts.md
