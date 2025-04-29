## Module name: Parallel algorithms

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

* Allows to execute *most* of the algorithms in the C++ standard in parallel
* Parallel algorithms are one form of parallelism included in the C++ standard

### Topic introduction

_Very brief introduction to the topic._

Algorithms that range over a large data set, can be accelerated by parallel execution. 
Exectution policies allow to executed the algorithms in the C++ standard on multiple cores or a single core. 

### Foundational: Knowledge about build systems

#### Background/Required Knowledge

A student: 
* Should know [lambdas](../functions/lambdas.md)
* Should know [algorithms](../program-design/algorithms.md)
* Should know [iterators](../program-design/iterators.md)
* Should know [containers](../program-design/containers.md)

#### Student outcomes

_A list of things "a student should be able to" after the curriculum._
_The next word should be an action word and testable in an exam._
_Max 5 items._

A student should be able to:

1. To explain parallel and sequential execution
2. Specify the appropriate execution policy for sequntial or parallel execution 

#### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._

1. The programmer has to make sure that the algorithm is theoretical parallel. For example, specifying parallel execution using state-full lambdas might give wrong results.
2. The programmer has to make sure that the parallel execution does not lead to race conditions. 

#### Points to cover

_This section lists important details for each point._

* Add execution policies as an additonal argument to the algorithm  
* The C++ 17 standard is required
* Mention `std::atomic` or `std::mutex` to avoid race conditions

### Main: 

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

* Nvidia supports to run `std::execution::par` on Nvidia GPUs. However, that is not yet in the C++ standard and will only work with Nvidia's HPC compiler.
* Currently, parallel algorithms are implemented using Intel's TBB library in GCC. You can set the number of used cores using `tbb::global_control(tbb::global_control::max_allowed_parallelism, nthreads);` provided by the header `#include "tbb/tbb.h"`.

