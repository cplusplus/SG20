## C++ object model: constructor

_Skeleton descriptions are typeset in italic text,_
_so please don't remove these descriptions when editing the topic._

### Overview

_Provides a short natural language abstract of the module’s contents._
_Specifies the different levels of teaching._

------------------------------------------------------------------------
Level             Objective
----------------- ------------------------------------------------------
Foundational:      Basic usage of constructors

Main:              Initialization and overloading   

Advanced:          TBD 

------------------------------------------------------------------------

### Motivation

_Why is this important?_
_Why do we want to learn/teach this topic?_

Constructors are fundamental to generate objects from classes and structs, so understanding them is essential to work with objects.

### Topic introduction

_Very brief introduction to the topic._

### Foundational: Basic use of constructors

#### Background/Required Knowledge

A student:

1. should know the notion of classes and structs %todo link to classes 

#### Student outcomes

_A list of things "a student should be able to" after the curriculum._
_The next word should be an action word and testable in an exam._
_Max 5 items._

A student should be able to:

1. Add constructors to classes and structs
2. Explain different types of initialization
3. Explain compiler provided constructors when these are provided, what these do, and when these go away
4. Explain differences between creating an object and declare a variable

#### Points to cover

* Overloading of constructors and default arguments
* Copy constructor and destructor
* Constructors can be used to initialize class members 

#### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._

* None

### Main: 

#### Background/Required Knowledge

* All of the above.
* Class inheritance %todo check for link
* Dynamic memory
* Difference between shared and unique pointers

#### Student outcomes

A student should be able to:

1. Explain the differences between the big five, namely, copy constructor, move constructor, copy/assign, move/assign, destructor, and constructor.
2. Construct a initializer list and explain conditions when it is necessary
3. Delegate to the constructor of the base class
4. Demonstrate and explain safe memory handling using shared or unique pointers
5. Define what RAII is, the role of the constructor in it; and the relationship with its destructor 

#### Caveats

* Order of construction should match the initalizer list order

#### Points to cover

* Not calling virtual functions from the base class
* Do not initialize data outside of the constructor (two face initialization)
* All objects should be initialized within the constructor and should have a well-defined state
* Difference between assignment and deep copy

For more details, we refer to the [C++ core guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines)

### Advanced: 

_These are important topics that are not expected to be covered but provide
guidance where one can continue to investigate this topic in more depth._

* Member references must be initialized in the constructor   
* Member classes not initialized explicitly will be initialized using the default constructor
* Exceptions thrown in constructor (needs to be extended)
* Protected constructor prevents direct construction of a base class
* Explicit constructor prevents implicit type conversion of a single argument 
* Member classes are constructed in the order they are declared
* Constructors for classes with static members must be defined outside of the body of the class
* Non-state data member can be given a default value at initialization, but constructor take 

