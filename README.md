README
======

This repository contains the source for the document:

  - Guidelines for Teaching C++

When the repository is tagged, this document is automatically built
and made available via GitHub Pages at:

  - https://cplusplus.github.io/SG20/latest
  - https://mdadams.github.io/sg20_guidelines_for_teaching_cpp/latest
  - https://mdadams.github.io/SG20/latest

The following software is needed to build the document:

  - pandoc
  - aspell
  - make
  - various basic POSIX utilities, including (amongst others):
      - awk
      - sed

To build, simply type:

  1. make clean
  2. make all
  3. make install

(Strictly speaking, step 2 can be skipped, since the install target
has a dependency on the all target.)

The above commands will build the document in several formats:

  - HTML format as a single HTML document:
    install/html/index.html
  - EPUB format:
    guidelines.epub
  - HTML format split across multiple HTML documents:
    install/html_split/index.html

The build process performs spell checking.
