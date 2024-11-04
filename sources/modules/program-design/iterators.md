## Program Design: iterators {#it}

_Skeleton descriptions are typeset in italic text,_
_so please don't remove these descriptions when editing the topic._

### Overview

_Provides a short natural language abstract of the module’s contents._
_Specifies the different levels of teaching._

------------------------------------------------------------------------
Level             Objective
----------------- ------------------------------------------------------
Foundational      Using iterators

Main              Writing iterators

Advanced          ---

------------------------------------------------------------------------

### Motivation

_Why is this important?_
_Why do we want to learn/teach this topic?_

Iterators provide a generic interface between algorithms and containers.
The container defines the iteration over its data.
Therefore, the algorithm does neither need to know about the iteration nor the concrete data types that are stored in the container.
This way, algorithms can be implemented in a generic way without detailed knowledge of the containers they operate on, and the containers can be written without predetermining what algorithms should be available for it.

### Topic introduction

_Very brief introduction to the topic._

### Foundational: Using iterators {#it-found}

#### Background/Required Knowledge

A student:
* containers [[Program Design: Containers - Foundational]][1]
* for loops
* [Maybe] [[Object Model: Value Semantics - Foundational]][2][[Object Model: Reference Semantics - Foundational]][3] TODO: revisited after ref/value semantics 

#### Student outcomes

_A list of things "a student should be able to" after the curriculum._
_The next word should be an action word and testable in an exam._
_Max 5 items._

A student should be able to:

1. write a for loop using iterators (not just range-based for).
2. use the canonical iterator operations (begin/end, dereference, etc.).
3. use the appropriate operations with regard to the iterators category.
4. show examples where iterators are invalidated by operations on a container.
5. demonstrate how iterators provide an abstraction between the operation and the underlying data structure.

#### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._

* Dangling iterators (i.e., having an iterator to a no longer valid container)
* `end()` marks the position after the last element and, by that, is not dereferencable
* When comparing iterators, both iterators need to belong to the same underlying data structure
* Keep in mind that iterators do not guarantee that the underlying memory is contiguous.

#### Points to cover

_This section lists important details for each point._

* Using standard iterators with iterator-based for loops
    * Difference between value/reference semantics based for loops
    * Explain connection to for-each
* Basic iterator nomenclature and functionality
    * begin/end
    * Give an example of the typical for loop pattern `iter != end()`
    * Dereferencing iterators
    * Advancing iterators
    * Iterator adapters for containers (e.g., `back_inserter`)
* Explain in a simple way the differences between different iterator notions
    * For example, forward/backward/random access
    * Defer a more detailed explanation of iterator categories to main
* Give a brief introduction to iterator invalidation
    * Defer a more detailed explanation to main
* Explain the design idea behind iterators
    * Iterators provide abstraction
    * Iterators decouple accessing elements and iterating over a container from the actual container type
    * Iterators store the iteration state (i.e., where you are in the container)


### Main: Writing iterators {#it-main}

#### Background/Required Knowledge

#### Student outcomes

A student should be able to:

1. create an iterator based on an existing iterator and change its behavior.
2. create an standard compliant iterator for a self written container.
3. determine when an iterator is invalidated and write code accordingly.

#### Caveats

* Beware when using iterators in a multi-threaded environment as both the iterator and the data structure need to be correctly synchronized (see XYZ). TODO: find reference
* Make sure that the implementation of the iterator offers at least the interface and guarantees that its category offers.


#### Points to cover

* When and how to defined internal/external iterators
    * Iterator adapters (external)
        * adds additional logic (e.g., reverse iterators)
        * non-linear iterators (e.g., skip some number elements)
    * API-extending iterators (external/internal)
        * e.g., adding a new pre-order traversal iterator to a tree
* Iterator invalidation
    * Modifying the underlying data structure can invalidate an iterator
        * Different types of containers have different iterator invalidation characteristics, even on similar methods (e.g., `vector.push_back` vs `list.insert`).
        * Invalidation can be unpredictable (e.g., a `push_back` to a vector may but does not have to invalidate an iterator)
        * Containers that don’t have stable addressing have the problem of iterator invalidation.
    * The iterator should not outlive the container (lifetime)
* Templates and iterators
    * Iterator type interface (`value_type`, `pointer`, `reference`, `iterator_category`)
    * To support different types of iterators algorithms often use template parameters for the concrete iterator type and only rely on the interface of an iterator (see topic [[Program Design: Algorithms - Main]][4])


### Advanced

_These are important topics that are not expected to be covered but provide
guidance where one can continue to investigate this topic in more depth._

[1]: ../program-design/containers.md
[2]: ../object-model/value-semantics.md
[3]: ../object-model/reference-semantics.md
[4]: ../program-design/algorithms.md
