## Meta-error handling: `static_assert` {#static-assert}

_Skeleton descriptions are typeset in italic text,_
_so please don't remove these descriptions when editing the topic._

### Overview

_Provides a short natural language abstract of the module’s contents._
_Specifies the different levels of teaching._

<table>
  <thead>
    <th>Level</th>
    <th>Objectives</th>
  </thead>
  <tr>
    <td>Foundational</td>
    <td>Calling <code>static_assert</code> with a constant expression</td>
  </tr>
  <tr>
    <td>Main</td>
    <td>Using <code>static_assert</code> to detect contract violations and improve error messages</td>
  </tr>
  <tr>
    <td>Advanced</td>
    <td></td>
  </tr>
</table>

### Motivation

_Why is this important?_
_Why do we want to learn/teach this topic?_

`static_assert` allows the developer to enforce that conditions which can 
be checked during compilation will force build errors when violated. 
Additionally, they are the best mechanism by which a developer can pass 
useful information to other developers regarding what violation occurred or 
what must be done, instead.

### Topic introduction

_Very brief introduction to the topic._

`static_assert` is a compile-time evaluated function that asserts the 
truth of a supplied predicate, issuing an optional user-supplied error 
message if the predicate is `false`.

### Foundational: Calling `static_assert` with a constant expression {#static-assert-basic}

#### Background/Required Knowledge

A student:

* Should be able to explain the difference between code evaluated at compile-time and run-time
* Should be able to cite some examples of compile-time known information, such as `sizeof(T)`

#### Student outcomes

_A list of things "a student should be able to" after the curriculum._
_The next word should be an action word and testable in an exam._
_Max 5 items._

A student should be able to:

1. Assert the expected size of a structure using `static_assert`

#### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._

#### Points to cover

_This section lists important details for each point._

* X
* In addition to what is wrong, a good error message will inform the user of how to correct it

### Main: Contracts and `static_assert` {#static-assert-intermediate}

#### Background/Required Knowledge

* All of the above.
* General understanding of compile-time requirements

#### Student outcomes

_A list of things "a student should be able to" after the curriculum._
_The next word should be an action word and testable in an exam._
_Max 5 items._

A student should be able to:

1. Utilize `static_assert` to verify preconditions of a meta-function
2. Utilize `static_assert` to verify the results of meta-functions for known values

#### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._

#### Points to cover

_This section lists important details for each point._

* When writing a meta-function, use `static_assert` to test the results
* Write `static_assert` calls at the scope of the code they are guarding
```cpp
template<typename T>
struct container {
	std::map<int, T> vals;

	// Test location #1
	static_assert(
		std::is_default_constructible_v<T>,
		"container type T must be default constructible");i

	void add(int key, T const& t) {
		// Test location #2
		static_assert(
			std::is_default_constructible_v<T>,
			"container type T must be default constructible");
		// std::map::operator[] requires default constructible type for 
		// the value. This will cause a build failure deep in the 
		// implementation of std::map, when T is not default constructible
		vals[key] = t;
	}
};

struct NoDefCtor {
	NoDefCtor() = delete;
	NoDefCtor(double d) {}
};

container<NoDefCtor> c; // If Test #1 was omitted, this would succeed
// This is ill-formed. Test #2 would catch this and provide a better 
// error message for the user
c.add(42, NoDefCtor(1.0)); 
```

### Advanced {#static-assert-advanced}

_These are important topics that are not expected to be covered but provide
guidance where one can continue to investigate this topic in more depth._
