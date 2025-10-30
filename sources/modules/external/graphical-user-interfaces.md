## External libraries: Desktop Graphical User Interfaces {#extern-gui}

_Skeleton descriptions are typeset in italic text,_
_so please don't remove these descriptions when editing the topic._

### Overview

_Provides a short natural language abstract of the module’s contents._
_Specifies the different levels of teaching._

------------------------------------------------------------------------
Level             Objective
----------------- ------------------------------------------------------
Foundational:      Basic use of desktop graphical user interfaces

Main:              Different forms of IO and accessibility

Advanced:          Internationalization and customization

------------------------------------------------------------------------

### Motivation

_Why is this important?_
_Why do we want to learn/teach this topic?_

For some applications a graphical user interface is beneficial. However, graphical user interfaces are not part of the C++ standard and external libraries are needed. We provide generic teaching goals and do not focus on a specific external library. Some mentionable platform-independent libraries are [Qt](https://www.qt.io/) and [wxWidgets](https://www.wxwidgets.org/) for interface development or [Cairo](https://www.cairographics.org/) and [OpenGL](https://www.opengl.org/) for graphics.

### Topic introduction

_Very brief introduction to the topic._

### Foundational: Basic use of desktop graphical user interfaces

#### Background/Required Knowledge

A student: 

1. should have a foundational knowledge of [linkage](../compilation-model/linkage.md)
2. should have a foundational knowledge of [header files](../compilation-model/headers.md)
3. should have a foundational knowledge of [build systems](../compilation-model/buildsystems.md)

#### Student outcomes

_A list of things "a student should be able to" after the curriculum._
_The next word should be an action word and testable in an exam._
_Max 5 items._

A student should be able to:

1. write an application with one window
2. add simple widgets like text boxes and buttons to the window
3. respond to events of buttons or other widgets
4. explain the mechanics of event-driven programming

#### Points to cover

* use basic API functions
* layout of the window
* handle events by callbacks

#### Caveats

_This section mentions subtle points to understand, like anything resulting in
implementation-defined, unspecified, or undefined behavior._

* programming user interfaces in C++ and in general require significant boiler plate code  
* API calls are specific to one library and might not be transferable to other libraries
* some libraries are written in C or other languages

### Main: Different forms of I/O and accessibility

#### Background/Required Knowledge

* all of the above

#### Student outcomes

A student should be able to:

1. add more advanced elements, like tables or images
2. handle multiple windows
3. show error and warning popups
4. use different forms of input and output (I/O), such as keyboard, mouse, or touch pad
5. explain basics of fonts and accessibility

#### Caveats

* programming user interfaces is rather complex and might not be applicable for most students

#### Points to cover

* more advanced API calls and design patterns
* modal vs non-modal dialogs

### Advanced: Technicalities and tools

_These are important topics that are not expected to be covered but provide
guidance where one can continue to investigate this topic in more depth._

* internationalization
* font designers 
* hardware acceleration
* custom widget generation
* event-driven programming using non-UI elements, such as timers or sockets
* multi-threaded user interface development

