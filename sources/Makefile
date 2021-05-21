#TOP_DIR = $(realpath ..)
TOP_DIR = ..

# Specify the document version.
# This can be overridden when invoked from the automated build process.
DOC_VERSION = X.Y.Z

# Specify whether a spelling error is an error (as opposed to a warning).
# This can be overridden when invoked from the automated build process.
# Please resist the temptation to set this variable to zero. ;-)
# DOC_SPELLCHECK_MUST_PASS = 0
DOC_SPELLCHECK_MUST_PASS = 1

# This can be overridden when invoked from the automated build process.
INSTALL_DIR = $(TOP_DIR)/install

# All of the Markdown source files (that are not generated during build).
SOURCES = \
  modules/compile-time-programming/requires-expressions.md \
  modules/functions/defaulted-parameters.md \
  modules/functions/user-defined-literals.md \
  modules/object-model/copy_elision.md \
  modules/object-model/copy-semantics.md \
  course_examples.md \
  disclaimer.md \
  glossary.md \
  contributing.md \
  introduction.md \
  main.md \
  obtaining_document.md \
  references.md \

# The Markdown files that are generated during the build process.
GENERATED_MARKDOWN = \
  knowledge_areas_summary.md \
  main.gen.md \
  contributors.md \

################################################################################
# Define primary targets.
################################################################################

# The all target builds the document in a minimal set of formats and
# performs a spell check.
.PHONY: all
all: documents spellcheck

# The documents target builds the document in a minimal set of formats.
.PHONY: documents
documents: guidelines.html guidelines_html guidelines.epub

# The world target builds the document in a few extra formats.
.PHONY: world
world: documents guidelines.pdf

# The spellcheck format performs a spell check on the document.
.PHONY: spellcheck
spellcheck: spellcheck_result.txt

# The clean target removes all files generated during the build process.
.PHONY: clean
clean:
	rm -f $(GENERATED_MARKDOWN)
	rm -f guidelines.html guidelines.pdf guidelines.epub guidelines.tex
	rm -rf guidelines.texi
	rm -rf guidelines_html
	rm -f spellcheck_result.txt
	rm -f spellcheck_expected_sorted.txt
	rm -f missfont.log

# The install target installs the build document (in various formats)
# in the directory $(INSTALL_DIR).
.PHONY: install
install: all
	if [ ! -d $(INSTALL_DIR) ]; then mkdir -p $(INSTALL_DIR) || exit 1; fi
	for dir in html html/images; do \
		if [ ! -d "$(INSTALL_DIR)/$$dir" ]; then \
			mkdir -p "$(INSTALL_DIR)/$$dir" || exit 1; \
		fi; \
	done
	cp -f images/cpp_logo.png $(INSTALL_DIR)/html/images
	cp -f guidelines.html $(INSTALL_DIR)/html/index.html
	cp -r -f guidelines_html $(INSTALL_DIR)/html_split
	cp -f guidelines.epub $(INSTALL_DIR)

################################################################################
# Some additional configuration.
################################################################################

MD_PREPROCESSOR = $(TOP_DIR)/tools/build/preprocessor
MAKE_MARKDOWN = $(TOP_DIR)/tools/build/make_markdown
SPELLCHECK_DIR = $(TOP_DIR)/config/spellcheck

################################################################################
# Preprocessing setup.
################################################################################

main.gen.md: $(SOURCES) contributors.md main.md
	$(MD_PREPROCESSOR) -v $(DOC_VERSION) < main.md > main.gen.md

knowledge_areas_summary.md: $(SOURCES) knowledge_areas.dat
	$(MAKE_MARKDOWN) < knowledge_areas.dat > knowledge_areas_summary.md

contributors.md:
	git log --all --pretty="%an" | sort | uniq > contributors.md

################################################################################
# Establish Pandoc settings.
################################################################################

PANDOC_OPTIONS += --toc --toc-depth 3
PANDOC_OPTIONS += --number-sections
PANDOC_OPTIONS += --standalone
PANDOC_OPTIONS += --pdf-engine=xelatex
#PANDOC_OPTIONS += --lua-filter=tools/pandoc_filters/meta_vars.lua
#PANDOC_OPTIONS += --metadata date="`date +%Y-%m-%d`"
PANDOC_OPTIONS += --metadata version=$(DOC_VERSION)

INPUT_FORMAT = markdown+header_attributes+multiline_tables

EPUB_CSS_FILE = css/default-pandoc.css

#HTML_TEMPLATE = templates/bootstrap_menu.html
HTML_TEMPLATE = $(TOP_DIR)/config/pandoc_templates/uikit.html

################################################################################
# Rules for generating the document in various formats.
################################################################################

guidelines.html: $(GENERATED_MARKDOWN)
	pandoc $(PANDOC_OPTIONS) --template $(HTML_TEMPLATE) --from $(INPUT_FORMAT) -o $@ main.gen.md

guidelines.epub: $(GENERATED_MARKDOWN)
	pandoc $(PANDOC_OPTIONS) -c $(EPUB_CSS_FILE) --from $(INPUT_FORMAT) -o $@ main.gen.md

guidelines.pdf: $(GENERATED_MARKDOWN)
	pandoc $(PANDOC_OPTIONS) --from $(INPUT_FORMAT) -o $@ main.gen.md

guidelines.texi: $(GENERATED_MARKDOWN)
	pandoc $(PANDOC_OPTIONS) --from $(INPUT_FORMAT) -o $@ main.gen.md

guidelines.docbook: $(GENERATED_MARKDOWN)
	pandoc $(PANDOC_OPTIONS) --from $(INPUT_FORMAT) -o $@ main.gen.md

guidelines_html: guidelines.texi
	makeinfo --no-validate --force --html -o guidelines_html guidelines.texi

guidelines.tex:
	pandoc $(PANDOC_OPTIONS) --from $(INPUT_FORMAT) --to latex -o $@ main.gen.md

################################################################################
# Rule for spellchecking.
################################################################################

spellcheck_result.txt: guidelines.html
	rm -f $@
	rm -f spellcheck_expected_sorted.txt
	sort $(SPELLCHECK_DIR)/ignored_words.txt | \
	  uniq > spellcheck_expected_sorted.txt
	PATH="$(TOP_DIR)/tools/build:$$PATH" pandoc --from $(INPUT_FORMAT) \
	  --lua-filter $(TOP_DIR)/tools/pandoc_filters/spellcheck.lua \
	  main.gen.md | sort | uniq > $@
	@status=0; \
	  diff -q spellcheck_expected_sorted.txt $@ || \
	  status=1; \
	  if [ $$status -ne 0 ]; then \
	      echo "SPELLING ERRORS DETECTED:"; \
	      diff -u spellcheck_expected_sorted.txt $@ | \
		  grep '^[+-]'; \
	      if [ $(DOC_SPELLCHECK_MUST_PASS) -ne 0 ]; then \
	          echo "ERROR: spelling errors detected"; \
	          exit 1; \
	      else \
	          echo "WARNING: spelling errors detected"; \
	      fi; \
	  fi
