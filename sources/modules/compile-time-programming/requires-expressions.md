## Module name: Requires Expressions {#req-expr}

_Skeleton descriptions are typeset in italic text,_
_so please don't remove these descriptions when editing the topic._

### Overview

_Provides a short natural language abstract of the module’s contents._
_Specifies the different levels of teaching._

-------------------------------------------------------------------------
Level              Objectives
------------------ ------------------------------------------------------
Foundational       Define and use requires-expressions to check
                   satisfaction of expressions by given parameters

Main               Define and use requires-expressions to check
                   properties of expressions

Advanced           ---
-------------------------------------------------------------------------

### Motivation

_Why is this important?_
_Why do we want to learn/teach this topic?_

Requires-expressions allow a developer to perform compile-time evaluation 
on the validity of other expressions. These are fundamental to the ability 
to write concepts. [[Compile-time programming: concepts]][1]

## Topic introduction

_Very brief introduction to the topic._

Requires-expressions are compile-time predicates which evaluate to true 
when their specified set of expressions are all valid for a given set of 
inputs.

### Foundational: Writing requires-expressions {#req-expr-basic}

#### Background/Required Knowledge

A student is able to:

* Write and use a function template [[Compile-time programming: function templates]][2]
* Differentiate between expressions and statements

It is helpful if:

* The student is aware that attempting to specialize the template with types or values which do not match otherwise unstated assumptions will cause errors within the template.

#### Student outcomes

_A list of things "a student should be able to" after the curriculum._
_The next word should be an action word and testable in an exam._
_Max 5 items._

A student should be able to:

1. Write a simple-requirement to assert the validity of an expression
2. Write a type-requirement to check the existence of a type by its identifier
3. Write a compound-requirement to test the resulting type of an expression
4. Write a nested-requirement to test the constexpr value of an operation, as opposed to just the syntactic validity
5. Use a requires-expression within a concept, requires-clause, or `if constexpr` condition

#### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._

To require that expressions, which evaluate to a boolean value 
like `sizeof(t) == 4`, evaluate to `true` a nested-requirement is needed 
(e.g., `requires sizeof(t) == 4;`). Omitting the `requires` results in a 
simple-requirement, which is satisfied based purely on syntactic validity, 
not on the result of the operation.

#### Points to cover

_This section lists important details for each point._

* All requires-expression requirements terminate with a semicolon.
* simple-requirements are used to check that an expression is well-formed.
* nested-requirements are introduced with `requires` and primarily used to check the result of an expression computable by the compiler, including concepts or other requires-expressions.
* type-requirements are introduced with `typename` and used to verify the existence of a type with a particular identifier.
* compound-requirements are enclosed in braces and can be used to check the resulting type of an expression.
* Checks are performed by the compiler, not at run time.
* If covering usage of requires-expression with requires-clause, [[Compile-time programming: requires clause]][3] demonstrate `requires requires` and show how to ever avoid writing it by using a concept. [[Compile-time programming: concepts]][1]

### Main: Advanced requirements {#req-expr-intermediate}

#### Background/required knowledge

* All of the above.
* Knowledge of `noexcept`

A student is able to:

* Write a concept [[Compile-time programming: concepts]][1]

#### Student outcomes

A student should be able to:

1. Write compound-requirements which test the `noexcept`ness of an expression.
2. Use a concept as the target of a compound-requirement.

#### Caveats

#### Points to cover

* Compound-requirements allow the optional ability to test whether an expression is marked as `noexcept`, by using a trailing `noexcept` keyword.

```cpp
struct S
{
	void foo() noexcept {}
	void bar() {}
};

static_assert(requires(S s) { { s.foo() } noexcept; } ); // Succeeds. s.foo() is noexcept
static_assert(requires(S s) { { s.bar() } noexcept; } ); // Fails. s.bar() is not noexcept
```
  
* If the return-type-requirement of a compound-requirement is a concept, that concept is given the resulting type as the first parameter, followed by the specified parameters in the compound-requirement. `{ ++x } -> C<int>` would substitute `C<decltype((++x)), int>` and check that concept C is satisfied for those parameters.

### Advanced {#req-expr-advanced}

[1]: ../compile-time-programming/concepts.md
[2]: ../compile-time-programming/function-templates.md
[3]: ../compile-time-programming/requires-clause.md
