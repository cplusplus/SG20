README
======

This repository contains the source for the document:

  - Guidelines for Teaching C++

When the repository is tagged, this document is automatically built
and made available via GitHub Pages at:

  - https://mdadams.github.io/sg20_guidelines_for_teaching_cpp/latest

The following software is needed to build the document:

  - pandoc
  - aspell
  - make
  - various basic POSIX utilities, including (amongst others):
      - awk
      - sed

To build, simply type:

  - make clean
  - make all

This will build the document in multiple formats.
The main two formats are:

  - HTML format as a single HTML document: guidelines.html
  - EPUB format: guidelines.epub

The build process performs spell checking.
