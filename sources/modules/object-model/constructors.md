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

Constructors are fundamental to generate objects from classes and structs, so understanding them is essential to work with objcets.

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

1. Explain the differences between the big five, namely, copy constructor, move constrcutor, copy/assign, move/assign, destructor, and constructor.
2. Construct a initializer list and explain conditions when it is necessary
3. Delegate to the constructor of the base class
4. Demonstrate and explain safe memory handling using shared or unique pointers
5. Define what RAII is and the role of the constructor 

#### Caveats

* Order of construction should match the initalizer list order

#### Points to cover

* Not calling virtual functions from the base class
* Do not initialze data outside of the constructor (two face initialization)
* Difference between assignment and deep copy

### Advanced: 

_These are important topics that are not expected to be covered but provide
guidance where one can continue to investigate this topic in more depth._

* Error handling within constructors
* Non-static data initialziers 
* Constructors with member references
* Purposes for protected constructors
* What does delete vs private means
* What does it mean to have an explicit constructor 
* Impact on const expr on constructor %extend later
* Rules on memory ordering %extend later
* Define constructor outside of the body of the class %extend later
