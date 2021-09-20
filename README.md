Guidelines for Teaching C++
===========================

This repository contains the source for the document:

  - Guidelines for Teaching C++

When the repository is tagged, this document is automatically built
and made available via GitHub Pages at:

  - <https://cplusplus.github.io/SG20/latest> (soon)
  - <https://mdadams.github.io/sg20_guidelines_for_teaching_cpp/latest>
    (currently)
  - <https://mdadams.github.io/SG20/latest> (currently)

# Prerequisites for Building the Document

The following software is needed to build the document:

  - pandoc
  - aspell
  - various basic POSIX utilities, including (amongst others):
      - make
      - awk
      - sed

If one would like to build the document in PDF format, the
following software is also required:

  - LaTex

# Building the Document

To build the document, simply type:

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

A make target called world is also defined.  Building this target (i.e.,
"make world") will generate the document in additional formats, including
PDF format, but requires that LaTeX be installed.

The build process performs spell checking.
The build will fail if any spelling errors are detected.

# Spell Checking

Words that are flagged as having spelling errors can be classified
into two categories:

  1. valid English words (such as technical terms) that are not in
     the spell checker's dictionary
  2. words that are not really "proper" English words but are also not
     really errors either (e.g., people's names)

Words in category 1 should be added to the file
config/spellcheck/wordlist.
Words in category 2 should be added to the file
config/spellcheck/ignored_words.txt

# Repository Organization

The files in this repository are organized into directories as follows:

- config:
  This directory contains configuration files that control various
  aspects of how the guidelines document is built.
    - pandoc_templates:
      This directory contains document templates used by pandoc during
      the document build process.
    - spellcheck:
      The directory contains lists of additional words and ignorable errors
      for spell checking.
- sources:
  This directory hierarchy contains the source files for the document.
    - css:
      This directory contains CSS files used by the document when built
      in HTML format.
    - images:
      This directory contains images used in the document.
    - modules:
      The directory hierarchy contains the information for individual modules
      and topics.  There is one directory per module and one file per topic.
- tools:
  The directory hierarchy contains various scripts and other tools used for
  building and deploying the document to GitHub pages site.
    - build:
      This directory contains scripts used for building and deploying the
      document.
    - old:
      This directory hierachy needs to be reorganized.  This directory
      should probably be renamed and its contents possibly reorganized
      or relocated elsewhere.
        - tools
            - tests
                - TEST_INPUTS
    - pandoc_filters:
      This directory contains various filters needed for pandoc.  These
      filters do things such as allow markdown-aware spell checking.
