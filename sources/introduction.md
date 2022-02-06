# Context and Aim of This Guide

This document is intended to serve as a resource for instructors
to assist in the preparation of courses on C++ in a variety of
settings, including university, college, and industry environments.
The main objectives of this document are as follows:

  - to provide guidelines for content to be covered by courses of various
    difficulty levels on C++ (e.g., topics and learning outcomes)
  - to note some common misunderstandings and problematic points that may
    be encountered when teaching particular topics
  - to suggest resources useful for teaching C++
  - to present examples of curriculum for specific courses

This document does not itself provide a curriculum for a single specific
course, but is rather a set of guidelines that can be used to prepare
curricula for a wide variety of courses that differ in focus and level
of sophistication.
(This said, however, some links to other documents with examples of
curricula for specific courses may be included herein.)
This document only intends to target the teaching of the
most recently ratified version of the C++ standard.
(This said, however, since older versions of this document are also
available, these older versions may be of some use to those who need
guidance in older versions of the standard, at least versions that
do not predate C++20.)

# Use of This Document

**[NOTE: This document follows the same license model as the C++ Core
Guidelines.  The LICENSE document is taken verbatim from the C++ Core
Guidelines.]**
This document is made available under a MIT-style license.
In simple terms, this license permits copying, use, modification,
and creation of derivative works.
A copy of the license is included in the section [LICENSE](#license).

# Contributing to This Document

Contributions to this document are welcome.
If you would like to help with this project as a contributor,
please read the section [How to Contribute](#contributing).

# Organization of This Document

The various concepts (i.e., ideas) to potentially be covered 
are partitioned into modules.
A module is very broad in scope and consists of numerous topics.

For each module, topics related to the module are identified.
Then, for each topic, learning outcomes are specified.
In order to address a wide variety of courses on C++, each topic
is addressed at three proficiency levels.
These proficiency levels allow each topic to be covered at more than
one level of detail.
This allows target audiences with different background and learning
objectives to be accommodated.
The three proficiency levels are as follows:

  - foundational:  This level gives the learner the idea that a
    facility exists, what benefits it offers, and the basic ways of using it.

  - main:  This level shows mainstream uses and techniques.
    For abstraction and organizational mechanisms it also demonstrates how to
    build them.
    This level should also give the learner a basic (but not detailed)
    understanding of how a
    facility might be implemented so that the learner can have a first-order
    understanding of any costs involved.

  - advanced:  This level gives information suitable for an expert.
    For most topics there is an expert level of knowledge that most
    programmers rarely need and techniques that require detailed understanding
    of language rules or library implementation.

The remainder of this document is organized as follows.
The various topics are listed grouped by module.
In cases where a topic might be classified into more
than one module, the topic is listed under the module of most direct
relevance.
This is done in order to avoid duplication of content.
(In the case that a topic is equally relevant to multiple modules,
the decision of which to select is made by a proverbial coin toss.)
The order in which modules and topics are presented
is not meant to imply any order of coverage in a course.
The order in which items are listed is essentially arbitrary.
