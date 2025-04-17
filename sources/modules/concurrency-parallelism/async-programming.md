## Module name: Asynchronous programming

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

Advanced          --- Add external libraries as a dependencies  

------------------------------------------------------------------------

### Motivation

_Why is this important?_
_Why do we want to learn/teach this topic?_

* Asynchronous programming allows for non-blocking functions launches and enables that functions are executed asynchronously.
* Asynchronous programming is one form of parallelism and concurrency included in the C++ standard

### Topic introduction

_Very brief introduction to the topic._

Build systems are used to configure, build, and install complex C++ projects. 


### Foundational: Knowledge about build systems

#### Background/Required Knowledge

A student: 
* Should know [lambdas](../functions/lambdas.md)

#### Student outcomes

_A list of things "a student should be able to" after the curriculum._
_The next word should be an action word and testable in an exam._
_Max 5 items._

A student should be able to:

1. To explain what asynchronous programming is
2. To explain what a futures and promise are

#### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._

None

#### Points to cover

_This section lists important details for each point._

* Mention how to launch a function or lambda asynchronously using `std::async`  
* Mention how to use a `std::future` as a place holder for the result

### Main: Launch functions asynchronous and obtain the results

#### Background/Required Knowledge

* All of the above.

#### Student outcomes

A student should be able to:

1. Do define a function or lambda for the computational task
2. Launch the function or lambda asynchronous and obtain the results

#### Caveats

The concept of asynchronous programming is no easy digestible for most students.


#### Points to cover

* The header `<future>` needs to be includes
* The return type of the function or lambda will the the template type of the future
* The first argument of `std::async` is the function or lambda and after that all arguments are provided

Example using a function
```
void print_square(double a)
{
 std::cout << "Result=" << a * a << std::endl;
}

std::future<void> f = std::async(print,5.0);
// We could do other work here
f.get()
```

Example using lambdas
```
// Compute the sum
std::future<double> f1 = std::async([](double a, double b){ return a + b;});
// Compute the square
std::future<double> f2 = std::async([](double a){ return a * a;});

// Gather the results and add them up
double res = f1.get() + f2.get();
```

### Advanced

_These are important topics that are not expected to be covered but provide
guidance where one can continue to investigate this topic in more depth._

* How to build libraries 
* How to have external libraries be downloaded during the build process
* Mention that build systems provide support for unit testing

