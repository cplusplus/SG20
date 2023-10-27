## Module name: Lambdas

_Skeleton descriptions are typeset in italic text,_
_so please don't remove these descriptions when editing the topic._

### Overview

_Provides a short natural language abstract of the module’s contents._
_Specifies the different levels of teaching._

------------------------------------------------------------------------
Level             Objective
----------------- ------------------------------------------------------
Foundational      Define and execute lambdas with basic capture syntax

Main              Passing instances of lambdas for use in external code

Advanced          Generic lambdas, utilizing mutable state, mapping 
                  to function objects, decay to function pointers

------------------------------------------------------------------------

### Motivation

_Why is this important?_
_Why do we want to learn/teach this topic?_

* function objects in relation to the standard library...
* Allows the developer to define and pass functionality as values/data/information
* Allows developer to operate in a functional-programming mindset
* Improves code readdability by localizing the code
* Effective means to help refactoring code from long functions to re-usable functions
* Library designs taking callables allows the library to be customizable for the consumer, while lambdas make this usage approachable

### Topic introduction

_Very brief introduction to the topic._

Lambdas were added in C++11 and have grown in power and functionality ever since.

### Foundational: Define and execute lambdas with basic capture syntax

#### Background/Required Knowledge

A student:
_TODO: Add cross-reference to these
Explain capture-by-value and capture-by-reference

#### Student outcomes

_A list of things "a student should be able to" after the curriculum._
_The next word should be an action word and testable in an exam._
_Max 5 items._

A student should be able to:

1. Use a lambda taking a concrete type as a parameter and return a value in response
2. 
3. 
4. 
5. 

#### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._

#### Points to cover

_This section lists important details for each point._

### Main: Passing instances of lambdas for use in external code

#### Background/Required Knowledge

* All of the above.

#### Student outcomes

A student should be able to:

1. Utilize std::function as a means to hold and transfer lambdas
2. Define a function-template taking a lambda as a template parameter
3. Use captures to change

#### Caveats

#### Points to cover

Capture can introduce new names
```
char const* const s = "5";
[x=atoi(s)](){}
```

```
std::ranges::for_each(
	std::vector{1,2,3,4,5},
	[init = true] (auto&& x) mutable {
		if (init) 
		{ std::cout << x; init = false}; 
		else 
		{ std::cout << ',' << x;}
	});
```

### Advanced
Explain why they can't write out the type of a lambda?
_These are important topics that are not expected to be covered but provide
guidance where one can continue to investigate this topic in more depth._
