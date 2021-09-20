SUBDIRS = \
  sources \

.PHONY: all world clean install
all world clean install:
	for subdir in $(SUBDIRS); do \
		( cd $$subdir && make -$(MAKEFLAGS) $@ ) || exit 1; \
	done
