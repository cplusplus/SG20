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

* Function objects in relation to the standard library, e.g. for passing functions to the standard algorithms or auxiliary functions
* Allows the developer to define and pass functionality as values/data/information
* Allows developer to operate in a functional-programming mindset
* Improves code readability by localizing the code
* Making code more compact by writing functions in-place 
* Library designs taking callables allows the library to be customizable for the consumer, while lambdas make this usage approachable

### Topic introduction

_Very brief introduction to the topic._

Lambdas were added in C++11 and have grown in power and functionality ever since.

### Foundational: Define and execute lambdas with basic capture syntax

#### Background/Required Knowledge

A student:
_TODO: Add cross-reference to these
Explain function argument  passing by value or by reference

#### Student outcomes

_A list of things "a student should be able to" after the curriculum._
_The next word should be an action word and testable in an exam._
_Max 5 items._

A student should be able to:

1. Use a lambda taking a concrete type as a parameter and return a value
2. Transform a function definition into a lambda and use it
3. Enumerate trade-offs of code-locality using lambdas vs code reuse with free-functions
4. Assign a lambda to a variable for multiple calls
5. Named lambdas to increase code readability
6. Explain capture-by-value and capture-by-reference



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

1. Utilize `std::function` as a means to hold and transfer lambdas
2. Define a function-template taking a lambda as a template parameter
3. Specify, per parameter, whether to capture by reference or value
4. Specify the default capture type for a lambda
5. Specify the return type for a lamda function, if not detected by the compiler
5. Use a lambda in a class, capturing and utilizing class data via `this`

#### Caveats

#### Points to cover

motivation: 
1. how to write library code to call user code? --- callbacks
2. root finding using lambdas
3. "customizing" generic algorithms

### Advanced
Explain why they can't write out the type of a lambda?
_These are important topics that are not expected to be covered but provide
guidance where one can continue to investigate this topic in more depth._


#### Background/Required Knowledge

* All of the above.

#### Student outcomes

A student should be able to:

1. Use a lambda to introduce a new identifier for use within the body of the lambda
2. Explain the relationships between generic lambdas and templates
3. Construct an object with choice between 2 constructors, using immediately-dispatched lambda (see first listing)
4. Utilize an immediately dispatched lambda to encode multiple statements where the language requires an expression
5. Use the `mutable` keyword to allow changing a captured-by-value or lambda-local value within the lambda body
6. Explicitly specify the return type for a lambda
7. Explain under what conditions an explicit return type is necessary

#### Caveats

#### Points to cover

Construct an object with choice between 2 constructors:
```
class X;
bool b;
X x = [c = b](){ if (c) return X(5, 10) else X("a", "b"); }();
```

Todo add caption
```
assert([](){
	std::vector v{1, 2, 3, 4, 5};
	for (auto x: v) std::cout << v << std::endl;
}());
```


Capture can introduce new names by initializing them as `capture-default`
```
char const* const s = "5";
[x=atoi(s)](){}
```

`Capture-default` variables can be altered by the lambda body if the lamda is marked as `mutable`
```
std::ranges::for_each(
	std::vector{1,2,3,4,5},
	// introducing new identifier
	// generic lambda
	// mutable allows changing "init"
	[init = true] (auto&& x) mutable {
		if (init) 
		{ std::cout << x; init = false}; 
		else 
		{ std::cout << ',' << x;}
	});
```

When to use lambdas or not:
forcing code into a lambda can prevent some features
```
std::for_each(std::par_sec, v, [](){/* can't utilize OpenMP here */}};
for(auto i : v){ /* OpenMP can be utilized here */ }
```

