# Module name: Requires Expressions

## Overview

<table>
  <thead>
    <th>Level</th>
    <th>Objectives</th>
  </thead>
  <tr>
    <td>Foundational knowledge</td>
    <td>Define and use requires-expressions to check satisfaction of expressions by given parameters</td>
  </tr>
  <tr>
    <td>Advanced</td>
    <td>Define and use requires-expressions to check properties of expressions</td>
  </tr>
  <tr>
    <td>Further studies</td>
    <td></td>
  </tr>
</table>

## Motivation

Requires-expressions allow a developer to perform compile-time evaluation on the validity of other expressions. These are fundamental to the ability to write concepts.

## Topic introduction

Requires-expressions are compile-time predicates which evaluate to true when their specified set of expressions are all valid for a given set of inputs.

## Foundational knowledge: Writing requires-expressions

### Background/Required Knowledge

A student is able to:

* Write and use a function template [1]
* Differentiate between expressions and statements


### Student outcomes

A student should be able to:

1. Write a simple-requirement to assert the validity of an expression
2. Write a type-requirement to check the existence of a type by its identifier
3. Write a compound-requirement to test the resulting type of an expression
4. Write a nested-requirement to test the constexpr value of an operation, as opposed to just the semantic validity
5. Use a requires-expression within a concept, requires-clause, or `if constexpr` condition

### Caveats

To require expressions which evaluate to a boolean value, such as `sizeof(t) == 4`, to only be satisfied when the result of the expression is `true`, you must use a nested-requirement, such as `requires sizeof(t) == 4;`. Omitting the `requires` results in a simple-requirement, which is satisfied based purely on semantic validity, not on the result of the operation.

### Points to cover

* All requires-expression requirements terminate with a semi-colon.
* simple-requirements are used to check the semantics of an expression.
* nested-requirements are introduced with `requires` and primarily used to check the result of an expression computable by the compiler, including concepts or other requires-expressions.
* type-requirements are introduced with `typename` and used to verify the existence of a type with a particular identifier.
* compound-requirements are enclosed in braces and can be used to check the resulting type of an expression.
* Parameters should be specified without cv-qualifiers, as though passed by-value.
* Checks are performed by the compiler, not at run time.

## Advanced: Advanced requirements

### Background/required knowledge

* All of the above.
* Knowledge of `noexcept`

### Student outcomes

A student should be able to:

1. Write compound-requirements which test the `noexcept`ness of an expression.
2. Use a concept as the target of a compound-requirement.

### Caveats

### Points to cover

* Compound-requirements allow the optional ability to test whether an expression is marked as `noexcept`, by using the `noexcept` keyword.
* If the return-type-requirement of a compound-requirement is a concept, that concept the concept is given the resulting type as the first parameter, followed by the specified parameters in the compound-requirement. `{ ++x } -> C<int>` would substitute `C<decltype((++x)), int>` and check that concept C is satisfied for those parameters.

## Further studies

[1]: ../compile-time-programming/function-templates.md





