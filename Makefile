SUBDIRS = \
  sources \

.PHONY: all clean install
all clean install:
	for subdir in $(SUBDIRS); do \
		( cd $$subdir && make -$(MAKEFLAGS) $@ ) || exit 1; \
	done
