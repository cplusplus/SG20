# Module name: Requires Expressions

## Overview

<table>
  <thead>
    <th>Level</th>
    <th>Objectives</th>
  </thead>
  <tr>
    <td>Foundational</td>
    <td>Define and use requires-expressions to check satisfaction of expressions by given parameters</td>
  </tr>
  <tr>
    <td>Advanced</td>
    <td>Define and use requires-expressions to check properties of expressions</td>
  </tr>
  <tr>
    <td>Advanced</td>
    <td></td>
  </tr>
</table>

## Motivation

Requires-expressions allow a developer to perform compile-time evaluation 
on the validity of other expressions. These are fundamental to the ability 
to write concepts. [[Compile-time programming: concepts]][1]

## Topic introduction

Requires-expressions are compile-time predicates which evaluate to true 
when their specified set of expressions are all valid for a given set of 
inputs.

## Foundational: Writing requires-expressions

### Background/Required Knowledge

A student is able to:

* Write and use a function template [[Compile-time programming: function templates]][2]
* Differentiate between expressions and statements

It is helpful if:

* A student is aware of the constraints imposed by their template definitions

### Student outcomes

A student should be able to:

1. Write a simple-requirement to assert the validity of an expression
2. Write a type-requirement to check the existence of a type by its identifier
3. Write a compound-requirement to test the resulting type of an expression
4. Write a nested-requirement to test the constexpr value of an operation, as opposed to just the syntactic validity
5. Use a requires-expression within a concept, requires-clause, or `if constexpr` condition

### Caveats

To require expressions which evaluate to a boolean value, such as 
`sizeof(t) == 4`, to only be satisfied when the result of the expression is 
`true`, you must use a nested-requirement, such as 
`requires sizeof(t) == 4;`. Omitting the `requires` results in a 
simple-requirement, which is satisfied based purely on syntact validity, 
not on the result of the operation.

### Points to cover

* All requires-expression requirements terminate with a semicolon.
* simple-requirements are used to check that an expression is well-formed.
* nested-requirements are introduced with `requires` and primarily used to check the result of an expression computable by the compiler, including concepts or other requires-expressions.
* type-requirements are introduced with `typename` and used to verify the existence of a type with a particular identifier.
* compound-requirements are enclosed in braces and can be used to check the resulting type of an expression.
* Checks are performed by the compiler, not at run time.
* If covering usage of requires-expression with requires-clause, [[Compile-time programming: requires clause]][3] demonstrate `requires requires` and show how to ever avoid writing it by using a concept. [[Compile-time programming: concepts]][1]

## Advanced: Advanced requirements

### Background/required knowledge

* All of the above.
* Knowledge of `noexcept`

A student is able to:

* Write a concept [[Compile-time programming: concepts]][1]

### Student outcomes

A student should be able to:

1. Write compound-requirements which test the `noexcept`ness of an expression.
2. Use a concept as the target of a compound-requirement.

### Caveats

### Points to cover

* Compound-requirements allow the optional ability to test whether an expression is marked as `noexcept`, by using the `noexcept` keyword.
  ```
struct S
{
	void foo() noexcept {}
	void bar() {}
};

static_assert(requires(S s) { { s.foo() } noexcept; } ); // Succeeds. s.foo() is noexcept
static_assert(requires(S s) { { s.bar() } noexcept; } ); // Fails. s.bar() is not noexcept
  ```
* If the return-type-requirement of a compound-requirement is a concept, that concept is given the resulting type as the first parameter, followed by the specified parameters in the compound-requirement. `{ ++x } -> C<int>` would substitute `C<decltype((++x)), int>` and check that concept C is satisfied for those parameters.

## Further studies

[1]: ../compile-time-programming/concepts.md
[2]: ../compile-time-programming/function-templates.md
[3]: ../compile-time-programming/requires-clause.md


