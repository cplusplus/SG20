# Specify the document version.
# This can be overridden when invoked from the automated build process.
DOC_VERSION = X.Y.Z

# Specify whether a spelling error is an error (as opposed to a warning).
# This can be overridden when invoked from the automated build process.
DOC_SPELLCHECK_MUST_PASS = 1

# All of the Markdown source files (that are not generated during build).
SOURCES = \
  doc/areas/compile-time-programming/requires-expressions.md \
  doc/areas/functions/defaulted-parameters.md \
  doc/areas/functions/user-defined-literals.md \
  doc/areas/object-model/copy_elision.md \
  doc/areas/object-model/copy-semantics.md \
  doc/course_examples.md \
  doc/disclaimer.md \
  doc/glossary.md \
  doc/contributing.md \
  doc/introduction.md \
  doc/main.md \
  doc/obtaining_document.md \
  doc/references.md \

# The Markdown files that are generated during the build process.
GENERATED_MARKDOWN = \
  knowledge_areas_summary.md \
  main.gen.md \

################################################################################
# Define primary targets.
################################################################################

.PHONY: all
all: documents spellcheck

.PHONY: documents
documents: guidelines.html guidelines_html guidelines.epub

.PHONY: world
world: documents guidelines.pdf

.PHONY: spellcheck
spellcheck: spellcheck_result.txt

.PHONY: clean
clean:
	rm -f guidelines.html guidelines.pdf guidelines.epub guidelines.tex
	rm -rf guidelines.texi
	rm -f main.gen.md knowledge_areas_summary.md
	rm -f pandoc.css
	rm -f missfont.log
	rm -rf guidelines_html
	rm -f spellcheck_result.txt
	rm -f spellcheck/spellcheck_expected_sorted.txt

.PHONY: install
install:
	if [ ! -d $(INSTALL_DIR) ]; then mkdir -p $(INSTALL_DIR) || exit 1; fi
	cp guidelines.html $(INSTALL_DIR)/index.html
	#cp pandoc.css $(INSTALL_DIR)/pandoc.css
	cp -r guidelines_html $(INSTALL_DIR)/split
	cp guidelines.epub $(INSTALL_DIR)

################################################################################
# Preprocessing setup.
################################################################################

knowledge_areas_summary.md: $(SOURCES) doc/knowledge_areas.dat
	bin/make_markdown < doc/knowledge_areas.dat > knowledge_areas_summary.md

main.gen.md: $(SOURCES) doc/main.md
	bin/preprocessor -v $(DOC_VERSION) < doc/main.md > main.gen.md

################################################################################
# Establish Pandoc settings.
################################################################################

PANDOC_OPTIONS += --toc --toc-depth 3
PANDOC_OPTIONS += --number-sections
PANDOC_OPTIONS += --standalone
PANDOC_OPTIONS += --pdf-engine=xelatex
#PANDOC_OPTIONS += --metadata date="`date +%Y-%m-%d`"
PANDOC_OPTIONS += --variable version=$(DOC_VERSION)
#PANDOC_OPTIONS += --variable mainfont=DejaVuSerif --variable sansfont=DejaVuSans

INPUT_FORMAT = markdown+header_attributes+multiline_tables

#CSS_FILE = css/default-pandoc.css
#CSS_FILE = css/github-pandoc.css
#CSS_FILE = css/pandoc.css
#CSS_FILE = css/epub.css

EPUB_CSS_FILE = css/default-pandoc.css

#HTML_TEMPLATE = templates/bootstrap_menu.html
HTML_TEMPLATE = templates/uikit.html

################################################################################
# Rules for generating the document in various formats.
################################################################################

#pandoc.css:
#	[ -e pandoc.css ] || ln -s $(CSS_FILE) pandoc.css

guidelines.html: $(GENERATED_MARKDOWN)
	#pandoc $(PANDOC_OPTIONS) -c pandoc.css --from $(INPUT_FORMAT) -o $@ main.gen.md
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
	rm -f spellcheck/spellcheck_expected_sorted.txt
	sort spellcheck/spellcheck_expected.txt | uniq > spellcheck/spellcheck_expected_sorted.txt
	PATH="bin:$$PATH" pandoc --from $(INPUT_FORMAT) --lua-filter filters/spellcheck.lua main.gen.md | sort | uniq > $@
	@status=0; \
	  diff -q spellcheck/spellcheck_expected_sorted.txt $@ || status=1; \
	  if [ $$status -ne 0 ]; then \
	      echo "SPELLING ERRORS DETECTED:"; \
	      diff -u spellcheck/spellcheck_expected_sorted.txt $@ | grep '^[+-]'; \
	      if [ $(DOC_SPELLCHECK_MUST_PASS) -ne 0 ]; then \
	          echo "ERROR: spelling errors detected"; \
	          exit 1; \
	      else \
	          echo "WARNING: spelling errors detected"; \
	      fi; \
	  fi
