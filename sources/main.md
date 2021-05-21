---
title_logo: images/cpp_logo.png
title: Guidelines for Teaching C++
author: SG20 (ISO C++ Study Group on Education)
geometry: margin=1in
output: pdf_document
---

__INCLUDE__(obtaining_document.md)

__INCLUDE__(disclaimer.md)

__INCLUDE__(introduction.md)

# Summary of Modules and Topics

In the sections that follow, the various modules and topics
are presented.
There is one section per module.
For each module, a table listing the various topics in that module
is provided.
The ID for a topic is linked to the detailed coverage of that
topic that comes later in the document.
If a topic has any learning outcomes at a given proficiency level, this is
indicated by a checkmark ("✔️").
If a topic has no learning outcomes
(simply because there
are not any, not because the information is missing),
this is indicated by an em dash ("—").
In the case that the information for a topic is completely
missing, a question mark ("?") symbol is used.

[**NOTE**: These topics are taken mostly from the SG20 GitHub repository.
They are not intended to be complete in any sense.
In fact, by gathering together all topics in one place where they are
easily viewed, it is hoped that missing and unbalanced items will be more
obvious.]

__INCLUDE__(knowledge_areas_summary.md)

# Detailed Information for Modules and Topics

[//]: # ( ********** START OF DETAILED TOPIC DOCUMENTS ********** )

__INCLUDE__(modules/object-model/copy-semantics.md)

__INCLUDE__(modules/functions/user-defined-literals.md)

__INCLUDE__(modules/functions/defaulted-parameters.md)

__INCLUDE__(modules/compile-time-programming/requires-expressions.md)

__INCLUDE__(modules/object-model/copy_elision.md)

__INCLUDE__(modules/meta-error-handling/static_assert.md)

[//]: # ( ********** END OF DETAILED TOPIC DOCUMENTS ********** )

__INCLUDE__(course_examples.md)

# License {#license}

**[NOTE: This license is copied verbatim from the C++ Core Guidelines.]**
<pre>
__INCLUDE__(../LICENSE.txt)
</pre>

# Contributors

For a complete list of contributors, please refer to the repository
containing this document on [GitHub](https://github.com/cplusplus/SG20).

__INCLUDE__(contributing.md)

__INCLUDE__(glossary.md)

__INCLUDE__(references.md)
